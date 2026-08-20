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
- `Website/storymap/storymap-example.html`
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

### 2026-08-07 15:30 HKT — Codex — Make the 試一試 mode switch rectangular

Summary:
- Changed the `印刷字／手寫字` switch container and buttons from pill-shaped controls to straight-corner rectangles.
- Kept the switch aligned to the right edge of the 1／2／3 progression row.

Files changed:
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser check at 1150×1600 reports `border-radius: 0px` for both the switch and its buttons.
- The switch and progression row have the same right edge.
- `git diff --check` passes and CSS brace balance remains 0.

Remaining:
- None for this shape adjustment.

### 2026-08-07 15:42 HKT — Codex — Restore the pill-shaped 試一試 mode switch

Summary:
- Restored the rounded pill styling for the `印刷字／手寫字` switch container and buttons.
- Kept the switch in the same right-aligned position beside the 1／2／3 progression row.

Files changed:
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- The switch and buttons now use `border-radius: 999px`.
- The right-side alignment rules remain unchanged.
- `git diff --check` passes and CSS brace balance remains 0.

Remaining:
- None for this styling adjustment.

### 2026-08-07 15:30 HKT — Codex — Reorder Part 8 handwritten labels

Summary:
- Increased the gap between `直排單欄` and `正文字體`.
- Moved `上奏官員` above `臣字款` while keeping a clear vertical gap between them.
- Refreshed the StoryMap asset query version so the new positions load in the preview.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- The Part 8 positions are now `17%`, `28%`, `38%`, and `52%` for the affected labels.
- CSS brace balance and `git diff --check` pass.

Remaining:
- None for this Part 8 label-order adjustment.

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

### 2026-08-05 15:39 HKT — Codex — Add source-text samples to printed OCR features

Summary:
- Replaced the printed-feature JSON keys `text_sample` and `paragraph_samples` with direct `text` and `paragraphs` entries.
- Added the source sequence beginning with `福建水師提督…`, followed by two paragraph samples under `分段`; each displayed sample shows four sentences followed by `……`.
- Added original punctuation-bearing text to `標題符號` while preserving the existing OCR guidance.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser-rendered printed feature data contains no `_sample` keys in the three requested features.
- The live page shows the expected source text and printed labels without console errors or warnings.

Remaining:
- The displayed excerpts remain source-text teaching examples and should be checked against the scanned page when used as evidence.

### 2026-08-05 15:56 HKT — Codex — Add source-text examples to handwritten OCR features

Summary:
- Added direct source text under `text` in the handwritten `直排單欄` and `正文字體` JSON windows.
- Used the same four-sentence source excerpt followed by `……`, without changing the existing handwritten layout and script metadata.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser-rendered handwritten features contain the new text examples and ellipsis.
- The live page reports no console errors or warnings.

Remaining:
- The handwritten excerpt remains an OCR teaching example and should be checked against the scan before being treated as confirmed transcription.

### 2026-08-05 16:05 HKT — Codex — Arrange handwritten labels in one right-side sequence

Summary:
- Repositioned all handwritten Part 3 labels to the right side in the requested order: `直排單欄`, `正文字體`, `上奏官員`, `臣字款`, `抬頭`, `硃批`, `浮水印`, `印章`.
- Refreshed the StoryMap CSS cache key so the new label positions load immediately.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser geometry shows all eight handwritten labels on the right with no overlap.
- Browser console reports no errors or warnings.

Remaining:
- At narrow widths, the existing responsive layout continues to place labels in the normal tag row.

### 2026-08-05 16:12 HKT — Codex — Increase transparency of handwritten folded bars

Summary:
- Reduced the opacity of collapsed `.part3-fx-panel` bars to `0.56`, affecting the folded bars on either side while leaving the two open scanned pages unchanged.
- Refreshed the StoryMap CSS cache key so the opacity adjustment loads immediately.

Files changed:
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser preview shows the `辨識手寫字` visual with 10 collapsed panels at computed opacity `0.56`.
- The visual remains visible and the browser reports no console errors or warnings.
- `git diff --check` passes.

Remaining:
- None for the folded-bar transparency adjustment.

### 2026-08-05 16:09 HKT — Codex — Move later handwritten labels to the left

Summary:
- Kept `直排單欄`, `正文字體`, `上奏官員`, and `臣字款` on the right.
- Moved `抬頭`, `硃批`, `浮水印`, and `印章` to the left in their existing vertical sequence.
- Refreshed the StoryMap CSS cache key.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser geometry confirms the two-sided label arrangement has no overlap.
- Browser console reports no errors or warnings.

Remaining:
- At narrow widths, the existing responsive layout continues to place labels in the normal tag row.

### 2026-08-05 16:13 HKT — Codex — Widen Part 3.7 and 3.8 feature boxes

Summary:
- Increased the combined visual-plus-text box width for `辨識印刷字` and `辨識手寫字` from 90vw to 96vw.
- Refreshed the StoryMap CSS cache key while keeping the two-column visual/text balance unchanged.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- At a 1280px desktop viewport, both feature boxes render at 1228.8px wide with equal visual and text columns.
- Browser console reports no errors or warnings.

Remaining:
- The existing responsive breakpoint continues to stack the two columns on narrow screens.

### 2026-08-05 16:21 HKT — Codex — Tighten handwritten PDF and label spacing

Summary:
- Kept the widened `辨識手寫字` visual and reduced the document-side padding so the two open PDF panels use more of the left column.
- Pulled the labels toward the page edges, with approximately 12px of intentional overlap on both sides; the responsive layout still returns labels to a normal row on narrow screens.
- Refreshed the StoryMap card stylesheet cache key.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- At a 1280px desktop viewport, the explorer is `1228.8px` wide, the open PDF panels are `212px` wide each, and the side padding is `64px`.
- Label geometry shows the right labels overlap the PDF edge by 12px; the left labels are tucked to the page edge with the same small overlap.
- Browser console reports no errors or warnings; `node --check` and `git diff --check` pass.

Remaining:
- None for this spacing adjustment.

### 2026-08-05 16:47 HKT — Codex — Remove punctuation from handwritten JSON text

Summary:
- Removed punctuation marks from the two handwritten OCR JSON text examples shown for `直排單欄` and `正文字體`.
- Kept punctuation in the feature descriptions, AI prompts, and Python examples.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser output for `辨識手寫字` shows the text examples without punctuation.
- `git diff --check` passes.

Remaining:
- None for this JSON display adjustment.

### 2026-08-05 17:22 HKT — Codex — Fix JSON viewer font-size controls

Summary:
- Moved the JSON label, filename, body-text, line-height, window width, and height variables onto the `#part-3-json-chart` visual block.
- Removed child-level defaults that overrode adjustments made on the visual block.
- Refreshed the StoryMap card stylesheet cache key.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- The browser inherits the controls from `#part-3-json-chart` and renders the label at 14px, filename at 11px, and JSON body at 15px.
- Browser console reports no errors or warnings; `git diff --check` passes.

Remaining:
- None for the JSON viewer font-size control fix.

### 2026-08-05 17:34 HKT — Codex — Spread handwritten labels around the PDF

Summary:
- Redistributed the eight handwritten feature labels across varied, stable vertical positions over the full PDF height.
- Kept the four labels on the right and four on the left, with each label positioned 10px outside the PDF edge.
- Reset the outward label transform at the responsive breakpoint so the mobile label row remains unchanged.
- Refreshed the StoryMap card stylesheet cache key.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser geometry reports a 10px gap from every floating label to the PDF edge.
- Browser screenshot shows the labels distributed across the visual instead of clustered in two vertical groups.
- Browser console reports no errors or warnings; `git diff --check` passes.

Remaining:
- None for the handwritten label layout adjustment.

### 2026-08-05 18:25 HKT — Codex — Move JSON paragraph collapse control

Summary:
- Moved the paragraph toggle after the hidden continuation so the expanded control appears after `等情前來。`.
- Replaced the expanded `收合` text with the upward chevron `⌃`; the collapsed state remains `...`.
- Added matching accessible labels and titles for both states.
- Refreshed the StoryMap CSS and JavaScript cache keys.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser test confirms expanded DOM order ends with `等情前來。` followed by `⌃`.
- Collapse returns the button to `...` and hides the continuation.
- `node --check storymap.js`, `git diff --check`, and browser console checks pass.

Remaining:
- None for the JSON paragraph toggle adjustment.

### 2026-08-05 18:34 HKT — Codex — Reorganize JSON field buttons

Summary:
- Arranged the JSON field buttons in three rows: 來源／標題／官職／姓名; 具奏日期／硃批日期／硃批內容／頁碼; and 段落一／段落二／段落三.
- Added hover, focus, pressed, and selected styles to every button.
- Changed JSON line highlighting from a timed flash to persistent selection that moves to the next clicked field.
- Refreshed the StoryMap CSS and JavaScript cache keys.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser geometry confirms three rows with 4, 4, and 3 buttons.
- Clicking 來源 selects its button and JSON line; clicking 標題 removes the previous selection and keeps the new one.
- Hover transition is present; browser console reports no errors or warnings; `node --check storymap.js` and `git diff --check` pass.

Remaining:
- None for the JSON field button layout and selection behavior.

### 2026-08-05 18:38 HKT — Codex — Keep completed OCR batch labels visible

Summary:
- Kept the 4×4/50-page batch track visible during both batch-entry and batch-to-single restart transitions.
- Made the verified tile state enforce the enlarged blue `50頁` label, so the green tick and completed label remain together until the single-page restart replaces the grid.
- Refreshed the StoryMap CSS cache key.

Files changed:
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Live OCR animation trace shows `trackOpacity: 1` while 16 completed tiles remain in the 50-page screen and during `is-switching-out`.
- The next single-page tile replaces the batch directly; the 50-page screen no longer fades out first.
- Verified tiles retain `50頁`, blue enlarged styling, and green ticks; browser console reports no errors or warnings.
- `node --check storymap.js` and `git diff --check` pass.

Remaining:
- None for the OCR batch persistence behavior.
### 2026-08-05 19:08 HKT — Codex — Convert JSON field labels to one-line carousel

Summary:
- Preserved the latest borderless JSON field-button design.
- Changed the 11 JSON field buttons from three rows into one horizontal strip with `‹` and `›` controls at the ends.
- Kept the selected JSON field highlight persistent while the arrows reveal previous or next fields.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser check reports one label row, horizontal overflow, working arrow scrolling, persistent selection, and no console errors or warnings.
- `node --check Website/storymap/storymap.js` and `git diff --check` pass.

Remaining:
- None for the JSON field navigation adjustment.

### 2026-08-05 19:12 HKT — Codex — Fix JSON carousel arrow initialization

Summary:
- Fixed the `‹` and `›` controls being disabled when the JSON label strip had not finished laying out.
- Added layout, page-load, resize, and resize-observer refreshes so the controls reflect the actual strip width.

Files changed:
- `Website/storymap/storymap.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Fresh browser load enables `›`, and both arrows scroll the one-line field strip in their respective directions.
- Browser console reports no errors or warnings; `node --check Website/storymap/storymap.js` passes.

Remaining:
- None for the JSON carousel controls.

### 2026-08-06 15:29 HKT — Codex — Use annotated PNGs for Part 7 feature labels

Summary:
- Mapped all seven Part 7 辨識印刷字 labels to the supplied annotated PNGs in `Website/storymap/辨識印刷字Label/`.
- Replaced the CSS highlight rectangles with image switching when a feature label is selected; Part 8’s CSS highlights remain unchanged.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Clicking 夾批 loads `辨識印刷字Label/夾批.png` with the matching alt text and no Part 7 CSS highlight element.
- Returning to page 1 restores `ocr-zhu25-printed-1-enhanced.png`; all seven PNGs match the base scan dimensions.
- `node --check storymap.js` and `git diff --check` pass.

Remaining:
- None for the Part 7 annotated-image interaction.

### 2026-08-06 15:40 HKT — Codex — Refine JSON controls and terminal-only field scrolling

Summary:
- Made the JSON carousel `‹` and `›` controls heavier and increased the selected-field orange underline from 2px to 4px.
- Replaced page-level `scrollIntoView()` with centered scrolling inside the JSON terminal body, so field buttons move only the terminal text.

Files changed:
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser interaction kept `window.scrollY` unchanged while `.part3-json-body.scrollTop` changed from 0 to 274 after clicking 段落三.
- The selected button and matching JSON line remain highlighted; the updated arrow weight and 4px underline are visible.
- Browser console reports no errors or warnings; `node --check Website/storymap/storymap.js` and `git diff --check` pass.

Remaining:
- None for the JSON control and terminal-scrolling adjustment.

### 2026-08-06 15:41 HKT — Codex — Use annotated PNGs for Part 8 handwritten labels

Summary:
- Mapped all eight Part 8 辨識手寫字 labels to the supplied annotated PNGs in `Website/storymap/辨識手寫字Label/`.
- Replaced CSS highlight rectangles with annotated-image source switching for the selected handwritten sheet while preserving the folded-paper layout.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Clicking 正文字體 loads `辨識手寫字Label/正文字體.png`; clicking 抬頭 switches to `辨識手寫字Label/抬頭.png` on the correct sheet.
- Returning to page 1 restores `ocr-zhu25-handwritten-1-enhanced.png`; no `.part3-fx-hl` elements are generated.
- `node --check storymap.js` and `git diff --check` pass.

Remaining:
- None for the Part 8 annotated-image interaction.

### 2026-08-06 15:41 HKT — Codex — Center Part 8 PDF and tighten handwritten labels

Summary:
- Centered the folded handwritten PDF within its document panel using symmetric layout spacing.
- Reduced the label-to-PDF gap from 10px to 4px on both sides.

Files changed:
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser geometry shows the PDF centered in the document panel and all labels 4px from the corresponding PDF edge.
- `node --check Website/storymap/storymap.js` and `git diff --check` pass.

Remaining:
- None for the Part 8 PDF and label positioning.

### 2026-08-06 15:43 HKT — Codex — Move Part 7 夾批 and 落款 labels to the left

Summary:
- Moved the `夾批` and `落款與尾批` labels in `7. 辨識印刷字` from the right side of the printed page to the left side.
- Preserved their existing vertical positions at 38% and 60%.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed the feature data now uses left-side anchors while retaining both original `top` values.

Remaining:
- Browser visual verification of the two moved labels.

### 2026-08-06 15:49 HKT — Codex — Reorder Part 8 handwritten labels

Summary:
- Reordered the Part 8 handwritten labels so the right side reads `直排單欄 → 正文字體 → 臣字款 → 上奏官員` from top to bottom.
- Reordered the left side to `抬頭 → 硃批 → 浮水印 → 印章` from top to bottom.

Files changed:
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser geometry confirms the requested left/right and top-to-bottom label order at the desktop layout.
- `node --check storymap.js` and `git diff --check` pass.

Remaining:
- None for the Part 8 label ordering.

### 2026-08-06 17:15 HKT — Codex — Match Part 7 and Part 8 label colours to annotated highlights

Summary:
- Updated all seven Part 7 label colours and all eight Part 8 label colours to follow the corresponding annotated PNG highlight tones.
- Used slightly darker, still soft versions of each highlight colour for readable labels; `硃批` uses a softened red derived from its red ink.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser computed styles report the new colour values for all seven printed-text labels and all eight handwritten labels.
- `node --check storymap.js` and `git diff --check` pass.

Remaining:
- None for the Part 7 and Part 8 label colours.

### 2026-08-06 17:58 HKT — Claude — Add Part 3 section 11 「試一試」 interactive prompt-writing exercise

Summary:
- New section `#part-3-try` after `10 OCR測試`. Left half: source page with highlight regions only, no labels. Right half: three-stage guided exercise (download PDF → assemble prompt in a Codex-style chat window → paste and diff OCR output).
- RPG dialogue box pinned to the bottom of the info panel carries all guidance; the chip, fill-in-the-blank dropdown, and free-text box render inside it. Wrong answers show ✗ and reset for a retry.
- Completed stages collapse into checked to-do rows. Assembled prompt lines are editable in place; the copy button reads live text.
- 印刷字／手寫字 toggle beside the title swaps document, highlights, sentences, and reference, resetting progress.
- Character-level LCS diff gives a match percentage with inline missing/extra marking; the user's pane stays editable for re-comparison.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap-cards.css`
- `Website/UI Idea/26-part3-try-it-ui.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check storymap.js` passes; CSS brace balance 0; HTML div balance 0; embedded JSON parses.

Remaining:
- Real 試一試 PDFs and reference OCR text still to be supplied; highlight boxes to be retuned once the real documents are in.

### 2026-08-06 18:44 HKT — Codex — Render 試一試 printed PDF pages as clearer PNG assets

Summary:
- Rendered `Website/storymap/試一試/印刷字/明清台灣檔案匯編 30 (dragged).pdf` at 400 PPI into one PNG per page.
- Applied a light unsharp-mask pass without contrast remapping or thresholding, preserving the original page layout and text.

Files changed:
- `Website/storymap/試一試/印刷字/明清台灣檔案匯編 30-page-1.png`
- `Website/storymap/試一試/印刷字/明清台灣檔案匯編 30-page-2.png`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Both pages were visually inspected after rendering.
- Both PNGs are RGB images at 3308×5260 pixels with no clipping or layout changes.
- Temporary render files were removed after the final PNGs were saved.

Remaining:
- None for this printed-PDF PNG export.

### 2026-08-06 18:48 HKT — Codex — Replace Part 7/8 feature heading with gradient number badge

Summary:
- Removed the `版面特徵` label from the shared feature result panel used by Part 7 `辨識印刷字` and Part 8 `辨識手寫字`.
- Added a square number badge before the active feature title; the number updates with the selected feature.
- Styled the badge with an orange-dominant gradient that fades into the website green.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser checks confirm both Part 7 and Part 8 render one square badge, show the selected feature number, and no longer render the old `版面特徵` label.
- `node --check Website/storymap/storymap.js` and `git diff --check` pass.

Remaining:
- None for this Part 7/8 badge change.

### 2026-08-06 18:57 HKT — Codex — Remove Part 7/8 numbered colour badge

Summary:
- Removed the orange-and-green square number badge from the shared feature result panel in Part 7 `辨識印刷字` and Part 8 `辨識手寫字`.
- Kept the active feature title and description in the same result panel.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- The badge markup, styling, and update code are no longer present.
- `node --check Website/storymap/storymap.js` and `git diff --check` pass.
- Browser checks confirm both Part 7 and Part 8 show the feature title and description with zero numbered badges; the browser console is clean.

Remaining:
- None for this Part 7/8 badge removal.

### 2026-08-06 18:57 HKT — Codex — Fit printed-PDF backdrops to the document content

Summary:
- Fixed the oversized dark PDF backdrop in Part 7 `辨識印刷字` and the printed mode of Part 11 `試一試`.
- The right information panel keeps the full explorer height, while the left document area and its PDF-derived backdrop use a content-based height and the PDF's available-height limit.
- Preserved the page-turn layer and controls; the printed page remains proportional and uncropped.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser checks confirmed both printed views render a compact left document backdrop instead of a full-height dark panel.
- Part 7 and Part 11 printed pages remain proportional, and the existing page-turn controls remain present.
- `git diff --check` passes.

Remaining:
- None for this backdrop-height fix.

### 2026-08-06 19:00 HKT — Codex — Restore natural PDF sizing in narrow windows

Summary:
- Added a narrow-window override for Part 7 `辨識印刷字` and Part 11 `試一試` printed mode.
- Desktop PDF height limits are cleared at the stacked breakpoint, so the document, backdrop, and page-turn layer return to natural proportional height.

Files changed:
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- The responsive override has higher specificity than the desktop PDF sizing rules and restores `height: auto` / `max-height: none` at `1040px` and below.
- CSS brace balance and `git diff --check` pass.

Remaining:
- None for the narrow-window PDF sizing fix.

### 2026-08-06 19:17 HKT — Codex — Refresh responsive PDF styles in the browser

Summary:
- Bumped the StoryMap stylesheet query so the browser loads the current PDF backdrop rules instead of the cached desktop CSS.
- Kept the narrow-window override for Part 7 `辨識印刷字` and Part 11 `試一試` printed mode, restoring natural document height and proportional images below `1040px`.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- The HTML now requests the refreshed `storymap.css` and `storymap-cards.css` versions.
- The responsive CSS has balanced braces; `git diff --check` passes.

Remaining:
- None for this cache and narrow-window correction.

### 2026-08-06 19:23 HKT — Codex — Move the printed/handwritten switch to the progress row

Summary:
- Moved the existing `印刷字／手寫字` switch into the generated `進度 1 2 3` row.
- The switch is appended after the three progress numbers and aligned to the far right; its existing mode-switch interaction is unchanged.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check Website/storymap/storymap.js` passes.
- CSS brace balance is 0 and `git diff --check` passes.
- The stylesheet and script query versions were refreshed so the moved control is not hidden by cached assets.

Remaining:
- None for this progress-row switch placement.

### 2026-08-06 19:27 HKT — Codex — Use printed 試一試 PDF and prompt-specific page images

Summary:
- Wired the printed `試一試` exercise to `Website/storymap/試一試/印刷字/`, including its local PDF, page 1 and page 2 PNGs, and annotated topic images.
- Step 2 now shows the matching annotated image for each topic prompt, including `標點.png`; steps without a topic image fall back to `page1.png` or `page2.png`.
- The OCR-purpose prompt now names the local PDF `為請酌籌加調官兵協力進剿事.pdf`.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser checks confirm the printed flow uses `page1.png` for the initial and installation/OCR-purpose states; `直排單欄` uses `直排單欄.png`; `分段` uses `分段.png`; `標點` uses `標點.png`; `文本資訊` uses `文本資訊.png`; and the no-topic `夾批` step falls back to `page2.png`.
- The PDF link resolves to `Website/storymap/試一試/印刷字/為請酌籌加調官兵協力進剿事.pdf`.
- Browser console logs are empty; `node --check Website/storymap/storymap.js` and `git diff --check` pass.

Remaining:
- None for the printed 試一試 asset routing.

### 2026-08-06 19:28 HKT — Codex — Restore narrow green document backdrop height

Summary:
- Kept the narrow-window PDF and page images at natural proportional height while restoring a minimum height for the green document area.
- Part 7 uses `--fx-explorer-h` and Part 11 uses `--try-explorer-h`, so each section retains its own adjustable panel height without reusing the wrong variable.

Files changed:
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- The final `max-width: 1040px` override clears the desktop height caps, keeps the PDF image `height: auto`, and applies section-specific minimum height to the green backdrop.
- Browser visual recheck was unavailable because the existing local file tab was blocked from reloading; static CSS checks were run instead.

Remaining:
- None for this narrow-window backdrop adjustment.

### 2026-08-06 19:31 HKT — Codex — Bind the exact printed PDF to Step 1

Summary:
- Added the supplied absolute PDF path to the printed `試一試` data used by Step 1.
- Step 1 keeps the browser-safe relative link for opening the same PDF from the website, while retaining the exact local source path as the PDF asset metadata.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser inspection confirms Step 1 carries `/Users/creamybanana/Downloads/DH Project/intro Website/Website/storymap/試一試/印刷字/為請酌籌加調官兵協力進剿事.pdf`, displays the correct filename, and advances to Step 2 with `page1.png`.
- Browser console logs are empty; `node --check Website/storymap/storymap.js` and `git diff --check` pass.

Remaining:
- None for the Step 1 PDF binding.

### 2026-08-06 19:44 HKT — Codex — Enhance npmpdf-3 handwritten pages

Summary:
- Rendered the supplied `試一試/手寫字/npmpdf-3.pdf` from its crop box at 400 DPI.
- Applied gentle autocontrast, contrast, and unsharp-mask enhancement, then exported one PNG per page and a matching three-page PDF.

Files changed:
- `Website/storymap/試一試/手寫字/npmpdf-3-enhanced.pdf`
- `Website/storymap/試一試/手寫字/npmpdf-3-1-enhanced.png`
- `Website/storymap/試一試/手寫字/npmpdf-3-2-enhanced.png`
- `Website/storymap/試一試/手寫字/npmpdf-3-3-enhanced.png`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- All three PNGs are high-resolution crop-box renders and were visually inspected.
- The final PDF has three pages and preserves the original approximately 836.7 × 608.4 pt page size; its pages were re-rendered and visually checked.

Remaining:
- None for the npmpdf-3 clarity enhancement.

### 2026-08-07 14:59 HKT — Codex — Move Part 8 handwritten labels closer to the PDF

Summary:
- Tightened the vertical positions of the top `直排單欄`／`抬頭` labels and the bottom `上奏官員` label in `辨識手寫字`.
- Kept the existing side offsets, label styling, and animation unchanged.

Files changed:
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Part 8 label positions now use `17%` for the two upper edge labels and `80%` for the lower edge label, keeping them closer to the visible PDF span.
- CSS brace balance and `git diff --check` pass.

Remaining:
- None for this Part 8 label-spacing adjustment.

### 2026-08-07 15:03 HKT — Codex — Refresh Part 8 label styles in the preview

Summary:
- Bumped the StoryMap asset query versions so the browser reloads the updated Part 8 handwritten-label positions instead of using the previous cached CSS.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- The HTML now requests the `20260807-part3-handwritten-labels-02` stylesheet and script versions.
- `git diff --check` passes.

Remaining:
- None for this Part 8 preview refresh.

### 2026-08-07 15:15 HKT — Codex — Shorten the printed 試一試 Step 1 guide

Summary:
- Changed the Step 1 guide text from the longer download-and-search instruction to `先把這份史料下載到你的電腦。`.

Files changed:
- `Website/storymap/storymap.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser DOM verification shows the shortened sentence in the printed `試一試` Step 1.
- Browser console logs are empty; `node --check Website/storymap/storymap.js` and `git diff --check` pass.

Remaining:
- None for this wording adjustment.

### 2026-08-07 15:25 HKT — Codex — Fill the 試一試 PDF backdrop and align the mode switch

Summary:
- Filled the green backdrop of the `試一試` PDF window to the full height of its left pane, removing the transparent white strip above and below the backdrop.
- Kept `印刷字／手寫字` inside the 1／2／3 progression row and pinned it to that row's right edge.

Files changed:
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- At a 1150×1600 browser viewport, the try PDF pane reports `background-size: 100% 100%, 100% 100%`.
- The mode switch's right edge is exactly aligned with the progression row's right edge.
- CSS brace balance is 0, `node --check Website/storymap/storymap.js` passes, and `git diff --check` passes.

Remaining:
- None for this layout adjustment.

### 2026-08-07 15:31 HKT — Claude — Make 試一試 3.6 頁碼 a plain two-choice question

Summary:
- Changed printed-mode step "3.6 頁碼" from an inline fill-in-blank `mc` dropdown to a new non-inline `choice` step kind: two standalone buttons (`保留` / `不保留`) below the guide box, per request "應否保留頁碼，2 option (not intext)". Guide text simplified to `應否保留頁碼？`.
- Added the `choice` renderer to `storymap.js` `nextStep()` and `.part3-try-choices`/`.part3-try-choice` styling to `storymap.css`.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check Website/storymap/storymap.js` passes; `json.loads()` on `data-part3-try-data` confirms 3.6 頁碼 is now `kind: "choice"` with `options: ["保留","不保留"]`, `answer: "保留"`.
- CSS brace balance 0.

Remaining:
- No git commit — working tree has concurrent unrelated edits from another agent in the same files.

### 2026-08-07 15:52 HKT — Claude — Freeze 試一試 chat header/footer; rectangle multi-option buttons

Summary:
- Phase 2 chat window: progress row and footer ("每一句都可以直接點進去修改。複製全部") now stay fixed; only the chat bubble list scrolls internally. Implemented via a JS-toggled `is-chat` class on `.part3-try-scroll` that turns it into a flex column (progress row + winbar + footer fixed-size, `.part3-try-chat` flex-fills and scrolls).
- Multi-select option buttons (inline `.part3-try-check`, block `.part3-try-multi-item`) changed from rounded pills to plain rectangles with tighter padding/smaller checkbox (shorter height).

Files changed:
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check Website/storymap/storymap.js` passes; CSS brace balance 0.
- `data-part3-try-data` JSON still parses (17 printed steps).

Remaining:
- No git commit — working tree has concurrent unrelated edits from another agent in the same files.

### 2026-08-07 16:05 HKT — Claude — Add "save as skill" step to 試一試 printed prompt flow

Summary:
- New chip step "4.5 儲存為 Skill" inserted after "4.4 正文" in printed mode: asks AI to save the just-defined OCR rules as a reusable skill so the same rules can be applied to other material from the same book without retyping the prompt. Existing "4.5 你自己的要求" renumbered to "4.6".

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `data-part3-try-data` JSON parses; printed steps now 18, no duplicate labels.

Remaining:
- Handwritten mode not updated with an equivalent step.
- No git commit — concurrent edits from another agent present in the working tree.

### 2026-08-07 15:40 HKT — Codex — Preserve 試一試 progress across mode switching

Summary:
- Stored the exercise state separately for 印刷字 and 手寫字, so switching modes preserves each mode's current phase, prompt step, answers, page, and OCR comparison state until the page is reloaded.
- Renamed the Step 1 button to `下載` and added a right-side `已下載` button that advances without opening the PDF.
- Styled `已下載` with a transparent background and green border, and refreshed the asset query version.

Files changed:
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser checks confirm `已下載` advances to Step 2, 手寫字 starts independently at Step 1, and returning to 印刷字 restores its Step 2 position.
- Browser console logs are empty; `node --check Website/storymap/storymap.js` and `git diff --check` pass.

Remaining:
- None for this 試一試 persistence and Step 1 control update.

### 2026-08-07 15:46 HKT — Codex — Add Google Cloud free-trial gallery

Summary:
- Added the supplied Google Cloud free-trial image as a one-image gallery on the right side of the Part 3 Google Cloud text card.
- Added the requested `details of free trail of google cloud` information-panel title and embedded the supplied Google Cloud documentation URL in that title.
- Added dedicated responsive sizing for the new card-and-gallery layout and refreshed the stylesheet cache key.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `Website/storymap/1661514832038.jpeg`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser geometry confirms the text card is on the left and the gallery is on the right at 1280px viewport width.
- Browser confirms the image loads at its native `1198×627` dimensions and the info-panel link resolves to `https://docs.cloud.google.com/free/docs/free-cloud-features?hl=zh-tw`.
- Google Cloud gallery JSON parses; `node --check`, `git diff --check`, and the asset existence check pass.

Remaining:
- None for this Google Cloud gallery addition.

### 2026-08-07 15:51 HKT — Codex — Translate Google Cloud gallery label

Summary:
- Translated the Google Cloud gallery information-panel title into Traditional Chinese as `Google Cloud 免費試用詳情`.
- Preserved the supplied Google Cloud documentation link unchanged.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed the gallery JSON title is Traditional Chinese and the `titleHref` remains the supplied URL.
- `git diff --check` passes.

Remaining:
- None for this label translation.

### 2026-08-07 15:55 HKT — Codex — Recover Google Cloud image in HTML

Summary:
- Restored the Google Cloud card’s right-side gallery markup in the StoryMap HTML.
- Restored the supplied image path, Traditional Chinese info-panel label, and documentation link.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed the HTML contains `1661514832038.jpeg` and the supplied documentation URL.
- `git diff --check` passes.

Remaining:
- None for this image recovery.

### 2026-08-07 15:54 HKT — Codex — Keep the latest prompt visible in the AI chatbox

Summary:
- Added an explicit latest-message scroll after rendering and restoring the Step 2 AI chatbox.
- The newest prompt remains visible when the chatbox is rebuilt after switching between 印刷字 and 手寫字.

Files changed:
- `Website/storymap/storymap.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser checks confirm the newest OCR prompt is the last chat bubble and the chatbox remains at its bottom position after mode switching.
- Browser console logs are empty; `node --check Website/storymap/storymap.js` and `git diff --check` pass.

Remaining:
- None for latest-prompt visibility.

### 2026-08-07 16:12 HKT — Claude — Recover 試一試 printed steps after concurrent overwrite

Summary:
- `storymap-example.html`'s working copy had reverted to an old pre-restructuring version (10 printed steps instead of 18, missing 2.1/3.5/4.5, different PDF filename/asset versions) — a concurrent write from another in-progress session, not something I did. The last commit (`d8626f4`) already had the correct 18-step version, so restored the working file to match HEAD via `git show d8626f4:...` copied back over the file (plain `git checkout` failed: `.git/index.lock` present, owned by another process, permission denied to remove).

Files changed:
- `Website/storymap/storymap-example.html` (restored to HEAD)
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- JSON parses; printed 18 / handwritten 10 steps confirmed correct; `git status` shows no diff vs HEAD for this file.

Remaining:
- `.git/index.lock` still present — likely another agent session is active on this same repo right now; recommend checking before further concurrent edits.

### 2026-08-07 16:22 HKT — Codex — Increase the upper space of the completed chat footer

Summary:
- Increased the top padding above `每一句都可以直接點進去修改。` and `複製全部` in the Step 2 AI chatbox.
- Added `--try-chatfoot-top-pad: 24px` to the adjustable Part 3 試一試 variables.
- Refreshed the stylesheet query version so the spacing change loads immediately.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser preview confirms both StoryMap stylesheets load the refreshed version and the computed `--try-chatfoot-top-pad` is `24px`.
- Browser console logs are empty; `node --check Website/storymap/storymap.js` and `git diff --check` pass.

Remaining:
- None for the chat footer spacing adjustment.

### 2026-08-07 16:40 HKT — Claude — Mirror printed try-it structure into handwritten mode

Summary:
- Added to handwritten 試一試: opening `撰寫 Prompt` advance card, `2.1 史料來源` chip (cites 《明清臺灣檔案彙編》第30冊 — verified against stage1_original_text.json doc_id 硃56, same document as printed), `4.2 輸出 JSON 的結構` chip, `4.3 史料資訊` multi (printed's field list minus 頁碼, since handwritten has no page-number feature), `4.4 正文` chip asking for the body to be merged into one paragraph (opposite of printed's 逐段列出), `4.5 儲存為 Skill` chip, and replaced the old custom `十 · 你自己的要求` with printed's `4.6 你自己的要求` verbatim.
- Handwritten steps: 10 → 16.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- JSON parses; printed 18 / handwritten 16 steps, no duplicate labels, all feature refs resolve.

Remaining:
- No git commit yet — recommend committing soon given the earlier concurrent-overwrite incident.

### 2026-08-07 16:50 HKT — Claude — Simplify handwritten prompt-defining guides to plain questions

Summary:
- Reworded three handwritten-only guide texts to simple questions: 撰寫 Prompt, 2.1 史料來源, 4.2 輸出 JSON 的結構. Printed mode untouched.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- JSON parses, step counts unchanged (printed 18 / handwritten 16).

Remaining:
- No git commit yet.

### 2026-08-07 17:17 HKT — Codex — Route handwritten 試一試 assets and folded page turning

Summary:
- Wired the handwritten 試一試 mode to `Website/storymap/試一試/手寫字/`, including its local PDF, `page1.png`–`page3.png`, and feature-specific images such as `直欄.png`, `作者.png`, `臣字.png`, `硃批.png`, and `水印.png`.
- Prompt-related feature steps now show the matching annotated image; ordinary prompt steps show the handwritten page scan. The handwritten document view does not add feature highlight labels or coloured overlays.
- Added folded-paper crease treatment and a short turn animation when moving between handwritten page scans.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser checks confirm the handwritten PDF path, page 1 and page 2 navigation, the turn class, zero overlay labels, and final routing to `水印.png` with `頁 3 / 3`.
- `node --check Website/storymap/storymap.js` and `git diff --check` pass; browser console logs are empty.

Remaining:
- No git commit yet.

### 2026-08-07 17:00 HKT — Claude — Renumber handwritten 版面要求 steps to match printed's numeric scheme

Summary:
- Handwritten's five 版面要求 quiz steps renamed from Chinese numerals to printed-style numbers: 四→3.1 閱讀順序, 五→3.2 上奏官員, 六→3.3 小字自稱, 七→3.4 硃批, 八→3.5 印章與浮水印, 九→4.1 JSON 格式 (now flows straight into the existing 4.2–4.6). Guide text for 3.2/3.3/3.4/3.5/4.1 shortened to plain questions, matching printed's style; actual prompt wording (before/after/options) unchanged.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- JSON parses; printed 18 / handwritten 16 steps, no duplicate labels, feature refs resolve.

Remaining:
- No git commit yet.

### 2026-08-07 17:10 HKT — Claude — Add distractor support to "multi" step; mark 硃批日期/硃批內容 wrong in handwritten

Summary:
- Added optional `wrong` field to the block-style "multi" quiz kind: listed items are shown but must stay unchecked (checking one turns red and blocks completion). Applied to handwritten's "4.3 史料資訊" — 硃批日期/硃批內容 are now distractors there, consistent with "3.4 硃批" already telling the AI to skip OCR'ing the rescript. Printed's 4.3 unaffected (no `wrong` field, still requires those two fields).

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check` passes; JSON parses; CSS brace balance 0.

