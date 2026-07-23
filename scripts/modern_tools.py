#!/usr/bin/env python3
"""User-friendly maintenance commands for AI Learner's Journal."""
from __future__ import annotations

import json
import os
import sqlite3
import sys
import zipfile
from datetime import datetime
from pathlib import Path

from sqlite_index import database_path, rebuild, search


def journal_dir() -> Path:
    return Path(
        os.environ.get("AI_JOURNAL_DIR", Path.home() / "AI-Journal")
    ).expanduser()


def doctor() -> int:
    root = journal_dir()
    checks = []
    checks.append(("Journal folder", root.exists(), str(root)))
    index = root / "index.json"
    checks.append(("Journal index", index.exists(), str(index)))
    if index.exists():
        try:
            data = json.loads(index.read_text(encoding="utf-8"))
            valid = isinstance(data.get("entries", []), list)
            detail = (
                f"{len(data.get('entries', []))} entries" if valid else "invalid format"
            )
        except (OSError, json.JSONDecodeError) as exc:
            valid, detail = False, str(exc)
        checks.append(("Index contents", valid, detail))
    checks.append(
        ("Entries folder", (root / "entries").exists(), str(root / "entries"))
    )
    checks.append(("Python", sys.version_info >= (3, 9), sys.version.split()[0]))
    print("AI Journal setup check\n")
    for label, ok, detail in checks:
        print(f"{'✓' if ok else '✗'} {label}: {detail}")
    failed = [item for item in checks if not item[1]]
    if failed:
        print(
            "\nSome checks need attention. Running `ai-journal setup` may repair folders."
        )
        return 1
    print("\nEverything looks ready.")
    return 0


def reindex() -> int:
    root = journal_dir()
    try:
        count = rebuild(root)
    except sqlite3.OperationalError as exc:
        print(f"Could not build the fast search database here ({exc}).")
        print("This can happen on network drives or USB sticks.")
        print("Basic search still works: ai-journal search \"<word>\"")
        return 1
    print(f"Search index rebuilt: {count} entries")
    print(f"Database: {database_path(root)}")
    return 0


def search_command(query: str, limit: int = 20) -> int:
    try:
        results = search(journal_dir(), query, limit)
    except sqlite3.OperationalError:
        # SQLite can fail on network drives / USB sticks. Fall back to the
        # plain full-text scan so the learner still gets an answer.
        from journal_cli import format_entry, search_entries

        matches = search_entries(query)[: max(1, limit)]
        if not matches:
            print(f'No journal entries matched "{query}".')
            return 0
        print(f'{len(matches)} result(s) for "{query}" (basic search)\n')
        for entry, snippet in matches:
            print(format_entry(entry))
            if snippet:
                print(f"      > {snippet}")
        return 0
    if not results:
        print(f'No journal entries matched "{query}".')
        return 0
    print(f'{len(results)} result(s) for "{query}"\n')
    for result in results:
        tags = ", ".join(result.tags) or "untagged"
        print(f"{result.id:>3}  {result.created[:10]}  {result.topic}")
        print(f"     Tags: {tags}")
        if result.snippet:
            print(f"     {result.snippet}")
    return 0


def backup(destination: str | None = None) -> int:
    root = journal_dir()
    if not root.exists():
        print(f"Journal folder not found: {root}", file=sys.stderr)
        return 1
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    target = (
        Path(destination).expanduser()
        if destination
        else Path.home() / f"AI-Journal-backup-{stamp}.zip"
    )
    target.parent.mkdir(parents=True, exist_ok=True)
    db_name = database_path(root).name
    with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in root.rglob("*"):
            # Skip the rebuildable search database (and its -wal/-shm
            # sidecars) plus interrupted temp writes.
            if not path.is_file():
                continue
            if path.name.startswith(db_name) or path.name.endswith(".tmp"):
                continue
            archive.write(path, path.relative_to(root.parent))
    print(f"Backup created: {target}")
    return 0
