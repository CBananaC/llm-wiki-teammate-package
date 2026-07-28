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

### 2026-07-28 16:30 HKT — Codex — Restored the 1.5 research-results section

Summary:
- Restored `1.5 / 研究成果` between 1.4 and 1.6 using the exact three
  paragraphs supplied for the introduction.
- Reconnected the existing 硃83 sample review interface as the section's
  backdrop.
- Added 1.5 to the introduction workflow navigation and extended its route to
  1.6.

Files changed:
- `Website/storymap/storymap.js`
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check Website/storymap/storymap.js` passes.
- Confirmed the 1.5 card data, review iframe, navigation node, and section
  anchor are present.
- `git diff --check` passes.

Remaining:
- Review the restored section and embedded review interface in the normal
  local HTTP preview when available.

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

### 2026-07-28 16:07 HKT — Codex — Add StoryMap display settings

Summary:
- Added an unboxed gear settings button at the far right of the StoryMap top
  bar.
- Added persistent A−/A＋ font-size controls with a wide 55%–220% range,
  outside-click and Escape-to-close behavior, and disabled endpoint buttons.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`

Verified:
- Confirmed the gear path matches the canonical project settings icon.
- Passed `node --check Website/storymap/storymap.js` and `git diff --check`.
- Browser-verified the no-border button, panel toggle, 105% scaling, 55% and
  220% limits, reload persistence, and reset to 100%.

Remaining:
- None for this change.

### 2026-07-28 20:11 HKT — Codex — Loaded Part 2.docx into the website

Summary:
- Read `Outline/Part 2.docx` and preserved its operating-process content and
  nested AI-analysis headings.
- Replaced the Part 2 placeholder hero with `1. 平台的運作流程` and its
  introductory statement.
- Added four independent card-and-backdrop sections for the overall process,
  workflow diagram, structured-data input, and AI extraction.
- Kept the three AI subsections inside the AI-extraction card.

Files changed:
- `Outline/Part 2.docx` (read-only source)
- `Website/storymap/storymap.js`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Rendered the DOCX to two page images and inspected both pages.
- Extracted and checked the DOCX paragraph text with the bundled document
  runtime.
- Passed `node --check` for both website JavaScript files and `git diff --check`.

Remaining:
- Review Part 2 in the normal local HTTP preview when available.

### 2026-07-28 18:45 HKT — Codex — Loaded Part 1.docx into the website

Summary:
- Read `Outline/Part 1.docx` and preserved its platform-overview text and six
  interface subsections.
- Replaced the Part 1 placeholder hero with `1. 平台的整體介面` and its
  introductory paragraph.
- Added independent card-and-backdrop sections for the four platform areas,
  導覽列, 時間與關係圖表, 節點資訊區, 原始史料區, and 人工智能分析區.
- Added subsection headings inside the relevant cards so the DOCX hierarchy
  remains readable on the website.

Files changed:
- `Outline/Part 1.docx` (read-only source)
- `Website/storymap/storymap.js`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Rendered the DOCX to two page images and inspected both pages.
- Extracted and checked the DOCX paragraph text with the bundled document
  runtime.
- Passed `node --check` for both website JavaScript files and `git diff --check`.

Remaining:
- Review Part 1 in the normal local HTTP preview when available.

### 2026-07-28 16:34 HKT — Codex — Rebuild 引言 workflow as full-width horizontal chart

Summary:
- Reworked the 引言 workflow into a full-width translucent deep-teal panel
  beneath the top bar.
- Replaced the previous route with a horizontal sequence: 清代奏折上諭、奏折
  上諭研究價值、three separate 研究困難 bubbles, 數位方法, and 案例：林爽文事件.
- Added white connector lines and text, coral difficulty labeling, and hover,
  focus, and selected-bubble states.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`

Verified:
- Passed `node --check Website/storymap/storymap.js` and `git diff --check`.
- Browser-verified the full-width panel geometry, deep translucent styling,
  seven horizontal workflow nodes, connector path, and direct section targets.

Remaining:
- None for this change.

### 2026-07-28 16:25 HKT — Codex — Redesign 引言 submenu as workflow map

Summary:
- Replaced the plain vertical 引言 submenu with a paper-toned workflow
  window containing five subtitle bubbles connected by a routed line.
- Kept each bubble as a direct link to its corresponding introduction section,
  with hover/focus motion and coral-accent interaction states.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`

Verified:
- Passed `node --check Website/storymap/storymap.js` and `git diff --check`.
- Browser-verified the five workflow nodes, their section links, chart layout,
  connector path, and themed submenu dimensions.

Remaining:
- None for this change.