Remaining:
- No git commit yet.

### 2026-08-07 17:20 HKT — Claude — Add two-blank "mc2" step kind; convert handwritten 4.4 正文 to it

Summary:
- New `mc2` step kind (two independent fill-in-blank selects in one sentence, both must be correct to advance) added to `storymap.js`. Handwritten's "4.4 正文" converted from a chip to `mc2`: "正文請【合併成一整段／逐段列出】，【忽略／保留】抬頭引致的分段。", correct = 合併成一整段 / 忽略. Printed's 4.4 unaffected.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check` passes; JSON parses; step counts unchanged (18/16).

Remaining:
- No git commit yet.

### 2026-08-07 17:30 HKT — Claude — Add "already downloaded" skip option to 安裝工具 step (both modes)

Summary:
- New optional `skip` field on "chip" steps renders a secondary, subdued button that advances without adding any line to the chat/prompt. Applied to both modes' "一 · 安裝工具" step with label "已下載".

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check` passes; JSON parses; CSS brace balance 0.

Remaining:
- No git commit yet.

### 2026-08-07 17:38 HKT — Claude — Add "4. 輸出要求" advance card to handwritten

Summary:
- Added printed's "4. 輸出要求" advance step (定義好版面規則後，現在要定義輸出格式。) to handwritten mode before "4.1 JSON 格式".

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- JSON parses; handwritten now 17 steps, no duplicate labels.

Remaining:
- No git commit yet.

### 2026-08-07 17:45 HKT — Claude — Always-clickable "完成，加入 prompt" button for block-style multi

Summary:
- Block-style "multi" quiz (4.3 史料資訊, both modes): "完成，加入 prompt" button is no longer disabled by selection count — clicking it always checks correctness, shaking/reddening on a wrong or incomplete answer instead of being unclickable.

Files changed:
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check` passes; CSS brace balance 0.

Remaining:
- No git commit yet.

### 2026-08-07 17:50 HKT — Claude — Left-align "已下載" skip button text

Summary:
- `.part3-try-chip--skip` text now left-aligned instead of centered.

Files changed:
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

### 2026-08-07 18:05 HKT — Claude — Add 具奏日期 quiz (handwritten) and JSON "issue" field (both modes)

Summary:
- Handwritten: new "3.5 具奏日期" mc step after "3.4 硃批" (印章與浮水印 renumbered 3.5→3.6). Asks whether the closing 乾隆X年X月X日 date is 具奏日期 or 硃批日期 (correct: 具奏日期).
- Both modes: "4.2 輸出 JSON 的結構" now describes three parts (史料資訊、正文、issue). New "4.5 issue" chip after "4.4 正文" defines the issue field: mark uncertain characters/punctuation as "(前5字)＋？(不確定的字)＋(後5字)". Trailing steps renumbered 4.5→4.6 (儲存為 Skill), 4.6→4.7 (你自己的要求).

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- JSON parses; printed 19 / handwritten 19 steps, no duplicate labels, feature refs resolve.

Remaining:
- No git commit yet.

### 2026-08-07 18:15 HKT — Claude — Rename "issue" to 待查; shuffle multi-select button order

Summary:
- "issue" JSON field renamed to "待查" in both modes' 4.2/4.5 steps.
- Block-style multi (4.3 史料資訊) option buttons now shuffle on each render; assembled chat sentence still always follows the fixed `items` order regardless of click order.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check` passes; JSON parses, no "issue" text remaining.

Remaining:
- No git commit yet.

### 2026-08-07 18:22 HKT — Claude — Fix broken JSON in "4.6 儲存為 Skill" (handwritten)

Summary:
- Missing closing quote on the "4.6 儲存為 Skill" chip string broke JSON parsing, taking down the whole 試一試 section. Fixed.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- JSON parses cleanly again; 19/19 steps, no duplicates.

Remaining:
- No git commit yet.

### 2026-08-07 18:30 HKT — Claude — Hide right/wrong coloring on multi (史料資訊) until 完成 is clicked

Summary:
- Multi-select chips (4.3 史料資訊) now stay neutral while picking; red "wrong" styling only reveals right after clicking "完成，加入 prompt", and resets to neutral on further clicks.

Files changed:
- `Website/storymap/storymap.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check` passes.

Remaining:
- No git commit yet.

### 2026-08-07 18:55 HKT — Claude — Accordion-fold visuals for 試一試 handwritten mode

Summary:
- Added section 8's accordion-fold ("風琴摺") visual to specific 試一試 handwritten feature steps: column/author/minor open "bc" (middle+right), stamp opens "ab" (left+middle), each using its own dedicated image split into 3 panels via background-size 300%.
- "3.4 硃批" and "3.5 具奏日期" instead show a flat crop of 奏報日期.png (middle+right two-thirds, no accordion), since both should display the same image.
- Removed "頁X／Y" label when any feature image is active (now shows the feature title in both modes).

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check` passes; CSS brace balance 0; JSON parses correctly.

Remaining:
- Not visually verified in a browser this turn — please check live and report any position/sizing issues.
- No git commit yet.

### 2026-08-07 19:10 HKT — Claude — Fix double-rendered document pane (pagestack + fold both visible)

Summary:
- `[hidden]` attribute was being overridden by unconditional `display:flex` rules on the page stack / fold / crop containers, causing them to render stacked on top of each other. Added explicit `[hidden]{display:none!important}` override for all three.

Files changed:
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- CSS brace balance 0.

Remaining:
- Printed-mode blank-space screenshot not yet diagnosed as bug vs. source image content.
- "2 by 2" accordion for normal page browsing not yet implemented — scope needs clarification.
- No git commit yet.

### 2026-08-07 19:35 HKT — Claude — Full multi-page 風琴摺 for handwritten normal browsing + fix sizing math

Summary:
- Handwritten mode's normal page browsing (not just quiz-feature steps) now uses the same accordion-fold as section 8: 3 pages × 3 sub-folds = 9 flat panels, default pairing ab/cd/ef via prev/next (±2), with quiz features able to jump to a non-default pair (bc/de) and continue stepping on that grid afterward.
- Fixed fold sizing: real image aspect ratio (≈155/338, measured via PIL on the actual PNGs) now drives `aspect-ratio` on open panels, and strip width is measured in JS pixels (`sizeFoldStrip()`) instead of an incorrect percentage-based calc.

Files changed:
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`
- `../PROJECT_LOG.md`
- `INTRO_WEBSITE_CHANGE_LOG.md`

Verified:
- `node --check` passes; CSS brace balance 0; JSON unaffected (19/19 steps).

Remaining:
- Not yet checked in a live browser.
- No git commit yet.

### 2026-08-07 19:55 HKT — Claude — Revert 風琴摺 accordion; back to plain page-by-page for 試一試

Summary:
- Rolled back the accordion-fold experiment entirely — handwritten mode is back to plain page1/2/3.png browsing with per-feature image swap-in, no folding/cropping. "3.4 硃批" uses 硃批.png again (via existing `rescript` feature); "3.5 具奏日期" now has a proper new `sendDate` feature (奏報日期.png) instead of the removed crop override. All accordion JS/CSS/HTML removed.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check` passes; CSS brace balance 0; JSON parses (19/19 steps, no dup labels, all feature refs resolve, no leftover fold/cropImage fields).

Remaining:
- Recommend committing now — back to a simple, verified-working state.

### 2026-08-07 20:10 HKT — Claude — Use memorial_print_ocr.json as printed 試一試 reference

Summary:
- Printed mode's compare-stage `reference` now holds the full memorial_print_ocr.json content verbatim (史料資訊／正文／待查), replacing the earlier plain-text placeholder, matching the flow's actual JSON output target.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- JSON parses; reference string itself parses to expected structure.

Remaining:
- No git commit yet.

### 2026-08-07 20:55 HKT — Claude — Simplify 試一試 phase 3 to stacked reference/mine text boxes; drop field-table + legend, collapse guide bar after compare

Summary:
- Replaced the field-by-field JSON table UI with two stacked text boxes (參考 OCR 結果 top, 你的 OCR 結果 bottom, editable), each 50% of the compare window's remaining height (score row + button row excluded via flexbox). Diff shown as inline red underline directly in each box's text (reused `diffTryChars`), no separate legend/side panel.
- After a compare runs, the bottom guide dialogue box hides to give the compare window the rest of the panel height; it reappears automatically on the next `showGuide()` call.
- "Your OCR result" box is now `contenteditable` instead of `<textarea>` so diff highlighting can render inline while still being editable.

Files changed:
- `Website/storymap/storymap.js`, `Website/storymap/storymap.css`

Verified:
- `node --check storymap.js` OK; CSS brace balance 0; JSON data block still parses, step counts unchanged.
- Not visually verified in a browser.

Remaining:
- No git commit yet.

### 2026-08-07 20:35 HKT — Claude — JSON-vs-JSON structured compare for 試一試 phase 3; handwritten reference now real OCR JSON too

Summary:
- Phase 3 compare (`runCompare` in storymap.js) now branches: if `d().reference` parses as JSON, compares the user's pasted text as JSON field-by-field (`flattenTryJson`/`diffTryJson`) with match/mismatch/missing/extra states per leaf path, invalid-JSON input shows a dedicated error panel; otherwise unchanged character-level diff.
- Handwritten `reference` replaced with full content of `memorial_handwritten_ocr.json` (external outputs folder), so both modes now use real OCR-output JSON as reference and both get the structured compare automatically.
- Download-reference button exports `.json` (formatted) when reference is JSON, `.txt` otherwise.

Files changed:
- `Website/storymap/storymap.js`, `Website/storymap/storymap.css`, `Website/storymap/storymap-example.html`

Verified:
- `node --check storymap.js` OK; CSS brace balance 0; both printed/handwritten `reference` fields parse as valid JSON; step counts unchanged (19/19).
- Not visually verified in a browser.

Remaining:
- No git commit yet.

### 2026-08-07 21:20 HKT — Claude — Nav renaming, responsive gate, teacher-preview mode (?preview=ocr) for GitHub hosting

Summary:
- Renamed the 4 top-nav tabs: 引言→平台簡介, 第一部分→平台介面, 第二部分→平台運作流程, 第三部分→運用平台研究其他問題.
- Added CSS-only viewport gate: narrow desktop window → "widen your window" overlay; mobile portrait → "rotate to landscape" overlay (`pointer:fine`/`pointer:coarse` media queries, no JS).
- Added `?preview=ocr` mode (same file, no duplicate site): jumps straight to Part 3 步驟二 OCR並結構化原始史料 on load, locks 主頁/平台介面/平台運作流程 tabs + brand link, fades+`inert`s content above 步驟二 and the 步驟八 LLM Wiki stage onward with a "尚在開發中" badge. Share link: `storymap-example.html?preview=ocr`.
- Fixed 2 absolute local-machine paths in 試一試's `pdfPath` JSON field → relative (matches existing `href`, cleanliness fix, not functional since `href` already took priority for the actual download link).
- Flagged, not changed: site has `../` links needing `Website/` (not just `storymap/`) as the published root (`../references.html`, `../UI Idea/demo-review-tool-fullview.png`, one PDF under `../Visual Material/情報路線/`); `Website/` is ~1GB total from large unlinked archival PDFs under `Visual Material/` — recommend pruning or Git LFS before pushing to GitHub.

Files changed:
- `Website/storymap/storymap-example.html`, `Website/storymap/storymap.css`, `Website/storymap/storymap.js`

Verified:
- `node --check` OK, CSS brace balance 0, HTML tag counts balanced, JSON data block parses, all referenced relative assets confirmed to exist on disk.
- Not visually verified in a browser.

Remaining:
- No git commit made.

### 2026-08-08 14:00 HKT — Codex — Remove the extra PDF page backdrop from the shared lightbox

Summary:
- Made the enlarged PDF image background transparent so it no longer adds a beige backdrop around the page. The dark modal overlay, navigation, close button, and bottom information panel remain unchanged.

Files changed:
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser computed style confirms the lightbox image background is transparent; the Part 7 lightbox still opens with its feature information panel.
- Browser console logs are empty; `node --check Website/storymap/storymap.js` and `git diff --check` pass.

Remaining:
- No git commit made.
- User to decide repo scope for hosting.

### 2026-08-07 21:45 HKT — Claude — Redo reverted image removals; redesign viewport-gate, align breakpoint with 辨識印刷字

Summary:
- Re-removed 適合的研究問題's chart container and the GitHub Repository photo in 所需的工具與資源 — both had reverted back into the file since the earlier turn that removed them, while other later edits (nav renaming, pdfPath fixes, preview mode) stayed intact. Possible concurrent-edit collision; flagged.
- Viewport-gate breakpoint changed 899px→1040px to match `.part3-feature-explorer`'s own stacking breakpoint (辨識印刷字 etc.).
- Gate copy updated to the requested wording; visual redesigned to match the site's hero/section-hero style (gradient backdrop, icon, yellow eyebrow, serif headline, larger body text) instead of the plain small card.

Files changed:
- `Website/storymap/storymap-example.html`, `Website/storymap/storymap.css`

Verified:
- `node --check` OK, CSS brace balance 0, HTML tag counts balanced, JSON data block parses, confirmed the two images are gone again.
- Not visually verified in a browser.

Remaining:
- No git commit made.

### 2026-08-07 22:30 HKT — Claude — Fix preview lock bug, extend fade to 步驟三至五, block mobile entirely, font-size pass

Summary:
- Fixed preview-mode tab lock: locked tabs (平台介面/平台運作流程) were still switching panels because the block-click listener was added after the original nav listener (same-target listeners fire in registration order, not by capture flag) — now clone-and-replace strips the original listener first.
- `#part-3-ai` (步驟三至五) added to the preview-mode fade list; only 步驟二 stays fully open now.
- Mobile gate now blocks touch devices in any orientation ("手機版仍在開發中，請改用電腦瀏覽"), not just portrait.
- Font sizes fixed: too-big Agentic AI/PaddleOCR and JSON-viewer visuals scaled down (20-25px→12-15px); too-small 試一試 text and steps 7/8's feature-explorer info-panel text + code windows scaled up (~11-13.5px→13-15px, code-window auto-shrink floor raised from 9px to 10.5px).

Files changed:
- `Website/storymap/storymap.js`, `storymap-example.html`, `storymap.css`, `storymap-cards.css`

Verified:
- `node --check` OK, both CSS files brace-balanced, HTML tag counts balanced, JSON data block parses.
- Not yet re-checked on the live t-preview deployment.

Remaining:
- No git commit made; user needs to push to the separate t-preview repo.

### 2026-08-07 22:45 HKT — Claude — Bump 輸出格式：JSON's button/body text to match Agentic OCR chat bubble size

Summary:
- 輸出格式：JSON's field-jump buttons and JSON code window text bumped from 12/12.5px to 15px, matching the size of the existing "set up PaddleOCR on my mac..." user-message bubble in 運用 Agentic AI 使用 PaddleOCR (`--agentic-codex-text-size: 15px`), per user's size reference.

Files changed:
- `Website/storymap/storymap-cards.css`

Verified:
- CSS brace balance 0, node --check OK (unaffected file).
- Not visually verified.

Remaining:
- No git commit made; t-preview folder not touched this round (its .git/index.lock still present).

### 2026-08-08 13:55 HKT — Codex — Add document lightbox navigation to Part 7, Part 8, and 試一試

Summary:
- Extended the shared image lightbox to accept per-page titles and descriptions while preserving existing image galleries.
- Made the Part 7 printed-document page, Part 8 handwritten folded panels, and both printed/handwritten 試一試 document views clickable. Each opens the enlarged document view with previous/next navigation, a bottom information panel, an X button, outside-click closing, and the existing keyboard controls.
- The enlarged view keeps the currently selected annotated feature image and its description where applicable; ordinary pages show the corresponding original scan.

Files changed:
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser checks passed for Part 7 (2 pages), Part 8 (4 scanned pages), printed 試一試 (2 pages), and handwritten 試一試 (3 pages), including page navigation, feature descriptions, X closing, and outside-click closing.
- Browser console logs are empty; `node --check Website/storymap/storymap.js` and `git diff --check` pass.

Remaining:
- No git commit made.

### 2026-08-08 13:30 HKT — Claude — 手機版：史料抽屜（7／8／11）＋解除手機封鎖

Summary:
- Mobile block removed (rotate gate deleted); phones now get a real layout. The "widen window" gate remains desktop-only.
- New ≤820px pattern for 7／8／11: info panel becomes the page body; document collapses into a left-pull drawer (default 172px, drag-resizable via right-border grip, expandable to full width).
- Drawer chrome: number circle + large feature name header; four joined icon buttons centered at the bottom (prev/next feature, expand, close); arrows step features while dragging the image past an edge changes page.
- Expanded state centers the PDF and zooms the image only (＋/−, pinch, double-tap, ctrl+wheel).
- Feature picking moves to a sticky chip row above the panel; chips proxy the existing tag buttons, with a MutationObserver syncing state back, so no feature logic is duplicated. 11 gets no chips (no tags) and its arrows fall back to page nav.
- Desktop untouched: the drawer wrapper is `display: contents` above 820px, so `.part3-fx-doc` remains a direct grid child.
- Prototypes kept in `Website/UI Idea/mobile-7-8-11-drawer-prototype{,-v2,-v3}.html`.

Files changed:
- `Website/storymap/storymap.css`, `storymap.js`, `storymap-example.html`

Verified:
- node --check OK; CSS balanced; HTML tags balanced; JSON blocks parse.
- Not tested in a browser or on a phone yet.

Remaining:
- No git commit; needs device testing then syncing to t-preview.

### 2026-08-08 14:05 HKT — Claude — 修正桌面版破版；移除窄視窗警告，改用手機版面

Summary:
- Fixed desktop breakage in 7／8／11: `.mdrawer-edge` was not hidden on desktop, and because the drawer wrapper is `display: contents`, those two edge labels became extra grid items and shifted the whole two-column layout. Now hidden by default, shown only in the mobile block.
- Removed the narrow-window warning overlay entirely (CSS + markup); narrow desktop windows get the mobile layout instead.
- Drawer breakpoint moved 820px → 1040px to match where the old gate fired.
- Deleted three obsolete ≤1040px stacking blocks whose ID selectors out-specified the drawer rules (one forced `min-height: 95svh` on the doc inside the drawer). Comment left in their place.

Files changed:
- `Website/storymap/storymap.css`, `storymap-example.html`

Verified:
- CSS brace depth scan clean (caught a stray `}`); node --check OK; HTML tags balanced; JSON parses; no viewport-gate refs left.
- Not yet checked in a browser — desktop ≥1041px is the priority re-check.

Remaining:
- No git commit; needs device pass then t-preview sync.

### 2026-08-08 15:07 HKT — Codex — Add the AI model comparison table

Summary:
- Added the six-column AI model comparison table beneath `選用的AI Model`.
- Preserved the requested Claude Opus and GPT（5.6） wording, completed DeepSeek Flash／Pro and Gemini Flash, and marked the latter two as `必須使用` through API.
- Added section-specific table sizing and horizontal scrolling for narrower screens.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`

Verified:
- Browser-rendered the table with four model rows beneath the text card.
- Confirmed horizontal scrolling at 820px viewport width.
- Browser console has no errors or warnings; `node --check Website/storymap/storymap.js` and `git diff --check` pass.

Remaining:
- No external deployment or t-preview sync performed.

### 2026-08-08 16:22 HKT — Codex — Simplify the narrow-screen menu control

Summary:
- Changed the narrow-screen `選單` control to show only the hamburger symbol.
- Removed its decorative border, background, rounded button surface, and text label so it matches the adjacent settings symbol.
- Kept the sliding section panel and its navigation behavior unchanged.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`

Verified:
- At 390px, the control has no text, transparent background, and no border; the menu still opens correctly.
- Browser console has no errors or warnings; `node --check Website/storymap/storymap.js`, CSS brace checks, and `git diff --check` pass.

Remaining:
- No external deployment or t-preview sync performed.

### 2026-08-08 16:17 HKT — Codex — Add a narrow-screen section menu

Summary:
- Replaced the centered top-level navigation with a single `選單` button at ≤1040px for both mobile and narrow computer windows.
- Added a right-to-left sliding section panel containing 主頁、平台簡介、平台介面、平台運作流程、運用平台研究其他問題.
- Added an X close button, backdrop close, Escape close, active-section highlighting, and automatic close after navigation.
- Kept the original desktop navigation unchanged above 1040px.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`

Verified:
- Browser-tested at 390px and 900px: menu button, five links, right-side panel, X close, and section navigation work.
- Browser-tested at 1280px: original navigation remains visible and compact menu is hidden.
- Browser console has no errors or warnings; `node --check Website/storymap/storymap.js`, CSS brace checks, and `git diff --check` pass.

Remaining:
- No external deployment or t-preview sync performed.

### 2026-08-08 16:16 HKT — Codex — Restore the Agentic AI visual on narrow screens

Summary:
- Kept the visual element for `運用 Agentic AI 使用 PaddleOCR` visible in both the mobile mode and the narrow computer-window mode.
- Added a scoped responsive height for the Agentic AI frame and an explicit height for its absolutely positioned scene, so the Python and Codex windows no longer collapse when the shared visual-frame rule changes to `height: auto`.

Files changed:
- `Website/storymap/storymap.css`

Verified:
- At 1024px wide, the Agentic frame is 560px high and the inner scene is rendered at about 519px high.
- At 390px wide, the Agentic frame is 560px high and the inner scene is rendered at 528px high.
- Browser screenshot confirms the overlapping PaddleOCR Python and Codex windows are visible in the mobile layout.
- No external deployment or t-preview sync performed.

Remaining:
- No git commit created because the worktree already contains unrelated user edits and prototype files.

### 2026-08-08 16:03 HKT — Codex — Add a mobile model-card carousel

Summary:
- Added a mobile-only vertical card layout for `選用的AI Model`.
- The first mobile view shows Claude Opus and GPT（5.6）; the arrow in the first card switches to DeepSeek Flash／Pro and Gemini Flash, with a back arrow on the second view.
- Kept the desktop six-column table unchanged and aligned the mobile breakpoint with the website's existing 1040px mobile mode.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap.js`

Verified:
- Browser-tested at 390px and 900px: vertical cards appear without horizontal overflow, and both carousel directions work.
- Browser-tested at 1280px: all four desktop table rows remain visible and arrows are hidden.
- Browser console has no errors or warnings; `node --check Website/storymap/storymap.js`, CSS brace checks, and `git diff --check` pass.

Remaining:
- No external deployment or t-preview sync performed.

### 2026-08-08 16:22 HKT — Codex — Refresh mobile photo-gallery scroll behavior

Summary:
- Confirmed the latest commit's mobile and narrow-computer photo gallery behavior: the image and collapsed title row appear first; scrolling down expands the information panel when its top reaches 56% of the viewport height, leaving space before the midpoint; scrolling back up collapses it after the 66% reset buffer.
- Bumped the StoryMap CSS/JS cache key so the preview loads the current behavior after reload.

Files changed:
- `Website/storymap/storymap-example.html`

Verified:
- `node --check Website/storymap/storymap.js` passed; `git diff --check` passed.
- Browser reload was blocked for the local `file://` page by the browser safety policy, so no new visual browser verification was recorded.

Remaining:
- Reload the local preview normally and check one mobile width and one narrow desktop width.

### 2026-08-08 16:36 HKT — Codex — Trigger photo-gallery expansion from the photo midpoint

Summary:
- Changed the mobile and narrow-computer scroll trigger to measure the photo stage's top edge instead of the information panel's top edge.
- The panel now expands when the photo top crosses the viewport midpoint; scrolling back up collapses it after a 56% reset buffer.
- Refreshed the StoryMap CSS/JS cache key.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`

Verified:
- `node --check Website/storymap/storymap.js` passed; CSS brace checks passed; `git diff --check` passed.
- Browser reload remained blocked for the local `file://` page by the browser safety policy.

Remaining:
- Reload the local preview and check the photo-top midpoint trigger at one mobile width and one narrow desktop width.

### 2026-08-08 16:40 HKT — Codex — Simplify the compact menu and font settings controls

Summary:
- Removed the visible `網站章節` heading from the narrow-screen section drawer.
- Moved the borderless `×` control beside the menu symbol in the header; it is shown only while the drawer is open, and the existing backdrop click closes the drawer.
- Removed the visible `網站設定` heading and changed the font controls to `字體 − 100% ＋`, without the `A−` or `A＋` labels.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`

Verified:
- `node --check Website/storymap/storymap.js` passed; `git diff --check` passed.
- The live page confirmed there is no drawer heading, no settings heading, and the controls render as `−` and `＋`; the desktop layout keeps the compact controls hidden.

Remaining:
- Check the open narrow-screen drawer visually at a mobile viewport.

### 2026-08-08 16:53 HKT — Claude — Mobile/narrow-screen layout for 所需的工具與資源 and 重用平台的基本流程

Summary:
- Approved sample prototype first (`Website/UI Idea/mobile-tools-flow-prototype.html`), then applied to the live site.
- 所需的工具與資源: mobile/narrow (≤1040px or touch) hides the 工具清單 list, 工具資訊 fills full height, left/right arrows switch tools via the existing radio-row logic, per-tool number box replaced by one shared tick badge that resets to empty and replays a fill+pop each time a new tool is shown.
- 重用平台的基本流程: 8 steps regridded into 2 columns × 4 rows (1-4 left top-to-bottom, 5 beside 4, 6-8 climbing back up the right column), fills remaining screen height, plays a staggered "unfold the box" reveal on first scroll into view (new `initPart3MobileFlowUnfold()`), replayable via a button. Desktop chevron unchanged.
- Deleted the stale `@media (max-width: 760px)` tools-checklist stacking block (conflicted with the new full-height design, same pattern as the earlier 7/8/11 stale-rule removals).

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`
- `Website/UI Idea/mobile-tools-flow-prototype.html`

Verified:
- `node --check Website/storymap/storymap.js` passed.
- CSS brace depth-scan balanced; HTML tag-balance counts matched; embedded JSON blocks parsed; all new data-attribute selectors cross-checked between HTML and JS.

Remaining:
- Not tested in an actual browser/device. No git commit made; t-preview not re-synced.

### 2026-08-08 16:55 HKT — Codex — Restrict settings and menu panels to their own hover zones

Summary:
- Isolated the font settings control from the menu control so hovering one cannot open the other panel.
- Settings opens while hovering the gear or its panel and closes after leaving that area.
- The compact menu opens while hovering the menu symbol or its drawer, closes after leaving both, and remains click-open for touch devices.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`

Verified:
- `node --check Website/storymap/storymap.js` passed; `git diff --check` passed; CSS brace checks passed.
- Live page confirmed the settings panel content and that the compact menu remains hidden on desktop; the browser supports the hover-state selector used for the menu close symbol.

Remaining:
- Check the hover transition visually at one narrow viewport.

### 2026-08-08 17:08 HKT — Codex — Remove the compact menu close button

Summary:
- Removed the `×` button from the header and deleted its styling and event listeners.
- The menu now closes through hover-out, outside-click, or Escape.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`

Verified:
- `node --check Website/storymap/storymap.js` passed; `git diff --check` passed; CSS brace checks passed.
- Confirmed no close-button selector or element remains.

Remaining:
- Check the menu visually at one narrow viewport.

### 2026-08-08 17:05 HKT — Codex — Make Part 2 research-value rows inline on narrow screens

Summary:
- Added a responsive two-row accordion for `清代奏折制度` and `清代奏折的研究價值`.
- Each row now follows the requested order: title bar → visual element → original text box.
- The second row receives the original second gallery image (`done-intro-2.png`) so its visual no longer remains at the bottom of the whole list.
- Scrolling to a row title auto-expands that row; clicking the title also opens or closes it. The original side-by-side layout remains available above 1040px and returns correctly after resizing.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap.js`

Verified:
- `node --check Website/storymap/storymap.js` passed; CSS brace checks and `git diff --check` passed.
- Browser visual reload remains unavailable for the local `file://` page because of the browser safety policy.

Remaining:
- Reload the page in a permitted HTTP/browser preview and check the row-title auto-expansion at mobile and narrow-computer widths.

### 2026-08-08 17:10 HKT — Codex — Make the first Part 3 sections viewport-height on narrow screens

Summary:
- Made `第三部分／運用平台研究其他的問題` and `1／適合的研究問題` share one viewport below the top bar; `2／所需的工具與資源` remains a separate full-viewport section.
- Changed the tools/resources checklist from a fixed height to a flexing panel, so its visual and text areas adapt to the remaining screen space.

Files changed:
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-cards.css`

Verified:
- At 1024×900 and 390×844, the cover plus research-question section sums to `100svh - 62px`; the tools section independently computes to `100svh - 62px`.
- The tools card now flexes to the remaining section height instead of retaining the previous 1000px fixed height.
- Browser screenshots confirm the research card and tools/resources panel fit the viewport; console has no errors or warnings.
- No external deployment or t-preview sync performed.

Remaining:
- No git commit created because concurrent Claude/user edits were present in the worktree; those changes were preserved.

### 2026-08-08 17:20 HKT — Claude — Fix mobile 工具與資源／基本流程 layout bugs

Summary:
- Tools carousel: fixed tick/count overlapping the title bar (offset nav layer below the bar); fixed copy text not rendering (grid percentage-height chain replaced with flexbox column).
- Flow grid: fixed uneven box sizes (`1fr` → `minmax(0,1fr)`), centered text, larger font, narrowed grid to 300px centered (chart background shows through as a shared backdrop), unified all 8 boxes to one background color.
- Removed the replay button entirely; reveal animation now triggers once via scroll position (when the heading text reaches 70% up the screen from the bottom) instead of an early IntersectionObserver.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`

Verified:
- `node --check` passed; CSS brace depth-scan balanced; HTML tag-balance matched; no leftover references to the removed button.

Remaining:
- Not tested in a real browser/device. No git commit made.

### 2026-08-08 17:40 HKT — Claude — Fix mobile 重用平台的基本流程 sizing/backdrop/color

Summary:
- Section height reduced to 95% of available screen.
- Removed the grey card backdrop behind the 8-box grid.
- Boxes are now true, identically-sized squares via a new `initPart3MobileFlowSquare()` (measures available space, sets `--flow-box-size` used for both grid axes). Larger number/label text.
- Odd boxes white/dark-text, even boxes dark green/light-text with yellow numbers, plus hover/active feedback.

Files changed:
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`

Verified:
- `node --check` passed; CSS brace depth-scan balanced.

Remaining:
- Not tested in a real browser/device.

### 2026-08-10 15:44 HKT — Codex — Remove Part 3 developing blur from OCR preview

Summary:
- Removed the `尚在開發中` faded/blurred overlay and interaction lock from `#part-3-ai` and `#part-3-wiki` in `?preview=ocr`, so the later Part 3 content displays normally.
- Kept the existing OCR preview entry point and the hidden `#part-3-research-questions` / `#part-3-tools` sections unchanged.

Files changed:
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`

Verified:
- `node --check Website/storymap/storymap.js` passed.
- Confirmed no `is-preview-faded`, `preview-faded-badge`, or `LOCKED_SECTION_IDS` references remain.
- Browser QA: `?preview=ocr` showed no faded/badge/inert state on the later Part 3 sections; the normal page did not receive preview styling.

Remaining:
- None for this adjustment.

### 2026-08-10 00:24 HKT — Codex — Keep the normal desktop Codex title bar visible

Summary:
- Moved the Part 4 Codex window 4px inside the scene in normal desktop mode so its title bar is not clipped by the scene's `overflow: hidden` boundary.
- Left mobile and narrow-computer positioning unchanged.
- Refreshed the StoryMap asset version query strings.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap-example.html`

Verified:
- Confirmed the Part 4 markup still contains only the Codex window.
- `node --check Website/storymap/storymap.js` and `git diff --check` passed.

Remaining:
- The in-app browser blocked the local file preview, so the normal desktop visual still needs a manual reload in the user's open preview.

### 2026-08-10 00:09 HKT — Codex — Simplify Part 4 and reclaim Try a Try visual space

Summary:
- Removed the PaddleOCR Python window from Part 4 in every layout and changed the Codex request to “set up PaddleOCR on my computer”.
- Moved the desktop Codex window into the former right-side window area, aligned its top edge with the Part 4 text card, and reduced its desktop height.
- Styled the JSON field controls to match the feature buttons used in Part 7.
- Kept the 印刷字／手寫字 switch beside「11 試一試」and removed the rendered 進度／1／2／3 bar so each step has more visual space.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap.js`

Verified:
- Browser checked desktop Part 4: Codex top edge matches the text card; Python window count is 0.
- Browser checked JSON controls and the Try a Try header; the JSON controls use the Part 7 button treatment and the progress bar is absent.
- Browser checked the narrow layout and reset the temporary viewport override.
- `node --check Website/storymap/storymap.js`, CSS brace checks, and `git diff --check` passed.

Remaining:
- Existing unrelated worktree changes were preserved; no mixed commit was created.

### 2026-08-10 11:53 HKT — Codex — Make the intro 01 gallery image-proportional and align intro 03 labels

Summary:
- Removed the normal desktop gallery's shared fixed height for `清代奏折制度`; each page now sizes its image stage from that image's native aspect ratio and recalculates when the gallery changes pages.
- Reduced the normal desktop gap between the `清代奏折制度` and `清代奏折的研究價值` cards.
- Applied the narrow layout's source-label positioning to the normal desktop `研究清代奏折的主要困難` panel so computed `--source-bubble-top` values are used.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`

Verified:
- Browser checked the local site at 1280px: gallery stage heights were independently measured as 427px, 430px, and 854px for pages 1–3; the card gap was 12px.
- Browser checked the narrow 980px fallback and confirmed the responsive gallery sizing remained active.
- Normal source labels received non-zero computed positions from `--source-bubble-top`.
- `node --check Website/storymap/storymap.js` passed.

Remaining:
- Existing unrelated worktree changes were preserved; no mixed commit was created.

### 2026-08-10 00:00 HKT — Codex — Responsive header, tools height, and OCR JSON timing

Summary:
- Kept the website name visible on the left side of the top bar in mobile and narrow computer modes.
- Set `所需的工具與資源` to fill the viewport height below the top bar in both modes.
- Slowed the JSON wording animation in the `使用OCR的原因` visual from 9ms to 18ms per character.
- Updated the StoryMap CSS and JavaScript cache-busting query versions.

Files changed:
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`

Verified:
- `node --check Website/storymap/storymap.js` passed and `git diff --check` passed.
- Confirmed the responsive header, tools height, and JSON timing overrides are present after the existing mobile/narrow rules.

Remaining:
- Mobile and narrow-screen visual checking still requires a manual reload in the user’s browser.

### 2026-08-08 17:22 HKT — Codex — Give OCR definition/test visuals more narrow-screen height

Summary:
- Kept `使用OCR的原因`／OCR definition and `OCR測試` each within one viewport below the top bar in mobile and narrow-computer modes.
- Reduced their top and bottom section padding to 18px maximum and increased the compact visual heights, while centering both visuals horizontally.
- Made the OCR scan scene internally flex so its document pages and JSON output share the shorter viewport-sized visual without expanding the page.

Files changed:
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-cards.css`

Verified:
- At 390×844, OCR definition is 782px high with a 320.7px centered visual; OCR test has a 303.8px centered visual, and both groups fit within their sections.
- At 1024×900, both sections are 838px high; the OCR visual is 342px and the test visual is 324px, centered horizontally.
- Browser screenshots show the enlarged visuals without adding inner page scrolling.

Remaining:
- No git commit created because concurrent Claude/user edits remain in the worktree; those changes were preserved.

### 2026-08-09 22:40 HKT — Codex — Responsive menu, OCR preview, and Part 3 visual fixes

Summary:
- Made the compact mobile menu button toggle the dropdown closed when clicked again.
- Removed the three pre-OCR sections from the OCR teacher preview so no developing blur area remains above OCR; later unfinished sections remain faded.
- Reduced the Agentic AI／PaddleOCR mobile typography, removed the 7／8 feature-filter backdrop, and changed the 9 JSON field controls to mobile pill buttons without arrows.
- Unified the mobile JSON text size across 7／8 and 9, and made the 11 PDF page fill its available area responsively with aspect-ratio-preserving containment.
- Updated the StoryMap script query version so the browser picks up the responsive fixes after reload.

