# Modernization implementation

This change keeps Markdown and `index.json` compatible while adding a rebuildable SQLite FTS5 search database.

## Integration points

Add these commands to `scripts/journal_cli.py`:

- `ai-journal doctor` → `modern_tools.doctor()`
- `ai-journal reindex` → `modern_tools.reindex()`
- `ai-journal find <query>` → `modern_tools.search_command(query, limit)`
- `ai-journal backup [destination]` → `modern_tools.backup(destination)`

After creating or appending an entry, call `sqlite_index.update_entry(get_journal_dir(), entry)`. Treat index-update failures as non-fatal because Markdown remains authoritative.

## Why an additive index

- Existing journals continue to work unchanged.
- Search can be rebuilt after corruption or upgrades.
- SQLite transactions reduce partial-write risk.
- FTS5 provides ranked, Unicode-aware full-text search without running a separate service.

## Installation

```bash
uv tool install .
ai-journal
```

For development:

```bash
uv sync --extra dev
uv run pytest
uv run ruff check .
```
