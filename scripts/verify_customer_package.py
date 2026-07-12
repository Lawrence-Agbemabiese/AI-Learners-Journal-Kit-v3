#!/usr/bin/env python3
"""Verify that a customer release archive contains novice-first onboarding."""

from __future__ import annotations

import sys
import zipfile
from pathlib import Path

REQUIRED_SUFFIXES = (
    "START HERE - AI Journal.command",
    "START HERE - AI Journal.bat",
    "START_HERE.md",
    "README.md",
    "README.txt",
    "docs/Quick_Start_v3.md",
    "docs/Storefront_Distribution_Checklist.md",
    "SUPPORT.md",
    "PRIVACY.md",
    "SECURITY.md",
    "REFUND_POLICY.md",
    "Start AI Journal (Web).command",
    "Start AI Journal (Web).bat",
    "scripts/web_server.py",
    "web/index.html",
)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/verify_customer_package.py <release.zip>")
        return 2

    archive_path = Path(sys.argv[1])
    if not archive_path.is_file():
        print(f"Archive not found: {archive_path}")
        return 2

    with zipfile.ZipFile(archive_path) as archive:
        names = archive.namelist()

    missing = [
        required
        for required in REQUIRED_SUFFIXES
        if not any(name.endswith(required) for name in names)
    ]

    if missing:
        print("Customer package verification FAILED.")
        print("Missing required files:")
        for item in missing:
            print(f"  - {item}")
        return 1

    print("Customer package verification passed.")
    print(f"Checked {len(REQUIRED_SUFFIXES)} novice-first requirements.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
