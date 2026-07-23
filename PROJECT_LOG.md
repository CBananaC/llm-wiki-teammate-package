# Project Log

This is the single progress record for human teammates, Codex, Claude, and
other agents. Read it before changing the project. After each coherent
adjustment, append one entry to the bottom of the change log.

## Current state

- Phase: active project; human validation of the formal/sample tools and preparation of the competition hand-in
- Formal review editor: none (原文 label alignment complete; human refresh next)
- Canonical Stage 1 data: `review-tools/shared data/stage1_original_text.json`
- Formal review tool: `review-tools/(1) formal/index.html`
- Sample review tool: `review-tools/(2) sample/index.html`
- Model comparison: `review-tools/(3) model-output-comparison/index.html`
- Workflow map: `review-tools/(4) workflow/index.html`
- Research memory: `wiki/index.md`
- Student-facing deliverable: a dynamic introduction and teaching website for the review system
- Context folders: `2nd Material & FYP/` and `Competition Info/`
- Google Cloud CLI/ADC account: `jhdgshhjs@gmail.com`
- Google Cloud billing account: `billingAccounts/010AE1-070B25-1144FD`

## Next priorities

1. Plan and build the dynamic introduction/teaching website, using the competition brief as a provisional requirements reference.
2. Confirm that the sample shows 199 回應上諭 lines and loads the newest meaningful bundle.
3. Select a genuinely small, representative corpus for the sample tool.
4. Migrate active scripts from the original `outputs/attempt-002/` paths to the reorganized layout.
5. Classify shared review bundles as accepted, experimental, rejected, or archived.

## Known cautions

- The formal and sample HTML files still embed source/timeline data inherited from the original implementation.
- Some scripts and skill notes still refer to paths in the original project.
- Only one human or agent should edit `review-tools/(1) formal/formal_all.data` at a time.
- `Competition Info/2026 PolyU AI X Digital Humanities Awards_AI_Classics(v.1).docx` is a bilingual public draft with unresolved placeholders and visible table/formatting inconsistencies; verify official rules before publishing dates, weights, links, or contacts.
- `2nd Material & FYP/` contains secondary scholarship, FYP working notes, extracted text, maps, and GIS material. Verify quotations, page references, licensing, and historical claims against the underlying sources before using them publicly.

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

### 2026-07-17 — Codex — Expanded yu_source discovery and evidence display

Summary: Ported Claude's expanded source-pairing work into the reorganized
project and merged its 14 sample-mode relationships without restoring the
retired `prior_report` feature.

Changed:
- Expanded the pairing workflow to discover named `據…奏` sources,
  `等奏` co-reporters, and unlabelled narrative facts ranked by content
  overlap within the fixed receipt window.
- Added segmented evidence fields (`yu_span_type`, `match_basis`,
  `memorialist`, and `segments`) to the runner and source-pair cards.
- Fixed static `yu-source.json` loading so it is applied after server-backed
  state is ready; both formal and sample tools use their reorganized routes.
- Added Claude's 14 `yu_source` relationships to
  `review-tools/(2) sample/sample_all.data` for 諭20、諭28、諭24、諭27.
- Registered the adapted skill and runner in the workflow source map.

Files:
- `tool/skills md/yu-source-pairing.md`
- `tool/scripts py/run_yu_source_pairing.py`
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `review-tools/(2) sample/sample_all.data`
- `review-tools/server.py`
- `PROJECT_LOG.md`

Verified:
- Python compilation, JSON parsing, and embedded JavaScript syntax checks pass.
- The runner dry-run for 諭20 produces named, corroborating, and content-ranked
  candidates using the reorganized shared-data path.
- A temporary server on port 8770 served both `yu-source.json` routes and
  exposed the new skill/script workflow sources.
- Sample state now contains 14 `yu_source` `__docPairs` with 23 evidence
  segments; formal and sample HTML received equivalent logic changes.

Remaining:
- Human visual review of the new segmented source cards is still recommended.

### 2026-07-17 — Codex — Added research shorthand

Summary: Documented the project's shorthand for 硃批 and 上諭 documents and
the left-to-right ordinal convention for the website's four-line chart.

Files:
- `AGENTS.md`
- `CLAUDE.md`
- `PROJECT_LOG.md`

Verified:
- `AGENTS.md` and `CLAUDE.md` contain the same updated guidance.
- The rules define `zhu` as `doc_type` 硃批, `yu` as `doc_type` 上諭, and `1st`
  as the chart's leftmost line, 戰場事件.

Remaining:
- None.

### 2026-07-17 — Codex — Corrected Yu–Zhu chart connection endpoint

Summary: Updated the mixed 上諭／硃批 pair line so it connects to the 硃批's
third-line imperial-side dot and marks that connected 硃批 with a green ring.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`

Verified:
- Both HTML files' embedded JavaScript parsed successfully.
- `git diff --check` passed.
- The endpoint and ring logic handles either document order in mixed pairs.

Remaining:
- Human visual confirmation in the chart is recommended.

### 2026-07-17 — Codex — Made yu_source Zhu markers selection-aware

Summary: The green circle for a `yu_source` Zhu now appears only when that Zhu
or its connected Yu is selected.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both HTML files' embedded JavaScript parsed successfully.
- `git diff --check` passed.

Remaining:
- Human visual confirmation in the chart is recommended.

### 2026-07-17 — Codex — Updated yu_source Yu–Zhu links

Summary: Changed only mixed `yu_source` links to connect the Yu and Zhu on
their third-line imperial-side dots and added a green ring to the Zhu dot.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both HTML files' embedded JavaScript parsed successfully.
- `git diff --check` passed.
- Official Yu/Zhu reply-pair rendering remains on the Zhu's second line with
  no green marker.

Remaining:
- Human visual confirmation in the chart is recommended.

### 2026-07-17 — Codex — Restored official Yu–Zhu pair rendering

Summary: Restored both official Yu/Zhu reply relations to connect the Yu's
third-line dot to the Zhu's second-line dot, with no green Zhu circle.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both HTML files' embedded JavaScript parsed successfully.
- `git diff --check` passed.
- The mixed-pair branch uses the original second-line Zhu endpoint.

Remaining:
- Human visual confirmation in the chart is recommended.

### 2026-07-17 — Codex — Scoped Yu–Zhu endpoint correction

Summary: Limited the third-line connection and green Zhu ring to the direction
where a 硃批 document replies to an 上諭; the reverse 上諭-to-硃批 direction
retains its previous rendering.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both HTML files' embedded JavaScript parsed successfully.
- `git diff --check` passed.
- The opposite mixed-pair direction uses the original side-selection branch.

Remaining:
- Human visual confirmation in the chart is recommended.

### 2026-07-17 19:15 HKT — Codex — Added timestamp and end-of-day logging rules

Summary: Required timestamps for new progress entries and documented the
end-of-day summary workflow.

Files:
- `AGENTS.md`
- `CLAUDE.md`
- `PROJECT_LOG.md`

Verified:
- Both instruction files require each new progress entry to include the date
  and time in `Asia/Hong_Kong` using `YYYY-MM-DD HH:MM`.
- Both instruction files require an end-of-day summary to review all progress
  entries for that date and append the summary without replacing them.
- The mandated agent-document synchronization check and byte-for-byte check
  passed after this log update.

Remaining:
- None.

### 2026-07-17 19:24 HKT — Codex — Highlighted source author in Yu–source output cards

Summary: Added a green author highlight for the source 硃批's author wherever
that author's name appears in the matched 上諭 quotation. This covers the
ordinary single-quotation path as well as the existing segmented source path.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- 諭13／硃24 resolves the source author as 徐嗣曾.
- The rendered quote path produces a green `dp-hl-author` mark around 徐嗣曾
  in `又據徐嗣曾由六百里馳奏…`.
- Both HTML files' embedded JavaScript parsed successfully.
- `git diff --check` passed.

Remaining:
- Human visual confirmation of the card in formal and sample views.

### 2026-07-17 19:27 HKT — Codex — Limited source-author highlight to 據…奏 attribution

Summary: Restricted the green source-author highlight to the author occurrence
inside the 上諭's `據…奏` attribution clause, leaving later occurrences such as
`徐嗣曾上奏` unhighlighted.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- The attribution occurrence in `又據徐嗣曾由六百里馳奏…` is eligible.
- A later `徐嗣曾上奏` occurrence is not eligible.
- Both HTML files' embedded JavaScript parsed successfully.
- `git diff --check` passed.

Remaining:
- Human visual confirmation of the card in formal and sample views.

### 2026-07-17 19:44 HKT — Codex — End-of-day summary

Summary: Reorganized the DH research workspace into a cleaner, documented
review system and refined the Yu–source and Yu–Zhu relationship displays.

Completed:
- Established numbered formal, sample, model-comparison, and workflow review
  surfaces with shared canonical data and isolated saved state.
- Consolidated proxy services, skills, and scripts under `tool/`; removed
  obsolete research-data, static launcher, dashboard, task, and duplicate
  pairing storage.
- Migrated and documented the project structure, progress log, FYP storage,
  service deployment configuration, GitHub publication preparation, and the
  new Google Cloud account/billing setup without pushing changes.
- Corrected sample pair and bundle loading, expanded `yu_source` discovery and
  evidence segmentation, and added 14 sample relationships.
- Refined chart endpoints, selection-aware Zhu markers, official Yu–Zhu
  rendering, and source-author highlighting limited to `據…奏` attribution.
- Added research shorthand and timestamp/end-of-day logging rules while
  keeping `AGENTS.md` and `CLAUDE.md` synchronized.

Files changed: Review-tool HTML/server files, shared review bundles, formal and
sample state, `tool/` scripts and skills, project documentation, and
`PROJECT_LOG.md`; no formal state was edited.

Verified: Repeated Python/JSON/embedded-JavaScript syntax checks, route and
workflow smoke tests, data/hash preservation checks, `git diff --check`, and
agent-document synchronization checks passed. The current working tree also
contains the latest Yu–source bundle and sample-state updates as uncommitted
changes.

Remaining:
- Human visual confirmation of the formal/sample charts and segmented source
  cards.
- Confirm 199 sample 回應上諭 lines and the newest meaningful bundle.
- Choose a small representative sample corpus, migrate legacy output paths,
  classify review bundles, and decide how legacy scripts should access data.
- Optional Gemini proxy use still requires Flask; the review surfaces work
  without it.

### 2026-07-18 13:35 HKT — Codex — Added source-document IDs to Yu–source cards

Summary: The official source document in 上諭—來源配對 cards now shows its ID
after the title, for example `〈為接咨挑選戰兵預備赴臺策應並擬親赴潮州事〉（硃71）`.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- The ID suffix is rendered only for `yu_source` cards.
- Other pairing-card title displays remain unchanged.
- Both HTML files' embedded JavaScript parsed successfully.
- `git diff --check` passed.

Remaining:
- Human visual confirmation of the source-document title and ID in formal and sample views.

### 2026-07-18 13:35 HKT — Codex — Reordered Yu–source cards around the official source

Summary: 上諭—來源配對 cards now show the official source document and quote
first, followed by `◀ 據奏來源`, then the 上諭 document and quote. Other pairing
card directions retain their existing order.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- `yu_source` uses source → connector → 上諭 ordering.
- Non-source pairing cards retain 上諭／硃批 → connector → official-document ordering.
- Both HTML files' embedded JavaScript parsed successfully.
- `git diff --check` passed.

Remaining:
- Human visual confirmation of the reordered source card in formal and sample views.

### 2026-07-18 13:38 HKT — Codex — Added horizontal dot-distance control

Summary: Added a `圓點水平距離` slider below `圓點大小` in the header Tools
menu to adjust the horizontal spacing between dots sharing a date.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both HTML files' embedded JavaScript parsed successfully.
- `git diff --check` passed.
- The control defaults to the existing `12 px` spacing and persists via
  `localStorage`.

Remaining:
- Human visual confirmation of the new header slider and chart spacing.

### 2026-07-18 14:10 HKT — Claude — Added configurable network-reach control (formal + sample)

Summary: Replaced the hard-coded highlighted-network walk (only the
response-chain edge recursed without limit; source docs, matched-memorial
link, info-source citations, and sibling events were each a fixed single
hop) with one configurable breadth-first walk. A new `網絡範圍` panel
(top-right toolbar button) lets the user set, per relationship type
(response chain, 諭↔回應 pairing, 諭→對應奏摺 memDoc, 事件→來源文件,
文件→其他相關事件 sibling, 諭→引用文件 info-source), how many hops from
the clicked dot/event that relationship may extend (0 = off, 1–4, or ∞).
The panel shows a live per-type node count and a total-lit-nodes summary
after every click, and re-highlights immediately when a setting changes.
Settings are global, so the same configuration is automatically applied to
every dot clicked (the user's "apply the same setting to other dots"
request). Configurations can be saved/loaded as named presets, one preset
can be marked default (auto-applied on load), and a node-count safety cap
flags/truncates runaway selections. All settings persist via
`localStorage` (`timelineReachSettings`, `timelineReachPresets`,
`timelineReachDefaultPreset`), matching the existing pattern used for
other chart display prefs. Applied the identical change to both formal
and sample per the formal/sample isolation rule (no mode-specific
divergence).

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Extracted the BFS traversal logic and unit-tested it against a synthetic
  event/document graph: single-type reach (source-only), multi-type reach
  (memDoc), full defaults, sibling-reach disabled (confirms fan-out stops
  as intended), doc-click seeding via pairing, and the node budget cap —
  all six cases produced the expected node sets.
- Both HTML files' embedded JavaScript (`new Function(...)` over the
  extracted `<script>` body) parsed successfully.
- Diffed the injected settings-module and panel code between the formal
  and sample files: byte-identical.

Remaining:
- Human visual/interactive confirmation of the panel and highlighting in
  both formal and sample views.
- Formal review editor field was not set before the initial formal-only
  edit earlier in this session (protocol step 2 missed); noting it here
  since the sample sync just completed under the editor field, now
  cleared.

### 2026-07-18 16:06 HKT — Claude — Retired the redundant outer column bar; unified 總摘要/原文 BODY section styling (formal + sample)

Summary: Implemented the UI change approved from the earlier before/after
sample (see prior chat sample, not committed to the repo). Two changes,
applied identically to both tools:
1. The outer `.ws-list-bar` / `.ws-tools` bar (`筆記／AI`, or `1 張卡片
   複製`) duplicated the card's/tool's own header whenever a column held
   just one item — which is the common case for the AI 助手 tool and a
   single document card. `refreshColumn()` now hides that bar entirely
   when a card column has 0–1 cards (`.bar-off`), leaving the card's own
   header as the column's visible top edge; the bar still appears, unchanged,
   for 2+ cards (dropdown navigation + bulk copy still needed there). The
   `筆記／AI` tools-column bar is always hidden now, since `showTool()`
   already guarantees at most one tool-box per tools column, so that bar
   never had a real multi-item case to serve. The single-card copy action
   that used to live in the outer bar moved to a new `複製` icon button
   (`.ip-copy`, "⧉") in the card's own header, wired to the same
   id/title copy logic.
2. `總摘要` and `原文 BODY` previously used two unrelated visual
   treatments (a tinted/bordered box vs. bare running text with a small
   label). Both now share one "card with a colored left accent rail + dot
   label" pattern — green accent for 總摘要, gold accent for 原文 BODY —
   so they read as one system instead of two. This only restyles the
   outer framing of each section; the highlight spans, margin notes,
   division/segment ("分段") rendering, and filter chips inside are
   untouched.

Both changes were added as new CSS rules at the very end of the
stylesheet (immediately before `</style>`, after the existing "UI
REFRESH v2" (`#ui-refresh`) layer), using `body`-prefixed selectors and
`!important` so they are the definitive, final-word style regardless of
which of the file's several earlier/overlapping style passes would
otherwise have won the cascade for these elements — confirmed by
rendering the real file in a headless browser both before and after the
change (see Verified).

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Loaded the real (unmodified) file in a headless Chromium instance and
  inspected computed styles / a screenshot of an injected `.ip-overall` /
  `.ix-text` structure first, to confirm empirically which of the file's
  layered style passes was actually winning before changing anything
  (rather than assuming from static reading — the file has at least three
  overlapping "redesign" CSS passes added over time).
