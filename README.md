# LLM Wiki Timeline — Teammate Package

This is the compact, runnable handoff copy of the 林爽文 timeline review site.
It is deliberately separate from the full research workspace.

## Start the site

Requires Python 3.10 or newer; no packages need to be installed for the core
website.

```bash
python3 run-local.py
```

The first start expands `archives/review-bundles.zip` into
`outputs/review-bundles/`. Then open <http://127.0.0.1:8766>.
The extracted folder is ignored by Git because the archive is the canonical
handoff copy; do not commit both.

If port 8766 is already occupied, choose another local port, for example:

```bash
LLM_WIKI_PORT=8767 python3 run-local.py
```

Keep the terminal open while using the site. Do not open the HTML file directly
with `file://`: the local server is what loads shared skills and bundles and
saves large timeline edits safely.

## What is included

```text
review-app/                 Local server and browser bridge
outputs/attempt-002/        Active timeline HTML, timeline JSON, and saved edits
skills/                     Saved prompts / task specifications
archives/review-bundles.zip All previous review bundles and large generated outputs
archives/research-workspace.zip
                            Original/OCR/cleaned source materials, scripts, and docs
gemini-proxy/               Optional multi-provider AI proxy and historical-place tools
chatgpt-proxy/              Standalone TokenRouter ChatGPT proxy for Cloud Run
```

The full timeline, including the original documents used by the active site, is
embedded in `outputs/attempt-002/stage1-timeline.html`. The accompanying JSON
files preserve the editable timeline data and source metadata.

## Optional AI tools

The review, edit, export, skills, and saved-bundle functions work locally. AI
chat, AI extraction, and place lookup use the included AI proxy. `run-local.py`
starts it automatically and exposes it through the same local origin, so the
normal setup does not need a separate proxy URL. The Settings panel supports
Gemini/Google Cloud, OpenAI GPT, ChatGPT via TokenRouter (`gpt-5.4`),
Anthropic Claude, DeepSeek, and third-party OpenAI-compatible APIs. Choose a
provider, then enter that provider's model, API base URL, and API key when
needed.

API keys entered in the page are held in browser session storage and sent only
to the configured proxy. Deploy and trust your own HTTPS proxy for shared use,
or configure keys as proxy environment variables so they never enter the
browser. Never commit credentials, API keys, or `.env` files.

Map and relationship-graph panels also load public JavaScript libraries and map
tiles when opened, so they need an internet connection.

## Accessing the archival workspace

`archives/research-workspace.zip` is a compact record of the original sources,
OCR/cleaned JSON and text, processing scripts, and project documentation. It is
not needed to run the website. Extract it beside this README only when you need
to inspect or reproduce those research artifacts.

## GitHub

Upload this folder as its own repository. Do not add `node_modules/`,
`__pycache__/`, `.DS_Store`, service-account files, or `.env` files. The active
saved state at `outputs/attempt-002/timeline-edits.local.json` must be included.

Do not have two people edit that JSON state on the same branch simultaneously;
commit/pull between editing sessions or use separate branches.
