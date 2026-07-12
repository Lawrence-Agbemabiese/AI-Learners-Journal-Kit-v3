import json
from pathlib import Path

from sqlite_index import rebuild, search, update_entry


def make_journal(tmp_path: Path) -> Path:
    journal = tmp_path / "AI-Journal"
    entry_dir = journal / "entries" / "2026" / "07"
    entry_dir.mkdir(parents=True)
    first = entry_dir / "20260711-python-functions.md"
    first.write_text(
        "# Python Functions\n\nFunctions make code reusable.\n", encoding="utf-8"
    )
    second = entry_dir / "20260710-docker-basics.md"
    second.write_text(
        "# Docker Basics\n\nContainers package applications.\n", encoding="utf-8"
    )
    (journal / "index.json").write_text(
        json.dumps(
            {
                "entries": [
                    {
                        "id": 1,
                        "topic": "Python Functions",
                        "filename": str(first.relative_to(journal)),
                        "created": "2026-07-11T10:00:00",
                        "tags": ["python", "beginner"],
                    },
                    {
                        "id": 2,
                        "topic": "Docker Basics",
                        "filename": str(second.relative_to(journal)),
                        "created": "2026-07-10T10:00:00",
                        "tags": ["docker"],
                    },
                ]
            }
        ),
        encoding="utf-8",
    )
    return journal


def test_rebuild_and_search_body(tmp_path):
    journal = make_journal(tmp_path)
    assert rebuild(journal) == 2
    results = search(journal, "reusable")
    assert [item.topic for item in results] == ["Python Functions"]


def test_search_tags(tmp_path):
    journal = make_journal(tmp_path)
    rebuild(journal)
    results = search(journal, "docker")
    assert results[0].id == 2


def test_update_entry_refreshes_body(tmp_path):
    journal = make_journal(tmp_path)
    rebuild(journal)
    entry = json.loads((journal / "index.json").read_text())["entries"][0]
    (journal / entry["filename"]).write_text(
        "# Python Functions\n\nDecorators wrap functions.\n", encoding="utf-8"
    )
    update_entry(journal, entry)
    assert search(journal, "decorators")[0].id == 1