- After patching, re-rendered the real file with a realistic single-card
  `.ws-list` + single-tool `.ws-tools` structure (same content as the
  16:06 screenshot reference) and confirmed visually: both outer bars
  gone, both headers share the same visual language, the copy icon sits
  in the card header without overlapping the (3-line) title, and 總摘要 /
  原文 BODY render as matching accent-bar cards.
- Both HTML files' embedded JavaScript parsed successfully
  (`new Function(...)` over the extracted `<script>` body).
- Diffed the injected JS edits and the new CSS block between the formal
  and sample files: byte-identical.

Remaining:
- Human visual/interactive confirmation in both formal and sample views,
  especially: a 2+ card column still shows the (unchanged) navigation
  bar as expected, and dark mode looks acceptable for the new accent
  colors (kept as fixed green/gold hex values rather than theme tokens).

### 2026-07-18 16:18 HKT — Claude — Dropped the single-doc copy button; redesigned the card-list dropdown (formal + sample)

Summary: Follow-up from human review of the 16:06 change (screenshot of
the real multi-card column). Two changes, applied identically to both
tools:
1. Removed the `.ip-copy` icon button added in the prior entry (human
   feedback: not needed for a single document). The rest of that change —
   hiding the outer bar for 0–1-card/tool columns — is unaffected.
2. Redesigned the `☰ N 張卡片 ▾` dropdown (`.col-dd-pop` / `.col-dd-item`,
   shown for columns with 2+ cards). Diagnosis: `.ddt` forced
   `white-space:nowrap` with ellipsis truncation regardless of popup
   width, so long document titles were never fully readable — confirmed
   from the human's screenshot (titles cut off mid-word) and by comparing
   against the AI panel's own `目錄` popover (`.cb-toc-item`), which
   already wraps normally with no truncation and was not affected by this
   bug. Discussed options with the human before implementing; agreed
   approach: wrap full titles (no truncation, matching the `目錄`
   pattern), combine badge + doc id + title into one flowing entry per
   card, widen the popup (360px → 460px max-width) and bump the item font
   size (12px → 13px). Added a hairline divider between entries since
   they can now be multi-line.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both HTML files' embedded JavaScript parsed successfully after each of
  the two edits.
- Confirmed no leftover `.ip-copy` references outside of one now-corrected
  comment.
- Confirmed the "UI REFRESH v2" (`#ui-refresh`) layer only touches
  `.col-dd-pop`'s background/border/shadow, not width or white-space, so
  it doesn't fight the new wrapping/width rules.
- Rendered the real file headlessly with realistic entries (short titles,
  a long title, mixed 上奏/上諭/硃批 badges) and confirmed visually: short
  entries stay compact on one line, long entries wrap cleanly to 2+
  lines, badges stay top-aligned against wrapped text, dividers separate
  entries.
- Diffed the JS/CSS edits between formal and sample files: identical.

Remaining:
- Human visual/interactive confirmation of both changes in the real app.

### 2026-07-18 16:26 HKT — Claude — Single dropdown trigger + content-fit card-list popup (formal + sample)

Summary: Second follow-up from human review of the multi-card column bar
(screenshot showed `☰ N 張卡片 ▾` and `複製` as two separate buttons, and
the redesigned dropdown from the 16:18 entry still wrapping titles to 2
lines with a badge/font that looked inconsistent with the rest of the
UI). Applied identically to both tools:
1. `refreshColumn()` now renders a single `☰ N 張卡片 ▾` trigger button
   only (the standalone `複製` button is dropped from the bar). `.ws-list-bar`
   changed from `justify-content:space-between` to `flex-end`, and
   `.col-titles` from `flex:1` to `flex:0 0 auto`, so the one remaining
   button sits snug against the column's own `✕` at the right edge
   instead of stretching across the bar.
2. `.col-dd-pop` changed from a fixed `min-width:280px/max-width:460px`
   band to `width:max-content` capped at `min(640px, 100vw-32px)` — a
   short title's popup now shrinks to fit it instead of leaving blank
   space, and a long title gets real room before wrapping at all, rather
   than wrapping prematurely at a mid-sized fixed width. `openColDropdown()`
   switched each entry's type badge from the 2-character label
   (`TYPE_LABEL`, e.g. `硃批`) to the same 1-character label the card's own
   badge already uses (`TYPE_SHORT_LABEL`, e.g. `硃`) — this was the
   concrete cause of the "font doesn't match the rest of the UI" feedback
   (a longer badge, not actually a different font), and freed up width
   that was contributing to unwanted 2-line wraps. Also switched
   `.ddt`'s `overflow-wrap` from `anywhere` to `break-word`, so embedded
   dates/numerals don't get split at an arbitrary character either.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both HTML files' embedded JavaScript parsed successfully.
- Confirmed no later CSS pass overrides `.ws-list-bar`'s
  `justify-content` (the "UI REFRESH v2" layer only touches its
  background/border), so the new right-clustered layout isn't fought by
  a later rule.
- Rendered the real file headlessly reproducing the human's screenshot
  scenario (two 硃批 cards) and confirmed: the bar shows one button
  clustered against ✕, and the dropdown shows both titles on a single
  line each with the short badge.
- Rendered a second case with one very long title and one very short
  one: the long title wraps at the 640px cap instead of overflowing the
  viewport or forcing the short entry to match its width; the short
  entry stays compact.
- Diffed the JS/CSS edits between formal and sample files: identical.

