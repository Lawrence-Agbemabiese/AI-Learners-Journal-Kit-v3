#!/usr/bin/env python3
"""Rebuildable SQLite full-text index for AI Learner's Journal.

Markdown remains the source of truth. The database can always be deleted and
rebuilt from index.json plus the entry files.
"""
from __future__ import annotations

import json
import sqlite3
from dataclasses import dataclass
from pathlib import Path

SCHEMA_VERSION = 1


@dataclass(frozen=True)
class SearchResult:
    id: int
    topic: str
    filename: str
    created: str
    tags: tuple[str, ...]
    snippet: str
    rank: float


def database_path(journal_dir: Path) -> Path:
    return journal_dir / "journal-search.sqlite3"


def connect(journal_dir: Path) -> sqlite3.Connection:
    journal_dir.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(database_path(journal_dir))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def initialize(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS metadata (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY,
            topic TEXT NOT NULL,
            filename TEXT NOT NULL UNIQUE,
            created TEXT NOT NULL,
            tags_json TEXT NOT NULL,
            body TEXT NOT NULL
        );
        CREATE VIRTUAL TABLE IF NOT EXISTS entries_fts USING fts5(
            entry_id UNINDEXED,
            topic,
            tags,
            body,
            tokenize='unicode61 remove_diacritics 2'
        );
        """
    )
    conn.execute(
        "INSERT OR REPLACE INTO metadata(key, value) VALUES('schema_version', ?)",
        (str(SCHEMA_VERSION),),
    )
    conn.commit()


def _read_index(journal_dir: Path) -> list[dict]:
    path = journal_dir / "index.json"
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Cannot read {path}: {exc}") from exc
    entries = data.get("entries", [])
    if not isinstance(entries, list):
        raise RuntimeError(f"Invalid journal index: {path}")
    return entries


def rebuild(journal_dir: Path) -> int:
    """Rebuild the search database. Returns the number of indexed entries."""
    conn = connect(journal_dir)
    try:
        initialize(conn)
        conn.execute("DELETE FROM entries")
        conn.execute("DELETE FROM entries_fts")
        count = 0
        for item in _read_index(journal_dir):
            try:
                entry_id = int(item["id"])
                filename = str(item["filename"])
                topic = str(item.get("topic") or "Untitled")
                created = str(item.get("created") or "")
            except (KeyError, TypeError, ValueError):
                continue
            tags = item.get("tags") or []
            if not isinstance(tags, list):
                tags = [str(tags)]
            path = journal_dir / filename
            try:
                body = path.read_text(encoding="utf-8")
            except OSError:
                body = ""
            tags_json = json.dumps(tags)
            conn.execute(
                """
                INSERT INTO entries(id, topic, filename, created, tags_json, body)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (entry_id, topic, filename, created, tags_json, body),
            )
            conn.execute(
                "INSERT INTO entries_fts(entry_id, topic, tags, body) VALUES (?, ?, ?, ?)",
                (entry_id, topic, " ".join(str(tag) for tag in tags), body),
            )
            count += 1
        conn.commit()
        return count
    finally:
        conn.close()


def needs_rebuild(journal_dir: Path) -> bool:
    """Return True when Markdown/index data is newer than the search database."""
    db = database_path(journal_dir)
    if not db.exists():
        return True
    try:
        db_mtime = db.stat().st_mtime
    except OSError:
        return True
    index_path = journal_dir / "index.json"
    try:
        if index_path.stat().st_mtime > db_mtime:
            return True
    except OSError:
        return False
    for item in _read_index(journal_dir):
        filename = item.get("filename")
        if not filename:
            continue
        try:
            if (journal_dir / str(filename)).stat().st_mtime > db_mtime:
                return True
        except OSError:
            continue
    return False


def _fts_query(text: str) -> str:
    tokens = [token.replace('"', '""') for token in text.split() if token.strip()]
    return " AND ".join(f'"{token}"*' for token in tokens)


def search(journal_dir: Path, query: str, limit: int = 20) -> list[SearchResult]:
    query = query.strip()
    if not query:
        return []
    if needs_rebuild(journal_dir):
        rebuild(journal_dir)
    conn = connect(journal_dir)
    try:
        initialize(conn)
        rows = conn.execute(
            """
            SELECT e.id, e.topic, e.filename, e.created, e.tags_json,
                   snippet(entries_fts, 3, '[', ']', ' … ', 18) AS snippet,
                   bm25(entries_fts, 0.0, 6.0, 3.0, 1.0) AS rank
            FROM entries_fts
            JOIN entries e ON e.id = CAST(entries_fts.entry_id AS INTEGER)
            WHERE entries_fts MATCH ?
            ORDER BY rank, e.created DESC
            LIMIT ?
            """,
            (_fts_query(query), max(1, min(limit, 200))),
        ).fetchall()
        return [
            SearchResult(
                id=row["id"],
                topic=row["topic"],
                filename=row["filename"],
                created=row["created"],
                tags=tuple(json.loads(row["tags_json"])),
                snippet=row["snippet"] or "",
                rank=float(row["rank"]),
            )
            for row in rows
        ]
    finally:
        conn.close()


def update_entry(journal_dir: Path, entry: dict) -> None:
    """Upsert one entry after create/append without rebuilding everything."""
    conn = connect(journal_dir)
    try:
        initialize(conn)
        filename = str(entry["filename"])
        path = journal_dir / filename
        try:
            body = path.read_text(encoding="utf-8")
        except OSError:
            body = ""
        tags = entry.get("tags") or []
        entry_id = int(entry["id"])
        topic = str(entry.get("topic") or "Untitled")
        tags_json = json.dumps(tags)
        conn.execute(
            """
            INSERT INTO entries(id, topic, filename, created, tags_json, body)
            VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET
                topic=excluded.topic,
                filename=excluded.filename,
                created=excluded.created,
                tags_json=excluded.tags_json,
                body=excluded.body
            """,
            (
                entry_id,
                topic,
                filename,
                str(entry.get("created") or ""),
                tags_json,
                body,
            ),
        )
        conn.execute("DELETE FROM entries_fts WHERE entry_id = ?", (entry_id,))
        conn.execute(
            "INSERT INTO entries_fts(entry_id, topic, tags, body) VALUES (?, ?, ?, ?)",
            (entry_id, topic, " ".join(str(tag) for tag in tags), body),
        )
        conn.commit()
    finally:
        conn.close()
