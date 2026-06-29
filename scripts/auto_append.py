#!/usr/bin/env python3
"""Append content to existing AI Journal entries."""

import json
import os
import sys
from datetime import datetime
from pathlib import Path


def get_journal_dir():
    """Get the AI Journal directory path."""
    return Path(os.environ.get("AI_JOURNAL_DIR", Path.home() / "AI-Journal"))


def status(label, value=None):
    """Print ASCII-safe status output for cross-platform terminal capture."""
    if value is None:
        print(label)
    else:
        print(f"{label}: {value}")


def load_index():
    """Load the journal index."""
    index_path = get_journal_dir() / "index.json"
    try:
        with open(index_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        status("No journal index found. Create your first entry with 'ai-journal new'")
        sys.exit(1)


def save_index(index_data):
    """Save the journal index."""
    index_path = get_journal_dir() / "index.json"
    index_data["stats"]["last_modified"] = datetime.now().isoformat() + "Z"
    tmp_path = index_path.with_suffix(".json.tmp")
    with open(tmp_path, "w") as f:
        json.dump(index_data, f, indent=2)
        f.write("\n")
    tmp_path.replace(index_path)


def find_entry(search_term):
    """Find entry by ID, topic, or slug."""
    index_data = load_index()

    # Try to find by ID first
    try:
        entry_id = int(search_term)
        for entry in index_data["entries"]:
            if entry["id"] == entry_id:
                return entry
    except ValueError:
        pass

    # Try to find by exact topic match
    for entry in index_data["entries"]:
        if entry["topic"].lower() == search_term.lower():
            return entry

    # Try to find by slug match
    for entry in index_data["entries"]:
        if entry["slug"] == search_term.lower():
            return entry

    # Try partial topic match
    search_lower = search_term.lower()
    matches = []
    for entry in index_data["entries"]:
        if search_lower in entry["topic"].lower():
            matches.append(entry)

    if len(matches) == 1:
        return matches[0]
    elif len(matches) > 1:
        status(f"Multiple entries found matching '{search_term}'")
        for match in matches:
            print(f"  {match['id']}: {match['topic']} ({match['created'][:10]})")
        print("Please be more specific or use the entry ID.")
        sys.exit(1)

    return None


def get_latest_entry():
    """Get the most recently created entry."""
    index_data = load_index()
    if not index_data["entries"]:
        return None

    # Sort by creation date and return the latest
    latest = max(index_data["entries"], key=lambda x: x["created"])
    return latest


# Map friendly section names to the actual Markdown headers in an entry.
SECTION_HEADERS = {
    "reflection": "## Reflection",
    "key points": "## Key Points",
    "key": "## Key Points",
    "questions & answers": "## Questions & Answers",
    "q&a": "## Questions & Answers",
    "qa": "## Questions & Answers",
    "full session content": "## Full Session Content",
    "full session": "## Full Session Content",
    "full": "## Full Session Content",
}


def _is_placeholder(line):
    """True if a line is a leftover template hint (bracket or HTML comment)."""
    s = line.strip()
    return (s.startswith("[") and s.endswith("]")) or (
        s.startswith("<!--") and s.endswith("-->")
    )


def append_to_entry(entry, content, section="Reflection"):
    """Append content under the requested section of an existing entry."""
    journal_dir = get_journal_dir()
    entry_path = journal_dir / entry["filename"]

    if not entry_path.exists():
        status("Entry file not found", entry_path)
        sys.exit(1)

    # Read current content
    with open(entry_path, "r", encoding="utf-8") as f:
        current_content = f.read()

    # Create timestamp for the new content
    timestamp = datetime.now().strftime("%I:%M %p")
    new_block = ["", f"### Update - {timestamp}", "", content, ""]

    header = SECTION_HEADERS.get((section or "").lower().strip(), "## Reflection")
    lines = current_content.split("\n")

    # Locate the chosen section header.
    insert_idx = None
    for i, line in enumerate(lines):
        if line.strip() == header:
            insert_idx = i + 1
            break

    if insert_idx is None:
        # Section header missing: append to the end rather than lose the note.
        updated_content = (
            current_content.rstrip("\n") + "\n" + "\n".join(new_block) + "\n"
        )
    else:
        # Skip blank lines after the header, then remove one leftover
        # placeholder hint if present, so the section reads cleanly.
        j = insert_idx
        while j < len(lines) and lines[j].strip() == "":
            j += 1
        if j < len(lines) and _is_placeholder(lines[j]):
            del lines[j]
        rebuilt = lines[:insert_idx] + new_block + lines[insert_idx:]
        updated_content = "\n".join(rebuilt)

    # Write updated content
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(updated_content)

    # Update word count in index
    index_data = load_index()
    for i, indexed_entry in enumerate(index_data["entries"]):
        if indexed_entry["id"] == entry["id"]:
            index_data["entries"][i]["word_count"] = len(updated_content.split())
            break

    save_index(index_data)

    status("Added your note to", entry["topic"])
    status("Section", header.lstrip("# ").strip())
    status("File", entry_path)
    status("Time", timestamp)


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print(
            "Usage: python auto_append.py [entry_id|topic|'latest'] "
            "'<content>' [section]"
        )
        print("Examples:")
        print("  python auto_append.py latest 'New insight about tmux sessions'")
        print("  python auto_append.py 1 'Additional Q&A content'")
        print("  python auto_append.py 'Terminal Commands' 'New command learned'")
        sys.exit(1)

    search_term = sys.argv[1]

    # Get content from second argument or stdin
    if len(sys.argv) >= 3:
        content = sys.argv[2]
    elif not sys.stdin.isatty():
        content = sys.stdin.read().strip()
    else:
        status("No content provided. Provide content as argument or via stdin.")
        sys.exit(1)

    # Optional section parameter
    section = sys.argv[3] if len(sys.argv) > 3 else "Q&A"

    # Find entry
    if search_term.lower() == "latest":
        entry = get_latest_entry()
        if not entry:
            status("No entries found. Create your first entry with 'ai-journal new'")
            sys.exit(1)
    else:
        entry = find_entry(search_term)
        if not entry:
            status(f"No entry found matching '{search_term}'")
            print("Use 'ai-journal list' to see available entries")
            sys.exit(1)

    # Append content
    append_to_entry(entry, content, section)

    # Optionally open the entry
    if "--open" in sys.argv:
        entry_path = get_journal_dir() / entry["filename"]
        import subprocess

        subprocess.run(["open", str(entry_path)], check=False)


if __name__ == "__main__":
    main()
