# Package Contents

This folder was assembled from the active `llm-wiki` workspace on 2026-07-10.

- The app uses the four files in `outputs/attempt-002/` at runtime.
- The 24 saved prompt files are directly available in `skills/`.
- The review-bundle archive is extracted automatically by `run-local.py` so the
  Bundles drawer works immediately after the first launch.
- The archival workspace is intentionally compressed to keep the GitHub handoff
  tree small while retaining the original/OCR/cleaned source materials and
  supporting code/docs.

The package does not contain credentials. AI functions need a separately
authorized Gemini proxy, as described in `README.md`.

To refresh the two archives from an updated full workspace before sharing a new
version, run `python3 tools/refresh_archives.py /path/to/llm-wiki`.
