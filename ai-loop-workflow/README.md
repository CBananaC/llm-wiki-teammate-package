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
runner under `skills/` and `scripts/`. The review server exposes those files to
the read-only source viewer through `/api/workflow-sources`.
