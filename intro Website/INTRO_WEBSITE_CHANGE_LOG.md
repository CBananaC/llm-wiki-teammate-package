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

### 2026-07-30 16:15 HKT — Codex — Refined the 第一部分 interface overview

Summary:
- Revised the `第一部分` UI concept from multiple overview cards to one large
  replica of the sample review tool beneath the `1. 平台的整體介面` cover.
- Added four clickable highlights with floating function labels for the
  導覽列、時間與關係圖表、原始史料區, and AI 分析區.
- Added free-exploration, guided-tour, reset, responsive, and replica-boundary
  ideas.

Files changed:
- `Website/UI Idea/03-第一部分.md`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed the four labels match the current platform areas and use the
  existing Traditional Chinese terminology.
- Passed `git diff --check`.

Remaining:
- Decide whether the replica should be a live sample embed, an annotated
  screenshot, or a purpose-built teaching replica.

### 2026-07-30 16:00 HKT — Codex — Refined research-result and case-study visuals

Summary:
- Updated the `研究成果` idea to use a looping GIF of the complete website UI,
  with callouts and a static accessibility fallback.
- Specified one dominant image for each `林爽文事件` card: Qing war-scene
  drawing, Taiwan-to-Beijing information-route map, and the two source-book
  covers.

Files changed:
- `Website/UI Idea/02-引言.md`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed the new image assignments are mapped to the existing three case
  cards and the source titles use Traditional Chinese.
- Passed `git diff --check`.

Remaining:
- Add the actual GIF, images, permissions, catalogue details, and citations
  once the source assets are selected.

### 2026-07-30 15:47 HKT — Codex — Added per-tab UI brainstorming notes

Summary:
- Created one markdown brainstorming file for each top-level website tab.
- Developed the `引言` concept around an interactive Qing document-route map,
  source images, a Taiwan-to-Beijing inset, and a Forbidden City inset.
- Separated the three `研究清代奏折的主要困難` ideas into document scale,
  communication relations, and event/source networks.
- Added interaction and content ideas for the platform interface, research
  workflow, and reuse/adaptation tabs.

Files changed:
- `Website/UI Idea/01-主頁.md`
- `Website/UI Idea/02-引言.md`
- `Website/UI Idea/03-第一部分.md`
- `Website/UI Idea/04-第二部分.md`
- `Website/UI Idea/05-第三部分.md`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed the five files match the current top-level tabs: `主頁`, `引言`,
  `第一部分`, `第二部分`, and `第三部分`.
- Confirmed the notes preserve Traditional Chinese UI labels and mark the
  institutional route as a simplified model requiring source validation.
- Passed `git diff --check`.

Remaining:
- Decide which ideas should be promoted into the live StoryMap after reviewing
  the notes and confirming image sources, permissions, and historical framing.

### 2026-07-30 15:15 HKT — Codex — Reformatted the independent StoryMap card-layout CSS

Summary:
- Reformatted every card rule so each property appears on its own line with an explanatory comment.
- Added a blank line between every card block while preserving all existing values and selectors.

Files changed:
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed all 49 card blocks remain present.
- Passed `git diff --check`.

Remaining:
- None for this change.

### 2026-07-30 15:00 HKT — Codex — Added the shared StoryMap card-layout synchronization rule

Summary:
- Added a common project rule requiring every StoryMap card creation, edit, or subtitle/title change to update the matching labelled block in `storymap-cards.css`.
- Required the Traditional Chinese subtitle/title comment in CSS to remain synchronized for easy manual identification.

Files changed:
- `../AGENTS.md`
- `../CLAUDE.md`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed `AGENTS.md` and `CLAUDE.md` are byte-for-byte identical.
- Passed `git diff --check`.

Remaining:
- None for this change.

### 2026-07-30 15:05 HKT — Codex — Remove oversized backdrop characters

Summary:
- Removed the large decorative Chinese character from every story-card backdrop.
- Preserved the existing backdrop colors, imagery, and card content.

Files changed:
- `Website/storymap/storymap.css`

Verified:
- Passed `git diff --check`.

Remaining:
- None for this change.

### 2026-07-30 15:03 HKT — Codex — Simplify the intro workflow header

Summary:
- Renamed the workflow node 奏折上諭研究價值 to 研究價值.
- Removed the three numbered 研究難處 nodes from the intro workflow header while retaining the general 研究難處 section link.

Files changed:
- `Website/storymap/storymap-example.html`

Verified:
- Confirmed the old header label and all three numbered difficulty nodes are absent from the workflow markup.
- Passed `git diff --check`.

Remaining:
- None for this change.

### 2026-07-30 14:40 HKT — Codex — Added an independent StoryMap card-layout stylesheet

Summary:
- Added one clearly labelled CSS block for each of the 49 StoryMap cards.
- Moved the practical editing workflow for card position, width, and section height into `storymap-cards.css`, with each block identified by the card's Traditional Chinese subtitle/title.
- Kept the existing HTML inline values as non-authoritative fallbacks and loaded the new stylesheet after the main StoryMap stylesheet.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed 49 StoryMap sections and 49 matching CSS layout blocks.
- Passed `git diff --check`.
- Browser-verified the first card at desktop width and at a 390px mobile width; desktop position/width and mobile stacked positioning both render as expected.

Remaining:
- None for this change.

### 2026-07-30 14:40 HKT — Codex — Remove the introductory cover tab

Summary:
- Removed the 引言 cover panel headed `從奏摺與上諭理解清代通信`.
- Kept the 引言 content cards and workflow navigation as the direct entry point.

Files changed:
- `Website/storymap/storymap-example.html`

Verified:
- Confirmed the removed heading and intro cover markup no longer appear in the page.
- Passed `git diff --check`.

Remaining:
- None for this change.

### 2026-07-30 14:36 HKT — Codex — Preserve the website’s original cover palette

Summary:
- Kept the competition cover’s spacing and hierarchy as the layout reference, but restored the introduction website’s deep-teal and restrained-coral background palette.

Files changed:
- `Website/storymap/storymap.css`

Verified:
- Passed `git diff --check`.

Remaining:
- None for this change.

### 2026-07-30 14:31 HKT — Codex — Accent the start-reading button

Summary:
- Changed `開始閱讀` to the website’s coral-orange text and border, with a matching hover state.

Files changed:
- `Website/storymap/storymap.css`

Verified:
- Passed `git diff --check`.

Remaining:
- None for this change.

### 2026-07-30 14:24 HKT — Codex — Build the cover-page competition links

Summary:
- Replaced the cover-page eyebrow with `2026 理大人工智能 X 數位人文獎・工具型作品示例` and enlarged the cover hierarchy.
- Added three thin, square-cornered buttons: `比賽網站`, `下載工具代碼`, and `開始閱讀`.
- Connected the buttons to the competition website, the project GitHub repository, and the 引言 panel respectively.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`

Verified:
- Passed `node --check Website/storymap/storymap.js` and `git diff --check`.
- Browser-verified the three labels, exact destinations, 1px white borders, square corners, and the `開始閱讀` panel switch to `#intro`.

Remaining:
- None for this change.

### 2026-07-29 17:56 HKT — Codex — Added the 4. 收取上諭的資訊 cover bar

Summary:
- Applied the thin backdrop-and-large-text cover bar to `4. 收取上諭的資訊`.
- Kept its three detailed imperial-edict subsections in the content card below.

Files changed:
- `Website/storymap/storymap.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed `node --check` for both website JavaScript files.
- Passed `git diff --check`.
- Confirmed `part-2-yu-info` now uses `coverBar: true` and the cover-bar card
  placement.

Remaining:
- Review the cover-bar height and long-card spacing in the normal local HTTP
  preview when available.

### 2026-07-29 17:52 HKT — Codex — Loaded the expanded Part 2 DOCX content

Summary:
- Re-read the current `Outline/Part 2.docx`, which had expanded to 64
  non-empty source paragraphs.
- Replaced the abbreviated Part 2 data with the complete workflow, structured
  input, AI Skills, communication-pairing, event-extraction, source-tracing,
  imperial-edict, and visualization content.
- Added separate cards for the detailed nested workflows so long sections are
  not hidden inside one overflowing card.
- Mapped every DOCX `(cover bar UI)` marker to the thin cover-bar renderer.

Files changed:
- `Outline/Part 2.docx` (read-only source)
- `Website/storymap/storymap.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Compared all 64 non-empty DOCX paragraphs against the website source; zero
  exact source strings are missing.
- Passed `node --check` for both website JavaScript files.
- Passed `git diff --check`.

Remaining:
- Review the complete Part 2 sequence and long-card spacing in the normal local
  HTTP preview when available.

### 2026-07-29 17:45 HKT — Codex — Added thin cover bars to selected Part 2 sections

Summary:
- Applied the thin, non-full-screen cover-bar treatment to `1. 平台的運作流程`
  and `3. 運作流程圖`.
- Added backdrop-backed large title text while keeping the detailed content in
  the readable card layer below.
- Left `4. 輸入結構化資料` and `5. 使用AI從原文中抽取資訊` as detailed card
  layouts.

Files changed:
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed `node --check` for both website JavaScript files.
- Passed `git diff --check`.
- Confirmed only the two selected Part 2 sections receive the `cover-bar`
  renderer and styling.

Remaining:
- Review the cover-bar height, backdrop contrast, and card placement in the
  normal local HTTP preview when available.

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

### 2026-07-30 03:47 HKT — Codex — Load complete Part 3 DOCX content

Summary:
- Added a new `第三部分` panel and loaded all Part 3 content from `Outline/Part 3.docx`.
- Preserved the source hierarchy as independent cards, with thin cover bars for `1. OCR 並結構化原始史料`, `2. 運用AI抽取資訊`, and `3. 後續功能：LLM Wiki`.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`

Verified:
- Rendered and visually inspected all 5 pages of `Outline/Part 3.docx`.
- Passed `node --check Website/storymap/storymap.js`.
- Exact-string coverage found all 69 non-empty Part 3 source paragraphs in the website; the three DOCX cover markers are represented as UI cover bars.

Remaining:
- The in-app browser blocked reloading the local `file://` preview, so live visual refresh remains to be checked through the normal local HTTP preview.

### 2026-07-30 14:10 HKT — Codex — Simplify cover page backdrop

Summary:
- Removed the `SCROLL TO EXPLORE` prompt from the cover page.
- Removed the decorative 奏・摺・諭 text from the cover backdrop.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`

Verified:
- Passed `node --check Website/storymap/storymap.js` and `git diff --check`.
- Confirmed neither cover decoration remains in the HTML or CSS.

Remaining:
- None for this change.

### 2026-07-30 14:12 HKT — Codex — Show settings on hover and rename font control

Summary:
- Made the website settings panel open when hovering over the gear area, with
  a small hover bridge between the gear and the dropdown.
- Kept keyboard focus, Escape, and click interactions available.
- Changed the visible and accessible font-control wording from 字級 to 字體.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`

Verified:
- Passed `node --check Website/storymap/storymap.js` and `git diff --check`.
- Browser-verified the gear opens the settings panel and the panel displays
  the 字體 label.

Remaining:
- None for this change.

### 2026-07-30 14:13 HKT — Codex — Move StoryMap content into HTML

Summary:
- Moved the authored StoryMap card text, headings, notes, citations, tables, cover bars, and backdrop labels from JavaScript data arrays into static HTML.
- Reduced `storymap.js` to interaction and presentation behavior while preserving the existing navigation, card hierarchy, Part 2 content, and Part 3 cover bars.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`

Verified:
- Passed HTML parsing, `node --check Website/storymap/storymap.js`, and `git diff --check`.
- Exact-string coverage remains complete for Part 2 (64/64) and Part 3 (69/69) source paragraphs.
- Browser-verified the HTTP preview at `#part-3`, including the Third Part navigation link, headings, paragraphs, and thin cover-bar sections.

Remaining:
- None for this change.

### 2026-07-30 14:29 HKT — Codex — Refine the cover competition label

Summary:
- Reduced the size of `2026 理大人工智能 X 數位人文獎・工具型作品示例` so the main platform title remains the visual focus.
- Changed the label to the website’s coral-orange accent color.

Files changed:
- `Website/storymap/storymap.css`

Verified:
- Passed `git diff --check`.

Remaining:
- None for this change.

### 2026-07-30 15:16 HKT — Codex — Fit the intro dropdown to its content

Summary:
- Reduced the intro workflow canvas to one content row instead of reserving unused branch rows.
- Kept the dropdown height content-driven, with its existing upper and lower padding providing the surrounding margins.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`

Verified:
- Confirmed the workflow canvas has a 54px content row and the dropdown has no fixed height.
- Passed `git diff --check`.

Remaining:
- None for this change.

### 2026-07-30 15:13 HKT — Codex — Center and equalize the intro workflow chain

Summary:
- Reflowed the six workflow buttons into consecutive centered columns.
- Equalized all five connector dashes and removed the unused gap caused by the former empty branch column.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`

Verified:
- Confirmed the workflow uses six consecutive columns and the SVG connector coordinates form five equal-length horizontal segments.
- Passed `git diff --check`.

Remaining:
- None for this change.

### 2026-07-30 15:11 HKT — Codex — Restore the straight intro workflow line

Summary:
- Restored the 研究難處 workflow button.
- Removed the unnecessary branch lines and connected 研究價值, 研究難處, and 數位方法 along one straight horizontal line.

Files changed:
- `Website/storymap/storymap-example.html`

Verified:
- Confirmed the 研究難處 button is present and the SVG contains only straight horizontal connectors for the main workflow.
- Passed `git diff --check`.

Remaining:
- None for this change.

### 2026-07-30 15:09 HKT — Codex — Remove the third intro workflow button

Summary:
- Removed the third workflow button, 研究難處, from the intro header.
- Preserved the connector line by joining it across the former button position to the existing branch and 數位方法 connector.

Files changed:
- `Website/storymap/storymap-example.html`

Verified:
- Confirmed the 研究難處 workflow button is absent and the SVG connector path remains continuous.
- Passed `git diff --check`.
- Browser visual refresh was not possible because the in-app browser blocks the local `file://` preview.

Remaining:
- None for this change.

### 2026-07-30 15:12 HKT — Codex — Preserve the workflow connector line

Summary:
- Kept the three numbered 研究難處 buttons removed from the intro workflow header.
- Extended the existing middle connector line across the empty branch area to 數位方法, while preserving the vertical branch line and upper/lower arms.

Files changed:
- `Website/storymap/storymap-example.html`

Verified:
- Confirmed the connector path remains in the SVG and reaches the 數位方法 connector.
- Passed `git diff --check`.

Remaining:
- None for this change.

### 2026-07-30 17:05 HKT — Codex — Mark Taiwan-war report routes on the visual reference map

Summary:
- Created a marked copy of the 賴福順 route-map PDF with a blue main-route orientation, numbered visible mainland points, a Taiwan continuation callout, and a red auxiliary-route note.
- Preserved the original PDF unchanged and labelled the annotation as UI guidance because this page is 圖十二 while the text's Taiwan-war discussion refers to 圖十三.

Files changed:
- `Website/Visual Material/情報路線/2乾隆重要戰爭之軍需硏究. 賴福順. 國立故宮博物院, 1984 (dragged) - marked Taiwan routes.pdf`

Verified:
- Rendered the marked one-page PDF and visually inspected the result.
- Confirmed Traditional Chinese labels render in the embedded font and the output remains one A4 landscape page.

Remaining:
- Locate and verify 圖十三 before using the Taiwan sea segment or auxiliary route as a precise historical map.

### 2026-07-30 17:23 HKT — Codex — Create a clear 硃40—諭24 demonstration data set

Summary:
- Added a self-contained demonstration overlay that keeps only the 10 event
  dots sourced from 硃40 and the 13 emperor-action dots sourced from 諭24.
- Retained one matching 硃40 AI output card per event and the structured AI
  action output data for all retained 諭24 actions.
- Added the requested 諭24-to-硃40 response connection as a demonstration-only
  pair, and hid unrelated base document dots in the overlay.

Files changed:
- `Website/Clear Data/clear-demo.data`
- `Website/Clear Data/source-documents.json`
- `Website/Clear Data/confirmed-pairs.json`
- `Website/Clear Data/README.md`
- `Website/Clear Data/build_clear_demo.py`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Parsed all three JSON files and compiled the builder successfully.
- Confirmed 23 retained events: 10 from 硃40 and 13 emperor actions from 諭24;
  no other event source remains.
- Confirmed every retained 諭24 emperor action has structured `emperorDetail`
  data and a source entry, and the pair is labelled `demonstration`.
- Passed `git diff --check`.

Remaining:
- Import the overlay into the sample review page and perform a live browser
  check if this demonstration needs to be presented interactively.

### 2026-07-30 17:33 HKT — Codex — Consolidate the clear demonstration into one export JSON

Summary:
- Embedded the complete 硃40 and 諭24 source records into `clear-demo.data`
  under `__sourceDocuments`.
- Kept the timeline events, AI outputs, hidden-document overlay, and requested
  demonstration pair in the same export-style JSON object.
- Removed the redundant standalone source-document and pair JSON files.

Files changed:
- `Website/Clear Data/clear-demo.data`
- `Website/Clear Data/README.md`
- `Website/Clear Data/build_clear_demo.py`
- `Website/Clear Data/confirmed-pairs.json` (removed)
- `Website/Clear Data/source-documents.json` (removed)
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- The single `clear-demo.data` file parses as JSON and contains both source
  records plus the `__docPairs` connection.
- Confirmed the event/action counts remain 10 硃40 events and 13 諭24 emperor
  actions, with no unrelated events.
- Passed `git diff --check`.

Remaining:
- Import the single export JSON into the sample review page and perform a live
  browser check if an interactive presentation is required.

### 2026-07-30 17:43 HKT — Codex — Keep all dots visible with a two-document interaction allowlist

Summary:
- Restored all 225 existing event and emperor-action dots to the single export,
  including the 202 硃40/諭24-independent dots.
- Added `__clearDemo` metadata that keeps all document dots visible while marking
  only 硃40 and 諭24 as clickable for future interaction code.
- Kept the selected 硃40 and 諭24 event IDs and AI output cards separated under
  their matching top-level document data.

