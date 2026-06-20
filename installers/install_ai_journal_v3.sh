#!/bin/bash
# Upgrade or install AI Journal Kit v3.0 from this repository bundle.

set -euo pipefail

echo "Installing AI Journal Kit v3.0"
echo "=============================="

JOURNAL_DIR="${AI_JOURNAL_DIR:-$HOME/AI-Journal}"
SCRIPTS_DIR="$JOURNAL_DIR/scripts"
BIN_DIR="$HOME/bin"
INSTALLER_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BUNDLE_DIR="$(cd "$INSTALLER_DIR/.." && pwd)"

mkdir -p "$JOURNAL_DIR/entries" "$JOURNAL_DIR/media" "$SCRIPTS_DIR" "$BIN_DIR"

if [ -f "$JOURNAL_DIR/ai-journal" ] || [ -d "$SCRIPTS_DIR" ]; then
    BACKUP_DIR="$JOURNAL_DIR/backup-$(date +%Y%m%d-%H%M%S)"
    mkdir -p "$BACKUP_DIR"
    [ -f "$JOURNAL_DIR/ai-journal" ] && cp "$JOURNAL_DIR/ai-journal" "$BACKUP_DIR/"
    find "$SCRIPTS_DIR" -maxdepth 1 -type f -name "*.py" -exec cp {} "$BACKUP_DIR/" \;
    echo "Backup created at $BACKUP_DIR"
fi

cp "$BUNDLE_DIR/ai-journal" "$JOURNAL_DIR/ai-journal"
cp "$BUNDLE_DIR/scripts"/*.py "$SCRIPTS_DIR/"
chmod +x "$JOURNAL_DIR/ai-journal" "$SCRIPTS_DIR"/*.py
ln -sf "$JOURNAL_DIR/ai-journal" "$BIN_DIR/ai-journal"

if [ -f "$BUNDLE_DIR/Start AI Journal.command" ]; then
    cp "$BUNDLE_DIR/Start AI Journal.command" "$JOURNAL_DIR/"
    chmod +x "$JOURNAL_DIR/Start AI Journal.command"
fi

if [ ! -f "$JOURNAL_DIR/index.json" ]; then
    cat > "$JOURNAL_DIR/index.json" <<EOF
{
  "version": "3.0",
  "created": "$(date -Iseconds)",
  "entries": [],
  "tags": {},
  "next_id": 1,
  "ai_stats": {
    "total_ai_assisted": 0,
    "sources_used": {},
    "avg_quality_rating": 0.0
  },
  "stats": {
    "total_entries": 0,
    "last_modified": "$(date -Iseconds)"
  }
}
EOF
fi

"$BIN_DIR/ai-journal" --help >/dev/null

echo ""
echo "Installation complete."
echo "Optional AI integration dependency:"
echo "  python3 -m pip install -r \"$BUNDLE_DIR/requirements.txt\""
echo ""
echo "Try:"
echo "  ai-journal"
echo "Or double-click:"
echo "  $JOURNAL_DIR/Start AI Journal.command"
