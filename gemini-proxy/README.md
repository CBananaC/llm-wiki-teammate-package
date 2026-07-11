# Multi-provider AI proxy

This folder keeps its historical `gemini-proxy` name, but the service supports:

- Gemini through the public Gemini API or Vertex AI
- OpenAI GPT
- Anthropic Claude
- DeepSeek
- Third-party OpenAI-compatible APIs

The timeline sends every AI task to the same proxy URL with a `provider` and
provider-specific `model`. API base URLs and keys can be supplied by the
browser settings or configured as environment variables on the proxy.

## Deploy

```bash
cd gemini-proxy
bash deploy.sh
```

The deploy script configures Vertex AI as the default Gemini backend. Paste the
printed HTTPS URL into the timeline's AI settings. The other providers do not
need extra deployment flags when users enter their own key in the page.

For server-managed credentials, set any of these Cloud Run environment
variables after deployment:

```text
GEMINI_API_KEY
GEMINI_API_BASE_URL
OPENAI_API_KEY
OPENAI_BASE_URL
OPENAI_DEFAULT_MODEL
ANTHROPIC_API_KEY
ANTHROPIC_BASE_URL
ANTHROPIC_DEFAULT_MODEL
DEEPSEEK_API_KEY
DEEPSEEK_BASE_URL
DEEPSEEK_DEFAULT_MODEL
CUSTOM_API_KEY
CUSTOM_BASE_URL
CUSTOM_DEFAULT_MODEL
```

Comma-separated `*_ALLOWED_MODELS` variables can provide a model catalog for
each provider. Set `ENFORCE_MODEL_ALLOWLIST=1` only when requests must be
limited to that catalog.

## Endpoints

- `GET /` returns health and provider configuration.
- `GET /providers` returns provider labels, defaults, and fallback models.
- `POST /models` accepts `{provider, api_base, api_key}` and discovers models
  when the upstream service exposes a model-list endpoint.
- `POST /chat` accepts the document task plus `{provider, model, api_base,
  api_key}`.

The existing task modes such as `summary`, `divide`, `ask`, event extraction,
and source tracing all use the selected provider through this common route.

## Security

- Use an HTTPS proxy you control. A proxy operator can see any key sent from
  browser settings.
- Browser-entered keys are kept in session storage, so they are cleared when
  the tab session ends. Environment-configured keys never enter the browser.
- API base URLs are restricted to public HTTPS endpoints by default. Set
  `ALLOW_PRIVATE_API_BASES=1` only for a trusted private deployment.
- `ALLOW_ORIGIN` defaults to `*`. Set it to the review site's origin when the
  site is hosted at a stable URL.
- An unauthenticated Cloud Run service using Vertex AI can incur cost. Add
  authentication or restrict access before sharing the proxy publicly.

## Local verification

```bash
python -m unittest discover -s tests -v
```