Files changed:
- `Website/Clear Data/clear-demo.data`
- `Website/Clear Data/README.md`
- `Website/Clear Data/build_clear_demo.py`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed no `__hidden` document overlay is present.
- Confirmed 225 total event/action dots, 10 selected 硃40 events, 13 selected
  諭24 emperor actions, and 10/9 selected AI output cards.
- Confirmed the clickable-document allowlist is exactly 硃40 and 諭24.
- Passed JSON parsing and `git diff --check`.

Remaining:
- Add the runtime click guard to the review page when the interaction behavior
  is ready to be implemented.

### 2026-07-30 17:56 HKT — Codex — Preserve the Preview-drawn Taiwan route as an HTML line layer

Summary:
- Used the four red Preview drawing annotations in the researcher-marked route PDF as the source line.
- Reconstructed them in the correct order, reversing the third and fourth segments where necessary, and joined them into one standalone SVG path.
- Added optional CSS animation and reduced-motion behaviour without changing the researcher’s source PDF.

Files changed:
- `Website/storymap/taiwan-war-report-route.svg`
- `Website/Visual Material/情報路線/2乾隆重要戰爭之軍需硏究. 賴福順. 國立故宮博物院, 1984 (dragged).pdf`

Verified:
- Parsed the SVG successfully; the 4,261-point path stays within the A4 map viewBox.
- Confirmed the source PDF contains four Preview stamp annotations and the extracted route order joins their endpoints.

Remaining:
- Insert the SVG path into the StoryMap map container when the HTML interaction is implemented.

### 2026-07-30 18:27 HKT — Codex — Add the map backdrop and location pins to the first two intro cards

Summary:
- Rendered the supplied `Fizzy Background.pdf` crop box as a web-ready PNG backdrop.
- Replaced the first two cards' decorative backgrounds with the map backdrop.
- Added separate SVG pin layers to both cards, placing red pins at the Beijing and Taiwan route endpoints.
- Kept the pin layer independent from the future animated route SVG.

Files changed:
- `Website/storymap/fizzy-background.png`
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/Visual Material/情報路線/Fizzy Background.pdf`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Rendered the PDF crop box to a 2106 × 1489 PNG matching the map's A4 coordinate ratio.
- Confirmed both cards contain the same two pins at the existing route SVG endpoint coordinates.
- Passed `node --check Website/storymap/storymap.js` and `git diff --check`.
- Browser visual validation was unavailable because the local preview address was rejected by the browser security policy.

Remaining:
- Add the standalone route SVG as an HTML layer when the line animation interaction is ready.

### 2026-07-30 18:36 HKT — Codex — Replace map spots with interactive Google-style pins

Summary:
- Replaced the oversized red polygon spots in both first cards with compact red teardrop pins and white centers.
- Added hover and keyboard-focus information popovers for 北京 and 臺灣（鹿仔港／鹿耳門）.
- Kept the pin geometry in the shared map SVG coordinate system so it remains aligned with the backdrop and future route animation.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed four pins, four accessible labels, and four hover popovers are present across the two cards.
- Passed `node --check Website/storymap/storymap.js` and `git diff --check`.

Remaining:
- Browser visual validation and the route-line animation remain pending because the local preview address is blocked by the browser security policy.

### 2026-07-30 19:13 HKT — Codex — Build the Taiwan-to-Beijing interactive route map

Summary:
- Applied the same `Fizzy Background.pdf`-derived map backdrop to the first two cards.
- Changed the interaction from hover-only labels to a click-driven Taiwan-first sequence: Taiwan starts alone, its gallery opens, the route draws to Beijing in one second, and Beijing then appears with its information window.
- Loaded the supplied `Visual Material/情報路線/taiwan-war-report-route.svg` at runtime and reversed its point sequence so the animation starts at Taiwan and ends at Beijing.
- Added a three-page Taiwan gallery with supplied project images and a rendered〈臺灣之役〉source page; reaching page three replays the route animation.
- Added keyboard activation, close controls, reduced-motion handling, and responsive information windows.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`
- `Website/storymap/taiwan-route-source-page.png`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed the route source contains 4,261 points and the reversed sequence starts at `(730.24, 510.39)` Taiwan and ends at `(627.41, 207.15)` Beijing.
- Confirmed both cards contain one route map, one Taiwan pin, one gallery, and the supplied route-source reference.
- Confirmed all backdrop, gallery, and route assets exist at their resolved paths.
- Passed `node --check intro Website/Website/storymap/storymap.js` and `git diff --check`.
- Browser visual validation remains unavailable because the local preview address is blocked by the browser security policy.

Remaining:
- Perform a human browser pass when the local preview can be opened, especially checking the information-window position at the smallest mobile width.

### 2026-07-30 19:47 HKT — Codex — Make the supplied route SVG work in local preview and update the first card text

Summary:
- Replaced the `fetch()`-dependent route loader with a native embedded object using the supplied `Visual Material/情報路線/taiwan-war-report-route.svg`.
- Reverse the embedded SVG path at activation time, then animate it from Taiwan to Beijing over one second.
- Replaced the first card's previous explanatory paragraphs with the four supplied chronological paragraphs about 柴大紀、乾隆帝硃批、軍機處登記 and the廷寄諭旨.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed both map instances directly reference the supplied route SVG through `route-line-object`.
- Passed `node --check` for the StoryMap and embedded-tool JavaScript files and `git diff --check`.

Remaining:
- Perform a human browser pass to confirm the embedded SVG's `contentDocument` is accessible in the user's local preview browser.

### 2026-07-30 19:56 HKT — Codex — Remove file-preview route and review-tool cross-origin failures

Summary:
- Generated `taiwan-war-report-route-reverse.svg` from the supplied route SVG by reversing its 4,261-point path sequence.
- Changed the map to load this local reverse derivative directly, with its own one-second draw animation, avoiding `contentDocument` access and the file-preview security error.
- Changed the review iframe to use the existing local HTTP review server on port 8766 even when the StoryMap is opened as a file, avoiding `file:///sample/...` and `file:///api/...` requests.

Files changed:
- `Website/storymap/taiwan-war-report-route-reverse.svg`
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed the reverse route asset starts at `(730.24, 510.39)` Taiwan and ends at `(627.41, 207.15)` Beijing, with 4,261 points.
- Confirmed StoryMap JavaScript no longer uses `fetch()` or `contentDocument` for the route.
- Passed both JavaScript syntax checks and `git diff --check`.

Remaining:
- Open the StoryMap through the local HTTP workflow and confirm the review server is running on port 8766.

### 2026-07-30 20:05 HKT — Codex — Move route gallery to Beijing and repair bidirectional playback

Summary:
- Replaced the old Taiwan three-page popup with a concise Taiwan starting-point information card.
- Moved the three-page image gallery to the Beijing popup, which is revealed after the Taiwan-to-Beijing animation.
- Added separate SVG route layers for the outbound Taiwan → Beijing animation and the return Beijing → Taiwan replay after page 3.
- Removed the route loader's dependency on an embedded-object load event, which was preventing the Beijing reveal in the user's preview.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed `node --check "Website/storymap/storymap.js"`.
- Passed `git diff --check`.
- Confirmed both route-map instances have a Taiwan info card, a hidden Beijing pin, a Beijing three-page gallery, and two direction-specific SVG layers.

Remaining:
- The in-app browser blocked localhost inspection in this turn; reopen the local preview and test Taiwan click → Beijing reveal → gallery page 3 → return animation.

### 2026-07-30 20:20 HKT — Codex — Bring route pins above the map popups

Summary:
- Raised the interactive route layer above the StoryMap card stacking layer.
- Raised the pin SVG above both information windows so the Taiwan and Beijing pins remain visible while their cards are open.
- Kept the line layer behind the information windows and pins.

Files changed:
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed `git diff --check`.
- Confirmed the route layer is z-index 5, the pin SVG is z-index 4, and the information windows remain z-index 3 within the route layer.

Remaining:
- Reload the local preview and confirm both red pins remain visible at Beijing and Taiwan while the Beijing gallery is on any of its three pages.

### 2026-07-30 20:23 HKT — Codex — Use supplied route narrative and reveal the SVG Beijing pin

Summary:
- Replaced the Beijing gallery copy with the three supplied passages about relay-station delivery, military-office registration, and the imperial edict sent to 柴大紀.
- Kept the red outbound route visible after it has appeared; the return layer now replays without first removing the already-visible red line.
- Fixed the Beijing marker reveal by removing the SVG `<g>` element's `hidden` attribute directly instead of assigning an unsupported SVG `hidden` property.

Files changed:
- `Website/storymap/storymap.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed `node --check "Website/storymap/storymap.js"`.
- Passed `git diff --check`.
- Confirmed all three gallery strings match the supplied Traditional Chinese text.

Remaining:
- Hard-refresh the local preview and click the Taiwan pin once; the Beijing pin should appear after the one-second route animation, with the three supplied passages available through its gallery.

### 2026-07-30 20:44 HKT — Codex — Add source image and reference link to the research-difficulty card

Summary:
- Changed `intro-1-3-a` to use `Visual Material/img2_4_2.jpg` as its full backdrop.
- Added a compact upper-corner `參考來源 ↗` button linking to the supplied National Palace Museum page, with the complete citation in its accessible title.
- Updated the card paragraph to refer directly to 《欽定剿平三省邪匪方略》 and removed the stale 戴英從 citation from this card.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed `node --check "Website/storymap/storymap.js"`.
- Passed `git diff --check`.
- Confirmed the image path and supplied external reference URL are present in the section.

Remaining:
- Hard-refresh the local preview and open 引言 → 3. 研究清代奏折的主要困難 to check the image crop and corner-button contrast.

### 2026-07-30 20:46 HKT — Codex — Add the 林爽文 demonstration-case artwork and source link

Summary:
- Updated `intro-1-6-a` with the supplied introductory sentence, `為展示本網站的研究方法及各項功能。`
- Replaced its backdrop with `Visual Material/印版平定台湾战图册6.png`.
- Added the same upper-corner `參考來源 ↗` treatment, linking to the supplied 國家文化記憶庫 record for 〈平定臺灣戰圖（七）生擒逆首林爽文〉.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed `node --check "Website/storymap/storymap.js"`.
- Passed `git diff --check`.
- Confirmed the supplied image path, sentence, and source URL are present in `intro-1-6-a`.

Remaining:
- Hard-refresh the local preview and open 引言 → 案例：林爽文事件 to check the artwork crop and reference-button contrast.

### 2026-07-30 20:49 HKT — Codex — Add the route map to the information-delay case card

Summary:
- Updated `intro-1-6-b` to use the `Fizzy Background` map backdrop and the full red Taiwan-to-Beijing route line.
- Kept the requested text: `第一，資訊傳遞是戰時軍事決策形成的重要環節。`
- Added a corner `參考來源 ↗` link to the local PDF for 賴福順《乾隆重要戰爭之軍需研究》（1984）.
- Left the card as a focused introduction so the map and route remain the main visual evidence for the information-delay point.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed `node --check "Website/storymap/storymap.js"`.
- Passed `git diff --check`.
- Confirmed the static route uses `taiwan-war-report-route-reverse.svg` and the reference link targets the exact local source PDF.

Remaining:
- Hard-refresh the local preview and open 引言 → 案例：林爽文事件 → the first reason card to check the red-line crop and PDF button.

### 2026-07-30 20:59 HKT — Codex — Add the 諭24／硃110 second-level communication comparison

Summary:
- Reworked `intro-1-3-b` for the requested second layer of communication, with the supplied explanation about 乾隆帝's 1月2日上諭 and 常青's 13日後回奏.
- Added two side-by-side embedded sample review-tool panels: 諭24 on the left and 硃110 on the right.
- Added exact-source highlighting to the sample embed URL. 諭24 highlights the coordinated-attack, provincial-troop, and 漳泉-reward passages; 硃110 highlights 常青's implementation and the settled 漳泉 situation.
- Added a compact comparison layout that keeps both document panels visible above the explanatory StoryMap card.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-cards.css`
- `../review-tools/(2) sample/index.html` (sample-only embed highlight support, as explicitly requested)
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed `node --check "Website/storymap/storymap.js"`.
- Passed `git diff --check`.
- Confirmed the canonical source records for 諭24 and 硃110 and used only exact wording for the visual highlights.

Remaining:
- Hard-refresh the local preview and open `#intro-1-3-b` to confirm both review panels load from port 8766 and the highlighted passages are visible.
- The review service was not running during this check and could not be started from the restricted session; keep the normal review server running on port 8766 for the embedded panels.

### 2026-07-30 21:06 HKT — Codex — Add the 硃119 source-network evidence panel

Summary:
- Reworked `intro-1-3-c` for the requested “事件、消息來源與資訊網絡” example.
- Added one embedded sample review-tool panel for 硃119, labelled `同日｜常青亦奏報臺灣軍情與四名消息來源`.
- Added exact-source highlighting for the four passages concerning 廈門蚶江員弁、署守備陳邦光、易連／王增錞, and 廈門同知劉嘉會.
- Added a three-column evidence table with the requested source, report-content, and quotation fields, while correcting the duplicated “的” in the surrounding explanatory paragraph.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed `node --check "Website/storymap/storymap.js"`.
- Passed inline-script parsing for `review-tools/(2) sample/index.html`.
- Passed `git diff --check`.
- Confirmed the canonical 硃119 record and selected only exact source wording for the highlights.

Remaining:
- Hard-refresh the local preview and open `#intro-1-3-c` with the review server running on port 8766 to check the highlighted passages and table layout.

### 2026-07-31 15:11 HKT — Codex — Restore omitted introduction prose in separate source cards

Summary:
- Restored the omitted `Outline/Content.docx` prose in independent source-text cards while preserving the newer visual/demo cards and their backdrops.
- Added three 1.1 source cards, the missing 1.3 source paragraphs, and the missing 1.6 case-introduction and first-reason paragraphs.
- Restored the inline Dai citation immediately after `超過二萬七千頁`, linked to the existing reference entry.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed the bundled `node --check` checks for both website JavaScript files.
- Passed `git diff --check`.
- Browser HTTP preview confirmed 17 intro sections/cards, no empty cards, no card overflow, and the inline reference link targets `../references.html#ref-dai-2019`.

Remaining:
- Review the new source-card backdrop positioning at the preferred browser width; the embedded review panels still require the separate port-8766 server for their content.

### 2026-07-31 15:11 HKT — Codex — Replace StoryMap sample iframes with local review-panel replicas

Summary:
- Replaced the StoryMap's embedded review-tool iframes for 硃83, 諭24／硃110, and 硃119 with local HTML/CSS mock review windows.
- Recreated the document header, metadata, tab strip, scrollable original-text area, and static evidence highlights so the teaching site can demonstrate the review interface without depending on port 8766.
- Left the standalone sample review tool unchanged.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed `node --check "Website/storymap/storymap.js"`.
- Passed `git diff --check`.
- Confirmed no `iframe`, `8766`, or `setReviewFrameSource` reference remains under `Website/storymap/`.

Remaining:
- Hard-refresh the local preview and visually check the three mock panels at `#intro-1-3-b`, `#intro-1-3-c`, and `#intro-1-5`.
- The in-app browser's local-page security policy prevented live visual inspection in this session.

### 2026-07-31 15:26 HKT — Codex — Rebuild the 諭24／硃110 StoryMap panels from sample-tool UI and canonical records

Summary:
- Replaced the abbreviated comparison mockups with panels following the sample review tool's document-card anatomy: document header, metadata table, controls, tab strip, scrollable original-text pane, and highlighted evidence.
- Embedded the complete canonical source bodies for 諭24 and 硃110 from `review-tools/shared data/stage1_original_text.json`.
- Corrected the metadata to the source records' dates and added local tab switching for 原文、AI 摘要、關係.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed `node --check "Website/storymap/storymap.js"`.
- Passed `git diff --check`.
- Confirmed canonical body prefixes and all requested highlight phrases for 諭24 and 硃110 are present.

Remaining:
- Hard-refresh the local preview and compare the panels against the supplied sample-tool screenshot at `#intro-1-3-b`.
- Live browser inspection remains blocked by the local-page security policy in this session.

### 2026-07-31 15:48 HKT — Codex — Match the StoryMap comparison panels to the sample review-tool document UI

Summary:
- Rebuilt the 諭24／硃110 replicas around the sample review tool's actual document-card anatomy: ghost move/minimize/close controls, centered header resize grip, type badge, compact metadata rows, filter/settings strip, and scrollable 原文 pane.
- Kept the complete canonical source bodies and requested evidence highlights for both documents.
- Added local minimize, close, filter, and settings affordances while keeping the two cards visible side by side.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed `node --check "Website/storymap/storymap.js"`.
- Passed HTML nesting validation and `git diff --check`.
- Confirmed both sample panels are present and no StoryMap iframe/8766 references remain.

Remaining:
- Hard-refresh the local preview and compare `#intro-1-3-b` against the supplied sample screenshot; live browser inspection remains blocked by the local-page security policy.

### 2026-07-31 16:00 HKT — Codex — Consolidate source card text and remove duplicate intro copy

Summary:
- Removed the four route/demo paragraphs from the `清代奏折制度` visual card.
- Combined the three `原文補回` source cards into one source card.
- Removed the two specified command/response paragraphs from the 1.3-b comparison card.
- Removed the 1.3-c sentence about 同日奏報 and its source-network evidence table.
- Removed the short duplicate `示範案例：林爽文事件` card while retaining the longer case-background card, and updated the workflow link to the retained card.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Bundled Node syntax checks passed for the StoryMap JavaScript files.
- `git diff --check` passed.
- Live preview contains 14 intro sections; the requested removed phrases and table are absent, the combined source card contains three paragraphs, the longer case card remains, and no card has internal overflow.

Remaining:
- Review the updated intro card spacing during the next visual pass.

### 2026-07-31 16:32 HKT — Codex — Add standalone UI upgrade options prototype

Summary:
- Added a self-contained comparison page with three UI directions: 展示優先、左右分欄、研究工作臺.
- Built three hand-crafted review-tool mock panels with separate tool and long-text zones; the prototype has no external embed and does not connect to formal or sample data.
- Restored the temporary iframe experiment in `intro-1-5` to the existing hand-built mock panel and preserved the current StoryMap content.