Remaining:
- Human visual/interactive confirmation in the real app. The bulk-copy
  action that used to live in the bar's `複製` button has no replacement
  yet (dropped per the request to reduce it to one button) — flag if
  that's still needed somewhere.

### 2026-07-18 16:37 HKT — Claude — AI 助手 panel header/footer cleanup (formal + sample)

Summary: Five UI fixes to the AI 助手 tool panel, from human review of a
screenshot. Applied identically to both tools:
1. Top row (`.chat-toprow` in `.tb-head`): the 目錄 / 收合輸入 / 最近卡片
   chips now show a single glyph each with no text label and no emoji —
   目錄 = `☰` (+ `▾`), 收合輸入 = `⊟`/`⊞` (toggles, unchanged glyph),
   最近卡片 = `↥`. All are text-default (non-emoji) Unicode symbols. The
   old `📑`/`↗` emoji icons and the Chinese text labels were removed;
   tooltips (`title=`) carry the meaning.
2. Duplicate date dividers: the chat log had both a left-aligned
   per-skill-run header (`.dp-runhdr`, "M/D · N 則") and a centered
   day-separator with flanking rules (`.sess-div`, added by
   `enhanceSeparators()`). The left-aligned `.dp-runhdr` is now hidden
   (`display:none`); only the centered `.sess-div` remains, and its label
   font was enlarged (10.5px → 13px, weight 600).
3. Footer chip row (`.cb-chiprow`): removed the `套用：` prefix and the
   `🗂` icon from the scope chip (now shows just the value, e.g. `硃41 ▾`
   — see updateScopeChip); relabeled the `動作` chip to `功能` and dropped
   its `⚡` icon; replaced the `設定` chip's text with a gear symbol only
   (`⚙`, plain — matches the doc panel's existing `.ip-settingsbtn` gear,
   which already renders monochrome in the app).
4. Chat input: cleared the `向 AI 提問…（Enter 送出）` placeholder so the
   type box starts with no default text.
5. Tool-box header drag handle (`.tb-head .ip-move.tb-move`, `✥`): was a
   bordered default-button box; now rendered as the same borderless ghost
   glyph as the header's `✕` (transparent, faint color, 16px, hover →
   ink). Scoped to `.tb-head` only, so document-card header buttons
   (`.ip-btns`) are unaffected.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both HTML files' embedded JavaScript parsed successfully.
- Rendered the real page's markup headlessly: confirmed the footer reads
  `硃41 ▾ / 功能 ▾ / [gear]` with no `套用：` prefix, the textarea has no
  placeholder, only the centered enlarged day separator shows, and the
  `✥` drag handle now renders borderless like the `✕`.
- NOTE / caveat: the headless Chromium build lacks font glyphs for `☰`,
  `⊟`, `↥`, and `⚙`, so those four symbols could not be visually
  confirmed in the screenshot (they showed blank). They are all standard
  BMP symbols present in macOS system fonts — `⊟` was already the app's
  compose-toggle glyph and `⚙` already renders (monochrome) in the doc
  panel — so they are expected to render on the user's Mac. This is the
  one item most worth a human eyeball.
- Diffed all edited regions between formal and sample: identical.

Remaining:
- Human confirmation that the four header/footer symbols (`☰ ⊟/⊞ ↥ ⚙`)
  render as intended on the user's machine (see caveat above).

### 2026-07-18 16:55 HKT — Claude — SVG icon buttons + doc info-panel polish (formal + sample)

Summary: The Unicode symbols from the previous entry did NOT render on the
user's machine (confirmed: the serif UI font lacks `☰ ⊟ ↥ ⚙` glyphs and
was not falling back). Replaced ALL such icon buttons with inline SVG
(renders identically everywhere and is verifiable headlessly), and did a
batch of doc info-panel fixes. A shared `const IC={...}` object of Feather-
style inline SVG strings (list, filter, gear, jump, collapse, expand,
move, minimize, restore, close) was added near the top of the main script
and referenced from every icon-button template. Applied identically to
both tools:
1. AI 助手 header/footer icons redone as SVG (list / chevron-collapse /
   jump-arrow in the top row; gear in the footer). Also had to override
   `body .cb-chip .cb-ic{ display:none }` (the app hides chip icons unless
   the chip is <300px) for `.cb-icon-only` chips so the glyphs always show.
2. Card-list column trigger (`.col-dd-btn`): the `☰ N 張卡片 ▾` text
   button is now a single borderless list-icon button, ghost-styled like
   the column ✕.
3. Doc-card header buttons (`.ip-btns`: move/min/close) redone as SVG and
   unified — equal 24px boxes, centered, no baseline drift (the old `▁`/`▢`
   glyphs sat low and looked mismatched next to `✥`/`✕`). fold/expand now
   swap the min button's innerHTML between the minimize and restore SVGs.
4. Removed the header grip line under a FOLDED card
   (`.card.folded .ip-head-resize{ display:none }`).
5. Doc filter button: `⏷ 篩選` → a single funnel SVG (text label hidden);
   the settings `⚙` beside it → gear SVG, so the two read as an icon pair.
6. Document-type badge (硃/諭/奏 before the title): now a larger rounded
   square (radius 7px, ~22px scaled by the 內文/正文 font size var `--fs`),
   instead of a tiny pill.
7. Removed the green/brown left accent rails (and the small dot markers)
   from the 總摘要 / 原文 BODY section boxes that were added on 2026-07-18
   16:06 — the user disliked them. The boxes + colored text labels remain.
8. Division part titles (`.seg-label`, e.g. "1. 奏報緣起"): enlarged from
   the 11.5px the ui-refresh layer forced, up to ~16px bold.
Also fixed a latent bug this exposed: a legacy global `svg{ min-width:1180px }`
rule (for the old single-view chart) was forcing every inline icon to
1180px; `.svgic` now sets `min-width:0 !important` (plus width/height 1em)
to neutralize it.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both HTML files' embedded JavaScript parsed successfully.
- Rendered both the doc card column and the AI panel headlessly using the
  file's actual `IC` SVG strings against the real stylesheet, and screenshotted:
  confirmed every icon renders at the intended ~15px (after the min-width
  fix), the badge is a large rounded square, the accent rails are gone,
  the folded card has no grip line, the seg title is enlarged, and the AI
  header/footer icons all show.
- Diffed the shared `IC` block and every new CSS/JS region between formal
  and sample: identical.

