# DeepSeek proxy via Google Cloud

Standalone Cloud Run proxy for the managed DeepSeek MaaS endpoint on Vertex
AI. It uses Application Default Credentials and the Cloud Run service account;
no DeepSeek API key is required.

Defaults:

- Project: `delta-entry-496910-e7`
- Vertex location: `global`
- Model: `deepseek-v3.2-maas`
- Long-request budget: 600 seconds upstream, 900 seconds Cloud Run/Gunicorn
- Concurrency: one worker and one Cloud Run instance to respect Vertex throttling

Deploy:

```bash
bash deploy.sh
```

The Cloud Run runtime service account receives `roles/aiplatform.user`. The
service exposes `/`, `/providers`, `/models`, and `/chat`, with the same core
request contract as the Gemini/GPT proxy.
