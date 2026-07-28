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

### 2026-07-28 15:27 HKT — Codex — Added typography hierarchy examples

Summary:
- Added a standalone comparison page with three simple card treatments for the four text layers: subtitle, pretext, body, and clickable APA-like reference.
- Used the same sample text in every option so the hierarchy can be compared before changing the main StoryMap cards.

Files changed:
- `Website/typography-hierarchy-options.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed the page contains three options and three reference links targeting the example reference position.
- Browser inspection showed the comparison cards rendered correctly; `git diff --check` passed.

Remaining:
- Choose one option before applying the hierarchy to the main introduction website.

### 2026-07-28 15:29 HKT — Codex — Added local AI agent rules

Summary:
- Added `AGENT.md` with folder-specific rules derived from the parent project
  instructions.
- Documented website architecture, source and research boundaries, review-tool
  isolation, validation, logging, handoff, and safety requirements.
- Added the new agent-rules file to the README file map.

Files changed:
- `AGENT.md`
- `README.md`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Compared the local rules with `../AGENTS.md` before writing them.
- Confirmed the guide uses current website paths, server ports, and validation
  commands.
- Preserved the concurrent typography comparison change and its existing log
  entries.

Remaining:
- Keep `AGENT.md`, `README.md`, and both change logs current as the website
  evolves.

### 2026-07-28 15:34 HKT — Codex — Split the website into StoryMap and embedded-tool folders

Summary:
- Moved the StoryMap page and its two assets into `Website/storymap/`.
- Moved the standalone embedded review tool and its two assets into `Website/embedded-tool/`.
- Updated page references, the file-mode review-tool fallback path, README guidance, and agent instructions.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`
- `Website/embedded-tool/review-tool-embed.html`
- `Website/embedded-tool/review-tool-embed.css`
- `Website/embedded-tool/review-tool-embed.js`
- `AGENT.md`
- `README.md`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed active code and documentation no longer use the old mixed `Website/assets/` layout.
- Confirmed the nested StoryMap file-mode fallback points to the review-tools directory.

Remaining:
- A concurrent uncommitted `storymap.js` edit removes section 1.5, so the moved StoryMap iframe was not independently checked; that edit was preserved. The moved embedded-tool page passed browser verification.

### 2026-07-28 15:36 HKT — Codex — Applied Option C card hierarchy and inline reference

Summary:
- Applied the selected Option C treatment to the main StoryMap cards: 30px
  serif subtitles matching Option A, compact body text, and left-rule pretext
  styling.
- Moved the Dai citation into the 1.3 body immediately after
  `超過二萬七千頁。` and linked it to an anchored reference-page entry.
- Updated the comparison page's Option C example and removed the standalone
  1.5 research-results navigation entry in accordance with the requested scope.

Files changed:
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-example.html`
- `Website/typography-hierarchy-options.html`
- `Website/references.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Both website JavaScript files pass `node --check`.
- `git diff --check` passes.
- Confirmed the inline citation and reference anchor paths in the edited HTML
  and JavaScript. The browser's file-page security policy prevented a fresh
  visual recheck in this pass.

Remaining:
- Review the visual spacing in the normal local HTTP preview when available.

### 2026-07-28 15:50 HKT — Codex — Removed card number labels

Summary:
- Removed the orange number line above each StoryMap subtitle, such as
  `1.3 / 01`.
- Removed the associated number styling and tightened the subtitle's top
  spacing.
- Restored the linked reference page after finding it deleted in the working
  tree, so the existing inline citation remains functional.

Files changed:
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`
- `Website/references.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check Website/storymap/storymap.js` passes.
- Confirmed the card renderer no longer outputs the number element.
- `git diff --check` passes.

Remaining:
- Review the updated card spacing in the normal local HTTP preview when available.

### 2026-07-28 15:37 HKT — Codex — Added the automatic checkpoint rule

Summary:
- Updated `AGENT.md` to require an immediate local commit after every
  validated coherent non-log change.
- Clarified that log edits belong with the related change and must not create a
  separate log-only commit.

Files changed:
- `AGENT.md`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed the new rule distinguishes non-log changes from log-only edits.
- Confirmed it preserves unrelated concurrent changes and prohibits automatic
  pushing.

Remaining:
- Follow this checkpoint rule for subsequent introduction-website changes.

### 2026-07-28 15:54 HKT — Codex — Set whole-project commit scope

Summary:
- Updated `AGENT.md` so automatic checkpoints commit the entire DH Project
  repository rather than only files changed inside `intro Website/`.
- Specified `git add -A` from the repository root, with a status and secret
  check before staging.

Files changed:
- `AGENT.md`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed the rule requires whole-repository staging and preserves the
  prohibition on automatic pushing and destructive operations.
- Inspected the current repository status before applying the scope change.

Remaining:
- Apply whole-repository staging for the checkpoint created by this change.
