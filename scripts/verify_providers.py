#!/usr/bin/env python3
"""Quick health check for the AI providers used by AI Journal.

Run it on YOUR machine with your own keys. Keys are read from environment
variables and from your saved ~/.ai-journal-config.json. They are never printed
or sent anywhere except straight to each provider for the test call.

It uses the exact same code path the app uses (ai_integration.live_answer), so
a PASS here means the app's "Save & test" will work for that provider too.

Usage:
    python3 scripts/verify_providers.py
"""

import os
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from ai_integration import PROVIDERS, live_answer, load_config  # noqa: E402


def collect_keys() -> dict:
    """Find a key for each provider from env vars, then saved config."""
    keys = {}
    cfg_keys = load_config().get("api_keys") or {}
    for pid, meta in PROVIDERS.items():
        key = os.getenv(meta["env"]) or cfg_keys.get(pid)
        if key:
            keys[pid] = key
    return keys


def main() -> int:
    keys = collect_keys()
    if not keys:
        print("No provider keys found in your environment or saved config.")
        print("Set one and run again, e.g.:  export GEMINI_API_KEY=your-key-here")
        return 1

    print("Testing each provider that has a key configured...\n")
    failures = 0
    for pid, meta in PROVIDERS.items():
        label = meta["label"]
        model = meta["model"]
        if pid not in keys:
            print(f"  {label:9} SKIP  (no key found)")
            continue
        try:
            answer = live_answer(
                "Reply with the single word: OK", pid, keys[pid], timeout=20
            )
            verdict = "PASS " if "OK" in answer.upper() else "PASS?"
            print(f"  {label:9} {verdict} ({model})  ->  {answer.strip()[:40]}")
        except Exception as exc:  # noqa: BLE001 - surface any provider error
            failures += 1
            print(f"  {label:9} FAIL  ({model})  ->  {exc}")

    print()
    if failures:
        print(f"{failures} provider(s) failed. See the messages above.")
        return 1
    print("All configured providers passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