Files changed:
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`

Verified:
- `node --check Website/storymap/storymap.js` passed and `git diff --check` passed.
- Cache-busted HTTP preview confirmed the three pre-OCR sections are hidden while `part-3-ai` and `part-3-wiki` remain faded.
- Existing concurrent StoryMap CSS changes and untracked handwritten image assets remain preserved.

Remaining:
- The in-app browser does not expose a mobile viewport and blocks the local `file://` tab, so final narrow-screen visual checking still requires a manual reload in the user’s browser.

### 2026-08-08 18:16 HKT — Codex — Recombine folded 手寫字 scans into two-panel pages

Summary:
- Divided each of `page1.png`, `page2.png`, and `page3.png` into equal horizontal panels using the requested order: right = `a`, middle = `b`, left = `c`.
- Recombined the panels into `1a1b`, `1c2a`, `2b2c`, `3a3b`, and `3c`, with a blank right half on `3c`.

Files changed:
- `Website/storymap/試一試/手寫字/1a1b.png`
- `Website/storymap/試一試/手寫字/1c2a.png`
- `Website/storymap/試一試/手寫字/2b2c.png`
- `Website/storymap/試一試/手寫字/3a3b.png`
- `Website/storymap/試一試/手寫字/3c.png`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- All five outputs are 3106×3423 RGB PNGs.
- Each output was visually inspected; source scans remain unchanged.
- `git diff --check` passes.

Remaining:
- None for this scan recombination.

### 2026-08-08 18:03 HKT — Codex — Add responsive row extension and narrow source windows

Summary:
- Added a smooth scroll-triggered extension for the normal responsive list rows in Parts 3 and 6; Part 3 rows 02–03 remain fully expanded as the zhu113/zhu119 communication views.
- Reduced normal expanded visual heights so the card, visual, and expanded information area fit approximately within the top-bar-excluded viewport, while preserving proportional image fitting.
- Narrowed and centered both source-document windows, kept their labels on both sides with controlled overlap, and hid source-detail hover text in the responsive modes.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`

Verified:
- `node --check Website/storymap/storymap.js` passed.
- Confirmed Part 3 rows 02–03 are excluded from the scroll-extension class and that the responsive source labels use the connector-calculated positions.
- Existing unrelated OCR and drawer/layout edits remain unstaged and preserved.

Remaining:
- Live visual browser verification remains unavailable because the local file URL is blocked by the in-app browser policy.

### 2026-08-08 18:09 HKT — Codex — Continue responsive row and source-window adjustment

Summary:
- Kept the scroll extension limited to ordinary rows and the 97% height target limited to the ordinary expanded row layout.
- Kept Part 3 rows 02–03 expanded and exempt from the row animation, with narrower zhu113/zhu119 documents and side labels that may overlap the windows.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap-cards.css`

Verified:
- `node --check Website/storymap/storymap.js` passed.
- `git diff --check` passed.

Remaining:
- Live visual browser verification remains unavailable because the local file URL is blocked by the in-app browser policy.

### 2026-08-08 18:06 HKT — Codex — Set cover/research group to a 60% height target

Summary:
- Set the combined `運用平台研究其他的問題`＋`適合的研究問題` responsive target to 60% of the top-bar-excluded viewport.
- Allowed the research section to grow to its content minimum on narrow screens so the research card remains fully readable instead of being clipped.

Files changed:
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-cards.css`

Verified:
- At 390×844, the cover is 287.0px and the content-safe research section is 367.0px.
- At 1024×900, the cover is 306px and the content-safe research section is 319.9px.
- CSS and syntax checks passed.

Remaining:
- No git commit created because concurrent Claude/user edits remain in the worktree; those changes were preserved.

### 2026-08-08 17:41 HKT — Codex — Narrow OCR visual width and test visual height

Summary:
- In mobile and narrow-computer modes, reduced the `使用OCR的原因` visual to 70% width and centered it horizontally.
- Reduced the `OCR測試` visual to 60% of its available visual height and centered it within the visual area.

Files changed:
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-cards.css`

Verified:
- At 390×844, the OCR visual is 250.6px wide and the test visual is 281.5px high from a 469.1px available area.
- At 1024×900, the OCR visual is 668.1px wide and the test visual is 389.3px high from a 648.9px available area.
- Both remain centered; syntax and CSS balance checks passed.

Remaining:
- No git commit created because concurrent Claude/user edits remain in the worktree; those changes were preserved.

### 2026-08-08 17:38 HKT — Codex — Restore original OCR section inner spacing

Summary:
- Restored the original top and bottom padding for the OCR definition and OCR test sections.
- Kept the 150% height for `1＋2＋visual` and 130% height for `10＋visual`; the visuals continue to flex into the remaining space and stay horizontally centered.

Files changed:
- `Website/storymap/storymap.css`

Verified:
- At 390×844, both sections restore 56px top/bottom padding; OCR visual height is 643.7px and OCR test visual height is 469.1px.
- At 1024×900, both sections restore 61.44px top/bottom padding; OCR visual height is 799.0px and OCR test visual height is 648.9px.

Remaining:
- No git commit created because concurrent Claude/user edits remain in the worktree; those changes were preserved.

### 2026-08-08 17:30 HKT — Codex — Expand OCR definition/test sections to 150%／130% height

Summary:
- Replaced the previous compact inner spacing with sections that use 150% of the top-bar-excluded viewport for `1＋2＋visual` and 130% for `10＋visual` in mobile and narrow-computer modes.
- Let both visuals flex into the additional section height and remain horizontally centered.

Files changed:
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-cards.css`

Verified:
- At 390×844, the OCR definition section is 1173px high with a 722px visual; the OCR test section is 1016.6px high with a 547.4px visual.
- At 1024×900, the OCR definition section is 1257px high with an 885.9px visual; the OCR test section is 1089.4px high with a 735.8px visual.
- Both visuals are horizontally centered; syntax and CSS balance checks passed.

Remaining:
- No git commit created because concurrent Claude/user edits remain in the worktree; those changes were preserved.

### 2026-08-08 17:45 HKT — Codex — Separate intro cards and responsive research visuals

Summary:
- Restored Part 2 as two complete, independent text cards and kept the existing three-page gallery between card 1 and card 2 on mobile and narrow-computer layouts.
- Replaced the responsive folded-row treatment for Parts 3 and 6 with sequential full text cards followed by their matching visual panels.
- Set the first visual row to approximately 97% of the top-bar-excluded viewport and the second and third rows to approximately 130%, with the Part 3 source visuals constrained to the website width.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`

Verified:
- Removed the previous `intro-inline` implementation and confirmed the original Part 2 gallery data remains in one gallery.
- `node --check Website/storymap/storymap.js` passed.
- Static structure and obsolete-selector checks passed.
- Live visual browser verification remains unavailable because the local file URL is blocked by the in-app browser policy.

Remaining:
- Review the responsive layout visually when the local browser can load the updated file.

### 2026-08-08 17:49 HKT — Codex — Make OCR visual proportional and test section content-sized

Summary:
- Kept the `使用OCR的原因` visual at 70% width, but changed its height to a proportional 1.05:1 width-to-height ratio so the pages and JSON output scale together.
- Restored `OCR測試` to a natural 1:1 visual size and removed the forced 130% section height; the whole part now follows the text, gap, visual, and original padding.
- Reduced the test text-to-visual gap to the normal compact section gap.

Files changed:
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-cards.css`

Verified:
- At 390×844, the OCR visual is 250.6×238.7px; the OCR test part is 866.3px high with a 322.2px visual.
- At 1024×900, the OCR visual is 668.1×636.3px; the OCR test part is 996.9px high with a 560px visual.
- Both modes retain the original 56px／61.44px section padding and the visuals are centered.

Remaining:
- No git commit created because concurrent Claude/user edits remain in the worktree; those changes were preserved.

### 2026-08-08 17:53 HKT — Codex — Trigger gallery panels from current image position

Summary:
- Removed the requirement for a prior scroll event before a gallery information panel can expand.
- Recalculate the image position after gallery creation, resizing, and tab visibility changes, so an image already above the screen midpoint opens its panel immediately.
- Kept the existing midpoint threshold, upward collapse buffer, and panel animation.

Files changed:
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`

Verified:
- `node --check Website/storymap/storymap.js` passed.
- Confirmed the `hasScrolled` gate is absent and the immediate position checks are registered.
- Existing unrelated OCR layout edits remain unstaged and preserved.

Remaining:
- Live visual browser verification remains unavailable because the local file URL is blocked by the in-app browser policy.

### 2026-08-08 18:03 HKT — Codex — Add responsive row extension and narrow source windows

Summary:
- Added a smooth scroll-triggered extension for the normal responsive list rows in Parts 3 and 6; Part 3 rows 02–03 remain fully expanded as the zhu113/zhu119 communication views.
- Reduced normal expanded visual heights so the card, visual, and expanded information area fit approximately within the top-bar-excluded viewport, while preserving proportional image fitting.
- Narrowed and centered both source-document windows, kept their labels on both sides with controlled overlap, and hid source-detail hover text in the responsive modes.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`

Verified:
- `node --check Website/storymap/storymap.js` passed.
- Confirmed Part 3 rows 02–03 are excluded from the scroll-extension class and that the responsive source labels use the connector-calculated positions.
- Existing unrelated OCR and drawer/layout edits remain unstaged and preserved.

Remaining:
- Live visual browser verification remains unavailable because the local file URL is blocked by the in-app browser policy.

### 2026-08-08 17:56 HKT — Codex — Widen the 7/8 mobile史料抽屜 and focus each highlight

Summary:
- Widened the default 7/8史料抽屜, enlarged the four bottom controls, and kept the width grip centered on the right border.
- Added per-feature focus coordinates and scale values so each annotated printed or handwritten image opens with its highlighted area centered.

Files changed:
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-cards.css`

Verified:
- `node --check Website/storymap/storymap.js` passed; CSS brace checks passed; `git diff --check` passed.
- Checked all 7 printed and 8 handwritten annotated assets and added a focus rule for each feature.

Remaining:
- Reload the live page and check the drawer at a narrow viewport.

### 2026-08-08 18:01 HKT — Codex — Content-size OCR definition section

Summary:
- Increased the `使用OCR的原因` visual to 80% width and kept its 1.05:1 proportional height.
- Removed the fixed 150% height from the OCR definition part; its height now follows cards 1 and 2, the compact gap, the visual, and the restored original padding.
- Removed the extra top space above `甚麼是 OCR？` and bottom space below the visual.

Files changed:
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-cards.css`

Verified:
- At 390×844, the part is 802.0px high, the centered visual is 286.4×272.8px, and the original 56px padding is restored.
- At 1024×900, the part is 1185.2px high, the centered visual is 763.5×727.1px, and the original 61.44px padding is restored.
- The card-to-visual gap is approximately 14px in both narrow modes.

Remaining:
- No git commit created because concurrent Claude/user edits remain in the worktree; those changes were preserved.

### 2026-08-09 22:54 HKT — Codex — Move Try a Try download controls into Step 1

Summary:
- Removed the `下載` and `已下載` buttons from the PDF metadata strip for both 印刷字 and 手寫字 modes.
- Added the two buttons below the Step 1 guide text, using the same primary／secondary interaction style as `一 · 安裝工具`.
- Kept `下載` opening the selected PDF before advancing, while `已下載` advances without opening it.

Files changed:
- `Website/storymap/storymap.js`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`

Verified:
- `node --check Website/storymap/storymap.js` passed and `git diff --check` passed.
- Live HTTP inspection confirmed both modes show the correct PDF filename, no old download-strip buttons, and the two Step 1 guide buttons.

Remaining:
- Narrow-screen visual checking still requires a manual reload in the user’s browser.

### 2026-08-09 23:07 HKT — Codex — Adjust folded 手寫字 scan recombinations

Summary:
- Rebuilt the folded scan outputs using the confirmed panel order `1b1a`, `2a1c`, `2c2b`, and `3c3b3a`.
- Removed the superseded derived outputs so the folder contains only the current recombinations.

Files changed:
- `Website/storymap/試一試/手寫字/1b1a.png`
- `Website/storymap/試一試/手寫字/2a1c.png`
- `Website/storymap/試一試/手寫字/2c2b.png`
- `Website/storymap/試一試/手寫字/3c3b3a.png`
- Removed superseded `1a1b.png`, `1c2a.png`, `2b2c.png`, `3a3b.png`, and `3c.png`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `1b1a.png`, `2a1c.png`, and `2c2b.png` are 3106×3423 RGB PNGs.
- `3c3b3a.png` is a 4659×3423 RGB PNG.
- Visual inspection confirmed the requested left-to-right panel sequences.

Remaining:
- No git commit created because concurrent Claude/user edits remain in the worktree; those changes were preserved.

### 2026-08-09 23:11 HKT — Codex — Hide the pre-步驟二 flow responsively

Summary:
- Hid `重用平台的基本流程` from normal computer mode because it appears before `步驟二`.
- Kept its title and explanation on mobile／narrow computer layouts, while hiding the 8-square flow chart and removing its reserved height.

Files changed:
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`

Verified:
- `node --check Website/storymap/storymap.js` passed and `git diff --check` passed.
- Confirmed the desktop and narrow-screen visibility rules are separated by the existing 1040px breakpoint.

Remaining:
- Narrow-screen visual checking still requires a manual reload in the user’s browser.

### 2026-08-09 23:16 HKT — Codex — Keep the pre-步驟二 chart visible

Summary:
- Removed the responsive hide rules so `重用平台的基本流程` and its 8-square chart remain visible in normal computer, mobile, and narrow computer modes.

Files changed:
- `Website/storymap/storymap.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`

Verified:
- `node --check Website/storymap/storymap.js` passed and `git diff --check` passed.

Remaining:
- Narrow-screen visual checking still requires a manual reload in the user’s browser.

### 2026-08-09 HKT — Claude — Fix 辨識手寫字 source image missing in mobile 史料 drawer

Summary:
- Section 8 renders its source as a 3D accordion of CSS background-image panels (thirds of a sheet), not `<img>`, so the drawer's image rules never matched and the panel showed blank.
- Drawer now shows one fold at a time at full drawer width (aspect from `--fold-aspect`); expanded shows two folds side by side.
- `<` / `>` step fold-by-fold in section 8; picking a feature chip jumps to that feature's fold; drag-to-edge and pinch zoom supported.
- Desktop accordion logic untouched (`.is-open` vs the new mobile-only `.is-mopen`).

Files changed:
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`

Verified:
- `node --check` passed; CSS depth-scan balanced; cascade order and JSON fold/feature indices confirmed.

Remaining:
- Not tested in a real browser/device.

### 2026-08-10 16:27 HKT — Codex — Add Codex-style AI Skills example for daily event classification

Summary:
- Added a right-side Codex-style conversation to `修改、建立AI Skills`, using `qianlong37_dates_by_day.json` as the user-provided input example.
- The prompt asks AI to segment each day into atomic events and classify them into the established 11 categories. The response presents a reusable Skill draft, `classify-qianlong-diary-events.md`, with `qianlong37_events_by_category.json` as the output target.
- The visual preserves source provenance, exact quotations, OCR uncertainty, and a researcher-review checkpoint, and stacks below the explanatory cards on narrow screens.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`

Verified:
- `git diff --check` passed.
- `node --check Website/storymap/storymap.js` passed; the existing Agentic Codex animation handled the new scene without JavaScript changes.
- In-app browser check passed at desktop and 390×844: desktop side-by-side geometry, mobile stacking, contained response scrolling, and completed animated response were confirmed.

Remaining:
- Unrelated concurrent StoryMap edits and four untracked handwritten-image assets remain untouched in the worktree.
- The visual is a draft Skill example for teaching; it does not execute the full classification pipeline.

### 2026-08-09 HKT — Claude — Refine 辨識手寫字 mobile drawer

Summary:
- `直排單欄` / `正文字體` moved from fold 0a to 1b so the drawer shows the fold containing their highlight.
- Collapsed drawer arrows switch feature again; fold/page stepping only in the expanded drawer (drag-to-edge matches).
- Width grip moved out of `.mdrawer` (its overflow+transform clipped it) to the root, now fixed-positioned so the right border runs through the button's centre; `--mdrawer-w` moved to the root accordingly.
- Collapsed drawer shows the fold at full drawer width (no padding).
- Expanded drawer reuses the original accordion, centred both ways, instead of the two-fold layout.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`

Verified:
- `node --check` passed; CSS depth-scan balanced; feature JSON re-parsed; specificity of new overrides confirmed.

Remaining:
- Not tested in a real browser/device.

### 2026-08-10 00:18 HKT — Codex — Separate Part 7/8 backdrop and PDF colors

Summary:
- Gave「7 辨識印刷字」and「8 辨識手寫字」separate backdrop and PDF color tokens.
- Kept the printed PDF a cool paper white and the handwritten PDF a warm manuscript-paper tone, with distinct dark backdrops behind each viewer.
- Applied the same separation to the responsive drawer, including the handwritten folded panels.

Files changed:
- `Website/storymap/storymap.css`

Verified:
- Browser checked both viewers at the default desktop viewport and at 390×844.
- Computed styles confirm separate backdrop/PDF layers: printed `rgb(23, 61, 64)` / `rgb(255, 253, 248)` and handwritten `rgb(38, 59, 62)` / `rgb(234, 216, 184)`.
- `git diff --check` passed; temporary browser viewport was reset.

Remaining:
- Existing unrelated worktree changes were preserved; no mixed commit was created.

### 2026-08-09 HKT — Claude — Assign remaining 辨識手寫字 features to their fold

Summary:
- 臣字款→1b (panel 4), 抬頭→2b (panel 7), 硃批→2a (panel 6), 印章→3a (panel 9); 浮水印 already correct at 3b (panel 10). 上奏官員 left unchanged (0a, not mentioned).

Files changed:
- `Website/storymap/storymap-example.html`

Verified:
- Re-parsed feature JSON, confirmed all resulting labels match the request.

Remaining:
- Not tested in a real browser/device.

### 2026-08-10 00:26 HKT — Codex — Lighten the Try a Try PDF backdrop

Summary:
- Replaced the dark green surrounding area in「11 試一試」with a very light grey backdrop in both 印刷字 and 手寫字 modes.
- Kept the printed PDF near-white and the handwritten PDF warm beige so the document surface remains distinct from the surrounding area.
- Applied the same colors to the narrow/mobile layout.

Files changed:
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-cards.css`

Verified:
- Browser checked both modes at the default viewport and at 390×844.
- Computed styles confirm light-grey backdrops and separate PDF surfaces in both modes.
- `node --check` and `git diff --check` passed; temporary browser viewport was reset.

Remaining:
- Existing unrelated worktree changes were preserved; no mixed commit was created.

### 2026-08-10 HKT — Claude — Fix width-grip position; more fold assignments

Summary:
- Grip was floating mid-image because `.mdrawer`'s width default and `.mdrawer-grip`'s left default were two different hardcoded values. Fixed by declaring `--mdrawer-w` once on the explorer root and having both consume the inherited value — single source of truth.
- 上奏官員→1b, 硃批→1c, 印章→1c (same fold as 硃批); 浮水印 unchanged at 3b.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`

Verified:
- `node --check` passed; CSS depth-scan balanced; feature JSON re-parsed, all 8 fold labels confirmed.

Remaining:
- Not tested in a real browser/device.

### 2026-08-10 00:33 HKT — Codex — Enlarge and align the Part 4 Codex visual

Summary:
- Enlarged the Agentic AI visual window in desktop and narrow layouts.
- Increased Codex text to 18px and the title bar text to 14px in all animation states.
- Removed the frame inset so the desktop Codex top aligns with the text card; the narrow layout now places the larger window directly below the card.

Files changed:
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-cards.css`

Verified:
- Browser checked desktop and 390×844 layouts.
- Desktop Codex top and text-card top both compute to `138.859375px`; narrow Codex is enlarged to `329.36 × 504px` with 18px text.
- `node --check` and `git diff --check` passed; temporary browser viewport was reset.

Remaining:
- Existing unrelated worktree changes were preserved; no mixed commit was created.

### 2026-08-10 HKT — Claude — Fix expanded mode blank for 辨識手寫字 drawer

Summary:
- Stepping folds via `<`/`>` while collapsed never updated the desktop accordion's `pair`/`.is-open` state, so expanding ("整頁") after arrow-stepping showed nothing (all panels stayed as closed slivers).
- Fixed: expanding now syncs `pair` to the current fold and calls the shared `render()`, so the right pair opens immediately.

Files changed:
- `Website/storymap/storymap.js`

Verified:
- `node --check` passed; call path traced (fullBtn → refresh → sync+render on every expand).

Remaining:
- Not tested in a real browser/device.

### 2026-08-10 00:39 HKT — Codex — Shorten the Part 4 Agentic AI visual

Summary:
- Reduced the Agentic AI visual height in both desktop and narrow layouts.
- Kept the enlarged 18px Codex text and aligned the shorter window to the text card on desktop and directly below it on narrow screens.
- Content remains scrollable inside the shorter Codex window.

Files changed:
- `Website/storymap/storymap-cards.css`

Verified:
- Browser checked desktop and 390×844 layouts.
- Desktop visual/codex height is `499.20 / 429.30px`; narrow visual/codex height is `460 / 395.59px`, with 18px text.
- Temporary browser viewport was reset.

Remaining:
- Existing unrelated worktree changes were preserved; no mixed commit was created.

### 2026-08-10 11:40 HKT — Codex — Restore normal-mode Part 3 steps and Try It desktop panel

Summary:
- Kept the sections before `步驟二` visible in normal mode; the explicit OCR preview remains the mode that hides them.
- Restored the desktop `試一試` info-panel top bar with `進度 1 2 3` and the `印刷字／手寫字` switch.
- Restored the dark-green PDF surround and made the desktop PDF use the available document height while preserving its aspect ratio; narrow mode keeps its existing mobile drawer layout.
- Added cache-busting version strings so the edited HTML, CSS, and JavaScript are loaded together.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-cards.css`

Verified:
- Browser checked normal desktop at 1280×900, including both 印刷字 and 手寫字 modes.
- Browser checked narrow mode at 390×844; the desktop panel header is hidden and the mobile switch/drawer remains active.
- `node --check Website/storymap/storymap.js`, `git diff --check`, and CSS brace checks passed.

Remaining:
- Existing unrelated worktree changes were preserved; no mixed commit was created.

### 2026-08-10 11:47 HKT — Codex — Match the Try It floating-paper composition

Summary:
- Adjusted the normal desktop `試一試` viewer to match the reference composition: a centered paper stack floating within the dark-green backdrop, with visible surrounding space and layered paper shadows.
- Kept the Try It document free of feature labels and preserved the narrow/mobile drawer layout.
- Added `--try-pdf-display-h` in `storymap-cards.css` as the single manual control for the desktop paper height; it is currently `76%` of the document backdrop.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap-example.html`

Verified:
- Browser checked the centered desktop paper geometry at 1280×900.
- Browser checked narrow mode at 390×844; its drawer and title-row switch remain active while the desktop panel top bar stays hidden.
- `node --check Website/storymap/storymap.js`, `git diff --check`, and CSS brace checks passed.

Remaining:
- Existing unrelated worktree changes were preserved; no mixed commit was created.

### 2026-08-10 11:52 HKT — Codex — Correct the normal handwritten Try It scan ratio

Summary:
- Corrected the normal desktop handwritten PDF to use its native landscape three-fold ratio (`4649:3380`) instead of stretching into a tall panel.
- Kept the handwritten page centered inside the floating paper stack and preserved the printed mode’s proportions.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap-example.html`

Verified:
- Browser checked handwritten mode at 1280×900: the rendered image now follows the source ratio and remains centered on the green backdrop.
- Browser switched back to printed mode and confirmed its existing `76%` floating-paper geometry remains unchanged.
- `node --check Website/storymap/storymap.js`, `git diff --check`, and CSS brace checks passed.

Remaining:
- Existing unrelated worktree changes were preserved; no mixed commit was created.

### 2026-08-10 12:02 HKT — Codex — Keep 重用平台的基本流程 visible in every version

Summary:
- Removed `part-3-basic-flow` from the `?preview=ocr` hidden-section list.
- Kept the existing normal, narrow, and mobile layouts unchanged while allowing the section to remain visible in all modes.
- Updated the preview documentation and cache-busting version.

Files changed:
- `Website/storymap/storymap.js`
- `Website/storymap/storymap-example.html`

Verified:
- Browser checked `重用平台的基本流程` at normal 1280px, narrow 980px, and mobile 390px with the OCR preview URL; the section remained unhidden and its title was present.
- `node --check Website/storymap/storymap.js` and `git diff --check` passed.

Remaining:
- Existing unrelated worktree changes were preserved; no mixed commit was created.

### 2026-08-10 HKT — Claude — Improve intro tab mobile UI

Summary:
- Added a scroll-in reveal (fade/rise/scale, plays once) for intro cards on mobile via `initIntroMobileReveal()`; sections 3 and 6's tap-to-open panels now pop open with an overshoot easing, animating to a JS-measured real height and releasing the cap afterwards.
- Removed gallery letterbox spacing on mobile by sizing the image area to the active image's aspect ratio (image size unchanged; `cover` images skipped).
- Tightened spacing around the 硃113/硃119 panels without changing their height.
- Shrank the 研究成果 GIF frame on mobile (`--intro-5-visual-scale`, default .78).

Files changed:
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-cards.css`

Verified:
- `node --check` passed; CSS depth-scans balanced; HTML tag balance unchanged; scripted check confirmed every new rule sits inside a mobile media query (desktop untouched).

Remaining:
- Not tested in a real browser/device. Tuning variables exposed for the new sizes/gaps.

### 2026-08-10 HKT — Codex — Normal handwritten Try It folded scan viewer

Summary:
- Normal desktop `試一試` handwritten mode now uses the supplied combined scans `1b1a.png`, `2a1c.png`, `2c2b.png`, and `3c3b3a.png`.
- Base two-part scans render in the same two-fold UI as `8 辨識手寫字`; three-part feature images such as `直欄.png` render as two adjacent folds and can switch to the second pair.
- Narrow/mobile mode continues to use the original single-image viewer, with a CSS safeguard hiding the desktop folded strip.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap-cards.css`
- `Website/storymap/試一試/手寫字/1b1a.png`
- `Website/storymap/試一試/手寫字/2a1c.png`
- `Website/storymap/試一試/手寫字/2c2b.png`
- `Website/storymap/試一試/手寫字/3c3b3a.png`

Verified:
- Browser checked desktop 1280×900 geometry and the annotated feature transition from `摺 1 / 2` to `摺 2 / 2`.
- Browser checked narrow 390×844 fallback: the folded strip is hidden and the original image remains visible.
- `node --check`, `git diff --check`, and CSS brace-depth checks passed.

Remaining:
- Existing concurrent worktree changes were preserved; no mixed commit or deployment was made.

### 2026-08-10 HKT — Codex — Simplify handwritten Try It spreads and final-page layout

Summary:
- Removed the brown fold-edge backdrop and paper-stack layers from normal desktop `試一試` handwritten mode.
- The indicator now shows only `頁 X / 4`.
- The final source spread now opens with a blank page on the left and the rightmost source page on the right.
- Updated `Website/storymap/試一試/手寫字/1b1a.png` so the isolated `奏` is smaller and centered while preserving the original image size and document details.

Files changed:
- `Website/storymap/storymap.js`
- `Website/storymap/storymap-cards.css`
- `Website/storymap/試一試/手寫字/1b1a.png`

Verified:
- Desktop browser checked `頁 1 / 4` and `頁 4 / 4` states, including the final blank-left spread.
- `1b1a.png` remains 3106×3423 RGB PNG.
- `node --check`, `git diff --check`, and CSS brace-depth checks passed.

Remaining:
- Existing concurrent worktree changes were preserved; no mixed commit or deployment was made.

### 2026-08-10 HKT — Codex — Correct handwritten Try It proportions and accordion transitions

Summary:
- Corrected the desktop handwritten Try It frame so the open pair keeps the supplied scan ratio rather than using the old stretched landscape ratio.
- Changed the desktop renderer to a persistent accordion strip like `8 辨識手寫字`: page folds remain in the strip, the previous page collapses, and the next page opens during arrow navigation.
- Kept the three-part annotated feature pair switching and the narrow/mobile single-image fallback.

Files changed:
- `Website/storymap/storymap.js`
- `Website/storymap/storymap-cards.css`

Verified:
- Desktop 1280×900 browser geometry matched the source ratio; page and annotated-feature transitions were checked.
- Narrow 390×844 browser fallback remained on the original image viewer.
- `node --check`, `git diff --check`, and CSS brace-depth checks passed.

Remaining:
- Existing concurrent worktree changes were preserved; no mixed commit or deployment was made.

### 2026-08-10 HKT — Claude — Intro mobile round 2

Summary:
- Gallery info panel now auto-shows for every image (2nd/3rd included) — it was being cleared on every page change and could only be restored by scrolling. Panel now expands downward (gallery height content-driven) instead of shrinking the image, and each image's window fits its own aspect ratio on mobile.
- Reveal system rebuilt: stronger motion, replays both scroll directions, with distinct effects per element type (heading slide-in, text rise, card rise+scale, visual scale, table and 硃113/硃119 panel opening top-to-bottom) plus staggered text inside cards/panels.
- Added muted per-section backdrop variation across the intro (`--intro-bg-1..6`), mobile-only.

Files changed:
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-cards.css`

Verified:
- `node --check` passed; CSS depth-scans balanced; scripted checks confirmed no reveal rule leaks to desktop and the source-panel selector no longer double-targets nested elements.

Remaining:
- Not tested in a real browser/device.

### 2026-08-10 HKT — Claude — Fix heading layout and missing 硃113/硃119 panels

Summary:
- Heading looked detached because `.title-row` inside `.copybox` got its own transform on top of the card's. Added a nesting guard so nested elements only use the opacity-based inner stagger.
- The two doc panels were blank because `clip-path` cut away their side callouts and created a clipping context. Removed clip-path from all reveal effects (opacity + transform only); top-to-bottom open now uses `scaleY` + top origin, and the JS-measured connectors are refreshed after the animation settles.

Files changed:
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`

Verified:
- `node --check` passed; CSS depth-scan balanced; confirmed no clip-path animation remains and no TDZ on the connector-refresh reference.

Remaining:
- Not tested in a real browser/device.

### 2026-08-10 HKT — Claude — Fix card overlapping section subtitle

Summary:
- Heading and its wrapper were both being animated (the previous guard was order-dependent), so the heading translated into the next card and got painted over. Replaced with an order-independent two-phase nesting filter; nested elements now use the opacity-only inner stagger.
- Also fixed `.acc-panels` (which carries `.visual-frame` and is `display: contents` on mobile) swallowing the reveal for the galleries and both source panels.
- Reduced travel distances below the block gaps and added z-index so transitioning elements can't be covered.

Files changed:
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`

Verified:
- `node --check` passed; CSS depth-scan balanced; simulated the nesting algorithm on the real DOM — 0 kept elements nested inside another, both source panels retained.

Remaining:
- Not tested in a real browser/device.

### 2026-08-10 HKT — Claude — Heading spacing, source-panel gaps, doc-panel unfold

Summary:
- Added breathing room between section heading, intro text and the first card (`--intro-head-gap`, `--intro-title-gap`).
- Tightened 通信關係複雜/資訊流向複雜 rows: stronger negative margins so each panel hugs its card, removed panel padding, cut the top inset, and made the document fill the panel so the empty bottom band goes away.
- Doc panel now unfolds: outer frame opacity-only (its callouts are JS-positioned), `.ip-body` scales open from the header, then body text, then staggered side callouts and connector lines. Connector geometry recomputed twice after the animation settles.

Files changed:
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-cards.css`

Verified:
- `node --check` passed; CSS depth-scans balanced; all new source rules confirmed inside the mobile media query; reduced-motion covered so `.ip-body` can't stay squashed.

Remaining:
- Not tested in a real browser/device.

### 2026-08-10 HKT — Claude — Card expand effect, longer durations, gallery fixes

Summary:
- All cards now unfold downward from their top edge (`scaleY`, layout-neutral so nothing below jumps); contents fade in after the unfold. Removed a conflicting ID-prefixed rule that would have pinned sections 03/06 cards open.
- Lengthened all reveal durations (`--reveal-fade` .7s / `--reveal-move` .95s, 110ms stagger) and pushed the connector refreshes to match.
- Fixed images 2/3 info panel for real: `renderBody()` was stripping `is-expanded` after `show()` set it; the decision now lives in `renderBody()` alone.
- Removed the grey/white board behind images: the `max-height` caps made contain-fit images shrink and expose the stage background. Caps dropped and stage/image backgrounds made transparent on mobile.

Files changed:
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-cards.css`

Verified:
- `node --check` passed; CSS depth-scans balanced; `is-expanded` handled in exactly one place; no mobile stage max-height caps remain.

Remaining:
- Not tested in a real browser/device.

### 2026-08-10 HKT — Claude — Card expand reworked as a true reveal

Summary:
- Card now uncovers its text via a `clip-path` curtain from the top edge instead of `scaleY` (which squashed the text). Layout-neutral, so nothing below shifts as it replays on scroll.
- Negative left/right/bottom insets keep the card's shadow from being clipped.
- Cards no longer fade in; the staggered inner-text animation is now limited to non-card blocks so the curtain isn't sweeping over invisible text.

Files changed:
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`

Verified:
- `node --check` passed; CSS depth-scan balanced; reduced-motion still resets clip-path.

Remaining:
- Not tested in a real browser/device.

### 2026-08-10 HKT — Claude — Doc panel uses the card curtain reveal

Summary:
- `.ip-body` now reveals via `clip-path` from the header downward (text at normal size) instead of `scaleY`, matching the card effect.
- Safe because the side callouts/connectors live outside `.ip-body`; clipping the outer panel is still avoided.
- Removed the separate body-text fade so the curtain isn't sweeping over blank space; callouts keep their staggered fade.

Files changed:
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`

Verified:
- `node --check` passed; CSS depth-scan balanced; no scaleY left on `.ip-body`; reduced-motion still resets clip-path.

Remaining:
- Not tested in a real browser/device.

### 2026-08-10 HKT — Claude — Text/card reveal effects extended to Part 3

Summary:
- Reveal system now supports multiple roots with different scopes. Part 3 gets text + card effects only; the intro keeps the full set.
- Part 3 deliberately excludes visuals: its visual elements are interactive (explorers, 試一試, agentic scenes) and the mobile 史料 drawer is `position: fixed`, so a transform/clip-path on any ancestor would break its positioning.

Files changed:
- `Website/storymap/storymap.js`

Verified:
- `node --check` passed; simulated Part 3 targeting on the real DOM — 26 targets, 0 nested, 0 touching interactive widgets; intro regression check unchanged (27 targets, both source panels intact).

Remaining:
- Not tested in a real browser/device.

### 2026-08-10 15:46 HKT — Claude — Remove gallery backdrop, left-align 硃113/硃119 doc panel, widen 研究成果 visual

Summary:
- Image galleries wrapped in `.acc-panel` (difficulty-quantity, case-background, case-route, case-sources) previously showed a second frame: `.acc-panel`'s own background/border/box-shadow sat behind `.photo-gallery`'s own background/border, reading as an extra "backdrop" between the image+caption panel and the page background. Removed via `.acc-panel:has(> .photo-gallery) { background: transparent; border: 0; box-shadow: none; }`, scoped to `#intro-1-3-a`/`#intro-1-6-a-source` and mobile-only, so the two 硃113/硃119 source-flow panels (not photo galleries) are untouched. Uses `:has()`, which needs a fairly recent browser (Chrome 105+/Safari 15.4+/Firefox 121+).
- 硃113/硃119 doc panel (mobile/narrow only): panel now left-aligns (`margin-left: 0`) instead of centering inside `.source-flow-visual`. Both label groups (`.source-callouts`/`-left` and `.source-callouts-right`), previously flanking the panel on both sides, now sit side by side on the right (`right: calc(var(--intro3-callout-w) + 10px)` and `right: 0`), freeing the left edge entirely for the document. Added shared `--intro3-callout-w` var on `#intro-1-3-a` so the panel's right-side padding reservation and both label columns stay in sync. Desktop is untouched (its `.source-callouts` rule is unconditional/unscoped by breakpoint and still flanks both sides).
- 研究成果 visual (`#intro-1-5 .review-capture-frame`, mobile only): width changed from `calc(100% * var(--intro-5-visual-scale, .78))` (78% of the padded `.story-inner` column) to a viewport breakout at 97% of screen width, reusing the same `margin: calc(50% - 48.5vw)`-style technique already used by `.part3-feature-explorer`. Default var renamed from `.78` to `.97`.

