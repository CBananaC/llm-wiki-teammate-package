# Local AI Agent Rules — Introduction Website

These rules apply to work inside `intro Website/`. The repository-level
`../AGENTS.md` remains authoritative. This file adds folder-specific guidance;
it does not replace the parent rules. User instructions take precedence when
they explicitly change the requested scope.

## Mission and scope

This folder contains the student-facing introduction and teaching demonstration
for the Qing digital-history review system about the 林爽文事件. Changes here
should improve the explanation, demonstration, accessibility, or maintainability
of that website without corrupting research evidence or review-tool state.

The main page is `Website/storymap/storymap-example.html`. It presents Traditional
Chinese introduction content as a scrollable StoryMap-style page and embeds the
sample review tool in section 1.5.

## Before editing

1. Read the parent `../PROJECT_LOG.md`, this file, `README.md`, and
   `INTRO_WEBSITE_CHANGE_LOG.md`.
2. Inspect `git status --short` from the repository root. Treat existing
   modifications and untracked files as user-owned unless clearly created by
   the current task.
3. Identify the exact requested files and the smallest coherent change. Do not
   reformat, rename, delete, or clean up unrelated files.
4. If the task involves formal review state, first check the parent log's
   `Formal review editor` field. Never edit formal state while another person
   or agent is listed.

## Source, language, and research rules

- Explain work in English unless the user requests Chinese. Preserve all
  website content in Traditional Chinese; never introduce Simplified Chinese.
- Use `Outline/Content.docx` as the current source for the visible introduction
  title, prose, section breaks, and 1.4 comparison table. Do not silently
  change wording when implementing it in `Website/storymap/storymap.js`.
- Never invent citations, page numbers, dates, people, titles, translations,
  or historical claims. Keep source evidence separate from interpretation and
  label uncertain or unverified material explicitly. For example, `頁碼待核`
  is not a verified page reference.
- Do not edit raw source material. Derived or corrected text must retain its
  provenance.
- Preserve exact UI labels and research distinctions, including `硃批`, `上諭`,
  `yu_source`, and `official_reply_to_yu` when they appear in reviewed data or
  documentation.

## Website architecture

- Keep `Website/storymap/storymap-example.html` structural. Its main responsibilities
  are the page shell, navigation, title, and `intro-content` mount point.
- Put StoryMap content data and rendering logic in
  `Website/storymap/storymap.js`. The `parts` array controls cards, section
  grouping, backdrops, the 1.4 table, and the section 1.5 iframe.
- Put StoryMap layout and responsive presentation in
  `Website/storymap/storymap.css`.
- Keep the standalone simplified review demonstration in
  `Website/embedded-tool/review-tool-embed.html` with its logic in
  `Website/embedded-tool/review-tool-embed.js` and styling in
  `Website/embedded-tool/review-tool-embed.css`.
- Preserve the real sample review-tool embed in section 1.5. It is an actual
  sample review interface, not merely a screenshot or decorative imitation.
  The current demonstration targets 硃83 and the `ai,original` panels.
- Preserve navigation grouping and section identity: 1.3 and 1.6 each contain
  multiple cards, but their cards belong to one navigation section.

## Review-tool and data boundaries

- Do not modify formal/sample saved state, raw source data, or review bundles as
  part of an introduction-website change unless the user explicitly requests
  that broader task.
- If a change to `review-tools/(1) formal/index.html` or
  `review-tools/(2) sample/index.html` is required, make the equivalent change
  to both files in the same task unless the user explicitly requests
  mode-specific behaviour. Record any intentional exception in
  `../PROJECT_LOG.md`.
- Never replace formal data with sample data. Preserve IDs, literal quotations,
  source anchors, and provisional-review semantics.
- Reuse canonical project visuals and icons where applicable. Do not substitute
  approximate icons when a canonical project asset exists.

## Validation

After JavaScript changes, run focused checks from the repository root:

```sh
cd "/Users/creamybanana/Downloads/DH Project"
node --check "intro Website/Website/storymap/storymap.js"
node --check "intro Website/Website/embedded-tool/review-tool-embed.js"
git diff --check
```

For browser validation, serve the project root on port 8765 and use the
existing review-tool server on port 8766 when available:

```sh
cd "/Users/creamybanana/Downloads/DH Project"
python3 -m http.server 8765
```

Check the page at
`http://127.0.0.1:8765/intro%20Website/Website/storymap/storymap-example.html`.
Confirm that the six navigation tabs, cards, 1.4 table, responsive layout,
section 1.5 硃83 AI card, original-document panel, and quote highlighting work.
Record visual checks honestly; do not claim browser verification if it was not
performed. Reuse a running port-8766 server instead of starting a duplicate.

## Logging and handoff

After every coherent change, append one timestamped entry using
`YYYY-MM-DD HH:MM HKT` to `INTRO_WEBSITE_CHANGE_LOG.md`. Each entry must state:

- author;
- summary;
- files changed;
- verification; and
- remaining work.

Also update `../PROJECT_LOG.md` for the corresponding project change. Do not
log every click, autosave, or read-only inspection. Keep unrelated concurrent
log entries intact.

After validation, stage the entire `/Users/creamybanana/Downloads/DH Project`
repository and create a concise local Git commit. Do not run `git push`
automatically. At handoff, report the changed files, verification performed,
remaining work, and any pre-existing or concurrent changes deliberately left
untouched.

### Automatic checkpoint rule

- Automatically create the local commit immediately after every coherent
  non-log change has been validated. Do not wait for a later task or user
  confirmation.
- Treat the corresponding log update as part of that same change, not as a
  separate commit. Do not create a commit whose only purpose is editing
  `INTRO_WEBSITE_CHANGE_LOG.md` or `../PROJECT_LOG.md`.
- When the checkpoint is triggered, use `git add -A` from the DH Project root so
  the commit covers the whole DH Project folder, including other current user
  changes. Inspect the status first and do not add credentials or secrets.
- Never push automatically. Preserve all committed content and do not use the
  whole-repository scope as permission to delete or overwrite files.

## Safety

- Do not store credentials, API keys, tokens, or service-account files.
- Do not use destructive commands on broad paths. Resolve exact targets first
  and prefer recoverable operations.
- Do not publish historical claims or competition requirements without checking
  the underlying source and marking provisional material as provisional.
