#!/usr/bin/env python3
"""Append content to existing AI Journal entries."""

import json
import os
import re
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


def append_to_entry(entry, content, section="Q&A"):
    """Append content to an existing entry."""
    journal_dir = get_journal_dir()
    entry_path = journal_dir / entry["filename"]

    if not entry_path.exists():
        status("Entry file not found", entry_path)
        sys.exit(1)

    # Read current content
    with open(entry_path, "r") as f:
        current_content = f.read()

    # Create timestamp for the new content
    timestamp = datetime.now().strftime("%I:%M %p")

    # Format new content with timestamp
    new_content = f"\n### Update - {timestamp}\n\n{content}\n"

    # Find where to insert based on section
    if section.lower() == "q&a" or section.lower() == "qa":
        # Insert after "## Questions & Answers" section
        qa_pattern = r"(## Questions & Answers\n)"
        if re.search(qa_pattern, current_content):
            updated_content = re.sub(
                qa_pattern, f"\\1{new_content}\n", current_content, count=1
            )
        else:
            # If Q&A section doesn't exist, add before Follow-up Actions
            followup_pattern = r"(## Follow-up Actions)"
            if re.search(followup_pattern, current_content):
                updated_content = re.sub(
                    followup_pattern,
                    f"## Questions & Answers{new_content}\n\\1",
                    current_content,
                    count=1,
                )
            else:
                # Just append to the end
                updated_content = current_content + new_content
    else:
        # For other sections or general content, append to the end
        updated_content = current_content + new_content

    # Write updated content
    with open(entry_path, "w") as f:
        f.write(updated_content)

    # Update word count in index
    index_data = load_index()
    for i, indexed_entry in enumerate(index_data["entries"]):
        if indexed_entry["id"] == entry["id"]:
            index_data["entries"][i]["word_count"] = len(updated_content.split())
            break

    save_index(index_data)

    status("Appended content to", entry["topic"])
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
