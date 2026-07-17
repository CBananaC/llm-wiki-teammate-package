# Project Log

This is the single progress record for human teammates, Codex, Claude, and
other agents. Read it before changing the project. After each coherent
adjustment, append one entry to the bottom of the change log.

## Current state

- Phase: active project; human validation of the formal and sample tools
- Formal review editor: none
- Canonical Stage 1 data: `review-tools/shared data/stage1_original_text.json`
- Formal review tool: `review-tools/(1) formal/index.html`
- Sample review tool: `review-tools/(2) sample/index.html`
- Model comparison: `review-tools/(3) model-output-comparison/index.html`
- Workflow map: `review-tools/(4) workflow/index.html`
- Research memory: `wiki/index.md`
- Google Cloud CLI/ADC account: `jhdgshhjs@gmail.com`
- Google Cloud billing account: `billingAccounts/010AE1-070B25-1144FD`

## Next priorities

1. Confirm that the sample shows 199 回應上諭 lines and loads the newest meaningful bundle.
2. Select a genuinely small, representative corpus for the sample tool.
3. Migrate active scripts from the original `outputs/attempt-002/` paths to the reorganized layout.
4. Classify shared review bundles as accepted, experimental, rejected, or archived.

## Known cautions

- The formal and sample HTML files still embed source/timeline data inherited from the original implementation.
- Some scripts and skill notes still refer to paths in the original project.
- Only one human or agent should edit `review-tools/(1) formal/formal_all.data` at a time.

## Logging rules

- Update the current-state sections when ownership, priorities, or risks change.
- Append one entry after a coherent file or data adjustment, not after every click, autosave, read-only inspection, or chat message.
- Every entry must state the author, summary, files changed, verification, and anything remaining.
- Before editing formal state, set `Formal review editor` above; clear it at handoff.
- Review-bundle completion files are research evidence, not substitutes for this log.
- If this file becomes unwieldy, choose an archive location then and leave a link here.

## Change log

### 2026-07-17 — Codex — Created the reorganized project

Summary: Created a clean working copy while preserving the original workspace.

Changed:
- Established formal and sample review modes under `review-tools/`.
- Limited `review-tools/shared data/` to the canonical Stage 1 JSON and review bundles.
- Preserved the LLM Wiki, research data, FYP writing, skills, scripts, and optional services.
- Unified `AGENTS.md` and `CLAUDE.md`.

Files:
- `review-tools/`
- `wiki/`
- `AGENTS.md`
- `CLAUDE.md`

Verified:
- Validated 323 JSON files and 36 Python files.
- Parsed embedded JavaScript in both review tools.
- Smoke-tested formal, sample, shared-data, bundle, skill, workflow, and status routes.
- Confirmed that the canonical Stage 1 JSON matches its source byte-for-byte.

Remaining:
- Human confirmation that the formal tool contains the expected research state.
- Sample reduction, legacy-script migration, and bundle classification.

### 2026-07-17 — Codex — Fixed sample pair count and bundle loading

Summary: Corrected the sample's older relationship snapshot and the bundle-detail API.

Changed:
- Gave sample an independent copy of the current formal confirmed-pair snapshot.
- Returned bundle manifests in `bundle.manifest` instead of applying `manifest.json` as skill output.

Files:
- `review-tools/(2) sample/confirmed-pairs.json`
- `review-tools/server.py`

Verified:
- Sample receives 278 confirmed pairs.
- The newest meaningful `yu-source` bundle exposes 11 pairs and 4 analyzed documents.
- Patched server and sample JavaScript passed syntax checks.

Remaining:
- Human visual confirmation of 199 回應上諭 lines and successful bundle loading.

### 2026-07-17 — Codex — Simplified progress tracking

Summary: Replaced the duplicated dashboard and task-file system with this single project log.

Changed:
- Removed the previous dashboard and multi-file task-tracking system.
- Updated human/agent instructions and active documentation to use `PROJECT_LOG.md`.
- Kept the `/status` webpage but changed its source to this log.