Files changed:
- `Website/UI Idea/06-UI-upgrade-options.html`
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check "Website/storymap/storymap.js"` passed.
- `git diff --check` passed.
- Local browser preview confirmed three option sections, three mock panels, and zero `<iframe>` elements in the new page.

Remaining:
- Choose one direction for the next implementation pass; the current page is a visual comparison prototype only.

### 2026-07-31 16:51 HKT — Codex — Refine the standalone UI options page

Summary:
- Updated only `Website/UI Idea/06-UI-upgrade-options.html`.
- Made the opening cover viewport-height and converted each option heading into a compact full-width cover block for the other tabs.
- Removed pill-style labels, kept the option subtitle on one desktop line, and moved each description below its subtitle.
- Simplified Option 02 by removing `Text zone / 02`, the numbered reading index, and the `版面重點` sub-card while retaining its subtitle, sub-subtitle, and point list.

Files changed:
- `Website/UI Idea/06-UI-upgrade-options.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `git diff --check` passed.
- Local browser preview confirmed a viewport-height opening cover, compact Option 02 cover, one-line desktop subtitle, three mock panels, zero `<iframe>` elements, and no pill selectors/text remnants.
- No other HTML file was edited for this adjustment.

Remaining:
- Choose one of the three refined layout directions for implementation in the main intro website.

### 2026-07-31 17:07 HKT — Codex — Polish the standalone options page workflow presentation

Summary:
- Updated only `Website/UI Idea/06-UI-upgrade-options.html`; no other HTML file was edited.
- Removed the dark backdrop from option subtitles and the outer backdrop around each hand-built review-tool panel, and reduced body/stage spacing.
- Replaced the frozen option navigation with a normal in-page row whose four tabs reveal branching workflow previews on hover or keyboard focus.
- Added polished workflow structures for 展示優先、左右分欄、研究工作臺 and 比較, including alternate routes, decision branches and return loops inspired by the supplied workflow reference.

Files changed:
- `Website/UI Idea/06-UI-upgrade-options.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `git diff --check` passed.
- Local browser preview confirmed the plain option headings, transparent review-tool stage, reduced padding, four workflow preview blocks, and non-sticky option row.

Remaining:
- Review the hover workflow previews in the target browser and choose the final layout direction for the main intro website.

### 2026-07-31 17:24 HKT — Codex — Replace option navigation with a whole-tab workflow chart

Summary:
- Updated only `Website/UI Idea/06-UI-upgrade-options.html`; no other HTML file was edited.
- Moved the 展示優先 text into the plain subtitle content area and removed its separate reading card.
- Replaced the `01 展示優先`／`02 左右分欄`／`03 研究工作臺`／`比較` bar and its per-option mini workflows with one whole-page workflow chart below the cover.
- Added top-bar hover/focus behavior for 主頁、引言、第一部分、第二部分、設定. The chart opens below the cover, remains reachable while the pointer moves into it, and its bubbles link to the corresponding page sections.
- Reduced each bubble to a short single-line label and removed visible explanatory text outside the chart.

Files changed:
- `Website/UI Idea/06-UI-upgrade-options.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `git diff --check` passed.
- Local browser preview confirmed the chart is hidden on load, opens after a top-bar interaction, contains nine clickable bubbles, and a chart bubble navigates to its target hash (`#option-b`).
- Confirmed the Option 01 reading card is removed and its text appears directly beneath the subtitle.

Remaining:
- Review the final workflow-chart spacing on a narrow mobile viewport.

### 2026-07-31 17:59 HKT — Codex — Apply the selected UI directions to the intro website

Summary:
- Kept the full-screen cover and existing independent top-tab shell, while upgrading the visible intro sections to the selected UI directions.
- Rebuilt 清代奏折制度 as an Option 03 text-left/map-right layout and folded the long institutional explanation into that card so the next scroll position is 清代奏折上諭的研究價值.
- Rebuilt 研究價值 and 研究成果：「清代奏摺與上諭分析平台」 as Option 02 visual-left/reading-right layouts; the platform demonstration remains a hand-built panel with no iframe or backdrop image.
- Rebuilt the research-difficulty and 林爽文事件 groups as clickable three-folder workbenches. Each active folder expands a full reading panel with a corresponding photo, route, or review-tool UI visual.
- Rebuilt 以數位方法研究清代奏折和上諭 as Option 01, placing the structured method table before the reading text.
- Polished the 引言 hover workflow chart and updated its links for the new section structure. Added keyboard and click behavior for both workbenches.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check "intro Website/Website/storymap/storymap.js"` passed.
- `node --check "intro Website/Website/embedded-tool/review-tool-embed.js"` passed.
- `git diff --check` passed.
- Local browser preview confirmed the full-screen cover, all five independent tab panels, the polished workflow chart, map interaction, Option 02 split panels, Option 01 table-first flow, both three-folder workbenches, clickable folder switching, `字體` settings label, and zero `<iframe>` elements in the page.

Remaining:
- The repeated difficulty instruction was interpreted as the final, more specific Option 03 three-folder workbench; revise the first difficulty card to a separate Option 02 split only if that repeated line was intended as a separate requirement.
- Narrow viewport visual review remains to be done in the target browser.

### 2026-07-31 17:29 HKT — Codex — Polish the whole-tab workflow chart

Summary:
- Updated only `Website/UI Idea/06-UI-upgrade-options.html`; no other HTML file was edited.
- Tightened the chart into a centered hierarchy with fixed, consistent bubble widths, smaller spacing, a shorter reveal area, clearer branch rails, and a connected path to 比較.
- Rebalanced the dark chart surface and node colors so the chart reads as one deliberate navigation map rather than a stretched row of cards.

Files changed:
- `Website/UI Idea/06-UI-upgrade-options.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `git diff --check` passed.
- Local browser preview at desktop width showed the compact centered chart, nine clickable bubbles, no horizontal overflow, and the Option 01 copy directly beneath its subtitle.

Remaining:
- Review the final chart spacing on a narrow mobile viewport.

### 2026-07-31 18:23 HKT — Codex — Refine workbench reading cards and section boundaries

Summary:
- Replaced the difficulty and 林爽文 workbench folder layouts with a fixed mock review panel and a right-side, one-card-at-a-time reading track. Clicking a card scrolls it into place; desktop scrolling updates the active card, while mobile cards expand their own content below the heading.
- Added clear section surfaces and divider lines throughout the introduction, and turned the long platform-result copy into a contained reading card.
- Updated the StoryMap card-layout comments so the two Option 03 blocks describe the new fixed-panel/card-track structure.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check Website/storymap/storymap.js` passed.
- `node --check Website/embedded-tool/review-tool-embed.js` passed.
- `git diff --check` passed for the StoryMap files.
- Local HTTP response contains both fixed mock panels, both card tracks, and the platform-result card content.
- The current in-app browser session rejected navigation from its open UI-idea file to the local StoryMap URL, so the updated visual state could not be reopened there in this turn.

Remaining:
- Open the local StoryMap URL in a browser session that permits the local HTTP origin and review desktop scroll tracking plus the mobile expanded-card state.

### 2026-07-31 18:36 HKT — Codex — Align StoryMap with the UI-upgrade prototype

Summary:
- Compared `Website/storymap/storymap-example.html` with `Website/UI Idea/06-UI-upgrade-options.html` and carried the prototype's visual grammar into the live StoryMap: warm paper background, compact section headings with rules, contained reading columns, lighter editorial surfaces, and the dark mock-tool toolbar anatomy.
- Added a compact intro top screen, preserved the full cover and tab routing, and moved the visible intro sections into the prototype's heading → demonstration → reading flow.
- Changed both workbenches to normal page-flow cards beside a sticky mock panel, so scrolling the page advances the text while the desktop demonstration remains visible.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check Website/storymap/storymap.js` passed.
- `node --check Website/embedded-tool/review-tool-embed.js` passed.
- `git diff --check` passed for the changed StoryMap files.
- Local HTTP markup smoke test found the new intro top screen, option headings, mock toolbar anatomy, brand mark, and workbench markup.
- The in-app browser tab was no longer available to the browser session for a fresh visual screenshot, so visual comparison remains unverified in this turn.

Remaining:
- Reopen the local StoryMap in the browser and review desktop spacing and the mobile stacked-card behavior.

### 2026-07-31 19:04 HKT — Codex — Refine section reading flow and visual hierarchy

Summary:
- Removed the redundant intro transition bar, orange option labels, and explanatory UI copy from the visible StoryMap sections; replaced them with numbered section headings.
- Rebuilt the first two reading sections around one shared map with two sequential text cards, preventing the map and text from overlapping as the reader scrolls.
- Added cumulative click/scroll opening for the three-card workbenches, separate visual panels for each card, clearer section backgrounds/dividers, and a contained result card for the platform description.
- Updated the method-section copy to the requested wording and synchronized the StoryMap card-layout comments.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check Website/storymap/storymap.js` passed.
- Targeted `git diff --check` passed.
- Local HTTP browser preview showed one shared map, separated section surfaces, and no visible overlap in the first two sections.
- Initial workbench cards were folded; clicking opened the selected card, and scrolling opened the next card while keeping the previous card open.

Remaining:
- The desktop interaction is verified locally; a separate narrow-mobile visual pass is still optional.

### 2026-07-31 19:07 HKT — Codex — Restore the previous header version

Summary:
- Restored the header markup and header styling from the commit immediately before the latest StoryMap prototype commit.
- Preserved the latest commit’s content-panel and StoryMap section changes outside the header.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`

Verified:
- Confirmed the first 75 lines of the HTML and first 70 lines of the CSS match the previous commit’s header.
- Passed `git diff --check`.

Remaining:
- None for this change.

### 2026-08-01 — Claude — Rewrite the StoryMap stylesheet and restructure the introduction tab

Summary: Replaced the four layered, mutually overriding CSS passes in
`storymap.css` with a single coherent stylesheet, and rebuilt the introduction
tab so no reading card covers a visual element. Header now centres the tab
names, keeps the settings button on the right, and opens a full-width,
centred chain-style dropdown. Introduction layouts: 01 and 02 place the text
column on the left with the visual on the right; 03 and 06 use the tap-to-expand
card layout with a matching panel; 04 places the lead-in paragraph and the
comparison table under the heading; 05 places the text above a full-width tool
panel. Adopted the two-font system, the dash bullet list with hanging indent,
the bold serif list heading, inline number badges (1–6), and a `--body-weight`
token for global reading-text weight.

Files:
- `intro Website/Website/storymap/storymap.css` (rewritten)
- `intro Website/Website/storymap/storymap-cards.css` (rewritten; obsolete
  absolute-positioning variables removed, per-section accent colours retained)
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.js`
- `intro Website/Website/UI Idea/07-redesign-options.html` (new, options study)
- `intro Website/Website/UI Idea/08-intro-colour-schemes.html` (new)
- `intro Website/Website/UI Idea/09-density-and-tables.html` (new)
- `intro Website/Website/UI Idea/10-table-contrast.html` (new)
- `intro Website/Website/UI Idea/11-text-hierarchy.html` (new)
- `intro Website/Website/UI Idea/12-text-hierarchy-final.html` (new)
- `intro Website/Website/UI Idea/13-combined-preview.html` (new)
- `intro Website/Website/UI Idea/14-dropdown-flowchart.html` (new)

Verified: `node --check` passed for `storymap.js`; `git diff --check` passed;
HTML tag balance checked programmatically (section/div/article all balanced).
No browser QA was performed in this session — this is stated plainly rather
than assumed.

Remaining: Parts 1–3 still use the previous `.story-card` / `.backdrop` markup
and are carried by a clearly-marked transitional block at the end of
`storymap.css`; they should be restructured next, after which that block can be
deleted. The Google Fonts link requires network access; self-hosting Inter and
Noto Serif TC is advisable if the demonstration must run fully offline.
Browser validation of the introduction tab is outstanding.

### 2026-08-01 — Claude — Add a reusable photo gallery component and use it in 引言 01

Summary: Added a `.photo-gallery` component (storymap.css section 7b, init
logic in storymap.js) — clean image stage with left/right arrow navigation,
keyboard arrow support, a "圖 X / N" counter, and a description area below the
image that shows only the title by default and expands to the full
description and reference on hover (click-to-expand on touch devices, via
`(hover: none)`). Replaced section 引言 01（清代奏折制度）'s visual, which had
been the interactive Taiwan–Beijing route map, with this gallery. The route
map (pins, animated route line, and its own embedded page gallery) was
relocated to 引言 06（示範案例：林爽文事件）'s "case-route" panel, replacing a
simpler static route graphic there — this is where the route map's actual
subject matter (Lin Shuangwen-era report transmission) belongs thematically.

Files:
- `intro Website/Website/storymap/storymap.css`
- `intro Website/Website/storymap/storymap.js`
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/UI Idea/15-photo-gallery.html` (new, options study)

Verified: `node --check` passed for `storymap.js`; `git diff --check` passed;
HTML tag balance and gallery/route-map marker counts checked programmatically
(one `data-photo-gallery`, one `data-route-map`, section/div counts balanced).
No browser QA was performed in this session.

Remaining: The two images now shown in 引言 01's gallery
(`img2_4_2.jpg`, `印版平定台湾战图册6.png`) are placeholders reused from
elsewhere in the site — their captions are marked "示範用佔位說明" /
"來源待補" in the data script inside `storymap-example.html` and are not
verified citations. Replace with real images and sourced captions for this
section before publishing. Browser validation of both the gallery and the
relocated route map (section 06) is outstanding.

### 2026-08-01 17:52 HKT — Codex — Replace the first gallery placeholders with supplied source documents

Summary:
- Updated the 清代奏摺制度 card with the exact requested two-paragraph Traditional Chinese text.
- Replaced the placeholder gallery with three supplied sources: 常青奏摺影像, the 十全武功軍報傳遞路線圖, and the 軍機處隨手登記檔 image.
- Rendered the selected PDF pages into web-ready PNG assets and linked each gallery source label back to its local PDF.
- Corrected the inherited `data-photo-gallery-data` attribute typo so the gallery initializer can load its JSON data.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/gallery-npmpdf-page1.png`
- `Website/storymap/gallery-route-map.png`
- `Website/storymap/gallery-register-page2.png`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed `node --check "Website/storymap/storymap.js"`.
- Passed `git diff --check` and HTML tag-balance validation.
- Passed gallery JSON, asset-existence, requested-text, and local-source-link checks.
- Rendered and visually inspected the selected PDF pages before using them as gallery assets.

Remaining:
- Browser visual and interaction QA remains to be performed in the local HTTP preview.

### 2026-08-02 09:51 HKT — Codex — Unify photo galleries and enlarge-on-tap behavior

Summary:
- Converted the standalone research-difficulty and case-background images to the same image-plus-information gallery UI used by the introductory gallery.
- Added enlarged-image lightbox behavior to route-gallery images as well as the standard photo galleries.
- Applied per-image fit, position, and zoom settings independently, resetting route-gallery settings when switching pages so one image cannot inherit another image's dimensions or crop.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed `node --check` for the StoryMap and embedded-tool JavaScript.
- Passed `git diff --check`.
- Passed targeted gallery, lightbox, per-image-setting, route-setting-reset, and HTML tag-balance checks.

Remaining:
- Browser visual and interaction QA remains to be performed in the local HTTP preview.

### 2026-08-02 10:00 HKT — Codex — Reset gallery area when switching pages

Summary:
- Fixed the gallery page-switch state so a touch-expanded information panel is collapsed before the next image is rendered.
- Reset the panel scroll position and optional per-page body-height override, preventing a longer page from leaving its expanded area on a shorter page.

Files changed:
- `Website/storymap/storymap.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed `node --check Website/storymap/storymap.js`.
- Passed `git diff --check`.
- Confirmed page switching removes `is-expanded`, resets scroll position, and reapplies page-specific layout variables.

Remaining:
- Browser visual and touch interaction QA remains to be performed in the local HTTP preview.

### 2026-08-02 10:03 HKT — Codex — Make expanded gallery height page-specific

Summary:
- Removed the shared fixed `32%` expanded-body height that forced every gallery page to occupy the same area.
- Expanded panels now use each page's natural description height, with a configurable maximum; the image stage remains fixed.
- Preserved the page-switch reset so a long page cannot leave its expanded height on a shorter page.

Files changed:
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed `node --check Website/storymap/storymap.js`.
- Passed `git diff --check`.
- Confirmed the shared `32%` expansion rule is removed and the page-specific `--gallery-body-max-h` rule is active.

Remaining:
- Browser visual and touch interaction QA remains to be performed in the local HTTP preview.

### 2026-08-02 10:13 HKT — Codex — Merge the research-difficulty table category

Summary:
- Merged the four research-tool rows under one vertically merged category label: 通信關係、資訊流向複雜.
- Preserved the AI, AI Skills, Python 文本搜尋, and 互動式網站 tools and their explanations.
- Centered the merged category label vertically across the four table rows.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed the old table labels are removed and the new label uses `rowspan="4"`.
- Passed `node --check Website/storymap/storymap.js` and `git diff --check`.

Remaining:
- Browser visual QA remains to be performed in the local HTTP preview.

### 2026-08-02 10:15 HKT — Codex — Split the research-difficulty table into two merged groups

Summary:
- Corrected the table to use two separate two-row groups: 史料數量龐大 for rows 1–2, and 通信關係、資訊流向複雜 for rows 3–4.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed exactly two `rowspan="2"` category cells are present.
- Passed `node --check Website/storymap/storymap.js` and `git diff --check`.

Remaining:
- Browser visual QA remains to be performed in the local HTTP preview.

### 2026-08-02 10:22 HKT — Codex — Standardize inline citations in the reference UI

Summary:
- Converted the inline citations for 莊吉發, 戴英從, and 許毓良 to the requested parenthetical format: `(作者，《書名》，年份)`.
- Linked each inline citation to its entry in `references.html` using the existing `inline-reference` treatment.
- Added the missing 莊吉發 and 許毓良 entries to the reference page.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/references.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed all three citation links and reference anchors are present.
- Passed `node --check Website/storymap/storymap.js` and `git diff --check`.

Remaining:
- Browser visual QA of the citation links remains to be performed in the local HTTP preview.

### 2026-08-02 10:31 HKT — Codex — Add gallery image references