Remaining:
- Human visual confirmation in the real app (esp. dark mode, and that the
  SVG icons inherit sensible colors in both themes — they use
  `stroke:currentColor`, so they follow each button's text color).

### 2026-07-20 14:38 HKT — Claude — Button unification + doc-panel polish, round 2 (formal + sample)

Summary: Six adjustments from human review, applied identically to both tools.
(A) Document-type badge (硃/諭/奏 before the title) was too large — reduced
to ~12px*--fs (smaller than the ~14px title) while still scaling with the
內文/正文 font size (--fs) and keeping the rounded-square shape.
(B) Unified every icon button to a single borderless ghost style — the doc
filter and settings buttons (and the AI icon-only chips) previously sat in
pill boxes; all boxes removed, one size (16px*--fs), faint colour, subtle
hover. Active (.on) state now shown by accent colour instead of a box.
(C) Removed the "AI 助手" title text from the AI tool panel header (kept the
other tool titles); the header now shows just its icons.
(D) The doc-card filter/settings bar was inset by the card's 16px padding,
leaving a visible gap on each side — it now full-bleeds to the card edge
(margin:0 -16px + matching padding), reading as a proper full-width toolbar.
(E) Hid the completion/status chip (✓ 完成 / 待處理) in AI output cards
(.cxh-chip).
(F) Replaced the 回覆 reply button text with a reply-arrow icon.
(G) Replaced the ✕ close (.turn-del / .turn-del-x) in AI output cards with
the unified close icon, matching every other symbol button.
F and G use CSS mask-image (data-URI SVG + background-color:currentColor)
rather than editing the ~9 separate button-markup sites, so they stay
theme-aware and required no JS/markup churn. Only (C) touched JS (one
ternary in createToolBox).

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both HTML files' embedded JavaScript parsed successfully.
- Rendered headlessly against the real stylesheet: doc card (badge now
  smaller than title, filter/settings borderless, filter bar full-width),
  an AI output card (no status chip; reply-arrow and unified close icons),
  and the AI header with the empty title (icons sit cleanly, no orphaned
  gap). All correct.
- Diffed the new CSS block and the JS edit between formal and sample: identical.

Remaining:
- Human confirmation in the real app, incl. dark mode. Note: the AI footer
  dropdown buttons that carry TEXT (套用 value `硃41 ▾`, `功能 ▾`) were left
  as bordered buttons — only icon buttons were de-boxed. Flag if those
  should go boxless too. The bulk-copy (`複製`) action removed earlier still
  has no replacement.

### 2026-07-20 14:52 HKT — Claude — Top-toolbar cleanup + live search dropdown (formal + sample)

Summary: Six changes to the dual-timeline top toolbar and search, applied
identically to both tools.
(1) Hid the floating 網絡範圍 (network-reach) launcher button
(`#reach-launch{display:none}`). The panel/feature still exists in code but
is no longer launchable from that button — relocate into 工具 if it's wanted
back.
(2) Replaced the text dropdown carets (`▾`) on the 點線類型 / 編輯圓點 / 工具
buttons with a small inline SVG chevron (`.dd-caret`), matching the SVG icon
system.
(3a) Match-count readout changed from `N 件符合（共 M 件）` to a compact
`N/M`, enlarged (16px*--fs, bold, tabular numerals).
(3b) The type-filter button now reads just `點線類型` — the running
dot/line counts (`6/7點 · 11/11線`) are hidden (`#tb-type-summary`).
(4) People/search font balance: the `人物` label is larger (14px*--fs); the
select value (選擇人物) and the search placeholder are smaller (11.5px*--fs).
The search `🔍` emoji was replaced with an inline SVG magnifier.
(5) Restyled the native `選擇人物` / `且-或` `<select>`s (appearance:none,
parchment bg, thin border, custom SVG chevron background) so they match the
rest of the UI instead of looking like OS-native dropdowns.
(6) NEW: a live search-results dropdown under the search box. As the user
types, it lists every matching document (badge + doc id + full title, same
full-text match the timeline filter uses, capped at 60 shown), with a
footer showing the total count and a `複製全部編號` button that copies ALL
matching doc IDs (not just the shown 60), one per line, to the clipboard.
Clicking a result opens that document (via `window.__cmdPickDot`).

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both HTML files' embedded JavaScript parsed successfully.
- Rendered the real page headlessly: toolbar shows chevron carets, styled
  person select, magnifier icon, `點線類型` (no counts), and `236/363`; the
  reach button computes to display:none.
- Drove the search live: typing shows the results dropdown with
  badge/id/title rows; the `複製全部編號` button copied 184 IDs (one per
  line, verified via clipboard read) and showed the "已複製 184 個編號"
  confirmation.
- Diffed the new JS + CSS regions between formal and sample: identical.

Remaining:
- Human confirmation in the real app (dark mode too). Note: search full-text
  matching is broad (matches any field incl. body text), so a common name
  like 黃仕簡 returns many docs — that's expected for full-text, flag if a
  title/id-only search mode is wanted instead.

### 2026-07-20 07:05 HKT — Claude — Fix toolbar --ui-fs scaling, widen search dropdown, restore doc-panel backdrop (formal + sample)

Summary: Three follow-up fixes to the previous toolbar+search round, applied
identically to both tools.

(1) The new toolbar/search elements (search box text, search-results list,
`人物`/`選擇人物`, `點線類型` label, the `N/M` match count) had been styled
against `--fs` (the 正文/content font-size scale) instead of `--ui-fs` (the
介面字級/interface font-size scale that 編輯圓點/工具/A−/A+ actually use).
Two pre-existing, higher-specificity legacy rules were also silently
overriding several of these to a flat, non-scaling size regardless of which
variable was used:
  - `body .dual-toolbar .pl { font-size:11px !important; }` — was pinning
    every `.pl` label (incl. `點線類型`) to a flat 11px.
  - `.dual-toolbar .pl, .dual-toolbar label, .dual-toolbar .count-readout{
    font-size:calc(15px * var(--fs,1)) !important; }` — was pinning the
    match-count readout to the content scale, not the interface scale.
  Both were switched to `var(--ui-fs,1)` (root-cause fix, not just a patch
  on top). All the round-9 toolbar/search CSS was also rewritten onto the
  `--ui-fs` axis with sizes matched to 編輯圓點/工具 (~15-16px baseline) and
  given `!important` where a same-specificity legacy rule would otherwise
  win by source order. Verified empirically: with `--ui-fs` forced to 1.3,
  編輯圓點 (19.5px), 點線類型 label (19.5px), match count (19.5px), search
  input (18.2px) and search-result rows (18.2px) now all scale together.
(2) `.search-pop` was widened from `max-width:min(520px, 80vw)` to
  `width:max-content` with `min-width:min(420px, 100vw-24px)` and
  `max-width:min(760px, 92vw)`; each `.search-item` row is now
  `white-space:nowrap` with the title (`.stt`) as a `flex:1 1 auto`
  ellipsis-truncating span, so badge+id+title render on one line by
  default instead of wrapping to two.
(3) The single-document info panel (`.ws-list.single`) previously sat flush
  and square against its sunken column background
  (`padding:0 !important; margin:0 !important; border-radius:0 !important`
  on the card), unlike the AI panel (`.ws-tools > .tool-box`), which keeps
  the standard `margin:8px 8px 0; border-radius:var(--r2)` treatment and so
  shows a visible light-brown backdrop with rounded corners. Restored the
  same margin/radius/padding to `.ws-list.single` and its card so the doc
  panel now matches the AI panel's backdrop + rounded-corner look.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both HTML files' embedded JavaScript parsed successfully (`new
  Function()` over the largest inline `<script>`).
- Diffed the edited regions between formal and sample: identical (the only
  diffs anywhere in the two files are the pre-existing formal/sample data
  paths and comments, unrelated to this round).
- Rendered headlessly: toolbar screenshot shows 點線類型/人物/編輯圓點/工具/
  count all visually consistent in size; typed a live search query and
  confirmed every result row (badge+id+title) sits on one line at the wider
  popup width; forced `--ui-fs` to 1.3 and re-measured computed font sizes
  to confirm every new element scales in lockstep with 編輯圓點/工具; built
  a synthetic single-card doc panel next to a synthetic AI tool-box panel
  and confirmed both now show the same backdrop margin + rounded top
  corners.

Remaining:
- Human confirmation in the real app, incl. dark mode and the real A−/A+
  control (this round verified `--ui-fs` scaling by setting the CSS
  variable directly in a headless page, not by clicking the actual
  toolbar's A+ button, which lives inside a popover not exercised here).

### 2026-07-20 07:25 HKT — Claude — Thin the doc-panel backdrop, tighten 總摘要/原文 box padding (formal + sample)

Summary: The previous backdrop restore (see the entry above) overcorrected —
`.ws-list.single` got its own 9px column padding *plus* the card's 8px
margin on every side (17px total), roughly double the AI panel's 8px
(`.ws-tools` has zero column padding; only the tool-box's own `margin:8px
8px 0` creates the backdrop). Fixed by zeroing `.ws-list.single`'s column
padding again and trimming the card's margin back to `8px 8px 0` (matching
`.ws-list > .card, .ws-tools > .tool-box` exactly, one-for-one) instead of
adding a bottom margin too.

Separately, the 總摘要 (`.ip-overall`) and 原文 BODY (`.ix-text`) boxes sat
much further from the card edge than an AI chat bubble does: `.ip-scroll`
had 14px of its own left/right padding, and the boxes added another 14-16px
on top of that (~28-30px total). Reduced `.ip-scroll`'s horizontal padding
to 8px (matching the AI panel's `.tb-body`) and trimmed `.ip-overall`
14px→11px and `.ix-text` 16px→13px horizontal padding, bringing the total
inset down to roughly the AI panel's ~21px.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both HTML files' embedded JavaScript parsed successfully.
- Diffed the edited regions between formal and sample: identical (same 77
  pre-existing lines of formal/sample-only differences as every prior
  round; nothing new).
- Rebuilt the synthetic single-card-doc-panel vs. tool-box-AI-panel
  comparison and confirmed both columns now show the same backdrop
  thickness, and the 總摘要/原文 boxes sit closer to the card's edges.

Remaining:
- Human confirmation in the real app, incl. dark mode.

### 2026-07-20 07:45 HKT — Claude — Fix invisible-glyph buttons, unify AI-panel/doc-panel symbol buttons, remove backdrop-on-hover, add delayed tooltips (formal + sample)

Summary: Four changes, applied identically to both tools.

(1) Found that `createToolBox()` (builds every tool-box header, incl. the
AI panel) and the event-card/day-card headers still built their
move/close buttons from raw `✥`/`×` text glyphs, missed by the earlier
site-wide switch to inline-SVG icons (`IC.move`/`IC.close`) that was done
specifically because Unicode symbols didn't render on the user's machine.
Converted all three remaining call sites to the SVG icons — this directly
addresses "unify the AI panel's top-right 2 buttons with other symbol
buttons," since they may have been rendering as blank/tofu boxes before.
(2) Unified `.tb-move`/`.tb-close` (AI panel header) onto the same
borderless "symbol button" family as `.ip-filterbtn`/`.ip-settingsbtn`/
`.cb-chip.cb-icon-only` (same 3px padding, same `var(--r1)` border-radius,
same auto sizing) instead of their own slightly different padding and no
radius.
(3) The doc panel's three top-right buttons (`.ip-btns` move/minimize/
close) showed a light-brown backdrop (`background:var(--sunken)`) on
hover, unlike every other symbol button's color-only hover. Two separate
legacy rules set this (one light-mode, one dark-mode with its own
`background:#33404c`/`var(--surface)`), so both were overridden — the
light-mode source rule directly, the dark-mode ones via an `!important`
override since they out-specificity a plain fix.
(4) Added a shared "hold to see label" tooltip system for every icon-only
symbol button (SVG icon or a 1-2 char glyph like ✕/+/−, detected
automatically — text buttons like `功能 ▾` are left alone since they
already show a label). A small script converts each such button's
existing `title` attribute to `data-tip` (suppressing the native OS
tooltip) on load and on every subsequent re-render via a MutationObserver
(most of these buttons are rebuilt by `innerHTML`, not persistent DOM
nodes). Pure-CSS delayed reveal: `opacity`/`visibility` transition with
no delay on the base rule (hides instantly) but a 1s `transition-delay`
on the `:hover` rule (so the black label only appears after ~1s of
hovering), positioned above the button, with a right-edge flip for
buttons near the edge of a popup (search results, TOC dropdown).

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both HTML files' embedded JavaScript parsed successfully.
- Diffed the edited regions between formal and sample: identical (same 77
  pre-existing formal/sample-only lines as every prior round).
- Rendered a synthetic AI tool-box header + doc card side by side:
  confirmed `title` attributes were converted to `data-tip` on load for
  every targeted button (tb-move, tb-close, ip-move, ip-min, ip-close,
  ip-filterbtn, ip-settingsbtn); confirmed hovering `.ip-move` shows only a
  color change, no backdrop; confirmed the black tooltip label appears
  only after ~1s of continuous hover and disappears promptly on mouse-out.

Remaining:
- Human confirmation in the real app, incl. dark mode.
- Investigating a separate report: "now can't show the full text of each
  doc in the doc info panel." Reviewed every CSS/JS change from the last
  two rounds (padding/backdrop/margin edits) and could not find a
  mechanism that would hide or truncate document body text — no
  `overflow:hidden`, `max-height`, or text-truncation rule was touched,
  and a synthetic single-card panel with a long multi-segment document
  scrolled to and fully displayed its last segment in testing. Real
  document data isn't available in this sandbox (the timeline fetches
  `/formal/...json` over `file://`, which the browser blocks via CORS, so
  no dots are clickable here) — asked the user for a screenshot of the
  broken state to pin down the actual cause rather than guessing further.

### 2026-07-20 08:20 HKT — Claude — Surface pipeline repeat-report flags in output cards (formal + sample)

Summary: The repeat-report dedup pass in run_mass_prompt_chain_test.py writes
same_as / earliest_report / repeat_candidates onto lin/qing/emperor cards in
the bundle (verified: the newest bundle zhu-first-10-official-loop carries 16
林 / 34 清 / 35 皇帝 flags, exactly matching the run log). But the website never
read those fields: applyLocalSkillBundle -> normalizeSkillEventItem dropped
them, and linkBundleReports recomputed repeats purely client-side via
matchCandidateInRegistry (a title/quote heuristic). A stale in-code comment
even says "the terminal script has no way to flag that an extracted event was
already reported" — no longer true. The heuristic misses what the LLM pass
caught, so flagged repeats never appeared as the output card's 「先前已回報」
(⚠) note + 併入既有事件 / 仍獨立加入 buttons.

Fix (three edits, applied identically to both files):
1. normalizeSkillEventItem now preserves card_id / same_as / earliest_report /
   repeat_candidates onto the ingested item.
2. extractRegistryEntry now carries cardId (it.card_id||it.id) so an
   earliest_report id can be resolved back to a registry entry.
3. linkBundleReports: when its own heuristic finds no match for an extract
   card, it falls back to the pipeline's same_as / earliest_report.id, resolves
   that earlier report in the registry by card id, and reuses the exact same
   __matchReg shape + downstream merge/commit path. registryEntryAllowedFor-
   Candidate still guards self / same-document / later-dated, so a flagged
   earlier report only surfaces when genuinely valid.

Scope of this fix = CROSS-document repeats (what the output card's re-report
note is designed for). Verified end-to-end by serving the real bundle + data
through server.py in headless Chromium, loading it via 載入技能輸出, and
inspecting the ingested items: every cross-document flagged 林 card and the
cross-document 清 cards that resolve now carry a correct __matchReg (which the
existing, unchanged render path turns into the ⚠ note).

NOT yet covered (need product decisions, see user):
- Same-document repeats: the majority of the 清 flags (~52 of 68 in the test)
  are two extracted actions WITHIN one 硃批 that report the same event. The
  card's re-report note is cross-document by design (invalidMatchRegForCandidate
  blocks same-doc), so these need a distinct indicator, not the existing note.
- Emperor-action cards: combined-emperor-actions.json ingests as kind
  'edictmatch' (em-item render), a different card type from the lin/qing
  extract cards; its same_as_event_id flags aren't surfaced yet.
- A few cross-doc flags don't resolve because their earliest card isn't in the
  loaded bundle set (committed in an earlier run / different bundle).

Files:
- review-tools/(1) formal/index.html
- review-tools/(2) sample/index.html
- PROJECT_LOG.md

Verified:
- Both files' embedded JS parsed; formal/sample edited regions identical.
- Real-data headless load of zhu-first-10-official-loop: flagged cross-doc
  cards receive a valid __matchReg; same-document flags correctly excluded by
  the existing cross-doc guard.

### 2026-07-20 08:45 HKT — Claude — Same-document + emperor-card repeat notes (formal + sample)

Summary: Follow-up to the cross-document repeat surfacing. The user asked to
also see the two repeat kinds the first pass deliberately left out. Both now
surface; verified end-to-end so that EVERY pipeline-flagged repeat produces a
note (no silently-dropped flags).

(1) Same-document repeats: when the pipeline flags a card as repeating an
earlier report in the SAME document, the cross-document ⚠ note (and the whole
__matchReg / merge machinery) intentionally excludes it. These now get a
distinct informational marker `.cx-samedocnote` ("↻ 本文書稍早已回報此事件：
<title>，<date>"), jump-enabled only when the earlier report resolves to a
committed event.
(2) Registry-miss cross-document repeats: many flagged earliest reports are a
committed EVENT id (evmrXX, not a bundle card id) or an older card that
predates card_id, so the registry can't resolve a *mergeable* target. Rather
than drop these, linkBundleReports now falls back to the pipeline's own
earliest_report record and emits a note-only cross-doc marker (`.cx-matchnote`,
no merge buttons, `xdocNoteHtml`), jump-enabled when the event id resolves.
(3) Emperor-action cards: combined-emperor-actions loads as kind 'edictmatch'
(em-item render), a different card type carrying same_as / earliest_report on
each point straight from the bundle (no normalize step strips them). Added
`emRepeatNoteHtml(pt)` rendered inside each em-item ("↻ 此諭令先前已於 <doc>／
<title>，<date> 下達（同一皇帝行動）").

All three notes reuse the existing cx-jumpreport hover/click handler (hover =
highlight the earlier dot on the timeline, click = open its event card), which
no-ops safely when it can't resolve a dot, so nothing new can throw.

Files:
- review-tools/(1) formal/index.html
- review-tools/(2) sample/index.html
- PROJECT_LOG.md

Verified (headless, real zhu-first-10-official-loop bundle + server.py, empty
edits so counts are clean):
- linqing flags: 26 cross-doc mergeable (⚠+merge) / 27 same-doc (↻) / 4
  cross-doc note-only (⚠) / 0 with no surface at all — every flag now shows.
- All 35 emperor repeat points carry earliest_report and render the note.
- DOM check on 硃22: 12 .cx-samedocnote + 20 .cx-matchnote rendered with real
  text; on 硃21: 40 .em-repeatnote rendered ("↻ 此諭令先前已於 硃25／…").
- Both files' embedded JS parsed; formal/sample edited regions identical.

Remaining:
- A page reload (not a fresh 載入技能輸出) drops these notes, same as the
  pre-existing __matchReg — they are recomputed only at bundle-load time. Not
  changed here; flag if persistence across reloads is wanted.

### 2026-07-22 15:23 HKT — Codex — Restored typed click-network focus (formal + sample)

Summary: Reconnected the explicit four click-type network rules to the existing
timeline renderer without removing Claude's configurable reach UI or document
and emperor-card changes. Focused network lines now dim unrelated pair links,
connected endpoint dots remain visible, and Yu-source focus preserves the green
third-line Zhu ring. Clicking a Zhu-sourced emperor action no longer recurses
into unrelated response chains.

Files:
- review-tools/(1) formal/index.html
- review-tools/(2) sample/index.html
- PROJECT_LOG.md

Verified:
- Both embedded HTML scripts parse successfully.
- Formal/sample typed-network helper and render sections are identical.
- Relationship smoke test covers a Yu, two responding Zhu documents, field
  events, and emperor actions; expected focus sets were produced.
- git diff --check passes.

Remaining:
- The in-app browser refused to reload the local file URL for visual
  verification; no browser workaround was used.

### 2026-07-22 15:45 HKT — Codex — Keep chart context visible during typed focus (formal + sample)

Summary: Kept the deterministic typed click-network focus and changed its
visual treatment so normally visible non-selected document dots, event dots,
and relationship lines remain rendered with dim transparency instead of being
omitted. Focused endpoints and the Yu-source Zhu green ring remain emphasized.

Files:
- review-tools/(1) formal/index.html
- review-tools/(2) sample/index.html
- PROJECT_LOG.md

Verified:
- Both embedded HTML scripts parse successfully.
- Formal/sample typed renderer sections are identical.
- git diff --check passes; AGENTS.md and CLAUDE.md remain identical.

Remaining:
- The in-app browser still refuses to reload the local file URL for visual
  verification; no browser workaround was used.

### 2026-07-22 16:03 HKT — Codex — Corrected emperor-action origin rendering (formal + sample)

Summary: Fixed typed emperor-action focus and provenance rendering for saved
events whose source references use aliases such as 天13 while chart records use
canonical 諭13 IDs. Alias-aware, quote-aware resolution now finds the correct
Yu/Zhu source, the selected action's own source line remains visible and hot,
and Zhu-origin actions do not expand through an unrelated memorial. Yu-to-
memorial, response, pair, and information-source lookups use the same resolver.

Files:
- review-tools/(1) formal/index.html
- review-tools/(2) sample/index.html
- PROJECT_LOG.md

Verified:
- Both embedded HTML scripts parse successfully.
- Formal/sample typed renderer sections are identical.
- All 179 saved emperor actions have resolvable origin aliases.
- git diff --check passes; AGENTS.md and CLAUDE.md remain identical.

Remaining:
- The in-app browser still refuses to reload the local file URL for visual
  verification; no browser workaround was used.

### 2026-07-22 15:37 HKT — Codex — Restored AI-loop Qing labels and stage order (formal + sample)

Summary: Preserved the `category` returned by 清方行動（三類合一）, rendered its
已執行軍事／待執行軍事／非軍事 badge in saved and live output, added a dedicated
回應先前上諭 card, and sorted bundle stages as 林方行動 → 清方行動 → 回應先前上諭
→ 皇帝行動 → 官員回應. Empty source-chain cards are hidden after their chains are
attached to action cards.

Files:
- review-tools/(1) formal/index.html
- review-tools/(2) sample/index.html
- PROJECT_LOG.md

Verified:
- Both embedded HTML scripts parse successfully.
- Both panels pass the expected stage-order and Qing-category mapping smoke tests.
- The saved prior-Yu renderer includes both quotations and linked document IDs.
- git diff --check passes.

Remaining:
- The in-app browser refused to reload the local file URL for visual verification; no browser workaround was used.

### 2026-07-22 16:03 HKT — Codex — Corrected repeat-report chronology

Summary: Fixed repeat labels to use the reporting document's send date rather
than an extracted event date. Same-document matches are now excluded from the
terminal dedup candidate pool, stale repeat annotations are cleared before a
rerun, and the formal/sample live registry uses each source document's send
date for eligibility, ordering, and displayed labels. Existing bundles whose
repeat stage was already marked done are automatically rechecked once via a
repeat-report version marker.

Files:
- `tool/scripts py/run_mass_prompt_chain_test.py`
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Python compilation passed.
- Embedded JavaScript in formal and sample parsed successfully.
- Synthetic case confirmed 硃25 (1786/12/10) receives no warning while 硃26
  (1786/12/12) points to 硃25 as the earliest report.
- Synthetic same-document verified-dot case produced no repeat warning.
- `git diff --check` passed.

Remaining:
- Resume the existing bundle with `--skip-done`; its old repeat stage will be
  rerun automatically, then reload the bundle in the website.

### 2026-07-22 15:41 HKT — Codex — Limited Qing category badges to Qing event cards

Summary: Added an actor guard to the AI event-card category badge so 已執行軍事、
待執行軍事、非軍事 appear only on cards whose actor is 清方. 林方 cards no longer
display a Qing category even if stale category metadata is present in a saved item.

Files:
- review-tools/(1) formal/index.html
- review-tools/(2) sample/index.html
- PROJECT_LOG.md

Verified:
- Both embedded HTML scripts parse successfully.
- Actor-guard smoke check passes in formal and sample.
- git diff --check passes.

Remaining:
- The in-app browser refused to reload the local file URL for visual verification; no browser workaround was used.

### 2026-07-22 15:38 HKT — Codex — Excluded AI-loop diagnostic files from panel loading

Summary: Prevented underscore-prefixed bundle diagnostics such as `_run-status.json`
and `_source-chain-raw.json` from becoming generic AI messages. Only review-stage
JSON files now enter the ordered panel output.

Files:
- review-tools/(1) formal/index.html
- review-tools/(2) sample/index.html
- PROJECT_LOG.md

Verified:
- Both embedded HTML scripts parse successfully.
- git diff --check passes.

Remaining:
- The in-app browser refused to reload the local file URL for visual verification; no browser workaround was used.

### 2026-07-22 15:34 HKT — Codex — Made typed click networks deterministic (formal + sample)

Summary: Replaced the typed-network highlight overlay with a visibility
projection. When a dot is selected, only the allowed document sides, event
dots, pair lines, event-source lines, response lines, and Yu-to-memorial lines
for that click type are rendered. The old configurable reach walk remains
available when no typed network is selected, and Claude's surrounding UI/data
adjustments remain intact.

Files:
- review-tools/(1) formal/index.html
- review-tools/(2) sample/index.html
- PROJECT_LOG.md

Verified:
- Both embedded HTML scripts parse successfully.
- Formal/sample typed helper and renderer sections are identical.
- Four-case relationship smoke test passes for event, official document, Yu,
  and emperor-action clicks.
- git diff --check passes; AGENTS.md and CLAUDE.md remain identical.

Remaining:
- The in-app browser refused to reload the local file URL for visual
  verification; no browser workaround was used.

### 2026-07-22 16:00 HKT — Codex — Restored complete existing emperor-action cards

Summary: Normalized nested `combined-emperor-actions.json` point lists when rendering
皇帝行動（既有配對） cards. Existing saved cards now expand their wrapper item into
the complete per-action list, while editing, adding, retrying, and official-response
linking continue to target the normalized points. New bundle output already uses the
same flat point shape.

Files:
- review-tools/(1) formal/index.html
- review-tools/(2) sample/index.html
- PROJECT_LOG.md

Verified:
- Both embedded HTML files parse successfully.
- The real Zhu22 nested bundle payload normalizes to all 7 emperor-action points in both tools.
- git diff --check passes.

Remaining:
- The in-app browser refused to reload the local file URL for visual verification; no browser workaround was used.

### 2026-07-22 16:39 HKT — Codex — Restricted repeats to cross-document reports and scoped emperor actions to the selected memorial

Summary: Changed repeat-report processing and both review UIs so same-document
repeat candidates and remainder labels are suppressed; only cross-document
repeats are sent to semantic review and shown. Tightened 皇帝行動 extraction so
an existing `yu_source` link only supplies an eligible 上諭 source, not every
imperial command in that 上諭. Each action now requires a verbatim
`memorial_anchor` in the selected memorial, and the runner drops unanchored
上諭-only actions. Versioned derived stages replace stale emperor rows and
stale official-response rows when an existing bundle is rerun with
`--skip-done`.

Files:
- tool/scripts py/run_mass_prompt_chain_test.py
- tool/proxy/gemini-proxy/main.py
- tool/skills md/emperor-actions-confirmed-zhu-yu.md
- tool/skills md/combine-confirmed-emperor-actions.md
- tool/skills md/repeat-report-dedup.md
- review-tools/(1) formal/index.html
- review-tools/(2) sample/index.html
- PROJECT_LOG.md

Verified:
- Python compilation passed for the runner and proxy.
- All embedded formal/sample HTML scripts parsed successfully.
- Cross-document repeat smoke test passed: same-document candidates were
  excluded, and the earlier sent document was selected as the canonical report.
- 硃25 relevance smoke test retained the 黃仕簡-supported action and rejected
  unanchored 任承恩／常青 actions.
- `git diff --check` passed.

Remaining:
- The changed proxy code must be deployed before a remote Gemini proxy run can
  use its new output schema. Rerun the affected bundle with `--skip-done` so
  硃25／硃26 receive the new emperor-action extraction and downstream cards.

### 2026-07-22 16:51 HKT — Codex — Replaced exact memorial-anchor filtering with semantic direct-response filtering

Summary: Revised the previous 皇帝行動 relevance rule after review. An exact
verbatim memorial anchor was too restrictive because a valid action from the
existing `yu_source` network may respond semantically without repeating the
same wording. The prompt and proxy now classify each action as `direct`,
`contextual`, or `unrelated`; only `direct` actions are emitted. `contextual`
means the action is genuinely part of the same incident or 上諭 network but
responds to another memorial, official, or problem, such as an action about
任承恩／常青 not raised by 硃25. The runner keeps optional exact quote support
when available but no longer requires it.

Files:
- tool/scripts py/run_mass_prompt_chain_test.py
- tool/proxy/gemini-proxy/main.py
- tool/skills md/emperor-actions-confirmed-zhu-yu.md
- tool/skills md/combine-confirmed-emperor-actions.md
- PROJECT_LOG.md

Verified:
- Python compilation passed for the runner and proxy.
- All embedded formal/sample HTML scripts parsed successfully.
- Semantic-gate smoke test retained a direct Yu-only action without an exact
  quote, retained the current 硃批 action, and rejected a contextual
  任承恩／上諭 action and a routine 尾批.
- `git diff --check` passed.

Remaining:
- Deploy the updated proxy before rerunning the remote bundle. The stage
  version was bumped so `--skip-done` regenerates emperor actions and their
  dependent merge/repeat/official-response stages.

### 2026-07-22 17:01 HKT — Codex — Fixed emperor-action scope, subtitles, repeats, and add controls

Summary: Reworked the emperor-action loop/UI path so a linked 上諭 is not treated
as one undifferentiated action. The runner now requires a direct, verbatim anchor
in the selected memorial, derives a point-specific subtitle when a model returns
the whole 上諭 title, and versions the affected stage for `--skip-done` reruns.
The formal and sample bundle loaders now honor `merge_group`/`merge_title`, show
one primary card per merged action, repair legacy nested/flat cards, and keep
the repeat notice directly under the point subtitle with the wording
「此皇帝行動先前已出現於較早文書：…」. Emperor-action cards now have both a
whole-card batch-add button and an individual point-level add button, matching
the 林／清 event workflow. The canonical prompt also explicitly requires
point-specific titles.

Files:
- tool/scripts py/run_mass_prompt_chain_test.py
- tool/skills md/emperor-actions-confirmed-zhu-yu.md
- tool/skills md/combine-confirmed-emperor-actions.md
- tool/skills md/official-document-review-loop.md
- review-tools/(1) formal/index.html
- review-tools/(2) sample/index.html
- PROJECT_LOG.md

Verified:
- Python compilation passed for the runner.
- All embedded formal/sample HTML scripts parsed successfully.
- A saved-bundle smoke check found 59 emperor points, 23 merge groups, 13
  multi-point groups, and 4 legacy whole-wrapper titles that now receive
  point-specific fallbacks.
- A fake-proxy relevance smoke test retained only the directly anchored action,
  rejected an unanchored direct-labelled action and a contextual action, and
  produced the specific point subtitle.
- The latest ten-document runner dry run completed without proxy calls.
- `git diff --check` passed; formal editor remains unset and no formal/sample
  saved-state data was edited.

Remaining:
- The existing bundle JSON is preserved as evidence and was not regenerated in
  this turn. Deploy the current proxy/prompt changes, then rerun the bundle with
  `--skip-done` so the new relevance filter and point titles replace stale
  emperor-action and downstream rows.

### 2026-07-22 17:46 HKT — Codex — Diagnosed empty non-event bundle stages and enforced SVO subtitles

Summary: Reviewed `zhu-first-10-official-loop2`. The bundle loader correctly
recognizes the stage filenames, but `combined-emperor-actions.json` and
`official-response.json` contain zero rows; the missing AI cards are therefore
an upstream empty-output/resume problem, not a card-rendering filename problem.
The runner now accepts a semantically `direct` emperor action from an existing
`yu_source` 上諭 even when the wording has no exact verbatim memorial anchor,
while continuing to reject `contextual` and `unrelated` actions. If emperor
actions are regenerated, merge, repeat-report, and official-response stages are
automatically invalidated and rerun. Event and source-chain subtitles are
normalized to complete subject–verb–object/action labels, and both event prompts
now require that form.

Files:
- tool/scripts py/run_mass_prompt_chain_test.py
- tool/proxy/gemini-proxy/main.py
- tool/skills md/extract-lin-actions.md
- tool/skills md/extract-qing-actions-all.md
- review-tools/(1) formal/index.html
- review-tools/(2) sample/index.html
- PROJECT_LOG.md

Verified:
- Python compilation passed for the runner and proxy.
- All embedded formal/sample HTML scripts parsed successfully.
- SVO smoke cases produce `林爽文攻陷彰化縣城`, `林爽文殺害俞峻`, and
  `黃仕簡委令邱維揚帶兵渡臺`.
- `git diff --check` passed.

Remaining:
- The reviewed bundle remains unchanged as source evidence. Rerun it with
  `--skip-done` after deploying the updated remote proxy so the empty emperor
  and official-response files are regenerated.

### 2026-07-22 17:52 HKT — Codex — Versioned SVO refresh and preserved 硃批 position evidence

Summary: Added an `svo-v1` event-stage version so `--skip-done` refreshes old
Lin/Qing event and source-chain JSON instead of leaving short legacy subtitles
in the raw bundle. Re-running an event stage now replaces that document's old
rows and source chains before rebuilding downstream stages. The combined-action
path also retains 硃批 `夾批`／`尾批` and the quoted memorial context for the
existing card UI.

Files:
- tool/scripts py/run_mass_prompt_chain_test.py
- review-tools/(1) formal/index.html
- review-tools/(2) sample/index.html
- PROJECT_LOG.md

Verified:
- Python compilation and embedded formal/sample HTML parsing passed.
- Runner version/SVO smoke test passed.
- `git diff --check` passed.

Remaining:
- Run the resume command after the remote proxy is deployed; this will refresh
  the affected event/source-chain, emperor-action, merge/repeat, and official-
  response outputs in the selected bundle.

### 2026-07-22 18:13 HKT — Codex — Explicit 硃批 position and evidence order in emperor-action cards

Summary: Fixed emperor-action cards whose source is a 硃批 so they identify the
source as `夾批` or `尾批`. For an interlinear `夾批`, the card now shows the
label and the exact memorial sentence being annotated before showing the
`硃批` label and imperial quotation. The runner infers this documentary
metadata from the original source text, so old bundles whose model output did
not include the fields can still render correctly in the website.

Files:
- tool/scripts py/run_mass_prompt_chain_test.py
- review-tools/(1) formal/index.html
- review-tools/(2) sample/index.html
- PROJECT_LOG.md

Verified:
- `硃26` quote `更好` infers `夾批` and `仍飭不動聲色，不得稍有張皇`.
- `硃25` quote `仍以調養為要，勿過勞` infers `夾批` and the preceding
  `奴才於初十日帶領官兵登舟候風放洋飛渡之際` clause.
- A trailing `已有旨了。` quote infers `尾批`.
- Python compilation, both formal/sample embedded-script parsing, UI
  render-order smoke tests, agent-doc synchronization, and `git diff --check`
  passed.

Remaining:
- Reload the reviewed bundle in the website to see the corrected card order;
  rerun the loop only if regenerated JSON evidence is also needed.

### 2026-07-22 18:19 HKT — Codex — Simplified emperor-action evidence labels

Summary: Replaced the crowded emperor-action card labels with the requested
short labels. The card now uses only `奏摺`, `夾批`／`尾批`, and `上諭`; the
previous `回應奏摺`, `硃批`, and `上諭回應` labels are no longer rendered in
this combined-action evidence block. The quotation order and clickable source
links remain unchanged.

Files:
- review-tools/(1) formal/index.html
- review-tools/(2) sample/index.html
- PROJECT_LOG.md

Verified:
- Formal and sample UI smoke tests show `夾批`, `奏摺`, the memorial context,
  the imperial quotation, and no obsolete labels.
- All embedded HTML scripts parsed, Python compilation passed, agent docs
  remain identical, and `git diff --check` passed.

Remaining:
- Reload the current bundle in the website to view the simplified labels.

### 2026-07-22 18:25 HKT — Codex — Suppress routine 已有旨了 tail comments

Summary: Prevented routine tail formulas such as `已有旨了。欽此。` from
being represented as emperor actions. The runner now removes routine 硃批
sources before building an action; a point with no substantive paired 上諭 is
dropped, while an action with a real 上諭 source keeps that source without the
routine Zhu quote. Both website views apply the same cleanup retroactively to
already saved bundles. The combined-action stage version is now `v8`, and the
proxy prompt explicitly tells the model not to list routine formulas as
sources.

Files:
- tool/scripts py/run_mass_prompt_chain_test.py
- tool/proxy/gemini-proxy/main.py
- tool/skills md/combine-confirmed-emperor-actions.md
- review-tools/(1) formal/index.html
- review-tools/(2) sample/index.html
- PROJECT_LOG.md

Verified:
- `已有旨了。欽此。` is removed as a runner source and as a UI-only point.
- A substantive 上諭 paired with that routine Zhu source remains visible with
  the 上諭 source only.
- Python compilation, formal/sample embedded-script parsing, runner/UI smoke
  tests, agent-doc synchronization, and `git diff --check` passed.

Remaining:
- Reload the bundle; rerun with `--skip-done` if regenerated JSON should also
  remove the routine source from the saved output.

### 2026-07-22 18:36 HKT — Codex — Show repeat-report flags in loaded AI cards

Summary: Fixed the review-bundle card renderer so cross-document repeat notices
are derived directly from each saved card's `same_as` and `earliest_report`
fields. The notice now survives an incomplete browser-side extraction registry,
uses the earliest reporting document date supplied by the loop, and continues
to suppress same-document repeats. The formal and sample renderers remain in
sync.

Files:
- review-tools/(1) formal/index.html
- review-tools/(2) sample/index.html
- PROJECT_LOG.md

Verified:
- The latest test bundle's 4 林 and 3 清 pipeline flags each produce a visible
  cross-document warning; 皇帝 remains at 0.
- A same-document annotation produces no warning.
- Legacy `__xdocRepeat` records still render, both embedded HTML scripts parse,
  Python compilation passes, and `git diff --check` passes.

Remaining:
- Refresh the website and load the bundle again so the updated renderer is used.

### 2026-07-22 18:39 HKT — Codex — Stack emperor-action source evidence into rows

Summary: Reworked the combined 皇帝行動 evidence block so each available
source is a complete horizontal row: `奏摺` context, `夾批`／`尾批` quotation,
and `上諭` quotation. This removes the previous CSS-grid placement that put
the labels for two different sources on the same line and made the quotations
appear under the wrong headings.

Files:
- review-tools/(1) formal/index.html
- review-tools/(2) sample/index.html
- PROJECT_LOG.md

Verified:
- A 夾批 with memorial context and 上諭 renders in the order `奏摺` → `夾批`
  → `上諭`, one row per source.
- Formal/sample source-render blocks are identical, both embedded HTML scripts
  parse, and `git diff --check` passes.

Remaining:
- Refresh the website and reload the bundle to see the three-row layout.

### 2026-07-22 18:45 HKT — Codex — Expand short 夾批 memorial context quotations

Summary: Fixed short `奏摺` evidence such as `首報加以重賞` on a 夾批 card.
The runner now recovers the complete sentence immediately before the inline
硃批 marker and replaces a shorter model-supplied context when necessary. The
proxy and saved prompt now explicitly require a complete sentence or clause
with enough context to identify the subject, action, and object. The website
also expands already-saved short context quotations at render time, so old
bundles do not require regeneration to display the clearer evidence.

Files:
- tool/scripts py/run_mass_prompt_chain_test.py
- tool/proxy/gemini-proxy/main.py
- tool/skills md/emperor-actions-confirmed-zhu-yu.md
- review-tools/(1) formal/index.html
- review-tools/(2) sample/index.html
- PROJECT_LOG.md

Verified:
- 硃26 `是` now displays `臣密飭該道、府明白曉諭各地保族、鄰人等，或有竄回原籍，立即捕拿，首報加以重賞`.
- Existing short saved context is expanded by the formal and sample UIs.
- The combined-action stage version is `v9`, both UI script sets parse, Python
  compilation passes, and `git diff --check` passes.

Remaining:
- Refresh the website and reload the bundle; rerun the loop with `--skip-done`
  if the longer quotation also needs to be written into regenerated JSON.

### 2026-07-22 19:06 HKT — Codex — Correct emperor-action source and response metadata

Summary: Fixed the 皇帝行動 card renderer to use each point's actual verified
source list instead of the item-level 上諭 fallback. Zhu-only actions now show
`📜 硃批` and open the 硃批 source; points with both sources show the memorial
and 上諭 quotations as separate evidence groups with a divider before 上諭.
The `↩ 回應` line now resolves the earliest confirmed reply document from the
existing pair network, so the 諭13 network displays 硃94 rather than the selected
memorial or a fabricated 上諭 citation.

Files:
- review-tools/(1) formal/index.html
- review-tools/(2) sample/index.html
- PROJECT_LOG.md

Verified:
- Formal and sample embedded HTML scripts parse.
- A Zhu-only 硃26 point renders `📜 硃批`, no `📜 上諭`, and resolves `硃94`.
- `git diff --check` passes.

Remaining:
- Refresh the website and reload the affected review bundle to see the corrected cards.

### 2026-07-22 19:26 HKT — Codex — Deduplicate emperor-action metadata rows

Summary: Cleaned the 皇帝行動 card metadata for combined Zhu/Yu actions. The
quotation area still preserves the separate 奏摺／夾批／上諭 evidence, while the
metadata area now keeps one canonical source row—the linked 上諭—followed by its
date. Duplicate 上諭 rows, the extra 硃批 metadata row, and the distracting
↩ 回應 row are no longer shown on this card.

Files:
- review-tools/(1) formal/index.html
- review-tools/(2) sample/index.html
- PROJECT_LOG.md

Verified:
- The 硃25 item `指示常青等嚴飭沿海巡防以防餘匪內渡` renders exactly one
  `📜 上諭` row for 諭13 and the 1786-12-27 date, with no duplicate source or
  response metadata.
- A Zhu-only point still renders its actual `📜 硃批` source.
- Formal and sample embedded HTML scripts parse, and `git diff --check` passes.

Remaining:
- Refresh the website and reload the bundle to see the cleaned card.

### 2026-07-22 19:27 HKT — Codex — Correct AI-loop elapsed dates and official-response receipt dates

Summary: Updated the formal and sample AI-loop card renderers so existing
皇帝行動 cards put the memorial-to-上諭 elapsed interval on the 上諭 date
line, while 官員回應 cards show the response send-to-receipt interval on the
canonical source dates. The 硃94 example now resolves to `1787/01/10（14 日）`
and `1787/01/22（12 日）`; the 諭13／硃21 pairing resolves to a 15-day
interval. Adding a response event now stores the source record's actual
皇帝收到日期. Also fixed two out-of-scope helpers that prevented the latest
bundle from completing its emperor-action and response-linking load path.

Files:
- review-tools/(1) formal/index.html
- review-tools/(2) sample/index.html
- PROJECT_LOG.md

Verified:
- Both embedded HTML script sets parse (5 formal blocks; 6 sample blocks).
- `git diff --check` passes.
- Date arithmetic confirms 15, 14, and 12 days for the requested links.
- Browser-level check of `zhu-first-10-official-loop` rendered the official
  response card with the corrected 硃94 send and receipt dates and retained the
  `加入為官員回應事件` action.

Remaining:
- Reload the affected bundle in the user's browser if the current tab has not
  yet been refreshed after this final source-date change.

## 2026-07-23 08:21 HKT — Codex

Current state:
- Ran the 28 `硃批` documents sent in 1786/12 in
  `zhu-december-official-loop`; all per-document extraction stages completed
  and the bundle was written.
- The recovery pass completed cross-document repeat detection with
  `林 36`, `清 39`, and `皇帝 14` flagged rows.
- The recovery pass was stopped at the user's request during
  `official-response`; 76 rows are present and 21 still have `responseError`,
  mostly remote disconnects in `硃41`, `硃42`, and `硃56`.
- No 1787/01 documents have been run.

Files changed:
- `tool/scripts py/run_mass_prompt_chain_test.py`
- `review-tools/shared data/review-bundles/zhu-december-official-loop/`
- `PROJECT_LOG.md`

Verification:
- `python3 -m py_compile "tool/scripts py/run_mass_prompt_chain_test.py"`
  passed.
- December bundle manifest and output files exist.
- The runner was patched so `--skip-done` retries rows with `responseError`
  instead of treating them as complete.

Remaining:
- Resume December `official-response` with the recovery command in the handoff
  message, then start the separate 1787/01 bundle month by month.

### 2026-07-23 11:05 HKT — Codex — Added local checkpoint rule

Summary: Documented the requirement to create local Git checkpoints after
coherent edits while keeping pushes separate and optional.

Files:
- `AGENTS.md`
- `CLAUDE.md`
- `PROJECT_LOG.md`

Verified:
- Both instruction files require staging only the current edit's files and
  creating a local commit after each coherent edit.
- The rule distinguishes local commits from `git push` and preserves unrelated
  pre-existing worktree changes.

Remaining:
- Commit the two instruction-file changes without staging unrelated changes.

### 2026-07-23 11:44 HKT — Codex — Recovered paired formal/sample UI and network source paths

Summary: Recovered the logged newer review-tool adjustments into both HTML
surfaces without replacing the current explicit typed click-network renderer.
Static `yu-source.json` pairs now enter the relationship graph, the normalized
人物/search controls and reviewed AI-output projection are restored, and the
document panel no longer renders the retired 標註／表格／AI原版 toggles. BODY
editing remains inline.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- All embedded HTML script blocks parse in both files.
- `git diff --check` passes.
- Both static Yu-source files contain 213 usable pairs, and the recovered
  formal/sample sections are equivalent after route-name normalization.
- The current typed click-network function remains present once per file.

Remaining:
- Human browser refresh and visual confirmation of the formal and sample tools.

### 2026-07-23 11:49 HKT — Codex — Added competition and research-context documentation

Summary: Read the new competition brief and the relevant second-hand/FYP
materials, then documented how they inform the completed review system and the
planned student-facing introduction/teaching website. The documentation now
separates secondary context from canonical primary-source evidence and records
that the competition brief is provisional.

Files:
- `2nd Material & FYP/README.md`
- `Competition Info/README.md`
- `README.md`
- `wiki/project-overview.md`
- `wiki/background/research-questions.md`
- `wiki/folder-structure.md`
- `wiki/index.md`
- `AGENTS.md`
- `CLAUDE.md`
- `PROJECT_LOG.md`

Verified:
- Reviewed the competition brief's theme, eligibility, submission formats,
  demonstration requirements, judging directions, AI-use disclosure, source
  acknowledgement, and draft timetable.
- Reviewed FYP notes on information delay, official document transmission,
  frontline autonomy, central decision-making, war/logistics, and spatial/GIS
  context, together with the secondary-research folder map and representative
  notes.
- Rendered and visually inspected all nine pages of the competition brief;
  preserved the source document unchanged.
- `AGENTS.md` and `CLAUDE.md` remain byte-for-byte identical; documentation has
  no whitespace errors.

Remaining:
- Confirm the final official competition rules before copying any dates,
  judging weights, links, or contact details into the teaching website.
- Design and implement the dynamic student-facing website as the next
  deliverable.

### 2026-07-23 11:56 HKT — Codex — Unified document-panel typography and backdrops

Summary: Adjusted the formal and sample document-information panels to use one
content font size, one uniform backdrop for every divided original-text part,
and a separate card backdrop for 摘要. Undivided original text is explicitly
rendered as one single-part card, avoiding nested or alternating backgrounds.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both HTML files parse all embedded script blocks.
- `git diff --check` passes.
- Render markup and final panel CSS are synchronized between formal and sample.

Remaining:
- Human browser refresh and visual confirmation of the revised card proportions.

### 2026-07-23 13:04 HKT — Codex — Restored header dropdown handlers

Summary: Restored the missing click wiring for the 編輯圓點 and 工具 menus in
both synchronized review tools. The existing timeline slider bindings were
left untouched, and selecting an edit-menu action still closes its menu.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- All embedded HTML script blocks parse in both files.
- The two new `primary-header-ui` blocks are byte-for-byte identical.
- `git diff --check` passes.

Remaining:
- The in-app browser refused to reload these local `file://` pages under its
  local-file policy; human refresh and click confirmation are still needed.

### 2026-07-23 13:08 HKT — Codex — Aligned 原文 with 摘要 text

Summary: Matched the divided 原文 heading's left inset to the 摘要 text
inset. Single-part original cards retain their existing card padding so the
heading is not indented twice.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- All embedded HTML script blocks parse in both files.
- The alignment CSS block is identical in formal and sample.
- `git diff --check` passes.

Remaining:
- Human browser refresh and visual confirmation of the horizontal alignment.

### 2026-07-23 13:52 HKT — Codex — Started the intro website outline

Summary: Recorded the approved framing of 奏折 and 上諭 as “two central forms
of Qing imperial communication,” the proposed homepage opening, and the full
brainstormed structure for the student-facing introduction and teaching site.

Files:
- `intro Website/outline.md`
- `PROJECT_LOG.md`

Verified:
- The outline records the system-first framing, with 林爽文事件 presented as
  a case study.
- The outline includes the AI-assisted, human-reviewed workflow and the
  proposed teaching sections for sources, OCR, relationship reconstruction,
  skills, models, loops, examples, and further use.
- `git diff --check` passes.

Remaining:
- Continue brainstorming the final information architecture, writing tone,
  interaction design, and page-level UI before implementation.

### 2026-07-23 14:12 HKT — Codex — Added the AI content-writing prompt

Summary: Created a Traditional Chinese writing prompt for the intro website.
It records the writing characteristics observed in `FYP_Essay.docx`, maps the
website sections to writing tasks, routes future research questions to the
appropriate `2nd Material & FYP/` subfolders, and requires author/title/year/
page-level citations with explicit handling of unresolved bibliography
differences.

Files:
- `intro Website/ai-content-writing-prompt.md`
- `PROJECT_LOG.md`

Verified:
- The prompt includes the approved system-first framing and all planned
  website sections.
- The prompt distinguishes primary evidence, published scholarship, working
  notes, and AI interpretation.
- The prompt includes citation templates, source-routing instructions, and a
  no-fabrication rule for missing pages or uncertain claims.
- `FYP_Essay.docx` was text-extracted and rendered to 25 page images for style
  review; all rendered pages were visually inspected.
- `git diff --check` passes.

Remaining:
- Use the prompt to draft the first website section, then adjust tone and
  paragraph length through human review.

### 2026-07-23 14:19 HKT — Codex — Drafted the 奏折 and 上諭 introduction

Summary: Wrote the first page-ready Traditional Chinese website section,
defining 奏折, 上諭, and 硃批 as connected parts of Qing imperial
communication. The draft follows the FYP's claim-evidence-interpretation
style and introduces the document journey that the website will visualize.

Files:
- `intro Website/outline.md`
- `PROJECT_LOG.md`

Verified:
- Read the relevant local research notes and the 王劍 article PDF before
  drafting.
- Added author/title/year/page citations, a transparent `頁碼待核` notice for
  the unpaginated宋希斌摘錄, and a source-verification checklist.
- `git diff --check` passes.

Remaining:
- Human review of the historical wording, citation page for 宋希斌, and the
  final distinction between 上諭 and 廷寄 before publication.

### 2026-07-23 14:24 HKT — Codex — Drafted the research-difficulty section

Summary: Wrote the Traditional Chinese section explaining why 奏折 and 上諭
are difficult to study, including corpus scale, fragmented communication
chains, multiple date fields, cross-sea delay, unequal information positions,
and the limits of plain-text reading.

Files:
- `intro Website/outline.md`
- `PROJECT_LOG.md`

Verified:
- Used the local 王劍 article PDF, 李智君 research text, FYP essay, and the
  project timing note before drafting.
- Included the 台951 primary-source record and marked the 李智君 page range
  and project-statistics provenance for further verification.
- `git diff --check` passes.

Remaining:
- Human review of the 13-day 台951 example, the 24.86/45-day project
  statistics, and all pending page-level citations before publication.

### 2026-07-23 14:31 HKT — Codex — Drafted the visualization section

Summary: Wrote the Traditional Chinese section explaining why visualizing
time, actors, places, actions, and document relationships is necessary for
studying 奏折 and 上諭. The section connects the 林爽文 research example and
the historical use of war maps to the website's evidence-aware chart design.

Files:
- `intro Website/outline.md`
- `PROJECT_LOG.md`

Verified:
- Used the local FYP research draft and 林加豐's article PDF before drafting.
- Applied full in-text bibliographic citations and marked the FYP draft's
  missing author/year as unresolved rather than inventing them.
- `git diff --check` passes.

Remaining:
- Human review of the FYP page reference and final alignment with the actual
  four-lane chart labels before publication.

### 2026-07-23 14:37 HKT — Codex — Drafted the website-purpose and system-flow section

Summary: Wrote the Traditional Chinese section explaining the website's
purpose and five-stage workflow: preserving original sources, AI extraction,
document-relationship reconstruction, human verification, and chart display.
The draft keeps the later sections on skills, models, and the AI loop available
for more detailed teaching.

Files:
- `intro Website/outline.md`
- `PROJECT_LOG.md`

Verified:
- Re-read `PROJECT_LOG.md` and the outline before editing.
- Used the local FYP essay, information-transmission notes, 王劍 article, and
  the source-compilation references before drafting.
- Used full in-text bibliographic citations and marked unresolved page or
  metadata issues instead of inventing them.
- `git diff --check` passes.

Remaining:
- Human review of the FYP draft's missing author/year, the 李智君 page number,
  and the mapping to the actual four-lane chart and chat-panel controls.

### 2026-07-23 14:45 HKT — Codex — Drafted the 林爽文 case-study section

Summary: Wrote the Traditional Chinese case-study section explaining why
林爽文事件 is a useful demonstration of the system: war communication,
cross-sea information delay, an available primary-source corpus, and the
relationship between battlefield documents and later official memory. The
section explicitly states that the case demonstrates a transferable method,
not the system's only research subject.

Files:
- `intro Website/outline.md`
- `PROJECT_LOG.md`

Verified:
- Used local copies of 李天鳴、李智君、李泰翰 and the project timing notes.
- Added full in-text citations and marked unresolved article pages and primary-
  source metadata for later checking.
- `git diff --check` passes.

Remaining:
- Human review of the 台852／台951 source details and the page numbers for
  李智君 and 李泰翰 before publication.

### 2026-07-23 14:52 HKT — Codex — Drafted the AI-human review design section

Summary: Wrote the Traditional Chinese section defining the core design
principle「AI 提出，人作判斷」. It explains skills, structured AI output, the
AI chat panel, source verification, review states, and the rule that only
human-confirmed results enter the four-lane chart.

Files:
- `intro Website/outline.md`
- `PROJECT_LOG.md`

Verified:
- Used the local 韓秀英 research text and the project's documented AI workflow.
- Applied full in-text citation and distinguished historical-method evidence
  from the website's own system design.
- `git diff --check` passes.

Remaining:
- Human review of the 韓秀英 page range and final alignment with the actual
  skill output schema, chat-panel controls, and chart status labels.

### 2026-07-23 15:04 HKT — Codex — Drafted the student usage section

Summary: Wrote the Traditional Chinese step-by-step section explaining how
students use the website: begin with a research question, select a small source
set, read original texts, inspect AI output, verify evidence, mark uncertainty,
confirm relationships, and add only reviewed results to the chart.

Files:
- `intro Website/outline.md`
- `PROJECT_LOG.md`

Verified:
- Used 唐振耀's local methods/source-analysis text and the 台951 source note.
- Applied full in-text bibliographic citations and preserved the distinction
  between source evidence and website teaching design.
- `git diff --check` passes.

Remaining:
- Human review of the 唐振耀 page range and the final wording of the website's
  step labels and confirmation states.

### 2026-07-23 15:06 HKT — Codex — Drafted the system-recreation section

Summary: Wrote the Traditional Chinese tutorial for recreating the system:
choosing a research question and source set, OCR and page-level verification,
source-preserving structuring, rule-based and LLM-assisted relationship
reconstruction, candidate review, and small-batch testing before scale-up.

Files:
- `intro Website/outline.md`
- `PROJECT_LOG.md`

Verified:
- Used 唐振耀's source-method discussion, the local OCR work specification,
  and the official-document review/pairing workflow files.
- Included full in-text citations and explicitly separated project rules from
  published historical claims.
- `git diff --check` passes.

Remaining:
- Human review of the exact OCR status labels, JSON field names, and relationship
  pairing rules against the final implementation.

### 2026-07-23 15:09 HKT — Codex — Drafted the AI-loop section

Summary: Wrote the Traditional Chinese section explaining the three AI-loop
components: task-specific skills, model selection by controlled testing, and a
repeatable/resumable per-document loop. It includes the project workflow,
evidence rules, bundle metadata, model-comparison dimensions, and cautions
against permanent model rankings or automatic relationship creation.

Files:
- `intro Website/outline.md`
- `PROJECT_LOG.md`

Verified:
- Used the local official-document loop, summary-skill files, model-comparison
  page, and existing GPT/Gemini/DeepSeek bundle manifests.
- Applied full in-text project-source citations and marked page numbers as not
  applicable for internal workflow documents.
- `git diff --check` passes.

Remaining:
- Human review of the model-comparison wording, current model labels, and the
  final skill/loop names before publication.
