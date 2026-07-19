#!/usr/bin/env python3
"""Create AI Journal entries and maintain the searchable index."""

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
        # Create default index if it doesn't exist
        default_index = {
            "version": "3.0",  # Updated version for AI integration
            "created": datetime.now().isoformat() + "Z",
            "entries": [],
            "tags": {},
            "ai_stats": {  # New AI-specific statistics
                "total_ai_assisted": 0,
                "sources_used": {},
                "avg_quality_rating": 0.0,
            },
            "stats": {
                "total_entries": 0,
                "last_modified": datetime.now().isoformat() + "Z",
            },
        }
        save_index(default_index)
        return default_index


def save_index(index_data):
    """Save the journal index."""
    index_path = get_journal_dir() / "index.json"
    index_path.parent.mkdir(parents=True, exist_ok=True)
    index_data["stats"]["last_modified"] = datetime.now().isoformat() + "Z"
    tmp_path = index_path.with_suffix(".json.tmp")
    with open(tmp_path, "w") as f:
        json.dump(index_data, f, indent=2)
        f.write("\n")
    tmp_path.replace(index_path)


def create_slug(topic):
    """Create a URL-friendly slug from a topic."""
    # Convert to lowercase, replace spaces and special chars with hyphens
    slug = re.sub(r"[^\w\s-]", "", topic.lower())
    slug = re.sub(r"[-\s]+", "-", slug)
    return slug.strip("-")