Summary:
- Added the supplied Chinese-style bibliographic references to gallery 1 image 1 and image 3.
- Added the supplied National Palace Museum reference to 研究清代奏折的主要困難 image 1.
- Added the supplied National Cultural Memory Bank reference to 示範案例：林爽文民變 image 1.
- Preserved external links and the 2026/08/02 browsing date where supplied.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed all four gallery source objects contain citation text and a link.
- Passed `node --check Website/storymap/storymap.js` and `git diff --check`.

Remaining:
- Browser visual QA of the expanded gallery references remains to be performed in the local HTTP preview.

### 2026-08-02 09:36 HKT — Codex — Widen the research-results and case-study introductions

Summary:
- Extended the title and introductory text block in 研究成果：「清代奏摺與上諭分析平台」 to the full content width.
- Extended the title and introductory sentence in 示範案例：林爽文民變（1786-1788） to the full content width.
- Preserved the visual panels and expandable case cards below.

Files changed:
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed both section-specific full-width rules are present.
- Passed StoryMap and embedded-tool JavaScript syntax checks and `git diff --check`.

Remaining:
- Browser visual and interaction QA remains to be performed in the local HTTP preview.

### 2026-08-02 09:20 HKT — Codex — Fix collapsed gallery information height

Summary:
- Changed the gallery image stage to fill the available height when the information panel is collapsed.
- Made the information panel auto-height by default, and restored its expanded height only on hover, focus, or touch expansion.

Files changed:
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed the collapsed and expanded gallery flex rules are present.
- Passed StoryMap and embedded-tool JavaScript syntax checks and `git diff --check`.

Remaining:
- Browser visual and interaction QA remains to be performed in the local HTTP preview.

### 2026-08-02 09:18 HKT — Codex — Make the second-card spacing explicit

Summary:
- Added an explicit responsive `margin-top` directly to the `清代奏折的研究價值` card and reinforced it with a section-specific `!important` rule.
- The visible separation is now independent of the shared grid-gap styling.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed both the inline and CSS margin rules are present.
- Passed StoryMap and embedded-tool JavaScript syntax checks and `git diff --check`.

Remaining:
- Browser visual and interaction QA remains to be performed in the local HTTP preview.

### 2026-08-02 09:16 HKT — Codex — Strengthen the section 4 full-width override

Summary:
- Strengthened the section 4 rule so both the introductory block and its body explicitly use `width: 100%` and no `max-width` constraint.

Files changed:
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed both section-specific width rules are present.
- Passed StoryMap and embedded-tool JavaScript syntax checks and `git diff --check`.

Remaining:
- Browser visual and interaction QA remains to be performed in the local HTTP preview.

### 2026-08-02 09:14 HKT — Codex — Widen the digital-methods introduction

Summary:
- Extended the `因此，研究奏摺時` introductory text in section 4 to the full content width of the website.
- Left the section title and comparison table unchanged.

Files changed:
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed the section-specific full-width rule is present.
- Passed StoryMap and embedded-tool JavaScript syntax checks and `git diff --check`.

Remaining:
- Browser visual and interaction QA remains to be performed in the local HTTP preview.

### 2026-08-02 09:13 HKT — Codex — Add spacing above the research-value card

Summary:
- Added dedicated responsive top margin above the `清代奏折的研究價值` card.

Files changed:
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed the second-card margin rule is present.
- Passed `node --check` for the StoryMap and embedded-tool JavaScript and `git diff --check`.

Remaining:
- Browser visual and interaction QA remains to be performed in the local HTTP preview.

### 2026-08-02 09:11 HKT — Codex — Combine the制度與研究價值 cards under one gallery

Summary:
- Moved `清代奏折的研究價值` into the `清代奏折制度` section as a second stacked text card.
- Reused the existing three-image gallery for both cards and removed the separate research-value gallery section.
- Kept the `研究價值` navigation target by assigning it to the moved card.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed `node --check` for the StoryMap and embedded-tool JavaScript.
- Passed `git diff --check`.
- Confirmed the combined section, shared gallery, retained navigation target, removed old section, and balanced HTML tags.

Remaining:
- Browser visual and interaction QA remains to be performed in the local HTTP preview.

### 2026-08-01 18:37 HKT — Codex — Remove hand-built mock-panel labels

Summary:
- Removed all visible `HAND-BUILT MOCK PANEL / 文書研究平台` labels from the StoryMap page.
- Preserved the underlying document-panel content and interactions.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed zero occurrences of the requested label remain.
- Passed `node --check` for the StoryMap and embedded-tool JavaScript.
- Passed `git diff --check` and HTML tag-balance validation.

Remaining:
- Browser visual and interaction QA remains to be performed in the local HTTP preview.

### 2026-08-01 18:29 HKT — Codex — Rewrite the 林爽文民變 demonstration case

Summary:
- Updated the case-study heading to `示範案例：林爽文民變（1786-1788）` and added the requested introductory sentence.
- Replaced the three expandable case cards with `林爽文民變`, `林爽文民變中的資訊傳遞`, and `史料來源`, using the supplied Traditional Chinese text.
- Synchronized the older duplicate case cards so they no longer display the previous headings or wording.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed `node --check` for the StoryMap and embedded-tool JavaScript.
- Passed `git diff --check`.
- Passed requested title, heading, prose, source-text, old-title removal, and balanced-HTML checks.

Remaining:
- Browser visual and interaction QA remains to be performed in the local HTTP preview.

### 2026-08-01 18:24 HKT — Codex — Revise the digital-methods introduction

Summary:
- Replaced the introductory sentence in 以數位方法研究清代奏折和上諭 with the requested explanation of analysing individual documents, communication relationships, and information networks.
- Kept the existing comparison table unchanged.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed `node --check` for the StoryMap and embedded-tool JavaScript.
- Passed `git diff --check`.
- Passed requested-text and balanced-HTML checks.

Remaining:
- Browser visual and interaction QA remains to be performed in the local HTTP preview.

### 2026-08-01 18:20 HKT — Codex — Add the research-difficulty introduction

Summary:
- Added `然而，研究奏折與上諭有不少困難。` directly beneath the 研究清代奏折的主要困難 heading and before the accordion cards.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed `node --check` for the StoryMap and embedded-tool JavaScript.
- Passed `git diff --check`.
- Passed the targeted sentence-presence and balanced-HTML checks.

Remaining:
- Browser visual and interaction QA remains to be performed in the local HTTP preview.

### 2026-08-01 18:15 HKT — Codex — Match the communication-difficulty point form

Summary:
- Changed the two questions in 通信關係複雜 from a numbered list to the dash-led point form used in `13-combined-preview.html`.
- Added the corresponding accordion-list styling for indentation, spacing, and accent-colour dash markers.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed `node --check` for the StoryMap and embedded-tool JavaScript.
- Passed `git diff --check`.
- Passed targeted point-list, wording, and balanced-HTML checks.

Remaining:
- Browser visual and interaction QA remains to be performed in the local HTTP preview.

### 2026-08-03 12:24 HKT — Codex — Center the route line in the case-study second image

Summary:
- Adjusted the second 林爽文民變 image to crop toward the eastern map area where the red route line appears.
- Set the route image to `cover`, right-side positioning, centered vertical positioning, and 1.85× zoom.

Files changed:
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed `git diff --check`.

Remaining:
- Reload the local HTTP preview to confirm the red line is visually centered; fine-tune `--photo-zoom` if necessary.

### 2026-08-03 12:09 HKT — Codex — Add controls for the case-study second image

Summary:
- Added a dedicated card-CSS selector for the `case-route` panel, the second image in 示範案例：林爽文民變.
- Exposed independent `--photo-fit`, `--photo-left`, `--photo-top`, and `--photo-zoom` values for the route image.

Files changed:
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed `git diff --check`.

Remaining:
- Browser visual QA remains to be performed in the local HTTP preview.

### 2026-08-03 11:49 HKT — Codex — Add independent gallery image positioning controls

Summary:
- Added card-CSS controls for each image's shown area and position: `--photo-fit`, `--photo-left`, `--photo-top`, and `--photo-zoom`.
- Added matching group defaults `--gallery-fit`, `--gallery-left`, and `--gallery-top`.
- Updated the existing gallery example to use separate horizontal and vertical controls.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed StoryMap JavaScript syntax checking and `git diff --check`.
- Confirmed the old combined position variables are no longer used.

Remaining:
- Browser visual QA remains to be performed in the local HTTP preview.

### 2026-08-03 11:42 HKT — Codex — Use the supplied intro_1 image directly

Summary:
- Updated the first 清代奏折制度 gallery image to load directly from `Visual Material/Done/intro_1.png`.
- Preserved its descriptive alt text: `常青奏摺影像，乾隆五十一年十二月十一日`.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed StoryMap JavaScript syntax checking and `git diff --check`.
- Confirmed the supplied image path is present in the gallery data.

Remaining:
- Browser visual QA remains to be performed in the local HTTP preview.

### 2026-08-03 11:36 HKT — Codex — Add hover explanations to information-source labels

Summary:
- Added the requested five explanations beneath 情報來源1–5 in the 硃119 source-flow panel.
- Sources 1 and 2 share the 清軍抵達臺灣 explanation; sources 3–5 show their corresponding reported events.
- Made each callout interactive on hover and keyboard focus, with connector positions refreshed during expansion.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed StoryMap JavaScript syntax checking and `git diff --check`.
- Confirmed five source-detail elements are present.

Remaining:
- Browser visual and hover interaction QA remains to be performed in the local HTTP preview.

### 2026-08-03 11:26 HKT — Codex — Replace intro images with Done assets

Summary:
- Replaced the intro's non-GIF images with the requested `Visual Material/Done` set.
- Mapped `intro_1–3` to 清代奏折制度, `intro_4` to the research-difficulty card, and `intro_7–10` to the four 林爽文民變 case images.
- Updated the route-map CSS backdrop to use the rendered `intro_8` asset.
- Kept the GIF and route SVG unchanged.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/done-intro-1.png`
- `Website/storymap/done-intro-2.png`
- `Website/storymap/done-intro-3.png`
- `Website/storymap/done-intro-4.jpg`
- `Website/storymap/done-intro-7.png`
- `Website/storymap/done-intro-8.png`
- `Website/storymap/done-intro-9.png`
- `Website/storymap/done-intro-10.png`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed StoryMap JavaScript syntax checking and `git diff --check`.
- Confirmed the intro image references point to the eight requested Done assets, with only the GIF and route SVG remaining as before.

Remaining:
- Browser visual QA remains to be performed in the local HTTP preview.

### 2026-08-03 10:54 HKT — Codex — Use Fizzy Background PDF in the information-transmission panel

Summary:
- Rendered the supplied `Fizzy Background.pdf` as a web-ready PNG for the `林爽文民變中的資訊傳遞` gallery panel.
- Kept the gallery source link pointing to the original PDF.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/fizzy-background-from-pdf.png`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed StoryMap JavaScript syntax checking and `git diff --check`.
- Confirmed the rendered image exists and the panel retains the original PDF link.

Remaining:
- Reload the local HTTP preview to confirm the backdrop visually.

### 2026-08-03 10:41 HKT — Codex — Fix row-spanned table column styling

Summary:
- Added explicit classes to all `數位工具` and `如何協助研究` body cells.
- Prevented the row-spanned layout from incorrectly applying the orange first-column style to `人工智能技能（AI Skills）` and `互動式網站`.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed StoryMap JavaScript syntax checking and `git diff --check`.
- Confirmed four tool cells and four help cells have explicit styling classes.

Remaining:
- Reload the local HTTP preview to confirm the corrected table visually.

### 2026-08-03 10:40 HKT — Codex — Match the table body column backgrounds

Summary:
- Applied the 人工智能技能（AI Skills） grey background to all body cells in both 數位工具 and 如何協助研究.
- Kept the header row unchanged.

Files changed:
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed `git diff --check`.

Remaining:
- Browser visual QA remains to be performed in the local HTTP preview.

### 2026-08-03 10:36 HKT — Codex — Restyle the digital-tools table column

Summary:
- Applied the table's grey backdrop to the 數位工具 column.
- Changed that column to the standard dark text colour instead of the orange accent colour.

Files changed:
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed `git diff --check`.

Remaining:
- Browser visual QA remains to be performed in the local HTTP preview.

### 2026-08-02 21:08 HKT — Codex — Scale the intro GIF proportionally

Summary:
- Replaced the fixed GIF height with `--visual-scale`.
- The GIF frame now scales its width and height together according to the original 2048×1080 aspect ratio.

Files changed:
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed `git diff --check`.

Remaining:
- Reload the local HTTP preview to confirm the proportional scaling visually.

### 2026-08-02 21:01 HKT — Codex — Widen the intro GIF container

Summary:
- Removed the shared 1560px content-width cap for the research-results section only, allowing the GIF to fill the available page width.

Files changed:
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed `git diff --check`.

Remaining:
- Reload the local HTTP preview to confirm the wider frame visually.

### 2026-08-02 20:59 HKT — Codex — Make the intro GIF height variable effective

Summary:
- Fixed the GIF frame's higher-specificity `height: auto` rule so `--visual-h` now controls its displayed height.

Files changed:
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed `git diff --check`.

Remaining:
- Reload the local HTTP preview to confirm the enlarged frame visually.

### 2026-08-02 10:45 HKT — Codex — Remove browsing dates from gallery references

Summary:
- Removed all `瀏覽日期` text from the gallery source labels.
- Preserved the full citation details and clickable source links.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed no `瀏覽日期` remains in the StoryMap gallery references.
- Passed `git diff --check`.

Remaining:
- Browser visual QA remains to be performed in the local HTTP preview.

### 2026-08-02 10:37 HKT — Codex — Apply PolyU full-reference format to gallery sources

Summary:
- Reformatted all gallery source labels according to the supplied PolyU Chinese thesis style.
- Updated the first gallery's three images, the research-difficulty image, and the case-study image.
- Preserved the supplied external links and browsing date, with Chinese title punctuation and publication ordering.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed `node --check Website/storymap/storymap.js`.
- Passed `git diff --check`.
- Confirmed all five gallery source objects use the new full-reference text.

Remaining:
- Browser visual QA of the expanded reference text remains to be performed in the local HTTP preview.

### 2026-08-01 18:13 HKT — Codex — Refine the research-difficulty cards

Summary:
- Removed the 參考來源 link and visible mock-panel labels from the 研究清代奏折的主要困難 section.
- Replaced the three accordion headings and bodies with the requested content: 史料數量龐大、通信關係複雜、 and 資訊流向複雜.
- Preserved the existing illustrative panel and accordion interaction.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed `node --check` for the StoryMap and embedded-tool JavaScript.
- Passed `git diff --check`.
- Passed targeted checks for removed labels, requested headings and prose, and balanced HTML tags.

Remaining:
- Browser visual and interaction QA remains to be performed in the local HTTP preview.
### 2026-08-02 11:25 HKT — Codex — Load the 硃40 review capture into the research-results card

Summary:
- Replaced the hand-built placeholder review panel in `研究成果：「清代奏摺與上諭分析平台」` with the current light-mode 硃40 review-tool GIF.
- Added the GIF as a local StoryMap asset and preserved its 2048×1080 aspect ratio with an accessible Traditional-Chinese alt description.

Files changed:
- `Website/storymap/zhu40-review-tool-capture.gif`
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed StoryMap and embedded-tool JavaScript syntax checks.
- Passed `git diff --check`.
- Browser QA confirmed one visible GIF image in the section, loaded successfully at its expected 2048×1080 natural dimensions, with the intended wide light-mode presentation.

Remaining:
- None for this insertion; formal and sample review data remain untouched.

### 2026-08-02 11:30 HKT — Codex — Improve the 硃40 review capture clarity

Summary:
- Re-encoded the research-results GIF at the same 2048×1080 size, frame count, and duration with controlled sharpening and optimized palette dithering.
- Preserved the light-mode interface, Traditional-Chinese text, interaction sequence, and website reference.

Files changed:
- `Website/storymap/zhu40-review-tool-capture.gif`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed the GIF remains 2048×1080, 74 frames, and 9.26 seconds.
- Confirmed the existing StoryMap image reference is unchanged.
- Browser QA confirmed the sharpened GIF loads visibly in the research-results section at 2048×1080 natural dimensions and the intended wide layout.
- Passed `git diff --check`.

Remaining:
- None for this clarity improvement; formal and sample review data remain untouched.

### 2026-08-02 20:57 HKT — Codex — Restore the original light color balance

Summary:
- Replaced the darker clarity pass with a new re-encode based directly on the original light-mode GIF.
- Used full-frame palette preservation and gentler sharpening so the original website colors and interface text remain faithful.

Files changed:
- `Website/storymap/zhu40-review-tool-capture.gif`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed the GIF remains 2048×1080, 74 frames, and 9.26 seconds.
- Confirmed the StoryMap reference remains unchanged.
- Browser QA confirmed the color-balanced GIF loads visibly in the research-results section at 2048×1080 natural dimensions with the original light presentation.
- Passed `git diff --check`.

Remaining:
- None for this correction; formal and sample review data remain untouched.

### 2026-08-02 21:02 HKT — Codex — Match the brighter unsolved-state capture

Summary:
- Brightened the GIF’s midtones from the original light-mode capture so the unsolved and panel-open states match the supplied screenshot’s brighter cream background and pale chart lines.
- Preserved the highlight colors, Traditional-Chinese text, interaction sequence, dimensions, and timing.

Files changed:
- `Website/storymap/zhu40-review-tool-capture.gif`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed the GIF remains 2048×1080, 74 frames, and 9.26 seconds.
- Browser QA confirmed the brighter GIF loads visibly in the research-results section at 2048×1080 natural dimensions, with the lighter unsolved/panel-open presentation.
- Passed `git diff --check`.

Remaining:
- None for this brightness correction; formal and sample review data remain untouched.

### 2026-08-02 23:08 HKT — Codex — Add the light 硃119 source-flow document panel

Summary:
- Replaced the old mock panel in `資訊流向複雜` with a light review-tool document-panel replica using the canonical 硃119 metadata and full original text.
- Added four external source bubbles with dynamic connector lines to the corresponding original-text excerpts; the four source categories use distinct highlight colors, with two exact excerpts grouped under 來源3.
- Kept the teaching-site-only filter/settings controls without adding unrelated filter data, and scoped the panel controls so minimize/close behavior does not alter the formal or sample review tools.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed all five rendered highlight spans are exact substrings of `硃119` in `../review-tools/shared data/stage1_original_text.json`, covering all four requested sources.
- Passed `node --check Website/storymap/storymap.js` and `git diff --check`.
- Browser QA on the local StoryMap confirmed the active panel, 4 source bubbles, 5 highlights, 4 SVG connectors, full 硃119 text, and no console warnings/errors.

