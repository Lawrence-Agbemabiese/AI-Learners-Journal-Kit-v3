#!/bin/bash
# Double-click launcher for the friendly AI Journal WEB UI.
# Starts a tiny local server and opens it in your browser.

set -euo pipefail

LAUNCHER_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Starting AI Journal (web)…"
echo "Your browser will open automatically. Keep this window open while you write."
echo "When you're done, click this window and press Ctrl-C to stop."
echo ""

python3 "$LAUNCHER_DIR/scripts/web_server.py"
