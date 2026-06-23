#!/usr/bin/env python3
"""Local web UI for AI Journal.

A tiny standard-library web server that wraps the existing journal logic
(entry_saver, auto_append, journal_cli, ai_integration) in a small JSON API
and serves the friendly browser front-end in ``web/``.

Design goals:
  - Standard library only (http.server) so there is nothing to install on a
    low-end machine.
  - Reuse the CLI's functions directly; do not duplicate journal logic.
  - Keep storage identical (plain Markdown in AI_JOURNAL_DIR / ~/AI-Journal) so
    the CLI and the web UI share the same data.
  - Bind to localhost only and reject cross-origin requests.

Run it:  python3 scripts/web_server.py
"""

import getpass
import json
import os
import re
import sys
import threading
import webbrowser
from datetime import date, datetime, timedelta
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

# Make the sibling modules importable whether launched from the repo root or
# from inside scripts/ (they import each other by bare module name).
SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from ai_integration import (  # noqa: E402
    PROVIDERS,
    answer_offline,
    get_active_provider,
    live_answer,
    load_config,
    save_config,
    save_live_answer,
)
from auto_append import append_to_entry, find_entry, get_latest_entry  # noqa: E402
from entry_saver import create_entry, get_journal_dir  # noqa: E402
from entry_saver import load_index as ensure_index  # noqa: E402
from journal_cli import search_entries  # noqa: E402

# Front-end assets live in ../web relative to this file.
WEB_DIR = (SCRIPTS_DIR.parent / "web").resolve()

HOST = "127.0.0.1"
DEFAULT_PORT = 8765

CONTENT_TYPES = {
    ".html": "text/html; charset=utf-8",
    ".js": "application/javascript; charset=utf-8",
    ".css": "text/css; charset=utf-8",
    ".svg": "image/svg+xml",
    ".json": "application/json; charset=utf-8",
    ".png": "image/png",
    ".ico": "image/x-icon",
}

# Heatmap is 13 weeks x 7 days = 91 cells, oldest -> newest (today is last).
HEAT_DAYS = 91
HEAT_LEVELS = 5  # 0..4


# ---------------------------------------------------------------------------
# Read helpers (presentation only; all journal logic lives in the CLI modules)
# ---------------------------------------------------------------------------

def _parse_created(entry: dict) -> date:
    """Return the calendar date an entry was created."""
    raw = (entry.get("created") or "")[:10]
    try:
        return datetime.strptime(raw, "%Y-%m-%d").date()
    except ValueError:
        return date.today()


def _relative_when(created: date, today: date | None = None) -> str:
    """Friendly relative day label: Today / Yesterday / N days ago."""
    today = today or date.today()
    days = (today - created).days
    if days <= 0:
        return "Today"
    if days == 1:
        return "Yesterday"
    if days < 7:
        return f"{days} days ago"
    if days < 14:
        return "Last week"
    return created.strftime("%b %d, %Y")


def _entry_preview(entry: dict) -> str:
    """First line of real content for an entry, skipping headings/metadata.

    Empty template entries (only HTML-comment hints) return "" so the UI can
    show a gentle placeholder instead of markup.
    """
    try:
        text = (get_journal_dir() / entry["filename"]).read_text(encoding="utf-8")
    except OSError:
        return ""
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        # Drop a leading bullet so we can detect placeholders and show clean text.
        core = line[2:].strip() if line.startswith(("- ", "* ")) else line
        if not core:
            continue
        # Skip headings, metadata, rules, and comment hints.
        if core.startswith(("#", "<!--", "---", "**", ">")):
            continue
        # Skip legacy bracket-style template placeholders, e.g.
        # "[Add your key insights here]" or task hints like "[ ] Your next step".
        if core.startswith("[") and core.endswith("]"):
            continue
        if core.startswith(("[ ]", "[]")):
            continue
        return core if len(core) <= 140 else core[:137] + "..."
    return ""


def _entry_summary(entry: dict, today: date | None = None) -> dict:
    """Shape an index entry for the front-end."""
    created = _parse_created(entry)
    return {
        "id": entry.get("id"),
        "topic": entry.get("topic", ""),
        "tags": entry.get("tags", []) or [],
        "created": entry.get("created", ""),
        "when": _relative_when(created, today),
        "preview": _entry_preview(entry),
        "ai_sources": entry.get("ai_sources", []),
    }