Remaining:
- None for this insertion. Formal and sample review data remain untouched; no push was performed.

### 2026-08-02 23:45 HKT — Codex — Refine 硃119 panel spacing, metadata, and source marks

Summary:
- Added visible space above the light document panel and limited the panel height so the complete original text is read through the internal scroll area.
- Rebalanced the document title, metadata, and body-text proportions; replaced the date row with `乾隆五十二年發出、硃批。`.
- Reduced the visible annotations to the five requested phrases: `前據各口岸探明`, `據廈門蚶江員弁稟到`, `接據署守備陳邦光稟稱`, `據北淡水署都司易連、新莊巡檢王增錞來稟`, and `據廈門同知劉嘉會稟稱`. Simplified the four external labels to `情報來源1`–`情報來源4`.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed all five requested phrases are exact substrings of canonical `硃119` in `../review-tools/shared data/stage1_original_text.json`.
- Passed `node --check Website/storymap/storymap.js` and `git diff --check`.
- Browser QA confirmed the 700px panel height, scrollable original-text area, 4 bubbles, 4 connectors, 5 requested marks, and no console warnings/errors.

Remaining:
- None for this refinement. Formal and sample review data remain untouched; no push was performed.

### 2026-08-03 00:10 HKT — Codex — Balance the source-flow number labels

Summary:
- Added a left-side `03` visual-element marker to the 硃119 document panel so it balances the existing right-side `03 資訊流向複雜` accordion marker.
- Reused the section’s light teal/accent number treatment and added a small-screen position adjustment.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser QA confirmed the left panel marker and right accordion marker both read `03`, the existing `情報來源1` visibility behavior remains intact, and no console warnings/errors were reported.
- Passed `git diff --check`.

Remaining:
- None for this visual-balance adjustment. Formal and sample review data remain untouched; no push was performed.

### 2026-08-02 23:59 HKT — Codex — Hide off-screen source labels and expose panel controls

Summary:
- Changed the source-annotation layer so an `情報來源` label and connector appear only when its corresponding highlight is inside both the document scroll viewport and the visible page viewport; labels for unscrolled/off-screen excerpts are hidden. `前據各口岸探明` is grouped with 情報來源1.
- Added clearly named panel variables to `Website/storymap/storymap-cards.css` for width, height, four margins, x/y offsets, top source-label space, and mobile top gap.
- Wired the shared panel CSS to those card-level variables so the 硃119 document panel can be repositioned and resized from the section block without editing the shared stylesheet.

Files changed:
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed `node --check Website/storymap/storymap.js` and `git diff --check`.
- Targeted validation confirmed 4 source bubbles, 5 requested highlights, with `前據各口岸探明` assigned to 情報來源1, plus all documented card-level control variables.
- Browser QA confirmed only the currently visible `情報來源1` label and connector are shown at the initial scroll position; hidden labels remain available to appear when their excerpts enter the visible viewport. No console warnings/errors were reported.

Remaining:
- None for this refinement. Formal and sample review data remain untouched; no push was performed.

### 2026-08-03 00:15 HKT — Codex — Align the left source-flow number with the document panel

Summary:
- Fixed the light 硃119 panel’s mirrored `03` marker so it aligns with the top of the document panel instead of floating in the gap beneath the section heading.
- Added `--source-panel-number-top` beside the other card-level panel controls, keeping the marker position easy to adjust from `storymap-cards.css`.

Files changed:
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser QA confirmed the marker top and document-panel top are aligned exactly, the right-side `03` accordion remains active, and only the currently visible `情報來源1` label remains shown.
- No browser console warnings/errors were reported. Passed `node --check Website/storymap/storymap.js` and `git diff --check`.

Remaining:
- None for this alignment fix. Formal and sample review data remain untouched; no push was performed.

### 2026-08-03 00:23 HKT — Codex — Keep only the sample 情報來源 callouts

Summary:
- Removed the mistaken mirrored `03` marker from the light 硃119 document panel.
- Kept the intended `情報來源1`–`情報來源4` callout labels and their left-side connector layout; offscreen labels remain hidden until their highlighted text is visible.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser QA confirmed no `.source-flow-panel-number` remains, `情報來源1` is visible on the left of the document, and `情報來源2`–`情報來源4` remain hidden at the initial scroll position.
- No browser console warnings/errors were reported. Passed `node --check Website/storymap/storymap.js` and `git diff --check`.

Remaining:
- None for this correction. Formal and sample review data remain untouched; no push was performed.

### 2026-08-03 00:33 HKT — Codex — Mirror five numbered 情報來源 callouts

Summary:
- Split the five requested highlighted phrases into five distinct sources: `前據各口岸探明`, `據廈門蚶江員弁稟到`, `署守備陳邦光稟稱`, `據北淡水署都司易連、新莊巡檢王增錞來稟`, and `據廈門同知劉嘉會稟稱`.
- Added matching single-number `情報來源1`–`情報來源5` callout labels on both the left and right sides of the document panel, with independent stacking and connectors for each side.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser QA confirmed 5 distinct highlights, 10 mirrored callout labels, 4 initially visible connectors for the first two visible sources, and no console warnings/errors.
- Passed `node --check Website/storymap/storymap.js` and `git diff --check`.

Remaining:
- None for this source-label balance change. Formal and sample review data remain untouched; no push was performed.

### 2026-08-03 00:44 HKT — Codex — Use one alternating-side label per source

Summary:
- Removed the duplicated mirrored labels so each of the five sources has exactly one callout.
- Kept odd-numbered labels `情報來源1`, `情報來源3`, and `情報來源5` on the left, and even-numbered labels `情報來源2` and `情報來源4` on the right.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser QA confirmed 5 total callout labels, 5 unique source keys, the first label on the left, the second on the right, and no console warnings/errors.
- Passed `git diff --check`.

Remaining:
- None for this alternating-label correction. Formal and sample review data remain untouched; no push was performed.

### 2026-08-03 00:46 HKT — Codex — Add requested case-study source images

Summary:
- Replaced the 02「林爽文民變中的資訊傳遞」visual with the requested single military-report route image, linked to `Fizzy Background.pdf`.
- Replaced the 03「史料來源」mock panel with a two-image gallery showing the cover page from volume 30 of《明清臺灣檔案彙編》and the first page of《天地會》（一）.
- Added web preview PNGs rendered from the two requested cover PDFs; the original PDFs remain the linked source files.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `Website/storymap/gallery-mingqing-taiwan-volume30-cover.png`
- `Website/storymap/gallery-tiandihui-1-cover.png`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Rendered and visually inspected the first pages of the requested PDFs.
- Confirmed the 02 gallery data contains 1 image and the 03 gallery data contains 2 images.
- Passed `node --check Website/storymap/storymap.js`, `node --check Website/embedded-tool/review-tool-embed.js`, and `git diff --check`.

Remaining:
- Local HTTP/browser visual QA passed and local checkpoint `06ce1d6` was created. Formal and sample review data remain untouched; no push was performed.

### 2026-08-03 10:37 HKT — Codex — Hide source labels at the document header

Summary:
- Updated the 硃119 source-label visibility test so a callout hides as soon as its highlight reaches the fixed document header, including the title/metadata area and filter bar.

Files changed:
- `Website/storymap/storymap.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser QA confirmed labels disappear when their highlights move into the panel header zone and reappear for later body highlights; no browser console warnings/errors were reported.
- Passed `node --check Website/storymap/storymap.js` and `git diff --check`.

Remaining:
- None for this header-visibility fix. Formal and sample review data remain untouched; no push was performed.

### 2026-08-03 11:32 HKT — Codex — Clarify image-panel references

Summary:
- Replaced the image-panel prompt `將滑鼠移到此處查看完整說明` with `閱讀更多` for galleries that contain explanatory paragraphs.
- When a gallery has no explanatory paragraph but does have a source, the full linked reference now appears directly below the image title and the prompt is omitted.

Files changed:
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Local HTTP browser QA found `閱讀更多` on description galleries and confirmed the source-only difficulty gallery has no hint, no hidden description container, and a visible full source reference.
- No browser warning/error logs were reported.
- Passed `node --check Website/storymap/storymap.js`, `node --check Website/embedded-tool/review-tool-embed.js`, and `git diff --check`.

Remaining:
- None for this image-panel behavior. Formal and sample review data remain untouched; no push was performed.

### 2026-08-03 15:08 HKT — Codex — Add 硃113 communication document panel

Summary:
- Replaced the second subcard's relationship mock with the light review-tool document-panel replica for 硃113.
- Added four single source callouts: `收發時間`, `回覆先前上諭1`, `回覆先前上諭2`, and `回覆先前上諭3`. The latter three identify 諭20、諭24、諭28 through hover titles containing their exact titles and issue dates.
- Highlighted both 硃113 send/receive dates with the same `收發時間` source key and added multi-highlight support to the connector visibility logic.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed the rendered 硃113 body text matches the canonical `stage1_original_text.json` record exactly.
- Browser QA confirmed the second subcard opens the 硃113 panel, highlights all four requested source ranges, keeps labels hidden above the panel header, reveals the `收發時間` label for the lower date highlights, and exposes the requested hover metadata in the label titles.
- Passed `node --check Website/storymap/storymap.js` and `git diff --check`.

Remaining:
- None for this 硃113 panel. Formal and sample review data remain untouched; no push was performed.

### 2026-08-03 15:16 HKT — Codex — Correct document dates and shorten 硃113 preview

Summary:
- Replaced the generic header date text for both 硃113 and 硃119 with their canonical send and 硃批 dates.
- Shortened the 硃113 panel after the third `欽此。` to `⋯⋯`, retaining the dated footer beginning at 乾隆五十二年正月十四日.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed both header dates against `review-tools/shared data/stage1_original_text.json`.
- Browser QA confirmed both headers, the requested ellipsis, the retained dated footer, and removal of the previously displayed continuation text.
- Passed `node --check Website/storymap/storymap.js` and `git diff --check`.

Remaining:
- None for this date and preview correction. Formal and sample review data remain untouched; no push was performed.

### 2026-08-03 15:52 HKT — Claude — Add the Part 1 interactive interface replica

Summary:
- Replaced the six placeholder `part-1-*` floating-backdrop sections with one sticky `lay-acc` layout: a persistent interactive replica of the sample review tool on the left, and the existing approved explanation cards on the right. All previously approved Traditional Chinese copy was preserved verbatim except the 時間與關係圖表 card, where `奏報事件` was corrected to `戰場事件` to match the real lane label in `review-tools/(2) sample/index.html`.
- Built the replica with four clickable highlight regions (`導覽列`, `時間與關係圖表`, `原始史料區`, `AI 分析區`), numbered hotspots, floating labels, and a progress readout. Selecting a region dims the others; the explanation cards and the replica hotspots drive the same region state.
- Wired the requested interactions: two 導覽列 callouts (`輸入與輸出資料`, `切換介面區域`); four fixed chart dots, one per lane, each opening a 節點資訊區; an AI-Skill filter that marks the extracted ranges inside the 硃42 original text; and the four-step AI sequence (local terminal run → upload prompt pointing at 輸入資料 → AI candidate cards → 加入圖表 creates a new lane dot whose panel and quotation resolve back to the highlighted original text).
- Added `part-1-interface-data.js`, a hand-editable generated data module holding the 硃42 record, the four lane dots, and two AI candidate cards. It is loaded with a plain `<script src>` so the page still works when opened directly from disk.
- Added `tool/scripts py/build_part1_interface_data.py`, which regenerates that module from `review-tools/shared data/stage1_original_text.json` and `review-tools/(2) sample/sample_all.data`, and fails if any quotation is not a literal substring of the canonical body.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/part-1-interface.css` (new)
- `Website/storymap/part-1-interface.js` (new)
- `Website/storymap/part-1-interface-data.js` (new, generated)
- `../tool/scripts py/build_part1_interface_data.py` (new)
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Provenance audit passed: the replica's 硃42 body, title, send/receive dates and rescript are byte-for-byte identical to `stage1_original_text.json`, and every dot and AI candidate matches its record in `sample_all.data` (subtitle, description and quotation). The 皇帝行動 dot's quotation is sourced from 諭24 and is confirmed present in that document; the replica states this instead of pretending the quote is inside 硃42.
- Headless DOM QA with jsdom exercised the full flow: 22 checks passed with no runtime errors, covering region switching, all four lane dots, node panels, quotation location, the AI-Skill filter, the terminal sequence, candidate upload, 加入圖表 creating a fifth dot, and 重設示範 restoring the initial four.
- Passed `node --check` on all three StoryMap JavaScript files and `git diff --check`. No Simplified Chinese was introduced.

Remaining:
- Human browser QA has not been performed: the Claude in Chrome extension was not connected during this session, so visual layout, sticky behaviour and responsive breakpoints were not confirmed in a real browser.
- The lane naming conflict between `AGENTS.md`/`CLAUDE.md` (`戰場事件`) and the previous Part 1 copy (`奏報事件`) was resolved in favour of the real tool label; confirm this is the intended terminology.
- Formal and sample review data remain untouched; no push was performed.

### 2026-08-03 16:06 HKT — Codex — Rebuild the third-part workshop layout

Summary:
- Reorganized 第三部分 around three retained cover bars: `1. OCR 並結構化原始史料`, `2. 運用AI抽取資訊`, and `3. 後續功能：LLM Wiki`.
- Divided the long explanatory text into left/right card layouts and added the requested visual treatments: a policy-interaction chart, five-card tools board, full-width reuse flow, OCR two-card explanation, OCR tool cards, interactive printed-page labels, JSON field chart, interactive AI Chain, and three LLM Wiki cards.
- Kept AI candidates, source paths, researcher decisions, and reusable results visually distinct.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Passed `node --check Website/storymap/storymap.js`, balanced the StoryMap section tags, and passed `git diff --check`.
- Browser QA on the local HTTP preview confirmed three main cover bars, the OCR image/text switch, printed-page label switching, JSON field switching, and AI Chain node switching with no browser warnings or errors.
- Checked the 390px responsive layout and corrected the AI Chain/page-flow overflow; restored the default browser viewport afterward.
- Formal and sample review data remain untouched; no push was performed.

Remaining:
- Review the complete third-part page content and card spacing in the normal browser preview with the existing Part 1 changes included.

### 2026-08-03 16:33 HKT — Codex — Establish the Part 1 sample-tool visual base

Summary:
- Reworked the 第一部分「平台的整體介面」replica shell to follow the sample review tool's basic anatomy: a control toolbar, horizontal four-lane time/relationship chart, and docked document and AI/tool windows.
- Replaced the oversized document preview with a bounded scroll area so 硃42's original text remains available without making the whole replica expand indefinitely.
- Kept the existing separate `part-1-interface-data.js` source boundary and existing interaction hooks for later refinement; this pass prioritizes the visual base rather than the guided interaction choreography.

Files changed:
- `Website/storymap/part-1-interface.js`
- `Website/storymap/part-1-interface.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser preview shows the four horizontal lanes, sample-style toolbar, compact docked panels, and a scrollable document body.
- Browser preview reports no warning/error console entries.
- Passed `node --check Website/storymap/part-1-interface.js` and `git diff --check`.

Remaining:
- Later refine the click sequence, callout placement, and exact sample-tool control behavior after the visual base is approved. Formal and sample review data remain untouched; no push was performed.

### 2026-08-03 17:18 HKT — Codex — Apply 林方／清方 event-and-source result UI

Summary:
- Reworked the Part 1 AI result area to follow the sample tool's 林方／清方 extraction anatomy: actor-group headers, event candidate cards, location/person/date facts, source quotation blocks, and nested source-chain blocks.
- Kept the existing confirmed 林方 event visibly separate from the two reviewable 清方 candidates, using the sample tool's red/blue actor distinction and green confirmed state.
- Added source-quotation定位, source-date demonstration, add, skip, source-chain reveal, and reset behaviour without coupling the replica to the independent explanation cards.

Files changed:
- `Website/storymap/part-1-interface.js`
- `Website/storymap/part-1-interface.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser QA confirmed two groups and three event cards, all three source quotations locate the 硃42 original, a confirmed 清方 candidate creates a new chart dot and reveals its source chain, skip leaves the candidate out of the chart, and reset restores the initial linked-document panel.
- Passed `node --check Website/storymap/part-1-interface.js` and `git diff --check`.
- Formal and sample review data remain untouched; the pre-existing StoryMap Part 3 edits were preserved.

Remaining:
- None for this event-and-source UI pass. No push was performed.
### 2026-08-03 16:49 HKT — Codex — Align Part 3 with UI template and vertical card sequence

Summary:
- Replaced the previous third-part workshop treatment with the layout structure from `Website/UI Idea/13-combined-preview.html`: the existing cover bar style, template cards, split/chart structure, full-width flow, and vertical reading sequence.
- Preserved all original 第三部分 headings and paragraphs verbatim. No explanatory copy or visual-material labels were added.
- Kept the three main step bars: `1. OCR 並結構化原始史料`, `2. 運用AI抽取資訊`, and `3. 後續功能：LLM Wiki`; all cards now appear one after another vertically.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Compared the Part 3 source against the original content: all 45 original paragraphs and 23 original headings are present.
- Browser QA confirmed the template-style cover bars, vertical card sequence, full-width flow, OCR chart labels, and AI Chain label interaction.
- Passed `node --check Website/storymap/storymap.js` and `git diff --check`.

Remaining:
- None for this layout correction. Formal and sample review data remain untouched; no push was performed.

### 2026-08-03 16:49 HKT — Codex — Rebuild Part 1 around the real sample-tool workspace

Summary:
- Replaced the approximate three-row chart treatment with the sample tool's actual visual anatomy: toolbar controls, four vertical type columns, a vertical date ruler, dense relationship-line texture, a linked-information panel, and a right-hand original-document panel.
- Matched the 硃42 document header more closely to the real sample card, including the compact date `1786/12/18-1/2（15 日）` and `明清台檔30, 113, 硃42` source line.
- Removed the replica's JavaScript listeners that opened, closed, or retargeted the right-side explanation cards. Those cards remain independent StoryMap content.

