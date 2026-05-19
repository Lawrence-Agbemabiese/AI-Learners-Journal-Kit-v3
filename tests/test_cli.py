import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "scripts" / "journal_cli.py"
AI_INTEGRATION = ROOT / "scripts" / "ai_integration.py"


def run_cli(tmp_path, *args, check=True, env=None):
    command_env = os.environ.copy()
    command_env.update(
        {
            "AI_JOURNAL_DIR": str(tmp_path / "AI-Journal"),
            "PYTHONPATH": str(ROOT / "scripts"),
        }
    )
    command_env.pop("OPENAI_API_KEY", None)
    command_env.pop("ANTHROPIC_API_KEY", None)
    command_env.pop("GEMINI_API_KEY", None)
    if env:
        command_env.update(env)

    result = subprocess.run(
        [sys.executable, str(CLI), *args],
        text=True,
        capture_output=True,
        env=command_env,
        check=False,
    )
    if check and result.returncode != 0:
        raise AssertionError(
            f"Command failed: {result.args}\n"
            f"stdout:\n{result.stdout}\n"
            f"stderr:\n{result.stderr}"
        )
    return result


def read_index(tmp_path):
    return json.loads((tmp_path / "AI-Journal" / "index.json").read_text())


def test_new_list_limit_and_search(tmp_path):
    run_cli(tmp_path, "new", "First Topic", "one")
    run_cli(tmp_path, "new", "Second Topic", "two")

    listing = run_cli(tmp_path, "list", "--limit", "1").stdout
    assert "Second Topic" in listing
    assert "First Topic" not in listing

    search = run_cli(tmp_path, "search", "one").stdout
    assert "First Topic" in search
    assert "Second Topic" not in search


def test_append_and_open_print_path(tmp_path):
    run_cli(tmp_path, "new", "Append Target", "notes")
    run_cli(tmp_path, "append", "latest", "A useful addition")

    entry_path = Path(
        run_cli(tmp_path, "open", "latest", "--print-path").stdout.strip()
    )
    assert entry_path.exists()
    assert "A useful addition" in entry_path.read_text()


def test_entry_ids_are_not_reused_after_index_deletion(tmp_path):
    run_cli(tmp_path, "new", "First Topic")
    index_path = tmp_path / "AI-Journal" / "index.json"
    index = read_index(tmp_path)
    index["entries"] = []
    index["stats"]["total_entries"] = 0
    index_path.write_text(json.dumps(index))

    run_cli(tmp_path, "new", "Second Topic")
    index = read_index(tmp_path)
    assert index["entries"][0]["id"] == 2
    assert index["next_id"] == 3


def test_ai_integration_without_api_key_creates_manual_entry(tmp_path):
    env = os.environ.copy()
    env.update(
        {
            "AI_JOURNAL_DIR": str(tmp_path / "AI-Journal"),
            "PYTHONPATH": str(ROOT / "scripts"),
        }
    )
    env.pop("OPENAI_API_KEY", None)
    env.pop("ANTHROPIC_API_KEY", None)
    env.pop("GEMINI_API_KEY", None)

    result = subprocess.run(
        [sys.executable, str(AI_INTEGRATION), "What is testing?"],
        text=True,
        capture_output=True,
        env=env,
        check=False,
    )

    assert result.returncode == 0
    index = read_index(tmp_path)
    assert index["entries"][0]["topic"] == "What is testing?"
    assert "manual" in index["entries"][0]["tags"]