def _profile_path() -> Path:
    """Where the learner's display name is stored (local, alongside the index)."""
    return get_journal_dir() / "profile.json"


def _load_profile() -> dict:
    try:
        return json.loads(_profile_path().read_text(encoding="utf-8")) or {}
    except (OSError, ValueError):
        return {}


def _save_profile(profile: dict) -> None:
    path = _profile_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(profile, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)


def _display_name() -> tuple[str, bool]:
    """Resolve the greeting name.

    Order: a name the learner saved -> the AI_JOURNAL_NAME env var -> a tidied
    version of the OS account name. Returns (name, name_set) where name_set is
    True only when the learner (or env) chose the name explicitly.
    """
    saved = (_load_profile().get("name") or "").strip()
    if saved:
        return saved, True
    env = (os.getenv("AI_JOURNAL_NAME") or "").strip()
    if env:
        return env, True
    raw = getpass.getuser() or "there"
    first = re.split(r"[._\-\s]+", raw)[0] or raw
    pretty = (first[:1].upper() + first[1:]) if first else "there"
    return pretty, False


def _all_entries_sorted() -> list[dict]:
    """All index entries, newest first."""
    index = ensure_index()
    return sorted(
        index.get("entries", []), key=lambda e: e.get("created", ""), reverse=True
    )


def _compute_stats() -> dict:
    """Streak, activity, heatmap and badges derived from the index."""
    index = ensure_index()
    entries = index.get("entries", [])
    today = date.today()

    active_days = {_parse_created(e) for e in entries}

    # Streak: consecutive days ending today (or yesterday, so you don't lose a
    # streak until a full day is missed).
    cursor = today
    if cursor not in active_days:
        cursor = today - timedelta(days=1)
    streak = 0
    while cursor in active_days:
        streak += 1
        cursor -= timedelta(days=1)

    # Heatmap counts per day for the last HEAT_DAYS days, oldest -> newest.
    counts: dict[date, int] = {}
    for e in entries:
        d = _parse_created(e)
        counts[d] = counts.get(d, 0) + 1
    heat = []
    start = today - timedelta(days=HEAT_DAYS - 1)
    for i in range(HEAT_DAYS):
        d = start + timedelta(days=i)
        c = counts.get(d, 0)
        heat.append(min(c, HEAT_LEVELS - 1))

    total = len(entries)
    asked_guide = any(
        "starter-guide" in (e.get("tags") or []) or "question" in (e.get("tags") or [])
        for e in entries
    )

    badges = []
    if total >= 1:
        badges.append({"icon": "\U0001F331", "label": "First entry"})
    if streak >= 3:
        badges.append({"icon": "\U0001F525", "label": "3-day streak"})
    if asked_guide:
        badges.append({"icon": "\U0001F4AC", "label": "Asked the Guide"})
    if total >= 7:
        badges.append({"icon": "\U0001F4DA", "label": "7 entries"})

    name, name_set = _display_name()

    return {
        "name": name,
        "name_set": name_set,
        "avatar": (name[:1].upper() if name else "A"),
        "streak": streak,
        "days_active": len(active_days),
        "total_entries": total,
        "badges": badges,
        "badge_count": len(badges),
        "heat": heat,
        "ai_assisted": index.get("ai_stats", {}).get("total_ai_assisted", 0),
    }


# ---------------------------------------------------------------------------
# Write helpers (delegate straight to the reused CLI functions)
# ---------------------------------------------------------------------------

def _create_entry(payload: dict) -> dict:
    topic = (payload.get("topic") or "").strip()
    if not topic:
        raise ValueError("A topic is required.")
    tags = payload.get("tags") or []
    if isinstance(tags, str):
        tags = [t.strip() for t in tags.replace(",", " ").split() if t.strip()]
    body = (payload.get("body") or "").strip() or None
    create_entry(topic, body, tags)
    return {"ok": True}


def _append_entry(payload: dict) -> dict:
    content = (payload.get("content") or "").strip()
    if not content:
        raise ValueError("Some text is required to add a note.")
    target = (payload.get("target") or "latest").strip() or "latest"
    section = payload.get("section") or "Reflection"

    entry = get_latest_entry() if target.lower() == "latest" else find_entry(target)
    if entry is None:
        raise LookupError(f"No entry found matching '{target}'.")
    append_to_entry(entry, content, section)
    return {"ok": True, "topic": entry.get("topic", "")}