Files changed:
- `Website/storymap/part-1-interface.js`
- `Website/storymap/part-1-interface.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser preview shows the three internal sample-tool columns, four vertical lane headers, dense background relationship lines, scrollable document text, and the real sample-style toolbar order.
- DOM check confirmed 4 lane columns, 112 presentation-only network lines, and a scrollable document panel; browser console had no warning/error entries.
- Passed `node --check Website/storymap/part-1-interface.js` and `git diff --check`.

Remaining:
- Exact chart data density and later guided interactions can be refined after this visual structure is approved. Formal and sample review data remain untouched; no push was performed.

### 2026-08-03 17:08 HKT — Codex — Split the remaining Part 3 sections into individual vertical parts

Summary:
- Divided `3. 選用的AI Model` and `4. Google Cloud` into separate vertical parts.
- Divided the three LLM Wiki paragraphs into three individual vertical parts: `完成 AI 分析及研究者審核後`, `研究者可將已審核的資料`, and `LLM Wiki 於是可以利用這些結構化資料`.
- Positioned the `適合的研究問題` visual to the right of its card, and kept the JSON structure explanation as the right-side visual element beside `9. 輸出格式：JSON`.
- Kept the cover bar, the three main step bars, the template UI, and all original text; added no new explanatory website copy or visual material.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Original-content comparison found all 45 original paragraphs and 23 original headings still present.
- Confirmed the new model, cloud, and three LLM Wiki section IDs exist in the local StoryMap, and the research visual uses the right grid column.
- Passed `node --check Website/storymap/storymap.js` and `git diff --check`.

Remaining:
- None for this requested Part 3 layout adjustment. Formal and sample review data remain untouched; no push was performed.

### 2026-08-03 17:59 HKT — Codex — Add a five-photo resource-card sample for 所需的工具與資源

Summary:
- Kept all five resource descriptions in one `2. 所需的工具與資源` part.
- Reworked the five cards into a stacked creative layout with alternating photo placement, a subtitle, a title, and the original paragraph text in each card.
- Reused five existing local project photos: the platform interface, scanned source material, an illustrated historical source, a route map, and a historical book image.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser preview confirmed five stacked cards, five photos, and five subtitles inside the single tools part.
- Static check confirmed all five original tools paragraphs remain present.
- Passed `node --check Website/storymap/storymap.js` and `git diff --check`.

Remaining:
- None for this requested resource-card sample. Formal and sample review data remain untouched; no push was performed.

### 2026-08-03 17:52 HKT — Claude — Replace 適合的研究問題 text boxes with an interactive swimlane gallery

Summary:
- Replaced the two `.relationship-node` prose boxes in `1. 適合的研究問題` (Part 3) with a two-slide interactive gallery (`.part3-qgallery`) reusing the four-line colour scheme already established in the Part 1 replica (戰場事件 #b5462e／官員上奏 #2f75b5／皇帝硃批下旨 #c46a2b／皇帝行動 #7d4ab8).
- Slide 1 draws three colour-coded, arrow-headed response chains on the same real chain already used elsewhere on the site (硃42 → 諭24 → 硃113): (1) 硃42 responding to four confirmed 戰場事件 dots, (2) three 諭24-derived 皇帝行動 dots responding to 硃42／諭24, (3) 硃113 (a later memorial) responding back to 諭24. Each chain has a coloured floating `Text` callout and a matching legend entry; hovering or clicking either highlights that chain's dots and arrows and dims the others. Clicking any dot opens a small tooltip with its title, description and quotation.
- Slide 2 reuses the identical structure and inserts five additional real 戰場事件 dots (from 硃56, 硃60, 硃71, 硃57, 硃61, all dated between 硃42's send date and 諭24's issue date) plus a `相隔 15 天` annotation, to demonstrate 地理距離與文書傳遞所造成的時間差 with events the emperor had not yet learned of when he wrote 諭24.
- Added `part-3-question-gallery-data.js`, generated by the new `tool/scripts py/build_part3_question_data.py`, which pulls every document, date and quotation from `stage1_original_text.json` and `sample_all.data` and fails the build if any quotation is not a literal substring of its cited document, or if a chosen event has no quotation at all.
- Arrows are drawn in real pixel coordinates (matching the approach already used in `part-1-interface.js`'s connector logic) rather than an abstract SVG viewBox, avoiding marker/scaling distortion.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/part-3-question-gallery.css` (new)
- `Website/storymap/part-3-question-gallery.js` (new)
- `Website/storymap/part-3-question-gallery-data.js` (new, generated)
- `../tool/scripts py/build_part3_question_data.py` (new)
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Provenance audit: all three documents (硃42, 諭24, 硃113) are byte-for-byte identical to `stage1_original_text.json`; every event/emperor-action/transit dot matches its `sample_all.data` record (subtitle, description, quotation) and every quotation is confirmed as a literal substring of its cited document's body. The 15-day transit gap is computed from the real send/announce dates, not hard-coded.
- Headless jsdom QA: 17 checks passed with no runtime errors — both slides render with the expected dot counts (11 and 16), 3 arrow groups and 3 text callouts on slide 1, the gap annotation and 4th legend item on slide 2, legend hover/click highlighting, dot-click tooltips, and prev/next navigation all work.
- Passed `node --check` on all four new/changed JS files and `git diff --check`. No Simplified Chinese was introduced.
- Real browser QA was attempted but could not be completed: the Claude in Chrome extension cannot script `file://` pages without the user first enabling "Allow access to file URLs" for the extension in `chrome://extensions` (itself an internal page the extension also cannot open). Visual layout, arrow geometry, tooltip positioning and label overlap have not been confirmed in an actual browser.
- `.relationship-visual` / `.relationship-node` / `.part3-research-chart` CSS in `storymap.css` is now unreferenced by any HTML; left in place rather than removed, since this task's scope was the research-question visual, not a cleanup pass.

Remaining:
- Human visual QA is needed. Serve the project root (`cd "/Users/creamybanana/Downloads/DH Project" && python3 -m http.server 8765`) and open `http://127.0.0.1:8765/intro%20Website/Website/storymap/storymap-example.html#part-3`, or enable file-URL access for the Claude in Chrome extension and retry. Check: dot/label overlap at each screen width, whether the three floating Text callouts collide with the legend or with each other, and whether the gap annotation on slide 2 sits legibly between the 官員上奏 and 皇帝硃批下旨 lines.
- Orphaned `.relationship-visual`/`.relationship-node` CSS could be removed in a later cleanup pass.
- Formal and sample review data remain untouched; no push was performed.

### 2026-08-03 18:11 HKT — Codex — Add an alternate HTML option for 所需的工具與資源

Summary:
- Added a standalone Option 02 sample in `Website/UI Idea/part3-tools-option-02.html`; the current StoryMap layout remains unchanged.
- Presented the five resource cards as an asymmetric archive wall: one large feature card, three compact cards, and one full-width backup card.
- Each card includes a subtitle, original paragraph text, and one existing local project photo.

Files changed:
- `Website/UI Idea/part3-tools-option-02.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser preview confirmed five cards, five subtitles, five loaded photos, responsive grid layout, and no broken images.
- Passed `git diff --check`.

Remaining:
- None for this standalone layout option. No production StoryMap content or research data was changed.

### 2026-08-03 18:21 HKT — Codex — Add a checklist-and-information-panel HTML option

Summary:
- Added `Website/UI Idea/part3-tools-option-03-checklist.html` as a separate checklist-style sample; the current StoryMap layout remains unchanged.
- Listed all five tools in a left window with checkboxes and active selection styling.
- Added one right-side information window that updates to show the selected tool's photo first and original information text below the photo.

Files changed:
- `Website/UI Idea/part3-tools-option-03-checklist.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser preview confirmed five checklist rows, five information views, five loaded photos, and no broken images.
- Interaction test confirmed selecting `Agentic AI` updates the right panel to `Agentic AI`, marks the row active, and keeps the checked state.
- Passed `git diff --check`.

Remaining:
- None for this standalone checklist option. No production StoryMap content or research data was changed.

### 2026-08-03 18:24 HKT — Codex — Refine checklist row alignment

Summary: Moved the item number to a dedicated left column and the tick box to the far right of each checklist row in the standalone Option 03 HTML sample.

Files changed: `Website/UI Idea/part3-tools-option-03-checklist.html`, `INTRO_WEBSITE_CHANGE_LOG.md`, and `../PROJECT_LOG.md`.

Verified: Browser preview confirmed the number-left / title-middle / tick-right alignment and the checked-state styling. No production StoryMap content or research data was changed.

Remaining: None for this checklist alignment refinement.

### 2026-08-03 18:37 HKT — Codex — Apply the checklist tools window to Part 3

Summary:
- Replaced the five-photo resource cards in the live `2. 所需的工具與資源` section with the checklist-and-information-panel layout.
- The left window now lists tools `1` through `5`; each option has a smaller subtitle beneath its title, and the tick is aligned to the far right.
- The right window shows the selected tool's photo first and the original information text below it. Removed the count/status labels.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap-cards.css`
- `Website/UI Idea/part3-tools-option-03-checklist.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser preview confirmed five checklist rows, five subtitles, far-right tick alignment, five information views, and loaded photos.
- Selecting `Agentic AI` updates the right panel and active row; the live section contains no count/status labels.
- Passed `node --check Website/storymap/storymap.js` and `git diff --check`.

Remaining:
- None for the applied checklist tools window. Existing Part 3 question-gallery changes were preserved.

### 2026-08-03 18:44 HKT — Codex — Enlarge text in the Part 3 tools information panel

Summary: Increased the selected tool title and original information paragraph inside the `所需的工具與資源` visual panel in both the live StoryMap section and the standalone checklist sample. Removed the unused status reference from the sample.

Files: `Website/storymap/storymap.css` and `Website/UI Idea/part3-tools-option-03-checklist.html`.

Verified: Browser preview showed the enlarged panel text; `node --check Website/storymap/storymap.js` and `git diff --check` passed. Existing Part 3 question-gallery changes were preserved.

Remaining: None for this text-size adjustment.

### 2026-08-03 18:51 HKT — Codex — Add adjustable dimensions to the Part 3 tools window

Summary: Added centralized CSS layout controls for the `所需的工具與資源` checklist and information panel. The live StoryMap and standalone sample now expose overall width, checklist-column width, overall height, checklist-row height, and information-photo height as variables.

Files: `Website/storymap/storymap.css` and `Website/UI Idea/part3-tools-option-03-checklist.html`.

Verified: Live browser preview showed all five checklist rows and five information views; selecting a row still changes the information panel. The standalone sample also loaded all five rows and views. Passed `node --check Website/storymap/storymap.js` and `git diff --check`.

Remaining: None for the adjustable tools-window layout.

### 2026-08-03 18:55 HKT — Codex — Enlarge Part 3 tools-window typography

Summary: Increased the text size for the five checklist rows, row numbers, subtitles, tick marks, the `工具清單` and `工具資訊` window headings, and the selected tool's information panel. Increased row height to keep the larger labels readable.

Files: `Website/storymap/storymap.css` and `Website/UI Idea/part3-tools-option-03-checklist.html`.

Verified: Browser preview showed the enlarged checklist and information-panel text with all five rows and both window headings visible. Passed `node --check Website/storymap/storymap.js` and `git diff --check`.

Remaining: None for this typography adjustment.

### 2026-08-03 19:01 HKT — Codex — Move Part 3 tools sizing controls into card CSS

Summary: Added the checklist and information-panel sizing variables to the `#part-3-tools` block in `Website/storymap/storymap-cards.css`, covering overall width, checklist-column width, overall height, row height, and information-photo height.

Files: `Website/storymap/storymap-cards.css`.

Verified: StoryMap browser preview loaded the card with one checklist, five rows, one information panel, and two window headings. Passed `node --check Website/storymap/storymap.js` and `git diff --check`.

Remaining: None for the card-specific sizing controls.

### 2026-08-03 19:11 HKT — Codex — Use fixed px and percentage sizing for Part 3 tools card

Summary: Changed the Part 3 tools card to use a fixed `px` height for the complete checklist and information window, a `%` width for the checklist column, and percentage rows for the information photo and text panel. Added internal scrolling so a smaller fixed height remains usable.

Files: `Website/storymap/storymap.css`, `Website/storymap/storymap-cards.css`, and `Website/UI Idea/part3-tools-option-03-checklist.html`.

Verified: Browser preview rendered the fixed-height card and percentage photo/info split. Existing user-edited Part 3 content changes were preserved. Passed `node --check Website/storymap/storymap.js` and focused `git diff --check` for the three edited sizing files.

Remaining: None for the requested sizing-unit adjustment.

### 2026-08-03 19:20 HKT — Codex — Refresh StoryMap card CSS version for adjustable sizing

Summary: Updated the `storymap-cards.css` query version in the StoryMap HTML so changes made in the `#part-3-tools` sizing block are loaded instead of the cached defaults. The current card settings now apply `1000px` overall height, `25%` checklist width, and `70% / 30%` photo/info proportions.

Files: `Website/storymap/storymap-example.html` and `Website/storymap/storymap-cards.css`.

Verified: Browser inspection identified the stale values before the cache refresh; after changing the stylesheet version, the StoryMap card loaded the updated stylesheet. Existing Agentic AI animation and content edits were preserved.

Remaining: None for the CSS cache-refresh fix.

### 2026-08-03 19:24 HKT — Codex — Let card-level sizing variables override component defaults

Summary: Removed the component-level dimension variables that were overriding `#part-3-tools`. The checklist now uses fallback values only, so the card stylesheet controls the actual layout. Refreshed the StoryMap base stylesheet version as well.

Files: `Website/storymap/storymap.css` and `Website/storymap/storymap-example.html`.

Verified: Browser preview rendered the current `1000px` card with the `70%` photo / `30%` information split, and the Agentic AI animation remained active after selecting its row. Existing animation and content edits were preserved.

Remaining: None for the card-variable inheritance fix.

### 2026-08-04 13:19 HKT — Codex — Make 工具清單 row height adjustable

Summary: Stopped the checklist grid from stretching every row to fill the full card height. `--part3-tools-row-height` now controls the grid track height, with content-required expansion for long labels; the standalone sample uses the same behavior.

Files: `Website/storymap/storymap.css`, `Website/storymap/storymap-cards.css`, `Website/storymap/storymap-example.html`, and `Website/UI Idea/part3-tools-option-03-checklist.html`.

Verified: Browser preview showed compact rows with readable long labels, and the standalone sample loaded all five rows and five information views. Passed `node --check Website/storymap/storymap.js` and focused `git diff --check`.

Remaining: None for the adjustable row-height fix.

### 2026-08-04 13:24 HKT — Codex — Add per-section Part 3 card controls

Summary: Added clearly labelled per-section variables to `Website/storymap/storymap-cards.css` so every Part 3 content card can independently adjust title/body font size, width, height, minimum height, padding, and line height. Added matching controls for the Part 3 chart cards, workflow cards, tools window typography, and OCR/AI/LLM Wiki stage bars. Refreshed the StoryMap stylesheet query version.

Files: `Website/storymap/storymap-cards.css`, `Website/storymap/storymap-example.html`, and this log.

Verified: HTTP browser preview loaded the new stylesheet; all 21 Part 3 content sections reported the card-width control, representative cards had non-zero dimensions and the expected computed font sizes, all three stage bars reported the new sizing layer, and the browser reported no errors or warnings. `node --check Website/storymap/storymap.js` and `node --check Website/storymap/part-3-question-gallery.js` passed. `git diff --check` still reports a pre-existing trailing-space line in the current user-edited `storymap-example.html`; that unrelated line was preserved.

Remaining: None for the requested per-section Part 3 controls. Adjust the variables in the labelled `#part-3-...` blocks when tuning a specific section.

### 2026-08-04 13:34 HKT — Codex — Give each Part 3 card an independent selector

Summary: Added stable IDs to the actual Part 3 multi-card and visual-card elements, including the two OCR definition cards, two AI Skills cards, two AI Chain cards, charts, workflow cards, the tools window, and the three LLM Wiki cards. Added one matching CSS control block per card ID, using the same direct-edit pattern as `#intro-1-2`; single-card sections remain directly adjustable by their section IDs.

Files: `Website/storymap/storymap-example.html`, `Website/storymap/storymap-cards.css`, and this log.

Verified: Confirmed 52 unique Part 3 IDs; every new `-card` and `-chart` ID has a matching selector block. Browser preview loaded `storymap-cards.css?v=20260804-part3-individual-cards`, rendered representative cards with non-zero dimensions, and reported no errors or warnings. `node --check Website/storymap/storymap.js` and `node --check Website/storymap/part-3-question-gallery.js` passed. `git diff --check` still reports the pre-existing trailing-space line in the current user-edited StoryMap HTML; it was preserved.

Remaining: None for individual Part 3 card adjustment.

### 2026-08-04 13:36 HKT — Codex — Match Part 3 basic-flow text to the full-width method layout

Summary: Removed the card treatment from `3. 重用平台的基本流程` and expanded its heading and explanatory paragraph to the full StoryMap content width, matching the text-above-table layout used by `以數位方法研究清代奏折`. The workflow diagram remains below the text as the visual block.

Files: `Website/storymap/storymap-example.html`, `Website/storymap/storymap-cards.css`, and this log.

Verified: HTTP browser preview showed the section heading and paragraph outside a card, with transparent background, no border or padding, and the same 1193px content width as the workflow frame. The browser reported no errors or warnings. `node --check Website/storymap/storymap.js` and `node --check Website/storymap/part-3-question-gallery.js` passed. `git diff --check` still reports the pre-existing trailing-space line at `storymap-example.html:1000`; it was preserved.

Remaining: None for the requested Part 3 basic-flow layout.

### 2026-08-04 13:37 HKT — Codex — Show full text in 工具資訊 without inner scrolling

Summary: Changed the Part 3 tools information pane to a 50% photo / 50% text split and removed the inner text scrollbar, so each current item’s full description remains visible in the information panel. Applied the same behavior to the standalone checklist sample.

Files: `Website/storymap/storymap.css`, `Website/storymap/storymap-cards.css`, `Website/storymap/storymap-example.html`, and `Website/UI Idea/part3-tools-option-03-checklist.html`.

