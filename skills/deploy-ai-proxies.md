# AI Proxy Deployment

Use this file when the source-chain prompts or other proxy code changes. All
services use the same Google Cloud project and region:

```text
PROJECT=delta-entry-496910-e7
REGION=asia-east1
```

The review website can use these proxy websites as its AI endpoint. The page
posts tasks to the selected URL's `/chat` route.

| Proxy | Cloud Run website | Service | Key requirement |
|---|---|---|---|
| Gemini / multi-provider | https://gemini-proxy-v2ewrxq4sq-de.a.run.app | `gemini-proxy` | Vertex AI uses the Cloud Run service account; no key required for the default Gemini/managed DeepSeek route |
| ChatGPT / TokenRouter | https://chatgpt-proxy-v2ewrxq4sq-de.a.run.app | `chatgpt-proxy` | `TOKENROUTER_API_KEY` |
| DeepSeek MaaS / Vertex | https://deepseek-proxy-v2ewrxq4sq-de.a.run.app | `deepseek-proxy` | No DeepSeek key; Cloud Run service account needs `roles/aiplatform.user` |
| GLM / TokenRouter | https://glm-proxy-v2ewrxq4sq-de.a.run.app | `glm-proxy` | `GLM_API_KEY` or `TOKENROUTER_API_KEY` |

## Redeploy every proxy

Run these from the repository root. The deploy scripts build the code in each
proxy directory and print the resulting Cloud Run URL.

```bash
cd /Users/creamybanana/genai-workshop/llm-wiki-teammate-package/gemini-proxy
bash deploy.sh

cd /Users/creamybanana/genai-workshop/llm-wiki-teammate-package/chatgpt-proxy
export TOKENROUTER_API_KEY='your-tokenrouter-key'
bash deploy.sh

cd /Users/creamybanana/genai-workshop/llm-wiki-teammate-package/deepseek-proxy
bash deploy.sh

cd /Users/creamybanana/genai-workshop/llm-wiki-teammate-package/glm-proxy
export GLM_API_KEY='your-tokenrouter-key'
bash deploy.sh
```

The source-chain prompt changes are included automatically because each
script deploys its current directory with `gcloud run deploy --source .`.

If the ChatGPT or GLM key already exists in the Cloud Run service and is not
available in the current shell, deploy the source while omitting environment
flags so the existing service environment remains unchanged:

```bash
cd /Users/creamybanana/genai-workshop/llm-wiki-teammate-package/chatgpt-proxy
gcloud run deploy chatgpt-proxy --source . --project delta-entry-496910-e7 --region asia-east1 --allow-unauthenticated --timeout 300 --min-instances 1

cd /Users/creamybanana/genai-workshop/llm-wiki-teammate-package/glm-proxy
gcloud run deploy glm-proxy --source . --project delta-entry-496910-e7 --region asia-east1 --allow-unauthenticated
```

## Key and environment settings

Never commit actual key values. Export them only in the deployment shell or
bind them from Secret Manager.

| Variable | Used by | Purpose |
|---|---|---|
| `TOKENROUTER_API_KEY` | ChatGPT; optional Gemini TokenRouter; GLM fallback | TokenRouter credential |
| `GLM_API_KEY` | GLM | GLM credential; takes precedence over `TOKENROUTER_API_KEY` |
| `GEMINI_API_KEY` | Gemini proxy | Optional public Gemini API credential |
| `OPENAI_API_KEY` | Gemini multi-provider proxy | Optional OpenAI provider credential |
| `ANTHROPIC_API_KEY` | Gemini multi-provider proxy | Optional Claude provider credential |
| `DEEPSEEK_API_KEY` | Gemini multi-provider proxy | Optional direct DeepSeek credential; not needed for Vertex MaaS |
| `CUSTOM_API_KEY` | Gemini multi-provider proxy | Optional third-party OpenAI-compatible credential |
| `CUSTOM_BASE_URL` | Gemini multi-provider proxy | Required with `CUSTOM_API_KEY` for a custom provider |
| `ALLOW_ORIGIN` | All proxies | Website origin; defaults to `*` for local file pages |
| `MODEL` / provider model variables | Each proxy | Default model selection |

The deploy scripts accept these non-secret settings:

| Proxy | Main settings |
|---|---|
| Gemini | `MODEL`, `VERTEX_LOCATION`, `MAX_OUTPUT_TOKENS`, `ALLOW_ORIGIN`, plus optional `TOKENROUTER_*` settings |
| ChatGPT | `TOKENROUTER_BASE_URL`, `TOKENROUTER_DEFAULT_MODEL`, `TOKENROUTER_ALLOWED_MODELS`, `MAX_OUTPUT_TOKENS`, `REQUEST_TIMEOUT_SECONDS`, `ALLOW_ORIGIN` |
| DeepSeek | `DEEPSEEK_MODEL`, `VERTEX_LOCATION`, `MAX_OUTPUT_TOKENS`, `REQUEST_TIMEOUT_SECONDS`, `ALLOW_ORIGIN` |
| GLM | `GLM_BASE_URL`, `GLM_MODEL`, `GLM_ALLOWED_MODELS`, `MAX_OUTPUT_TOKENS`, `ALLOW_ORIGIN` |

For a stable hosted website, set `ALLOW_ORIGIN` to that website's exact origin
instead of `*`. Keep `TOKENROUTER_API_KEY` and `GLM_API_KEY` server-side; do not
paste them into HTML or commit them to the repository.

## Check the deployed websites

```bash
curl -L --fail https://gemini-proxy-v2ewrxq4sq-de.a.run.app/
curl -L --fail https://chatgpt-proxy-v2ewrxq4sq-de.a.run.app/
curl -L --fail https://deepseek-proxy-v2ewrxq4sq-de.a.run.app/
curl -L --fail https://glm-proxy-v2ewrxq4sq-de.a.run.app/
```

Each response should report `ok: true`. To find the URL again:

```bash
gcloud run services list \
  --project delta-entry-496910-e7 \
  --region asia-east1 \
  --format='table(metadata.name,status.url,status.latestReadyRevisionName)'
```

## Local proxy use

```bash
cd /Users/creamybanana/genai-workshop/llm-wiki-teammate-package
export TOKENROUTER_API_KEY='your-tokenrouter-key'
python3 run-local.py
```

The local website can point at the printed local proxy endpoint. Clear any
cached proxy URL in the AI settings panel when switching between local and
Cloud Run services.
