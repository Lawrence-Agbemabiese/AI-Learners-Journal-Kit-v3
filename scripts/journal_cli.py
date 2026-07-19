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
from entry_saver import load_index as ensure_index


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


def prompt_required(label: str) -> str:
    """Prompt until the user enters a non-empty value."""
    while True:
        value = input(f"{label}: ").strip()
        if value:
            return value
        print(f"{label} is required.")


def prompt_optional_list(label: str, example: Optional[str] = None) -> list[str]:
    """Prompt for a comma- or space-separated list, with an optional example."""
    hint = f" (optional, e.g. {example})" if example else " (optional)"
    value = input(f"{label}{hint}: ").strip()
    if not value:
        return []
    return [item.strip() for item in value.replace(",", " ").split() if item.strip()]


def prompt_multiline(label: str) -> str:
    """Prompt for multiline input without requiring shell quoting."""
    print(f"{label}:")
    print("Enter your text. Finish with a blank line.")
    lines = []
    while True:
        line = input()
        if line == "" and lines:
            break
        if line == "" and not lines:
            print("Please enter at least one line.")
            continue
        lines.append(line)
    return "\n".join(lines)


def format_entry(entry: dict) -> str:
    """Format a single entry for terminal output."""
    ai_info = ""
    if entry.get("ai_sources"):
        ai_info = f" | AI: {', '.join(entry['ai_sources'])}"

    review_info = ""
    if entry.get("quality_rating"):
        review_info = f" | review: {entry['quality_rating']}/10"

    tags = ", ".join(entry.get("tags", [])) or "untagged"
    return (
        f"{entry['id']:>3} | {entry['created'][:10]} | "
        f"{entry['topic']}{ai_info}{review_info} | tags: {tags}"
    )


def resolve_entry(target: str) -> Optional[dict]:
    """Resolve an entry by id, topic, slug, or latest."""
    if target.lower() == "latest":
        return get_latest_entry()
    return find_entry(target)


def cmd_new(args: argparse.Namespace) -> None:
    """Create a new journal entry."""
    topic = args.topic or prompt_required("Entry topic")
    tags = (
        args.tags
        if args.topic
        else prompt_optional_list("Tags", example="python, beginner, bug-fix")
    )
    create_entry(topic, tags=tags)


SECTION_CHOICES = {
    "1": "Reflection",
    "2": "Key Points",
    "3": "Questions & Answers",
    "4": "Full Session Content",
}


def cmd_append(args: argparse.Namespace) -> None:
    """Append content to an existing journal entry."""
    require_index()
    target = args.target or input("Entry to update [latest]: ").strip() or "latest"
    entry = resolve_entry(target)
    if entry is None:
        print(f"No entry found matching '{target}'", file=sys.stderr)
        raise SystemExit(1)

    # Interactive when content was not passed on the command line (menu path).
    interactive = getattr(args, "content", None) is None

    # Show which entry we're about to write to and let the user redirect.
    # (Asking AI can silently create a new "latest" entry, so confirm here.)
    if interactive:
        print(f'\nAdding to: "{entry["topic"]}"  (created {entry["created"][:10]})')
        if input("Is this the right entry? [Y/n]: ").strip().lower().startswith("n"):
            index = load_index()
            print("\nYour entries:")
            for existing in sorted(
                index["entries"], key=lambda e: e["created"], reverse=True
            ):
                print("  " + format_entry(existing))
            pick = input("\nType the number of the entry to use: ").strip()
            chosen = resolve_entry(pick) if pick else None
            if chosen is None:
                print("No matching entry. Nothing was changed.")
                return
            entry = chosen

    content = args.content or prompt_multiline("Content to add")

    section = args.section
    if section is None:
        if interactive:
            print("\nWhere should this go?")
            print("  1. Reflection (default)")
            print("  2. Key Points")
            print("  3. Questions & Answers")
            print("  4. Full Session Content")
            section = SECTION_CHOICES.get(
                input("Choose 1-4 [1]: ").strip(), "Reflection"
            )
        else:
            section = "Reflection"

    append_to_entry(entry, content, section)


def cmd_list(args: argparse.Namespace) -> None:
    """List journal entries."""
    index = load_index()
    entries = sorted(index["entries"], key=lambda entry: entry["created"], reverse=True)
    if args.limit is not None:
        entries = entries[: args.limit]
    for entry in entries:
        print(format_entry(entry))