Files:
- `PROJECT_LOG.md`
- `AGENTS.md`
- `CLAUDE.md`
- `README.md`
- `review-tools/server.py`
- `review-tools/static/index.html`
- `review-tools/static/status.html`
- `review-tools/(2) sample/README.md`
- `wiki/README.md`
- `wiki/LOCAL_SETUP.md`
- `wiki/folder-structure.md`

Verified:
- `AGENTS.md` and `CLAUDE.md` remain byte-for-byte identical.
- No active documentation refers to the retired dashboard, task directory, or task IDs.

Remaining:
- Restart the local review server before using the updated `/status` page.

### 2026-07-17 — Codex — Simplified historical documents and FYP storage

Summary: Removed the unused historical-document archive and gave the FYP a clear home under second-hand material.

Changed:
- Removed the unreferenced `docs/` directory and its old review-tool session report.
- Replaced `manuscript/` with `Second hand material/FYP/`.
- Moved the FYP Word document without modifying its contents.

Files:
- `Second hand material/FYP/FYP_Essay.docx`
- `README.md`
- `wiki/folder-structure.md`
- `PROJECT_LOG.md`

Verified:
- The moved FYP document has the same SHA-256 hash as the original location.
- No active documentation outside this historical log refers to `docs/` or `manuscript/`.

Remaining:
- None.

### 2026-07-17 — Codex — Promoted the model-output comparison tool

Summary: Moved the model-comparison HTML out of attempt storage and made it a named review tool.

Changed:
- Moved and renamed `research-data/attempts/attempt-002/model-output-comparison.html` to `review-tools/(3) model-output-comparison/index.html`.
- Updated its default source and bundle paths to the shared review-tool data.
- Added the `/model-output-comparison` server route and launcher button.

Files:
- `review-tools/(3) model-output-comparison/index.html`
- `review-tools/server.py`
- `review-tools/static/index.html`
- `review-tools/static/app.js`
- `README.md`
- `review-tools/README.md`
- `wiki/folder-structure.md`
- `PROJECT_LOG.md`

Verified:
- The comparison HTML and launcher JavaScript pass syntax checks.
- The comparison route loads the renamed HTML.
- The canonical Stage 1 JSON and example review-bundle paths are reachable.

Remaining:
- None.

### 2026-07-17 — Codex — Consolidated project tooling

Summary: Grouped proxy services, Markdown skills, and Python scripts under one tool folder.

Changed:
- Moved `services/` to `tool/proxy/`.
- Moved `skills/` to `tool/skills md/`.
- Moved `scripts/` to `tool/scripts py/`.
- Migrated server, local launcher, workflow map, wiki links, script roots, prompt paths, and documentation to the new locations.

Files:
- `tool/proxy/`
- `tool/skills md/`
- `tool/scripts py/`
- `run-local.py`
- `review-tools/server.py`
- `review-tools/(4) workflow/`
- `AGENTS.md`
- `CLAUDE.md`
- `README.md`
- `wiki/`
- `PROJECT_LOG.md`

Verified:
- All Python files pass syntax compilation from their new locations.
- The server loads all Markdown skills from `tool/skills md/`.
- The workflow source map resolves both skills and scripts in the new folders.
- `run-local.py` resolves the Gemini proxy from `tool/proxy/`.
- `AGENTS.md` and `CLAUDE.md` remain byte-for-byte identical.

Remaining:
- Some legacy scripts still refer to the original data/output layout; that migration remains a separate cleanup.

### 2026-07-17 — Codex — Removed non-canonical research-data storage

Summary: Removed the entire research-data holding area at the user's direction.

Changed:
- Deleted the alternate Stage 1 dataset, enriched dual-timeline copy, and historical pairing outputs.
- Deleted the empty `sources/` and `derived/` placeholders.
- Removed `research-data/` from the documented project structure and current cautions.

Files removed:
- `research-data/`

Verified:
- `review-tools/shared data/stage1-date-adjusted.json` remains intact as the canonical Stage 1 source.
- Formal and sample state, relationship JSON, and shared review bundles remain intact.
- The promoted model-output comparison remains at `review-tools/(3) model-output-comparison/index.html`.

Remaining:
- Legacy scripts that expect `outputs/attempt-002/dual-timeline-data.json` still require a separate data-path decision before they can run.

