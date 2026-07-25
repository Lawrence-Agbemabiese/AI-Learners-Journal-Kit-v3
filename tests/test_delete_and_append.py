"""Tests for v3.4.0: append-to-today/date targets and entry deletion."""

import json
import os
import subprocess
import sys
import threading
import urllib.error
import urllib.request
from datetime import datetime, timedelta
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
CLI = SCRIPTS / "journal_cli.py"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))


def run_cli(tmp_path, *args, user_input=None, check=True):
    env = os.environ.copy()
    env.update(
        {
            "AI_JOURNAL_DIR": str(tmp_path / "AI-Journal"),
            "PYTHONPATH": str(SCRIPTS),
        }
    )
    for key in ("OPENAI_API_KEY", "ANTHROPIC_API_KEY", "GEMINI_API_KEY"):
        env.pop(key, None)
    result = subprocess.run(
        [sys.executable, str(CLI), *args],
        input=user_input,
        text=True,
        capture_output=True,
        env=env,
        check=False,
    )
    if check and result.returncode != 0:
        raise AssertionError(
            f"Command failed: {result.args}\nstdout:\n{result.stdout}\n"
            f"stderr:\n{result.stderr}"
        )
    return result


def read_index(tmp_path):
    return json.loads(
        (tmp_path / "AI-Journal" / "index.json").read_text(encoding="utf-8")
    )


def journal_files(tmp_path):
    entries = tmp_path / "AI-Journal" / "entries"
    return sorted(str(p.relative_to(tmp_path / "AI-Journal")) for p in entries.rglob("*.md"))


# --- append targets --------------------------------------------------------


def test_append_today_appends_to_todays_entry(tmp_path):
    run_cli(tmp_path, "new", "Morning study")
    run_cli(tmp_path, "append", "today", "An afternoon thought")
    path = Path(
        run_cli(tmp_path, "open", "latest", "--print-path").stdout.strip()
    )
    assert "An afternoon thought" in path.read_text(encoding="utf-8")


def test_append_today_creates_entry_when_none_exists(tmp_path):
    result = run_cli(tmp_path, "append", "today", "First note of the day")
    assert "Notes -" in result.stdout
    index = read_index(tmp_path)
    assert len(index["entries"]) == 1
    assert "daily-notes" in index["entries"][0]["tags"]


def test_append_today_skips_yesterdays_entry(tmp_path):
    run_cli(tmp_path, "new", "Old entry")
    index_path = tmp_path / "AI-Journal" / "index.json"
    index = read_index(tmp_path)
    yesterday = (datetime.now() - timedelta(days=1)).isoformat() + "Z"
    index["entries"][0]["created"] = yesterday
    index_path.write_text(json.dumps(index), encoding="utf-8")

    run_cli(tmp_path, "append", "today", "Fresh note")
    index = read_index(tmp_path)
    assert len(index["entries"]) == 2  # a new today-entry was started
    old_file = tmp_path / "AI-Journal" / index["entries"][0]["filename"]
    assert "Fresh note" not in old_file.read_text(encoding="utf-8")


def test_append_by_date_target(tmp_path):
    run_cli(tmp_path, "new", "Dated entry")
    today = datetime.now().strftime("%Y-%m-%d")
    run_cli(tmp_path, "append", today, "Found by date")
    path = Path(
        run_cli(tmp_path, "open", "latest", "--print-path").stdout.strip()
    )
    assert "Found by date" in path.read_text(encoding="utf-8")


# --- same-day duplicates & unicode ----------------------------------------


def test_duplicate_topic_same_day_gets_numbered_not_lost(tmp_path):
    run_cli(tmp_path, "new", "Python basics")
    result = run_cli(tmp_path, "new", "Python basics")
    assert "Python basics (2)" in result.stdout
    index = read_index(tmp_path)
    topics = {e["topic"] for e in index["entries"]}
    assert topics == {"Python basics", "Python basics (2)"}
    assert len(journal_files(tmp_path)) == 2