def _set_profile(payload: dict) -> dict:
    name = (payload.get("name") or "").strip()
    profile = _load_profile()
    if name:
        profile["name"] = name[:40]
    else:
        profile.pop("name", None)  # empty clears it, falling back to OS name
    _save_profile(profile)
    resolved, name_set = _display_name()
    return {"ok": True, "name": resolved, "name_set": name_set}


def _provider_catalog() -> list[dict]:
    return [
        {
            "id": pid,
            "label": m["label"],
            "get_key_url": m["get_key_url"],
            "note": m.get("note", ""),
        }
        for pid, m in PROVIDERS.items()
    ]


def _ai_status() -> dict:
    prov = get_active_provider()
    base = {"providers": _provider_catalog()}
    if not prov:
        base.update({"enabled": False, "provider": None, "label": None, "masked": None})
        return base
    pid, key, _model = prov
    masked = ("••••" + key[-4:]) if len(key) >= 4 else "••••"
    base.update(
        {"enabled": True, "provider": pid, "label": PROVIDERS[pid]["label"], "masked": masked}
    )
    return base


def _set_ai_key(payload: dict) -> dict:
    provider = (payload.get("provider") or "").strip().lower()
    api_key = (payload.get("api_key") or "").strip()
    if provider not in PROVIDERS:
        raise ValueError("Choose a valid AI provider.")
    if not api_key:
        raise ValueError("Paste your API key.")
    # Validate the key with a tiny live call so bad keys are caught immediately.
    try:
        live_answer("Reply with the single word: OK", provider, api_key, timeout=20)
    except RuntimeError as exc:
        raise ValueError(str(exc))
    cfg = load_config()
    cfg.setdefault("api_keys", {})[provider] = api_key
    cfg["provider"] = provider
    save_config(cfg)
    return _ai_status()


def _disconnect_ai(_payload: dict) -> dict:
    cfg = load_config()
    prov = cfg.get("provider")
    if prov and isinstance(cfg.get("api_keys"), dict):
        cfg["api_keys"].pop(prov, None)
    cfg["provider"] = None
    save_config(cfg)
    return _ai_status()


def _ask(payload: dict) -> dict:
    question = (payload.get("question") or "").strip()
    if not question:
        raise ValueError("Type a question first.")

    prov = get_active_provider()
    if prov:
        pid, key, model = prov
        try:
            answer = live_answer(question, pid, key, model)
            label = save_live_answer(question, answer, pid)
            return {"ok": True, "matched": True, "answer": answer, "source": label, "message": None}
        except RuntimeError as exc:
            answer, matched, _ = answer_offline(question)
            msg = f"Live AI didn't answer ({exc})."
            if matched:
                msg += " Showing the offline Starter Guide instead."
            return {
                "ok": True,
                "matched": matched,
                "answer": answer,
                "source": "Starter Guide" if matched else None,
                "message": msg,
            }

    answer, matched, _ = answer_offline(question)
    return {
        "ok": True,
        "matched": matched,
        "answer": answer,
        "source": "Starter Guide" if matched else None,
        "message": (
            None
            if matched
            else (
                "Full AI answers switch on with a free key (one-time setup). "
                "I've saved your question so you can come back to it."
            )
        ),
    }


# ---------------------------------------------------------------------------
# HTTP handler
# ---------------------------------------------------------------------------