### 2026-07-17 — Codex — Numbered the review surfaces and removed static

Summary: Made the four review surfaces visibly ordered and retired the separate static launcher.

Changed:
- Renamed the folders to `(1) formal`, `(2) sample`, `(3) model-output-comparison`, and `(4) workflow`.
- Removed `review-tools/static/` and its launcher/status assets.
- Made `/` open the formal review tool directly.
- Kept `/formal`, `/sample`, `/model-output-comparison`, and `/workflow/` as stable browser routes.
- Made `/status` serve `PROJECT_LOG.md` directly without a separate status page.
- Updated collaborator instructions and active setup/structure documentation.

Files:
- `review-tools/(1) formal/`
- `review-tools/(2) sample/`
- `review-tools/(3) model-output-comparison/`
- `review-tools/(4) workflow/`
- `review-tools/server.py`
- `review-tools/README.md`
- `README.md`
- `AGENTS.md`
- `CLAUDE.md`
- `wiki/LOCAL_SETUP.md`
- `wiki/folder-structure.md`
- `PROJECT_LOG.md`

Files removed:
- `review-tools/static/`

Verified:
- All 36 Python files pass syntax parsing.
- Embedded JavaScript in formal, sample, and comparison plus the workflow JavaScript pass syntax checks.
- Formal, sample, comparison, workflow, status, skills, bundle, and workflow-source routes pass local smoke tests.
- `/` returns the same formal HTML as `/formal`; the former static path returns 404.
- `AGENTS.md` and `CLAUDE.md` remain byte-for-byte identical.
- Formal state, sample state, and canonical Stage 1 data are preserved during installation.

Remaining:
- The review server is running on port 8768. The optional Gemini proxy is still unavailable because Flask is not installed; the four review surfaces work without it.

### 2026-07-17 — Codex — Renamed shared storage to shared data

Summary: Gave the review tools' common data folder a clearer human-readable name.

Changed:
- Renamed `review-tools/shared/` to `review-tools/shared data/`.
- Updated the server, collaborator instructions, HTML source metadata, and active documentation to the new disk path.
- Kept the browser route `/shared/` unchanged for compatibility with the review interfaces.

Files:
- `review-tools/shared data/`
- `review-tools/server.py`
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `review-tools/README.md`
- `README.md`
- `AGENTS.md`
- `CLAUDE.md`
- `wiki/LOCAL_SETUP.md`
- `wiki/folder-structure.md`
- `PROJECT_LOG.md`

Verified:
- The canonical Stage 1 file retained its SHA-256 hash.
- Stage 1 data and all 57 review bundles load through the server.
- Formal and sample embedded JavaScript pass syntax checks.
- All 36 Python files pass syntax parsing.
- `AGENTS.md` and `CLAUDE.md` remain byte-for-byte identical.

Remaining:
- The review server is running on port 8768. The optional Gemini proxy still requires Flask; shared data and all four review surfaces work without it.

### 2026-07-17 — Codex — Renamed formal and sample aggregate state files

Summary: Replaced the old edits-oriented filenames with names that describe each mode's complete saved overlay.

Changed:
- Renamed formal `timeline-edits.json` to `formal_all.data`.
- Renamed sample `sample-edits.json` to `sample_all.data`.
- Updated server persistence, HTML comments, export filenames, import-file filters, collaborator rules, and documentation.

Files:
- `review-tools/(1) formal/formal_all.data`
- `review-tools/(2) sample/sample_all.data`
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `review-tools/server.py`
- `AGENTS.md`
- `CLAUDE.md`
- `wiki/LOCAL_SETUP.md`
- `PROJECT_LOG.md`

Relationship audit:
- `confirmed-pairs.json` contains all 154 pair identities and fields from `yu-pairing.json`.
- It contains none of the 11 `yu-source.json` pairs.
- It contains 14 of 20 `zhu-pairing.json` pair identities; 9 preserve the full candidate object exactly and 5 have different evidence.
- It does not contain any source file's `analyzed` list and therefore is not a complete replacement for the three files.