def test_unicode_topic_and_content_roundtrip(tmp_path):
    run_cli(tmp_path, "new", "Résumé — čeština & 日本語", "unicode")
    run_cli(tmp_path, "append", "latest", "Emoji note ✨ and accents: café")
    path = Path(
        run_cli(tmp_path, "open", "latest", "--print-path").stdout.strip()
    )
    text = path.read_text(encoding="utf-8")
    assert "café" in text and "✨" in text
    search = run_cli(tmp_path, "search", "café").stdout
    assert "Résumé" in search


def test_empty_topic_never_creates_nameless_file(tmp_path):
    env = os.environ.copy()
    env["AI_JOURNAL_DIR"] = str(tmp_path / "AI-Journal")
    result = subprocess.run(
        [sys.executable, str(SCRIPTS / "entry_saver.py"), "   "],
        text=True,
        capture_output=True,
        env=env,
        stdin=subprocess.DEVNULL,
    )
    assert result.returncode == 0
    files = journal_files(tmp_path)
    assert len(files) == 1
    assert files[0].endswith("untitled-entry.md")


# --- delete ----------------------------------------------------------------


def test_delete_soft_moves_to_trash_and_keeps_index_consistent(tmp_path):
    run_cli(tmp_path, "new", "Keep me", "keep")
    run_cli(tmp_path, "new", "Delete me", "gone")
    run_cli(tmp_path, "delete", "Delete me", "--yes")

    index = read_index(tmp_path)
    topics = [e["topic"] for e in index["entries"]]
    assert topics == ["Keep me"]
    assert index["stats"]["total_entries"] == 1
    assert "gone" not in index["tags"] and "keep" in index["tags"]

    trash = tmp_path / "AI-Journal" / "trash"
    trashed = list(trash.glob("*delete-me.md"))
    assert len(trashed) == 1
    assert "Delete me" in trashed[0].read_text(encoding="utf-8")
    log = json.loads((trash / "trash-index.json").read_text(encoding="utf-8"))
    assert log[0]["entry"]["topic"] == "Delete me"


def test_delete_requires_confirmation(tmp_path):
    run_cli(tmp_path, "new", "Precious entry")
    result = run_cli(tmp_path, "delete", "Precious entry", user_input="n\n")
    assert "Nothing was deleted" in result.stdout
    assert len(read_index(tmp_path)["entries"]) == 1


def test_delete_purge_removes_file_permanently(tmp_path):
    run_cli(tmp_path, "new", "Purge me")
    run_cli(tmp_path, "delete", "Purge me", "--purge", "--yes")
    assert journal_files(tmp_path) == []
    assert read_index(tmp_path)["entries"] == []
    trash = tmp_path / "AI-Journal" / "trash"
    assert not trash.exists() or not list(trash.glob("*purge-me.md"))


def test_delete_purge_confirmation_needs_typed_delete(tmp_path):
    run_cli(tmp_path, "new", "Half-hearted purge")
    result = run_cli(
        tmp_path, "delete", "Half-hearted purge", "--purge", user_input="y\n"
    )
    assert "Nothing was deleted" in result.stdout
    assert len(read_index(tmp_path)["entries"]) == 1


def test_search_index_consistent_after_delete(tmp_path):
    run_cli(tmp_path, "new", "Grep lesson", "shell")
    run_cli(tmp_path, "append", "latest", "grep finds text in files")
    found = run_cli(tmp_path, "find", "grep").stdout
    assert "Grep lesson" in found
    run_cli(tmp_path, "delete", "Grep lesson", "--yes")
    found = run_cli(tmp_path, "find", "grep").stdout
    assert "No journal entries matched" in found


# --- web API ---------------------------------------------------------------


@pytest.fixture()
def server(tmp_path, monkeypatch):
    monkeypatch.setenv("AI_JOURNAL_DIR", str(tmp_path / "AI-Journal"))
    monkeypatch.setenv("AI_JOURNAL_CONFIG", str(tmp_path / "ai-config.json"))
    for key in ("OPENAI_API_KEY", "ANTHROPIC_API_KEY", "GEMINI_API_KEY", "GROQ_API_KEY"):
        monkeypatch.delenv(key, raising=False)
    import web_server

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


