#!/usr/bin/env python3
"""Build customer-ready release archives and checksums."""

import argparse
import hashlib
import json
import subprocess
import tarfile
import zipfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"

EXCLUDED_DIRS = {
    ".git",
    ".github",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    "__pycache__",
    "dist",
    "test-install",
}

EXCLUDED_SUFFIXES = {
    ".pyc",
    ".pyo",
    ".tmp",
}

EXCLUDED_FILES = {
    ".DS_Store",
    "bandit-medium-high.json",
}

REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
    "SUPPORT.md",
    "PRIVACY.md",
    "REFUND_POLICY.md",
    "SECURITY.md",
    "ai-journal",
    "requirements.txt",
    "installers/Installer.command",
    "installers/Installer.bat",
    "installers/install_ai_journal_v3.sh",
    "docs/Quick_Start_v3.md",
    "docs/Workshop_Facilitator_Guide.md",
    "docs/Paid_Product_Checklist.md",
    "docs/Release_Checklist.md",
    "docs/Release_Notes_v3.0.1.md",
]


def run_git(args):
    """Run a git command and return stripped stdout."""
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout.strip()


def assert_clean_tree(allow_dirty):
    """Fail release builds from dirty worktrees unless explicitly allowed."""
    if allow_dirty:
        return
    status = run_git(["status", "--porcelain"])
    if status:
        raise SystemExit(
            "Working tree is not clean. Commit or stash changes, or use --allow-dirty "
            "for local smoke-test builds."
        )


def validate_required_files():
    """Ensure the paid/beta package contains the expected public surface."""
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).exists()]
    if missing:
        raise SystemExit("Missing required release files:\n" + "\n".join(missing))


def should_include(path):
    """Return true when a path should be packaged."""
    if any(part in EXCLUDED_DIRS for part in path.parts):
        return False
    if path.name in EXCLUDED_FILES:
        return False
    if path.suffix in EXCLUDED_SUFFIXES:
        return False
    return path.is_file()


def collect_files():
    """Collect package files in deterministic order."""
    files = []
    for path in ROOT.rglob("*"):
        relative = path.relative_to(ROOT)
        if should_include(relative):
            files.append(relative)
    return sorted(files, key=lambda item: item.as_posix())


def sha256(path):
    """Compute SHA256 for a file."""
    digest = hashlib.sha256()
    with open(path, "rb") as file_obj:
        for chunk in iter(lambda: file_obj.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_zip(output_path, files, package_root):
    """Write a deterministic ZIP archive."""
    with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for relative in files:
            archive.write(ROOT / relative, f"{package_root}/{relative.as_posix()}")


def write_tar(output_path, files, package_root):
    """Write a gzip-compressed tar archive."""
    with tarfile.open(output_path, "w:gz") as archive:
        for relative in files:
            archive.add(
                ROOT / relative, arcname=f"{package_root}/{relative.as_posix()}"
            )


def write_checksums(paths):
    """Write SHA256SUMS.txt for release artifacts."""
    checksum_path = DIST / "SHA256SUMS.txt"
    lines = [f"{sha256(path)}  {path.name}" for path in paths]
    checksum_path.write_text("\n".join(lines) + "\n")
    return checksum_path


def write_manifest(version, files, artifacts):
    """Write machine-readable release metadata."""
    try:
        commit = run_git(["rev-parse", "HEAD"])
    except (subprocess.CalledProcessError, FileNotFoundError):
        commit = "unknown"

    manifest = {
        "product": "AI Learner's Journal Kit",
        "version": version,
        "commit": commit,
        "built_at": datetime.now(timezone.utc).isoformat(),
        "artifacts": [
            {
                "name": artifact.name,
                "sha256": sha256(artifact),
                "bytes": artifact.stat().st_size,
            }
            for artifact in artifacts
        ],
        "file_count": len(files),
        "required_files": REQUIRED_FILES,
    }
    manifest_path = DIST / "release-manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
    return manifest_path


def main():
    """Build release archives."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", required=True, help="Release version, e.g. v3.0.1")
    parser.add_argument(
        "--allow-dirty",
        action="store_true",
        help="Allow local smoke-test builds from a dirty working tree",
    )
    args = parser.parse_args()

    version = args.version.lstrip()
    package_root = f"ai-learners-journal-kit-{version}"

    assert_clean_tree(args.allow_dirty)
    validate_required_files()

    DIST.mkdir(exist_ok=True)
    files = collect_files()

    zip_path = DIST / f"{package_root}.zip"
    tar_path = DIST / f"{package_root}.tar.gz"

    write_zip(zip_path, files, package_root)
    write_tar(tar_path, files, package_root)
    checksum_path = write_checksums([zip_path, tar_path])
    manifest_path = write_manifest(version, files, [zip_path, tar_path])

    print(f"Built {zip_path}")
    print(f"Built {tar_path}")
    print(f"Wrote {checksum_path}")
    print(f"Wrote {manifest_path}")


if __name__ == "__main__":
    main()
