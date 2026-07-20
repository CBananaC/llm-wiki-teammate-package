# Imperial Communication Analysis Workflow

This folder contains the bilingual interactive workflow chart:

- `index.html` — algorithm structure and accessible controls
- `styles.css` — light-mode vertical flowchart presentation
- `app.js` — English／Traditional Chinese switching, step details, and source-file viewer

Run the local review app and open:

```text
http://127.0.0.1:8766/workflow/
```

Every selectable step is mapped to an existing Markdown prompt/skill or Python
runner under `tool/skills md/` and `tool/scripts py/`. The review server exposes those files to
the read-only source viewer through `/api/workflow-sources`.

The current map presents the official-document-first loop implemented by the AI
chat action `官文優先審閱迴圈`: summary, division, 林方 events, combined 清方
actions, duplicate-report/source-chain review, pair-grounded 上諭 response
analysis, combined multi-source emperor actions, emperor-action de-duplication,
and pair-grounded later official responses. Relationship stages consume the
curated pair JSON and do not search the corpus again.