Verified:
- Both `.data` files remain valid JSON and retain their pre-rename hashes during installation.
- Formal and sample state APIs load the renamed files.
- Both pages and their embedded JavaScript pass smoke and syntax tests.
- All 36 Python files pass syntax parsing.
- `AGENTS.md` and `CLAUDE.md` remain byte-for-byte identical.

Remaining:
- The review server is running on port 8768. The optional Gemini proxy still requires Flask; both state APIs and review pages work without it.

### 2026-07-17 — Codex — Removed duplicated candidate pairing outputs

Summary: Kept curated runtime relationships beside each HTML and removed duplicate candidate-generation files.

Changed:
- Removed `yu-pairing.json` and `zhu-pairing.json` from both formal and sample folders.
- Changed both HTML startup loaders to read only their local `confirmed-pairs.json`.
- Removed the startup code that converted `yu-pairing.json` candidates into saved review suggestions.
- Updated collaborator instructions and the documented folder structure.

Files removed:
- `review-tools/(1) formal/yu-pairing.json`
- `review-tools/(1) formal/zhu-pairing.json`
- `review-tools/(2) sample/yu-pairing.json`
- `review-tools/(2) sample/zhu-pairing.json`

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `AGENTS.md`
- `CLAUDE.md`
- `wiki/folder-structure.md`
- `PROJECT_LOG.md`

Verified:
- Both pages load all 278 curated relationships from `confirmed-pairs.json`.
- Removed candidate-file URLs return 404 and are no longer requested by either HTML.
- Formal and sample embedded JavaScript pass syntax checks.
- `AGENTS.md` and `CLAUDE.md` remain byte-for-byte identical.
- Candidate provenance remains recoverable from 8 `yu-pairing` and 5 `zhu-pairing` files in shared review bundles.

Remaining:
- Existing candidate-derived chat records inside `formal_all.data` or `sample_all.data` were deliberately preserved as review history.

### 2026-07-17 — Codex — Renamed response relations and retired prior reports

Summary: Replaced ambiguous relationship labels across the active project and
removed the `prior_report` relationship type and its review feature.

Changed:
- Renamed `reply_to_yu` to `official_reply_to_yu`.
- Renamed `reply_to_zhu` to `official_reply_to_emperor_zhu`.
- Removed the single confirmed `prior_report` pair (`硃224` → `硃238`) and its
  duplicated structured records from formal saved state.
- Removed the prior-report action, prompt, matching code, renderer branches,
  runner, saved skill, and obsolete one-off HTML patch script.
- Added legacy-bundle import normalization: old response labels are converted
  in memory and old `prior_report` records are ignored. Historical bundle files
  remain unchanged as provenance.