### 2026-07-28 16:11 HKT — Codex — Center top-bar navigation

Summary:
- Centered the section buttons as a group in the desktop top bar while
  keeping the settings button as the only right-aligned control.
- Preserved the existing compact mobile top-bar behavior.

Files changed:
- `Website/storymap/storymap.css`

Verified:
- Passed `node --check Website/storymap/storymap.js` and `git diff --check`.
- Browser-verified that the navigation group is centered at 1280px and the
  settings control remains aligned to the right edge.

Remaining:
- None for this change.

### 2026-07-28 16:43 HKT — Codex — Refine 引言 flowchart branch layout

Summary:
- Removed all extra dropdown headings and step-number labels.
- Rebuilt the chart to match the requested algorithm-style flow: two left
  nodes, a three-way vertical 研究困難 branch, then 數位方法 and 案例：林爽文事件.
- Changed the bubbles to transparent ellipses with white outlines/text and
  coral hover, focus, and selected states.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`

Verified:
- Passed `node --check Website/storymap/storymap.js` and `git diff --check`.
- Browser-verified seven bubbles, no extra menu text, white text styling,
  elliptical borders, and branch connector geometry.

Remaining:
- None for this change.

### 2026-07-28 16:49 HKT — Codex — Compress workflow bubbles and preserve hover area

Summary:
- Reduced the workflow canvas and ellipse height so the dropdown occupies much
  less vertical space.
- Kept the full-width chart and branch geometry intact.
- Changed dropdown closing to wait until the pointer has left both the 引言
  trigger and the full workflow panel.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`

Verified:
- Passed `node --check Website/storymap/storymap.js` and `git diff --check`.
- Browser-verified 54px bubbles, a 220px chart canvas, and the fixed full-width
  panel position.

Remaining:
- None for this change.

### 2026-07-28 16:49 HKT — Codex — Split the introduction website into independent top-level tabs

Summary:
- Changed the page from one continuous list of the cover and all sections into
  four independently displayed views: 主頁, 引言, 第一部分, and 第二部分.
- Kept the existing introduction cards inside the 引言 view and added a
  shorter cover-style masthead at the top of 引言 and both parts.
- Added hash-based tab switching and preserved direct links to individual
  introduction sections from the workflow menu.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`

Verified:
- Passed `node --check Website/storymap/storymap.js` and `git diff --check`.
- Browser-verified that each top-level tab hides the other panels, that the
  compact masthead renders at 287px in the current desktop preview, and that
  direct `#intro-1-3-b` navigation opens 引言 and scrolls to the target card.

Remaining:
- 第一部分 and 第二部分 currently contain their independent mastheads only;
  their substantive content can be added into those panels when supplied.

### 2026-07-28 16:59 HKT — Codex — Extend 引言 flow with research difficulty and results

Summary:
- Removed the orange active underline from the top navigation.
- Added 研究難處 before the three difficulty bubbles and 研究成果 after
  數位方法, preserving the horizontal branch flow.
- Kept the compact ellipse bubbles and white connector styling.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`

Verified:
- Passed `node --check Website/storymap/storymap.js` and `git diff --check`.
- Browser-verified nine bubbles, three branch rows, 54px bubble height, the
  220px chart canvas, and no active underline pseudo-element.

Remaining:
- None for this change.

### 2026-07-28 17:11 HKT — Codex — Change workflow bubbles to thin-border rectangles

Summary:
- Replaced the ellipse bubbles with compact, lightly rounded rectangular
  bubbles using a 1px white border and restrained shadow.

Files changed:
- `Website/storymap/storymap.css`

Verified:
- Passed `node --check Website/storymap/storymap.js` and `git diff --check`.
- Browser-verified 1px border, 8px corner radius, and compact 54px node height.

Remaining:
- None for this change.

### 2026-07-28 17:15 HKT — Codex — Remove workflow bubble corner rounding

Summary:
- Set the workflow rectangles to square corners with no border radius.

Files changed:
- `Website/storymap/storymap.css`

Verified:
- Passed `node --check Website/storymap/storymap.js` and `git diff --check`.
- Browser-verified `border-radius: 0px`, a 1px border, and 54px height.

Remaining:
- None for this change.

### 2026-07-28 17:17 HKT — Codex — Narrow workflow rectangles

Summary:
- Reduced the horizontal width of each workflow rectangle while preserving
  square corners, thin borders, and the existing flow layout.

Files changed:
- `Website/storymap/storymap.css`

Verified:
- Passed `node --check Website/storymap/storymap.js` and `git diff --check`.
- Browser-verified 137px rendered width at the current desktop viewport,
  54px height, 1px border, and zero corner radius.

Remaining:
- None for this change.
