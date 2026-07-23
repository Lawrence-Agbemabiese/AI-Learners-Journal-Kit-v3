#!/usr/bin/env python3
"""Delete AI Journal entries safely.

Design:
  - Soft delete (default): the entry's Markdown file moves to
    ``<journal>/trash/`` and the entry is removed from index.json. Nothing is
    destroyed; a learner (or support) can restore the file by hand and run
    ``ai-journal reindex``. A small ``trash/trash-index.json`` keeps the
    original index record + original path to make restores easy.
  - Purge: the file is permanently removed. Used for the explicit
    ``ai-journal delete --purge`` path only, always behind a confirmation.

After either operation the JSON index and (via mtime detection plus an
explicit row removal) the optional SQLite search index stay consistent.
"""

import json
import os
from datetime import datetime
from pathlib import Path

from auto_append import load_index, save_index


def get_journal_dir():
    """Get the AI Journal directory path."""
    return Path(os.environ.get("AI_JOURNAL_DIR", Path.home() / "AI-Journal"))


def trash_dir():
    """Folder deleted entries are moved to (inside the journal, visible)."""
    return get_journal_dir() / "trash"


def _trash_log_path():
    return trash_dir() / "trash-index.json"


def _load_trash_log():
    try:
        return json.loads(_trash_log_path().read_text(encoding="utf-8")) or []
    except (OSError, ValueError):
        return []


def _save_trash_log(log):
    trash_dir().mkdir(parents=True, exist_ok=True)
    tmp = _trash_log_path().with_suffix(".json.tmp")
    tmp.write_text(
        json.dumps(log, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    tmp.replace(_trash_log_path())


def _remove_from_index(entry):
    """Remove one entry record from index.json and fix the derived counters."""
    index_data = load_index()
    kept = [e for e in index_data["entries"] if e.get("id") != entry.get("id")]
    if len(kept) == len(index_data["entries"]):
        return False  # nothing removed (already gone)
    index_data["entries"] = kept
    index_data["stats"]["total_entries"] = len(kept)

    # Keep tag counts in step with the entries that remain.
    for tag in entry.get("tags", []) or []:
        if tag in index_data.get("tags", {}):
            index_data["tags"][tag] -= 1
            if index_data["tags"][tag] <= 0:
                del index_data["tags"][tag]

    save_index(index_data)
    return True


def _remove_from_search_db(entry):
    """Drop the entry from the optional SQLite search index, if it exists."""
    journal = get_journal_dir()
    try:
        from sqlite_index import database_path, remove_entry

        if database_path(journal).exists():
            remove_entry(journal, int(entry["id"]))
    except Exception:
        # The search DB is rebuildable; a failed row-delete only means the
        # next search triggers an automatic rebuild.
        pass


def delete_entry(entry, purge=False):
    """Delete an entry. Returns the trash path (soft) or None (purge).

    ``entry`` is an index record (dict with id/filename/topic). Confirmation
    is the caller's job - this function just does the work.
    """
    journal = get_journal_dir()
    entry_path = journal / entry["filename"]
    trashed_to = None

    if purge:
        if entry_path.exists():
            entry_path.unlink()
    else:
        trash_dir().mkdir(parents=True, exist_ok=True)
        if entry_path.exists():
            stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            target = trash_dir() / f"{stamp}-{entry_path.name}"
            n = 2
            while target.exists():
                target = trash_dir() / f"{stamp}-{n}-{entry_path.name}"
                n += 1
            entry_path.replace(target)
            trashed_to = target

        log = _load_trash_log()
        log.append(
            {
                "deleted_at": datetime.now().isoformat(),
                "trash_file": (trashed_to.name if trashed_to else None),
                "original_path": entry["filename"],
                "entry": entry,
            }
        )
        _save_trash_log(log)

    _remove_from_index(entry)
    _remove_from_search_db(entry)
    return str(trashed_to) if trashed_to else None