def post(base, path, payload):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(base + path, data=data, method="POST")
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=5) as r:
            return r.status, json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        return exc.code, json.loads(exc.read().decode("utf-8"))


def test_web_append_today_creates_entry_when_none(server):
    status, body = post(
        server, "/api/append", {"target": "today", "content": "web quick note"}
    )
    assert status == 200 and body["ok"] is True
    assert body["topic"].startswith("Notes -")
    status, listing = get(server, "/api/entries")
    assert listing["entries"][0]["when"] == "Today"


def test_web_append_to_specific_entry_by_id(server):
    post(server, "/api/entries", {"topic": "First"})
    post(server, "/api/entries", {"topic": "Second"})
    status, listing = get(server, "/api/entries")
    first_id = [e for e in listing["entries"] if e["topic"] == "First"][0]["id"]
    status, body = post(
        server, "/api/append", {"target": str(first_id), "content": "targeted note"}
    )
    assert status == 200 and body["topic"] == "First"


def test_web_delete_endpoint_soft_deletes(server, tmp_path):
    post(server, "/api/entries", {"topic": "Web delete me"})
    status, listing = get(server, "/api/entries")
    entry_id = listing["entries"][0]["id"]
    status, body = post(server, "/api/delete", {"id": entry_id})
    assert status == 200 and body["ok"] is True
    status, listing = get(server, "/api/entries")
    assert listing["entries"] == []
    trash = tmp_path / "AI-Journal" / "trash"
    assert list(trash.glob("*web-delete-me.md"))


def test_web_edit_updates_body_index_and_search(server, tmp_path):
    post(server, "/api/entries", {"topic": "Editable", "body": "Original fragment."})
    _, listing = get(server, "/api/entries")
    entry_id = listing["entries"][0]["id"]

    status, body = post(
        server,
        "/api/entry/update",
        {"id": entry_id, "body": "# Editable\n\nPolished thought, fragment removed."},
    )
    assert status == 200 and body["ok"] is True

    # File content replaced
    _, detail = get(server, "/api/entry?id=%d" % entry_id)
    assert "Polished thought" in detail["body"]
    assert "Original fragment" not in detail["body"]

    # Search sees the new text, not the old
    _, res = get(server, "/api/search?q=polished")
    assert any(e["id"] == entry_id for e in res["entries"])
    _, res = get(server, "/api/search?q=original")
    assert not any(e["id"] == entry_id for e in res["entries"])

    # Index word count refreshed
    index = json.loads(
        (tmp_path / "AI-Journal" / "index.json").read_text(encoding="utf-8")
    )
    entry = [e for e in index["entries"] if e["id"] == entry_id][0]
    assert entry["word_count"] == len(
        "# Editable\n\nPolished thought, fragment removed.".split()
    )


def test_web_edit_rejects_empty_body(server):
    post(server, "/api/entries", {"topic": "Keep content"})
    _, listing = get(server, "/api/entries")
    entry_id = listing["entries"][0]["id"]
    status, body = post(server, "/api/entry/update", {"id": entry_id, "body": "   "})
    assert status == 400
    assert "empty" in body["error"].lower()


def test_web_edit_unknown_id_is_404(server):
    status, body = post(
        server, "/api/entry/update", {"id": 999999, "body": "anything"}
    )
    assert status == 404


def test_web_edit_preserves_unicode(server):
    post(server, "/api/entries", {"topic": "Unicode edit"})
    _, listing = get(server, "/api/entries")
    entry_id = listing["entries"][0]["id"]
    status, _ = post(
        server,
        "/api/entry/update",
        {"id": entry_id, "body": "# Unicode edit\n\nCafé ✨ 日本語 works."},
    )
    assert status == 200
    _, detail = get(server, "/api/entry?id=%d" % entry_id)
    assert "Café ✨ 日本語" in detail["body"]


def test_web_delete_unknown_id_is_404(server):
    status, body = post(server, "/api/delete", {"id": 424242})
    assert status == 404


def test_web_delete_invalid_id_is_400(server):
    status, body = post(server, "/api/delete", {"id": "not-a-number"})
    assert status == 400