Files changed:
- `Website/storymap/storymap-cards.css`

Verified:
- CSS brace-depth scan balanced on both stylesheets; `node --check storymap.js` unaffected (no JS touched).
- BeautifulSoup check against the real HTML: exactly the 4 photo-gallery-containing `.acc-panel`s (difficulty-quantity, case-background, case-route, case-sources) match `:has(> .photo-gallery)`; the two source-flow `.acc-panel`s (difficulty-relations, difficulty-network) do not.
- Confirmed `.source-callouts source-callouts-left`/`.source-callouts source-callouts-right` and `.source-flow-document` class names in the HTML match the selectors used.

Remaining:
- Not tested in a real browser/device — no way to confirm the label columns don't visually collide with each other at very narrow widths, or that connector lines (still visible in the 981–1040px non-touch sliver) redraw correctly against the new right-side label positions. The connector geometry is computed at runtime from actual element positions, so it should adapt automatically, but this needs an on-device check.
- `:has()` selector support should be confirmed against whatever browser will actually be used to present this to the teacher, if it's an older one.

### 2026-08-10 16:14 HKT — Claude — Revert 硃113/硃119 doc panel to centered + left/right labels

Summary:
- Undid the earlier left-align + right-stacked-labels layout for the mobile/narrow 硃113/硃119 doc panel, per user request to go back to the previous UI.
- `#intro-1-3-a .source-flow-document` (mobile): `margin-left` back to `auto` (centered again). Width (`min(85%, 760px)`) and `margin-bottom: 20px` were left as-is — those look like a manual tweak made directly in the file since the last session entry, not part of what was being reverted.
- Removed the mobile-only overrides on `#intro-1-3-a .source-flow-visual` padding and `#intro-1-3-a .source-callouts`/`.source-callouts-right`. With those gone, both label groups fall back to the unconditional base rule earlier in the file (left group at `left: 0`, right group at `right: 0`) — the original flanking layout.
- `--intro3-callout-w` variable is left in place (still used by the base `.source-callouts` width rule); it's just no longer referenced by the mobile block.

Files changed:
- `Website/storymap/storymap-cards.css`

Verified:
- CSS brace-depth scan balanced.

Remaining:
- Not tested in a real browser/device.

### 2026-08-10 16:45 HKT — Codex — Simplify AI Skills example response

Summary:
- Updated the `修改、建立AI Skills` example with the requested Traditional-Chinese prompt for a reusable Skill that divides each day's 起居注 OCR text into non-overlapping events and classifies them.
- Reduced the AI response to `已整理為 Skill 草稿：`, `classify-qianlong-diary-events.md`, `11 個固定分類`, and the 11 fixed category labels only; removed JSON event examples and extra output details.

Files changed:
- `Website/storymap/storymap-example.html`

Verified:
- `git diff --check` passed.
- `node --check Website/storymap/storymap.js` passed.
- In-app browser check confirmed the exact prompt, completed response, hidden thinking phase, and no JSON event item.

Remaining:
- The worktree contains unrelated concurrent StoryMap edits and four untracked handwritten-image assets; no unrelated files were staged or removed.

- This remains a visual draft example and does not execute the full 220-day classification pipeline.

### 2026-08-10 16:53 HKT — Codex — Add VS Code Skill editor behind Codex response

Summary:
- Added a VS Code-style window behind the Codex conversation in the `修改、建立AI Skills` visual.
- Put the actual `classify-qianlong-diary-events.md` Skill draft in the editor animation, including daily non-overlapping event segmentation, Traditional-Chinese fixed categories, JSON output requirements, verbatim quotations, and researcher review safeguards.
- Removed the English category identifiers from the Codex response; it now shows only the Traditional-Chinese category labels and no JSON event items.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-cards.css`

Verified:
- `git diff --check` passed.
- `node --check Website/storymap/storymap.js` passed.
- In-app browser check confirmed the VS Code window is behind Codex, both animations render, the Codex response completes, and no English type identifiers appear in the response.

Remaining:
- The worktree contains unrelated concurrent StoryMap edits and four untracked handwritten-image assets; no unrelated files were staged or removed.
- This remains a visual Skill draft example and does not execute the full 220-day classification pipeline.

### 2026-08-10 17:01 HKT — Codex — Make the VS Code Skill editor clickable and complete

Summary:
- Extended the Part 3 window interaction so the VS Code Skill editor can be clicked to move in front of Codex, while Codex remains available as the other layer.
- Expanded the editor animation to show the complete `classify-qianlong-diary-events.md` draft: task, input, segmentation rules, fixed Traditional-Chinese categories, JSON output requirements, verbatim evidence, uncertainty handling, and researcher review.
- Refreshed the StoryMap JavaScript version query so the new click behavior is loaded in the browser.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-cards.css`

Verified:
- `git diff --check` passed.
- `node --check Website/storymap/storymap.js` passed.
- In-app browser check confirmed clicking the visible VS Code title bar raises it to the front and the complete Skill text renders.

Remaining:
- The worktree contains unrelated concurrent StoryMap edits and four untracked handwritten-image assets; no unrelated files were staged or removed.
- This remains a visual Skill draft example and does not execute the full 220-day classification pipeline.

### 2026-08-10 17:10 HKT — Codex — Restore staged Codex and VS Code animation

Summary:
- Restored the Part 3 AI Skills sequence: typed Codex prompt, Codex thinking, VS Code Skill typing, then typed Codex output.
- Removed the green background from the AI Skills scene by making its scene background transparent.
- Added clearly grouped manual size, position, title-font, and content-font variables for both windows in base, narrow, and mobile sections of `storymap-cards.css`.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap-cards.css`

Verified:
- `git diff --check` passed.
- `node --check Website/storymap/storymap.js` passed.
- In-app browser timing check confirmed the four stages occur in order, Codex output appears after the full VS Code text, the scene background is transparent, and clicking VS Code raises it to the front.

Remaining:
- The worktree contains unrelated concurrent StoryMap edits and four untracked handwritten-image assets; no unrelated files were staged or removed.
- This remains a visual Skill draft example and does not execute the full 220-day classification pipeline.

### 2026-08-10 17:21 HKT — Codex — Increase AI Skills visual frame height

Summary:
- Increased the `修改、建立AI Skills` visual frame height through its existing responsive `--part3-ai-skills-frame-height` variables.
- Updated desktop, narrow, and mobile values so the taller frame remains manually adjustable per mode.

Files changed:
- `Website/storymap/storymap-cards.css`

Verified:
- `git diff --check` passed.
- `node --check Website/storymap/storymap.js` passed.
- Browser geometry check confirmed the desktop frame now renders at 680px height.

Remaining:
- The worktree contains unrelated concurrent StoryMap edits and four untracked handwritten-image assets; no unrelated files were staged or removed.

### 2026-08-10 17:29 HKT — Codex — Play AI Skills animation once per reload

Summary:
- Changed the `修改、建立AI Skills` animation controller to run once per page reload instead of restarting whenever the section re-enters the viewport.
- The prompt, thinking, VS Code Skill typing, and Codex output sequence now keeps its one-shot state while scrolling away and back.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`

Verified:
- `git diff --check` passed.
- `node --check Website/storymap/storymap.js` passed.
- Browser check confirmed the one-shot flag remains set after scrolling away and returning to the section.

Remaining:
- The worktree contains unrelated concurrent StoryMap edits and four untracked handwritten-image assets; no unrelated files were staged or removed.

### 2026-08-10 17:34 HKT — Codex — Add numbered Skill instruction card

Summary:
- Added the `2` number box to `建立新的 Skill 時，研究者應說明：`.
- Replaced the card copy with the requested question-led instructions and retained the small-document testing step before batch processing.

Files changed:
- `Website/storymap/storymap-example.html`

Verified:
- `node --check Website/storymap/storymap.js` passed.
- Confirmed the card renders the number box and exact revised Traditional-Chinese content.

Remaining:
- The worktree contains unrelated concurrent StoryMap edits and four untracked handwritten-image assets; no unrelated files were staged or removed.

### 2026-08-10 17:56 HKT — Codex — Rename AI API and AI Chain execution cards

Summary:
- Renamed the first AI execution card to `使用AI Api 執行Skills`.
- Turned the repeated-operation explanation into a numbered card titled `使用AI Chain 執行Skills`.

Files changed:
- `Website/storymap/storymap-example.html`

Verified:
- `git diff --check` passed.
- `node --check Website/storymap/storymap.js` passed.
- Confirmed both cards render their requested titles and number boxes.

Remaining:
- The worktree contains unrelated concurrent StoryMap edits and four untracked handwritten-image assets; no unrelated files were staged or removed.

### 2026-08-10 17:58 HKT — Codex — Correct AI extraction card numbering

Summary:
- Corrected the visible number boxes under `運用AI抽取資訊` to one sequence: Skills 1–2, API 3, Chain 4, Model 5, and Google Cloud 6.

Files changed:
- `Website/storymap/storymap-example.html`

Verified:
- `git diff --check` passed.
- `node --check Website/storymap/storymap.js` passed.
- Confirmed the six AI extraction cards render the corrected number boxes.

Remaining:
- The worktree contains unrelated concurrent StoryMap edits and four untracked handwritten-image assets; no unrelated files were staged or removed.

### 2026-08-10 18:25 HKT — Codex — Replace AI model card with full-width format section

Summary:
- Removed the `5 選用的AI Model` section, including its explanatory paragraphs, comparison table, mobile interaction code, and unused styling.
- Kept `6 檢視史料的版面及格式` as the full-width, no-card section already present in Part 3.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap.js`

Verified:
- `git diff --check` passed.
- `node --check Website/storymap/storymap.js` passed.
- Targeted browser check confirmed no `#part-3-model` section remains and the `6 檢視史料的版面及格式` block is no-card and spans the full story width.

Remaining:
- The worktree contains unrelated concurrent StoryMap edits, a modified UI Idea draft, and four untracked handwritten-image assets; no unrelated files were staged or removed.

### 2026-08-10 18:27 HKT — Claude — Add circular AI Chain visual to #part-3-ai-chain

Summary:
- Replaced the horizontal six-node `.workflow-chain` bar (`#part-3-ai-chain-chart`, `data-part3-chart-toggle="chain-1".."chain-6"`) with a new circular AI Chain visual placed beside the two existing text cards (`使用AI Api 執行Skills` / `使用AI Chain 執行Skills`, kept exactly as Codex last renamed/renumbered them in this same worktree — this change does not touch their text or option numbers).
- New visual: seven round step cards (renamed per prior user instruction: 文書總結 → 抽取事件 → 抽取官員行動 → 追溯資訊來源 → 抽取皇帝回應 → 抽取官員後續回應 → 輸出JSON) arranged on an arc, each filling via a conic-gradient progress ring in sequence; step 7 deliberately has no connecting arc back to step 1 (gap stays visible). Background is a Matrix-style falling-text canvas using verbatim characters from `doc_id: 硃25`'s `body` field in `review-tools/shared data/stage1_original_text.json` (黃仕簡, 為奏彰化失陷已調兵赴臺事 — directly about the 林爽文事件), not random glyphs; original paragraph breaks were collapsed into single full-width spaces to form one continuous character stream, no wording altered.
- Layout: new `#part-3-ai-chain .part3-chain-ring-layout` grid (left column stacks the two existing text cards via `.part3-chain-ring-copy`, right column is the new `.part3-chain-ring-visual`), mirroring the existing `#part-3-ai-skills .part3-ai-skills-layout` left-copy/right-visual pattern, including the same 1040px collapse-to-one-column breakpoint.
- New JS: `initPart3ChainRing()` in `storymap.js`, following the existing `initOcrScanScene`/`initGifAnnotations` conventions (`[data-part3-chain-ring]` container query, `IntersectionObserver` gated start/stop, `ResizeObserver`-driven canvas sizing, `prefers-reduced-motion` static fallback). The now-generic `initPart3OriginalCharts()` toggle handler is untouched and simply matches zero elements for this section now (it still serves `#part-3-basic-flow-chart`, unaffected).
- Bumped cache-busting query strings for the two files actually changed: `storymap-cards.css?v=20260810-claude-chain-ring-01`, `storymap.js?v=20260810-claude-chain-ring-01`. `storymap.css` was not modified, so its query string is untouched.
- This is an adaptation of the previously drafted `UI Idea/28-ai-chain-circle-scan-animation-draft.html`, developed interactively over several rounds with the user, now wired into the live section instead of the standalone draft.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap.js`

Verified:
- `node --check Website/storymap/storymap.js` passed.
- Python-based structural checks: balanced `<div>`/`<section>` tags, balanced CSS braces in both stylesheets, exactly 7 `.part3-chain-ring-node` and 6 `.part3-chain-ring-link` elements, no leftover `part3-chain-frame` / `part-3-ai-chain-chart` references, no duplicate `id` introduced by this change (four pre-existing duplicate ids elsewhere — `case-route`, `case-background`, `case-sources`, `difficulty-quantity` — are unrelated to this edit and were not touched).
- Re-read the live HTML/CSS immediately before each edit to check for concurrent Codex changes to the same lines; none occurred between read and write this time.

Remaining:
- Not tested in a real browser/device — no headless browser was available in this session to screenshot the result. Please check rendering, the matrix-rain performance, and mobile/narrow layout on an actual device before treating this as final.
- The worktree still contains unrelated concurrent StoryMap edits from the other active session; only the three files above were staged by this change.
- Open questions carried over from the draft: whether the matrix-rain source text should rotate across multiple documents instead of only 硃25, and whether the circular visual's timing (1.1s/step, 55ms per rain glyph refresh) needs tuning once seen live.

### 2026-08-10 18:35 HKT — Claude — Drop backdrop and captions on the AI Chain ring; expose sizing variables

Summary:
- Removed the `例如，研究者可以建立一條處理奏摺的 AI Chain：` lead line and the `7 → 1 不相連` gap caption from the circular AI Chain visual; the visual now has no on-canvas text besides the seven step names and the completion badge.
- Removed the solid `background: var(--ink)` "card" behind the whole visual — it now sits directly on the section's own background with just a thin `--line`-toned border, no fill, no drop-shadow.
- Rewrote the Matrix-rain canvas logic in `initPart3ChainRing()` (`storymap.js`): the old approach painted an opaque dark fill on init plus a semi-transparent `fillRect` every frame, which (regardless of the container's own background) built up into a solid dark-green backdrop inside the canvas itself as frames accumulated. Replaced with a `globalCompositeOperation = 'destination-out'` erase pass each frame (fades old glyphs by reducing alpha instead of painting over them), so the canvas never accumulates a solid fill and starts fully transparent (`clearRect`, no initial `fillRect`).
- Because the backdrop is gone, the rain glyphs and idle link strokes (previously light cream, tuned for a dark backdrop) were invisible against the section's light paper background. Switched idle glyphs/leader glyphs to darker saturated greens and idle link strokes to a dark ink tone; active-link glow switched from a yellow-on-yellow shadow to an accent-orange glow for better separation.
- Exposed `--part3-chain-ring-max-width` / `--part3-chain-ring-margin` as overridable custom properties on `#part-3-ai-chain .part3-chain-ring-visual`, with distinct override points at desktop (base rule), ≤1040px, and ≤620px — mirroring the `--agentic-vscode-*` manual-tuning pattern already used under `#part-3-ai-skills`. Desktop overall width is still controlled by the existing `--part3-chain-ring-visual-width` (% of the grid row) in the `#part-3-ai-chain` root block. These four variables are the intended hooks for manually repositioning/resizing the visual per breakpoint going forward.
- Bumped `storymap-cards.css`/`storymap.js` cache-busting queries to `...-claude-chain-ring-02`.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap.js`

Verified:
- `node --check Website/storymap/storymap.js` passed.
- Balanced HTML tags, balanced CSS braces; no leftover `chain-ring-gap-note` / `chain-ring-lead` references in either file; still exactly 7 step nodes and 6 arcs.

Remaining:
- Still not tested in a real browser/device this session — the destination-out fade technique and the new glyph colors should be checked visually, especially glyph legibility against the actual `.surface-b` paper tone at small sizes.
- The four new sizing/position variables are only wired for the three documented breakpoints; no UI control exists yet for adjusting them, they're meant to be edited directly in `storymap-cards.css`.

### 2026-08-10 18:45 HKT — Claude — Restore the AI Chain ring's dark card backdrop

Summary:
- User asked to bring the backdrop back after the previous change removed it. Restored `background: var(--ink)`, the border alpha, and the drop-shadow on `#part-3-ai-chain .part3-chain-ring-visual`.
- Restored the original light-on-dark colors that pair with a dark card: rain glyphs back to the bright greens (`rgba(214,255,230,.42)` / `rgba(58,209,138,.3)`), idle link stroke back to light cream (`rgba(247,243,234,.22)`), active-link glow back to the yellow-tinted shadow (`rgba(243,201,103,.55)`).
- Kept the `destination-out` alpha-erase fix from the previous change (it prevents the canvas from self-accumulating an extra dark tint over time regardless of whether the card behind it is dark or transparent) — only the color values and the card's own background/border/shadow were reverted, not the fade technique itself.
- Bumped cache-busting queries to `...-claude-chain-ring-03`.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap.js`

Verified:
- `node --check Website/storymap/storymap.js` passed; CSS brace balance checked.

Remaining:
- Still not tested in a real browser/device this session.

### 2026-08-11 14:03 HKT — Codex — Let Google Cloud text card fit its content

Summary:
- Updated the Google Cloud layout so the text card no longer stretches to the gallery's width or height.
- Kept the gallery at its independent visual height and allowed the card to shrink-wrap its text at desktop and narrow widths.

Files changed:
- `Website/storymap/storymap-cards.css`

Verified:
- `git diff --check` passed.
- `node --check Website/storymap/storymap.js` passed.
- Browser geometry confirmed independent sizing at 1280px and 390px viewports.

Remaining:
- The worktree contains unrelated concurrent StoryMap edits and a modified AI Chain UI draft; no unrelated files were staged or removed.

### 2026-08-11 14:12 HKT — Codex — Consolidate the LLM Wiki text cards

Summary:
- Combined the former second and third LLM Wiki cards into one research card.
- Added number-box titles to the two remaining cards: `LLM Wiki` and `LLM Wiki 與歷史研究`.
- Updated the matching StoryMap CSS selectors and removed the unused third-card styling.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check intro Website/Website/storymap/storymap.js` passed.
- `git diff --check` passed; no stale `part-3-wiki-analysis` references remain in the live StoryMap files.
- Browser check at 1280×720 showed both numbered cards with the requested titles; a 390×844 DOM check confirmed both cards fit the narrow width and the combined card contains both paragraphs.
- No browser console errors or warnings were reported.

Remaining:
- The narrow live screenshot remains affected by the pre-existing mobile scroll-reveal state, which was left outside this content-only change.
- Existing concurrent StoryMap edits and untracked handwritten-image assets remain untouched; no push was performed.

### 2026-08-11 14:27 HKT — Codex — Fix initial Try a Try PDF rendering

