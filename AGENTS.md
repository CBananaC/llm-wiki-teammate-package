# Project Instructions for Human and AI Collaborators

## Purpose

This repository supports historical research on the 林爽文事件. The formal
review tool is the source-review workspace; the sample tool is isolated
presentation data; the LLM Wiki is the durable thinking and project-memory
layer that consumes human-reviewed results.

## Language and research rules

- Use English for explanation by default and Traditional Chinese when Chinese is needed.
- Never invent citations, dates, people, titles, translations, or historical claims.
- Keep source evidence separate from interpretation and mark uncertainty explicitly.
- Do not edit raw source material. Derived or corrected material must retain provenance.

## Canonical project areas

- `review-tools/(1) formal/`: complete review UI, relationship files, and formal saved state.
- `review-tools/(2) sample/`: isolated sample UI, relationship files, and sample saved state.
- `review-tools/(3) model-output-comparison/`: side-by-side model-output comparison UI.
- `review-tools/(4) workflow/`: interactive map of the review and LLM workflow.
- `review-tools/shared data/stage1_original_text.json`: canonical Stage 1 source dataset shared by both tools.
- `review-tools/shared data/review-bundles/`: shared model-run and human-review bundles.
- `wiki/`: research context, rules, attempts, errors, interpretations, and accepted exports.
- `tool/skills md/`: canonical prompt/task specifications used by website and terminal workflows.
- `tool/scripts py/`: reproducible data-processing and model-run scripts.
- `tool/proxy/`: optional local and deployable AI proxy services.
- GitHub repository: <https://github.com/CBananaC/llm-wiki-teammate-package>

## Progress protocol

1. Read `PROJECT_LOG.md` before starting work.
2. Before editing formal state, set `Formal review editor` in the log. Do not edit while another person or agent is listed.
3. After each coherent adjustment, append one log entry with the author, summary, files changed, verification, and anything remaining.
4. Update the log's current state when priorities, ownership, or risks change.
5. Do not log every click, autosave, read-only inspection, or chat message.
6. At handoff, clear the formal editor field when applicable and record the next concrete action.

## Formal/sample isolation

- When editing either `review-tools/(1) formal/index.html` or
  `review-tools/(2) sample/index.html`, always make the equivalent change to
  both HTML files in the same task. Diverge only when the user explicitly asks
  for mode-specific behavior, and record that exception in `PROJECT_LOG.md`.
- Formal edits save only to `review-tools/(1) formal/formal_all.data`.
- Sample edits save only to `review-tools/(2) sample/sample_all.data`.
- Each tool owns its own curated `confirmed-pairs.json` and `yu-source.json`.
- Candidate `yu-pairing.json` and `zhu-pairing.json` outputs remain in shared review bundles, not beside the HTML files.
- Never replace formal data with sample data.
- Only Stage 1 source JSON and review bundles are shared.

## Agent-file synchronization

`AGENTS.md` and `CLAUDE.md` must remain byte-for-byte identical. Run
`"tool/scripts py/check_agent_docs.sh"` after editing either file.

## Terminal-command protocol

- Whenever providing a terminal command to the user, include an explicit `cd`
  command to the exact required working directory first. Never assume the
  user's current directory, including in multi-step command blocks.

## GitHub push protocol

- Never execute `git push` for the user, even when the user asks to push.
  Provide the exact `git push` command instead, always preceded by an explicit
  `cd` to the repository root. Explain if the command will replace an existing
  remote branch.

## Review-bundle naming

- When asked to create a review bundle, use a short, descriptive semantic name
  instead of concatenating document IDs or numbers. Keep the complete document
  list inside the bundle manifest; do not put a long number list in the folder
  or bundle name.

## Safety

- Do not store credentials, API keys, tokens, or service-account files.
- Preserve user changes and inspect Git state before moving or removing data.
- Treat review bundles and formal saved state as research evidence, not disposable build output.