def create_entry(topic, content=None, tags=None, ai_metadata=None):
    """Create a new journal entry with optional AI metadata."""
    if tags is None:
        tags = []

    now = datetime.now()
    slug = create_slug(topic)

    # Create entry filename with date and slug
    entry_filename = f"{now.strftime('%Y%m%d')}-{slug}.md"

    # Create year/month directory structure
    entry_dir = get_journal_dir() / "entries" / now.strftime("%Y") / now.strftime("%m")
    entry_dir.mkdir(parents=True, exist_ok=True)

    entry_path = entry_dir / entry_filename

    # Handle duplicate entries intelligently
    if entry_path.exists():
        print(f"Entry already exists: {entry_path}")

        # If it's a similar topic, suggest variations
        variations = [
            topic.replace("what is", "what is an").replace(
                "what is an an", "what is an"
            ),
            topic.replace("what is an", "what is"),
            topic + " detailed",
            topic + " advanced",
            topic.replace("?", " explained?") if "?" in topic else topic + " explained",
        ]

        for variation in variations:
            var_slug = create_slug(variation)
            var_filename = f"{now.strftime('%Y%m%d')}-{var_slug}.md"
            var_path = entry_dir / var_filename

            if not var_path.exists():
                # create_entry announces the new entry itself; no print here.
                return create_entry(variation, content, tags, ai_metadata)

        return str(entry_path)

    # Create enhanced entry content with AI metadata
    content_sections = []

    # Header
    content_sections.append(f"# {topic}")
    content_sections.append("")

    # Metadata section
    metadata_lines = [
        f"**Date:** {now.strftime('%B %d, %Y')}",
        f"**Time:** {now.strftime('%I:%M %p')}",
        f"**Tags:** {', '.join(tags) if tags else 'untagged'}",
    ]

    # Add AI metadata if present
    if ai_metadata:
        if ai_metadata.get("source"):
            metadata_lines.append(f"**AI Source:** {ai_metadata['source']}")
        if ai_metadata.get("quality_rating"):
            metadata_lines.append(
                f"**Review Score:** {ai_metadata['quality_rating']}/10"
            )
            metadata_lines.append(
                "**Review Score Note:** This estimates structure and completeness, "
                "not factual correctness."
            )
        if ai_metadata.get("confidence"):
            metadata_lines.append(
                f"**Confidence:** {ai_metadata['confidence'].title()}"
            )
        if ai_metadata.get("risk_level"):
            metadata_lines.append(
                f"**Risk Level:** {ai_metadata['risk_level'].title()}"
            )

    content_sections.extend(metadata_lines)
    content_sections.append("")

    # Main content or template
    if content:
        content_sections.append(content)
    else:
        # Default template.
        # NOTE: guidance hints use HTML comments (<!-- ... -->) so they are
        # invisible when the note is rendered as Markdown. This keeps empty
        # entries looking clean (portfolio-ready) while still guiding the
        # writer in the raw file. Hints are removed automatically as each
        # section gets real content (see auto_append.append_to_entry).
        template = """## Key Points

<!-- One or two big things you learned. Delete this line as you fill it in. -->

## Questions & Answers

<!-- Questions you asked and the answers you found. -->

## Follow-up Actions

<!-- - [ ] Your next step -->

---

## Full Session Content

<!-- Your detailed notes, commands you ran, and what happened. -->

---

## Reflection

<!-- What did you learn? What confused you? What will you try next? -->"""
        content_sections.append(template)

    entry_content = "\n".join(content_sections)

    # Write the entry
    with open(entry_path, "w") as f:
        f.write(entry_content)

    # Update index with enhanced metadata
    index_data = load_index()

    next_id = index_data.get("next_id")
    if next_id is None:
        existing_ids = [entry.get("id", 0) for entry in index_data["entries"]]
        next_id = max(existing_ids, default=0) + 1

    entry_record = {
        "id": next_id,
        "topic": topic,
        "slug": slug,
        "filename": str(entry_path.relative_to(get_journal_dir())),
        "created": now.isoformat() + "Z",
        "tags": tags,
        "word_count": len(entry_content.split()),
    }
    index_data["next_id"] = next_id + 1

    # Add AI metadata to entry record
    if ai_metadata:
        if ai_metadata.get("session_id"):
            # Lets importers recognize a session they have already imported.
            entry_record["session_id"] = ai_metadata["session_id"]
        entry_record["ai_sources"] = [ai_metadata.get("source", "unknown")]
        entry_record["quality_rating"] = ai_metadata.get("quality_rating", 0)
        entry_record["confidence"] = ai_metadata.get("confidence", "medium")
        entry_record["risk_level"] = ai_metadata.get("risk_level", "low")
        entry_record["verification_status"] = ai_metadata.get(
            "verification_status", "untested"
        )

        # Update AI statistics
        if "ai_stats" not in index_data:
            index_data["ai_stats"] = {
                "total_ai_assisted": 0,
                "sources_used": {},
                "avg_quality_rating": 0.0,
            }

        index_data["ai_stats"]["total_ai_assisted"] += 1
        source = ai_metadata.get("source", "unknown")
        if source in index_data["ai_stats"]["sources_used"]:
            index_data["ai_stats"]["sources_used"][source] += 1
        else:
            index_data["ai_stats"]["sources_used"][source] = 1

        # Update average review score. Keep the JSON key for compatibility.
        total_ai = index_data["ai_stats"]["total_ai_assisted"]
        current_avg = index_data["ai_stats"]["avg_quality_rating"]
        new_rating = ai_metadata.get("quality_rating", 5)
        index_data["ai_stats"]["avg_quality_rating"] = (
            (current_avg * (total_ai - 1)) + new_rating
        ) / total_ai

    index_data["entries"].append(entry_record)
    index_data["stats"]["total_entries"] += 1

    # Update tag counts
    for tag in tags:
        if tag in index_data["tags"]:
            index_data["tags"][tag] += 1
        else:
            index_data["tags"][tag] = 1

    save_index(index_data)

    status("Created new entry", entry_path)
    status("Topic", topic)
    status("Tags", ", ".join(tags) if tags else "untagged")

    # Show AI metadata if present
    if ai_metadata:
        if ai_metadata.get("source"):
            status("AI Source", ai_metadata["source"])
        if ai_metadata.get("quality_rating"):
            review_bar = "#" * ai_metadata["quality_rating"] + "-" * (
                10 - ai_metadata["quality_rating"]
            )
            status("Review Score", f"{review_bar} ({ai_metadata['quality_rating']}/10)")

    return str(entry_path)


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python entry_saver.py '<topic>' [tags...]")
        print("Example: python entry_saver.py 'Terminal Commands' tmux bash")
        sys.exit(1)

    topic = sys.argv[1]
    tags = sys.argv[2:] if len(sys.argv) > 2 else []

    # Read content from stdin if available
    content = None
    if not sys.stdin.isatty():
        content = sys.stdin.read().strip()

    entry_path = create_entry(topic, content, tags)

    # Optionally open the entry in default editor
    if "--open" in sys.argv:
        import subprocess

        subprocess.run(["open", str(entry_path)], check=False)


if __name__ == "__main__":
    main()
