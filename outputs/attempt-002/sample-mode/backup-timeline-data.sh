#!/usr/bin/env bash
# backup-timeline-data.sh  (lives in outputs/attempt-002/sample-mode/)
# Snapshots the LIVE timeline overlay (../timeline-edits.local.json) into
# ./backups/ as a timestamped file. Run before demos/experiments.
# Restore with restore-timeline-data.sh.
set -euo pipefail
cd "$(dirname "$0")"
SRC="../timeline-edits.local.json"
[ -f "$SRC" ] || { echo "No ../timeline-edits.local.json — nothing to back up."; exit 1; }
mkdir -p backups
TS="$(date +%Y%m%d-%H%M%S)"
DEST="backups/timeline-edits.backup-$TS.json"
cp "$SRC" "$DEST"
echo "Backed up ../timeline-edits.local.json -> sample-mode/$DEST ($(du -h "$DEST" | cut -f1))"
echo "Restore later with:  ./restore-timeline-data.sh $DEST"
