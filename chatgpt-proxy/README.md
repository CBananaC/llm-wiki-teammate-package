# Standalone ChatGPT proxy

This is a separate Cloud Run proxy for ChatGPT through TokenRouter. It uses
the OpenAI-compatible `POST /v1/chat/completions` endpoint and keeps the API
key on the server.

## Local run

From this directory:

```bash
export TOKENROUTER_API_KEY='your-key'
python3 -m pip install -r requirements.txt
python3 main.py
```

The service listens on `http://127.0.0.1:8080` by default. Set
`TOKENROUTER_BASE_URL` to override the default
`https://www.tokenrouter.tech/v1` endpoint.

## Deploy to Cloud Run

```bash
export TOKENROUTER_API_KEY='your-key'
bash deploy.sh
```

The key is read from the shell environment and is not committed to the
repository. For production, use a Cloud Run Secret Manager binding instead of
placing the credential directly in an environment-variable command.

## Endpoints

- `GET /` — health and active model
- `GET /providers` — provider metadata for the timeline settings panel
- `POST /models` — model discovery with a fallback to `gpt-5.4`
- `POST /chat` — summary, divide, ask, and structured review tasks
- `GET/POST /geocode` — historical place-name lookup passthrough

The `/chat` request format is compatible with the existing Gemini proxy. The
proxy ignores any browser-supplied API key and always uses
`TOKENROUTER_API_KEY` from its own environment.
