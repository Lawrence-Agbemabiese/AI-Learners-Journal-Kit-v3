import json
import os
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "scripts" / "journal_cli.py"
AI_INTEGRATION = ROOT / "scripts" / "ai_integration.py"
BUILD_RELEASE = ROOT / "scripts" / "build_release.py"


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


def test_interactive_new_prompts_for_topic_and_tags(tmp_path):
    result = run_cli_with_input(tmp_path, "Prompted Topic\nlearning notes\n", "new")

    assert result.returncode == 0
    index = read_index(tmp_path)
    assert index["entries"][0]["topic"] == "Prompted Topic"
    assert index["entries"][0]["tags"] == ["learning", "notes"]


def test_interactive_append_prompts_for_content(tmp_path):
    run_cli(tmp_path, "new", "Prompt Append")
    # Interactive append now: confirm target (Enter = yes), enter content,
    # blank line to finish, then choose a section (Enter = Reflection).
    result = run_cli_with_input(
        tmp_path,
        "\nFirst prompted line\nSecond prompted line\n\n\n",
        "append",
        "latest",
    )

    assert result.returncode == 0
    entry_path = Path(
        run_cli(tmp_path, "open", "latest", "--print-path").stdout.strip()
    )
    assert "First prompted line\nSecond prompted line" in entry_path.read_text()


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


def _run_ai_integration(tmp_path, question):
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

    return subprocess.run(
        [sys.executable, str(AI_INTEGRATION), question],
        text=True,
        capture_output=True,
        env=env,
        check=False,
    )


def test_ai_integration_without_api_key_saves_followup_entry(tmp_path):
    # No key + no canned answer: do not dead-end; save the question to revisit.
    result = _run_ai_integration(tmp_path, "How do I scale a Kubernetes cluster?")

    assert result.returncode == 0
    index = read_index(tmp_path)
    assert index["entries"][0]["topic"] == "How do I scale a Kubernetes cluster?"
    assert "unanswered" in index["entries"][0]["tags"]
    result.stdout.encode("ascii")


def test_ai_integration_starter_brain_answers_common_question(tmp_path):
    # No key but a known beginner concept: answered offline and saved.
    result = _run_ai_integration(tmp_path, "What is an API?")

    assert result.returncode == 0
    assert "Starter Guide" in result.stdout
    index = read_index(tmp_path)
    assert "starter-guide" in index["entries"][0]["tags"]
    result.stdout.encode("ascii")


def test_compare_command_is_not_advertised(tmp_path):
    help_text = run_cli(tmp_path, "--help").stdout

    assert "compare" not in help_text


def test_cli_output_is_ascii_safe_for_captured_windows_output(tmp_path):
    result = run_cli(tmp_path, "new", "Encoding Safe Topic", "windows")

    result.stdout.encode("ascii")
    assert "Created new entry" in result.stdout


def test_release_builder_creates_customer_package():
    version = "pytest-smoke"
    result = subprocess.run(
        [sys.executable, str(BUILD_RELEASE), "--version", version, "--allow-dirty"],
        text=True,
        capture_output=True,
        cwd=ROOT,
        check=False,
    )

    assert result.returncode == 0, result.stderr

    package_name = f"ai-learners-journal-kit-{version}"
    zip_path = ROOT / "dist" / f"{package_name}.zip"
    manifest_path = ROOT / "dist" / "release-manifest.json"
    checksums_path = ROOT / "dist" / "SHA256SUMS.txt"

    assert zip_path.exists()
    assert manifest_path.exists()
    assert checksums_path.exists()

    with zipfile.ZipFile(zip_path) as archive:
        names = set(archive.namelist())

    required = {
        f"{package_name}/README.md",
        f"{package_name}/LICENSE",
        f"{package_name}/SUPPORT.md",
        f"{package_name}/PRIVACY.md",
        f"{package_name}/REFUND_POLICY.md",
        f"{package_name}/SECURITY.md",
        f"{package_name}/CHANGELOG.md",
        f"{package_name}/docs/Quick_Start_v3.md",
        f"{package_name}/installers/Installer.command",
        f"{package_name}/installers/Installer.bat",
    }
    assert required.issubset(names)
    assert not any("/.git/" in name or "/dist/" in name for name in names)


def run_cli_with_input(tmp_path, user_input, *args):
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

    return subprocess.run(
        [sys.executable, str(CLI), *args],
        input=user_input,
        text=True,
        capture_output=True,
        env=command_env,
        check=False,
    )
