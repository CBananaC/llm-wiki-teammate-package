# Introduction Website — AI Working Guide

Read this file before editing anything in `intro Website/`. The folder contains
the student-facing introduction and teaching demonstration for the Qing
digital-history review system about the 林爽文事件.

## Purpose

The website explains why the project studies Qing official documents, how AI
and visualisation support source review, and how the review tool can be used to
study the 林爽文事件. The main demonstration is a scrollable StoryMap-style
page with Traditional Chinese introduction content and a real sample review
tool embedded in section 1.5.

## File map

- `Website/storymap-example.html` — page shell, navigation, title, and the
  `intro-content` mount point. Keep this file mostly structural.
- `Website/assets/storymap.js` — main introduction content data and rendering
  logic. The `parts` array defines the cards, sections, backgrounds, table, and
  review-tool iframe.
- `Website/assets/storymap.css` — StoryMap layout, card styling, backgrounds,
  navigation, and responsive behaviour.
- `Website/review-tool-embed.html` — standalone simplified review-tool embed
  page for the self-contained demonstration UI.
- `Website/assets/review-tool-embed.js` — self-contained 硃83 demonstration
  data and interactions for the AI card and original-text panel.
- `Website/assets/review-tool-embed.css` — styling for the standalone review
  embed.
- `AGENT.md` — folder-specific rules for AI agents; the parent `../AGENTS.md`
  remains authoritative.
- `Outline/` — Word drafts and planning material. `Outline/Content.docx` is
  the current source for the visible introduction title, prose, section
  breaks, and 1.4 comparison table. Word lock files beginning with `~$` are
  temporary files and should not be treated as source material.
- `INTRO_WEBSITE_CHANGE_LOG.md` — folder-specific record of every coherent
  change. Update it after each edit.
- `../PROJECT_LOG.md` — project-wide progress record. Update it for every
  coherent project change as required by the repository instructions.

## Editing rules for AI

1. Use English for explanations, but preserve the website's Traditional
   Chinese wording and exact labels. Do not introduce Simplified Chinese.
2. Treat source evidence, interpretation, and AI-generated extraction as
   separate things. Do not invent historical claims, citations, dates, people,
   translations, or page numbers. The current draft contains items marked
   `頁碼待核`; do not present those as verified citations.
3. When changing visible introduction text, compare the requested wording with
   `Outline/Content.docx`, then update the corresponding data in
   `Website/assets/storymap.js`. Preserve section numbering and navigation
   grouping: 1.3 and 1.6 each contain multiple cards.
4. Preserve the real sample review-tool embed in section 1.5. It is not a
   decorative mockup. The current example targets 硃83 and the panels
   `ai,original`.
5. Do not edit raw source material or formal/sample saved state as part of an
   introduction-website change. If a change to either formal or sample review
   HTML is necessary, make the equivalent change to both files and record why.
6. Inspect Git status before editing. Preserve unrelated user changes,
   including Word drafts, temporary lock files, assets, and review-tool data.
7. After each coherent change, append a timestamped entry to
   `INTRO_WEBSITE_CHANGE_LOG.md` containing author, summary, files changed,
   verification, and remaining work. Also append the corresponding entry to
   `../PROJECT_LOG.md` when the project-wide instructions require it.
8. Keep `AGENTS.md` and `CLAUDE.md` byte-for-byte identical if either is ever
   changed. Run the repository's agent-document check afterward.

## Running and checking the website

For the embedded real sample review tool, use the existing local review server
on port 8766 when available. The static introduction page is normally served
from the project root on port 8765:

```sh
cd "/Users/creamybanana/Downloads/DH Project"
python3 -m http.server 8765
```

Open:

```text
http://127.0.0.1:8765/intro%20Website/Website/storymap-example.html
```

When the page is opened over HTTP, the StoryMap iframe uses the review server
at `http://127.0.0.1:8766/sample`. When opened as a local `file://` page, it
uses the relative sample-page fallback. Reuse a running port-8766 server
instead of starting a duplicate server.

After JavaScript edits, run focused syntax and whitespace checks from the
repository root:

```sh
cd "/Users/creamybanana/Downloads/DH Project"
node --check "intro Website/Website/assets/storymap.js"
node --check "intro Website/Website/assets/review-tool-embed.js"
git diff --check
```

For a browser check, confirm the page loads without console errors, all six
navigation tabs work, the 1.4 table is readable, and section 1.5 displays the
硃83 AI card and original-document panel. Report any visual checks that were
not performed rather than assuming they passed.

## Change handoff

Make a local Git checkpoint after each coherent edit, staging only the files
changed by that edit. Do not push automatically. At handoff, state what was
changed, what was verified, and what remains.