def search_entries(query: str) -> list[tuple[dict, Optional[str]]]:
    """Search entries by title, tag, AND full text. Pure: returns matches.

    Returns a list of (entry, snippet) tuples sorted newest-first. ``snippet``
    is the first non-heading line containing the query, or ``None`` when the
    match came only from the topic/tags. Shared by the CLI and the web layer
    so search behaves identically in both.
    """
    index = load_index()
    query = (query or "").lower()
    journal_dir = get_journal_dir()

    matches = []
    for entry in index["entries"]:
        in_meta = query in entry["topic"].lower() or any(
            query in tag.lower() for tag in entry.get("tags", [])
        )

        snippet = None
        try:
            text = (journal_dir / entry["filename"]).read_text(encoding="utf-8")
        except OSError:
            text = ""
        if query in text.lower():
            for line in text.splitlines():
                stripped = line.strip()
                if (
                    query in stripped.lower()
                    and stripped
                    and not stripped.startswith("#")
                    and not stripped.startswith("<!--")
                ):
                    snippet = (
                        stripped if len(stripped) <= 100 else stripped[:97] + "..."
                    )
                    break

        if in_meta or snippet is not None:
            matches.append((entry, snippet))

    return sorted(matches, key=lambda m: m[0]["created"], reverse=True)


def cmd_search(args: argparse.Namespace) -> None:
    """Search journal entries by title, tag, AND the text inside each entry."""
    query = args.query or prompt_required("Search keyword")
    matches = search_entries(query)

    if not matches:
        print("No matches found.")
        return

    for entry, snippet in matches:
        print(format_entry(entry))
        if snippet:
            print(f"      > {snippet}")


def open_path(path: Path) -> None:
    """Open a file with the platform default application."""
    if sys.platform == "darwin":
        subprocess.run(["open", str(path)], check=False)
    elif os.name == "nt":
        os.startfile(str(path))  # type: ignore[attr-defined]
    else:
        subprocess.run(["xdg-open", str(path)], check=False)


