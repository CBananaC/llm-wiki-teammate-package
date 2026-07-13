# sample-mode/

Tooling for building **sample / presentation data** without touching the live
timeline. Everything here is optional — the real site in the parent folder runs
fine without it.

## The parent folder (`outputs/attempt-002/`) is the LIVE site + data

- `stage1-timeline.html` — the real website (documents are baked in as `DUAL`).
- `timeline-edits.local.json` — the real saved overlay (events, emperor-action
  dots, yu→zhu reply lines, chat). The server reads/writes this via `/api/edits`.
- the `*.json` data files — source/layout data.

Do not move those; `review-app/server.py` expects them there.

## What's in here

| File | Purpose |
|------|---------|
| `stage1-timeline-blank.html` | An **empty** copy of the site: same document dots, no events. Fully isolated — its own localStorage key, and it reads/writes **`/api/edits-blank`** (not the real `/api/edits`). Build sample yu→zhu replies here for a presentation. |
| `sample-edits.local.json` | The blank page's own **disk-backed** sample data. Auto-loads on reload via `/api/edits-blank`, so samples survive a refresh with no localStorage size cap. Never affects the real timeline. |
| `make-blank-page.js` | Regenerates `stage1-timeline-blank.html` from `../stage1-timeline.html`. Run after any change to the live HTML. |
| `backup-timeline-data.sh` | Snapshots `../timeline-edits.local.json` into `backups/`. |
| `restore-timeline-data.sh` | Restores `../timeline-edits.local.json` from a backup (auto-saves current state first). |
| `backups/` | Timestamped data snapshots (git-ignored). |

**Disk-sync:** the blank page persists its samples to `sample-edits.local.json`
through the server (`/api/edits-blank`), completely separate from the real
`../timeline-edits.local.json` (`/api/edits`). This means a full-size restore is
not limited by localStorage, and reloading the blank page reloads your samples.
The **🧹 清空範例** button clears both localStorage and the disk file, then reloads.
(Disk-sync needs the local server running via `run-local.py`; opened as `file://`
it falls back to localStorage only.)

## How to use

Start the site normally from the package root:

```bash
python3 run-local.py
```

- **Live site:** <http://127.0.0.1:8766/app>
- **Blank sample page:** <http://127.0.0.1:8766/attempt-002/sample-mode/stage1-timeline-blank.html>

On the blank page, the bottom-right **🧹 清空範例** button resets it to empty
anytime. Its data lives under its own localStorage key, so it never affects the
live timeline.

Back up before a demo, restore after:

```bash
cd outputs/attempt-002/sample-mode
./backup-timeline-data.sh          # -> backups/timeline-edits.backup-<ts>.json
./restore-timeline-data.sh         # restore newest backup
```

Regenerate the blank page after editing the live HTML:

```bash
node outputs/attempt-002/sample-mode/make-blank-page.js
```
