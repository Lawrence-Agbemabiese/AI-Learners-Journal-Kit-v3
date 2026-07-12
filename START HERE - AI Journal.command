#!/bin/bash
# Friendly top-level launcher for non-technical macOS users.
set -e
cd "$(dirname "$0")"

if [ -f "Start AI Journal (Web).command" ]; then
  exec bash "Start AI Journal (Web).command"
fi

if [ -f "scripts/web_server.py" ]; then
  echo "Starting AI Journal..."
  echo "Your browser will open automatically."
  echo "Keep this window open while using the journal."
  python3 "scripts/web_server.py"
else
  echo "AI Journal files could not be found."
  echo "Please read START_HERE.md or contact support."
  read -r -p "Press Return to close."
fi
