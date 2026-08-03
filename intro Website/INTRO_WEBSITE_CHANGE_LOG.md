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
