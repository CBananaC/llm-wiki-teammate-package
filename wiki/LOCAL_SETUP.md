# Local Review-Tool Setup

Run from the project root with Python 3.10 or newer:

```bash
python3 run-local.py
```

Open:

- Formal review: <http://127.0.0.1:8766/formal>
- Sample review: <http://127.0.0.1:8766/sample>
- Model comparison: <http://127.0.0.1:8766/model-output-comparison>
- Workflow: <http://127.0.0.1:8766/workflow/>
- Project log: <http://127.0.0.1:8766/status>

Health check:

```bash
curl http://127.0.0.1:8766/api/health
```

Formal and sample state are isolated. Never copy `sample_all.data` over `formal_all.data`. Do not use `file://` when saving or using APIs. Optional AI proxy failures do not prevent the review tools from running.

