"""Tests for the local web UI server (scripts/web_server.py).

Each test starts the real ThreadingHTTPServer on an ephemeral port, pointed at
a temporary AI_JOURNAL_DIR, and exercises the JSON API over HTTP. This proves
the web layer and the CLI share the same storage and reuse the same logic.
"""

import json
import os
import sys
import threading
import urllib.error
import urllib.request
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))


@pytest.fixture()
def server(tmp_path, monkeypatch):
    """Start the web server on a free port against a temp journal dir."""
    monkeypatch.setenv("AI_JOURNAL_DIR", str(tmp_path / "AI-Journal"))
    for key in ("OPENAI_API_KEY", "ANTHROPIC_API_KEY", "GEMINI_API_KEY"):
        monkeypatch.delenv(key, raising=False)

    import web_server  # imported after env is set

    httpd = web_server.make_server(port=0)
    port = httpd.server_address[1]
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{port}"
    finally:
        httpd.shutdown()
        httpd.server_close()


def get(base, path):
    with urllib.request.urlopen(base + path, timeout=5) as r:
        return r.status, json.loads(r.read().decode("utf-8"))


def post(base, path, payload, headers=None):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(base + path, data=data, method="POST")
    req.add_header("Content-Type", "application/json")
    for k, v in (headers or {}).items():
        req.add_header(k, v)
    try:
        with urllib.request.urlopen(req, timeout=5) as r:
            return r.status, json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        return exc.code, json.loads(exc.read().decode("utf-8"))


def test_health(server):
    status, body = get(server, "/api/health")
    assert status == 200
    assert body == {"ok": True}


def test_stats_empty(server):
    status, body = get(server, "/api/stats")
    assert status == 200
    assert body["total_entries"] == 0
    assert body["streak"] == 0
    assert len(body["heat"]) == 91
    assert body["badges"] == []


def test_create_entry_then_stats_and_list(server):
    status, body = post(server, "/api/entries", {"topic": "My first loop", "tags": "python, beginner", "body": "Used a for loop."})
    assert status == 200 and body["ok"] is True

    status, stats = get(server, "/api/stats")
    assert stats["total_entries"] == 1
    assert stats["streak"] == 1
    assert any(b["label"] == "First entry" for b in stats["badges"])

    status, listing = get(server, "/api/entries")
    assert listing["entries"][0]["topic"] == "My first loop"
    assert "python" in listing["entries"][0]["tags"]
    assert listing["entries"][0]["when"] == "Today"


def test_create_requires_topic(server):
    status, body = post(server, "/api/entries", {"topic": "   "})
    assert status == 400
    assert "topic" in body["error"].lower()


def test_append_to_latest(server):
    post(server, "/api/entries", {"topic": "Terminal basics"})
    status, body = post(server, "/api/append", {"target": "latest", "content": "Learned about cd."})
    assert status == 200 and body["ok"] is True
    assert body["topic"] == "Terminal basics"

    # The appended note should be findable by full-text search.
    status, res = get(server, "/api/search?q=cd")
    assert any("Terminal basics" == e["topic"] for e in res["entries"])


def test_append_requires_content(server):
    post(server, "/api/entries", {"topic": "Anything"})
    status, body = post(server, "/api/append", {"target": "latest", "content": ""})
    assert status == 400


def test_ask_known_question_saves_starter_guide(server):
    status, body = post(server, "/api/ask", {"question": "What is an API?"})
    assert status == 200
    assert body["matched"] is True
    assert "waiter" in body["answer"].lower()

    status, listing = get(server, "/api/entries")
    saved = listing["entries"][0]
    assert "starter-guide" in saved["tags"]


def test_ask_unknown_question_is_saved_pending(server):
    status, body = post(server, "/api/ask", {"question": "Explain monad transformers in Haskell"})
    assert status == 200
    assert body["matched"] is False
    assert body["answer"] is None

    status, listing = get(server, "/api/entries")
    assert "unanswered" in listing["entries"][0]["tags"]


def test_search_matches_topic(server):
    post(server, "/api/entries", {"topic": "Loops in Python", "body": "for loops are fun"})
    post(server, "/api/entries", {"topic": "CSS colors", "body": "hex codes"})
    status, res = get(server, "/api/search?q=python")
    assert status == 200
    topics = [e["topic"] for e in res["entries"]]
    assert "Loops in Python" in topics
    assert "CSS colors" not in topics


def test_cross_origin_post_blocked(server):
    status, body = post(server, "/api/ask", {"question": "What is git?"}, headers={"Origin": "http://evil.example.com"})
    assert status == 403


def test_static_index_served(server):
    with urllib.request.urlopen(server + "/", timeout=5) as r:
        assert r.status == 200
        html = r.read().decode("utf-8")
    assert "AI Coding Journal" in html


def test_profile_default_not_set(server):
    status, body = get(server, "/api/profile")
    assert status == 200
    assert body["name_set"] is False
    assert body["name"]  # falls back to a tidied OS name


def test_set_and_persist_profile(server):
    status, body = post(server, "/api/profile", {"name": "Ama"})
    assert status == 200 and body["ok"] is True
    assert body["name"] == "Ama" and body["name_set"] is True

    # Reflected in stats and re-readable.
    _, stats = get(server, "/api/stats")
    assert stats["name"] == "Ama" and stats["name_set"] is True
    assert stats["avatar"] == "A"
    _, prof = get(server, "/api/profile")
    assert prof["name"] == "Ama"


def test_clear_profile_falls_back(server):
    post(server, "/api/profile", {"name": "Ama"})
    status, body = post(server, "/api/profile", {"name": ""})
    assert status == 200
    assert body["name_set"] is False


def test_shares_storage_with_cli(server, tmp_path):
    """An entry made over the API must be visible to the CLI modules."""
    post(server, "/api/entries", {"topic": "Shared storage check"})
    import entry_saver

    index = entry_saver.load_index()
    assert any(e["topic"] == "Shared storage check" for e in index["entries"])
