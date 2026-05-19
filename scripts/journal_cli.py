#!/usr/bin/env python3
"""Cross-platform command dispatcher for AI Journal."""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Optional

from auto_append import append_to_entry, find_entry, get_latest_entry
from entry_saver import create_entry, get_journal_dir


def require_index() -> Path:
    """Return the index path or exit with a useful error."""
    index_path = get_journal_dir() / "index.json"
    if not index_path.exists():
        print(
            f"No journal found at {get_journal_dir()}. "
            'Create one with: ai-journal new "<topic>"',
            file=sys.stderr,
        )
        raise SystemExit(1)
    return index_path


def load_index() -> dict:
    """Load the journal index."""
    return json.loads(require_index().read_text())


def format_entry(entry: dict) -> str:
    """Format a single entry for terminal output."""
    ai_info = ""
    if entry.get("ai_sources"):
        ai_info = f" | AI: {', '.join(entry['ai_sources'])}"

    quality_info = ""
    if entry.get("quality_rating"):
        quality_info = f" | quality: {entry['quality_rating']}/10"

    tags = ", ".join(entry.get("tags", [])) or "untagged"
    return (
        f"{entry['id']:>3} | {entry['created'][:10]} | "
        f"{entry['topic']}{ai_info}{quality_info} | tags: {tags}"
    )


def resolve_entry(target: str) -> Optional[dict]:
    """Resolve an entry by id, topic, slug, or latest."""
    if target.lower() == "latest":
        return get_latest_entry()
    return find_entry(target)


def cmd_new(args: argparse.Namespace) -> None:
    """Create a new journal entry."""
    create_entry(args.topic, tags=args.tags)


def cmd_append(args: argparse.Namespace) -> None:
    """Append content to an existing journal entry."""
    require_index()
    entry = resolve_entry(args.target)
    if entry is None:
        print(f"No entry found matching '{args.target}'", file=sys.stderr)
        raise SystemExit(1)
    append_to_entry(entry, args.content, args.section)


def cmd_list(args: argparse.Namespace) -> None:
    """List journal entries."""
    index = load_index()
    entries = sorted(index["entries"], key=lambda entry: entry["created"], reverse=True)
    if args.limit is not None:
        entries = entries[: args.limit]
    for entry in entries:
        print(format_entry(entry))


def cmd_search(args: argparse.Namespace) -> None:
    """Search journal entries by topic or tag."""
    index = load_index()
    query = args.query.lower()
    matches = [
        entry
        for entry in index["entries"]
        if query in entry["topic"].lower()
        or any(query in tag.lower() for tag in entry.get("tags", []))
    ]

    if not matches:
        print("No matches found.")
        return

    for entry in sorted(matches, key=lambda entry: entry["created"], reverse=True):
        print(format_entry(entry))


def open_path(path: Path) -> None:
    """Open a file with the platform default application."""
    if sys.platform == "darwin":
        subprocess.run(["open", str(path)], check=False)
    elif os.name == "nt":
        os.startfile(str(path))  # type: ignore[attr-defined]
    else:
        subprocess.run(["xdg-open", str(path)], check=False)


def cmd_open(args: argparse.Namespace) -> None:
    """Open a journal entry."""
    require_index()
    entry = resolve_entry(args.target)
    if entry is None:
        print(f"No entry found matching '{args.target}'", file=sys.stderr)
        raise SystemExit(1)

    entry_path = get_journal_dir() / entry["filename"]
    if args.print_path:
        print(entry_path)
        return
    open_path(entry_path)


def cmd_ask(args: argparse.Namespace) -> None:
    """Run the AI integration command."""
    import ai_integration

    sys.argv = ["ai_integration.py", args.question, *args.options]
    ai_integration.main()


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser."""
    parser = argparse.ArgumentParser(
        prog="ai-journal",
        description="AI Journal CLI v3.0",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    new_parser = subparsers.add_parser("new", help="Create a new entry")
    new_parser.add_argument("topic")
    new_parser.add_argument("tags", nargs="*")
    new_parser.set_defaults(func=cmd_new)

    append_parser = subparsers.add_parser("append", help="Append to an entry")
    append_parser.add_argument("target")
    append_parser.add_argument("content")
    append_parser.add_argument("section", nargs="?", default="Q&A")
    append_parser.set_defaults(func=cmd_append)

    list_parser = subparsers.add_parser("list", help="List entries")
    list_parser.add_argument("--limit", type=int)
    list_parser.set_defaults(func=cmd_list)

    search_parser = subparsers.add_parser("search", help="Search entries")
    search_parser.add_argument("query")
    search_parser.set_defaults(func=cmd_search)

    open_parser = subparsers.add_parser("open", help="Open an entry")
    open_parser.add_argument("target")
    open_parser.add_argument("--print-path", action="store_true")
    open_parser.set_defaults(func=cmd_open)

    ask_parser = subparsers.add_parser("ask", help="Ask an AI and curate the response")
    ask_parser.add_argument("question")
    ask_parser.add_argument("options", nargs=argparse.REMAINDER)
    ask_parser.set_defaults(func=cmd_ask)

    compare_parser = subparsers.add_parser("compare", help="Compare AI sources")
    compare_parser.add_argument("question")
    compare_parser.add_argument("options", nargs=argparse.REMAINDER)
    compare_parser.set_defaults(
        func=lambda args: cmd_ask(
            argparse.Namespace(
                question=args.question,
                options=["--compare", "chatgpt,claude,gemini", *args.options],
            )
        )
    )

    return parser


def main() -> None:
    """Run the CLI."""
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