def cmd_open(args: argparse.Namespace) -> None:
    """Show a journal entry in the terminal; offer to open it in an app too."""
    require_index()
    target = args.target or input("Entry to open [latest]: ").strip() or "latest"
    entry = resolve_entry(target)
    if entry is None:
        print(f"No entry found matching '{target}'", file=sys.stderr)
        raise SystemExit(1)

    entry_path = get_journal_dir() / entry["filename"]
    if getattr(args, "print_path", False):
        print(entry_path)
        return

    # Show the entry right here in the terminal. This avoids surprising the
    # user by launching whatever app happens to be the system's .md handler.
    try:
        text = (entry_path).read_text(encoding="utf-8")
    except OSError as exc:
        print(f"Could not read entry: {exc}", file=sys.stderr)
        raise SystemExit(1)

    # Hide invisible template hints so the preview reads cleanly.
    visible = "\n".join(
        line
        for line in text.split("\n")
        if not (line.strip().startswith("<!--") and line.strip().endswith("-->"))
    )

    rule = "-" * 60
    print(f"\n{rule}\n{visible.strip()}\n{rule}")
    print(f"Saved at: {entry_path}")

    try:
        answer = input("Open in your default app too? [y/N]: ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        answer = ""
    if answer.startswith("y"):
        open_path(entry_path)


def cmd_ask(args: argparse.Namespace) -> None:
    """Run the AI integration command."""
    import ai_integration

    question = args.question or prompt_required("Question for AI")
    sys.argv = ["ai_integration.py", question, *args.options]
    ai_integration.main()


def cmd_setup(args: argparse.Namespace) -> None:
    """Run a beginner-friendly setup check."""
    journal_dir = get_journal_dir()
    scripts_dir = journal_dir / "scripts"
    journal_dir.mkdir(parents=True, exist_ok=True)
    (journal_dir / "entries").mkdir(exist_ok=True)
    (journal_dir / "media").mkdir(exist_ok=True)
    scripts_dir.mkdir(exist_ok=True)

    ensure_index()

    print("Setup check complete.")
    print(f"Journal folder: {journal_dir}")
    print(f"Entries folder: {journal_dir / 'entries'}")
    print(f"Python: {sys.version.split()[0]}")

    try:
        import openai  # noqa: F401

        print("Optional OpenAI package: installed")
    except ImportError:
        print("Optional OpenAI package: not installed")
        print("Install later with: python -m pip install -r requirements.txt")

    if os.getenv("OPENAI_API_KEY"):
        print("OpenAI API key: configured")
    else:
        print("OpenAI API key: not configured")


def cmd_web(args: argparse.Namespace) -> None:
    """Launch the friendly local web UI in the browser."""
    import web_server

    port = getattr(args, "port", None) or web_server.DEFAULT_PORT
    web_server.run(port=port, open_browser=not getattr(args, "no_browser", False))


def cmd_import(args: argparse.Namespace) -> None:
    """Import a Claude Code session as a draft journal entry."""
    import session_import

    session_import.run(take_latest=getattr(args, "latest", False))


def cmd_menu(args: argparse.Namespace) -> None:
    """Show a simple menu for users who do not want to memorize commands."""
    while True:
        print("\nAI Journal")
        print("1. Create a new journal entry")
        print("2. Add to latest entry")
        print("3. Ask AI and save answer")
        print("4. Search my journal")
        print("5. Open latest entry")
        print("6. Import a Claude Code session as a draft entry")
        print("7. Run setup check")
        print("8. Quit")
        choice = input("Choose an option (1-8): ").strip()

        if choice == "1":
            cmd_new(argparse.Namespace(topic=None, tags=[]))
        elif choice == "2":
            cmd_append(argparse.Namespace(target="latest", content=None, section=None))
        elif choice == "3":
            cmd_ask(argparse.Namespace(question=None, options=[]))
        elif choice == "4":
            cmd_search(argparse.Namespace(query=None))
        elif choice == "5":
            cmd_open(argparse.Namespace(target="latest", print_path=False))
        elif choice == "6":
            cmd_import(argparse.Namespace(latest=False))
        elif choice == "7":
            cmd_setup(argparse.Namespace())
        elif choice == "8":
            print("Goodbye.")
            return
        else:
            print("Please choose a number from 1 to 8.")


def cmd_doctor(args: argparse.Namespace) -> None:
    """Run an expanded, beginner-friendly health check."""
    from modern_tools import doctor

    raise SystemExit(doctor())


def cmd_reindex(args: argparse.Namespace) -> None:
    """Rebuild the optional SQLite full-text search index."""
    from modern_tools import reindex

    raise SystemExit(reindex())


def cmd_find(args: argparse.Namespace) -> None:
    """Run ranked full-text search."""
    from modern_tools import search_command

    query = args.query or prompt_required("Search words")
    raise SystemExit(search_command(query, args.limit))


def cmd_backup(args: argparse.Namespace) -> None:
    """Create a portable ZIP backup of the journal."""
    from modern_tools import backup

    raise SystemExit(backup(args.destination))


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser."""
    parser = argparse.ArgumentParser(
        prog="ai-journal",
        description="AI Journal CLI v3.0",
    )
    subparsers = parser.add_subparsers(dest="command")

    new_parser = subparsers.add_parser("new", help="Create a new entry")
    new_parser.add_argument("topic", nargs="?")
    new_parser.add_argument("tags", nargs="*")
    new_parser.set_defaults(func=cmd_new)

    append_parser = subparsers.add_parser("append", help="Append to an entry")
    append_parser.add_argument("target", nargs="?")
    append_parser.add_argument("content", nargs="?")
    append_parser.add_argument("section", nargs="?", default=None)
    append_parser.set_defaults(func=cmd_append)

    list_parser = subparsers.add_parser("list", help="List entries")
    list_parser.add_argument("--limit", type=int)
    list_parser.set_defaults(func=cmd_list)

    search_parser = subparsers.add_parser("search", help="Search entries")
    search_parser.add_argument("query", nargs="?")
    search_parser.set_defaults(func=cmd_search)

    open_parser = subparsers.add_parser("open", help="Open an entry")
    open_parser.add_argument("target", nargs="?")
    open_parser.add_argument("--print-path", action="store_true")
    open_parser.set_defaults(func=cmd_open)

    ask_parser = subparsers.add_parser("ask", help="Ask an AI and curate the response")
    ask_parser.add_argument("question", nargs="?")
    ask_parser.add_argument("options", nargs=argparse.REMAINDER)
    ask_parser.set_defaults(func=cmd_ask)

    web_parser = subparsers.add_parser(
        "web", help="Open the friendly web UI in a browser"
    )
    web_parser.add_argument("--port", type=int, default=None)
    web_parser.add_argument("--no-browser", action="store_true")
    web_parser.set_defaults(func=cmd_web)

    menu_parser = subparsers.add_parser("menu", help="Open the beginner menu")
    menu_parser.set_defaults(func=cmd_menu)

    import_parser = subparsers.add_parser(
        "import", help="Import a Claude Code session as a draft entry"
    )
    import_parser.add_argument(
        "--latest", action="store_true", help="Import the most recent session"
    )
    import_parser.set_defaults(func=cmd_import)

    setup_parser = subparsers.add_parser("setup", help="Run setup checks")
    setup_parser.set_defaults(func=cmd_setup)

    doctor_parser = subparsers.add_parser(
        "doctor", help="Check that AI Journal is ready"
    )
    doctor_parser.set_defaults(func=cmd_doctor)

    reindex_parser = subparsers.add_parser(
        "reindex", help="Rebuild fast full-text search"
    )
    reindex_parser.set_defaults(func=cmd_reindex)

    find_parser = subparsers.add_parser("find", help="Ranked full-text journal search")
    find_parser.add_argument("query", nargs="?")
    find_parser.add_argument("--limit", type=int, default=20)
    find_parser.set_defaults(func=cmd_find)

    backup_parser = subparsers.add_parser("backup", help="Create a ZIP backup")
    backup_parser.add_argument("destination", nargs="?")
    backup_parser.set_defaults(func=cmd_backup)

    return parser


def main() -> None:
    """Run the CLI."""
    parser = build_parser()
    args = parser.parse_args()
    if not hasattr(args, "func"):
        cmd_menu(args)
        return
    args.func(args)


if __name__ == "__main__":
    main()
