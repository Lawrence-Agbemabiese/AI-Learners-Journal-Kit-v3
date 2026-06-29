"""Tests for the local web UI server (scripts/web_server.py).

Each test starts the real ThreadingHTTPServer on an ephemeral port, pointed at
a temporary AI_JOURNAL_DIR, and exercises the JSON API over HTTP. This proves
the web layer and the CLI share the same storage and reuse the same logic.
"""

import json
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
    monkeypatch.setenv("AI_JOURNAL_CONFIG", str(tmp_path / "ai-config.json"))
    for key in (
        "OPENAI_API_KEY",
        "ANTHROPIC_API_KEY",
        "GEMINI_API_KEY",
        "GROQ_API_KEY",
    ):
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
    status, body = post(
        server,
        "/api/entries",
        {
            "topic": "My first loop",
            "tags": "python, beginner",
            "body": "Used a for loop.",
        },
    )
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


def test_entry_detail_returns_full_body(server):
    post(
        server,
        "/api/entries",
        {
            "topic": "Photosynthesis",
            "body": "## AI Response\n\nPlants make food from light.",
        },
    )
    status, listing = get(server, "/api/entries")
    entry_id = listing["entries"][0]["id"]

    status, detail = get(server, "/api/entry?id=%d" % entry_id)
    assert status == 200
    assert detail["topic"] == "Photosynthesis"
    assert "Plants make food from light." in detail["body"]


def test_entry_detail_missing_id_is_400(server):
    with pytest.raises(urllib.error.HTTPError) as exc:
        get(server, "/api/entry")
    assert exc.value.code == 400


def test_entry_detail_unknown_id_is_404(server):
    with pytest.raises(urllib.error.HTTPError) as exc:
        get(server, "/api/entry?id=999999")
    assert exc.value.code == 404


def test_append_to_latest(server):
    post(server, "/api/entries", {"topic": "Terminal basics"})
    status, body = post(
        server, "/api/append", {"target": "latest", "content": "Learned about cd."}
    )
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
    status, body = post(
        server, "/api/ask", {"question": "Explain monad transformers in Haskell"}
    )
    assert status == 200
    assert body["matched"] is False
    assert body["answer"] is None

    status, listing = get(server, "/api/entries")
    assert "unanswered" in listing["entries"][0]["tags"]


def test_search_matches_topic(server):
    post(
        server,
        "/api/entries",
        {"topic": "Loops in Python", "body": "for loops are fun"},
    )
    post(server, "/api/entries", {"topic": "CSS colors", "body": "hex codes"})
    status, res = get(server, "/api/search?q=python")
    assert status == 200
    topics = [e["topic"] for e in res["entries"]]
    assert "Loops in Python" in topics
    assert "CSS colors" not in topics


def test_cross_origin_post_blocked(server):
    status, body = post(
        server,
        "/api/ask",
        {"question": "What is git?"},
        headers={"Origin": "http://evil.example.com"},
    )
    assert status == 403


def test_static_index_served(server):
    with urllib.request.urlopen(server + "/", timeout=5) as r:
        assert r.status == 200
        html = r.read().decode("utf-8")
    assert "AI Coding Journal" in html


def test_entry_preview_skips_placeholders(tmp_path, monkeypatch):
    monkeypatch.setenv("AI_JOURNAL_DIR", str(tmp_path))
    import web_server

    p = tmp_path / "e.md"
    # Empty template entry (legacy bracket placeholder) -> no preview leaked.
    p.write_text(
        "# Topic\n\n**Date:** x\n\n## Key Points\n\n- [Add your key insights here]\n\n"
        "## Reflection\n\n<!-- hint -->\n",
        encoding="utf-8",
    )
    assert web_server._entry_preview({"filename": "e.md"}) == ""

    # Real content -> shown without the leading bullet.
    p.write_text(
        "# Topic\n\n## Key Points\n\n- I learned about loops.\n", encoding="utf-8"
    )
    assert web_server._entry_preview({"filename": "e.md"}) == "I learned about loops."


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


def test_ai_status_default_disabled(server):
    status, body = get(server, "/api/ai/status")
    assert status == 200
    assert body["enabled"] is False
    ids = {p["id"] for p in body["providers"]}
    assert {"groq", "gemini", "openai", "anthropic"} <= ids


def test_live_answer_parsers(monkeypatch):
    """Each provider style parses its own response shape correctly."""
    import ai_integration as ai

    monkeypatch.setattr(
        ai,
        "_http_post_json",
        lambda *a, **k: {"choices": [{"message": {"content": "  oa  "}}]},
    )
    assert ai.live_answer("q", "groq", "k") == "oa"  # openai-compatible

    monkeypatch.setattr(
        ai,
        "_http_post_json",
        lambda *a, **k: {"candidates": [{"content": {"parts": [{"text": "gm"}]}}]},
    )
    assert ai.live_answer("q", "gemini", "k") == "gm"

    monkeypatch.setattr(
        ai,
        "_http_post_json",
        lambda *a, **k: {"content": [{"type": "text", "text": "claude!"}]},
    )
    assert ai.live_answer("q", "anthropic", "k") == "claude!"


