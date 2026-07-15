# LLM Wiki Review App

This is the local integration layer for the existing 林爽文 timeline HTML.

It is intentionally local-first. Long AI jobs should run from terminal scripts and save artifacts into the LLM Wiki. The existing website UI should remain the human review workspace: timeline, info panels, event dots, AI chat, notes, source-chain tools, and editing behavior.

## Design Commitments

- Keep the complete current HTML UI and function. This app serves it at `/app`.
- Add local APIs and bridge panels around the current UI instead of replacing it.
- Do not rebuild the per-document metadata/data table as a new major surface. The three main document types already work through the review chain.
- Treat LLM Wiki skills as the durable source of saved prompts.
- Treat browser AI chat as a human-assistance layer, not the main batch processor.
- Save batch outputs as local JSON/Markdown artifacts that can be reloaded, edited, backed up, and fed back into the LLM Wiki.

## Review Chain

The working chain is:

1. Summary
2. Division into parts
3. 林方行動 and source evidence
4. 清方行動 and source evidence
5. 皇帝回應, 硃批, and related 上諭
6. Source-chain review
7. Human notes and corrections
8. Wiki export

Each chain step should map to one skill file in `llm-wiki/skills/`.

## Artifact Shape

Review bundles should be split by skill and output kind:

```text
llm-wiki/outputs/review-bundles/
  1786-10_1786-12/
    manifest.json
    source-docs.json
    skills/
      summary.md
      divide-parts.md
      extract-lin-actions.md
      extract-qing-actions.md
      emperor-response.md
      source-chain.md
    outputs/
      summary.json
      division-parts.json
      lin-events.json
      qing-events.json
      emperor-response.json
      source-chain.json
    human-edits/
      notes.json
      event-edits.json
      source-edits.json
    wiki-export/
      summary.md
      division-parts.md
      event.md
      source-chain.md
```

The app should load existing bundles and write back review edits without changing raw data.

## Run Locally

```bash
python3 llm-wiki/review-app/server.py
```

Then open:

```text
http://127.0.0.1:8766
```

The preserved timeline UI itself is also available directly:

```text
http://127.0.0.1:8766/app
```

The interactive algorithm map for the pre-reading stage and the two AI review
loops is available at:

```text
http://127.0.0.1:8766/workflow/
```

Select any flowchart step to read its algorithm, input/output contract, and the
full Markdown skill and Python runner used by that step.