class JournalHandler(BaseHTTPRequestHandler):
    server_version = "AIJournalWeb/1.0"

    # --- small helpers -----------------------------------------------------

    def _send_json(self, obj, status=200):
        body = json.dumps(obj).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _read_json(self) -> dict:
        length = int(self.headers.get("Content-Length") or 0)
        if not length:
            return {}
        raw = self.rfile.read(length)
        try:
            return json.loads(raw.decode("utf-8")) or {}
        except (ValueError, UnicodeDecodeError):
            return {}

    def _same_origin(self) -> bool:
        """Block cross-site requests; we only trust localhost callers."""
        host = (self.headers.get("Host") or "").split(":")[0]
        if host not in ("127.0.0.1", "localhost"):
            return False
        origin = self.headers.get("Origin")
        if origin:
            host_o = urlparse(origin).hostname
            if host_o not in ("127.0.0.1", "localhost"):
                return False
        return True

    def log_message(self, fmt, *args):  # quieter console
        pass

    # --- routing -----------------------------------------------------------

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        if path.startswith("/api/"):
            return self._handle_api_get(path, parse_qs(parsed.query))
        return self._serve_static(path)

    def do_POST(self):
        parsed = urlparse(self.path)
        if not parsed.path.startswith("/api/"):
            return self._send_json({"error": "Not found"}, 404)
        if not self._same_origin():
            return self._send_json({"error": "Cross-origin request blocked"}, 403)
        payload = self._read_json()
        try:
            if parsed.path == "/api/entries":
                return self._send_json(_create_entry(payload))
            if parsed.path == "/api/append":
                return self._send_json(_append_entry(payload))
            if parsed.path == "/api/ask":
                return self._send_json(_ask(payload))
            if parsed.path == "/api/profile":
                return self._send_json(_set_profile(payload))
            if parsed.path == "/api/ai/key":
                return self._send_json(_set_ai_key(payload))
            if parsed.path == "/api/ai/disconnect":
                return self._send_json(_disconnect_ai(payload))
        except ValueError as exc:
            return self._send_json({"error": str(exc)}, 400)
        except LookupError as exc:
            return self._send_json({"error": str(exc)}, 404)
        except Exception as exc:  # pragma: no cover - defensive
            return self._send_json({"error": f"Something went wrong: {exc}"}, 500)
        return self._send_json({"error": "Not found"}, 404)

    def _handle_api_get(self, path, query):
        try:
            if path == "/api/health":
                return self._send_json({"ok": True})
            if path == "/api/stats":
                return self._send_json(_compute_stats())
            if path == "/api/profile":
                name, name_set = _display_name()
                return self._send_json({"name": name, "name_set": name_set})
            if path == "/api/ai/status":
                return self._send_json(_ai_status())
            if path == "/api/entries":
                today = date.today()
                limit_vals = query.get("limit")
                entries = [_entry_summary(e, today) for e in _all_entries_sorted()]
                if limit_vals:
                    try:
                        entries = entries[: int(limit_vals[0])]
                    except ValueError:
                        pass
                return self._send_json({"entries": entries})
            if path == "/api/search":
                q = (query.get("q") or [""])[0]
                today = date.today()
                results = []
                for entry, snippet in search_entries(q):
                    item = _entry_summary(entry, today)
                    if snippet:
                        item["snippet"] = snippet
                    results.append(item)
                return self._send_json({"query": q, "entries": results})
        except Exception as exc:  # pragma: no cover - defensive
            return self._send_json({"error": f"Something went wrong: {exc}"}, 500)
        return self._send_json({"error": "Not found"}, 404)

    def _serve_static(self, path):
        rel = "index.html" if path in ("", "/") else path.lstrip("/")
        target = (WEB_DIR / rel).resolve()
        # Prevent path traversal outside the web directory.
        if WEB_DIR not in target.parents and target != WEB_DIR:
            return self._send_json({"error": "Forbidden"}, 403)
        if not target.is_file():
            return self._send_json({"error": "Not found"}, 404)
        data = target.read_bytes()
        ctype = CONTENT_TYPES.get(target.suffix.lower(), "application/octet-stream")
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


# ---------------------------------------------------------------------------
# Server lifecycle
# ---------------------------------------------------------------------------

def make_server(port: int = DEFAULT_PORT) -> ThreadingHTTPServer:
    """Create (but do not start) the threaded server. port=0 picks a free port."""
    ensure_index()  # make sure the journal + index exist before serving
    return ThreadingHTTPServer((HOST, port), JournalHandler)


def run(port: int = DEFAULT_PORT, open_browser: bool = True) -> None:
    """Start the server, open the browser, and serve until Ctrl-C."""
    httpd = make_server(port)
    actual_port = httpd.server_address[1]
    url = f"http://{HOST}:{actual_port}/"
    print("AI Journal is running.")
    print(f"  Open this in your browser:  {url}")
    print(f"  Your notes are saved in:    {get_journal_dir()}")
    print("  Press Ctrl-C here to stop.")
    if open_browser:
        threading.Timer(0.6, lambda: webbrowser.open(url)).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping AI Journal. Your notes are saved. Goodbye!")
    finally:
        httpd.server_close()


def main() -> None:
    port = DEFAULT_PORT
    if os.getenv("AI_JOURNAL_PORT"):
        try:
            port = int(os.environ["AI_JOURNAL_PORT"])
        except ValueError:
            pass
    no_browser = "--no-browser" in sys.argv
    run(port=port, open_browser=not no_browser)


if __name__ == "__main__":
    main()