Verified: Browser preview loaded `storymap-cards.css?v=20260804-full-info-01`; all four current StoryMap item views and all five standalone sample views reported visible information content with `overflow: visible`. The Agentic AI animation remained active.

Remaining: None for the full-information-pane adjustment.

### 2026-08-04 13:45 HKT — Codex — Organize Part 3 CSS with numbered card controls

Summary:
- Added a numbered Part 3 CSS index from Part 3.0 through Part 3.7.
- Renamed section-default, stage-bar, visual-card, and individual-card blocks so each adjustment has a precise label such as Part 3.1.2 or Part 3.4.2.1.
- Preserved all existing selectors and sizing values; this change only improves navigation and editing clarity.

Files changed:
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed the numbered index maps to the matching `#part-3-*` selectors.
- Focused `git diff --check` passes for `Website/storymap/storymap-cards.css`.

Remaining:
- None for the CSS organization request.

### 2026-08-04 13:48 HKT — Codex — Make 工具資訊 height content-driven

Summary: Changed the active tool information view to use an automatic text row. Each item’s information panel now sizes itself from its own description, while the photo fills the remaining height of the fixed tools window. The standalone checklist sample uses the same layout.

Files: `Website/storymap/storymap.css`, `Website/storymap/storymap-cards.css`, `Website/storymap/storymap-example.html`, and `Website/UI Idea/part3-tools-option-03-checklist.html`.

Verified: Browser measurements showed different information heights for repository (340px), Agentic AI (384px), AI API (296px), and the backup item (296px), with no inner scrolling. The standalone sample also reported content-driven heights across all five views, and the Agentic AI animation remained active.

Remaining: None for the content-driven information height adjustment.

### 2026-08-04 13:59 HKT — Codex — Put OCR card controls in website order

Summary:
- Reordered the Part 3.4 OCR controls in `storymap-cards.css` to follow the actual StoryMap sequence from the OCR stage through structured-material import.
- Simplified each CSS heading to the visible card title; untitled OCR definition cards use the first ten-word paragraph excerpt, and paired visual blocks are labelled as text card or chart.
- Kept all selectors and sizing declarations unchanged while moving the matching card-control blocks beside their displayed section.

Files changed:
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed the CSS Part 3.4 sequence matches the OCR section order in `Website/storymap/storymap-example.html`.
- `node --check Website/storymap/storymap.js` and `node --check Website/storymap/part-3-question-gallery.js` passed.
- Focused `git diff --check` passes for `Website/storymap/storymap-cards.css`.

Remaining:
- None for the OCR CSS organization request.

### 2026-08-04 14:10 HKT — Codex — Make OCR scanning animation width and height adjustable

Summary:
- Fixed the Part 3.4.2.3 OCR animation sizing control. The animation was capped by the parent grid at `440px`, so changing its child `--ocr-scene-max-w` alone could not make it wider.
- Added `--ocr-scene-column-w` to the same numbered control block and connected the parent grid to it; increased the default animation column to `620px` and the JSON output window to `12em`.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser measurement confirmed the live OCR scene renders at `620px` wide with the updated `1000px` maximum and a visible `12em` output panel.
- `node --check Website/storymap/storymap.js` and `node --check Website/storymap/part-3-question-gallery.js` passed.
- Focused `git diff --check` passes for the edited CSS files.

Remaining:
- None for the OCR animation sizing fix.

### 2026-08-04 14:13 HKT — Codex — Set OCR animation width to 65 percent

Summary:
- Changed `--ocr-scene-column-w` in Part 3.4.2.3 from a fixed `620px` to `65%`, so the OCR animation scales with the Part 3.4 content width.

Files changed:
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser measurement confirmed a `775.43px` animation width inside a `1192.97px` Part 3.4 content area, exactly `65%`.

Remaining:
- None for the percentage-based OCR width adjustment.

### 2026-08-04 14:16 HKT — Codex — Add OCR animation text font controls

Summary:
- Added direct controls for the OCR animation’s JSON text font size, line height, font family, and filename label size in Part 3.4.2.3.
- Preserved the current rendered defaults: `11.5px` JSON text and `11px` filename text.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser measurement confirmed the new controls are active: JSON text `11.5px` with `20.125px` line height, and filename text `11px`.
- Focused `git diff --check` passes for the edited CSS files.

Remaining:
- None for the OCR animation font-control request.

### 2026-08-04 14:22 HKT — Codex — Add OCR output-window width control

Summary:
- Added `--ocr-output-w` to Part 3.4.2.3 so the JSON output window can be adjusted independently from the overall OCR animation width.
- Kept the default at `100%` of the animation area and documented percentage or fixed-pixel values.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser measurement confirmed the output window is using `--ocr-output-w: 100%` and measures `661.78px` inside the `715.78px` animation scene.
- Focused `git diff --check` passes for the edited CSS files.

Remaining:
- None for the OCR output-window width request.

### 2026-08-04 14:28 HKT — Codex — Center OCR output window

Summary:
- Centered the OCR JSON output window horizontally inside the animation scene when its configured width is narrower than the scene.
- Kept the existing output-window width and vertical flow unchanged.

Files changed:
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser measurement confirmed the output window is centered within the animation scene.
- Focused `git diff --check` passes for the edited CSS file.

Remaining:
- None for the OCR output-window alignment request.

### 2026-08-04 14:39 HKT — Codex — Add full-screen OCR PDF page viewer

Summary:
- Added click-to-open full-screen viewing for both OCR document previews: the 硃25 handwritten PDF sequence and the printed PDF sequence.
- Added description text below the page, X/outside-click/Escape close behavior, page counter, left/right buttons, and keyboard ArrowLeft/ArrowRight navigation through each document’s pages.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check Website/storymap/storymap.js` passes.
- `git diff --check` passes for the edited StoryMap files.
- The animation output window remains horizontally centered at its configured width.

Remaining:
- Full-screen click navigation should receive a final in-app visual check after the StoryMap scroll position is focused on the OCR section.

### 2026-08-04 14:46 HKT — Codex — Increase basic-flow step spacing and height

Summary: Increased the vertical gap between each workflow number and its title, and increased the minimum height of every chevron step in `3. 重用平台的基本流程`. The values are controlled by the workflow card’s CSS variables.

Files: `Website/storymap/storymap.css`, `Website/storymap/storymap-cards.css`, `Website/storymap/storymap-example.html`, and this log.

Verified: Browser preview loaded `storymap-cards.css?v=20260804-flow-step-01`; all eight steps measured 170px high with a 22px number-to-title gap. Existing workflow content remained intact.

Remaining: None for the basic-flow spacing and height adjustment.

### 2026-08-04 14:50 HKT — Codex — Correct OCR enlarged-window source references

Summary: Updated the enlarged OCR page viewer so both document sequences show the shared article title, author, and sent date, while the handwritten pages show the full 《宮中檔奏摺—乾隆朝》 reference and both Qing archive links. The printed pages now use the website's concise `明清台檔30, 80, 硃25` reference.

Files: `Website/storymap/storymap.js` and this log.

Verified: `node --check Website/storymap/storymap.js` and `git diff --check` pass. Existing uncommitted workflow, OCR animation, CSS, PDF, and image changes were preserved.

Remaining: None for the OCR enlarged-window reference text.

### 2026-08-04 14:51 HKT — Codex — Rebuild Agentic AI scene with Codex pet and four real-data windows

Summary:
- Replaced the two-window Agentic AI animation in Part 3 with four independently positioned windows: the official AI loop terminal, review-tool HTML writing, 硃25 OCR output, and the official-document review skill.
- Used real project commands, file paths, source-record fields, OCR snippets, and skill steps in the animated window data.
- Restyled the blue robot toward the supplied Codex pet reference, including the fluffy blue head, dark terminal face with `> _`, and a cropped lower body so the full robot does not need to be shown.
- Added independent CSS controls for each window's width, height, left/top position, font size, and 傾斜角度.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Four embedded Agentic AI data blocks parse successfully.
- `node --check` passes for both StoryMap scripts.
- HTTP browser preview shows all four windows animating behind the Codex pet; the configured dimensions, positions, font sizes, and angles are active, with no browser errors or warnings.
- Focused `git diff --check` passes for all four edited StoryMap files.

Remaining:
- None for the Agentic AI four-window animation request.

### 2026-08-04 14:54 HKT — Codex — Smooth and reduce the Agentic AI pet

Summary:
- Replaced the segmented blue-part outlines with continuous radial blue gradients and soft inset shading across the Codex pet’s head, body, and arms.
- Removed the remaining hard borders from the pet components, including the terminal face panel, and reduced the pet container to `27%` width by `50%` height while keeping the lower body cropped.

Files changed:
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- HTTP browser preview shows the smaller, borderless, gradient-shaded pet centered in front of the four animated windows.
- Browser measurement reports `0px` borders for all eleven pet components and no console errors or warnings.
- Focused `git diff --check` passes for the edited StoryMap CSS.

Remaining:
- None for the Agentic AI pet refinement request.

### 2026-08-04 15:22 HKT — Codex — Resize Agentic AI pet and expand work-window source content

Summary:
- Replaced the window titles with the requested task labels: `Run Python`, `Create Website`, `Process OCR`, and `Write Skills`.
- Expanded all four animation sequences with longer source-backed content: the actual Python loop command and outputs, sample review-tool loading code, the 硃25 metadata and original-text excerpts, and the full official-document review Skill stages.
- Added responsive pet-size variables and capped the Codex pet at a readable smaller size; longer terminal content now scrolls without showing a scrollbar.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Four JSON animation blocks parse with 11, 11, 12, and 12 lines; titles match the requested labels.
- HTTP browser preview shows the longer content animating in all four windows; the pet measures `235px × 255.95px` at the checked viewport and no browser errors or warnings were reported.
- `node --check` passes for both StoryMap scripts and focused `git diff --check` passes for the edited StoryMap files.

Remaining:
- None for the Agentic AI title, source-content, and pet-size update.

### 2026-08-04 15:01 HKT — Codex — Align Part 3 workflow steps and OCR cards

Summary:
- Replaced the three detailed Part 3 stage numbers with workflow labels: `步驟二`, `步驟三至五`, and `步驟八`.
- Made all eight basic-flow chevrons buttons. Step 1 now scrolls to `1. 適合的研究問題`, and the other buttons target their corresponding Part 3 content.
- Changed Part 3 card headings to use the intro tab's coloured number squares. Moved `1. 甚麼是 OCR？` into the OCR definition card, added `2. 使用OCR的原因`, and renumbered the remaining OCR cards.
- Added sticky-header scroll offsets for direct card and stage-bar targets.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check Website/storymap/storymap.js` and `node --check Website/storymap/part-3-question-gallery.js` pass.
- `git diff --check` passes.
- In the HTTP browser preview, clicking the first flow button reaches the `適合的研究問題` card and clicking the second reaches the OCR definition card; the cards show 49px coloured squares and the OCR stage bar shows `步驟二`.
- Reloading the nested Part 3 hash keeps the Part 3 panel active; browser console reports no errors or warnings.

Remaining:
- None for this requested Part 3 numbering and navigation adjustment.

### 2026-08-04 15:23 HKT — Codex — Make 工具清單 row height adjustable

Summary:
- Changed the Part 3 `工具清單` grid from content-driven `minmax(..., max-content)` rows to the documented fixed `--part3-tools-row-height` value.
- Removed the duplicate row-height override from `#part-3-tools-card`, so the value in the card CSS control block now reaches the live list items.
- Added a cache-busting version for the updated StoryMap stylesheets while preserving the existing width and Agentic AI sizing changes.

Files changed:
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- At the normal 1280px preview width, the current `--part3-tools-row-height: 100px` produces four 100px list items.
- At the 700px responsive breakpoint, all four rows retain the 100px minimum height.
- Reloaded the cache-busted stylesheet URLs and confirmed no browser errors or warnings.
- `git diff --check` passes.

Remaining:
- None for the adjustable `工具清單` row-height control.

### 2026-08-04 15:11 HKT — Codex — Added the Chinese reference-style rule

Summary:
- Added a rule requiring AI agents to consult the PolyU Chinese writing-format
  PDF before writing or revising Chinese footnotes, citations, or bibliographies.
- Recorded the PDF's key conventions for Chinese quotation marks, title marks,
  footnote placement, first/subsequent citations, and bibliography forms.

Files changed:
- `AGENT.md`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Extracted and visually reviewed the nine-page PDF before writing the rule.
- Confirmed the rule preserves unresolved source details instead of inventing
  citation metadata.

Remaining:
- Apply this reference rule to future Chinese citations and bibliography edits.

### 2026-08-04 15:15 HKT — Codex — Complete OCR enlarged-window Chinese references

Summary: Completed the printed OCR citation from the intro-tab source record as `《明清台灣檔案匯編》，第30冊，頁80，硃25。` and converted the handwritten archive and PDF destinations into embedded links on descriptive text. Adjusted the lightbox image height so the full reference remains visible below the enlarged page.

Files changed:
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`

Verified: The local preview shows the printed full reference and the handwritten caption shows clickable `《清代檔案檢索系統》` and `PDF影像` links. Both captions remain visible below the image; `node --check` passes for `storymap.js`.

Remaining: None for the OCR enlarged-window citation display.

### 2026-08-04 15:18 HKT — Codex — Apply Chinese reference-style ordering

Summary: Reordered the handwritten OCR citation to follow the PolyU Chinese reference rule: author, article title, source collection, date, archive number and item, then institution/database and access date. The existing embedded archive and PDF links were retained.

Files changed:
- `Website/storymap/storymap.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`

Verified: The citation now begins `黃仕簡，〈奏聞臺灣彰化縣賊匪殺官陷城及奴才辦理赴剿緣由事〉，《宮中檔奏摺—乾隆朝》` and preserves all verified source details.

Remaining: Browser recheck and local checkpoint.

### 2026-08-04 15:28 HKT — Codex — Keep Agentic AI pet size fixed across viewport widths

Summary:
- Changed the Codex pet width and height controls from viewport-relative `clamp()` values to fixed `235px × 256px` values.
- Fixed the terminal-face and body-face font sizes as well, so the robot’s visual scale does not change when the screen width changes.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser measurements at 1280px and 800px viewport widths both report `235px × 256px` for the pet and `22px` for the face text.
- No browser errors or warnings were reported.
- Focused `git diff --check` passes for the edited CSS files.

Remaining:
- None for the fixed-size Codex pet update.

### 2026-08-04 15:31 HKT — Codex — Show the complete summary Skill in Write Skills

Summary:
- Replaced the short stage list in the `Write Skills` window with the full source-backed `tool/skills md/quick-summary.md` content.
- The animated window now shows the Skill name, `Kind: summary`, the complete Traditional-Chinese Website Prompt, purpose, distinction from richer schema Skills, and its terminal, website, and proxy usage paths.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- The four Agentic AI data blocks parse successfully; `Write Skills` contains 18 animated lines.
- HTTP browser preview completed all 18 lines with scrolling and reported no browser errors or warnings.
- Focused `git diff --check` passes for the updated StoryMap HTML.

Remaining:
- None for the full summary Skill display.

### 2026-08-04 15:23 HKT — Codex — Remove repeated OCR caption prefix

Summary: Removed the repeated article title, author, sent date, and `第 N 頁` label from both OCR enlarged-image captions. The handwritten and printed source references remain below the image, while the separate page counter and left/right navigation remain available.

Files changed:
- `Website/storymap/storymap.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`

Verified: Browser preview captions now show only the source references: the handwritten archive citation and the printed `《明清台灣檔案匯編》，第30冊，頁80，硃25。` entry.

Remaining: Local checkpoint.

### 2026-08-04 15:26 HKT — Codex — Restore title and date inside OCR references

Summary: Added `黃仕簡，〈為奏彰化失陷已調兵赴臺事〉（1786/12/10）` to both OCR source references while keeping the article’s archival citation order and existing embedded links.

Files changed:
- `Website/storymap/storymap.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`

Verified: The reference now contains the requested title, author, and Gregorian date without restoring the repeated caption prefix.

Remaining: Browser recheck and local checkpoint.

### 2026-08-04 15:44 HKT — Codex — Add PaddleOCR point-form card and GitHub visual

Summary:
- Converted the three PaddleOCR advantages into the intro website's dash-led point-form list UI.
- Added the supplied `PaddleOCR.png` as a visual box on the left of the PaddleOCR text card, with a linked info panel labelled `PaddleOCR GitHub`.
- Used the visible repository identity in the image (`PaddlePaddle/PaddleOCR`) to link to the canonical GitHub repository.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- HTTP browser preview shows the visual box on the left, the PaddleOCR text card on the right, three point-form items, and the `PaddleOCR GitHub` link.
- The image path, alt text, GitHub href, three list items, and two-column grid were checked in the live page; no browser errors or warnings were reported.
- Focused `git diff --check` passes for the updated StoryMap files.

Remaining:
- None for the PaddleOCR point-form and visual-link update.

### 2026-08-04 15:52 HKT — Codex — Move PaddleOCR text left and make the visual photo-only

Summary:
- Reversed the PaddleOCR two-column layout so the text card is on the left and the image is on the right.
- Replaced the custom repository visual and `PaddleOCR GitHub` info panel with the StoryMap's standard photo-gallery component, using only the supplied photo and no visible title, description, or source panel.
- Kept the image in `contain` mode so the full screenshot remains visible.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser preview shows the PaddleOCR text card on the left and the photo-only gallery on the right at 1280px width.
- Live-page checks confirm the gallery body is hidden, the image loads from `PaddleOCR.png`, and the gallery JSON contains only one image entry.
- `node --check`, gallery JSON parsing, file existence, and `git diff --check` all pass.

Remaining:
- None for this layout adjustment.

### 2026-08-04 15:57 HKT — Codex — Restore the linked PaddleOCR info panel

Summary:
- Restored the visible info panel beneath the PaddleOCR photo.
- Made the panel text exactly `PaddleOCR GitHub` and embedded the PaddleOCR GitHub URL directly in that label.
- Added a reusable gallery `titleHref` field so linked gallery titles render as accessible links.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser preview shows the text card on the left, the photo on the right, and one visible linked info-panel label reading `PaddleOCR GitHub`.
- Live-page checks confirm the label text, GitHub href, image path, and panel visibility; no browser errors or warnings were reported.
- `node --check`, gallery metadata parsing, and `git diff --check` pass.

Remaining:
- None for this panel correction.

### 2026-08-04 16:19 HKT — Codex — Add independent PaddleOCR photo-width control

Summary:
- Added `--paddleocr-photo-width` to control only the PaddleOCR GitHub gallery width in `storymap-cards.css`.
- Made the gallery image stage use the supplied image's 2:1 aspect ratio, so changing the width automatically changes the image height.
- Fixed the text-card track at `74ch`, so adjusting the photo width does not resize the text card on desktop.

Files changed:
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser preview reports a 668.9px text card and a 501.0px photo at the default `--paddleocr-photo-width: 42%`; the photo stage ratio is 2.00 and the info panel remains visible.
- Browser preview shows no errors or warnings.
- `node --check` and `git diff --check` pass.

Remaining:
- To resize the photo, edit `--paddleocr-photo-width` in the `#part-3-paddleocr` block.

