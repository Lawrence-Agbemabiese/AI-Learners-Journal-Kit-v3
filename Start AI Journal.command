#!/bin/bash
# Double-click launcher for the beginner AI Journal menu.

set -euo pipefail

LAUNCHER_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ -x "$HOME/bin/ai-journal" ]; then
    "$HOME/bin/ai-journal" menu
elif [ -x "$LAUNCHER_DIR/ai-journal" ]; then
    "$LAUNCHER_DIR/ai-journal" menu
else
    python3 "$LAUNCHER_DIR/scripts/journal_cli.py" menu
fi

echo ""
read -r -n 1 -p "Press any key to close this window..."