def test_set_ai_key_then_ask_live(server, monkeypatch):
    import web_server

    monkeypatch.setattr(
        web_server, "live_answer", lambda *a, **k: "LIVE: a folder holds files."
    )
    status, body = post(
        server, "/api/ai/key", {"provider": "groq", "api_key": "test-key-1234"}
    )
    assert status == 200 and body["enabled"] is True
    assert body["label"] == "Groq" and body["masked"].endswith("1234")

    status, ask = post(server, "/api/ask", {"question": "what is a folder?"})
    assert ask["source"] == "Groq"
    assert ask["answer"].startswith("LIVE:")

    # Live answer saved to journal as ai-assisted.
    _, listing = get(server, "/api/entries")
    assert "ai-assisted" in listing["entries"][0]["tags"]


def test_set_ai_key_rejects_bad_key(server, monkeypatch):
    import web_server

    def boom(*a, **k):
        raise RuntimeError("That API key was rejected. Check it and try again.")

    monkeypatch.setattr(web_server, "live_answer", boom)
    status, body = post(server, "/api/ai/key", {"provider": "groq", "api_key": "bad"})
    assert status == 400
    assert "rejected" in body["error"].lower()
    # And AI stays disabled.
    _, st = get(server, "/api/ai/status")
    assert st["enabled"] is False


def test_ask_falls_back_to_offline_when_live_fails(server, monkeypatch):
    import ai_integration
    import web_server

    # Enable AI directly (skip validation), then make live calls fail.
    ai_integration.save_config({"provider": "groq", "api_keys": {"groq": "k"}})
    monkeypatch.setattr(
        web_server,
        "live_answer",
        lambda *a, **k: (_ for _ in ()).throw(RuntimeError("network down")),
    )

    status, body = post(server, "/api/ask", {"question": "what is an API?"})
    assert status == 200
    assert body["source"] == "Starter Guide"  # offline fallback kicked in
    assert "waiter" in body["answer"].lower()
    assert "network down" in body["message"]


def test_disconnect_ai(server, monkeypatch):
    import ai_integration

    ai_integration.save_config({"provider": "groq", "api_keys": {"groq": "k"}})
    _, st = get(server, "/api/ai/status")
    assert st["enabled"] is True
    status, body = post(server, "/api/ai/disconnect", {})
    assert status == 200 and body["enabled"] is False


def test_live_answer_includes_journal_context(monkeypatch):
    """When context is supplied, live_answer sends it in the user message."""
    import ai_integration as ai

    captured = {}

    def fake_post(url, body, headers, timeout):
        captured["body"] = body
        return {"choices": [{"message": {"content": "ok"}}]}

    monkeypatch.setattr(ai, "_http_post_json", fake_post)
    ai.live_answer(
        "How do while loops work?",
        "groq",
        "k",
        context="- For loops: a for loop repeats a fixed number of times.",
    )
    sent = captured["body"]["messages"][-1]["content"]
    assert "JOURNAL NOTES" in sent
    assert "for loop repeats" in sent
    assert "How do while loops work?" in sent

    # No context -> the user message is just the question.
    ai.live_answer("plain question", "groq", "k")
    assert captured["body"]["messages"][-1]["content"] == "plain question"


def test_ask_passes_journal_context_to_live_answer(server, monkeypatch):
    import ai_integration
    import web_server

    ai_integration.save_config({"provider": "groq", "api_keys": {"groq": "k"}})
    post(
        server,
        "/api/entries",
        {"topic": "For loops", "body": "A for loop repeats a fixed number of times."},
    )

    captured = {}
    monkeypatch.setattr(
        web_server,
        "live_answer",
        lambda *a, **k: captured.update(context=k.get("context", "")) or "LIVE answer",
    )

    status, body = post(
        server,
        "/api/ask",
        {"question": "How are while loops different from for loops?"},
    )
    assert status == 200
    assert "For loops" in captured["context"]
    assert body["used_journal"] is True


def test_ask_respects_use_journal_false(server, monkeypatch):
    import ai_integration
    import web_server

    ai_integration.save_config({"provider": "groq", "api_keys": {"groq": "k"}})
    post(
        server,
        "/api/entries",
        {"topic": "For loops", "body": "A for loop repeats a fixed number of times."},
    )

    captured = {}
    monkeypatch.setattr(
        web_server,
        "live_answer",
        lambda *a, **k: captured.update(context=k.get("context", "")) or "LIVE answer",
    )

    status, body = post(
        server, "/api/ask", {"question": "What is a variable?", "use_journal": False}
    )
    assert status == 200
    assert captured["context"] == ""
    assert body.get("used_journal") is False


def test_journal_context_empty_when_no_entries(server):
    import web_server

    assert web_server._journal_context("anything at all") == ""


def test_shares_storage_with_cli(server, tmp_path):
    """An entry made over the API must be visible to the CLI modules."""
    post(server, "/api/entries", {"topic": "Shared storage check"})
    import entry_saver

    index = entry_saver.load_index()
    assert any(e["topic"] == "Shared storage check" for e in index["entries"])
