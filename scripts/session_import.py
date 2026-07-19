#!/usr/bin/env python3
"""Import an AI coding session into the journal as a DRAFT entry.

Reads the local session history that Claude Code already stores on disk
(``~/.claude/projects/<project>/<session>.jsonl``) and turns one session into
a draft journal entry: your real prompts are pre-filled, and the sections
only you can write (Reflection, Key Points) are left for you.

The point is to remove the boring transcription work so the learner's effort
goes where the value is: what you changed after the AI's answer, what broke,
and what the session proves you can do.

Design notes
- Offline, standard library only. Nothing leaves your computer.
- Read-only with respect to session files: we never modify or delete them.
- Claude Code is the first supported tool; the reader is isolated in
  ``ClaudeCodeReader`` so more tools (Gemini CLI, Cursor, Aider...) can be
  added later without touching the rest.
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

from entry_saver import create_entry, load_index

# How much of each prompt/reply we keep in the draft.
MAX_PROMPTS = 12
PROMPT_CHARS = 300
REPLY_CHARS = 200
MAX_SESSIONS_LISTED = 10


def sessions_root() -> Path:
    """Folder Claude Code writes session history to (override for tests)."""
    return Path(
        os.environ.get("CLAUDE_PROJECTS_DIR", Path.home() / ".claude" / "projects")
    )


def _text_of(content) -> str:
    """Extract plain text from a message content field (str or blocks)."""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for block in content:
            if isinstance(block, dict) and block.get("type") == "text":
                parts.append(block.get("text", ""))
        return "\n".join(parts)
    return ""


def _looks_like_noise(text: str) -> bool:
    """Skip system-injected lines that are not something the learner typed."""
    stripped = text.strip()
    return (
        not stripped
        or stripped.startswith("<")  # <command-name>, <local-command-stdout>, ...
        or stripped.startswith("Caveat:")
    )


def _shorten(text: str, limit: int) -> str:
    text = " ".join(text.split())  # collapse whitespace/newlines
    if len(text) <= limit:
        return text
    return text[: limit - 3].rstrip() + "..."


class ClaudeCodeReader:
    """Reads Claude Code JSONL session files."""

    tool_name = "Claude Code"

    def list_sessions(self):
        """Return session descriptors, newest first."""
        root = sessions_root()
        if not root.is_dir():
            return []
        found = []
        for path in root.glob("*/*.jsonl"):
            try:
                mtime = path.stat().st_mtime
            except OSError:
                continue
            found.append({"path": path, "modified": mtime})
        found.sort(key=lambda s: s["modified"], reverse=True)
        return found

    def read_session(self, path: Path) -> dict:
        """Parse one session file into prompts, replies, and metadata."""
        prompts, replies = [], []
        summary = None
        project = path.parent.name.replace("-", "/").lstrip("/")
        first_ts = last_ts = None

        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError:
                    continue

                rtype = record.get("type")
                if rtype == "summary" and record.get("summary"):
                    summary = record["summary"]
                    continue
                if record.get("isMeta"):
                    continue

                ts = record.get("timestamp")
                if ts:
                    first_ts = first_ts or ts
                    last_ts = ts

                # Prefer the real project folder when recorded.
                if record.get("cwd"):
                    project = Path(record["cwd"]).name

                message = record.get("message") or {}
                if rtype == "user" and message.get("role") == "user":
                    text = _text_of(message.get("content"))
                    if not _looks_like_noise(text):
                        prompts.append(text)
                elif rtype == "assistant" and message.get("role") == "assistant":
                    text = _text_of(message.get("content"))
                    if text.strip():
                        replies.append(text)

        return {
            "path": path,
            "project": project,
            "summary": summary,
            "prompts": prompts,
            "replies": replies,
            "first_ts": first_ts,
            "last_ts": last_ts,
        }


def _fmt_ts(ts) -> str:
    """ISO timestamp -> friendly local-ish string (best effort)."""
    if not ts:
        return "unknown time"
    try:
        return datetime.fromisoformat(str(ts).replace("Z", "+00:00")).strftime(
            "%B %d, %Y %H:%M"
        )
    except ValueError:
        return str(ts)


def build_draft(session: dict) -> str:
    """Turn a parsed session into draft entry content (Markdown)."""
    prompts = session["prompts"]
    replies = session["replies"]
    shown = prompts[:MAX_PROMPTS]

    lines = []
    lines.append("## Key Points")
    lines.append("")
    lines.append(
        "<!-- One or two big things you learned this session. "
        "Only you can write this part. -->"
    )
    lines.append("")
    lines.append("## AI Prompt Log (imported)")
    lines.append("")
    if shown:
        for i, prompt in enumerate(shown, 1):
            lines.append(f"{i}. {_shorten(prompt, PROMPT_CHARS)}")
        if len(prompts) > len(shown):
            lines.append(f"...and {len(prompts) - len(shown)} more prompts.")
    else:
        lines.append("(No prompts could be extracted from this session.)")
    lines.append("")
    lines.append(
        "<!-- Pick ONE prompt above and note how you would improve it next time. -->"
    )
    lines.append("")
    lines.append("## Full Session Content")
    lines.append("")
    lines.append(f"Imported from {ClaudeCodeReader.tool_name}.")
    lines.append("")
    lines.append(f"- Project: {session['project']}")
    lines.append(
        f"- Session time: {_fmt_ts(session['first_ts'])} to "
        f"{_fmt_ts(session['last_ts'])}"
    )
    lines.append(f"- Exchanges: {len(prompts)} prompts, {len(replies)} AI replies")
    if replies:
        lines.append(f"- First AI reply began: {_shorten(replies[0], REPLY_CHARS)}")
    lines.append("")
    lines.append(
        "<!-- Paste only the moments that mattered: the command that worked, "
        "the error message, the fix. -->"
    )
    lines.append("")
    lines.append("## Follow-up Actions")
    lines.append("")
    lines.append("<!-- - [ ] Your next step -->")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Reflection")
    lines.append("")
    lines.append(
        "<!-- The section that turns history into proof. "
        "What did you CHANGE after the AI's answers? What broke, and how did "
        "you fix it? What would you tell a reviewer this session proves you "
        "can do? -->"
    )
    return "\n".join(lines)


def find_already_imported(session: dict):
    """Return the existing entry for this session, if it was imported before."""
    session_id = session["path"].stem
    for entry in load_index().get("entries", []):
        if entry.get("session_id") == session_id:
            return entry
    return None


def import_session(session: dict) -> str:
    """Create the draft journal entry for a parsed session."""
    if session["summary"]:
        topic = session["summary"]
    elif session["prompts"]:
        topic = _shorten(session["prompts"][0], 60)
    else:
        topic = f"Session in {session['project']}"

    return create_entry(
        topic,
        content=build_draft(session),
        tags=["session-import", "claude-code"],
        ai_metadata={
            "source": "claude-code-import",
            "session_id": session["path"].stem,
        },
    )


def choose_session(reader: ClaudeCodeReader, take_latest: bool):
    """List sessions and let the user pick one (or auto-pick latest)."""
    sessions = reader.list_sessions()
    if not sessions:
        print(f"No {reader.tool_name} sessions found in {sessions_root()}.")
        print(
            "If you use Claude Code under another account or folder, set "
            "CLAUDE_PROJECTS_DIR to that folder and try again."
        )
        return None

    if take_latest:
        return reader.read_session(sessions[0]["path"])

    print(f"\nRecent {reader.tool_name} sessions (newest first):")
    parsed = []
    for i, item in enumerate(sessions[:MAX_SESSIONS_LISTED], 1):
        details = reader.read_session(item["path"])
        parsed.append(details)
        label = details["summary"] or (
            _shorten(details["prompts"][0], 60) if details["prompts"] else "(empty)"
        )
        when = datetime.fromtimestamp(item["modified"]).strftime("%b %d %H:%M")
        print(
            f"{i:>3}. [{when}] {details['project']}: {label} "
            f"({len(details['prompts'])} prompts)"
        )

    pick = input(f"\nImport which session? (1-{len(parsed)}) [1]: ").strip() or "1"
    try:
        return parsed[int(pick) - 1]
    except (ValueError, IndexError):
        print("Not a valid choice. Nothing was imported.")
        return None


def run(take_latest: bool = False) -> None:
    """Entry point used by the CLI and the menu."""
    reader = ClaudeCodeReader()
    session = choose_session(reader, take_latest)
    if session is None:
        return

    existing = find_already_imported(session)
    if existing is not None:
        print(
            f'\nYou already imported this session on {existing["created"][:10]}: '
            f'"{existing["topic"]}" (entry {existing["id"]})'
        )
        print(f"Open it with: ai-journal open {existing['id']}")
        print("Nothing new was created.")
        return

    entry_path = import_session(session)
    print("\nDraft entry created from your session.")
    print("Your prompts are pre-filled; the Reflection is yours to write.")
    print("\nYour Reflection questions (also inside the entry as editing hints):")
    print("  - What did you CHANGE after the AI's answers?")
    print("  - What broke, and how did you fix it?")
    print("  - What would you tell a reviewer this session proves you can do?")
    print("\nAnswer them now with: ai-journal append   (choose Reflection)")
    print(f"Or edit the file directly. Saved at: {entry_path}")


def main() -> None:
    take_latest = "--latest" in sys.argv
    run(take_latest=take_latest)


if __name__ == "__main__":
    main()
