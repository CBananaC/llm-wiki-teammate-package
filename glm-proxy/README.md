# GLM proxy

Standalone Cloud Run proxy for GLM through the same OpenAI-compatible
TokenRouter provider used by the GPT proxy.

Defaults:

- Base URL: `https://www.tokenrouter.tech/v1`
- Model: `glm-5.2` (override with `GLM_MODEL`)
- Credential: `GLM_API_KEY` or `TOKENROUTER_API_KEY`

Deploy:

```bash
export GLM_API_KEY='your-key'
GLM_MODEL=glm-5.2 bash deploy.sh
```

Endpoints are `/`, `/providers`, `/models`, and `/chat`. The `/chat` contract
matches the existing Gemini/GPT proxy for summary, divide, ask, and structured
review tasks. The API key is read only from the service environment.