Summary:
- Changed the shared Try a Try PDF image from lazy to eager loading.
- Set eager loading again during initialization so the fit-content desktop page stack receives intrinsic image dimensions before the first render.
- Bumped the StoryMap script query string so browsers load the fix.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check intro Website/Website/storymap/storymap.js` passed.
- `git diff --check` passed.
- Browser reproduction showed printed mode page 1 loading immediately at 297px wide instead of collapsing to 2px; handwritten mode showed two initial fold panels with image backgrounds and a 588px-wide stack.
- No browser console errors or warnings were reported.

Remaining:
- Existing unrelated concurrent StoryMap edits, UI drafts, and handwritten-image assets remain untouched; no push was performed.

### 2026-08-11 14:40 HKT — Codex — Split the final handwritten Try a Try spread

Summary:
- Replaced the final desktop handwritten composite page with two normal two-fold pages: `3b3a.png`, followed by `empty3c.png` with a blank left half and 3c on the right.
- Removed the special final-page blank-fold logic and updated the handwritten desktop page count to five.
- Moved the `水印` feature mapping to the new final page while preserving the original combined scan asset.

Files changed:
- `Website/storymap/試一試/手寫字/3b3a.png`
- `Website/storymap/試一試/手寫字/empty3c.png`
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Both derived PNGs are exact 3106×3423 RGB composites; `3b3a.png` matches the source middle+right crop, and `empty3c.png` preserves the source 3c crop on its right half.
- `node --check intro Website/Website/storymap/storymap.js` passed.
- `git diff --check` passed.
- Browser check showed `頁 4 / 5` using `3b3a.png` with two open folds, then `頁 5 / 5` using `empty3c.png` with the blank-left／3c-right layout; no browser errors or warnings were reported.

Remaining:
- The original `3c3b3a.png` remains preserved but is no longer used by the Try a Try desktop page list.
- Existing unrelated concurrent StoryMap edits and UI assets remain untouched; no push was performed.

### 2026-08-11 15:06 HKT — Claude — Merge LLM Wiki cards and add knowledge-network visual

Summary:
- Merged `#part-3-wiki-intro` and `#part-3-wiki-data` into one `#part-3-wiki-data` section: two text cards left, new right-side "LLM Wiki 知識網絡" visual (chat-bubble question → one-shot Obsidian-style graph "thinking" animation → typed AI answer with citations), mirroring the `#part-3-ai-chain` left-copy/right-visual pattern.
- Added `initPart3WikiVisual()` to `storymap.js` and matching scoped CSS to `storymap-cards.css` (incl. 1040px/620px breakpoints), ported from `UI Idea/29-llm-wiki-network-animation-draft.html`.
- Simplified the AI-answer text per user direction: dropped the quoted 硃批 line and the inline 諭13/硃25 uncertainty caveat (kept in the draft's note-list/source-note instead), shortened the 吳正龍 2018 citation, renamed the "皇帝及後續官員的回應" label to "皇帝的回應" (and the sample question to match), added spacing between the answer's three parts.
- Updated the draft file to match (visual now right of the combined cards) and bumped cache-busting versions to `...-claude-wiki-visual-01`.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap.js`
- `Website/UI Idea/29-llm-wiki-network-animation-draft.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check` passed on `storymap.js` and the draft's extracted script.
- Tag/brace balance checks passed on `storymap-example.html`, `storymap-cards.css`, and the draft file; no dangling references to the removed `#part-3-wiki-intro` id.

Remaining:
- Browser/device visual QA still needed (no headless browser available in this sandbox).

### 2026-08-11 15:07 HKT — Codex — Center the Try a Try handwritten PDF spread

Summary:
- Centered the visible handwritten Try a Try fold pair instead of right-aligning the `row-reverse` strip.
- Removed inactive-page fold panels from the desktop layout while retaining the current page's fold state, preventing page-dependent horizontal shifts and right-edge clipping.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap.js`

Verified:
- Browser geometry at the desktop viewer width showed the open pair centered exactly on `頁 1 / 5`, `頁 4 / 5`, and `頁 5 / 5`; page 4 loaded `3b3a.png` and page 5 loaded `empty3c.png`.
- No browser console errors or warnings were reported.
- `node --check intro Website/Website/storymap/storymap.js` and `git diff --check` passed.

Remaining:
- Existing concurrent LLM Wiki edits, cache-busting values, UI draft, and handwritten assets were preserved; no commit or push was made.

### 2026-08-11 15:42 HKT — Codex — Refine OCR, Google Cloud, and LLM Wiki visuals

Summary:
- Reduced the OCR test visual's `1頁` and `50頁` labels to 22px.
- Made the Google Cloud gallery stage follow the active image's natural aspect ratio so the image has no extra top or bottom spacing.
- Replaced the visible `諭13` label in the LLM Wiki answer with the full 上諭 title; source-note provenance in the UI draft still retains the source ID where needed.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap.js`
- `Website/UI Idea/29-llm-wiki-network-animation-draft.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser preview with cache-busting loaded the current StoryMap files: OCR labels computed to 22px; Google Cloud rendered at the image's natural ratio with 0px top and bottom gap; the LLM Wiki answer contained the full 上諭 title and no `諭13`.
- `node --check Website/storymap/storymap.js` and `git diff --check` passed.

Remaining:
- No commit or push was made; the updated files remain in the working tree for review.

### 2026-08-11 17:10 HKT — Codex — Split 平台介面 into five topic sections with focused visuals

Summary:
- Replaced the single Part 1 replica plus five-card accordion with five independent topic sections: 導覽列、時間與關係圖表、節點資訊區、原始史料區、人工智能分析區.
- Added a dark topic bar for each interface area, matching the internal `步驟二` stage-bar treatment used in the final tab.
- Put the explanatory text below each bar; the four multi-paragraph topics remain text cards, while the single-paragraph 節點資訊區 is plain text.
- Reused the source-backed 硃42 demonstration data in five independently initialized replicas, each focused on its own interface area and displayed at full visual width.
- Added the node-area default panel state and responsive toolbar wrapping so the new section layout remains contained on narrow screens.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/part-1-interface.js`
- `Website/storymap/part-1-interface.css`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check Website/storymap/part-1-interface.js` and `node --check Website/storymap/storymap.js` passed.
- `git diff --check` passed.
- Browser checks at 1280×900 and 390×844 confirmed five topic bars, four text cards plus one plain-text section, centered full-width visual frames, no narrow-screen horizontal overflow, a visible default node panel, chart-node interaction, source filtering, and AI result loading.
- Browser console returned no error or warning entries.

Remaining:
- Create the local Git checkpoint; do not push automatically.

### 2026-08-11 16:23 HKT — Codex — Refine LLM Wiki response wording

Summary:
- Replaced `起居注於十二月二十七日收悉，同日並以上諭` with `於十二月二十七日收悉，同日以上諭` in the live LLM Wiki visual and its UI draft.

Files changed:
- `Website/storymap/storymap.js`
- `Website/UI Idea/29-llm-wiki-network-animation-draft.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Rendered LLM Wiki response contained the new wording and no longer contained the old wording.
- `node --check Website/storymap/storymap.js`, `git diff --check`, and focused source search passed.

Remaining:
- No commit or push was made; concurrent working-tree edits were preserved.

### 2026-08-11 16:09 HKT — Codex — Refine basic-flow and PaddleOCR result visibility

Summary:
- Reduced the basic-flow visual's step numbers to 16px and reduced the number-to-title gap to 8px in both desktop and narrow layouts.
- Reset the PaddleOCR Agentic AI result phase to the top of its scroll container so `Worked for 5m 44s` is followed immediately by the first output sentence.
- Bumped the StoryMap asset query versions for the new CSS and JavaScript.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap.js`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser checks at 390px and 1280px computed the flow number as 16px, its gap as 8px, and the label beginning 8px after the number box.
- PaddleOCR result phase showed `Worked for 5m 44s` at the top and the first sentence immediately below it, with the result body at scroll position 0.
- No browser console logs were reported.
- `node --check Website/storymap/storymap.js` and `git diff --check` passed.

Remaining:
- Concurrent LLM Wiki and related working-tree edits were preserved; no additional commit or push was made.

### 2026-08-11 15:56 HKT — Codex — Refine Part 3 responsive OCR and source panels

Summary:
- Reduced the number in the `8` card square in both desktop and narrow layouts.
- Kept each Part 3 `步驟 X` label aligned with the stage title below it by removing the narrow-layout heading offset.
- Slowed the OCR reason visual's JSON typing and made Agentic AI PaddleOCR output follow the nearest scrollable window as new text appears.
- Fixed the expanded 7／8 source drawers so printed pages retain their full visible height and handwritten folds retain a usable height instead of collapsing to a few pixels.
- Bumped the StoryMap asset query versions so the current CSS and JavaScript are loaded after the responsive fixes.

Files changed:
- `Website/storymap/storymap.js`
- `Website/storymap/storymap.css`
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser checks at 390px and 1280px showed the step-label/title x-coordinate delta at 0; the `8` number computed to 13px on narrow layout and 17.28px on desktop.
- Expanded 7 showed the complete current source image without transform or max-height clipping; expanded 8 showed a 319px-tall fold with both open panels visible. OCR output advanced at the slower timing, and the PaddleOCR body followed its maximum scroll position while text was loading.
- No browser console logs were reported.
- `node --check Website/storymap/storymap.js` and `git diff --check` passed.

Remaining:
- Concurrent LLM Wiki and related working-tree edits were preserved; no additional commit or push was made.

### 2026-08-11 16:03 HKT — Codex — Enlarge LLM Wiki node labels and use 起居注 terminology

Summary:
- Enlarged the LLM Wiki network node labels to 13px on desktop and 11px on narrow screens.
- Renamed the network node and visible answer references from `硃25` to `起居注`.
- Kept the full 上諭 title in the answer.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap.js`
- `Website/UI Idea/29-llm-wiki-network-animation-draft.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser preview showed all LLM Wiki node labels at 13px, the node label `起居注`, and no `硃25` in the network or answer text.
- `node --check Website/storymap/storymap.js` and `git diff --check` passed.

Remaining:
- No commit or push was made; the updated files remain in the working tree for review.

### 2026-08-11 16:13 HKT — Codex — Combine the Skill prompt and AI output scroll area

Summary:
- Updated the `Codex — Create Skill` window in the second AI Skills visual mode so the researcher prompt and AI thinking/result output share one scrollable content area.
- Kept the Codex title bar fixed while the combined prompt/output area follows newly typed content to the bottom.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser preview confirmed the prompt row and AI phase body share `.agentic-codex-scroll`; the shared container is vertically scrollable and the body no longer owns a separate scrollbar.
- `node --check Website/storymap/storymap.js` and `git diff --check` passed.

Remaining:
- No commit or push was made; the updated files remain in the working tree for review.

### 2026-08-11 16:25 HKT — Codex — Enlarge and contain the phone AI Skills visual

Summary:
- Increased the phone-specific height of the「建立新的 Skill」visual.
- Repositioned and resized the VS Code and Codex windows so both remain fully inside the mobile frame instead of being clipped at the right or bottom edges.

Files changed:
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser geometry at 390px showed both windows fully contained within the frame: left, right, top, and bottom clipping checks all passed.
- `node --check Website/storymap/storymap.js` and `git diff --check` passed.

Remaining:
- No commit or push was made; the updated files remain in the working tree for review.

### 2026-08-11 17:30 HKT — Codex — Exported the platform interface replica to a standalone HTML page

Summary:
- Added one standalone page containing the five interactive replicas shown in the `平台介面` tab: 導覽列、時間與關係圖表、節點資訊區、原始史料區 and 人工智能分析區.
- Reused the existing canonical Part 1 data, styling, and interaction modules so the new page remains tied to the reviewed 硃42 demonstration.

Files changed:
- `Website/storymap/platform-interface-replica.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`

Verified:
- Inspected the live `平台介面` tab before extracting the replica.
- Confirmed all five mode roots render on the new page, with no browser console errors.
- Browser-tested chart node opening, AI Skill source highlighting, AI result loading, and adding a candidate to the chart.
- `node --check` and `git diff --check` passed.

Remaining:
- The new HTML intentionally references the adjacent Part 1 CSS, data, and behavior files; keep those files together when moving or publishing the page.
- Existing unrelated working-tree changes were preserved; no push was made.

### 2026-08-11 17:34 HKT — Codex — Restructure 平台運作流程 into topic bars and paragraph cards

Summary:
- Replaced the old centered Part 2 story-card layout with topic bars for 運作流程圖, 輸入結構化資料, 使用AI從原文中抽取資訊, the four analysis stages, and 視覺化呈現分析的結果.
- Moved numbered topics into option-number boxes and split every paragraph from 輸入結構化資料 onward into its own left-aligned text card.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser preview at 1280px showed eight full-width topic bars, all Part 2 cards sharing the same left edge, and no remaining old story-card or cover-bar markup.
- Confirmed 40 cards from 輸入結構化資料 onward each contain exactly one paragraph; no horizontal overflow or browser console logs were reported.
- `git diff --check` passed.

Remaining:
- Local checkpoint `f693b35` created; unrelated concurrent working-tree edits remain unstaged and nothing was pushed.

### 2026-08-11 17:44 HKT — Codex — Turned 運作流程圖 into the second numbered Part 2 text card

Summary:
- Kept `平台的運作流程` as numbered card 1 and changed `運作流程圖` into a separate numbered card 2.
- Removed the flow section's topic-bar heading while preserving the clickable flow diagram and its existing links to the detailed Part 2 sections.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`

Verified:
- Browser preview showed card 1 `平台的運作流程` and card 2 `運作流程圖` as separate text cards.
- Confirmed the flow diagram remains present beneath card 2 and the former `流程概覽` topic bar is gone.
- `node --check Website/storymap/storymap.js` and `git diff --check` passed; no browser console errors were reported.

Remaining:
- Existing concurrent Part 2 flowchart and project-log edits were preserved; nothing was pushed.

### 2026-08-11 17:48 HKT — Codex — Moved the input-result paragraph into the first input card

Summary:
- Moved `輸入後，網站會讀取這些欄位，並根據文書的收發日期，在時間與關係圖表上建立各份文書的節點；同時，文書區亦會顯示文書的基本資料及完整原文。` into the `在選定研究主題及所使用的奏摺與上諭後` card.
- Placed it immediately after the parenthetical ending `「重用平台於其他研究主題」中再作介紹。）` and rendered it in bold.
- Removed the now-redundant standalone paragraph card.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`

Verified:
- The input section now contains three cards; the first contains one `<strong>` element with the requested sentence and the sentence appears only once.
- Browser computed the moved text at font weight 700 with no console errors.
- `node --check Website/storymap/storymap.js` and `git diff --check` passed.

Remaining:
- Existing concurrent Part 2 and project-log edits were preserved; nothing was pushed.

### 2026-08-11 18:38 HKT — Codex — Shortened Part 2 flow labels and stacked mobile AI bubbles

Summary:
- Shortened the Part 2 flow visual labels to `選定題目與史料`, `OCR 並結構化史料`, `輸入結構化史料`, `使用AI抽取資訊`, and `視覺化分析的結果`.
- Changed the mobile AI Skills group from a 2×2 grid to a single vertical stack so 分析階段一 appears above 分析階段二, matching the desktop flow.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`

Verified:
- Browser preview checked the shortened labels at 1280px and 390px widths.
- Mobile computed positions confirmed 分析階段一 is above 分析階段二; no browser console warnings or errors were reported.
- `git diff --check` passed.

Remaining:
- Existing unrelated Part 1 and sample-data edits were preserved; nothing was pushed.

### 2026-08-11 18:03 HKT — Codex — Unboxed Part 2.2 flow-chart introduction

Summary:
- Changed `運作流程圖` in Part 2.2 to use the full-width, no-card text treatment used by Part 3’s `檢視史料的版面及格式`.
- Removed `點擊任一節點，可跳至該階段的詳細說明。` while keeping the numbered title and existing flow-chart navigation.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`

Verified:
- Focused source inspection confirmed the introduction is outside the card class and the removed sentence no longer appears.
- `git diff --check` passed.

Remaining:
- Existing concurrent Part 2 flow-chart changes were preserved; browser preview was not run in this checkpoint and nothing was pushed.

### 2026-08-11 17:57 HKT — Codex — Combined the standalone platform-interface replica

Summary:
- Reworked `Website/storymap/platform-interface-replica.html` from five separate mode-specific sections into one combined full-interface replica based on the previous combined implementation.
- Kept the navigation bar, time-and-relationship chart, original-document area, AI analysis area, and chart-opened node-information panel together in the same interactive surface.

Files changed:
- `Website/storymap/platform-interface-replica.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`

Verified:
- Browser preview rendered one replica root in `all` mode with four interface regions, four chart nodes, and document/AI/node panels.
- Clicking a chart node opened the node-information panel; no browser console errors were reported.
- `node --check Website/storymap/part-1-interface.js` and `git diff --check` passed.

Remaining:
- Existing concurrent Part 2 and project-log edits were preserved; nothing was pushed.

### 2026-08-11 18:45 HKT — Codex — Restored mobile AI grid and stacked normal-screen preparation steps

Summary:
- Restored the previous mobile 2×2 layout for the four AI Skills bubbles.
- Added a normal-screen vertical group so 步驟一 `選定題目與史料` sits above 步驟二 `OCR 並結構化史料`, with the same stacked-bubble treatment used for the analysis stages.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`

Verified:
- Browser preview at 1280px confirmed 步驟一 is above 步驟二 and the AI bubbles remain vertically stacked on normal screens.
- Browser preview at 390px confirmed the four AI bubbles use the restored 2×2 grid; no browser console warnings or errors were reported.
- `git diff --check` passed.

Remaining:
- Existing concurrent Part 1, sample-data, and StoryMap edits were preserved; nothing was pushed.

### 2026-08-11 19:32 HKT — Codex — Rebuilt replica chart geometry from one SVG data model

Summary:
- Replaced separately CSS-positioned replica dots and SVG lines with a shared JavaScript-rendered SVG chart.
- Added a compact `chartPreview` projection sourced from the sample review state, including lane ratios, nodes, dates, and links; SVG coordinates now follow the sample tool's shared lane-X/date-Y pattern.
- Kept chart-dot keyboard/click activation, AI output cards, candidate insertion, reset, and responsive redraw behavior.

Files changed:
- `tool/scripts py/build_part1_interface_data.py`
- `Website/storymap/part-1-interface-data.js`
- `Website/storymap/part-1-interface.js`
- `Website/storymap/part-1-interface.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser comparison checked the replica against `http://127.0.0.1:8166/sample`; the replica rendered four SVG dots and three links, and every link endpoint matched its corresponding dot coordinate exactly.
- Clicking the event SVG dot opened the expected AI output card; both pages reported no warning or error logs.
- Parsed `/Users/creamybanana/Downloads/sample_all.data`: all 25 events had usable `dateAr` values, and representative records normalized to the renderer's `{id, lane, actor, dateAr}` node shape.
- `node --check Website/storymap/part-1-interface.js` and `git diff --check` passed.

Remaining:
- Direct `file://` navigation was blocked by the in-app browser security policy; verification used the equivalent local HTTP preview at port 8765. No push was performed.

### 2026-08-11 19:12 HKT — Codex — Rewrote and widened the Part 2 input introduction

Summary:
- Replaced the old OCR/input paragraph under `#part-2-input` with the requested explanation, including the reference to `OCR 並結構化原始史料（with embedded website）`.
- Moved that paragraph out of the text-card treatment and made it span the full StoryMap content width; kept the two later explanatory paragraphs as cards.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `git diff --check` passed.
- In the local HTTP StoryMap at `#part-2`, the new block renders at the full content width with transparent background, no border, and no padding; the two remaining cards retain their original treatment.
- Narrow viewport check at 390px also passed without horizontal overflow.
- The page-wide browser console still reports the pre-existing `nodePanel is not defined` error from concurrent `part-1-interface.js` work; no Part 2-specific browser error was observed.

Remaining:
- Preserve the unrelated concurrent edits; no deployment or push was performed.

### 2026-08-11 18:51 HKT — Codex — Match the replica tools menu and event-chain panel to the sample

Summary:
- Replaced the replica's compact gear popover with the sample-style settings menu containing 資料, 字級, 連線, and 時間軸 sections, including the 匯入 control, exact 介面字級／正文 labels, and live slider readouts.
- Changed the replica's 事件鏈 shortcut from a chart highlight to a full-width scrollable event-chain panel with source, reported-event, and imperial-action cards, collapsible details, arrows, and matching controls.
- Bumped the shared Part 1 asset query version so both the standalone replica and StoryMap load this adjustment.

Files changed:
- `Website/storymap/part-1-interface.js`
- `Website/storymap/part-1-interface.css`
- `Website/storymap/platform-interface-replica.html`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Inspected the live `/sample` toolbar menu and populated 事件鏈 panel in the in-app browser as the visual reference.
- `node --check "intro Website/Website/storymap/part-1-interface.js"` passed.
- `git diff --check` passed.
- Source checks confirmed the full settings sections, event-chain trigger/body, and cache-busted assets are present.
- The replica itself could not be loaded in the current browser session because the requested `file://` page and the separate local 8765 navigation were blocked by browser URL policy; no replica visual pass is claimed.

Remaining:
- Open the replica once in a browser that permits the local page and visually confirm the two states at the target viewport.
- Existing concurrent Part 1, StoryMap, sample-data, and project-log edits were preserved; nothing was pushed.

### 2026-08-11 18:52 HKT — Codex — Matched AI chat overlays in the platform replica

Summary:
- Added the replica's conversation menu with the two supplied review-run entries and metadata.
- Added the sample-style 功能 menu with grouped actions and separators.
- Added the AI settings overlay with provider, model, API Base, API Key, memory, proxy URL, and a working key-visibility control.
- Positioned all three overlays at the viewport level so the 功能 list is not clipped by the dock.

Files changed:
- `Website/storymap/part-1-interface.js`
- `Website/storymap/part-1-interface.css`

Verified:
- Compared against `http://127.0.0.1:8766/sample` in the in-app browser.
- Opened and visually checked the conversation menu, 功能 menu, and 設定 overlay in the local HTTP replica preview.
- Confirmed the settings eye control changes the API key input type and the 林方事件 action still loads three candidate cards.
- `node --check` and `git diff --check` passed; the replica browser console reported no warnings or errors.

Remaining:
- The browser session did not provide a separate narrow viewport override for an additional 516px visual pass; no deployment or push was performed.

### 2026-08-11 19:00 HKT — Codex — Matched the replica four-line chart to the sample network

Summary:
- Replaced the replica's four decorative chart lines with a source-backed vertical timeline preview using the current sample event state and canonical Stage 1 document records.
- Added aligned 戰場事件／官員上奏／皇帝硃批下旨／皇帝行動 lanes, date grid lines, document circles, event squares, emperor-action squares, and relationship links while preserving the four interactive teaching nodes.
- Regenerated the preview data and bumped the local asset versions so the standalone replica and StoryMap load the current chart implementation.

Files changed:
- `tool/scripts py/build_part1_interface_data.py`
- `Website/storymap/part-1-interface-data.js`
- `Website/storymap/part-1-interface.js`
- `Website/storymap/part-1-interface.css`
- `Website/storymap/platform-interface-replica.html`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser preview at the local HTTP-served replica rendered four axes, 318 document circles, 210 event squares, and 316 relationship lines; the chart visually matches the sample's dense lane layout.
- `node --check Website/storymap/part-1-interface.js`, `node --check Website/storymap/storymap.js`, and `git diff --check` passed.
- The browser blocks direct `file://` navigation, so the same replica file was verified through the local HTTP preview; no browser warnings or errors were reported.

Remaining:
- Existing concurrent work was preserved; nothing was pushed.

### 2026-08-12 13:05 HKT — Codex — Renumbered and wired the Part 2 flow chart

Summary:
- Renumbered the Part 2 flow chart's structured-input and AI-extraction nodes from steps 4/5 to steps 3/4.
- Updated the matching Part 2 cover labels and aligned the flow-node titles with the requested section titles, including the final `視覺化呈現分析的結果` label.
- Made Part 2 nested hashes and flow-node clicks reveal the `平台運作流程` panel and scroll to the requested stage, including 分析階段一至四.
- Bumped the existing StoryMap script version query so browsers load the updated routing code.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check "intro Website/Website/storymap/storymap.js"` and `git diff --check` passed.
- Browser verification at 1280px and 390px confirmed all seven requested flow links show the correct Part 2 cover/title and keep Part 2 visible.
- Direct `#part-2-summary` deep-link routing was confirmed; the browser reported no warnings or errors.

Remaining:
- Existing concurrent StoryMap edits remain preserved; nothing was pushed.

### 2026-08-11 19:27 HKT — Codex — Removed the chart date and zoom bar

Summary:
- Removed the `1786/12/18 — 1787/01/02` date row and `圖表大小` controls from the platform-interface replica.
- Kept the four-line chart, including its trackpad scrolling and gesture-based zoom behavior.

Files changed:
- `Website/storymap/part-1-interface.js`
- `Website/storymap/part-1-interface.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser inspection confirmed the date row and zoom controls are absent.
- Browser interaction confirmed the chart still scrolls vertically; console warnings and errors were empty.
- `node --check` and `git diff --check` passed.

Remaining:
- Existing concurrent Part 1 and StoryMap edits were preserved; nothing was pushed.



### 2026-08-11 19:26 HKT — Codex — Placed the JSON viewer beside structured-data input

Summary:
- Moved the existing `輸出格式：JSON` filter and JSON viewer into the right side of `輸入結構化資料`.
- Kept the opening `在選定研究主題和史料後...` paragraph full width above the two-column text-and-visual layout.
- Kept the two remaining explanatory paragraphs as left-aligned text cards and left Part 3 with its text explanation and anchor.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap.js`

Verified:
- `node --check Website/storymap/storymap.js` and `git diff --check` passed.
- Desktop browser check confirmed the introduction spans the full width, the cards are on the left, and the JSON/filter visual is on the right.
- Browser interaction check confirmed selecting `標題` still highlights and scrolls to the JSON field.
- Mobile browser check confirmed the order is introduction, text cards, then JSON visual.

Remaining:
- Existing concurrent work was preserved; nothing was pushed.

### 2026-08-11 19:21 HKT — Codex — Added sample-style four-line chart navigation

Summary:
- Wrapped the replica chart in a native scroll viewport so ordinary two-finger trackpad movement pans the chart.
- Applied the sample tool's meta/ctrl-wheel pinch-zoom model, zooming around the pointer, with click-drag panning as a mouse fallback.
- Added compact chart-size controls and kept the four chart nodes, AI result routing, and reset demonstration working.

Files changed:
- `Website/storymap/platform-interface-replica.html`
- `Website/storymap/part-1-interface.js`
- `Website/storymap/part-1-interface.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Compared the live `http://127.0.0.1:8166/sample` chart and its `dualScroll` wheel/pan implementation in the in-app browser.
- Confirmed the replica's native chart scroll position changes, the zoom control changes the canvas to 125% and expands its scroll area, reset returns it to 100%, and a chart dot still opens the AI output card.
- `node --check "intro Website/Website/storymap/part-1-interface.js"`, `git diff --check`, and the browser console warning/error check passed.

Remaining:
- The in-app browser blocks direct `file://` navigation, so verification used the same file through the documented local HTTP preview. Nothing was pushed.

### 2026-08-11 19:20 HKT — Codex — Hid the embedded-link label from the Part 2 OCR sentence

Summary:
- Changed the visible wording from `按此(embedded)了解OCR方法` to `按此了解OCR方法`.
- Kept only `此` as the clickable text, with the same embedded OCR-section target.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check Website/storymap/storymap.js` and `git diff --check` passed.
- Browser verification confirmed the link text is exactly `此`, the sentence reads `按此了解OCR方法`, the target remains `#part-3-ocr-definition`, and `(embedded)` is not visible.

Remaining:
- Existing concurrent work was preserved; nothing was pushed.

### 2026-08-11 19:18 HKT — Codex — Changed the Part 2 OCR reference to an embedded link prompt

Summary:
- Replaced the visible `方法詳見 OCR 並結構化原始史料（with embedded website）` wording with `按此(embedded)了解OCR方法`.
- Made `按此(embedded)` link directly to the embedded OCR section at `#part-3-ocr-definition`.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check Website/storymap/storymap.js` and `git diff --check` passed.
- Browser verification confirmed the link is visible, has the expected anchor, and lands on `#part-3-ocr-definition`.

Remaining:
- Existing concurrent work was preserved; nothing was pushed.

### 2026-08-11 19:06 HKT — Codex — Simplified the replica chart to one readable data chain

Summary:
- Removed the dense sample-state network from the replica screenshot.
- Kept only the four source-backed teaching nodes and three connected segments across the four lanes, with larger, readable markers and solid relationship lines.
- Removed the generated bulk chart-preview records and bumped the local asset version.

Files changed:
- `tool/scripts py/build_part1_interface_data.py`
- `Website/storymap/part-1-interface-data.js`
- `Website/storymap/part-1-interface.js`
- `Website/storymap/part-1-interface.css`
- `Website/storymap/platform-interface-replica.html`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Local browser preview shows four data dots and three usable relationship lines, with no dense marker mesh.
- `node --check Website/storymap/part-1-interface.js`, `node --check Website/storymap/storymap.js`, and `git diff --check` passed.
- Browser console reported no warnings or errors.

Remaining:
- Existing concurrent work was preserved; nothing was pushed.




### 2026-08-11 19:25 HKT — Codex — Merged the AI Skills explanation into one card

Summary:
- Kept the existing AI Skills definition and placed the platform-specific explanation immediately after it inside the same numbered `AI Skills` card.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check Website/storymap/storymap.js` passed.
- `node --check Website/embedded-tool/review-tool-embed.js` passed.
- `git diff --check` passed.
- Browser preview confirmed the card is visible and contains both paragraphs in the requested order.
- Browser console still reports the unrelated concurrent Part 1 error `addDot is not defined`.

Remaining:
- Existing concurrent Part 1 and Part 2 edits were preserved; nothing was pushed.

### 2026-08-11 19:03 HKT — Codex — Removed the preparation-step connector arrow

Summary:
- Removed the internal arrow between `選定題目與史料` and `OCR 並結構化史料` while keeping the two bubbles stacked on normal screens.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`

Verified:
- Confirmed the internal connector markup and CSS are gone; the external flow arrows remain.
- `git diff --check` passed.

Remaining:
- Existing concurrent Part 1, sample-data, and StoryMap edits were preserved; nothing was pushed.

### 2026-08-11 19:14 HKT — Codex — Routed chart node information into AI output cards

Summary:
- Removed the bottom-of-chart node-information panel from the replica.
- Clicking a chart dot now switches to the AI 分析區 and opens a type-specific card: 林方事件／皇帝行動 use event-result cards, while 官員上奏／硃批 use document-result cards.
- Kept the 節點資訊區 label inside the AI panel and preserved clickable source quotations for original-text location.

Files changed:
- `Website/storymap/part-1-interface.js`
- `Website/storymap/part-1-interface.css`
- `Website/storymap/platform-interface-replica.html`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser checks confirmed all four dot types open in the AI panel, no `[data-nodepanel]` remains, and the chart stays free of a bottom overlay.
- `node --check Website/storymap/part-1-interface.js`, `node --check Website/storymap/storymap.js`, and `git diff --check` passed.
- Browser console reported no warnings or errors.

Remaining:
- Existing concurrent work was preserved; nothing was pushed.

### 2026-08-11 19:36 HKT — Codex — Centered the Part 2 flow chart horizontally

Summary:
- Centered the desktop `運作流程圖` flex content within its dark backdrop.
- Kept the narrow/mobile layout vertically top-aligned so the responsive flow remains unchanged.

Files changed:
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `git diff --check` passed.
- Browser preview confirmed equal 29px horizontal gaps between the chart and its backdrop on desktop.
- Confirmed the mobile rule keeps the chart column top-aligned.

Remaining:
- Nothing remaining for this adjustment; nothing was pushed.

### 2026-08-12 13:11 HKT — Codex — Expanded Part 2 Skill panels to full text and single-run typing

Summary:
- Expanded the Part 2 VS Code panels from representative excerpts to the full text of all six source-backed Skills requested for the workflow.
- Kept the editor body scrollable so complete Skills remain readable within the same visual window.
- Made the typing animation run once per page load and retain the complete text; reloading the page starts it again.

Files changed:
- `Website/storymap/storymap-example.html`

Verified:
- All six requested Skill filenames and full source blocks are embedded in the three panels; all `12/12` Agentic-line JSON blocks parse successfully.
- `node --check Website/storymap/storymap.js` and `git diff --check` passed.

Remaining:
- Existing concurrent Part 1 and other StoryMap edits were preserved; nothing was pushed.

### 2026-08-12 13:08 HKT — Codex — Removed the replica area-list subtitle

Summary:
- Removed the `導覽列・時間與關係圖表・原始史料區・人工智能分析區` subtitle beneath `完整平台介面複本`.
- Kept the four interactive interface areas and their labels inside the replica unchanged.

Files changed:
- `Website/storymap/platform-interface-replica.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser inspection confirmed the subtitle is absent and the replica still loads.
- `node --check` on the related JavaScript files and `git diff --check` passed.

Remaining:
- Nothing remaining for this adjustment; nothing was pushed.

### 2026-08-12 13:09 HKT — Codex — Froze the replica chart date column

Summary:
- Kept the chart's date/ruler column fixed at the left edge while the four-line timeline scrolls horizontally.
- Preserved the ruler's shared vertical and zoom coordinate system so its labels remain aligned with the chart dates.

Files changed:
- `Website/storymap/part-1-interface.js`
- `Website/storymap/platform-interface-replica.html`

Verified:
- Browser preview confirmed the ruler stays at the left edge after horizontal chart scrolling.
- `node --check Website/storymap/part-1-interface.js` passed.
- `git diff --check` passed.

Remaining:
- Nothing remaining for this adjustment; nothing was pushed.

### 2026-08-12 13:00 HKT — Codex — Hid the requested Part 2 hero note and card number

Summary:
- Hid the Part 2 hero sentence beginning `平台旨在處理清代奏摺與上諭研究中的兩大主要困難`.
- Hid the `1` marker from the `平台的運作流程` card while keeping its heading and explanatory paragraphs visible.
- Preserved both original snippets in reversible HTML comments.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed the requested sentence and number are inside reversible comments and are no longer rendered as page content.
- `git diff --check` passed.

Remaining:
- Existing concurrent StoryMap and Part 3 edits remain untouched; nothing was pushed.

### 2026-08-12 13:21 HKT — Codex — Activated the Part 1 replica tools dropdown

Summary:
- Matched the sample review tool's settings behavior in the platform-interface replica: export, split export, import, skill-output loading, interface/body font controls, line opacity, dot spacing, day spacing, and lane spacing now perform real scoped actions.
- Kept replica state isolated under its own local-storage key and made import/export operate on the teaching replica's state without changing formal or sample saved data.
- Added a scoped body-font override so the 正文 control changes document/event reading text independently of 介面字級.

Files changed:
- `Website/storymap/part-1-interface.js`
- `Website/storymap/part-1-interface.css`

Verified:
- `node --check Website/storymap/part-1-interface.js` passed.
- `git diff --check` passed.
- Browser check over the local HTTP preview confirmed the settings panel opens, timeline sliders redraw, font controls apply, split export reports success, and both JSON file inputs restore an imported chart node; no browser warnings or errors were reported.

Remaining:
- Nothing remaining for this adjustment; nothing was pushed.

### 2026-08-12 12:59 HKT — Codex — Added source-backed AI Skill panels to Part 2 workflow cards

Summary:
- Added VS Code-style panels on the right of the related Part 2 text-card groups for event extraction, source tracing, and the three 上諭 analysis Skills.
- Displayed the actual Skill filenames and representative rules from `extract-lin-actions.md`, `extract-qing-actions-all.md`, `trace-source-chain.md`, `extract-yu-emperor-actions.md`, `confirmed-yu-response-analysis.md`, and `extract-yu-reported-events.md`.
- Kept the Qing action extraction as one three-category output (`done`, `plan`, `nonmil`) and retained the quoted-evidence / researcher-review boundary.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`

Verified:
- Agentic-line JSON blocks parsed successfully (`12/12`); `node --check Website/storymap/storymap.js` passed.
- Browser desktop check confirmed the VS Code window is to the right of each related card group.
- Browser mobile check at 390px confirmed the panels stack below the cards, remain visible, and produce no horizontal overflow; console reported no warnings or errors.

Remaining:
- Existing concurrent Part 1 and other StoryMap edits were preserved; nothing was pushed.

### 2026-08-11 19:43 HKT — Codex — Stabilized replica chart dot hover and click

Summary:
- Prevented the shared HTML-dot hover transform from moving SVG chart circles away from their data coordinates.
- Excluded chart nodes from the chart pan gesture so clicking a dot opens its AI 分析區 card reliably.

Files changed:
- `Website/storymap/part-1-interface.css`
- `Website/storymap/part-1-interface.js`
- `Website/storymap/platform-interface-replica.html`

Verified:
- Browser preview confirmed hovering keeps the circle centered on its SVG coordinate and clicking the circle opens the AI 分析區 card.
- `node --check Website/storymap/part-1-interface.js` passed.
- `git diff --check` passed.

Remaining:
- Nothing remaining for this adjustment; nothing was pushed.

### 2026-08-12 13:05 HKT — Codex — Renumbered the Part 2 workflow diagram card

Summary:
- Changed the number box beside `運作流程圖` from `2` to `1`.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed the `運作流程圖` card now renders with number `1`.
- `git diff --check` passed.

Remaining:
- Nothing remaining for this adjustment; nothing was pushed.

### 2026-08-12 13:15 HKT — Codex — Hid the full Part 2 overview card reversibly

Summary:
- Hid the entire `平台的運作流程` overview card, including its heading, number box, and both explanatory paragraphs.
- Preserved the complete card markup in one reversible HTML comment.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed the overview card is no longer rendered while the full original text remains in HTML comments.
- `git diff --check` passed.

Remaining:
- Existing concurrent Part 1 edits remain untouched; nothing was pushed.

### 2026-08-12 13:15 HKT — Codex — Removed the four chart lane labels

Summary:
- Removed the visible four-label row above the chart: `戰場事件`, `官員上奏`, `皇帝硃批下旨`, and `皇帝行動`.
- Kept the four-line chart, chart nodes, and numbered interface markers unchanged.

Files changed:
- `Website/storymap/part-1-interface.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser inspection confirmed the lane-label row is absent and all four labels have zero rendered matches inside the chart.
- The chart still loads with no browser warnings or errors.
- `node --check` and `git diff --check` passed.

Remaining:
- Existing concurrent Part 1 CSS edits remain untouched; nothing was pushed.

### 2026-08-12 13:14 HKT — Codex — Hid the empty Part 2 overview section reversibly

Summary:
- Hid the entire empty `part-2-overview` section so no blank card area remains after removing its card.
- Preserved the section and complete card markup in one reversible HTML comment.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed the `part-2-overview` section is absent from the rendered DOM and the following `運作流程圖` section remains present.
- `git diff --check` passed.

Remaining:
- Existing concurrent Part 1 edits remain untouched; nothing was pushed.

### 2026-08-12 13:18 HKT — Codex — Fixed Part 2 Step 1/2 redirects and header overlap

Summary:
- Routed the Part 2 flow's Step 1 link to Part 3's `適合的研究問題` card instead of keeping the Part 2 panel active.
- Routed Step 2 to the complete `步驟二／OCR 並結構化原始史料` stage cover.
- Added a sticky-header offset to nested StoryMap redirects so the selected target begins below the navigation bar rather than being covered by it.
- Bumped the StoryMap script version query so the updated redirect behavior loads in the browser.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check "intro Website/Website/storymap/storymap.js"` and `git diff --check` passed.
- Browser verification at 1280px and 390px confirmed Step 1 and Step 2 activate Part 3, show the requested headings, and place the target at or below the 62px header boundary.
- Browser console reported no warnings or errors.

Remaining:
- Existing concurrent Part 1 edits remain untouched; nothing was pushed.

### 2026-08-12 13:24 HKT — Codex — Updated the Step 3 structured-data introduction

Summary:
- Replaced the opening sentence under `輸入結構化資料` with the requested wording about converting selected research materials into structured JSON, loading it into the platform, creating document nodes, and displaying the original text.
- Kept the `此` link pointing to `#part-3-ocr-definition` for the OCR-method explanation.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser preview confirmed the sentence renders directly below the `輸入結構化資料` title in 步驟三.
- `node --check "Website/storymap/storymap.js"` and `git diff --check` passed.

Remaining:
- Existing concurrent Part 1, StoryMap routing, and log edits remain untouched; nothing was pushed.

### 2026-08-12 13:38 HKT — Codex — Removed the Part 1 teaching overlay

Summary:
- Removed the four numbered area labels (`導覽列`, `時間與關係圖表`, `原始史料區`, and `AI 分析區`) from the replica.
- Removed their explanatory callouts, progress/reset strip, dimmed-region treatment, active border, and hotspot behavior.
- Kept the recreated tool's actual toolbar, chart, document panel, AI panel, event-chain control, chart nodes, and chart gestures.

Files changed:
- `Website/storymap/part-1-interface.js`
- `Website/storymap/part-1-interface.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser inspection found zero hotspot, callout, progress, active-region, or active-class elements; the chart and four tool regions still load.
- Browser interaction confirmed the AI toolbar control still works without restoring any highlight overlay.
- Browser console reported no warnings or errors; `node --check` and `git diff --check` passed.

Remaining:
- Existing concurrent StoryMap and log edits remain untouched; nothing was pushed.

### 2026-08-12 13:28 HKT — Codex — Moved the structured-data introduction to the cover tab

Summary:
- Added the requested structured-data introduction beneath the cover title.
- Removed the duplicate paragraph from `輸入結構化資料` so the sentence appears only on the cover tab.
- Kept the `此` link pointing to `#part-3-ocr-definition` for the OCR-method explanation.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser preview confirmed the paragraph renders below the cover title and the Step 3 duplicate is absent.
- Browser console reported no warnings or errors; `node --check "Website/storymap/storymap.js"` and `git diff --check` passed.

Remaining:
- Existing concurrent Part 1, StoryMap routing, and log edits remain untouched; nothing was pushed.

### 2026-08-12 13:38 HKT — Codex — Placed the structured-data text under the Step 3 title

Summary:
- Moved the structured-data introduction from the home cover into the `輸入結構化資料` section hero, directly below the title shown in the Step 3 header.
- Kept the OCR-method link on `此` and removed the cover-only version.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser preview of `#part-2-input` confirmed the text is visible directly beneath `輸入結構化資料` and the cover copy is absent.
- Browser console reported no warnings or errors; `node --check "Website/storymap/storymap.js"` and `git diff --check` passed.

Remaining:
- Existing concurrent Part 1, StoryMap routing, and log edits remain untouched; nothing was pushed.

### 2026-08-12 13:45 HKT — Codex — Increased the Step 3 cover-bar height

Summary:
- Increased only the `輸入結構化資料` cover bar to `230px` at the current desktop viewport so its title and explanatory text have more vertical space.
- Bumped the `storymap-cards.css` version query so the new height loads without stale browser CSS.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser preview measured the Step 3 cover bar at `230px`; the explanatory text remained visible and the browser console reported no warnings or errors.
- `node --check "Website/storymap/storymap.js"` and `git diff --check` passed.

Remaining:
- Existing concurrent Part 1, review-tool, StoryMap data, routing, and log edits remain untouched; nothing was pushed.

### 2026-08-12 16:18 HKT — Codex — Matched 載入技能輸出 to the sample bundle picker

Summary:
- Replaced the replica's native file-chooser-only behavior with the sample tool's newest-first bundle picker.
- Bundle cards now show the bundle name as the load action, timestamp, skill chain, document count, and a compact `文書：…` preview.
- Selected bundles load their saved JSON outputs into the replica's AI panel using the existing skill-specific cards; no extra chart dots are created.
- Added the local review API route as the preferred source, with the replica's bundled sample outputs and file chooser retained as standalone fallbacks.

Files changed:
- `Website/storymap/part-1-interface.js`
- `Website/storymap/part-1-interface.css`
- `Website/storymap/platform-interface-replica.html`
- `Website/storymap/storymap-example.html`
- `../review-tools/server.py`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser QA opened the picker from `工具 → 載入技能輸出`, showed two fallback bundle cards, and loaded `yu-first-5-gemini36` as 9 turns / 32 output cards.
- Browser QA loaded `zhu-december-rerun-g36` as 10 turns / 10 output cards.
- `node --check Website/storymap/part-1-interface.js`, `python3 -m py_compile ../review-tools/server.py`, and `git diff --check` passed.

Remaining:
- The local review API must be running at `127.0.0.1:8166` for the full live bundle list; standalone file use falls back to the bundled sample outputs or manual `.data` / `.json` selection.

### 2026-08-12 16:14 HKT — Codex — Added numbered communication-relation cards

Summary:
- Converted the two paragraphs under `重建通信關係` into numbered text cards.
- Added the labels `第一層的通信關係` and `深層的通信關係`, with the original paragraph content retained beneath each label.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser preview confirmed both cards render below the communication-relation cover bar with number boxes `1` and `2`.
- Browser console reported no warnings or errors; `node --check "Website/storymap/storymap.js"` and `git diff --check` passed.

Remaining:
- Existing concurrent Part 1, review-tool, StoryMap data, routing, and log edits remain untouched; nothing was pushed.

### 2026-08-12 15:06 HKT — Codex — Corrected the event-chain backdrop boundary

Summary:
- Removed the unused brown stage area to the left of the event-chain panel by making the eventline stage column exactly match the dock width.
- Kept the event-chain backdrop to the panel's 8px outer margin and synchronized that boundary as the panel expands or contracts.

Files changed:
- `Website/storymap/part-1-interface.js`
- `Website/storymap/part-1-interface.css`
- `Website/storymap/platform-interface-replica.html`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser geometry showed chart and dock boundaries meeting at `x=575`, then `x=551` after widening; the backdrop remained only `8px` left of the event-chain card.
- The event-chain panel widened from `204px` to `228px` while AI/document widths stayed unchanged; browser screenshot matched the corrected boundary.
- Browser diagnostics, `node --check`, and `git diff --check` passed.

Remaining:
- Existing concurrent Part 1, review-tool, StoryMap data, routing, and log edits remain untouched; nothing was pushed.

### 2026-08-12 14:20 HKT — Codex — Merged and narrowed the Part 2 summary card

Summary:
- Combined the `第一組 AI Skills 負責總結文書` and `摘要和分段結果會顯示在原始文書區中` paragraphs into one unnumbered, untitled text card.
- Added a visible paragraph gap controlled by `--part2-summary-paragraph-gap`.
- Added CSS controls for the shared Part 2 text-card width and the narrower summary-card width.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed the summary stage contains one text card with two paragraphs and no number box or subtitle.
- `git diff --check` passed.

Remaining:
- Existing concurrent Part 1, review-tool, StoryMap data, routing, and log edits remain untouched; nothing was pushed.

### 2026-08-12 14:46 HKT — Codex — Corrected panel resizing to independent left-edge handles

Summary:
- Removed the shared AI/document divider behavior. The only desktop resize affordances are now the left edge of each panel: AI between the chart and AI panel, and document between the AI and document panels.
- Moving a handle left or right changes only the panel that owns that left edge; the neighboring panel width remains unchanged, the dock stays anchored to the right, and the chart absorbs the available space without overlap.
- Kept the event-chain panel's own left-edge handle and independent width behavior.

Files changed:
- `Website/storymap/part-1-interface.js`
- `Website/storymap/part-1-interface.css`
- `Website/storymap/platform-interface-replica.html`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser QA changed AI from `183px` to `207px` while document stayed `215px`, then changed document to `239px` while AI stayed `207px`.
- The chart-to-dock boundary remained flush and the panel gap remained `9px`; after closing AI, the document remained `239px` wide with no chart/document overlap.
- Browser diagnostics, `node --check`, and `git diff --check` passed; both panels reopened from the toolbar.

Remaining:
- Existing concurrent Part 1, review-tool, StoryMap data, routing, and log edits remain untouched; nothing was pushed.

### 2026-08-12 14:02 HKT — Codex — Docked the event chain and connected it to uploaded chart data

Summary:
- Moved 事件鏈 into the Part 1 tool dock so it opens as a panel beside the chart, alongside the AI and document panels.
- Replaced the hardcoded event-chain cards with a renderer driven by the selected chart node, source IDs, response links, dates, descriptions, quotations, and imported raw records.
- Kept the event-chain panel open when a dot is selected, and excluded unconfirmed AI candidates from the displayed chain unless they become chart data.

Files changed:
- `Website/storymap/part-1-interface.js`
- `Website/storymap/part-1-interface.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Imported `/Users/creamybanana/Downloads/sample_all.data` through the replica's existing 匯入 control; the chart expanded to 29 dots and selecting imported `匪徒於大墩殺害官員` displayed source-backed data from `硃25` and related events.
- Reload returned to the four built-in dots, confirming the upload test did not replace the starting dataset.
- `node --check`, `git diff --check`, and browser error/warning diagnostics passed.

Remaining:
- Existing concurrent Part 1, review-tool, StoryMap data, routing, and log edits remain untouched; no clean local checkpoint was created because the two implementation files contain overlapping pre-existing edits.

### 2026-08-12 14:01 HKT — Codex — Matched the settings panel to the sample scale

Summary:
- Reduced the settings dropdown again to a 410px desktop maximum with compact 26px controls, smaller labels, tighter spacing, and a 380px mobile maximum.
- Kept the dropdown open for `介面字級` and `正文` button clicks so users can make repeated adjustments without reopening it.
- Bumped the interface stylesheet query so the latest sizing rules load immediately.

Files changed:
- `Website/storymap/part-1-interface.css`
- `Website/storymap/part-1-interface.js`
- `Website/storymap/platform-interface-replica.html`
- `Website/storymap/storymap-example.html`

Verified:
- Browser preview measured the open settings panel at `410px × 410px`, with all 7 buttons and 6 sliders present.
- Clicking `介面字級 A＋` and `正文 A＋` kept the dropdown open and updated the scoped font variables.
- `node --check Website/Website/storymap/part-1-interface.js` and `git diff --check` passed.

Remaining:
- Existing concurrent Part 1, review-tool, StoryMap data, routing, and log edits remain untouched; nothing was pushed.

### 2026-08-12 13:57 HKT — Codex — Resized the settings dropdown

Summary:
- Reduced the settings dropdown to a 620px desktop maximum with smaller padding, section gaps, buttons, typography, slider rows, and slider thumbs.
- Added a viewport-safe maximum height and a narrower mobile width so the complete settings list remains usable without dominating the interface.
- Bumped the interface stylesheet query so the resized dropdown loads immediately.

Files changed:
- `Website/storymap/part-1-interface.css`
- `Website/storymap/platform-interface-replica.html`
- `Website/storymap/storymap-example.html`

Verified:
- Browser preview measured the open settings panel at `620px × 483px`, with all 7 buttons and 6 sliders present.
- `node --check Website/Website/storymap/part-1-interface.js` and `git diff --check` passed.

Remaining:
- Existing concurrent Part 1, review-tool, StoryMap data, routing, and log edits remain untouched; nothing was pushed.

### 2026-08-12 13:51 HKT — Codex — Reduced the Part 1 replica top bar

Summary:
- Reduced the toolbar height, padding, gaps, button heights, search field, people selector, gear button, and mobile wrapped height so the top bar takes less vertical space without changing chart/document panel sizes.
- Bumped the interface stylesheet query so the compact toolbar rules load immediately.

Files changed:
- `Website/storymap/part-1-interface.css`
- `Website/storymap/platform-interface-replica.html`
- `Website/storymap/storymap-example.html`

Verified:
- Browser preview measured the toolbar at `44px`, its controls at `29px`, and loaded `part-1-interface.css?v=20260812-toolbar-compact-01`.
- `node --check Website/storymap/part-1-interface.js` and `git diff --check` passed.

Remaining:
- Existing concurrent Part 1, review-tool, StoryMap data, routing, and log edits remain untouched; nothing was pushed.

### 2026-08-12 13:47 HKT — Codex — Refreshed the replica font stylesheet

Summary:
- Bumped the Part 1 interface stylesheet query in the standalone replica and StoryMap embed so the live page loads the CSS rule that applies the separate 介面字級 and 正文 controls.

Files changed:
- `Website/storymap/platform-interface-replica.html`
- `Website/storymap/storymap-example.html`

Verified:
- Browser preview loaded `part-1-interface.css?v=20260812-tools-font-01`.
- The rendered document text changed from `17.94px` to `15.18px` after one 正文 decrease, and interface controls changed from `16.9px` to `15.6px` after one 介面字級 decrease.
- `git diff --check` passed.

Remaining:
- Existing concurrent Part 1, review-tool, StoryMap data, routing, and log edits remain untouched; nothing was pushed.

### 2026-08-12 13:52 HKT — Codex — Restored document-dot AI chat provenance

Summary:
- Added saved `硃40.chat` and `諭24.chat` projections to the Part 1 replica so the AI output that forms the clear-demo event and emperor-action dots can be loaded and inspected in the AI analysis area.
- Added a matched source panel on the chart node for the `諭24` emperor-action dot, and updated the formal/sample document-dot handlers so the underlying review tools open the matching AI card as well.
- Kept the replica's existing 硃42 document viewer while labelling the clear-demo chat sources separately.

Files changed:
- `Website/storymap/part-1-interface-data.js`
- `Website/storymap/part-1-interface.js`
- `Website/storymap/part-1-interface.css`
- `Website/storymap/platform-interface-replica.html`
- `Website/storymap/storymap-example.html`
- `../review-tools/(1) formal/index.html`
- `../review-tools/(2) sample/index.html`
- `../tool/scripts py/build_part1_interface_data.py`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser QA loaded `硃40.chat` (10 output items) and `諭24.chat` (32 output items) from the replica; clicking the emperor-action node revealed its linked `諭24.chat` output.
- `node --check`, generated-data parsing, and `git diff --check` passed.

Remaining:
- Existing concurrent Part 1, review-tool, StoryMap data, routing, and log edits remain untouched; nothing was pushed.

### 2026-08-12 13:57 HKT — Codex — Moved the Step 4 explanatory sentence into its cover bar

Summary:
- Placed `完成輸入結構化原始文書後，下一步便是運用 AI 和AI Skills，從史料中提取特定的資訊。` directly below `使用AI從原文中抽取資訊` in the Part 2 cover bar.
- Removed the duplicate paragraph from the first content card below the cover bar.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser preview confirmed the sentence is visible beneath the Step 4 title and appears zero times in the content cards.
- Browser console reported no warnings or errors; `node --check "Website/storymap/storymap.js"` and `git diff --check` passed.

Remaining:
- Existing concurrent Part 1, review-tool, StoryMap data, routing, and log edits remain untouched; nothing was pushed.

### 2026-08-12 13:59 HKT — Codex — Added closable and resizable replica panels

Summary:
- Added working X controls for the AI chat and document panels in the standalone Part 1 replica.
- Added a keyboard- and pointer-resizable divider between the two panels, with min/max width limits and toolbar reopening after either panel is closed.
- Kept the behavior available to the shared Part 1 interface renderer used by the StoryMap example.

Files changed:
- `Website/storymap/part-1-interface.js`
- `Website/storymap/part-1-interface.css`
- `Website/storymap/platform-interface-replica.html`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser QA closed AI, expanded the document panel, reopened AI from the toolbar, closed the document panel, expanded AI, and reopened both with Note.
- Keyboard divider resizing changed the AI/document split from `46%/54%` to `51.31%/48.69%`.
- `node --check`, `git diff --check`, and browser diagnostics passed.

Remaining:
- Existing concurrent Part 1, review-tool, StoryMap data, routing, and log edits remain untouched; nothing was pushed.

### 2026-08-12 14:01 HKT — Codex — Increased the Step 4 cover-bar height

Summary:
- Increased only the `使用AI從原文中抽取資訊` cover bar to `230px`, matching the additional space used for Step 3.
- Bumped the `storymap-cards.css` version query so the new height loads without stale browser CSS.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser preview measured the Step 4 cover bar at `230px`; the title and explanatory sentence remained visible.
- Browser console reported no warnings or errors; `node --check "Website/storymap/storymap.js"` and `git diff --check` passed.

Remaining:
- Existing concurrent Part 1, review-tool, StoryMap data, routing, and log edits remain untouched; nothing was pushed.

### 2026-08-12 14:02 HKT — Codex — Added numbered cards for structured-data fields and dates

Summary:
- Converted the two Part 2 structured-data paragraphs into numbered text cards.
- Set the first card subtitle to `JSON中的文本資料` and the second to `收發日期`.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed the two cards render with number boxes `1` and `2` and the requested subtitles.
- `git diff --check` passed.

Remaining:
- Existing concurrent Part 1, review-tool, StoryMap data, routing, and log edits remain untouched; nothing was pushed.

### 2026-08-12 14:11 HKT — Codex — Added left-edge resize handles to every replica panel

Summary:
- Added sample-tool-style left-edge resize handles to the AI, document, and event-chain panels.
- Kept keyboard support on every handle and retained the shared divider as an additional desktop control for the AI/document split.
- Added event-chain width persistence during the current view and reset support.

Files changed:
- `Website/storymap/part-1-interface.js`
- `Website/storymap/part-1-interface.css`
- `Website/storymap/platform-interface-replica.html`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser preview found visible left-edge handles for AI and document panels.
- AI and document handles independently changed the split from `46%/54%` to `43%/57%` and back to `46%/54%` with keyboard resizing.
- Event-chain handle changed its width from `225px` to `249px`; browser diagnostics, `node --check`, and `git diff --check` passed.

Remaining:
- Existing concurrent Part 1, review-tool, StoryMap data, routing, and log edits remain untouched; nothing was pushed.

## 2026-08-12 14:14 HKT — Codex — Put the event chain beside existing panels

Summary:
- Kept AI and document panels visible when 事件鏈 opens.
- Positioned 事件鏈 as the first same-level panel to the left of the existing AI/resizer/document columns.
- Preserved panel resizing flex ratios and kept the eventline usable when one or both existing panels are closed; narrow layouts scroll horizontally across the peer panels.

Files changed:
- `Website/storymap/part-1-interface.js`
- `Website/storymap/part-1-interface.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser geometry: eventline x=510 width=248, AI x=771 width=192, divider x=968 width=10, doc x=982 width=225; all share y=48 and height=624.
- Clicking the built-in event dot kept eventline open, kept AI/document displays active, and showed the source-backed `硃42` chain.
- `node --check`, `git diff --check`, and browser diagnostics passed.

Remaining:
- Existing overlapping project edits remain untouched; no clean checkpoint was created and nothing was pushed.

### 2026-08-12 15:44 HKT — Codex — Restored frozen four-line chart tabs

Summary:
- Restored the four chart tabs `戰場事件`, `官員上奏`, `皇帝硃批下旨`, and `皇帝行動`.
- Kept the tab row fixed above the chart's scroll viewport and synchronized each tab's horizontal position with its lane axis and dots during panning and redraws.

Files changed:
- `Website/storymap/part-1-interface.js`
- `Website/storymap/part-1-interface.css`
- `Website/storymap/platform-interface-replica.html`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser replica showed all four labels with no diagnostics.
- Vertical scrolling left the tabs fixed; horizontal panning moved the labels with the chart content.
- `node --check` and `git diff --check` passed.

Remaining:
- Existing concurrent edits remain untouched; no clean checkpoint was created and nothing was pushed.

### 2026-08-12 15:54 HKT — Codex — Bound chart-tab text to 介面字級

Summary:
- Changed the four frozen chart-tab labels to use the replica's `--font-scale`, controlled by `介面字級`; `正文` remains independent.

Files changed:
- `Website/storymap/part-1-interface.css`
- `Website/storymap/platform-interface-replica.html`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser font size changed from `22.4px` at `1.4×` to `24px` at `1.5×` after using the `介面字級` A＋ control.
- Browser diagnostics, `node --check`, and `git diff --check` passed.

Remaining:
- Existing concurrent edits remain untouched; no clean checkpoint was created and nothing was pushed.

### 2026-08-12 14:54 HKT — Codex — Synchronized the event-chain backdrop with its panel width

Summary:
- Bound the brown dock backdrop width to the event-chain panel track plus the unchanged AI/document panel tracks.
- When the event-chain left handle moves, its right edge and the AI/document panels remain fixed; the backdrop expands or contracts from the left with the event-chain panel.

Files changed:
- `Website/storymap/part-1-interface.js`
- `Website/storymap/part-1-interface.css`
- `Website/storymap/platform-interface-replica.html`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser geometry changed the event-chain panel from `204px` to `236px` while AI stayed `183px` and document stayed `215px`.
- The brown dock backdrop expanded from `640px` to `664px`, its left edge moved left, and the event-chain right edge stayed fixed; shrinking reversed this without overlap.
- Browser diagnostics, `node --check`, and `git diff --check` passed.

Remaining:
- Existing concurrent Part 1, review-tool, StoryMap data, routing, and log edits remain untouched; nothing was pushed.

## 2026-08-12 15:23 HKT — Codex — Matched AI chat cards to each skill type

Summary:
- Replaced the one generic saved-output card with data-driven layouts for event extraction, emperor actions, official responses, document pairing, source tracing, and 上諭審閱迴圈 outputs.
- Added Qing action status badges, labelled 上諭／官員回應 quotations, provenance-flow styling, and explicit non-overlapping expanded skill cards.
- Released the dedicated AI view from the right-anchored dock width so the cards use the full AI reading panel.

Files changed:
- `Website/storymap/part-1-interface.js`
- `Website/storymap/part-1-interface.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Dedicated AI panel width is 1150px at the desktop browser preview.
- `硃40.chat` rendered 10 extraction cards with separate 林方／清方 headers and seven `清軍事：已執行` badges.
- `諭24.chat` rendered 8 emperor-action cards and 24 official-response cards; expanded cards had no overlap.
- Clicking the emperor-action chart dot opened the specialized card and its saved source card with two locatable quotations; browser diagnostics were clear.
- `node --check`, `git diff --check`, and browser diagnostics passed.

Remaining:
- Existing concurrent Part 1, review-tool, StoryMap data, routing, and log edits remain untouched; no clean checkpoint was created and nothing was pushed.

## 2026-08-12 15:40 HKT — Codex — Applied 正文 scaling to AI chat content

Summary:
- Scoped the AI chat/source body to the combined `介面字級 × 正文` scale while leaving the AI panel chrome on `介面字級`.
- Bumped the shared Part 1 behavior script version in the standalone replica and StoryMap page.

Files changed:
- `Website/storymap/part-1-interface.js`
- `Website/storymap/platform-interface-replica.html`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `正文` A＋ changed the linked AI source title from `23.52px` to `25.48px` while the settings panel remained open at `410px × 410px`.
- `aiBody` received the updated local scale (`1.68` → `1.82`); JavaScript syntax and diff checks passed.

Remaining:
- Existing concurrent Part 1, StoryMap data, routing, stylesheet, and log edits remain untouched; no deployment or push was performed.

## 2026-08-12 15:44 HKT — Codex — Removed node summary bars and coloured card edges

Summary:
- Removed the visible `節點資訊區／戰場事件` header from selected chart-node cards.
- Removed the `擷取林方行動` and `皇帝行動` group bars from node-card views.
- Replaced coloured left accents on AI cards with neutral one-pixel outlines while preserving the card content, quotations, and source actions.

Files changed:
- `Website/storymap/part-1-interface.js`
- `Website/storymap/part-1-interface.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser node view showed no node-summary or event-group bars and retained the event title, description, quotation, facts, and saved-source content.
- Event-card computed `border-left` was neutral (`1px solid rgb(226, 216, 196)`) rather than the red skill accent; browser diagnostics were clear.
- `node --check` and `git diff --check` passed.

Remaining:
- Existing concurrent edits remain untouched; no clean checkpoint was created and nothing was pushed.

### 2026-08-12 15:57 HKT — Codex — Routed four-line chart clicks into the panel dock

Summary:
- Middle-line dots now open the AI result card on the left and the document panel on the right.
- The leftmost and rightmost dots now open their type-specific `節點資訊區` card to the left of the existing panels.
- When the event-chain panel is already open, an outer-lane click keeps the order `[節點資訊區][事件鏈][AI][文書]`.
- Kept the four source-backed dots readable and clickable by sizing the chart to the available viewport instead of rendering an oversized unusable canvas.

Files changed:
- `Website/storymap/part-1-interface.js`
- `Website/storymap/part-1-interface.css`
- `Website/storymap/platform-interface-replica.html`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser QA confirmed the left outer node opens `戰場事件`, the right outer node opens `皇帝行動`, and both retain visible AI and document panels.
- Browser QA confirmed a middle node hides the node card while retaining AI plus document panels.
- Browser QA confirmed event-chain ordering with an outer node open.
- `node --check Website/storymap/part-1-interface.js` and `git diff --check` passed.

Remaining:
- Existing concurrent edits remain untouched; no deployment or push was performed.

### 2026-08-12 16:12 HKT — Codex — Moved the communication-Skills explanation into its cover tab

Summary:
- Moved `平台設有兩種的 Skills，用於辨識一份奏摺所回應的硃批或上諭，以及辨識一份上諭所回應的奏摺。` beneath the `重建通信關係` cover title.
- Removed the duplicate paragraph card from the section body.
- Increased the cover-tab height with a dedicated `#part-2-communication-bar` CSS control.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed the paragraph appears once as the cover subtitle and is absent from the body-card list.
- Confirmed the communication cover uses the increased `clamp(260px, 34vh, 340px)` height control.
- `git diff --check` passed.

Remaining:
- Existing concurrent Part 1, review-tool, StoryMap data, routing, and log edits remain untouched; nothing was pushed.

### 2026-08-12 16:47 HKT — Claude — Added a layer-3 substage cover for 辨識奏摺所回應的上諭

Summary:
- Added a new "layer 3" sub-cover for the `重建通信關係` (layer 2) child topic `辨識奏摺所回應的上諭`, replacing the previous pattern of putting the sub-title inside a numbered `.part2-text-card`.
- New `.part2-substage-cover` reuses the layer-2 hero gradient but is flush to the left screen edge (negative margin cancels the section's own `--part-pad-x`), spans ~55–58vw, and fades to full transparency on the right via an 11-stop eased `mask-image` (no fade on the left). A large faint stage numeral (`2-1` / `之一`) replaces layer 2's small eyebrow.
- Only applied to `#part-2-yu-response` so far; `#part-2-zhu-response` still uses the old numbered-card title pending sign-off.
- Iterated first as a standalone mockup (`Website/storymap/storymap-layer3-cover-ideas.html`) before implementing in the live page.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap-layer3-cover-ideas.html` (new standalone mockup, not linked from the site)
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Re-read the edited HTML/CSS regions to confirm markup and selectors match.
- Could not browser-QA the live page: local navigation to `http://127.0.0.1:8765/...` was blocked by the Chrome tool's own safety check; user should refresh and confirm visually.
- `git status` showed pre-existing staged changes not made in this session and a `.git/index.lock`; no `git add`/`git commit` was run.

Remaining:
- User visual sign-off on the new cover, then decide whether to apply the same treatment to `#part-2-zhu-response`.
- Local checkpoint commit still needed once the pre-existing staged/lock state is resolved or reviewed.

### 2026-08-12 17:05 HKT — Claude — Extended the layer-3 substage cover to four more sub-topics

Summary:
- Applied `.part2-substage-cover` to `#part-2-zhu-response` (辨識奏摺所回應的硃批, `2-2`), `#part-2-yu-source` (辨識上諭所回應的奏摺, `2-3`), `#part-2-events` (抽取官員奏報的事件、官員對事件的回應, `3-1`), and `#part-2-sources` (追溯資訊的來源, `3-2`), replacing each numbered-card title the same way `#part-2-yu-response` was handled earlier today.
- Removed each section's `.title-row`/number/`<h2>` and kept the paragraph text unchanged and untitled.
- Made `border-bottom` transparent on the section immediately before each new cover (`#part-2-yu-response`, `#part-2-zhu-response`, `#part-2-extract-content`, `#part-2-events`) so no seam shows.
- Removed two now-unused `.part2-numbered-card` compound selectors left over in `storymap-cards.css`.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Re-read each edited block; confirmed only the intended sections' border-bottom rules changed.
- Could not browser-QA live (Chrome tool still blocks local navigation); user should confirm visually.
- `git status` shows continued concurrent activity on this branch (a commit `13d490e` landed from another session) plus a `.git/index.lock`; no `git add`/`git commit` was run.

Remaining:
- User visual sign-off on all five covers in sequence.
- Local checkpoint commit still pending.

### 2026-08-12 17:38 HKT — Codex — Grouped Part 2 cards and attached visuals to their requested parts

Summary:
- Kept each requested explanation as an individual card while grouping the cards into explicit parts for `辨識奏摺所回應的上諭`, `辨識上諭所回應的奏摺`, `抽取官員奏報的事件、官員對事件的回應`, `追溯資訊的來源`, and `收取上諭的資訊`.
- Placed the `通信關係複雜` visual in the first part of `辨識奏摺所回應的上諭`; placed the Visual Studio Code visuals in the requested first or second parts for the extraction substages.
- Added `為奏聞提臣等赴臺並飭沿海官員嚴密巡查事` to the second card of `辨識奏摺所回應的硃批`.
- Moved the requested explanatory sentences into the cover tabs for `辨識上諭所回應的奏摺` and `抽取奏摺的資訊`.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `git diff --check` passed and the stylesheet brace count remains balanced (`651` opening / `651` closing braces).
- Browser QA passed at the default wide viewport and a temporary 390px viewport: card-part counts and visual alignment matched the requested groups, mobile visual order follows its associated part, and browser console warnings/errors were empty.
- Preserved the existing concurrent uncommitted edits; no staging, commit, or push was performed.

Remaining:
- User visual sign-off on the updated Part 2 card groupings.
- Local checkpoint commit remains pending until concurrent git activity settles.

### 2026-08-12 18:04 HKT — Codex — Corrected Part 2 row layout and removed inter-part strips

Summary:
- Kept each requested Part 2 part as one full-width backdrop containing one text card; the card now stays in the left column and its requested visual sits in the right column of the same row.
- Removed the vertical grid gaps between adjacent parts so no thin page-background strips appear between the backdrops.
- Left the Part 3 `修改、建立 AI Skills` area untouched.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `git diff --check` passed; stylesheet braces remain balanced (`666` opening / `666` closing).
- Browser QA passed at the wide viewport and temporary 390px viewport: text cards stay left of visuals on desktop, adjacent part gaps are `0px`, full-width backdrop pseudo-elements reach both viewport edges, every target part contains exactly one text card, the five covers remain 390px wide, and browser warnings/errors are empty.
- Diff inspection shows no changes to the Part 3 `修改、建立 AI Skills` area.

Remaining:
- User visual sign-off on the corrected Part 2 rows.
- Local checkpoint commit remains pending until concurrent git activity settles; no staging, commit, or push was performed.

### 2026-08-12 18:12 HKT — Codex — Applied the latest Part 2 card grouping request

Summary:
- Kept `辨識奏摺所回應的上諭` as three individual card parts with `通信關係複雜` in the first part, and `辨識奏摺所回應的硃批` as four individual card parts with the `為奏聞提臣等赴臺並飭沿海官員嚴密巡查事` visual in the second part.
- Kept the requested cover-tab notes for `辨識上諭所回應的奏摺` and `抽取奏摺的資訊`.
- Grouped the later cards as requested: 上諭來源配 `3+2`, 抽取事件 `2+2` with the VS Code visual in the second group, 追溯來源 `1+2` with the visual in the first group, and 收取上諭資訊 `2+1+1`.
- Removed the inherited visual top offset so each visual is contained by its assigned part backdrop.
- Left Part 3 `修改、建立 AI Skills` untouched.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `git diff --check` passed; stylesheet braces remain balanced (`666` opening / `666` closing).
- Browser QA passed at the wide viewport and temporary 390px viewport: requested article counts and visual row assignments matched, visuals stayed inside their assigned parts, card rows had no gaps, all five covers remained 390px wide, and browser warnings/errors were empty.
- Diff inspection showed no changes to the Part 3 `修改、建立 AI Skills` area.

Remaining:
- User visual sign-off on the latest Part 2 grouping.
- Local checkpoint commit remains pending until concurrent git activity settles; no staging, commit, or push was performed.

### 2026-08-12 18:29 HKT — Codex — Tightened the 3-1 substage cover section

Summary:
- Treated `抽取官員奏報的事件、官員對事件的回應` like the compact substage cover treatment under `重建通信關係`, removing the extra section padding around the cover.
- Made the 3-1 section's top and bottom borders transparent, kept the cover's existing gradient and typography, and restored flush-left/viewport-edge alignment on desktop and mobile.

Files changed:
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `git diff --check` passed; stylesheet braces remain balanced (`670` opening / `670` closing).
- Browser QA passed at the wide viewport and temporary 390px viewport: the 3-1 cover has zero surrounding section padding, transparent borders, desktop cover bounds left `0` and mobile bounds `0–390`, and browser warnings/errors were empty.

Remaining:
- User visual sign-off on the compact 3-1 cover.
- Local checkpoint commit remains pending until concurrent git activity settles; no staging, commit, or push was performed.

### 2026-08-12 18:26 HKT — Codex — Removed the 02 通信關係複雜 visual

Summary:
- Hid the `02 通信關係複雜` visual beside `辨識奏摺所回應的上諭`.
- Preserved the complete figure markup in a reversible HTML comment.
- Expanded the remaining text-card column across the row so no empty visual column remains.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Confirmed the visual is absent from the rendered DOM and the three related text-card parts remain visible.
- Confirmed the no-visual layout uses one full-width grid column.
- `git diff --check` passed.

Remaining:
- Local checkpoint commit remains pending until the active Git lock is released; nothing was pushed.

### 2026-08-12 18:32 HKT — Codex — Applied compact spacing to all substage cover sections

Summary:
- Extended the compact-cover treatment from `3-1` to all five substage sections: `2-1` 上諭回應、`2-2` 硃批回應、`2-3` 上諭來源、`3-1` 事件抽取及 `3-2` 來源鏈追溯.
- Removed the inherited top and bottom section padding, made each section border transparent, and kept every cover flush with the viewport edge.

Files changed:
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `git diff --check` passed; stylesheet braces remain balanced (`669` opening / `669` closing).
- Browser QA passed at the wide viewport and temporary 390px viewport, including `辨識奏摺所回應的硃批`: all five sections have zero top/bottom padding, transparent borders, covers starting at left `0`, mobile cover widths exactly `390px`, and browser warnings/errors were empty.
- Preserved the concurrent `通信關係複雜` visual removal and other unrelated edits.

Remaining:
- User visual sign-off on the compact substage covers.
- Local checkpoint commit remains pending until concurrent git activity settles; no staging, commit, or push was performed.

### 2026-08-12 18:35 HKT — Codex — Removed remaining substage-cover border lines

Summary:
- Made the border lines on the full-width backdrop pseudo-elements transparent for all five substage sections, in addition to the already transparent section borders.
- Preserved the cover gradients, text, sizing, and viewport-edge alignment.

Files changed:
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `git diff --check` passed; stylesheet braces remain balanced (`670` opening / `670` closing).
- Browser QA confirmed both section borders and backdrop borders compute as transparent for `2-1` through `3-2`; browser warnings/errors were empty.

Remaining:
- User visual sign-off on the borderless substage covers.
- Local checkpoint commit remains pending until concurrent git activity settles; no staging, commit, or push was performed.

### 2026-08-12 18:38 HKT — Codex — Narrowed the 上諭-response text cards

Summary:
- Set the text cards in `辨識奏摺所回應的上諭` to occupy 45vw on wide screens.
- Kept the cards left-aligned and restored the existing full-width card sizing below the narrow-screen breakpoint.

Files changed:
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Scoped the width rule to `#part-2-yu-response` so other Part 2 text cards are unchanged.
- Preserved the reversible hidden `02 通信關係複雜` visual markup.
- Browser QA at a 1280px viewport measured all three cards at 576px (45vw) with the same left edge; the hidden visual count remained zero.
- `git diff --check`, JavaScript syntax validation, and stylesheet brace validation passed.

Remaining:
- Local checkpoint commit remains blocked by the active `.git/index.lock` held by another process; nothing was staged or pushed.

### 2026-08-12 18:45 HKT — Codex — Rebuilt the Part 1 chart dots from the sample backup

Summary:
- Rebuilt the replica chart projection from `/Users/creamybanana/Downloads/sample_all-2.data` and the canonical Stage 1 documents instead of the previous four-placeholder-node fallback.
- Preserved the sample’s dated placement rules: document circles on the official and imperial lines, event squares on the event and emperor lines, same-date horizontal spreading, and stored source/response relationships.
- Kept undated or hidden event records out of the rendered chart, matching the sample renderer’s behavior.
- Updated the replica and StoryMap example cache versions so the rebuilt data and renderer load together.

Files changed:
- `tool/scripts py/build_part1_interface_data.py`
- `Website/storymap/part-1-interface-data.js`
- `Website/storymap/part-1-interface.js`
- `Website/storymap/platform-interface-replica.html`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Generated 363/363 source document records, 513 dated document placements, 210 event squares, 723 chart nodes, and 459 stored chart links.
- JavaScript syntax checks, Python compilation, and `git diff --check` passed.
- Browser QA confirmed a middle document click opens the AI and document panels, while an outer event click opens the 節點資訊區 alongside the existing panels; browser warnings/errors were empty.

Remaining:
- Continue the remaining sample-tool parity work after the dot reconstruction is visually approved.
- Local checkpoint commit remains pending while the active Git lock/concurrent work is present; nothing was staged or pushed.

### 2026-08-12 19:04 HKT — Codex — Opened each clicked document dot in its own document panel

Summary:
- Embedded the full canonical source records for the 363 document IDs represented by chart dots, so the replica can open any selected document without a server-only fetch.
- Changed document-dot clicks to update the right-hand document panel with that dot’s own title, metadata, summary, and original text.
- Removed the hard-coded `AI 官員上奏` / `AI 硃批` output-card fallback from document-dot clicks; the AI panel now shows a neutral selected-document state while event dots retain their existing event output behavior.
- Updated both replica HTML cache versions for the new data and click behavior.

Files changed:
- `tool/scripts py/build_part1_interface_data.py`
- `Website/storymap/part-1-interface-data.js`
- `Website/storymap/part-1-interface.js`
- `Website/storymap/platform-interface-replica.html`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Official dot `doc-奏2-L` opened 奏2’s title and original text; the AI panel contained no `AI 官員上奏` card.
- Imperial dot `doc-硃42-R` opened 硃42’s title and original text; the AI panel contained no generic document-output card.
- An event square still opened 節點資訊區 and kept the existing AI panel behavior.
- The preview rendered 363/363 document records, 513 document circles, and 210 event squares; browser warnings/errors were empty.
- JavaScript syntax checks, Python compilation, and `git diff --check` passed.

Remaining:
- Local checkpoint commit remains pending because concurrent staged/unstaged work is present; nothing was staged or pushed for this change.

### 2026-08-13 14:15 HKT — Codex — Replaced the 上諭-response subsection with the four-bar reference interaction

Summary:
- Removed the former explanatory-card stack and 諭43／硃160 side visual from `辨識奏摺所回應的上諭`.
- Added the four reference bars from `final_out_v2.html`: 引述標記, 上諭發出日期, 上諭引文, and 奏摺作者.
- Preserved the reference content, expanding text cards, Skill typing window, sequential 硃160／諭43 reveals, one-open-bar behavior, responsive stacking, and synchronized clue highlighting.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `Website/storymap/part2-yu-response-bars.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`

Verified:
- Four bars are generated in the target subsection and the former cards/visual are absent there.
- Desktop browser check confirmed the three-window reveal and quote highlighting across all matching marks.
- Narrow browser check at 390px confirmed stacked bars and stacked Skill/document windows.
- Switching bars closes and resets the previous bar; browser error/warning diagnostics were empty.
- JavaScript syntax and `git diff --check` passed; the temporary viewport override was reset.

Remaining:
- Local checkpoint commit remains pending because concurrent staged/unstaged work is present; nothing was staged or pushed.

### 2026-08-19 18:18 HKT — Codex — Refined Layer 2 visual scale, typography, and document chrome

Summary:
- Enlarged the full-width Layer 2 explanations and the 2.1–2.3 visual content typography.
- Added per-visual chart scaling and thicker relationship lines; the 2.2 first relationship is centered on two endpoints so at least two dots remain visible.
- Applied the 2.1 transparent, noninteractive toolbar treatment to all three visuals and removed the document-panel `+`, `−`, and `×` controls.

Files changed:
- `Website/storymap/part-1-interface.js`
- `Website/storymap/part2-yu-response-bars.js`
- `Website/storymap/part2-zhu-response-bars.js`
- `Website/storymap/part2-yu-source-bars.js`
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`

Verified:
- JavaScript syntax checks passed for the interface and all three Layer 2 visual modules.
- `git diff --check` passed.
- Browser QA on the cache-busted local 8761 page confirmed the larger description/content type, chart scales of 1.5× / 1.25× / 1.5× for 2.1 / 2.2 / 2.3, thicker visible lines, at least two visible dots in each visual, transparent toolbars, and hidden document controls.
- Browser QA of 2.2 item 03 confirmed `引號中的硃批文字` uses the enlarged summary, Skill, and highlighted document text.

Remaining:
- The pre-existing concurrent edits in `../PROJECT_LOG.md`, `Website/storymap/part-1-interface.css`, and the untracked review bundles remain untouched; no push was performed.

### 2026-08-13 11:41 HKT — Codex — Enlarged and cleaned the 2-1 evidence visual

Summary:
- Reduced the text column beside `辨識奏摺所回應的上諭`'s 諭43／硃160 visual so the visual can occupy more horizontal space.
- Increased the visual stage height and removed its outer backdrop, border, padding, and shadow.
- Removed the 0px-width 諭43 panel border that created the unwanted straight line through the collapsed visual.

Files changed:
- `Website/storymap/storymap-cards.css`
- `../PROJECT_LOG.md`
- `INTRO_WEBSITE_CHANGE_LOG.md`

Verified:
- Desktop and mobile browser checks passed; the expanded panels retain the intended interaction and no longer show a center divider.
- Browser error and warning logs were empty; `git diff --check` passed.

Remaining:
- Local checkpoint commit remains pending because concurrent staged/unstaged work is present; nothing was staged or pushed for this change.

### 2026-08-13 12:06 HKT — Codex — Restored AI chat 功能 and 設定 controls

Summary:
- Made the AI chat panel’s 功能 menu produce saved-result cards or source-derived summary/section results instead of closing without an action.
- Made AI 設定 fields editable, persisted for the replica, resettable, and usable after a document dot is selected.
- Kept the controls available after saved AI cards replace the panel body.

Files changed:
- `Website/storymap/part-1-interface.js`
- `Website/storymap/part-1-interface.css`
- `Website/storymap/platform-interface-replica.html`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- After selecting 硃42, 功能 → 摘要 rendered a result card and closed the menu.
- 功能 → 全文來源鏈 rendered saved source-chain output when available.
- 設定 opened after document selection; provider selection, model editing, and reset worked.
- `node --check`, `git diff --check`, and browser error/warning checks passed during the focused interaction test.

Remaining:
- A reload-based persistence probe timed out during chart startup; the visible edit/reset interaction and in-page saved state passed.
- Local checkpoint commit remains pending because concurrent staged/unstaged work is present; nothing was staged or pushed for this change.

### 2026-08-13 11:40 HKT — Codex — Cleaned the 上諭-response visual spacing

Summary:
- Removed the full-viewport card-part backdrops in `辨識奏摺所回應的上諭`, eliminating the thin dark edge strips at the left and right.
- Set the section to a clean continuous background.
- Reduced the moved `為奏聞提臣等赴臺並飭沿海官員嚴密巡查事` visual to a responsive 360–560px height so the first text part extends below the visual, matching the intended visual-to-part relationship.
- Bumped the StoryMap CSS cache version so the browser receives the correction.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Fresh browser QA at 1280px: the edge backdrop pseudo-elements are `display: none`; the source visual is 360px high while its first text part is taller; the full section remains taller than the visual.
- The moved source visual remains in grid column 2 / row 1, with its connector line and dot still rendered; the newer evidence visual remains present.
- Fresh browser diagnostics were empty.
- JavaScript syntax, CSS brace balance, and `git diff --check` passed.

Remaining:
- Local checkpoint commit remains pending while concurrent staged/unstaged work is present; nothing was pushed.

### 2026-08-13 11:54 HKT — Codex — Fixed incomplete alternating Part 2 backdrops

Summary:
- Fixed the shared `.part2-card-part` backdrop stacking so each colored band reaches both viewport edges instead of leaving a narrow strip at the left and right.
- Kept the existing alternating backdrop colors for each part.
- Applied the fix consistently to the grouped sections, including `辨識奏摺所回應的硃批` and `辨識奏摺所回應的上諭`.
- Bumped the StoryMap CSS cache version.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Fresh browser QA at 1280px confirmed full-width backdrop geometry with the expected color sequence `#f6f1e8`, `#efe8dc`, `#e8dfd1`, then `#f6f1e8` in the 硃批 section.
- Fresh browser QA confirmed the 上諭-response first text part remains taller than its moved visual.
- No horizontal overflow was introduced; browser diagnostics were empty.
- JavaScript syntax, CSS brace balance, and `git diff --check` passed.

Remaining:
- Local checkpoint commit remains pending while the active Git lock/concurrent staged work is present; nothing was pushed.

### 2026-08-12 19:39 HKT — Codex — Moved the 硃113 visual beside the 上諭-response card

Summary:
- Moved the existing `為奏聞提臣等赴臺並飭沿海官員嚴密巡查事` source-flow visual into `辨識奏摺所回應的上諭`.
- Positioned it in the right column of the first row, beside the `「上諭—回應配對」Skill 會根據以下線索` card.
- Kept the single HTML visual instance in the 硃批 section as the maintenance source and relocate the live node at initialization; the now-empty 硃批 visual column collapses.

Files changed:
- `Website/storymap/storymap.js`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Wide browser QA at 1280px: the visual is in `#part-2-yu-response`, grid column 2 / row 1, with the first text card in the left column; the 硃批 section has no visual and uses one column.
- The moved source-flow visual still rendered its connector lines and dots, and retained its callout behavior.
- JavaScript syntax, CSS brace balance, and `git diff --check` passed.

Remaining:
- Local checkpoint commit remains pending because concurrent staged/unstaged work is present; nothing was staged or pushed.

### 2026-08-12 19:24 HKT — Codex — Restored saved per-document AI chat cards

Summary:
- Projected the saved `chat` histories from `/Users/creamybanana/Downloads/sample_all-2.data` for all 239 chart documents with stored AI output.
- Preserved the saved card fields and card types, including document pairs, extract results, official responses, source traces, and emperor actions.
- Clicking a document dot now opens that document’s saved AI cards in the AI panel; documents without saved output remain empty.
- Kept saved pair evidence and source-chain quotations available in their cards, and updated both replica HTML cache versions.

Files changed:
- `tool/scripts py/build_part1_interface_data.py`
- `Website/storymap/part-1-interface-data.js`
- `Website/storymap/part-1-interface.js`
- `Website/storymap/platform-interface-replica.html`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- 硃42 opened 151 saved AI cards across 133 output turns, including extract, official-response, and document-pair card types with quotations.
- 硃65, which has no saved chat history in the input data, kept an empty AI panel while its document panel opened normally.
- An event square still rendered its content in 節點資訊區.
- The preview rendered 513 document circles and 210 event squares; browser warnings/errors were empty.
- JavaScript syntax checks, Python compilation, and `git diff --check` passed.

Remaining:
- Local checkpoint commit remains pending because concurrent staged/unstaged work is present; nothing was staged or pushed for this change.

### 2026-08-12 19:13 HKT — Codex — Removed document context text from the AI panel

Summary:
- Removed the auto-filled `已開啟文書` title, document ID, and explanatory placeholder from the AI panel after a document-dot click.
- Kept the selected document’s full source text and metadata in the right-hand document panel.

Files changed:
- `Website/storymap/part-1-interface.js`
- `Website/storymap/platform-interface-replica.html`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- After clicking `doc-奏2-L`, the AI body is empty and the document panel still shows 奏2’s original text.
- An event square still renders its content in 節點資訊區.
- JavaScript syntax validation and `git diff --check` passed; browser diagnostics were empty.

Remaining:
- Local checkpoint commit remains pending because concurrent staged/unstaged work is present; nothing was staged or pushed for this change.

### 2026-08-12 19:35 HKT — Codex — Removed saved-chat source chrome

Summary:
- Removed the `AI 輸出來源` header, `.chat` filename, saved-output summary, sample launcher, and load controls from the per-document AI panel.
- Kept each saved turn’s heading, skill/prompt metadata, output cards, quotations, and document-specific results; documents without saved chat remain empty.

Files changed:
- `Website/storymap/part-1-interface.js`
- `Website/storymap/platform-interface-replica.html`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- The replica rendered 513 document circles and 210 event squares after reload.
- 硃42 opened 133 saved turns with 151 cards, with no source header, `.chat` label, launcher, load text, or summary.
- 硃65 opened with an empty AI body and no placeholder text.
- An event square still opened a populated node panel without the source wrapper.
- JavaScript syntax checks, `git diff --check`, and browser error/warning checks passed.

Remaining:
- Local checkpoint commit remains pending because concurrent staged/unstaged work is present; nothing was staged or pushed for this change.

### 2026-08-12 19:43 HKT — Codex — Flattened saved AI output cards

Summary:
- Removed per-turn headings, bundle/run metadata, prompts, and their backdrop containers from the saved AI panel.
- Kept each document’s saved output cards, card-level provenance, quotations, and event-node focus behavior.

Files changed:
- `Website/storymap/part-1-interface.js`
- `Website/storymap/part-1-interface.css`
- `Website/storymap/platform-interface-replica.html`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- 硃42 showed 151 saved cards with zero turn wrappers and no `第…回`, bundle, or `本機技能輸出` text in the AI panel.
- JavaScript syntax checks and `git diff --check` passed.
- Browser error/warning logs were empty.

Remaining:
- Local checkpoint commit remains pending because concurrent staged/unstaged work is present; nothing was staged or pushed for this change.

### 2026-08-13 12:06 HKT — Codex — Added shared doc_panel_sample UI to Part 2 replicas

Summary:
- Added `Website/storymap/doc_panel_sample.html` as a standalone 硃113 document-panel reference, including the title metadata, move/minimize/close controls, filter/settings row, highlighted original text, and working sample controls.
- Applied the same `.source-flow-document`／`.ip` panel structure to the `總結文書` visual and both document panes in the `系統會根據三項條件篩選候選文書` visual, while preserving their existing summary animation and evidence-linking behavior.
- Added panel-specific styling so the two replicas inherit the 硃113 panel proportions, typography, spacing, controls, and fold behavior without changing their content or highlights.

Files changed:
- `Website/storymap/doc_panel_sample.html`
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `Website/storymap/part2-summary-visual.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Standalone sample loaded in the local browser; its fold and filter controls toggled correctly.
- Main-page browser check confirmed the two new document replicas render with the shared panel structure; clicking the first evidence mark still reveals the 諭43 pane and activates its matching target text.
- HTML parsing, JavaScript syntax checks, and `git diff --check` passed. Browser diagnostics were empty before the final CSS-only fold fallback check.

Remaining:
- Local checkpoint commit remains pending because concurrent staged/unstaged work is present; nothing was staged or pushed for this change.
- A final browser control recheck after the CSS fallback timed out while the local preview was transitioning; the fallback itself passed static validation.

### 2026-08-13 12:14 HKT — Codex — Removed the remaining Part 2 backdrop strip

Summary:
- Made the no-visual communication card rows explicitly span the viewport, with a calculated centered-wrapper offset so the card alignment stays unchanged at both standard and wide desktop widths.
- Kept the existing alternating row colors (`#f6f1e8`, `#efe8dc`, `#e8dfd1`, then repeat) and disabled the old pseudo-backdrop only for this no-visual layout.
- Bumped the StoryMap stylesheet cache version so the correction is visible after reload.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Fresh local browser preview showed the alternating rows reaching the left and right viewport edges with no vertical strip; the text cards remained aligned.
- Browser error and warning diagnostics were empty.
- `git diff --check` passed for the edited files.

Remaining:
- Local checkpoint commit remains pending because concurrent staged/unstaged work is present; nothing was pushed.

### 2026-08-13 13:48 HKT — Codex — Copied the 為奏料理撤兵及回省日期事 panel into 2-2

Summary:
- Updated `辨識奏摺所回應的硃批` so its right-side visual slot copies the single document panel titled `為奏料理撤兵及回省日期事` from the 2-1 evidence visual.
- Kept the 諭43 panel and three-condition interaction exclusive to 2-1.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/part2-evidence-visual.js`
- `Website/storymap/storymap-cards.css`
- `../PROJECT_LOG.md`
- `INTRO_WEBSITE_CHANGE_LOG.md`

Verified:
- Browser check confirmed the copied 2-2 panel title and single-panel layout.
- Browser diagnostics were empty; JavaScript syntax and `git diff --check` passed.

Remaining:
- Local checkpoint commit remains pending because concurrent staged/unstaged work is present; nothing was staged or pushed.

### 2026-08-13 13:16 HKT — Codex — Fixed narrow document-panel header stacking

Summary:
- Wrapped the candidate-document title and metadata in the shared `.ip-titles` header container so narrow panels keep the document details below the title instead of placing them in a side column.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- At 390px width, both the 硃160 and 諭43 panels place metadata below their titles with no horizontal overlap.
- Browser error and warning diagnostics were empty; the temporary viewport override was reset.
- HTML parsing, JavaScript syntax checks, and `git diff --check` passed.

Remaining:
- Local checkpoint commit remains pending because concurrent staged/unstaged work is present; nothing was staged or pushed for this change.

### 2026-08-13 13:13 HKT — Codex — Extended the backdrop fix across all grouped Part 2 sections

Summary:
- Replaced the centered pseudo-backdrop for every `part2-card-part` with a real viewport-width row surface, using a calculated offset so each row begins at the viewport edge while its text card keeps the established content alignment.
- Applied the same correction to `辨識奏摺所回應的上諭`, `辨識奏摺所回應的硃批`, `辨識上諭所回應的奏摺`, `抽取官員奏報的事件、官員對事件的回應`, `追溯資訊的來源`, and `收取上諭的資訊`.
- Kept the per-row alternating colors and preserved the right-side visuals above the row surfaces.
- Bumped the StoryMap stylesheet cache version.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Fresh browser geometry check: every affected row spans x=0 to the viewport right edge; cards remain inset and visuals remain visible.
- Verified alternating row colors for all six affected section IDs.
- Browser error and warning diagnostics were empty.
- `git diff --check` passed.

Remaining:
- Local checkpoint commit remains pending because concurrent staged/unstaged work is present; nothing was pushed.

### 2026-08-13 14:30 HKT — Codex — Replaced the 硃批-response subsection with the three-bar reference interaction

Summary:
- Removed the former four explanatory cards and copied communication visual from `辨識奏摺所回應的硃批`.
- Added the three reference bars from `final_out_1.html`: 「奉硃批」等引述標記、同一官員較早發出、引號中的硃批文字.
- Preserved the reference content, Skill typing window, sequential 硃297／硃155 reveals, one-open-bar behavior, synchronized clue highlighting, and responsive stacking.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `Website/storymap/part2-zhu-response-bars.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`

Verified:
- Three bars render in the target subsection; the former cards and copied visual are absent there.
- Desktop browser check confirmed the Skill → 硃297 → 硃155 reveal and matching-clue highlighting.
- Narrow browser check at 390px confirmed stacked bars and stacked document windows.
- Switching bars closes and resets the previous bar; browser error/warning diagnostics were empty.
- JavaScript syntax and `git diff --check` passed; the temporary viewport override was reset.

Remaining:
- Local checkpoint commit remains pending because concurrent staged/unstaged work is present; nothing was staged or pushed.

### 2026-08-13 14:39 HKT — Codex — Restored Part 2 subsection boundaries after the 硃批 three-bar edit

Summary:
- Removed an accidental `</main>` inserted inside the 硃批 subsection, which had closed the Part 2 parent container before 2-3 and made the later cover tabs lose their styling.
- Restored the individual cover-tab rendering for 2-3「辨識上諭所回應的奏摺」and the later 3-1／3-2 subsections without changing the new 硃批 three-bar content.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Desktop browser check confirmed the affected sections remain direct children of `#part-2-content` and each has a visible `.part2-substage-cover`.
- Narrow browser check at 390px confirmed visible full-width cover tabs for 2-3, 3-1, and 3-2; the 2-3 deep link positions its cover below the sticky header.
- Reopened the 硃批 first bar and confirmed its three-bar interaction still opens the Skill window and document panel.
- Browser error and warning diagnostics were empty; `git diff --check` passed.

Remaining:
- Local checkpoint commit remains pending because concurrent staged/unstaged work is present; nothing was staged or pushed.

### 2026-08-13 15:17 HKT — Codex — Replaced 2-3 cards with the final_out_2 常青等 two-bar interaction

Summary:
- Removed all explanatory cards from `辨識上諭所回應的奏摺`.
- Added the requested bars `「據常青等奏」引述標記` and `收發日期・常青等`, using the reference Skill window, 諭13 panel, and three concurrent candidate excerpt panels from `final_out_2.html`.
- Preserved sequential reveal, typing, clue highlighting, one-open-bar behavior, and responsive stacking.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `Website/storymap/part2-yu-source-bars.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`

Verified:
- Two requested bars render and the former 2-3 card stack is absent.
- Desktop browser check confirmed the Skill → 諭13 → three candidate excerpt reveal and synchronized marker/date highlighting.
- Narrow browser check at 390px confirmed the cover tab remains below the sticky header, bars stay within the viewport, and the three candidate panels stack vertically without overflow.
- Browser error and warning diagnostics were empty; JavaScript syntax and `git diff --check` passed; the temporary viewport override was reset.

Remaining:
- Local checkpoint commit remains pending because concurrent staged/unstaged work is present; nothing was staged or pushed.

### 2026-08-13 15:28 HKT — Codex — Removed the communication breadcrumb from Part 2.1–2.3 cover tabs

Summary:
- Removed the `重建通信關係` breadcrumb above the first bar/title area in 2.1 `辨識奏摺所回應的上諭`, 2.2 `辨識奏摺所回應的硃批`, and 2.3 `辨識上諭所回應的奏摺`.
- Kept the section numbers, titles, 2.3 explanatory note, bars, and all reveal interactions unchanged.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Desktop browser check confirmed no breadcrumb remains in the three requested covers and the first bars remain directly below each cover.
- Narrow browser check at 390px confirmed full-width covers, no horizontal overflow, and no browser errors or warnings; the temporary viewport override was reset.
- `git diff --check` passed.

Remaining:
- Local checkpoint commit remains pending because concurrent staged/unstaged work is present; nothing was staged or pushed.

### 2026-08-13 15:32 HKT — Codex — Removed the legend labels above the Part 2.1–2.3 bars

Summary:
- Removed the legend rows above the first bar in 2.1, 2.2, and 2.3, including `引述標記`, `同一官員較早發出`, and `硃批引文` in the 硃批 subsection.
- Preserved every numbered bar, document panel, and interaction effect.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Desktop and 390px browser checks confirmed zero legend rows in the three requested subsections and no empty gap before the first bar.
- Narrow layout retained full-width covers and no horizontal overflow; browser error and warning diagnostics were empty.
- `git diff --check` passed; the temporary viewport override was reset.

Remaining:
- Local checkpoint commit remains pending because concurrent staged/unstaged work is present; nothing was staged or pushed.
### 2026-08-13 15:15 HKT — Codex — Removed the four evidence bars from the 上諭-response subsection

Summary:
- Removed the `引述標記`, `上諭發出日期`, `上諭引文`, and `奏摺作者` accordion bars from `辨識奏摺所回應的上諭`.
- Restored the subsection's three explanatory text cards and its right-side 諭43／硃160 evidence visual.
- Left the 硃批-response and 上諭-source subsections unchanged.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser DOM check confirmed three text-card parts, zero 2-1 request bars, and one right-side evidence visual titled `為奏料理撤兵及回省日期事`.
- Browser error and warning diagnostics were empty.
- JavaScript syntax and `git diff --check` passed.

Remaining:
- Local checkpoint commit remains pending because concurrent staged/unstaged work is present; nothing was staged or pushed.
### 2026-08-13 15:27 HKT — Codex — Restored the four evidence bars in the 上諭-response subsection

Summary:
- Restored the four bars `引述標記`, `上諭發出日期`, `上諭引文`, and `奏摺作者` in `辨識奏摺所回應的上諭`.
- Restored the `part2-yu-response-bars.js` script include and kept the subsection boundary separate from the following sections.

Files changed:
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser DOM check confirmed exactly four 2-1 bars and no nested later sections.
- Browser error and warning diagnostics were empty.
- JavaScript syntax and `git diff --check` passed.

Remaining:
- Local checkpoint commit remains pending because concurrent staged/unstaged work is present; nothing was staged or pushed.

### 2026-08-13 15:28 HKT — Codex — Tuned the 2-2 three-window bar layout

Summary:
- Added breathing room below the final bar in `辨識奏摺所回應的硃批` and reduced the gap between its three bars.
- Increased the height of the three revealed windows and enlarged their Skill/document text; the mobile window override now uses the larger height as well.
- Removed the `Visual Studio Code —` prefix from all three 2-2 Skill window titles.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`

Verified:
- Fresh desktop browser check confirmed 14px bar spacing, 102.4px bottom padding, three 480px-high windows, enlarged computed fonts, and the exact title `zhu-response-pairing.md` in all three windows.
- Browser error and warning diagnostics were empty; JavaScript syntax and `git diff --check` passed.

Remaining:
- Local checkpoint commit remains pending because the repository has concurrent staged/unstaged work and an active Git lock; nothing was pushed.

### 2026-08-13 16:01 HKT — Codex — Applied the final_out_4 UI style to Part 2.1–2.3

Summary:
- Added the shared final_out_4 waiting state: narrow request bars remain on the left while a large Skill preview window sits on the right and fades out when a bar opens.
- Matched the reference visual treatment for all three subsections with the same card overflow behavior, stage divider, visual padding, Skill-window transition, shadows, and responsive hiding of the idle preview.
- Removed the `Visual Studio Code —` prefix from the revealed 2-1 and 2-3 Skill window titles so all revealed request windows use the same filename-only treatment; the new idle preview keeps the reference titlebar wording.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap-example.html`
- `Website/storymap/part2-req-ui-style.js`
- `Website/storymap/part2-yu-response-bars.js`
- `Website/storymap/part2-yu-source-bars.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Desktop browser check confirmed idle Skill previews for 2-1, 2-2, and 2-3; 4, 3, and 2 request bars respectively; matching 16px 18px 20px visual padding; and the preserved 2-2 14px gap, 480px stage, 14px Skill text, and 16px document text.
- Open/close checks confirmed the idle preview hides while a bar is open, the card expands and stage reveals, then the idle preview returns after closing.
- Mobile viewport check confirmed the idle preview is hidden and the stacked windows retain their section-specific heights.
- Browser diagnostics were empty; JavaScript syntax and `git diff --check` passed.

Remaining:
- Local checkpoint commit remains pending because the repository has concurrent staged/unstaged work and an active Git lock; nothing was staged or pushed.

### 2026-08-13 16:31 HKT — Claude — Merged the 2-1/2-2/2-3 visual stage into the request card and synced the idle-to-active Skill-window handoff with the card-open animation

Summary:
- Nested `.req-stage-wrap` inside `.req-card` (previously a sibling below it) for all request items in `辨識奏摺所回應的上諭` (2-1, JS-built), `辨識奏摺所回應的硃批` (2-2, static markup), and `辨識上諭所回應的奏摺` (2-3, JS-built) so the revealed three/four-window stage now expands as part of the card itself, matching the already-shared idle-Skill-preview CSS (`overflow: visible` on open cards, stage-wrap top divider, Skill-window scale(1.28→1)) that was already in `storymap-cards.css` but had no matching DOM nesting to act on.
- Changed each section's `openItem`/`open` function so the card's width-open animation, the stage-wrap's reveal, and the idle-big-Skill-window → this-row's-small-Skill-window handoff now start in the same click, instead of the handoff being delayed until after the width, panel, word-card, and stage-wrap steps had already run in sequence (previously ~1.4s after click). The word-card text still fades in on its original timing, just no longer gating the visual stage.
- No CSS changes were needed — `storymap-cards.css` already carried the merged-card rules from the prior `final_out_4` pass; this change only supplies the matching HTML/JS structure.
- No source document text, citations, dates, or translations were touched — layout/timing only.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/part2-yu-response-bars.js`
- `Website/storymap/part2-zhu-response-bars.js`
- `Website/storymap/part2-yu-source-bars.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Built a standalone Playwright test harness (sandboxed copy, not on the repo) loading the real `storymap-cards.css` plus the three edited `part2-*-bars.js` files and the restructured 2-1/2-2/2-3 markup; confirmed 4/3/2 request bars render for 2-1/2-2/2-3 respectively.
- Confirmed via computed-style sampling at 60ms/120ms/250ms after click that the card width and the row's Skill-window opacity/scale now animate together from click time (previously the Skill window stayed at opacity 0 until ~1.4s in).
- Screenshotted each section's open state: 2-1 (4-window layout), 2-2 (3-window layout), 2-3 (docstack with 3 candidate 硃批 cards) all render merged into the card with no clipping.
- Checked a 720px-wide viewport: idle Skill preview correctly hidden below 860px, stacked single-column layout intact, no console/page errors across open/close/switch cycles.
- `node --check` passed on all three edited `.js` files; a custom Python HTML-tag-balance checker confirmed the restructured `storymap-example.html` has the same (pre-existing, unrelated) tag-balance signature as the original file, i.e. no new imbalance introduced.
- Verified via `device_list_dir` that none of the four target files changed on disk between staging and write-back (no mtime drift), so the commit could not have overwritten concurrent edits; `device_commit_files` reported all four writes succeeded with none rejected.

Remaining:
- Per user instruction this run did not touch git (repo currently has a large amount of unrelated concurrent staged/unstaged work and what look like active lock files from another agent session); the four files above are written to disk but not staged or committed. A local `git add`/`git commit` covering only these four files, plus this log update, is the next step whenever the concurrent git state is clear.
- The reference `final_out.html` draft used to derive this change lived in the assistant's session workspace only (not in this repo).

### 2026-08-13 16:40 HKT — Codex — Added vertical section space and manual request-card sizing controls

Summary:
- Reserved the full height of the idle Skill preview inside each 2-1–2-3 section so it no longer overlaps the following cover tab.
- Added responsive top and bottom spacing around each section's request-card area, keeping bars and windows separated from adjacent cover tabs.
- Added grouped CSS variables for folded-card width, expanded-card width, folded Skill-window height, expanded window height, expanded Skill/document grid proportions, and section spacing.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Desktop browser geometry confirmed 38.4px top spacing and 64px bottom spacing for all three sections; idle preview height is reserved in the section flow.
- Expanded checks confirmed 2-1 uses a 360px stage, 2-2 retains its 480px stage, and 2-3 uses its wider document-stack columns without overlap.
- Mobile check confirmed 24px/48px section spacing, hidden idle previews, and stacked responsive windows.
- Browser diagnostics were empty; JavaScript syntax and `git diff --check` passed.

Remaining:
- Local checkpoint commit remains pending because concurrent staged/unstaged work and an active Git lock are present; nothing was staged or pushed.

### 2026-08-13 17:04 HKT — Codex — Expanded the concise Traditional-Chinese Skills

Summary:
- Made the shortened Skill descriptions in 2-1, 2-2, and 2-3 slightly longer by restoring the key matching conditions without returning to the original long English wording.
- Kept the existing Traditional-Chinese labels and evidence-highlight groups intact, including date, quotation, author, source, and same-official clues.

Files changed:
- `Website/storymap/part2-yu-response-bars.js`
- `Website/storymap/part2-yu-source-bars.js`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser DOM check confirmed the updated Skill bodies across 2-1, 2-2, and 2-3, with all nine idle previews using the updated Traditional-Chinese text and no browser diagnostics.
- JavaScript syntax, `git diff --check`, and the existing page structure checks passed.

Remaining:
- Local checkpoint commit remains pending because concurrent staged/unstaged work and an active Git lock are present; nothing was staged or pushed.

### 2026-08-13 16:46 HKT — Codex — Enlarged the 2.1–2.3 request-card windows and typography

Summary:
- Increased the expanded Skill/document stage height to 480px as the shared baseline for 2-1, 2-2, and 2-3.
- Enlarged the Skill body to 14px, document titles to 17px, metadata to 13px, and document body text to 16px.
- Enlarged the 2-3 stacked candidate-panel typography and set the mobile revealed windows to 360px while retaining the stacked doc layout.
- Added the typography values to the existing manual request-card CSS controls.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser checks confirmed 480px expanded stages and the requested larger text across 2-1, 2-2, and 2-3.
- The 2-3 document stack retained its three-panel layout and readable scrollable content after the typography increase.
- Mobile checks confirmed 360px revealed windows and no console diagnostics.
- JavaScript syntax and `git diff --check` passed.

Remaining:
- Local checkpoint commit remains pending because concurrent staged/unstaged work and an active Git lock are present; nothing was staged or pushed.

### 2026-08-13 16:51 HKT — Codex — Reduced the out-of-card VS Code preview

Summary:
- Reduced only the idle Skill preview that sits outside the expanded text card: its desktop height is now `clamp(320px, 44vh, 440px)` and its width is limited to `min(72%, 900px)`.
- Kept the expanded in-card windows at the larger 480px height and 14px Skill typography.
- Exposed the folded preview width beside the existing folded preview height in the manual request-card sizing controls.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser geometry confirmed the out-of-card preview is 320px high and 858.9px wide at the desktop test viewport across 2-1, 2-2, and 2-3.
- Expanded 2-1 verification confirmed the in-card Skill window remains 480px high with 14px text.
- Browser diagnostics were empty; JavaScript syntax and `git diff --check` passed.

Remaining:
- Local checkpoint commit remains pending because concurrent staged/unstaged work and an active Git lock are present; nothing was staged or pushed.

### 2026-08-13 16:59 HKT — Codex — Shortened and translated the 2.1–2.3 Skills

Summary:
- Replaced the long English Skill snippets in 2-1, 2-2, and 2-3 with concise Traditional Chinese instructions.
- Preserved each clue's highlighting group so the matching evidence continues to illuminate in the document windows.
- Changed the generated idle-preview heading to `# AI 技能：` while keeping the filename tabs intact.

Files changed:
- `Website/storymap/part2-yu-response-bars.js`
- `Website/storymap/part2-zhu-response-bars.js`
- `Website/storymap/part2-yu-source-bars.js`
- `Website/storymap/part2-req-ui-style.js`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser DOM check confirmed all 2-1/2-2/2-3 Skill bodies are concise Traditional Chinese and the three idle previews use the translated heading.
- JavaScript syntax, `git diff --check`, and browser diagnostics passed.

Remaining:
- Local checkpoint commit remains pending because concurrent staged/unstaged work and an active Git lock are present; nothing was staged or pushed.

### 2026-08-13 17:41 HKT — Codex — Refined Layer 2 cover labels and Skill-window UI

Summary:
- Changed the Layer 2 cover labels to `2.1`, `2.2`, and `2.3`, removing the old `之一`/`之二`/`之三` suffixes.
- Added full-width Traditional Chinese explanations beneath each Layer 2 cover and before its expandable Skill bars.
- Made folded bars fit their complete titles, enlarged the VS Code title/activity UI, and made the idle Skill previews fit their text.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `Website/storymap/part2-req-ui-style.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser checks confirmed the new numbering, full-width explanations, title-sized folded bars, content-fit previews, expanded 2.1 window sizing, and no browser warnings or errors.
- JavaScript syntax checks and `git diff --check` passed.

Remaining:
- Local checkpoint commit remains pending because concurrent staged/unstaged work and an active Git lock are present; nothing was staged or pushed.
### 2026-08-13 17:48 HKT — Codex — Rebalanced the 2-3 source-matching visual

Summary:
- Changed the three source-matching windows in `辨識上諭所回應的奏摺` to 25% / 25% / 50% from left to right.
- Increased the desktop visual stage height and made the three candidate panels in the third window content-fit, so each complete excerpt is visible without an internal text clip.
- Kept the responsive mobile stacking rules unchanged.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/part2-yu-source-bars.js`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser geometry check measured 269.742px / 269.742px / 539.484px at a 1155px visual width, which is exactly 25% / 25% / 50% after the fixed connectors.
- Both 2-3 bars used the updated layout; all three candidate panels had equal scroll and content heights, so their excerpts were fully visible.
- Browser error and warning diagnostics were empty.
- JavaScript syntax and `git diff --check` passed.

Remaining:
- Local checkpoint commit remains pending because concurrent staged/unstaged work is present; nothing was staged or pushed.

### 2026-08-13 17:49 HKT — Codex — Applied the sample document panel to Layer 2.1–2.3

Summary:
- Added the shared `doc_panel_sample.html`-based document-panel structure to all document windows in `辨識奏摺所回應的上諭`, `辨識奏摺所回應的硃批`, and `辨識上諭所回應的奏摺`.
- Standardized the visible metadata dates into compact two-line header rows, including `乾隆52年1月26日發出` and `乾隆52年2月14日硃批` for the requested 2.1 panel.
- Made each opened panel focus its matching highlighted excerpt in the scrollable text pane and replaced the previous muted highlight treatment with a more colourful, evidence-specific palette.
- Bound the sample panel controls recursively so the candidate document panels in 2.3 use the same UI and interactions.

Files changed:
- `Website/storymap/part2-doc-panel.js`
- `Website/storymap/part2-yu-response-bars.js`
- `Website/storymap/part2-zhu-response-bars.js`
- `Website/storymap/part2-yu-source-bars.js`
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- JavaScript syntax checks and `git diff --check` passed.
- Local browser QA confirmed the sample panel anatomy, metadata rows, colourful marks, and automatic excerpt positioning in 2.1; 2.3 confirmed six candidate mini-panels with the same sample structure and working controls.
- Browser diagnostics were empty. The narrow DOM pass reported no horizontal overflow.

Remaining:
- Local checkpoint commit remains pending because concurrent staged/unstaged work is present; nothing was staged or pushed.
### 2026-08-13 17:56 HKT — Codex — Equalized and corrected the 2-3 source-matching highlights

Summary:
- Changed the three source-matching windows in `辨識上諭所回應的奏摺` to equal 33% / 33% / 33% widths.
- Increased the excerpt text in the third candidate-document window to 15px with a readable line height.
- In `02 收發日期・常青等`, added the 硃批 date highlight to all three candidate panels.
- Removed the highlight marker from `又據徐嗣曾由六百里馳奏`, so neither `「據常青等奏」引述標記` nor `收發日期・常青等` can highlight it.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/part2-yu-source-bars.js`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser geometry check measured equal 359.656px / 359.656px / 359.656px windows after the fixed connectors.
- The candidate excerpt font computed to 15px.
- The first bar had no active `又據徐嗣曾由六百里馳奏` mark; the second bar highlighted all three `乾隆51年12月27日` 硃批 dates and no unwanted mark.
- Browser error and warning diagnostics were empty; JavaScript syntax and `git diff --check` passed.

Remaining:
- Local checkpoint commit remains pending because concurrent staged/unstaged work is present; nothing was staged or pushed.

### 2026-08-13 17:56 HKT — Codex — Enlarged Layer 2 explanations and narrowed requirement highlights

Summary:
- Increased the full-width explanatory paragraph before each Layer 2 expandable-bar set so the purpose and method of each part are easier to read.
- Made source-document highlights active-only: the selected bar now highlights only its matching evidence group, while quotation, date, author, and other non-selected groups remain unhighlighted.
- Narrowed the 2.1 Skill description highlight to `「奉上諭」` rather than the surrounding explanation text.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/part2-yu-response-bars.js`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser QA measured the new Layer 2 explanation paragraph at 20.48px at the test viewport.
- Browser QA confirmed the 2.1 marker bar highlights marker evidence only; quotation, date, and author marks remain transparent. The same active-only behavior was confirmed in 2.2 and 2.3.
- Browser diagnostics were empty; JavaScript syntax checks and `git diff --check` passed.

Remaining:
- Local checkpoint commit remains pending because concurrent staged/unstaged work is present; nothing was staged or pushed.

### 2026-08-13 18:08 HKT — Codex — Removed highlight borders from Part 2 document marks

Summary:
- Removed the colored outline and box-shadow border from all active highlights in the Part 2 document panels.
- Kept the highlight fill colors and the existing highlight animation.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser checks for both `「據常青等奏」引述標記` and `收發日期・常青等` reported `box-shadow: none` and no visible outline for every active mark.
- Browser error and warning diagnostics were empty.
- `git diff --check` passed.

Remaining:
- Local checkpoint commit remains pending because concurrent staged/unstaged work is present; nothing was staged or pushed.

### 2026-08-13 18:09 HKT — Codex — Moved Layer 2 explanations into the cover tabs

Summary:
- Moved the explanatory text for 2.1, 2.2, and 2.3 directly beneath each cover-tab subtitle instead of leaving it below the cover.
- Used the requested 2.1 wording beginning `一種深層的通信關係是：有些奏摺會回應官員收到的上諭。` and kept the corresponding matching explanations for the 硃批 and 上諭來源 stages.
- Increased the cover-tab vertical padding and enlarged the explanation text so the subtitle area has more height and reads as part of the cover.

Files changed:
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-cards.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser QA confirmed all three descriptions are inside their cover tabs, directly below the titles, at 18.56px on desktop and 17.16px on the 390px narrow viewport.
- Narrow-layout QA reported no horizontal overflow; browser diagnostics were empty.
- `git diff --check` passed.

Remaining:
- Local checkpoint commit remains pending because concurrent staged/unstaged work is present; nothing was staged or pushed.

### 2026-08-13 18:14 HKT — Codex — Centered the 2.3 source flow and removed the duplicate third candidate title

Summary:
- Removed the `硃 為奏彰化失陷已調兵赴臺事` title row from the third candidate window in 2.3 while retaining its metadata and excerpt.
- Constrained the desktop 2.3 flow to a centered 1120px composition so the three main windows and their arrows sit centrally within the visual.
- Bumped the stylesheet cache version for the layout change.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser QA measured the centered 2.3 stage at x=80px, width=1120px, with the three main windows at equal 348px widths and both arrows inside the centered composition.
- Browser QA confirmed the third candidate `.m1` title row is hidden while the other candidate headers remain visible.
- Browser diagnostics were empty; JavaScript syntax checks and `git diff --check` passed.

Remaining:
- Local checkpoint commit remains pending because concurrent staged/unstaged work is present; nothing was staged or pushed.

### 2026-08-13 18:23 HKT — Codex — Removed the third 2.3 candidate panel and equalized the three-window flow

Summary:
- Removed the entire `硃25` candidate panel for `為奏彰化失陷已調兵赴臺事` from 2.3.
- Kept the three main windows—Skill, 上諭, and the remaining candidate-document group—at equal widths and centered them across a 1120px desktop stage, approximately 94% of the text-card width.
- Updated the stylesheet cache version.

Files changed:
- `Website/storymap/part2-yu-source-bars.js`
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser QA found two remaining candidate panels, no `硃25` title/panel, three main window widths of 348px, and a centered stage at x=80px with width 1120px.
- Browser diagnostics were empty; JavaScript syntax checks and `git diff --check` passed.

Remaining:
- Local checkpoint commit remains pending because concurrent staged/unstaged work is present; nothing was staged or pushed.

### 2026-08-13 18:28 HKT — Codex — Filled the 2.3 visual width and vertically centered the three windows

Summary:
- Expanded the 2.3 desktop stage to the full available inner text-card width instead of the earlier fixed 1120px cap.
- Vertically centered the shorter Skill and 上諭 windows against the taller remaining candidate-document group, so the three main windows share the same y-axis center.
- Updated the stylesheet cache version.

Files changed:
- `Website/storymap/storymap-cards.css`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser QA measured a 1154.97px stage inside a 1192.97px text card (96.8% width), three equal 359.66px windows, and identical vertical centers at y=904.71px.
- Browser diagnostics were empty; JavaScript syntax checks and `git diff --check` passed.

Remaining:
- Local checkpoint commit remains pending because concurrent staged/unstaged work is present; nothing was staged or pushed.

### 2026-08-15 14:30 HKT — Codex — Added 50% Skill window alongside text panel in 2.1 description card

Summary:
- Upgraded the 2.1 (辨識奏摺所回應的上諭) description card below the visual to a side-by-side 50%/50% split layout.
- Left 50% displays the requirement summary text, and right 50% displays an equal-height VS Code-styled Skill window showing concise `yu-response-pairing.md` rules without vertical scrollbars.
- Highlighted corresponding rules for each of the four clues (引述標記, 發出日期, 上諭引文, 奏摺作者) matching the active requirement.
- Synchronized requirement switching across arrows, bubbles, and document mark clicks.

Files changed:
- `Website/storymap/part2-yu-response-bars.js`
- `Website/storymap/storymap-2-1-yu-response-skills-sample.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check` passed for `part2-yu-response-bars.js`.
- `git diff --check` passed without formatting or syntax errors.

Remaining:
- Continue human review and testing in browser.

### 2026-08-15 16:00 HKT — opencode — 2-1 chart: hidden emperor-action to official-document links

Summary:
- Filtered out the 55 purple lines connecting emperor actions on lane 4 to official memorial documents on lane 2 in `part2-yu-response-bars.js` (and `storymap-2-1-yu-response-draft-v8.html`).
- Retained the remaining 65 emperor-action lines connecting emperor action squares directly to their source `shangyu` decree dots on lane 3.
- Total background links on 2.1 chart refined to 380 links + 1 foreground example link (`諭43` ↔ `硃160`).

Files changed:
- `Website/storymap/part2-yu-response-bars.js`
- `Website/storymap/storymap-2-1-yu-response-draft-v8.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check` passed on `part2-yu-response-bars.js`.
- Python verification confirmed exactly 55 emperor-to-official links dropped and 380 background links remain.

Remaining:
- Visual validation in browser.



### 2026-08-15 15:00 HKT — Codex — Expanded Top and Bottom Breathing Room in 2.1 Skill Window

Summary:
- Set `.req-skill-body` to unconstrained natural expansion (`overflow: visible !important`, `min-height: max-content`, `flex: 1 1 auto`) to ensure the entire Skill text is always fully visible with zero scrolling and zero clipping.
- Increased top and bottom padding of `.req-skill-body` to `18px 18px 20px` for generous vertical breathing space around the Skill content.
- Adjusted `.req-desc-body` padding to `16px 20px 18px` and `.req-skill-activitybar` padding to `16px 0`.
- Expanded row margins and leading line spacing to enhance readability.

Files changed:
- `Website/storymap/part2-yu-response-bars.js`
- `Website/storymap/storymap-2-1-yu-response-skills-sample.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check` passed for `part2-yu-response-bars.js`.
- `git diff --check` passed without formatting errors.

Remaining:
- Browser validation.

### 2026-08-15 15:15 HKT — Codex — Focused Key Response Text in Left Document Panel (硃160)

Summary:
- Emphasized the core response quotation (`同日，接奉廷寄...欽此。`) in the left document panel with 100% opacity and clear contrast (`.doc-focus`).
- Dimmed the preceding and following non-key context text on the left panel to `opacity: 0.35` (`.doc-dim`) with hover reveal to make the relevant response text instantly visible.

Files changed:
- `Website/storymap/part2-yu-response-bars.js`
- `Website/storymap/storymap-2-1-yu-response-skills-sample.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check` passed for `part2-yu-response-bars.js`.
- `git diff --check` passed without formatting errors.

Remaining:
- Browser validation.

### 2026-08-15 15:30 HKT — Codex — Made Highlighted Text Normal When Active on Left Panel

Summary:
- Ensured all highlighted text and active clue marks (including author `孫士毅` and `.doc-author-lead`) switch to normal full opacity (`100%`) when active or highlighted.
- Retained context dimming (`opacity: 0.35`) for non-active background text while guaranteeing zero transparency on any active clue element.

Files changed:
- `Website/storymap/part2-yu-response-bars.js`
- `Website/storymap/storymap-2-1-yu-response-skills-sample.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check` passed for `part2-yu-response-bars.js`.
- `git diff --check` passed without formatting errors.

Remaining:
- Browser validation.

### 2026-08-15 16:00 HKT — Codex — Added 3-Way Width Changer to 2.3, Chart Centering on Example Chains, and Dock Edge Resizer

Summary:
- Removed the 50% width limit on document panel docks, allowing dragging up to 100% full visual width (`--stage-dock-pct`).
- Set default dock widths: 50% for 2.1 and 2.2, and 70% for 2.3 (3 document panels).
- Added left dock edge resizer handle (`.part1-stage-resize[data-stage-dock-resize]`) allowing smooth dragging between the timeline chart and the document dock.
- Added 3-way draggable resizers (`inject3WayResizers`) between the 3 document panels in 2.3 (`諭13`, `硃21`, `硃22`).
- Synchronized background nodes and background links in 2.2 and 2.3 to match 2.1's exact background dataset (filtered non-example blue circles, preserved all background timeline links with `opacity: 0.22`, and overlaid prominent foreground active links).
- Configured automated chart viewport centering (`centerPairLine()`) across 2.1, 2.2, and 2.3 to focus directly on each stage's active example line chain.
- Fixed `renderAiIdle` imperial edict date field access in `part-1-interface.js`.

Files changed:
- `Website/storymap/part-1-interface.js`
- `Website/storymap/part-1-interface.css`
- `Website/storymap/part2-yu-response-bars.js`
- `Website/storymap/part2-zhu-response-bars.js`
- `Website/storymap/part2-yu-source-bars.js`
- `Website/storymap/storymap-example.html`
- `Website/storymap/storymap-part2-complete-sample.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check` passed for `part-1-interface.js`, `part2-yu-response-bars.js`, `part2-zhu-response-bars.js`, and `part2-yu-source-bars.js`.
- `git diff --check` passed cleanly.

Remaining:
- Browser QA validation.

### 2026-08-19 18:14 HKT — Codex — Standardized Layer 2 document metadata

Summary:
- Read the latest project commit `e78e659` and updated the document-panel metadata used by the 2.1–2.3 workflow visuals.
- Removed visible document IDs from the workflow pair panels and normalized the 上諭 source to `《天地會》` without the duplicated `天地會` prefix, volume, page, or ID.
- Changed the 2.3 上諭 date to `乾隆51年12月12日下旨`.
- Standardized 奏摺 metadata dates to two lines: `乾隆51年12月12日上奏` / `乾隆51年12月27日硃批` (and the corresponding dates for the other panels), removing the arrow format.
- Removed IDs from the narrow candidate labels, leaving `正文` and `引文摘錄`.

Files changed:
- `Website/storymap/part-1-interface.js`
- `Website/storymap/part2-doc-panel.js`
- `Website/storymap/part2-yu-response-bars.js`
- `Website/storymap/part2-zhu-response-bars.js`
- `Website/storymap/part2-yu-source-bars.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser QA on the local 8761 page confirmed the updated metadata across 2.1, 2.2, and 2.3; no old arrows, `諭13`/`硃21`/`硃22` IDs, or duplicated `天地會 《天地會》1` source text remain in the workflow pair panels.
- The 390px narrow pass confirmed the requested 2.3 metadata and ID-free labels with no horizontal overflow; browser diagnostics were empty.
- JavaScript syntax checks and `git diff --check` passed.

Remaining:
- Local checkpoint commit remains pending because concurrent staged/unstaged work is present; nothing was staged or pushed.

### 2026-08-19 18:17 HKT — Codex — Removed the pair-visual 1:1 dock ceiling

Summary:
- Updated the shared pair-document layout used by the 2.1, 2.2, and 2.3 workflow visuals so the document dock can expand to 100% of the visual width while the chart remains independently resizable.
- Made the dock backdrop belong to the live document column and its document stack, so it follows the dock width instead of reading as a fixed-width background.
- Added explicit 0–100% resize semantics and keyboard endpoints to the chart/document separator; refreshed the CSS and JavaScript cache-busters on the StoryMap page.

Files changed:
- `Website/storymap/part-1-interface.css`
- `Website/storymap/part-1-interface.js`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check` passed for the shared interface and all three workflow visual scripts.
- `git diff --check` passed.
- Browser QA on the local 8761 page at a 1280px desktop viewport reached an exact `100.00%` document dock in 2.1, 2.2, and 2.3; each dock matched its document-stack width, and 2.3 retained all three document panels inside the expanded dock.
- Fresh-load checks confirmed the default proportions remain 50% / 50% for 2.1 and 2.2, 30% / 70% for 2.3, and the surrounding stage-3 visual layouts still render without a fixed visual max-width or browser diagnostics.

Remaining:
- The side-by-side pair resize control intentionally switches to the existing stacked layout at the mobile breakpoint (900px and below).

### 2026-08-19 18:22 HKT — Codex — Aligned 2.3 source-clue labels and numbered highlights

Summary:
- Read the latest project commit `e78e659` and aligned the 2.3 `平台運作流程` source-clue labels with the 2.1/2 treatment: `「據⋯⋯奏」引述標記` and `收發日期`.
- Fixed the 2.3 desktop clue index circles, floating clue badge, and Skill highlight colour references to the existing 2.3 source palette, so the numbered labels are visibly rendered and the selected document text/highlight label changes with the active clue.

Files changed:
- `Website/storymap/part2-yu-source-bars.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check` passed for `part2-yu-source-bars.js`, `part2-doc-panel.js`, and `part-1-interface.js`; `git diff --check` passed.
- Browser QA on local `http://127.0.0.1:8765`: 2.3 clue 1 showed circle `1` and `「據⋯⋯奏」引述標記`; advancing showed circle `2`, `收發日期`, blue date circle/badge, active date marks, and the matching Skill highlight.
- The 2.1 reference retained its existing numbered treatment; the 390×844 pass showed both exact 2.3 labels without horizontal overflow; browser diagnostics were empty.

Remaining:
- Local checkpoint commit is isolated to the requested source-clue patch where possible; unrelated concurrent changes remain unstaged and no push was performed.

### 2026-08-19 18:32 HKT — Codex — Expanded the 2.3 硃 source panels to full text

Summary:
- Replaced the short teaching excerpts in the 2.3 `辨識上諭所回應的奏摺` visual with the full canonical bodies for 硃21 and 硃22.
- Preserved the existing source excerpts as `markerA` highlights under `「據⋯⋯奏」引述標記`, including the requested `十一月二十七夜……不能前進` passage in the 硃21 panel.
- Removed highlight box shadows so the fill has no coloured border, and kept the date highlight in each 硃 panel.

Files changed:
- `Website/storymap/part2-yu-source-bars.js`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check Website/storymap/part2-yu-source-bars.js` passed.
- `git diff --check` passed.
- Browser QA on local 8761 confirmed full body text in both 硃 panels: 硃21 length 877 with 5 source highlights, and 硃22 length 795 with 4 source highlights; the body client and scroll heights match, and active highlights have no box shadow.
- Browser diagnostics were empty.

Remaining:
- No further 2.3 source-panel changes are pending for this request; concurrent work remains unstaged and no push was performed.

### 2026-08-19 18:34 HKT — Codex — Unified highlight-card typography across Layer 2

Summary:
- Reduced the 2.1 highlight-card title to match its explanation text.
- Unified the highlight-card title and explanation to 18px in 2.1, 2.2, and 2.3, using the shared site font scale.
- Refreshed the three Layer 2 visual script cache-busters so the typography change loads on a fresh page.

Files changed:
- `Website/storymap/part2-yu-response-bars.js`
- `Website/storymap/part2-zhu-response-bars.js`
- `Website/storymap/part2-yu-source-bars.js`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`

Verified:
- JavaScript syntax checks passed for all three Layer 2 visual modules.
- `git diff --check` passed.
- Browser QA on the local 8761 page reported 18px for both the highlight title and explanation in 2.1, 2.2, and 2.3; line height is consistent and browser diagnostics were empty.

Remaining:
- Existing concurrent edits and untracked review bundles remain untouched; no checkpoint commit or push was performed.

### 2026-08-19 18:46 HKT — Codex — Matched the 2.3 收發日期 label and circle to the yellow highlight

Summary:
- Changed the 2.3 date colour token to the same yellow used by the active `收發日期` text highlight.
- Matched the active `收發日期` label and number circle to that yellow, with dark text for contrast; the date Skill mark and floating number now use the same token as well.
- Refreshed the 2.3 source-visual cache-buster.

Files changed:
- `Website/storymap/part2-yu-source-bars.js`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check Website/storymap/part2-yu-source-bars.js` passed.
- `git diff --check` passed.
- Browser QA on local 8761 confirmed the active `收發日期` label, circle, document highlight, Skill mark, and floating number all use `rgb(255, 214, 68)`; browser diagnostics were empty.

Remaining:
- Existing concurrent edits and untracked review bundles remain untouched; no checkpoint commit or push was performed.

### 2026-08-20 13:31 HKT — Codex — Built the standalone OCR teaching website

Summary:
- Added an individual `ocr/` teaching page for `OCR 並結構化原始史料`, carrying the eleven-step learning route from OCR basics through the guided exercise.
- Added source-grounded OCR image flows, PaddleOCR and scanner references, an Agentic AI setup demonstration, printed/handwritten layout explorers, a five-page batch-test simulation, and a guided prompt exercise.
- Added the current interactive JSON field viewer, including field navigation, highlighted JSON lines, source/date/硃批 fields, and the explicit AI-candidate versus researcher-verification distinction that is absent from the current live page.

Files changed:
- `Website/ocr/index.html`
- `Website/ocr/ocr.css`
- `Website/ocr/ocr.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check Website/ocr/ocr.js` passed.
- `git diff --check` passed.
- Browser preview at `http://127.0.0.1:8765/intro%20Website/Website/ocr/` loaded at 1280px with no console errors or warnings.
- JSON field selection, Agentic AI demonstration, five-page test simulation, guided exercise completion, handwritten-mode switching, and the 390×844 responsive layout were checked; the mobile document width remained 390px with no horizontal overflow.

Remaining:
- This is the first local website deliverable for user review. GitHub repository setup and publishing have not been started yet; unrelated existing worktree changes remain untouched.

### 2026-08-20 13:53 HKT — Codex — Replaced the standalone OCR redesign with the original StoryMap code

Summary:
- Replaced the custom standalone OCR implementation with a literal copy of `Website/storymap/storymap-example.html`, preserving the original HTML, CSS, JavaScript, labels, data, and asset references.
- Added only a standalone wrapper to open at `#part-3-ocr`, hide unrelated StoryMap panels, and restore the original JSON viewer beside `輸出格式：JSON` after the shared script relocates it to Part 2.
- Removed the custom standalone `ocr.css` and `ocr.js` files so the individual page no longer uses a separate redesign.

Files changed:
- `Website/ocr/index.html`
- `Website/ocr/ocr.css` (removed)
- `Website/ocr/ocr.js` (removed)
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Local browser preview loaded at `http://127.0.0.1:8765/intro%20Website/Website/ocr/#part-3-ocr` with only the original OCR panel visible and no browser diagnostics.
- The original `輸出格式：JSON` viewer is visible; its `硃批內容` control selected and highlighted the matching JSON line.
- `git diff --check` passed; unrelated concurrent worktree changes remain untouched.

Remaining:
- GitHub repository setup and publishing remain pending user review of this corrected literal-copy version.

### 2026-08-20 13:59 HKT — Codex — Rebuilt and verified the literal OCR copy

Summary:
- Rebuilt `Website/ocr/index.html` from verified smaller chunks of the canonical StoryMap HTML after checking the first extraction for line-offset loss.
- Confirmed that removing only the standalone wrapper from the rebuilt page produces the original `storymap-example.html` byte content after trailing-whitespace normalization.

Files changed:
- `Website/ocr/index.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- The local page opens at `#part-3-ocr`, keeps only the original OCR panel visible, and has no browser diagnostics.
- `輸出格式：JSON` renders beside its original card; selecting `硃批內容` highlights the corresponding JSON field.
- `git diff --check` passed; unrelated concurrent worktree changes remain untouched.

Remaining:
- GitHub repository setup and publishing remain pending user review.

### 2026-08-20 14:09 HKT — Codex — Simplified the OCR header and repaired Step 9 responsiveness

Summary:
- Hid the shared StoryMap tabs and compact menu in the standalone page, changed the top brand to `OCR 並結構化原始史料`, and removed the visible `步驟二` eyebrow.
- Enlarged and raised the OCR cover title so the individual page opens with its own teaching cover.
- Restored the Step 9 card/JSON two-column layout for computer widths and a one-column layout below 980px, preventing the JSON viewer from collapsing into an implicit overflowing column.

Files changed:
- `Website/ocr/index.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- At 1280px, the Step 9 card is 501.9px wide and the JSON viewer is 668.1px wide with no horizontal overflow.
- At 1024px, the two-column layout remains within the viewport; at 900px, the card and viewer stack with no horizontal overflow.
- The only visible stage eyebrow is removed from the OCR cover, the top navigation tabs/menu are hidden, the `硃批內容` JSON control still highlights its field, and browser diagnostics are empty.

Remaining:
- GitHub repository setup and publishing remain pending user review.

### 2026-08-20 14:01 HKT — Codex — Hid later StoryMap stages from the standalone OCR page

Summary:
- Hid the nested `part-3-ai` stage labelled `步驟三至五` and the later `part-3-wiki` stage from the individual OCR page.
- Kept the original OCR stage, `輸出格式：JSON` viewer, and `試一試` section unchanged.

Files changed:
- `Website/ocr/index.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser rendering shows only the visible eyebrow `步驟二`; both later stages have `display: none` and zero layout height.
- The JSON viewer remains inside the original `#part-3-json` visual slot with height 408px at the local preview viewport.
- Browser diagnostics and `git diff --check` are clean.

Remaining:
- GitHub repository setup and publishing remain pending user review.

### 2026-08-20 14:26 HKT — Codex — Matched the 3.1 visual to the 2.1 review-tool UI

Summary:
- Reworked the 3.1 presentation layer to use the 2.1 compact toolbar, full-width review-tool frame, wide chart, inset rounded panels, and event-card styling from the clicked-dot interface.
- Kept the existing 3.1 text cards below the visual and preserved the event extraction, quote positioning, add-to-chart, dot selection, and close-panel behavior.
- Set the visual to 100vw by 95vh on computer widths, with the existing stacked layout retained for narrow screens.

Files changed:
- `Website/storymap/part2-events-visual.css`
- `Website/storymap/part2-events-visual.js`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Local browser preview at `http://127.0.0.1:8455/Website/storymap/storymap-example.html?visual=20260820-ui02#part-2-events` rendered the visual at 1280px wide and 684px high, matching 95vh at the 720px viewport.
- Default state shows six saved AI candidate cards, the 硃83 summary and five divisions, and no event-detail panel.
- Quote click located the source highlight; adding a candidate created one event dot; clicking the dot opened the rightmost full event panel; closing it restored the three-panel layout.
- `node --check` passed for the visual data and behavior files; browser error logs were empty; `git diff --check` passed.

Remaining:
- Existing unrelated worktree changes and review bundles remain untouched; no remote push was performed.

### 2026-08-20 18:38 HKT — Codex — Set the standalone OCR default font and cover entry point

Summary:
- Set the standalone OCR page's own font-scale preference to start at `80%`, while keeping the existing settings control and preserving the main website's separate preference.
- Changed clean and legacy `#part-3-ocr` entry links to open at the beginning cover target `#part-3-ocr-bar`.
- Added a dedicated green-square, white-`O` favicon for the OCR browser tab and bumped the standalone script cache version.

Files changed:
- `Website/ocr/index.html`
- `Website/ocr/favicon.svg`
- `Website/storymap/storymap.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Local browser preview opened both the clean URL and the legacy `#part-3-ocr` URL at `scrollY: 0`, with the cover at the viewport top and the displayed font setting at `80%`.
- Clicking the existing settings control's `＋` changed the setting to `85%`; `−` restored it to `80%`.
- Browser favicon links resolve to the standalone `favicon.svg`; browser warning/error logs were empty.
- `node --check Website/storymap/storymap.js` and `git diff --check` passed.

Remaining:
- The new source changes are local only; no GitHub push or live-page verification was performed for this edit.

### 2026-08-20 19:07 HKT — Codex — Set the mobile OCR default font to 55%

Summary:
- Set the standalone OCR page to use `55%` as its mobile default while keeping `80%` as the desktop default.
- Stored mobile and desktop OCR font preferences under separate keys so viewport-specific settings do not overwrite each other.
- Bumped the standalone script cache version.

Files changed:
- `Website/ocr/index.html`
- `Website/storymap/storymap.js`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser preview at 390×844 reports `55%`, effective `--font-scale: 0.825`, and the cover at `scrollY: 0`.
- The mobile settings control changes `55%` to `60%` and restores it to `55%`.
- Browser preview at 1280×720 still reports `80%`; browser warning/error logs were empty.
- `node --check Website/storymap/storymap.js` and `git diff --check` passed.

Remaining:
- No GitHub push was executed; the exact push command will be handed off after the local checkpoint.

### 2026-08-20 17:46 HKT — Codex — Added OCR browser-tab favicon

Summary:
- Added a green square favicon with a white “O” for the standalone OCR browser tab; the tab title remains `OCR原始史料`.

Files changed:
- `Website/ocr/index.html`

Verified:
- Local browser preview reports the SVG favicon link loaded successfully and retains the expected document title.
- `git diff --check` passed.

Remaining:
- A pre-existing `storymap.js` cache-buster edit in `Website/ocr/index.html` was left unstaged and untouched; existing unrelated worktree changes and review bundles remain untouched; no remote push was performed.

### 2026-08-20 17:44 HKT — Codex — Restricted enlarged card text to mobile

Summary:
- Narrowed the enlarged OCR card supporting text rule to actual mobile input devices or very small screens, so the narrow-computer layout is not changed.

Files changed:
- `Website/ocr/index.html`

Verified:
- Browser preview at 390×844 reports 18px card text.
- Browser preview at 722×1305 reports the original 16px card text, confirming the narrow-computer layout is excluded.
- Both layouts have zero horizontal overflow; browser diagnostics were empty; `git diff --check` passed.

Remaining:
- Existing unrelated worktree changes and review bundles remain untouched; no remote push was performed.

### 2026-08-20 17:42 HKT — Codex — Enlarged mobile OCR card supporting text

Summary:
- Increased the supporting paragraph text inside every OCR card from 16px to 18px on mobile and narrow layouts, while preserving the existing font-size setting scale.

Files changed:
- `Website/ocr/index.html`

Verified:
- Browser preview at 390×844 and 722×1305 reports 18px card text, 34.2px line height, and zero horizontal overflow.
- Browser preview at 1280×720 remains at the original 16px desktop size.
- Browser diagnostics were empty; `git diff --check` passed.

Remaining:
- Existing unrelated worktree changes and review bundles remain untouched; no remote push was performed.

### 2026-08-20 17:36 HKT — Codex — Enlarged OCR cover copy and menu labels

Summary:
- Enlarged the orange 「理大人工智能 × 數位人文獎 2026 教學」 kicker and the cover description across desktop, narrow desktop, and mobile layouts.
- Enlarged the OCR dropdown menu text and spacing.
- Removed numeric prefixes from the desktop OCR top bar and increased the space between its seven tabs; the mobile dropdown keeps its numbered list.

Files changed:
- `Website/ocr/index.html`

Verified:
- Browser preview at 2048×720 shows larger 23px kicker/29px description text, seven label-only top-bar tabs, 19.2px tab text, and expanded tab spacing.
- Browser preview at 390×844 shows larger cover copy, a larger dropdown list, and zero horizontal overflow; 722×1305 also remains within the viewport.
- Browser diagnostics were empty; `git diff --check` passed.

Remaining:
- Existing unrelated worktree changes and review bundles remain untouched; no remote push was performed.

### 2026-08-20 17:29 HKT — Codex — Removed mobile feature-filter pinning

Summary:
- Removed the sticky/floating behavior from the 「選擇版面特徵」 filter in steps 7 and 8 on the standalone OCR page, keeping the filter in normal document flow while scrolling.

Files changed:
- `Website/ocr/index.html`

Verified:
- Browser preview at 390×844 reports both step 7 and step 8 filters as `position: static` with `z-index: auto`.
- Browser preview at 1280×720 keeps the filters hidden and the original desktop feature tags absolute/floating.
- Browser diagnostics were empty; `git diff --check` passed.

Remaining:
- Existing unrelated worktree changes and review bundles remain untouched; no remote push was performed.

### 2026-08-20 15:58 HKT — Codex — Matched the 3.1 AI panel header and removed the document filter row

Summary:
- Removed the five document division filter controls while retaining the five boxed document parts and their subtitles.
- Added the screenshot-matched three-icon AI chat header, leaving out the right-side window actions.
- Added `擷取` and the source skill (`林方行動` or `清方行動`) to the top of every saved AI candidate card.

Files changed:
- `Website/storymap/part2-events-visual.js`
- `Website/storymap/part2-events-visual.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Desktop browser preview at 1280×911 shows the 80vh visual, five document-part boxes with subtitles, no division-filter row, and an AI header with exactly three controls and no right-side action group.
- Six AI cards show the requested mode and skill labels; quote定位, 加入圖表, event-dot selection, and the rightmost event-detail panel still work.
- 390×844 remains full-width with no horizontal overflow; browser error logs are empty; JavaScript syntax and diff checks pass.

Remaining:
- Existing unrelated worktree changes, review bundles, and user-owned edits remain untouched; no remote push was performed.

### 2026-08-20 16:10 HKT — Codex — Added 2.3-style width changers to the 3.1 panels

Summary:
- Added vertical separators between the chart, AI output, and 硃83 source panels, matching the 2.3 resizer treatment.
- Made the separators draggable with pointer input and keyboard-adjustable with the arrow keys; the third separator appears when the event-detail panel opens.
- Hid the width changers in the mobile stacked layout so the existing responsive panel flow remains unchanged.

Files changed:
- `Website/storymap/part2-events-visual.js`
- `Website/storymap/part2-events-visual.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Desktop browser preview shows two visible width changers with `role="separator"`; pointer dragging and `ArrowRight`/`ArrowLeft` update adjacent panel percentages.
- Opening an added event reveals the third width changer and keeps the event detail panel in the rightmost position; closing restores the two-panel separators.
- 390×844 hides the separators without horizontal overflow; browser error logs are empty; JavaScript syntax and diff checks pass.

Remaining:
- Existing unrelated worktree changes, review bundles, and user-owned edits remain untouched; no remote push was performed.

### 2026-08-20 16:18 HKT — Codex — Moved event details left and simplified the event panel

Summary:
- Moved the clicked event-detail panel to the far-left desktop column, with the chart, AI panel, and source panel following it.
- Removed the relationship list, saved-source block, document identifier, and `done` category pill from the event-detail content.
- Preserved the width changers by remapping them to the reordered event/chart/AI/source columns.

Files changed:
- `Website/storymap/part2-events-visual.js`
- `Website/storymap/part2-events-visual.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Clicking the first added dot places the event panel at the far left and keeps `賊匪攻陷鳳山縣城` visible.
- The event panel no longer contains `關係`, `保存來源`, `zhu-january-official-loop`, `outputs/lin-events.json`, `硃83`, or `done`.
- The reordered third width changer works with keyboard arrows; closing the event restores the default three-panel layout. Syntax, diff, and browser-error checks pass.

Remaining:
- Existing unrelated worktree changes, review bundles, and user-owned edits remain untouched; no remote push was performed.

### 2026-08-20 15:45 HKT — Codex — Matched the OCR cover redesign and added section navigation

Summary:
- Applied the supplied cover sample's dark teal composition to `Website/ocr/index.html`, including the larger right-side handwritten watermark, raised one-line title, and full-height mobile cover.
- Added a shortened OCR-only menu using `主頁`, `簡介`, `辨識`, `JSON`, and `試一試`, with single-digit labels `1` through `5`.
- Added the mobile hamburger drawer beside the original floating `介面字級` settings control and kept navigation inside the individual OCR page.

Verified:
- Browser preview at 1280×720 and 390×844 shows the responsive cover layouts with no horizontal overflow.
- Desktop section navigation and mobile drawer links work; the JSON link remains on the OCR page and reaches `#part-3-json`.
- Original font-size settings opened at `100%`; browser console had no warnings or errors; `git diff --check` passed.

Remaining:
- Awaiting user review of the updated cover/menu before deployment or GitHub publishing.

### 2026-08-20 15:42 HKT — Codex — Refined the 3.1 shared toolbar, date placement, and document sections

Summary:
- Kept the 2.1 toolbar visible but disabled, moved it above the chart, AI panel, and document panel, and removed document-panel filter controls.
- Corrected the chart dates so `十二月十三日` uses `1786/12/13` and `十二月二十八日` uses `1786/12/28`.
- Restored the document division buttons and boxed part subtitles, removed the AI-card colour rail, enlarged AI/source text, and reduced the desktop visual to 80vh.

Files changed:
- `Website/storymap/part2-events-visual-data.js`
- `Website/storymap/part2-events-visual.js`
- `Website/storymap/part2-events-visual.css`
- `Website/storymap/storymap-example.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Local preview shows the disabled shared toolbar spanning all three default columns; the document panel has no inputs/filter controls and contains five division buttons plus five boxed parts with subtitles.
- The first candidate renders at chart date `1786/12/13`, reveals only after `加入圖表`, and opens the rightmost event panel when clicked.
- Desktop visual height is 80vh; 390×844 remains full-width with no horizontal overflow. Quote定位, division navigation, event detail, syntax checks, diff checks, and browser console checks pass.

Remaining:
- Existing unrelated worktree changes, review bundles, and user-owned edits remain untouched; no remote push was performed.

### 2026-08-20 15:23 HKT — Codex — Reused the 2.1 chart engine and background data in 3.1

Summary:
- Replaced the custom 3.1 chart drawing with the shared `part1-interface.js` chart engine and `part-1-interface.css` four-lane styling used by 2.1.
- Projected the same background chart data into 3.1, selected the real `doc-硃83-L` background node as the 硃83 document dot, and kept the six saved AI candidates hidden until confirmation.
- Preserved quote定位, 加入圖表, event-dot selection, rightmost event-detail, and the four explanatory text cards below the visual.

Files changed:
- `Website/storymap/part2-events-visual.js`
- `Website/storymap/part2-events-visual.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Local preview at `http://127.0.0.1:8455/Website/storymap/storymap-example.html?visual=20260820-final#part-2-events` shows the shared chart at 1280×720 with a 1280px-wide, 684px-high visual; 390×844 shows the full-width stacked layout.
- Default state contains 604 shared chart dots, 603 background dots, the foreground `doc-硃83-L` node, six hidden candidate nodes, and six hidden candidate links.
- Quote click locates the source highlight; adding a candidate reveals its chart dot/link and disables its card action; clicking the dot opens `賊匪攻陷鳳山縣城`; closing restores the default panels.
- Browser error logs are empty; `node --check Website/storymap/part2-events-visual.js` and `git diff --check` pass.

Remaining:
- Existing unrelated worktree changes, review bundles, and user-owned edits remain untouched; no remote push was performed.

### 2026-08-20 14:28 HKT — Codex — Added a standalone OCR cover design draft

Summary:
- Added `Website/ocr/cover-draft.html` as an isolated visual draft, leaving `Website/ocr/index.html` unchanged.
- Uses the handwritten PDF page 1 asset `Website/storymap/試一試/手寫字/page1.png`; a browser-side luminance pass removes the paper, folds, and scan background and leaves only soft white handwriting.
- Keeps the floating square settings control and adds the fine-line extraction treatment on the right side without covering the cover title.

Verified:
- Browser preview passed at 1280×800 and 390×844; the narrow layout has no horizontal overflow.
- Settings button opens the `介面字級` control beside the button; `git diff --check` passed.

Remaining:
- Awaiting user review of the cover draft before applying any design to the main OCR page.

### 2026-08-20 14:48 HKT — Codex — Applied the OCR cover design to the individual website

Summary:
- Updated `Website/ocr/index.html` with the requested cover title `OCR原始史料` and description `以清代奏摺為例，介紹如何OCR和結構化手寫本和印刷本的原始史料。`.
- Removed the draft eyebrow, source metadata/date, and `查看史料` link from the live cover.
- Reused the original StoryMap settings UI and font-size behavior instead of adding a separate draft slider.
- Applied the handwritten PDF page 1 text-only watermark and omitted the first upper-right `奏` character.

Verified:
- Local browser checks at 1280×800 and 390×844 passed with no horizontal overflow.
- Original settings UI opened correctly and changed the shared font scale from 100% to 105%; it was restored to 100% after testing.
- Existing OCR, `輸出格式：JSON`, and `試一試` content remains available below the cover.

Remaining:
- Awaiting user review of the integrated individual website before any publication.

### 2026-08-20 15:01 HKT — Codex — Simplified the 3.1 visual chrome and enlarged panel text

Summary:
- Hid the internal visual toolbar and repeated chart, AI, document, summary, division, part-heading, footer, and saved-bundle labels requested for the 3.1 presentation.
- Enlarged the AI candidate and 硃83 source text while keeping quotation location, add-event, event-dot, and rightmost event-detail interactions intact.
- Kept the original four explanatory text cards below the visual unchanged.

Files changed:
- `Website/storymap/part2-events-visual.css`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Local browser preview at `http://127.0.0.1:8455/Website/storymap/storymap-example.html?visual=20260820-final#part-2-events` rendered the visual at 1280px wide and 684px high at a 1280×720 viewport; the normal preview viewport was restored afterward.
- Default state has six candidate cards, five source-document parts, zero event dots, a hidden event-detail panel, and four original explanatory text cards.
- Quotation click located three source highlights; adding the first candidate created one dot and disabled its action; clicking the dot opened `賊匪攻陷鳳山縣城` in the rightmost panel; closing restored the default panel state.
- Browser error logs were empty, `node --check Website/storymap/part2-events-visual.js` passed, and `git diff --check` passed.

Remaining:
- Existing unrelated worktree changes and review bundles remain untouched; no remote push was performed.

### 2026-08-20 16:28 HKT — Codex — Refined the standalone OCR cover and workflow menu

Summary:
- Added the orange `理大人工智能 × 數位人文獎 2026 教學` kicker, enlarged the cover description, and restored the sample scan sweep over the text-only handwritten watermark.
- Kept the watermark at its intrinsic width while scaling and centering the complete layer for desktop, narrow-computer, and phone layouts; narrow screens now use the mobile cover composition and keep the watermark inside its frame.
- Replaced repeated workflow labels in both navigation surfaces with seven unique tabs, each with one number: `1 OCR`, `2 PaddleOCR`, `3 準備OCR`, `4 辨識印刷字`, `5 辨識手寫字`, `6 輸出格式`, and `7 試一試`.
- Moved the original settings control into the sticky OCR menu on wide screens while retaining the floating control for the cover and mobile layouts.

Files changed:
- `Website/ocr/index.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser preview checked at 1280×720, 722×1305, and 390×844; the cover remains full-height on narrow layouts, the title stays on one line, the watermark/frame is centered, the scan effect is present, and horizontal overflow is zero.
- Both the desktop bar and mobile drawer expose the same seven unique numbered tabs; the original settings panel opens and the sticky menu placement is active when the bar reaches the top.
- Browser diagnostics were empty and `git diff --check` passed.

Remaining:
- Existing unrelated worktree changes and review bundles remain untouched; no remote push was performed.

### 2026-08-20 16:41 HKT — Codex — Enlarged and centered the OCR watermark

Summary:
- Cropped the transparent handwriting canvas to the visible ink after removing the isolated first `奏`, so the large blank right side of the source PDF no longer shrinks or offsets the watermark.
- Removed the responsive watermark downscaling and kept the extracted text layer centered inside the scan frame at full-computer, narrow-computer, and mobile widths.

Files changed:
- `Website/ocr/index.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser preview at 1280×720, 722×1305, and 390×844 shows the handwriting enlarged, centered inside the frame, and without horizontal overflow.
- Browser diagnostics were empty; `git diff --check` passed.

Remaining:
- Existing unrelated worktree changes and review bundles remain untouched; no remote push was performed.

### 2026-08-20 17:19 HKT — Codex — Rebalanced OCR navigation and responsive cover spacing

Summary:
- Centered the seven desktop OCR tabs as a group, increased their label size, and placed each tab title before its number so the number sits on the right.
- Returned the settings button to the original right-side horizontal position in the top menu while keeping it inside the menu bar when that bar is sticky.
- Enlarged the orange teaching kicker and moved the narrow/mobile scan frame into the blank area below the description, centered with its watermark.

Files changed:
- `Website/ocr/index.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser preview at 2048×720 confirms the tab group is centered at the viewport midpoint, tab text is 15.2px, titles precede right-side numbers, and the settings button remains at the original right offset.
- Browser preview at 722×1305 and 390×844 confirms the larger kicker, description-first cover order, centered scan frame/watermark, one-line title, and zero horizontal overflow.
- Browser diagnostics were empty; `git diff --check` passed.

Remaining:
- Existing unrelated worktree changes and review bundles remain untouched; no remote push was performed.

### 2026-08-20 17:48 HKT — Codex — Added approved references to clicked OCR images

Summary:
- Replaced the outdated handwritten lightbox citation with the approved `故宮075669號` reference, linked only on `《清代檔案檢索系統》` and without a browsing date.
- Added publisher details `（臺北：遠流，2006）` to the printed citations for the main OCR example and the printed `試一試` example.
- Applied the same source-reference treatment to the Part 3 printed/handwritten feature galleries and both `試一試` modes; 硃 identifiers are not displayed.

Files changed:
- `Website/storymap/storymap.js`
- `Website/ocr/index.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check Website/storymap/storymap.js` passed.
- `git diff --check` passed.
- Browser-tested the main handwritten and printed OCR images, printed and handwritten `試一試`, and the printed/handwritten feature galleries. Captions showed the approved references, the handwritten system title contained the embedded link, no full URL or browsing date was visible, and no 硃 ID was shown.
- Visual overlay checked at 1280×720.

Remaining:
- Existing unrelated worktree changes and review bundles remain untouched; no remote push was performed.

### 2026-08-20 17:53 HKT — Codex — Limited expanded image panels to references only

Summary:
- Removed page labels, feature descriptions, and generic scan-page text from the clicked-image overlay.
- The expanded info panel now shows only the applicable approved reference; the handwritten archive title remains the only embedded link.

Files changed:
- `Website/storymap/storymap.js`
- `Website/ocr/index.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- `node --check Website/storymap/storymap.js` passed.
- `git diff --check` passed.
- Browser-tested the main OCR images, both `試一試` modes, and the printed/handwritten feature galleries. Each expanded caption contained only its reference; no full URL, browsing date, or 硃 identifier was visible.
- Visual expanded overlay checked at 1280×720.

Remaining:
- Existing unrelated worktree changes and review bundles remain untouched; no remote push was performed.

### 2026-08-20 17:58 HKT — Codex — Added a references section to the OCR page

Summary:
- Added a `參考資料` section at the bottom of the standalone OCR website.
- Listed the two printed `明清臺灣檔案彙編` references and the handwritten archive reference, with only `《清代檔案檢索系統》` shown as the embedded link text.

Files changed:
- `Website/ocr/index.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser preview found one bottom reference section with three entries and one embedded archive link; the full URL is not visible.
- Scrolled to the page bottom at 1280×720 and visually confirmed the section layout and link styling.
- `git diff --check` passed.

Remaining:
- Existing unrelated worktree changes and review bundles remain untouched; no remote push was performed.

### 2026-08-20 17:49 HKT — Codex — Made the former 150% OCR font size the default 100% baseline

Summary:
- Made the former 150% reading view the effective 100% baseline for the shared website font-scale control.
- Kept the displayed percentage relative to that new baseline, so `100%` now renders the requested larger OCR text while `＋` and `−` remain usable.
- Bumped the OCR stylesheet/script cache versions for the typography change.

Files changed:
- `Website/storymap/storymap.css`
- `Website/storymap/storymap.js`
- `Website/ocr/index.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- The requested URL reloads with displayed `100%` and effective `--font-scale: 1.5`.
- The representative `試一試` filename text is `18.75px` at the new `100%`, matching its earlier `150%` measurement; one increase reports `105%` and scales it to `19.6875px`, then restores to `100%`.
- Browser warning/error logs were empty; `node --check Website/storymap/storymap.js` and `git diff --check` passed.

Remaining:
- Existing unrelated worktree changes and review bundles remain untouched; no deployment or GitHub push was performed.

### 2026-08-20 18:23 HKT — Codex — Published the individual OCR site with GitHub Pages

Summary:
- Confirmed the current branch `codex/current-project-update` was already pushed to `CBananaC/llm-wiki-teammate-package`.
- Changed the repository's GitHub Pages source from `gh-pages` to `codex/current-project-update` at `/ (root)` and waited for `pages-build-deployment #3` to complete.

Files changed:
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Live individual OCR site: `https://cbananac.github.io/llm-wiki-teammate-package/intro%20Website/Website/ocr/`
- Live page loads `OCR原始史料`, the cover text, watermark asset, favicon, and scripts; browser diagnostics were empty and horizontal overflow was 0.

Remaining:
- Existing unrelated worktree changes and review bundles remain untouched; no local `git push` was executed because the branch already matched its remote.

### 2026-08-20 18:05 HKT — Codex — Restyled the references as bottom additional information

Summary:
- Changed the bottom `參考資料` block from a large white card to the website's existing compact `.aside` additional-information treatment.
- Preserved all three references and the embedded `《清代檔案檢索系統》` link text.

Files changed:
- `Website/ocr/index.html`
- `INTRO_WEBSITE_CHANGE_LOG.md`
- `../PROJECT_LOG.md`

Verified:
- Browser preview at 1280×720 shows the references in the compact muted bordered panel at the page bottom.
- The section contains three references and no visible full URL.
- `git diff --check` passed.

Remaining:
- Existing unrelated worktree changes and review bundles remain untouched; no deployment or GitHub push was performed.
