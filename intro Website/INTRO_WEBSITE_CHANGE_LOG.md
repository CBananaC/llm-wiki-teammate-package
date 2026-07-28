# Intro Website Change Log

This log records coherent changes made inside `intro Website/`. Each entry
includes the date and time in Hong Kong time, author, summary, files changed,
verification, and remaining work. Update this file after every coherent change
to the folder.

## Baseline

Created on 2026-07-28 15:24 HKT. The folder already contained uncommitted
changes before this log was created; those files are preserved and are not
attributed to this setup entry:

- `Outline/Content.docx`
- `Outline/Outline.docx`
- `Outline/Intro.docx`
- `Outline/Part 1.docx`
- temporary Word lock files under `Outline/`
- `Website/assets/`

## Change log

### 2026-07-28 15:24 HKT — Codex — Created the folder-specific change log

Summary:
- Added a dedicated change log for the introduction website folder.
- Defined the required fields and update rule for future coherent changes.
- Recorded the pre-existing uncommitted baseline without modifying those files.

Files changed:
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed the log is located directly in `intro Website/`.
- Confirmed the pre-existing uncommitted files remain untouched.

Remaining:
- Keep this log updated after every coherent change made inside this folder.

### 2026-07-28 15:26 HKT — Codex — Added the AI working guide

Summary:
- Added a folder README explaining the introduction website's purpose, file
  structure, source-of-truth rules, review-tool dependency, testing workflow,
  and change-log requirements.

Files changed:
- `README.md`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Reviewed the current StoryMap, standalone embed, asset files, and repository
  instructions before writing the guide.
- Confirmed the README uses exact current paths and documents the HTTP and
  file-mode review embed behaviour.

Remaining:
- Keep the README and both change logs current as the website evolves.

### 2026-07-28 15:26 HKT — Codex — Split the introduction website into separate HTML, CSS, and JavaScript files

Summary:
- Removed the large inline style and script blocks from both website pages.
- Kept each page's markup in its HTML file and moved its presentation and page logic/data into separate files under `Website/assets/`.

Files changed:
- `Website/storymap-example.html`
- `Website/review-tool-embed.html`
- `Website/assets/storymap.css`
- `Website/assets/storymap.js`
- `Website/assets/review-tool-embed.css`
- `Website/assets/review-tool-embed.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Both extracted JavaScript files pass `node --check`.
- All external asset references exist and the HTML files contain no inline CSS or JavaScript.
- Browser inspection confirmed the introduction cards/table and review embed render from the split files.
- Browser interaction confirmed quote highlighting still works; `git diff --check` passed.

Remaining:
- The separate review-tools server could not be started in the restricted shell, so the StoryMap iframe's server-backed route remains to be rechecked when that server is available.