### 2026-08-04 16:29 HKT — Codex — Cap PaddleOCR gallery width by Part 3 percentage

Summary:
- Added `--paddleocr-photo-max-width` so the adjustable PaddleOCR GitHub gallery cannot exceed a chosen percentage of the Part 3 width.
- Clamped the gallery against both that percentage cap and the remaining space beside the fixed text card.

Files changed:
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser preview reports `--paddleocr-photo-width: 42%`, `--paddleocr-photo-max-width: 60%`, a 2.00 image aspect ratio, and the visible `PaddleOCR GitHub` label.
- `node --check` and `git diff --check` pass.
- Existing concurrent Agentic AI edits remain preserved and uncommitted.

Remaining:
- Change `--paddleocr-photo-width` or `--paddleocr-photo-max-width` in the `#part-3-paddleocr` block to adjust the current width or its maximum.

### 2026-08-04 16:40 HKT — Codex — Fix the invisible Agentic AI × PaddleOCR animation

Summary:
- Fixed the Part 3 Agentic AI × PaddleOCR animation frame so its absolutely positioned windows receive a real inner height.
- Preserved the existing `.visual-frame` height control and the independent window size/position variables.

Files changed:
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser geometry now reports a 266.8px visible `.agentic-scene` with rendered PaddleOCR Python and Codex windows; both animation sequences contain generated `.line` elements.
- Browser console reports no errors or warnings.
- `node --check` and `git diff --check` pass.

Remaining:
- None for the visibility bug. Existing concurrent Agentic AI HTML, JavaScript, and card-control edits remain preserved and uncommitted.

### 2026-08-04 16:48 HKT — Codex — Place and enlarge the Agentic AI × PaddleOCR visual

Summary:
- Restored the Part 3 text-card/visual two-column layout, placing the animation on the right of its text card on desktop.
- Added an independently adjustable `--agentic-frame-height` control, enlarged the overlapping windows, and made the animation frame backdrop transparent.
- Added a cache-busting stylesheet version so the updated card controls load reliably after CSS edits.

Files changed:
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser geometry reports a 501.9px text column beside a 668.1px visual column; the transparent frame is 665.6px tall and the inner scene is 612.4px tall.
- Both PaddleOCR Python and Codex windows fit within the scene, and the browser console reports no errors or warnings.
- `node --check` and `git diff --check` pass.

Remaining:
- Adjust `--agentic-frame-height` and the window variables in `#part-3-agentic-ocr-chart` if a different desktop composition is preferred. The mobile override keeps the card above the visual.

### 2026-08-04 16:57 HKT — Codex — Make Agentic AI windows clickable and remove the frame border

Summary:
- Removed the border from the transparent Agentic AI × PaddleOCR visual frame.
- Made the whole Codex and PaddleOCR Python windows clickable so the selected window is brought to the front; the exposed title bars remain available when the windows overlap.

Files changed:
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser reports `0px none` for the frame border and a transparent frame background.
- Clicking the visible `PaddleOCR Python` and `Codex` window labels switches z-index between `3` and `2` as intended.
- Browser console reports no errors or warnings; `node --check` and `git diff --check` pass.

Remaining:
- None for this interaction and frame styling change.

### 2026-08-04 17:00 HKT — Codex — Add Codex working and completed-result phases

Summary:
- Removed the incorrect static `Worked for 10m 1s` text.
- Split the Codex animation into a larger-text working/thinking phase and a completed-result phase.
- When the work phase finishes, it is hidden and only the PaddleOCR installation result remains visible; re-entering the scene starts the work phase again.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- During playback, `Working…` is visible, the thinking font computes to `16px`, and the result phase is hidden.
- After completion, the thinking phase is hidden and six result lines are visible; `Worked for 10m 1s` is absent.
- Browser console reports no errors or warnings; `node --check` and `git diff --check` pass.

Remaining:
- None for the Codex phase behavior.

### 2026-08-04 17:11 HKT — Codex — Add Codex completion footer and window transitions

Summary:
- Added `Worked for 5m 44s` to the completed Codex output footer.
- Added linked `PaddleOCR quick start` and `OCR pipeline guide` file items plus four compact Codex/Python/PaddlePaddle/PaddleOCR brand marks.
- Matched the user prompt and output text at `16px` and added card-like transform, opacity, and shadow transitions when switching windows.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- During thinking, the footer is hidden, the prompt and thinking text both compute to `16px`, and the result is hidden.
- After completion, the footer displays with the requested duration, two guide links, four logos, and six result lines; the thinking phase is hidden.
- Window switching toggles the front class and z-index for both windows; transitions compute as `transform .32s`, `opacity .24s`, and `box-shadow .32s`.
- Browser console reports no errors or warnings; `node --check` and `git diff --check` pass.

Remaining:
- None for this Codex output-footer and switching transition change.

### 2026-08-04 17:32 HKT — Codex — Simplify the completed Codex output

Summary:
- Removed the Files links, file icons, and four logo marks from the completed Codex state.
- Moved `Worked for 5m 44s` into the result body above the PaddleOCR installation-complete message.
- Kept the working phase free of the completion line and preserved the matching `16px` prompt/output typography.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- During playback, the result is hidden and `Worked for 5m 44s` is not visible.
- After completion, the result begins with `Worked for 5m 44s`, followed by `PaddleOCR is now installed and verified on your Apple Silicon Mac.`
- No footer, Files links, file icons, or brand-logo elements remain; browser console reports no errors or warnings.
- `node --check` and `git diff --check` pass.

Remaining:
- None for this output simplification.

### 2026-08-04 17:48 HKT — Codex — Remove the Python-code section and expand format guidance

Summary:
- Removed the `執行 OCR 的Python 代碼` section from Part 3.
- Renumbered the following Part 3 OCR sections from 6 through 11.
- Rebuilt `檢視史料的版面及格式` as a no-card, full-width text section matching the research-results presentation.
- Split the content into the requested two paragraphs: using PaddleOCR and checking font/layout characteristics.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser confirms `#part-3-code` is absent, `#part-3-format` has two paragraphs, and the title/body article spans the full 1192.97px website content width.
- The format article has transparent background and no border.
- Browser console reports no errors or warnings; `git diff --check` passes.

Remaining:
- None for this Part 3 sequence and full-width text change.

### 2026-08-04 16:59 HKT — Codex — Add book-scanner gallery to OCR materials preparation

Summary:
- Replaced the text-only `OCR 前的材料準備` layout with a two-column card and the shared single-image gallery UI used by `研究清代奏折的主要困難`.
- Added `book_scanner_202401.png`, the title `理大圖書館中的掃描器`, a Traditional-Chinese description, and an embedded source link to the PolyU Library book-scanning page.
- Added card CSS controls for gallery width, height, mobile height, image fit, image position, zoom, and expanded-description height.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-cards.css`
- `Website/Visual Material/book_scanner_202401.png`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser loaded the supplied 860×639 PNG and rendered the title, description, source link, and `閱讀更多` gallery behavior.
- Desktop computed layout is a two-column `597.297px 572.625px` card/gallery arrangement with a 620px gallery height.
- Gallery CSS controls compute to `contain`, centered image position, and 1× zoom; the official PolyU source URL is present in the link.
- Gallery JSON parses successfully, the image asset exists, `node --check` passes, and `git diff --check` passes.

Remaining:
- None for this requested gallery addition.

### 2026-08-04 17:46 HKT — Codex — Style the materials copyright note

Summary:
- Marked the copyright and database-terms reminder in `OCR 前的材料準備` as a separate note.
- Styled it as smaller orange text without changing the wording or the other body paragraph.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser computes the note as `rgb(196, 93, 56)`, 12px, weight 600, with the original Traditional-Chinese text intact.
- `node --check` and `git diff --check` pass.

Remaining:
- None for this styling adjustment.

### 2026-08-04 19:46 HKT — Codex — Make Part 3.7 backdrop white

Summary:
- Changed the `辨識印刷字` section backdrop from the shared beige `surface-c` color to white.
- Used a higher-specificity card CSS override so the shared Part 3 surface rule cannot replace it.

Files changed:
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser computes `#part-3-printed` background as `rgb(255, 255, 255)` while the title and interactive explorer remain present.
- `node --check` and `git diff --check` pass.

Remaining:
- None for this backdrop adjustment.

### 2026-08-05 12:58 HKT — Codex — Expand Part 3.8 handwritten-text body

Summary:
- Expanded only the `辨識手寫字` article and body paragraph to the full website content width.
- Left Part 3.7 `辨識印刷字` and the handwritten interactive explorer unchanged.

Files changed:
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser computes the Part 3.8 article, body, and paragraph at `1192.97px`, matching the website content width.
- The handwritten explorer remains present below at `1152px`.
- `node --check` and `git diff --check` pass.

Remaining:
- None for this Part 3.8 width adjustment.

### 2026-08-05 13:09 HKT — Codex — Enhance OCR handwritten page clarity

Summary:
- Created clearer, higher-resolution versions of the four `硃25` handwritten OCR pages while preserving the archival page composition, text, annotations, seals, watermark, and paper texture.
- Saved the originals unchanged and updated the live StoryMap OCR animation and Part 3 feature data to use the enhanced assets.

Files changed:
- `Website/storymap/ocr-zhu25-handwritten-1-enhanced.png`
- `Website/storymap/ocr-zhu25-handwritten-2-enhanced.png`
- `Website/storymap/ocr-zhu25-handwritten-3-enhanced.png`
- `Website/storymap/ocr-zhu25-handwritten-4-enhanced.png`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser loads `ocr-zhu25-handwritten-1-enhanced.png` at `1466×1073` from the updated gallery path.
- All four enhanced files exist and the gallery metadata references the enhanced filenames.
- The enhanced outputs were visually inspected for clearer ink edges, page texture, red annotations, seals, watermark, and margins.

Remaining:
- The original four page images remain available under their original filenames for comparison or rollback.

### 2026-08-05 13:20 HKT — Codex — Enhance OCR printed page clarity

Summary:
- Created clearer, higher-resolution versions of the two `硃25` printed OCR pages while preserving the printed characters, headings, page numbers, margins, and clean page composition.
- Saved the originals unchanged and updated the live StoryMap OCR animation and Part 3 printed-text panel to use the enhanced assets.

Files changed:
- `Website/storymap/ocr-zhu25-printed-1-enhanced.png`
- `Website/storymap/ocr-zhu25-printed-2-enhanced.png`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser loads `ocr-zhu25-printed-1-enhanced.png` at `995×1580` in both the OCR animation and the Part 3 printed-text panel.
- The OCR page list references both enhanced printed assets.
- The enhanced outputs were visually inspected for sharper type edges, preserved headings, page numbers, margins, and page layout.

Remaining:
- The original two printed page images remain available under their original filenames for comparison or rollback.

### 2026-08-05 13:48 HKT — Codex — Rework printed-text feature labels and OCR guidance

Summary:
- Replaced the printed-text explorer's old labels with `文本資訊`, `橫排單欄`, `分段`, `頁碼`, `標題符號`, `夾批`, and `落款與尾批`.
- Updated every feature's description, AI prompt, Python example, and JSON output to match the requested 《明清臺灣檔案彙編》 workflow, including metadata extraction, right-to-left reading order, indentation-based paragraphs, page numbers, emperor's inline 硃批, and separate footer dates.
- Removed the unrequested printed-text labels for `正文`, `收錄註記`, and the old `頁碼（續頁）` presentation.
- Updated the individual label and highlight coordinates in the Part 3 CSS; left the handwritten feature data unchanged.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Both embedded Part 3 feature JSON blocks parse successfully.
- The printed explorer renders seven requested labels; clicking `夾批` switches to page 2 and clicking `落款與尾批` shows the separate date/尾批 output.
- The handwritten explorer still renders its original seven labels and two-fold interaction.
- `node --check Website/storymap/storymap.js`, `git diff --check`, and browser console checks pass.

Remaining:
- The handwritten labels/content remain unchanged because no replacement list was specified for that section.

### 2026-08-05 13:54 HKT — Codex — Remove page badges and move printed 硃批 labels left

Summary:
- Removed the off-page `p.2` badges from Part 3 explorer labels.
- Moved `夾批` and `落款與尾批` to the left side of the printed-page explorer.
- Bumped the StoryMap JavaScript cache key so the browser loads the updated label renderer.

Files changed:
- `Website/storymap/storymap.js`
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Page-two labels display as `夾批` and `落款與尾批` without `p.2`.
- Computed label geometry places both labels on the left side.
- JavaScript syntax, diff whitespace, and browser console checks pass.

Remaining:
- None for this label adjustment.

### 2026-08-05 15:19 HKT — Codex — Separate handwritten labels to prevent overlap

Summary:
- Re-spaced the handwritten labels on both sides so labels from different pages do not occupy the same vertical position.
- Refreshed the CSS cache key after the position adjustment.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser reports zero intersecting label rectangles.
- Labels display without `第 x 摺` text and without console errors.

Remaining:
- None for this label adjustment.

### 2026-08-05 14:00 HKT — Codex — Preserve handwritten fold indicators

Summary:
- Kept the printed explorer free of `p.2` badges while preserving the handwritten explorer's fold indicators such as `第 4 摺`.
- Bumped the StoryMap JavaScript cache key again and verified the final rendered labels in both explorers.

Files changed:
- `Website/storymap/storymap.js`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Printed labels show no page suffixes.
- Handwritten labels retain their fold numbers.
- Printed `夾批` and `落款與尾批` remain on the left side; browser console checks pass.

Remaining:
- None for this correction.

### 2026-08-05 14:04 HKT — Codex — Remove the remaining printed page suffix

Summary:
- Confirmed that printed Part 3 labels should use plain feature names with neither `p.1` nor `p.2`.
- Refreshed the StoryMap script cache key so the browser loads the no-badge renderer consistently.
- Preserved handwritten fold indicators such as `第 4 摺` and the existing left-side placement of `夾批` and `落款與尾批`.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser output: printed labels are `文本資訊`, `直排單欄`, `分段`, `頁碼`, `標題符號`, `夾批`, and `落款與尾批`, with no page suffix.
- Handwritten labels retain their fold indicators.
- Browser console has no errors or warnings.

Remaining:
- None for this label adjustment.

### 2026-08-05 14:37 HKT — Codex — Add source-text samples to printed OCR JSON

Summary:
- Added short original-text excerpts to the OCR JSON windows for `直排單欄`, `分段`, and `標題符號`.
- Used source wording from the OCR evidence so the examples demonstrate reading order, paragraph grouping, and punctuation in context.
- Refreshed the StoryMap script cache key for the updated JSON windows.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- The embedded data for the three feature windows contains the new original-text samples in their JSON panels.
- The embedded page data remains valid, JavaScript syntax passes, and diff whitespace checks pass.

Remaining:
- The displayed excerpts remain OCR evidence and should not be treated as researcher-confirmed transcription without image checking.

### 2026-08-05 15:07 HKT — Codex — Rework handwritten OCR feature labels

Summary:
- Removed `首行「奏為奏聞事」`, `摺縫`, and the old combined seal feature.
- Added `正文字體`, `上奏官員`, `浮水印`, and `印章`; revised `直排單欄`, `臣字款`, `抬頭`, and `硃批（草書）` guidance.
- Assigned the features to the requested first, third, and sixth pages and placed their labels on the requested left or right sides.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Handwritten labels now render as `直排單欄`, `正文字體`, `上奏官員`, `臣字款`, `抬頭`, `硃批`, `浮水印`, and `印章`.
- Feature data contains matching AI prompts, Python examples, and OCR JSON output; removed feature keys are absent.
- Browser placement checks and console checks pass.

Remaining:
- OCR guidance remains a teaching example; the scan should still be image-checked before treating extracted text as confirmed transcription.

### 2026-08-05 15:18 HKT — Codex — Remove fold numbers from handwritten labels

Summary:
- Removed the `第 x 摺` badge text from handwritten Part 3 labels.
- Kept the feature names and their page/side positions unchanged.
- Refreshed the StoryMap script cache key.

Files changed:
- `Website/storymap/storymap.js`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Handwritten labels display only `直排單欄`, `正文字體`, `上奏官員`, `臣字款`, `抬頭`, `硃批`, `浮水印`, and `印章`.
- Printed labels remain without page badges.
- JavaScript syntax and browser console checks pass.

Remaining:
- None for this label adjustment.

### 2026-08-05 15:22 HKT — Codex — Map features to website pages

Summary:
- Corrected the handwritten feature assignments to use the website's six accordion pages rather than PDF pages or individual scan subparts.
- Kept page 1 features on panels 0–1, moved `抬頭` and `硃批（草書）` to website page 3, and moved `浮水印` and `印章` to website page 6.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser indicators progress through `頁 1 / 6` to `頁 6 / 6`.
- Feature mapping resolves to website pages 1, 3, and 6 as requested; labels remain non-overlapping and contain no fold-number text.

Remaining:
- None for this page-mapping adjustment.

### 2026-08-05 15:30 HKT — Codex — Remove JSON field names from handwritten guidance

Summary:
- Removed explicit JSON field and column names from the handwritten Part 3 版面特徵 and AI Prompt text only.
- Preserved the user's current handwritten feature adjustments and left the Python and OCR JSON examples unchanged.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- The rendered handwritten feature data contains no technical field names in any `desc` or `prompt` value.
- All eight handwritten labels remain visible without overlap, and the browser reports no errors or warnings.

Remaining:
- The OCR examples remain instructional evidence and should still be checked against the scanned images before being treated as confirmed transcription.
