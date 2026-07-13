#!/usr/bin/env bash
# restore-timeline-data.sh [backup-file]  (lives in outputs/attempt-002/sample-mode/)
# Restores the LIVE timeline overlay (../timeline-edits.local.json) from a backup.
# If no file is given, uses the most recent backups/timeline-edits.backup-*.json.
#
# IMPORTANT: after restoring, reload the live site (with the local server running,
# `python3 run-local.py`); the app prefers the server/disk copy, so it will pick
# up the restored file. If a stale browser cache still shows old data, run this in
# the browser console then reload:
#     localStorage.removeItem('llmwiki.timeline.edits.v1')
set -euo pipefail
cd "$(dirname "$0")"
DEST="../timeline-edits.local.json"
SRC="${1:-}"
if [ -z "$SRC" ]; then
  SRC="$(ls -1t backups/timeline-edits.backup-*.json 2>/dev/null | head -n1 || true)"
  [ -n "$SRC" ] || { echo "No backup given and none found in backups/."; exit 1; }
fi
[ -f "$SRC" ] || { echo "Backup not found: $SRC"; exit 1; }

# validate JSON before overwriting
if command -v node >/dev/null 2>&1; then
  node -e "JSON.parse(require('fs').readFileSync('$SRC','utf8'))" || { echo "Refusing to restore: $SRC is not valid JSON."; exit 1; }
fi

# safety copy of whatever is live right now, so a restore is itself undoable
if [ -f "$DEST" ]; then
  mkdir -p backups
  SAFE="backups/timeline-edits.prerestore-$(date +%Y%m%d-%H%M%S).json"
  cp "$DEST" "$SAFE"
  echo "Saved current live data as sample-mode/$SAFE (in case you need to undo this restore)."
fi

cp "$SRC" "$DEST"
echo "Restored $SRC -> ../timeline-edits.local.json ($(du -h "$DEST" | cut -f1))"
echo "Reload the live site (with run-local.py running) to see the restored data."