- Documented the two current confirmed relationship values.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(1) formal/confirmed-pairs.json`
- `review-tools/(1) formal/formal_all.data`
- `review-tools/(2) sample/index.html`
- `review-tools/(2) sample/confirmed-pairs.json`
- `review-tools/(2) sample/sample_all.data`
- `review-tools/README.md`
- `tool/scripts py/`
- `tool/skills md/`
- `wiki/skills.md`
- `PROJECT_LOG.md`

Files removed:
- `tool/scripts py/run_prior_report_pairing.py`
- `tool/scripts py/patch_yu_source_loader.py`
- `tool/skills md/prior-report-pairing.md`

Verified:
- Both confirmed files are identical and contain 277 pairs: 263
  `official_reply_to_yu` and 14 `official_reply_to_emperor_zhu`.
- Formal state migrated 1,319 old 上諭-reply labels and 122 old 硃批-reply
  labels; 461 duplicated `prior_report` scalar occurrences were removed with
  their containing pair/chat records. Sample state migrated 518 old 上諭-reply
  labels. Top-level state keys were preserved.
- Both HTML files, all 24 remaining Python scripts, both state files, and both
  confirmed files pass syntax/JSON checks.
- Formal, sample, comparison, workflow, confirmed-file, and state routes pass
  staged local smoke tests.
- `AGENTS.md` and `CLAUDE.md` remain byte-for-byte identical.

Remaining:
- The optional Gemini proxy still requires Flask; all four review surfaces and
  their local data work without it.

### 2026-07-17 — Codex — Added the GitHub source link to service documentation

Summary: Linked the proxy/service guide to the requested GitHub repository and
repeated the no-push protocol where service redeployment instructions live.

Changed:
- Added the repository link and push protocol to
  `tool/proxy/PROXY_WEBSITES.md`.

Verified:
- `AGENTS.md` and `CLAUDE.md` remain byte-for-byte identical.
- No `git push` was executed by Codex.

### 2026-07-17 — Codex — Switched Google Cloud authentication account

Summary: Updated local Google Cloud user authentication and ADC from the
exhausted Appleisblue account to `jhdgshhjs@gmail.com`.

Changed:
- Authenticated `jhdgshhjs@gmail.com` with `gcloud auth login --update-adc`.
- Set it as the active gcloud account for project `delta-entry-496910-e7`.
- Granted the new account project Editor access using the existing Appleisblue
  owner credential. The organization policy rejected an external `roles/owner`
  binding (`ORG_MUST_INVITE_EXTERNAL_OWNERS`), so Editor is the permitted
  operational replacement.
- Left the old Appleisblue credential stored but inactive as a fallback; no
  project source file contained a hard-coded Appleisblue email.
- Preserved `GOOGLE_APPLICATION_CREDENTIALS`, which points to the dedicated
  Vision OCR service account rather than the old user account.

Verified:
- Active gcloud account: `jhdgshhjs@gmail.com`.
- ADC token is available under the new login.
- New account can access the project, list all Cloud Run services, list the Gen
  2 `mail-digest` Cloud Function, and list project service accounts.

Remaining:
- The old user credential remains available but inactive. The project billing
  account and any free-credit allocation are separate from the login account;
  changing users does not transfer project billing credits.

### 2026-07-17 — Codex — Enabled proxy deployment under the new account

Summary: Completed the operational permission migration needed for
`jhdgshhjs@gmail.com` to deploy and run this project’s proxies and Cloud
Functions.

Changed:
- Added the existing project-level AI/data roles to the new account:
  Vertex AI, Datastore, Document AI, Secret Manager, and Service Usage.
- Added `roles/iam.serviceAccountUser` for the new account on the default
  compute, Document AI OCR, and mail-digest runtime service accounts.
- Kept project Editor as the broadest permitted user role; external Owner was
  blocked by the organization policy.

Verified:
- The new account can access the project and list all Cloud Run services.
- It can list the Gen 2 `mail-digest` Cloud Function and service accounts.
- All four deployed proxy websites returned `ok: true` from their health
  endpoints: Gemini, ChatGPT, DeepSeek, and GLM.
- Active gcloud account remains `jhdgshhjs@gmail.com`; ADC remains available.

Remaining:
- Local `run-local.py` still reports the optional Flask proxy dependency as
  unavailable; deployed Cloud Run proxies are healthy and usable.

### 2026-07-17 — Codex — Relinked proxy project to the new billing account

Summary: Moved the project’s Cloud Billing association from the old account to
the open billing account available to `jhdgshhjs@gmail.com`.

Changed:
- Relinked `delta-entry-496910-e7` from
  `billingAccounts/013832-166089-56CBE6` to
  `billingAccounts/010AE1-070B25-1144FD`.
- Added the required `roles/billing.projectManager` project role to the new
  account; it already had Billing Admin on the target billing account.

Verified:
- Project billing is enabled and reports the new billing account.
- All four proxy Cloud Run services remain listed and available.
- The Gen 2 `mail-digest` Cloud Function remains active.

Remaining:
- Whether the target billing account’s promotional credit is still available
  must be confirmed in Google Cloud Billing; the CLI exposes the account but not
  the remaining promotional-credit balance.

### 2026-07-17 — Codex — Prepared GitHub publication without pushing

Summary: Connected the reorganized project to the requested GitHub repository
locally and added a no-agent-push rule.

Changed:
- Added the repository reference to the project README and collaborator rules:
  <https://github.com/CBananaC/llm-wiki-teammate-package>.
- Added a safety `.gitignore` for credentials, service-account files, local
  environments, caches, and macOS metadata.
- Prepared the project for a local Git repository and commit; no remote push was
  executed.
- Added the rule that agents must provide, but never execute, `git push`, with
  an explicit `cd` first.

Verified:
- The Downloads project had no existing `.git` directory or remote.
- The GitHub repository exists and its current `main` branch has unrelated
  legacy history; publishing this reorganized folder will require the user’s
  explicit force-with-lease push command.
- `AGENTS.md` and `CLAUDE.md` remain byte-for-byte identical.

Remaining:
- The user must run the prepared force-with-lease push command if they want the
  reorganized folder to replace the current GitHub `main` branch.

### 2026-07-17 — Codex — Centralized proxy deployment and collaborator rules

Summary: Created a canonical quick-reference for every project proxy website
and made paired HTML edits and explicit working directories mandatory.

Changed:
- Moved the proxy deployment note from the prompt-skill folder to
  `tool/proxy/PROXY_WEBSITES.md`, where infrastructure documentation belongs.
- Verified and listed the four current Cloud Run proxy websites for Gemini,
  ChatGPT, DeepSeek, and GLM.
- Kept copy-pasteable redeployment blocks for every proxy, each beginning with
  its exact absolute `cd` command.
- Added a collaborator rule requiring equivalent changes to both formal and
  sample HTML whenever either is edited, unless the user explicitly requests a
  documented mode-specific difference.
- Added a collaborator rule requiring every terminal command supplied to the
  user to include an explicit `cd` to the required working directory.
- Added a collaborator rule requiring short semantic review-bundle names;
  document-ID lists must be stored in the manifest rather than the bundle name.
- Added the proxy guide to the top-level project index and corrected its local
  startup example to include `cd`.

Files:
- `tool/proxy/PROXY_WEBSITES.md`
- `README.md`
- `AGENTS.md`
- `CLAUDE.md`
- `PROJECT_LOG.md`

File moved:
- `tool/skills md/deploy-ai-proxies.md` → `tool/proxy/PROXY_WEBSITES.md`

Verified:
- Google Cloud Run reports the four documented proxy URLs and current ready
  revisions in project `delta-entry-496910-e7`, region `asia-east1`.
- Every shell block in `tool/proxy/PROXY_WEBSITES.md` includes an explicit
  absolute `cd` command.
- Collaborator instructions prohibit long number or document-ID lists in
  review-bundle names.
- `AGENTS.md` and `CLAUDE.md` remain byte-for-byte identical.

Remaining:
- Actual API keys remain intentionally absent from the project; ChatGPT and GLM
  redeployment requires the documented environment variable or an existing
  Cloud Run service configuration.

### 2026-07-17 — Codex — Renamed the canonical original-text dataset

Summary: Renamed the shared Stage 1 JSON so its role as the canonical original
text corpus is explicit.

Changed:
- Renamed `review-tools/shared data/stage1-date-adjusted.json` to
  `review-tools/shared data/stage1_original_text.json`.
- Updated both review HTML loaders and embedded source metadata.
- Updated the review server, active Python scripts, skills, collaborator
  instructions, top-level documentation, and wiki references.
- Preserved historical review-bundle manifests and earlier log entries as
  provenance rather than rewriting records of past runs.

Files:
- `review-tools/shared data/stage1_original_text.json`
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `review-tools/server.py`
- `tool/scripts py/`
- `tool/skills md/`
- `README.md`
- `review-tools/README.md`
- `AGENTS.md`
- `CLAUDE.md`
- `wiki/`
- `PROJECT_LOG.md`

Verified:
- The renamed JSON retained SHA-256
  `200a96a20d0f6b0d4eaf248faf36fc3faeb44e8e8825d4c49dc47f3a352acc14`.
- No active file outside historical bundles and earlier log entries refers to
  `stage1-date-adjusted.json`.
- Both review HTML files and all Python scripts pass syntax checks.
- `AGENTS.md` and `CLAUDE.md` remain byte-for-byte identical.
- Formal, sample, shared-data, comparison, workflow, and state routes pass live
  smoke tests on port 8768.

Remaining:
- The optional Gemini proxy still requires Flask; all four review surfaces and
  their local data work without it.
