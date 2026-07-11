# Gemini proxy (Cloud Run)

A tiny server that lets the timeline's info panel ask Gemini about a document
**without putting any API key in the browser**. It calls Vertex AI with the
Cloud Run service account's own credentials.

## Deploy

```bash
cd gemini-proxy
bash deploy.sh
```

This uses project `delta-entry-496910-e7`, region `asia-east1`, model
`gemini-2.5-flash` (the same model as the summarization script). Override with
env vars, e.g. `MODEL=gemini-2.5-pro REGION=asia-east1 bash deploy.sh`.

The script grants the runtime service account `roles/aiplatform.user` and
deploys with `--allow-unauthenticated` so the static page can reach it. If you
prefer authenticated access, remove that flag and front it differently.

When it finishes it prints the service URL. Copy that URL into the timeline:
open a document, in the **互動標註** tab click **⚙ 設定**, paste the URL, save.
It is remembered in this browser only.

## Endpoint

`POST /chat` with JSON `{mode, doc_id, doc_type, title, body, rescript, summary, highlight, question}`.

- `mode: "summary"` → `{mode, text}` a tighter prose summary.
- `mode: "divide"`  → `{mode, parts:[{label, summary, excerpt}]}` segmented text.
- `mode: "ask"`     → `{mode, text}` free-text answer (uses `question`/`highlight`).

`GET /` is a health check returning the active model/project/location.

## Security notes

- No key is exposed to the browser; auth is the Cloud Run service account.
- `ALLOW_ORIGIN` defaults to `*`. A local `file://` page sends `Origin: null`,
  so `*` is the simplest. Set it to a specific origin if you host the page.
- Cost: each click is one Gemini call. `gemini-2.5-flash` is inexpensive, but
  the endpoint is public when `--allow-unauthenticated`; delete the service when
  not in use, or add auth, if cost/abuse is a concern.
