# Package Contents

This folder was assembled from the active `llm-wiki` workspace on 2026-07-11.

- The app uses the four files in `outputs/attempt-002/` at runtime.
- The 25 saved prompt files are directly available in `skills/`, including the
  `上諭` review loop (`shangyu-review-loop.md`) and the new `上諭`—response
  pairing skill (`yu-response-pairing.md`).
- The terminal runners live as a loose, editable `scripts/` folder (this is now
  the working copy; they are no longer packed into the research archive).
- The review-bundle archive is extracted automatically by `run-local.py` so the
  Bundles drawer works immediately after the first launch.
- The archival workspace is intentionally compressed to keep the GitHub handoff
  tree small while retaining the original/OCR/cleaned source materials and
  supporting code/docs.

The package does not contain credentials. AI functions need a separately
authorized AI proxy, as described in `README.md`; the included proxy supports
Gemini and the TokenRouter-backed `gpt-5.4` route as well as other providers.
The standalone `chatgpt-proxy/` directory can be deployed separately when a
dedicated ChatGPT endpoint is preferred.

To refresh the two archives from an updated full workspace before sharing a new
version, run `python3 tools/refresh_archives.py /path/to/llm-wiki`.
