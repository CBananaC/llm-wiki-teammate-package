# Project Log

This is the single progress record for human teammates, Codex, Claude, and
other agents. Read it before changing the project. After each coherent
adjustment, append one entry to the bottom of the change log.

## Current state

- Phase: active project; human validation of the formal/sample tools and preparation of the competition hand-in
- Formal review editor: none (document-click emperor-action origin links added in both renderers; browser validation next)
- Canonical Stage 1 data: `review-tools/shared data/stage1_original_text.json`
- Formal review tool: `review-tools/(1) formal/index.html`
- Sample review tool: `review-tools/(2) sample/index.html`
- Model comparison: `review-tools/(3) model-output-comparison/index.html`
- Workflow map: `review-tools/(4) workflow/index.html`
- Research memory: `wiki/index.md`
- Student-facing deliverable: a dynamic introduction and teaching website for the review system
- Context folders: `2nd Material & FYP/` and `Competition Info/`
- Active Google Cloud CLI/ADC account: `myzhangrose@gmail.com`
- Active Gemini proxy project: `project-c9468478-3aaa-4bbc-b9a`
- Active Gemini proxy billing account: `billingAccounts/010B91-23E657-2A0942`
- Previous Gemini proxy project remains available at `delta-entry-496910-e7` until its service is retired.

## Next priorities

1. Plan and build the dynamic introduction/teaching website, using the competition brief as a provisional requirements reference.
2. Confirm that the sample shows 199 回應上諭 lines and loads the newest meaningful bundle.
3. Select a genuinely small, representative corpus for the sample tool.
4. Migrate active scripts from the original `outputs/attempt-002/` paths to the reorganized layout.
5. Classify shared review bundles as accepted, experimental, rejected, or archived.

## Known cautions

- The active formal and sample HTML files no longer embed original Stage 1 records; server-backed pages fetch `review-tools/shared data/stage1_original_text.json`. Their remaining inline document projection contains only derived AI review summaries and recipient projections.
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
- `tool/proxy/gemini-proxy/deploy.sh`
- `tool/proxy/PROXY_WEBSITES.md`
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

### 2026-07-23 15:15 HKT — Codex — Drafted the research-example and further-use section

Summary: Completed the final Traditional Chinese content section for the intro
website. It explains how to display selected 林爽文 research outcomes, present
information-delay calculations and strategy changes with provenance, demonstrate
human rejection of an unsupported AI pairing, and extend only verified results
to the LLM Wiki and future research questions.

Files:
- `intro Website/outline.md`
- `PROJECT_LOG.md`

Verified:
- Used the local FYP research draft, the project timing note, the 諭27 review
  bundle, and the project overview/workflow documents.
- Used full in-text citations and marked unpublished, internal, pending-page, and
  project-statistics evidence separately from published historical claims.
- `git diff --check` passes.

Remaining:
- Final editorial review of the complete outline, exact UI lane names, internal
  statistics, and missing FYP author/year metadata before publication.

### 2026-07-23 18:05 HKT — Codex — Revised the Qing document introduction

Summary: Revised the opening website section to introduce 奏折、硃批 and 上諭 as
three connected but distinct layers of Qing imperial communication. The revision
defines 奏折 as the upward official memorial, 硃批 as the emperor's vermilion
reply that may be absent, and 上諭 as an imperial instruction. It also separates
上諭 from 廷寄, explains that the communication chain is not automatic, and adds
a 林爽文 case example based on奏折 and 上諭 used alongside battle maps.

Files:
- `intro Website/outline.md`
- `PROJECT_LOG.md`

Verified:
- Consulted and visually checked the local 王劍 PDF, and read the relevant local
  宋希斌 and 李泰翰 source extracts.
- Added full in-text citations and marked the 宋希斌 page number as pending where
  the local excerpt does not expose a reliable book page.
- `git diff --check` passes.

Remaining:
- Human verification of the exact 宋希斌 book pages, 李泰翰 PDF page references,
  and the final project field names for 奏折、硃批、上諭 and 廷寄.

### 2026-07-23 18:11 HKT — Codex — Added the political and historical importance section

Summary: Added a Traditional Chinese section explaining why 奏折、硃批 and 上諭
are important for Qing political and historical research. The section connects
them to central decision-making, emperor–official relations, information delay,
first-hand evidence, local governance, military administration, and scalable
digital research, while also explaining their evidentiary limits.

Files:
- `intro Website/outline.md`
- `PROJECT_LOG.md`

Verified:
- Used 王劍、宋希斌、李智君 and 李泰翰 materials from `2nd Material & FYP`,
  together with the project corpus description.
- Added full in-text citations and clearly marked pending source pages and
  project-specific calculations for later verification.
- `git diff --check` passes.

Remaining:
- Human verification of the pending 宋希斌 and 李智君 page numbers and the exact
  document sample used for any information-delay statistics.

### 2026-07-23 16:00 HKT — Codex — Added merge controls for repeated emperor actions

Summary: Repeated 皇帝行動 cards now resolve stable `same_as` / `card_id` references to the earlier committed emperor-action dot. An uncommitted repeat offers both merge and standalone-add choices; an already separate repeat keeps its open button and offers a merge action.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both HTML files parse all inline scripts successfully.
- The persisted sample point `硃34#emperor#28` resolves to `evmrx6mkh6qw4`.
- Live sample-server UI shows `＋併入既有皇帝行動` for the requested card and both merge/standalone buttons for uncommitted repeat cards.
- `git diff --check` passes.

Remaining:
- No button was clicked during verification because doing so would alter the saved research state; the rendered handlers and data targets were inspected without mutation.

### 2026-07-23 16:23 HKT — Codex — Restored controls on all repeated Qing-event cards

Summary: Repeated 清方事件 cards now resolve saved `same_as` / `earliest_report` metadata even when `__matchReg` was not persisted. Every cross-document repeat exposes the merge-into-existing-event and independent-add choices; an already-added independent repeat keeps its dot and shows a disabled independent-state control plus the merge-to-source action.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both HTML files parse all inline scripts successfully.
- The saved sample `硃21` repeat `常青起程親赴泉州` resolves to the existing `硃26` event `常青起程前往蚶江` (`evmrx7ik2zzv2`).
- The saved-data renderer check found controls on all 5 formal and 154 sample cross-document repeat cards.
- `git diff --check` passes and the new helper/action sections are parity-identical between formal and sample.

Remaining:
- No state-mutating button click was performed; visual browser verification remains for the next available local browser session.

### 2026-07-23 16:36 HKT — Codex — Kept repeat merge handler in the AI-panel scope

Summary: Corrected the repeat merge helper so the global commit routine receives the panel-local repeat target explicitly. This prevents a real button click from losing access to the resolver nested in `renderAI`.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Inline-script parsing and `git diff --check` pass for both tools.
- Formal/sample repeat-target, action-markup, and handler sections are parity-identical.
- An in-memory click simulation commits both the unadded and already-added `硃21` repeat to `evmrx7ik2zzv2` and adds the `硃21` source mention without touching the saved file.

Remaining:
- No state-mutating browser click was performed; visual browser verification remains when a usable local browser session is available.

### 2026-07-24 15:51 HKT — Codex — Made Stage 1 JSON the live original-text source

Summary: Confirmed that both HTML files contain an embedded `DUAL` presentation
projection, while the previous JSON request only populated search indexing. Both
tools now load the canonical Stage 1 JSON at runtime and overlay matching
document bodies, rescripts, metadata, authors, and dates before rebuilding the
timeline. Reviewed AI summaries remain separate; the embedded projection is
kept only as a `file://`/offline fallback.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both HTML files' inline JavaScript parsed successfully.
- `git diff --check` passes.
- The project server loaded `/formal` and the shared JSON route at
  `http://127.0.0.1:8899`.
- The opened formal card for `硃65` matched the canonical JSON body exactly
  (873 characters), confirming the live card uses the shared source.

Remaining:
- Reload the website after editing `stage1_original_text.json`; existing open
  cards are refreshed automatically after the initial source load.
- The pre-existing formal-editor entry for emperor-action work remains unchanged
  in the current-state section.

### 2026-07-24 15:58 HKT — Codex — Anchored AI-loop emperor actions to their source document

Summary: Combined official-document/Yu emperor actions now carry an explicit
visual origin. Yu-origin actions use the 上諭's announce date and link only to
that Yu dot; Zhu-origin actions use the 硃批's receive date and link only to
that Zhu dot. Older outputs without origin metadata use the Yu-first, Zhu-
fallback rule, while all additional source quotations remain available as
evidence in the review card.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `tool/skills md/combine-confirmed-emperor-actions.md`
- `tool/proxy/gemini-proxy/main.py`
- `tool/scripts py/run_mass_prompt_chain_test.py`
- `PROJECT_LOG.md`

Verified:
- Both HTML files' inline JavaScript parsed successfully.
- Synthetic mixed-source checks passed for explicit Yu, explicit Zhu, and
  legacy Zhu fallback placement dates in both tools.
- Python syntax passed for the proxy and terminal AI-loop runner.
- `git diff --check` passed.

Remaining:
- Human visual confirmation remains pending because the in-app browser still
  refuses to reload the local file URL.

### 2026-07-24 16:17 HKT — Codex — Focused the active document card

Summary: Added a separate reading-card state to both review tools. When more
than one document card is open, the card being read now has a thin orange
outline. Clicking a card expands it, folds the other cards in the same panel,
and moves the reading state to the clicked card. Ctrl/⌘ multi-selection and
editing controls retain their existing behavior.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both HTML files' inline JavaScript parsed successfully.
- `git diff --check` passes.
- The live formal tool opened a 53-card panel; clicking one card left exactly
  that card expanded and reading while the other 52 cards folded.
- The computed reading outline uses the orange theme color.

Remaining:
- Human confirmation at the user's exact window size, if desired.

### 2026-07-24 17:14 HKT — Codex — Removed pictograms from AI panel cards

Summary: Refined the paired AI-panel renderer so combined Qing extraction cards
display `清廷行動`, Qing category badges remain Qing-only, and repeated reports
retain the `併入已有事件` / `獨立加入` choices. Removed pictographic markers
from event facts, source metadata, response cards, and related panel labels while
keeping the underlying text and controls unchanged.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- All 5 formal and 6 sample inline scripts parsed successfully with Node.
- Targeted checks passed for `清廷行動`, Qing-only categories, repeat controls,
  and the absence of pictographic emoji code points.
- `git diff --check` passed.

Remaining:
- Browser visual verification was unavailable in this environment; no
  state-mutating UI click was performed.

### 2026-07-25 13:13 HKT — Codex — Removed the header 編輯圓點 trigger

Summary: Removed the visible `編輯圓點` header button in both review tools and moved its six existing actions into `工具 > 編輯圓點`, preserving edit, add-dot, link, clear-links, add-event, and hidden-dot functionality.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both embedded UIs parsed successfully with Node.
- The header contains no `tb-editbtn` or `tb-editpop`; each of the six edit action IDs remains exactly once inside the Tools dropdown.
- `git diff --check` passed.

Remaining:
- Human visual confirmation of the revised Tools dropdown in both review tools.

### 2026-07-25 13:10 HKT — Codex — Simplified the Tools dropdown

Summary: Replaced `清快取` with `載入技能輸出`, removed the Skills and Bundles buttons and the Display group, and renamed the font-size group to `字級` in both review tools. Removed the obsolete cache handler and guarded the removed Display handlers so the pages remain error-free.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both embedded UIs parsed successfully with Node.
- Both pages contain one `載入技能輸出` button and no cache, Skills, Bundles, chart-display, or theme-toggle dropdown controls.
- `git diff --check` passed.

Remaining:
- Human visual confirmation of the revised Tools dropdown in both review tools.

### 2026-07-24 17:43 HKT — Codex — Grouped responding Yu and Zhu evidence

Summary: Kept the responding `上諭` and its related `硃批` evidence inside one
bordered source group in the combined `皇帝行動` card. Individual source units
still have clear separators, explicit 奏摺-first ordering, and each 上諭 source
now shows only its title and date without the redundant `上諭` and `日期`
metadata labels.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- All 5 formal and 6 sample inline scripts parsed successfully with Node.
- Synthetic formal/sample source renders passed for grouped Zhu/Yu output,
  奏摺-first ordering, and unlabeled 上諭 metadata.
- `git diff --check` passed for both HTML files.

Remaining:
- Browser visual verification was unavailable in this environment; no
  state-mutating UI click was performed.

### 2026-07-24 17:30 HKT — Codex — Hid empty trace cards and clarified emperor sources

Summary: Removed empty `追溯來源` result cards when no source chains are
returned. Refined the paired `皇帝行動` source layout so each source's
quotation and metadata stay together, while a stronger divider separates the
next source.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- All 5 formal and 6 sample inline scripts parsed successfully with Node.
- Targeted checks passed for empty trace suppression, source-info border reset,
  and the inter-source divider in both tools.
- `git diff --check` passed.

Remaining:
- Browser visual verification was unavailable in this environment; no
  state-mutating UI click was performed.

### 2026-07-24 17:21 HKT — Codex — Simplified combined emperor-action cards

Summary: Updated the paired `皇帝行動` renderer for existing Zhu/Yu matches.
The card now uses one concise header, hides the overview block and action-type
label, shows `奏摺原文` before its 夾批 quotation, uses `夾批` / `尾批` labels,
and places separators between complete quotation/source-information units
instead of between a quotation and its own metadata.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- All 5 formal and 6 sample inline scripts parsed successfully with Node.
- Targeted renderer checks passed for the concise header, hidden overview and
  action-type label, memorial quotation ordering, and position labels.
- `git diff --check` passed.

Remaining:
- Browser visual verification was unavailable in this environment; no
  state-mutating UI click was performed.

### 2026-07-25 13:21 HKT — Codex — Kept edit-dot access on right-click and widened connection controls

Summary: Removed the 編輯圓點 action group from the Tools dropdown while retaining its hidden action targets for the timeline right-click menu. Made the 連線 and 時間軸 slider cards and tracks span the full dropdown width, using the header 介面字級 scale for their labels and values.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both paired HTML files passed embedded-script parsing.
- Hidden edit-dot targets and full-width connection rules passed targeted structural checks.
- `git diff --check` passed.

Remaining:
- Browser visual verification was unavailable in this environment; human visual confirmation is still needed.

### 2026-07-25 14:10 HKT — Codex — Matched the Tools icon to the document-panel gear

Summary: Replaced the header Tools control with the exact document-panel `IC.gear` SVG and removed the dropdown arrow. The control remains icon-only with its `工具` accessibility label and dropdown behavior.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both paired HTML files passed embedded-script parsing.
- Header gear paths match the document-panel gear exactly; no caret remains.
- `git diff --check` passed.

Remaining:
- Browser visual verification was unavailable in this environment; human visual confirmation is still needed.

### 2026-07-25 13:31 HKT — Codex — Replaced the Tools label with a settings icon

Summary: Replaced the visible 工具 text in the formal and sample header buttons with an inline settings SVG. The dropdown caret, behavior, title, and accessible label remain unchanged.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both paired HTML files passed embedded-script parsing.
- Both header buttons contain the settings icon and retain `aria-label="工具"`.
- `git diff --check` passed.

Remaining:
- Browser visual verification was unavailable in this environment; human visual confirmation is still needed.

### 2026-07-25 13:46 HKT — Codex — Restored official-loop cross-document repeat detection

Summary: Reintroduced the `repeat-report` stage in the official-document loop.
The stage now sends 林方 and 清方 cards to the Gemini `repeat_report` mode for
meaning-based sameness decisions, compares against current-run cards, earlier
official-loop bundle cards, and verified events in `formal_all.data`, and writes
the earliest reporting document's sent date into `earliest_report`. Same-document
matches and 皇帝行動 are excluded; nothing is merged automatically.

Files:
- `tool/scripts py/run_mass_prompt_chain_test.py`
- `tool/skills md/repeat-report-dedup.md`
- `PROJECT_LOG.md`

Verified:
- `python3 -m py_compile "tool/scripts py/run_mass_prompt_chain_test.py"`
  passed.
- `git diff --check` passed.
- Dry-run completed for 硃64 without proxy calls.
- A mocked repeat-report test produced `same_as` and `earliest_report` only for
  the later cross-document card.
- The bundle chain and manifest now declare the in-loop `repeat-report` stage.

Remaining:
- Run a real small two-document bundle with Gemini, inspect the 林/清 cards in
  the website, then run the December/January/February/March batches with the
  restored stage.

### 2026-07-25 13:53 HKT — Codex — Suppressed source chains for author-self-reported events

Summary: Changed the official-document extraction path so an event reported by
the memorial's own author is treated as direct testimony. The terminal loop no
longer calls source-chain tracing for those events, and both formal and sample
UIs hide stale or newly generated source-chain blocks and source-search controls
for them. The event's own quotation remains visible as the primary evidence.

Files:
- `tool/scripts py/run_mass_prompt_chain_test.py`
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Python compilation passed.
- All embedded JavaScript blocks parsed: 5 formal, 6 sample.
- `git diff --check` passed.
- Detection tests passed for an author-named relation source, explicit
  `親歷`, and a report sourced to another official.
- Resuming an older bundle removes stale author-self source-chain rows before
  writing the cleaned `source-chain.json`.

Remaining:
- Human visual confirmation in both review tools, especially for mixed cards
  containing both direct author reports and earlier-source events.

### 2026-07-25 13:36 HKT — Codex — Simplified AI current-card scope control

Summary: Removed the `單一／部分／全部` scope dropdown from the AI typing area. The composer now displays the document dot currently selected on the chart, and a normal chart-card click resets the AI context to that document.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both paired HTML files passed embedded-script parsing.
- AI typing-area scope dropdown markup and old scope-choice error text are absent.
- Normal chart-card click resets to one current document; draft flushing occurs before the context switch.
- `git diff --check` passed for the touched files.

Remaining:
- Browser visual verification was unavailable in this environment; human visual confirmation is still needed.

### 2026-07-25 13:30 HKT — Codex — Refined source-chain completion and composer feedback

Summary: Moved `✓ 已加入來源鏈` to the bottom action area of committed source-chain cards, removed the per-event `▸ 搜尋來源` control, and suppressed add-success messages from the AI composer so the typing area stays clear.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both paired HTML files passed embedded-script parsing.
- Committed source-chain status placement and removal of the per-event source-search control passed targeted structural checks.
- `git diff --check` passed for the touched files.

Remaining:
- Browser visual verification was unavailable in this environment; human visual confirmation is still needed.

### 2026-07-25 13:25 HKT — Codex — Unified header button typeface

Summary: Made every button in the header toolbar inherit the same typeface as the left-side filter controls in both formal and sample tools.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both paired HTML files passed embedded-script parsing.
- Header font rule was found exactly once in each page.
- `git diff --check` passed.

Remaining:
- Browser visual verification was unavailable in this environment; human visual confirmation is still needed.

### 2026-07-25 13:55 HKT — Codex — Removed outer emperor-action quotation border

Summary: Removed the outer box, border, background, and inset padding around the combined quotation group in `皇帝行動` cards while retaining the individual quotation panels and source separators.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both paired HTML files passed embedded-script parsing.
- The shared emperor-action quotation-group style was reset consistently in formal and sample.
- `git diff --check` passed.

Remaining:
- Browser visual verification was unavailable in this environment; human visual confirmation is still needed.

### 2026-07-25 14:01 HKT — Codex — Restored all open-document AI chat output

Summary: Decoupled the AI chat display from the current clicked-document target. The panel now shows saved AI turns from all open document stores and matching multi-document groups, while new prompts continue to use the clicked document as their active target.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both paired HTML files passed embedded-script parsing.
- The all-chat view and current-store write bridge passed targeted structural checks.
- `git diff --check` passed.

Remaining:
- Browser visual verification was unavailable in this environment; human visual confirmation is still needed.

### 2026-07-25 14:15 HKT — Codex — Restored saved AI output from all workspace groups

Summary: Expanded the AI panel's read-only history to include every persisted workspace group, including multi-document AI-loop runs whose source cards are not currently open. New prompts still write to the clicked document's active store.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both paired HTML files passed embedded-script syntax parsing.
- Live formal-tool verification rendered 602 AI output cards with visible scroll content and confirmed saved outputs including 硃25, 硃71, and 諭43.
- `git diff --check` passed for the touched UI and log patch.

Remaining:
- Browser visual verification used the live formal tool; the sample page still has only static paired-file checks.

### 2026-07-25 14:21 HKT — Codex — Fixed sample AI panel render exception

Summary: Restored the missing `isAuthorSelfReportCandidate` helper in the sample tool so extract cards can render their source-chain controls without aborting the entire AI chat panel.

Files:
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both paired HTML files passed embedded-script syntax parsing.
- Reproduced the sample AI-panel interaction against the local server: 214 output cards rendered and the browser captured no errors.
- `git diff --check` passed.

Remaining:
- Formal-page visual verification was not repeated because the helper was already present there; formal/sample parity is confirmed by the paired source check.

### 2026-07-25 14:27 HKT — Codex — Restored repeat labels for legacy loop bundles

Summary: Made the formal and sample AI panels recognize the existing `same_as` and `earliest_report` fields written by earlier terminal repeat-report runs, even when those bundles lack the newer `repeat_verdict` field. Future terminal runs now persist `repeat_verdict: same` for exact matches.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `tool/scripts py/run_mass_prompt_chain_test.py`
- `PROJECT_LOG.md`

Verified:
- The `zhu83-official-loop` bundle contains one 林 and five 清 cross-document repeat annotations.
- Python compilation, both embedded HTML-script syntax checks, and `git diff --check` passed.

Remaining:
- Reload the bundle in the website AI panel to visually confirm the warning labels; no browser session was available in this check.

### 2026-07-25 14:31 HKT — Codex — Skipped routine 硃批 acknowledgments in 皇帝行動

Summary: The terminal official-document loop now excludes standalone routine rescripts `知道了。欽此。`, `覽`, and `覽。欽此。` from the combined emperor-action source set. Existing linked 上諭 sources remain eligible for substantive emperor actions, and a substantive 夾批 in the same document is preserved.

Files:
- `tool/scripts py/run_mass_prompt_chain_test.py`
- `tool/skills md/emperor-actions-confirmed-zhu-yu.md`
- `PROJECT_LOG.md`

Verified:
- Python compilation passed.
- Routine-acknowledgment cases passed, while `已有旨了。欽此。` and `好` remain eligible.
- `git diff --check` passed.

Remaining:
- The local Git index is read-only in this environment, so the required local checkpoint commit could not be created.

### 2026-07-26 23:42 HKT — Codex — Added December provisional cards to terminal deduplication

Summary: The global 林方／清方 repeat-report stage now automatically loads extracted cards from `zhu-december-rerun-g36` as an unverified historical candidate pool. It compares current-run cards against those cards and formal verified events, orders candidates by reporting-document send date, and records the historical bundle when it supplies the matched repeat title.

Files:
- `tool/scripts py/run_mass_prompt_chain_test.py`
- `PROJECT_LOG.md`

Verified:
- The December bundle contributes 70 林方 and 173 清方 provisional candidates.
- A mocked repeat-report call confirmed that a December candidate is sent to the LLM comparison stage.
- Python compilation and `git diff --check` passed.

Remaining:
- The existing Git index is read-only here, so no local checkpoint commit was created.

### 2026-07-27 00:12 HKT — Codex — Separated dedup output and made official responses document-scoped

Summary: The terminal loop now writes 林方／清方 dedup results to a separate bundle, compares them with `zhu-december-rerun-g36` and that dedup bundle's previous output, and tracks the dedup completion marker with its source document IDs. Official-response now runs after the emperor-action stage for each document, so an old global completion marker cannot suppress newly added documents.

Files:
- `tool/scripts py/run_mass_prompt_chain_test.py`
- `PROJECT_LOG.md`

Verified:
- Dry-run confirmed the comparison bundles are `zhu-december-rerun-g36` and `zhu-january-dedup`.
- Python compilation and `git diff --check` passed.

Remaining:
- The existing Git index is read-only here, so no local checkpoint commit was created.

### 2026-07-25 15:01 HKT — Codex — Repaired Zhu 22 emperor-action source pairing

Summary: Updated the formal and sample 皇帝行動 renderers for `zhu-december-rerun-g36`. A responding 上諭 now follows its related 奏摺 quote before any separate 尾批, and a missing 上諭 quote is recovered from the identified 上諭 record only when the bundle source list omits it.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- The Zhu 22 first point renders in 奏摺 → 上諭 → 尾批 order.
- The second point renders the exact 諭13 sentence containing「跡涉張皇」.
- Both embedded HTML script sets parsed, the bundle-specific renderer check passed, and `git diff --check` passed.

Remaining:
- The local Git index is read-only in this environment, so the required local checkpoint commit still needs to be created when index write access is available.

### 2026-07-25 15:03 HKT — Codex — Created local checkpoint

Summary: Created local commit `e127027` for the paired Zhu 22 emperor-action renderer repair.

Verified:
- Only the two HTML files and `PROJECT_LOG.md` were included; unrelated saved bundle changes remain unstaged.

### 2026-07-25 15:17 HKT — Codex — Grouped responding sources in emperor-action cards

Summary: Changed the formal and sample 皇帝行動 source renderers so each 奏摺 and its responding 上諭／硃批 sources render inside one response group. Separators now appear only between independent source groups, not between a quotation and its response.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- The `zhu-december-rerun-g36` Zhu 22 first point renders its 奏摺 quote before the responding 上諭 and keeps all three source blocks inside one group.
- A synthetic multi-source case creates separate groups at the next 奏摺 boundary.
- Both embedded HTML script sets parsed and `git diff --check` passed.

Remaining:
- Unrelated sample state and review-bundle changes remain unstaged.

### 2026-07-25 16:14 HKT — Codex — Removed AI chat panel auto-repositioning

Summary: Removed the shared chat-log scroll-anchor restoration that ran after panel buttons re-rendered AI output, including `用文書發送日` and source-chain add actions. Browser scroll anchoring is also disabled on the chat log so the panel keeps the user's current viewport without delayed movement.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both embedded HTML script sets parsed and `git diff --check` passed.
- The local sample preview opened the AI panel with `overflow-anchor: none`, and the legacy `__anchor` restoration code was absent.

Remaining:
- Unrelated sample state, review-bundle, proxy, and script changes remain unstaged.

### 2026-07-25 16:43 HKT — Codex — Reduced AI chat panel button lag

Summary: Debounced the large localStorage cache write and reused one serialized edit payload for server and local persistence, with a pagehide flush for exit safety. Button-triggered AI chat refreshes now skip the global candidate cleanup and emperor-event repair scan; those checks still run on full refreshes. Removed the remaining chart auto-focus after emperor-action buttons so clicks do not reposition the visible chart.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both embedded HTML script sets parsed successfully.
- `git diff --check` passed.
- The formal and sample implementations contain the same fast-refresh and debounced-persistence behavior.

Remaining:
- Unrelated sample state, review-bundle, proxy, and script changes remain unstaged.
- Interactive timing should be rechecked in the running website with a large AI output bundle.

### 2026-07-25 16:54 HKT — Codex — Removed automatic AI chat scroll restoration

Summary: Removed the remaining AI-chat viewport restoration paths in formal and sample. Quote clicks no longer capture and restore the AI card/panel position, AI output refreshes no longer jump to the latest result, and the note editor no longer snaps its AI log to the bottom. Explicit user navigation such as the table of contents and 最近卡片 remains available.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both embedded HTML script sets parsed successfully.
- `git diff --check` passed.
- No `captureAIQuoteAnchor`, `restoreAIQuoteAnchor`, or AI-log `log.scrollTop` restoration remains.

Remaining:
- Unrelated sample state, review-bundle, proxy, script, and earlier unstaged HTML changes remain untouched.

### 2026-07-27 00:05 HKT — Codex — Redeployed Gemini proxy under myzhangrose billing

Summary: Authenticated `myzhangrose@gmail.com`, enabled the required Google Cloud services in its project, and redeployed the Gemini proxy so Vertex AI usage runs through that project and its billing account.

Files:
- `PROJECT_LOG.md`

External deployment:
- Project: `project-c9468478-3aaa-4bbc-b9a`
- Billing account: `billingAccounts/010B91-23E657-2A0942` (`我的结算账号`)
- Cloud Run service: `gemini-proxy`
- Service URL: `https://gemini-proxy-bxtckyrt7q-de.a.run.app`
- Runtime model: `gemini-3.5-flash`

Verified:
- Cloud Run creator and last modifier are `myzhangrose@gmail.com`.
- The health endpoint returned `ok: true` and the target project.
- The target project was confirmed billing-enabled before deployment; a final billing API read hit a temporary Google Cloud quota limit.

Remaining:
- Update the timeline panel's AI settings to use the new service URL.
- Retire the old service only after the new URL is confirmed in the website.

### 2026-07-27 00:21 HKT — Codex — Restored repeat labels from terminal AI bundles

Summary: Preserved repeat-report fields when loading 林方／清方 event cards and taught both AI-chat renderers to read `same_as_event_id`, `same_as_event_ids`, and `repeat_of_title` in addition to the older `same_as`／`earliest_report` shape. Provisional bundle IDs now resolve to a loaded earlier event when possible; bundle-only matches still show the repeat warning and independent-add control.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- The zhu83 bundle contains repeat annotations on 12/18 林方 cards and 21/61 清方 cards.
- Both HTML implementations passed fixtures for bundle-only repeats and provisional IDs with a loaded alternate event ID.
- Both embedded HTML script sets parsed successfully, the formal tool reloaded without console errors, and `git diff --check` passed.

Remaining:
- Interactive verification with the full `zhu83-official-loop` bundle remains limited because the local browser state was not modified with the bundle during this check.
- Unrelated sample state, review-bundle, proxy, and script changes remain unstaged.

### 2026-07-27 00:42 HKT — Codex — Repaired incomplete 硃97 repeat labels

Summary: AI cards now enrich an incomplete `__matchReg` pointer from its linked earlier candidate before rendering the repeat notice. This prevents 硃97 from falling back to the generic `已於 較早文書 回報過` text when the earlier title, source document, or reporter was present in the linked card but missing from the pointer snapshot.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both HTML implementations parsed successfully.
- A fixture with an empty repeat pointer recovered the earlier title `常青親赴泉州調度防務`, source `硃21`, and reporter `常青` in both tools.
- `git diff --check` passed.

Remaining:
- The full 硃97 bundle was not reloaded into the browser during this check; the reproduced pointer path was verified directly against both renderers.
- Unrelated project, sample-state, review-bundle, proxy, and script changes remain untouched.

### 2026-07-27 01:50 HKT — Codex — Enabled incremental dedup-bundle writes

Summary: Cross-document 林方／清方 deduplication now writes its separate bundle after each comparison, including partial progress after a failed comparison, so a long run can resume without waiting for the entire dedup pass to finish.

Files:
- `tool/scripts py/run_mass_prompt_chain_test.py`
- `PROJECT_LOG.md`

Verified:
- Python compilation and `git diff --check` passed before the January run.
- January 1787 run completed with 54/54 document statuses, Lin 44/128 repeat classifications, Qing 84/332 repeat classifications, and per-document official-response processing.
- No `responseError`, traceback, remote-disconnect, or failed-run text was found in the January bundles.

Remaining:
- January and February 1787 runs are complete. The February bundle has 41/41 document statuses, 51 Lin cards, 184 Qing cards, 32 emperor-action source groups, 66 official-response cards, 12/51 Lin repeats, and 13/184 Qing repeats.
- The February dedup marker records comparison against `zhu-december-rerun-g36` and `zhu-february-dedup`; no response errors or tracebacks remain.
- The runner/script edit could not be committed because Git could not create `.git/index.lock` in this environment.

### 2026-07-27 11:49 HKT — Codex — Scoped AI chat pair output and bundle ordering

Summary: Each document AI panel now shows `⇄ 上諭回應的奏折` turns only when the panel's document is one of the relationship documents. Bundle-loaded output is ordered within each bundle as 林方 events, 清方 events (`已執行軍事`、`待執行軍事`、`非軍事`), 皇帝行動, then 官員回應.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Formal and sample chat-render blocks are identical.
- Both HTML implementations passed inline-script parsing, pair-scope and bundle-rank fixtures, and `git diff --check`.

Remaining:
- Full interactive browser verification with a loaded multi-document bundle remains pending.

### 2026-07-27 12:04 HKT — Codex — Collapsed standalone repeat-report cards

Summary: AI panels now treat a standalone `dedup`／repeat-report bundle as annotation data rather than a second event run. Matching 林方／清方 cards are kept once, repeat metadata is transferred to the substantive card, and unmatched dedup candidates remain visible.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- The saved 硃137 fixture changed from 15 stored turns to 11 visible turns, with four duplicate extract cards collapsed and the repeat title preserved on the original Qing card.
- Formal and sample chat-render blocks remained identical; both HTML implementations parsed successfully and `git diff --check` passed.

Remaining:
- Full interactive browser verification remains unavailable because the local preview server is isolated from the browser process in this environment.

### 2026-07-27 11:54 HKT — Codex — Ran January and February 1787 上諭 loops with Gemini 3.6 Flash

Summary: Ran the January 1787 上諭 set (21 documents) and then the February 1787 上諭 set (34 documents) sequentially through the provided Gemini proxy with `gemini-3.6-flash`. The runner wrote each stage JSON and per-document status incrementally as documents completed.

Files:
- `review-tools/shared data/review-bundles/yu-1787-01-gemini36-full/`
- `review-tools/shared data/review-bundles/yu-1787-02-gemini36-full/`
- `review-tools/shared data/review-bundles/yu-1787-02-repair-116-gemini36/`
- `PROJECT_LOG.md`

Verified:
- January and February manifests contain the expected chronological 上諭 IDs and model `gemini-3.6-flash`.
- All 21 January and 34 February documents have summary, division, reported-events, emperor-action, and official-response status flags; both repeat-report passes completed.
- January output counts are 21 summaries, 21 divisions, 24 林方 cards, 68 清方 cards, 20 emperor-action rows, and 89 official-response rows.
- February output counts are 34 summaries, 34 divisions, 37 林方 cards, 107 清方 cards, 32 emperor-action rows, and 121 official-response rows.
- A January HTTP 502 and a February final-call timeout were recovered automatically. A separate February timeout left one empty `諭116` official-response row; the document was rerun in the repair bundle, and its two recovered response items were integrated into the final February row. Final `諭116` response-item counts are 2, 1, 2, and 2.
- Final JSON parsing, status checks, action/response row checks, and error-field scans passed for both month bundles.

Remaining:
- The proxy does not have pricing configured for `gemini-3.6-flash`, so cost summaries report no USD estimate.
- The final bundles still require human loading/review in the timeline interface.

### 2026-07-27 12:39 HKT — Codex — Normalized AI chat table of contents

Summary: Updated the formal and sample AI-chat TOC dropdowns so entries show only the skill name, with the time and bundle name beneath it as lighter metadata. Removed symbols, document IDs, and result counts from TOC titles, kept each title on one line, and constrained the dropdown to the AI panel bounds.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- All embedded script blocks parsed successfully in both HTML files.
- Formal and sample TOCs rendered with full-width single-line titles and lighter time metadata; bundle metadata appeared when present.
- Formal and sample dropdown rectangles stayed within their respective AI panel rectangles in the local browser.
- `git diff --check` passed.

Remaining:
- No remaining implementation work; human visual confirmation can be done after reloading either review tool if desired.

### 2026-07-27 12:49 HKT — Codex — Resolved dedup bundle pointers in AI cards

Summary: Corrected formal and sample AI-chat loading of repeat-report bundles. Dedup turns now resolve `run:<doc>:<index>` references to the earlier canonical card, retain the repeat marker there, ignore local bundle-only pointers, and never render unmatched dedup annotations as independent events.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both HTML files' embedded scripts parsed successfully.
- `git diff --check` passed.
- A focused `硃146` fixture resolved to the earlier `硃87` card; a title-only local bundle pointer was rejected.
- Existing bundle and saved-data files were not edited.

Remaining:
- Live browser visual confirmation is still needed after reloading the review tool.

### 2026-07-27 13:06 HKT — Codex — Refined AI chat settings popover

Summary: Updated the formal and sample AI chat settings popover so its labels, fields, memory checkbox, and action controls follow `正文` through `--fs`; made it full width and bounded to the AI panel; changed the label to `API Base`; replaced the text refresh and API-key symbols with the shared SVG icon style; and removed the proxy-help note, `使用本機` control, and its unused styling. The proxy URL field remains editable.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both HTML files' embedded scripts parsed successfully.
- `git diff --check` passed.
- The live formal AI settings popover rendered at the AI panel width, stayed within the panel bounds, showed `API Base`, omitted the removed text and button, and used SVG refresh/eye controls with matching field heights.

Remaining:
- Sample parity was verified by matching source changes and script parsing; the local preview server exposed the formal tool for live visual inspection.

### 2026-07-27 13:18 HKT — Codex — Confined AI settings to card display area

Summary: Adjusted the formal and sample AI settings popovers to use the AI card display region (`.chat-log`) as their vertical boundary, so the settings no longer cover the typing/composer area. Changed all settings typography and control sizing from `正文` (`--fs`) to `字級` (`--ui-fs`).

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both HTML files' embedded scripts parsed successfully.
- `git diff --check` passed.
- Live formal-panel geometry showed the settings popover entirely inside `.chat-log` and not overlapping `.chat-box`; computed settings controls followed the `--ui-fs` scale.

Remaining:
- Human confirmation after reloading the sample tool remains useful.

### 2026-07-27 13:04 HKT — Codex — Preserved duplicate cards and removed dedup self-links

Summary: Confirmed that the January and February dedup manifests compared against their own output bundles, producing self-referential `same_as_event_id` values. Kept dedup cards visible, changed repeat display to prefer external `run:<doc>:<index>` references, retained each card's own title, guarded the runner against self-comparison, and repaired current self-primary dedup fields while preserving all event rows.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `tool/scripts py/run_mass_prompt_chain_test.py`
- `review-tools/shared data/review-bundles/zhu-january-dedup/manifest.json`
- `review-tools/shared data/review-bundles/zhu-january-dedup/outputs/lin-events.json`
- `review-tools/shared data/review-bundles/zhu-january-dedup/outputs/qing-actions-all.json`
- `review-tools/shared data/review-bundles/zhu-february-dedup/manifest.json`
- `review-tools/shared data/review-bundles/zhu-february-dedup/outputs/lin-events.json`
- `review-tools/shared data/review-bundles/zhu-february-dedup/outputs/qing-actions-all.json`
- `PROJECT_LOG.md`

Verified:
- January and February manifests no longer list themselves as comparison bundles.
- No current dedup output retains its own bundle as `same_as_event_id`.
- `硃146` now stores `same_as_event_id: run:硃87:19`; its 332 Qing cards remain present.
- Both HTML files parse and `git diff --check` passes.

Remaining:
- Existing generated bundle/data edits from the ongoing reruns remain unstaged; live browser visual confirmation is still needed after reload.

### 2026-07-27 12:52 HKT — Codex — Ordered legacy prior-edict pair cards

Summary: Moved `回應先前上諭（既有配對）` docpair turns ahead of the new AI-loop event cards while keeping them immediately after ordinary `上諭回應的奏折` pairs. The loop order now starts with source pairs, then prior-edict analysis, then 林方／清方／皇帝／官員回應 output.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- A focused `硃146` sort fixture produced the requested order.
- Both HTML files' embedded scripts parsed successfully.
- `git diff --check` passed.

Remaining:
- Live browser visual confirmation is still needed after reloading the review tool.

### 2026-07-27 12:56 HKT — Codex — Collapsed duplicate AI-panel TOC entries

Summary: Updated the formal and sample AI-panel TOCs to group consecutive turns by their visible label, including ordinary source-pair turns and per-label bundle stages. Repeated labels now show a count such as `上諭回應的奏折（6）` or `擷取林方行動（4）`, while single entries remain unchanged.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Synthetic `AAAABCDD` fixture rendered as `A（4） B C D（2）`.
- Both HTML files' embedded scripts parsed successfully.
- `git diff --check` passed.

Remaining:
- Live browser visual confirmation is still needed after reloading the review tool.

### 2026-07-27 13:27 HKT — Codex — Added clean cross-month dedup reruns

Summary: Added a dedup-only rerun path for existing official-loop bundles. January can compare only against December, and February can compare against the freshly rerun January dedup bundle plus December. Same-document and same-card pointers are rejected before output, while earlier report author, document title, and document ID are stored for the repeat label.

Files:
- `tool/scripts py/run_mass_prompt_chain_test.py`
- `tool/skills md/repeat-report-dedup.md`
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- `--dedup-only` dry-run printed the requested December comparison pool for a 硃146 example.
- A local deterministic mock processed the six 硃146 林／清 cards and emitted no same-document references; each repeat included `repeat_report_author`, `repeat_report_doc_title`, and `repeat_report_doc_id`.
- Both HTML files' embedded scripts parsed, Python compilation passed, and `git diff --check` passed.
- The mock was used only for plumbing validation; no research text was sent to the external Gemini proxy because that network request was not authorized in this environment.

Remaining:
- Run the supplied January command, then the February command, with the configured proxy to obtain real model judgments.

### 2026-07-27 13:27 HKT — Codex — Added provider-driven model dropdown

Summary: Replaced the main AI chat settings model text field and refresh button with a native dropdown in both formal and sample tools. The dropdown starts with the provider fallback models, and focusing or changing `AI 服務` triggers `/models` discovery; returned provider models replace the list while preserving the selected model.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both HTML files' embedded scripts parsed successfully.
- `git diff --check` passed.
- Live formal preview showed a native model `<select>` with no refresh button; switching to `OpenAI GPT` populated its fallback model list and displayed the provider error state only because the local AI service was not running.

Remaining:
- With the AI service running and provider credentials configured, live `/models` results will replace the fallback lists; the sample tool should be visually reloaded for human confirmation.

### 2026-07-27 13:29 HKT — Codex — Recovered blank AI event subtitles

Summary: Restored visible titles for AI-loop 林方／清方 event cards whose saved `subtitle` field is empty. The paired renderers now recover the title from repeat metadata, linked source-chain events, or source labels before showing a neutral fallback; newly normalized loop items use the same recovery path.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both HTML files' embedded scripts parsed successfully.
- `git diff --check` passed.
- After a live sample reload and 硃24 selection, all 63 rendered event cards had nonblank titles; the affected Lin card displayed `林爽文等結黨搶劫`.
- The existing saved state was not rewritten; its original blank fields remain recoverable through the renderer.

Remaining:
- No remaining display issue observed; human visual confirmation after reopening the formal tool remains useful.

### 2026-07-27 13:40 HKT — Codex — Prevented button tooltips from being covered

Summary: Replaced per-button tooltip pseudo-elements with a shared body-level tooltip portal in both review tools. Labels still appear after a short hover delay, but now stay above local panels and overflow boundaries, flip below buttons near the top edge, and remain clamped inside the viewport.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both HTML files' embedded scripts parsed successfully.
- `git diff --check` passed.
- Tooltip portal markup and behavior are present once in each HTML file.

Remaining:
- Human visual confirmation after reopening both review tools remains useful, especially for tooltips inside open drawers and dropdowns.

### 2026-07-27 13:45 HKT — Codex — Shortened button tooltip delay

Summary: Reduced the shared hover-tooltip delay from 600ms to 400ms in both review tools.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both HTML files use the same 400ms tooltip delay.

Remaining:
- Human visual confirmation after reopening both review tools remains useful.

### 2026-07-27 13:39 HKT — Codex — Added parallel repeat-report dedup workers

Summary: Added a dedicated bounded worker option for cross-document repeat-report searches. `--dedup-workers` accepts 2-8 and defaults to 6; candidate payloads are built chronologically and responses are applied in that order so parallel requests do not reorder or change the dedup output semantics.

Files:
- `tool/scripts py/run_mass_prompt_chain_test.py`
- `PROJECT_LOG.md`

Verified:
- Ran an exactly five-card `硃79` dedup-only test through a local deterministic mock with `--dedup-workers 6`; 5 requests completed and the mock observed up to 4 in flight because only four cards had candidates.
- The test output contained 5 cards, 5 mock repeat annotations, and 0 same-document repeat references.
- `--dedup-workers 1` is rejected; Python compilation and `git diff --check` passed.

Remaining:
- Real January and February reruns still require explicit authorization to send research text to the configured external model proxy.

### 2026-07-27 13:39 HKT — Codex — Restored editable model suggestions

Summary: Changed the AI chat model control in both formal and sample tools from a native select back to an editable text input with a clickable suggestion list below it. Clicking/focusing shows all known provider models; typing filters the suggestions; clicking a suggestion fills and saves the model. Added the requested GPT-5.5/GPT-5.6 Sol/Terra/Luna and Gemini 3.6 fallback entries, while live `/models` discovery remains able to replace them with the provider’s returned catalogue.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `tool/proxy/gemini-proxy/main.py`
- `tool/proxy/chatgpt-proxy/main.py`
- `PROJECT_LOG.md`

Verified:
- Both HTML files parsed successfully; both proxy Python files compiled successfully.
- `git diff --check` passed.
- Live formal preview showed an editable input, a clickable filtered suggestion list below it, and successful suggestion selection.
- TokenRouter suggestions included `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-5.5`, and `gpt-5.4`; Gemini suggestions included `gemini-3.6-flash` and related models.

Remaining:
- With a running provider proxy and credentials, the live `/models` response should be checked against each provider’s current catalogue.

### 2026-07-27 13:42 HKT — Codex — Restricted document filters to approved events

Summary: Removed unapproved AI chat findings from the document-panel filter projection. The filter now shows user annotations plus committed event/provenance highlights, with event chips rendered as a smaller filter type followed by the event title and without per-label counts. Clicking an event chip opens its existing event information card in a dedicated column immediately to the left of the document panel; multiple selected event cards share that column.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both HTML files' embedded scripts parsed successfully.
- `git diff --check` passed.
- Live sample verification showed no chip count elements, two-level event labels, and two clicked event cards in one column left of the 硃40 document panel.
- Live formal verification showed the same filter rendering path with the approved-only projection; no unapproved AI labels appeared.

Remaining:
- Existing unrelated working-tree changes and saved sample state were left untouched.

### 2026-07-27 13:55 HKT — Codex — Separated filter counts from highlight subtitles

Summary: Corrected the document-panel filter presentation. The dropdown now groups highlights by filter type and shows only the filter plus its count, such as `林方行動 3`; event subtitles are no longer repeated in the dropdown. The document highlight area now shows each highlight's filter type together with its event subtitle, and clicking an event highlight opens its information card beside the document panel.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both HTML files' embedded scripts parsed successfully.
- `git diff --check` passed.
- Live sample dropdown showed `林方行動 3`, `清軍事：已執行 6`, `清軍事：待執行 1`, and `來源鏈 5` without event titles.
- Live sample highlight markup showed filter type plus event subtitle, and clicking a highlight opened an event card in the column left of the document card.

Remaining:
- Existing unrelated working-tree changes remain untouched.

### 2026-07-27 13:56 HKT — Codex — Removed annotation indexes from highlight labels

Summary: Removed the separate numeric marker from event highlight-area labels. Highlight labels now contain only the filter type and event subtitle; numeric counts remain in the filter dropdown chips.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both HTML files' embedded scripts parsed successfully.
- `git diff --check` passed.

Remaining:
- Existing unrelated working-tree changes remain untouched.

### 2026-07-27 14:11 HKT — Codex — Added report dates to repeat labels

Summary: Repeat-report labels now append the referenced report document date after its title and ID, using stored `repeat_report_date` first and the referenced source document date as a fallback. The dedup runner also writes `repeat_report_date` for future bundles and clears stale values before reruns.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `tool/scripts py/run_mass_prompt_chain_test.py`
- `PROJECT_LOG.md`

Verified:
- Both HTML files' embedded scripts parsed successfully.
- The `天90` fallback record resolves to `1787/01/04`, producing the requested date suffix after `（天90）`.
- Python compilation and `git diff --check` passed.

Remaining:
- Human visual confirmation after reloading the formal and sample tools.

### 2026-07-27 14:15 HKT — Codex — Enabled repeat merges into existing chart events

Summary: Fixed repeat-card target resolution in both tools. When a repeat record's `same_as_event_id` already identifies a chart event, the UI now resolves that live event before falling back to the report-document metadata, so `併入已有事件` is enabled for existing dots such as the `硃83` targets.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Formal state contains the `硃83` target events `evmrd8qehqp5n` and `evmrd9see7hs5`.
- Both HTML files' embedded scripts parsed successfully and the live-target priority is present in both.
- `git diff --check` passed.

Remaining:
- Human click confirmation after reloading the formal and sample tools.

### 2026-07-27 14:58 HKT — Codex — Repaired repeat-target fallback and canonical repeat metadata

Summary: Repeat cards now prefer live chart events, but can also materialize a candidate-shaped merge target from `repeat_report_doc_id` when an old bundle points to an event ID that is not present in the current isolated state. Repeat labels now resolve reporter and date metadata through `stage1_original_text.json`, including aliases such as `天90` → canonical `硃90`, while retaining the AI event title in the label.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Canonical Stage 1 lookup for `天90` resolves to `硃90`, author `普吉保`, send date `1787/01/04`.
- Both HTML files' embedded scripts parsed successfully.
- `git diff --check` passed.

Remaining:
- Human click confirmation for a 硃83 repeat card after reloading the formal and sample tools.

### 2026-07-27 15:01 HKT — Codex — Corrected 天90 canonical alias priority

Summary: The canonical Stage 1 resolver now prefers `硃90` for a repeat pointer labelled `天90` before considering same-number `諭90`, preventing the unrelated 李侍堯 record from supplying the repeat label metadata.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Live sample 硃83 output displays `已由 普吉保 於 〈調遣建延水師兵渡臺〉（天90） (1787/01/04) 回報過`.
- The same repeat card contains an enabled `併入已有事件` button.
- Both HTML files' embedded scripts parsed successfully and `git diff --check` passed.

Remaining:
- No known implementation work remains for this request; formal visual confirmation is still optional.

### 2026-07-27 15:43 HKT — Codex — Reused and consolidated repeat-event dots

Summary: Repeat-card merge actions now prefer the existing chart event that carries the reported document, add the new document as a second source, and silently consolidate same-actor, same-title duplicate dots left by earlier repeat clicks. The existing-document lookup now tolerates archived repeat pointers while retaining title matching so unrelated events from the same document are not absorbed.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Formal 硃83's `賊匪直攻鳳山縣城` repeat reused the existing `硃77` + `硃83` event; the formal saved event set did not gain a new dot.
- A temporary sample test event was removed after verification; the pre-existing sample working-state changes remain untouched.
- Both HTML files' embedded scripts parsed successfully and `git diff --check` passed.

Remaining:
- Human confirmation of other repeat targets with different event titles remains advisable before bulk-cleaning saved event data.

### 2026-07-27 17:47 HKT — Codex — Redrew merged repeat events with complete source links

Summary: Fixed the repeat-merge render order in both review tools. The new source mention and duplicate-dot consolidation now finish before the chart redraw, so the surviving event's black tooltip and event-to-document line use the same source list. Event tooltips now identify source IDs with their document titles, and source lines carry explicit event/source metadata for `硃83` verification.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Formal `evmr4lfqnug4u` renders with one `.edot` and one `.elink[data-source-doc="硃83"]` after reload.
- Both HTML files' embedded scripts parsed successfully and `git diff --check` passed.

Remaining:
- The current sample saved state has no `硃83` event source to display; the sample renderer is updated in parity with formal.

### 2026-07-27 18:02 HKT — Codex — Refreshed repeat-event provenance labels

Summary: Fixed the missing redraw when a repeat pointer has no prior document ID. The surviving event now always redraws after its new source mention is added, so its source line and hover label cannot remain stale. Event-dot native labels now include each linked source document's ID, title, and canonical date, and the repeat-report jump label uses the same metadata.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Formal surviving event `evmr4lfqnug4u` has one dot, source lines for `硃77` and `硃83`, and a native hover title naming both source documents.
- Formal AI panel opened without console errors after reload.
- Sample rendered 208 event dots; a sample dot carried the native hover title and no console errors were reported.
- Both HTML files' embedded scripts parsed successfully and `git diff --check` passed.

Remaining:
- The unrelated pre-existing working-tree changes remain unstaged.

### 2026-07-27 18:04 HKT — Codex — Removed embedded original-source payloads from the active review tools

Summary: The formal and sample review pages now fetch their original document records from the canonical Stage 1 JSON at runtime. The large embedded `DUAL` and `TIMELINE` source-data payloads were removed; the main timeline keeps only the derived AI review projection and rebuilds document metadata, original text, and rescripts from the fetched source.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Both active pages fetched and rendered the canonical source in the live review server: 363 document records, 393 dual-line dots, and overview totals of 279 official / 160 reply / 74 上諭 entries.
- The live 硃40 panel displayed its source body, while no original body prefix remained in either HTML file.
- Both HTML files' inline scripts parsed successfully, browser console error logs were empty, and `git diff --check` passed.
- No embedded `const DUAL = [...]` or `const TIMELINE = {...}` source payload remains in either active page.

Remaining:
- The archival `review-tools/(1) formal/sample_1.html` was not changed; the active server routes use the formal and sample `index.html` files above.

### 2026-07-27 18:14 HKT — Codex — Created structured Traditional Chinese website-content draft

Summary:
- Regenerated the introduction-website planning draft as a structured Traditional Chinese document with subtitles and prose paragraphs under each section.
- Reorganised the content around the platform as a reusable research framework for 奏摺 and 上諭, with the 林爽文事件 retained as the demonstration case.
- Added the AI processing loop between adapting information-extraction Skills and human verification, including JSON input, Python batch processing, AI API calls, intermediate review bundles, website import, and researcher review.

Files:
- `intro Website/網站內容草稿_第三稿.docx`
- `PROJECT_LOG.md`

Verified:
- The DOCX rendered to 14 pages with the document renderer.
- Visually inspected the cover, introduction, communication-reconstruction section, AI processing loop, reuse tutorial, and conclusion pages; no clipping or overlap was observed.

Remaining:
- The draft still needs the project-specific screenshots, repository/API links, final citations, and any confirmed author or affiliation information before it becomes the final website manuscript.

### 2026-07-27 18:26 HKT — Codex — Added a contents page to the website-content draft

Summary:
- Added a two-page contents section after the cover of `網站內容草稿_第三稿.docx`.
- The contents lists the introduction, platform workflow, communication reconstruction,奏摺／上諭 analysis branches, AI processing loop, human verification, reuse tutorial, and 林爽文示範 sections.
- Kept the contents as a draft navigation aid; the final website can convert it into linked interactive navigation.

Files:
- `intro Website/網站內容草稿_第三稿.docx`
- `PROJECT_LOG.md`

Verified:
- The updated DOCX rendered to 13 pages.
- Visually inspected the cover, both contents pages, the opening of the main draft, and the final pages; Chinese glyphs, headings, spacing, and page breaks rendered correctly.

Remaining:
- Add final website links and interactive page anchors when the website implementation is ready.

### 2026-07-27 18:39 HKT — Codex — Created StoryMap UI example

Summary:
- Added a standalone StoryMap-style HTML prototype for the introduction website.
- Demonstrated a fixed top tab, scrolling full-screen sections, adjustable backdrop/card placement through CSS variables, and optional title/subtitle/body card layers.
- Included example backdrop types for image, video, code, and a review-tool interface mockup that can later be replaced by the actual review website or iframe.

Files:
- `intro Website/storymap-example.html`
- `PROJECT_LOG.md`

Verified:
- HTML structure check passed.
- Embedded JavaScript passed syntax validation.
- `git diff --check` passed for the new prototype.

Remaining:
- Replace demonstration assets and mock review-tool content with project-approved media and the final website embed when available.

### 2026-07-27 18:52 HKT — Codex — Simplified 硃83 quotation-review example

Summary:
- Updated `storymap-example.html` so the 硃83 demonstration contains only an AI chat/output panel and a full original-document panel.
- Kept one AI result card with the 清方行動 extraction and the source quotation 「至續派之福寧鎮及銅山、羅源等營，共兵一千名，亦催令陸續繼進」.
- Clicking the quotation selects the card, scrolls to the matching passage in the original document panel, highlights it, and updates the review status message.

Files:
- `intro Website/storymap-example.html`
- `PROJECT_LOG.md`

Verified:
- Review-demo structure check passed: one AI output card, one original-document panel, and no extra floating card in the example.
- Embedded JavaScript passed syntax validation.
- `git diff --check` passed.

Remaining:
- Live click testing in the in-app browser was blocked because the browser security policy would not reload the local `file://` page; the interaction was checked statically instead.

### 2026-07-27 18:34 HKT — Codex — Preserved existing events during repeat-source merges

Summary:
- Changed repeat merging in both review tools to reuse a live event dot that already carries the earlier report, even when the registry candidate itself is not marked as added.
- Removed destructive fuzzy duplicate removal from the repeat-source attachment path; adding a repeated report no longer deletes the previously added event.
- Coalesced the chart/document redraw into the next animation frame so the merge button is not blocked by a full timeline render.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `review-tools/(1) formal/formal_all.data`
- `PROJECT_LOG.md`

Verified:
- Parsed all embedded scripts in both HTML files successfully.
- Tested the `硃156` repeat card for `賊兵攻陷彰化縣城`: the existing event `evmr8qwl3e4r0` remained visible as one event and gained `硃156` as an additional source; no second matching event was created.
- `git diff --check` passed.

Remaining:
- Human confirmation of additional repeat targets, especially cases with non-identical titles, remains advisable.

### 2026-07-27 18:55 HKT — Codex — Restricted new annotations to modified text drags and retuned highlight labels

Summary:
- Updated both active review tools so `新增標註` requires an actual text drag with Command on macOS or Ctrl on Windows; ordinary selection and modifier-clicks do not open the editor.
- Moved inline annotation labels to the end of the complete matched quotation, including quotations split into multiple matched fragments or divisions; margin notes now anchor to the final visible mark.
- Unified the filter type and event title label typography and gave the label, note border, and highlight barrier a shared highlight-colour tone.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Parsed all embedded scripts in both HTML files successfully and `git diff --check` passed.
- Reloaded the live formal and sample pages after the edit; both rendered the canonical document view with no browser console errors.
- Confirmed the final-quote anchoring is applied in both renderers and that both files contain the same interaction/style changes.

Remaining:
- A human should perform one Mac Command-drag and one Windows Ctrl-drag on an event-bearing document to confirm the input modifier behavior on each platform; the automated coordinate drag test timed out in the narrow review pane and did not change saved data.

### 2026-07-27 19:07 HKT — Codex — Simplified highlight-label styling

Summary:
- Removed the nested label border and background so each inline highlight label has one shared boundary only.
- Made `林方行動` bold and darker while keeping the event title at the same compact size and font family.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Parsed all embedded scripts in both HTML files successfully and `git diff --check` passed.
- Reloaded the formal and sample pages in the live review server; both loaded successfully with empty browser error logs.

Remaining:
- Human visual confirmation on an event-bearing document remains advisable.

### 2026-07-27 19:13 HKT — Codex — Attached repeat reports to the surviving event and document link

Summary:
- Made repeat-source merging prefer the deduplication pointer's explicit existing event ID before resolving a live extraction candidate or falling back to title matching.
- Kept the surviving event dot, appended the repeated document as a source mention, and allowed the normal chart renderer to draw the event-to-document link.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `review-tools/(1) formal/formal_all.data`
- `PROJECT_LOG.md`

Verified:
- In the formal tool, merged the `硃21` repeated card `民變軍攻陷彰化城` into `evmr8qwl3e4r0` without creating a second event dot.
- Confirmed the surviving event contains `硃21` as a source and the chart contains one `硃21` event-link; the same state remained after reload.
- Parsed all embedded scripts in both HTML files successfully and `git diff --check` passed.

Remaining:
- Human confirmation of another repeat target with a different title remains advisable.

### 2026-07-27 19:36 HKT — Codex — Matched StoryMap 硃83 example to the sample review UI and source data

Summary:
- Replaced the custom review mock-up in `intro Website/storymap-example.html` with the sample review tool's visible panel structure: one `tool-box` AI panel with one `chat-extract` result card and one `card` original-document panel.
- Used the approved sample extraction for 硃83: `常青催令福寧鎮等兵繼進`, its description, location, actor, category, and exact source quotation.
- Embedded the complete canonical 硃83 original body from `review-tools/shared data/stage1_original_text.json`, including the date lines and 硃批 text; clicking the sample-style `.cx-q` quotation scrolls to and highlights its matching passage.
- Added working `加入` and `略過` review actions for the demonstration card.

Files:
- `intro Website/storymap-example.html`
- `PROJECT_LOG.md`

Verified:
- Confirmed the embedded original body exactly matches the canonical Stage 1 硃83 body, with one exact quotation occurrence.
- Confirmed there is one AI quotation card, one full original-document panel, and no extra StoryMap information card in the review-demo section.
- Parsed the embedded JavaScript successfully and `git diff --check` passed.

Remaining:
- Live interaction testing remains limited because the in-app browser blocks reloads of the local `file://` prototype; the source/data and interaction structure were statically verified.

### 2026-07-27 19:43 HKT — Codex — Converted the StoryMap review example to a customizable iframe

Summary:
- Added `intro Website/review-tool-embed.html` as a self-contained iframe version of the sample review UI.
- Updated the StoryMap review section to load the iframe with `doc=硃83&panels=ai,original`, showing only the AI panel and original-document panel.
- Added query-parameter handling so the embed can later switch documents and visible panels without changing the StoryMap layout.
- Kept the exact canonical 硃83 body and sample extraction data in the embed, including quotation highlighting and `加入`／`略過` review actions.

Files:
- `intro Website/storymap-example.html`
- `intro Website/review-tool-embed.html`
- `PROJECT_LOG.md`

Verified:
- Confirmed the iframe is present in the StoryMap review section and the embed reads `doc` and `panels` URL parameters.
- Confirmed the iframe body exactly matches the canonical Stage 1 硃83 body.
- Parsed JavaScript in both HTML files successfully and `git diff --check` passed.

Remaining:
- Live browser reload testing remains limited by the in-app browser's local `file://` security restriction; local static validation passed.

### 2026-07-27 20:02 HKT — Codex — Switched the StoryMap example to the real sample review-tool HTML

Summary:
- Replaced the StoryMap iframe source with `review-tools/(2) sample/index.html`, so the demonstration now uses the actual sample review-tool interface and its canonical data rather than a visual recreation.
- Added the same URL-driven embed mode to the formal and sample review tools. `embed=1`, `doc=硃83`, and `panels=ai,original` open one selected document, show the AI and original-document panels, hide the timeline and other tools, and preserve the full original-text area.
- Scoped the demonstration AI panel to the 硃83 extraction containing 「至續派之福寧鎮及銅山、羅源等營，共兵一千名，亦催令陸續繼進」.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `intro Website/storymap-example.html`
- `PROJECT_LOG.md`

Verified:
- Added the same embed CSS and initializer to both formal and sample HTML files, and exposed the loaded `DUAL` records for the initializer.
- Parsed all embedded scripts in both review-tool HTML files successfully and `git diff --check` passed.
- Confirmed the StoryMap iframe now targets the real sample HTML with the requested 硃83 and panel parameters.

Remaining:
- Live local `file://` verification remains limited by the in-app browser security restriction; the sample review tool may require its normal local server because it loads the canonical source through `/shared/stage1_original_text.json`.

### 2026-07-27 20:18 HKT — Codex — Added a file-mode source fallback for the embedded sample tool

Summary:
- Added a synchronized `file://` fallback to the formal and sample review-tool HTML files for the embedded 硃83 demonstration.
- The fallback contains the canonical 硃83 metadata and full original body, allowing the actual review-tool UI to initialise without a cross-origin `fetch`.
- Kept the normal `/shared/stage1_original_text.json` fetch for server-hosted use; only the embedded file-mode overview loader is skipped because the StoryMap displays the AI and original-document panels rather than the overview chart.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Parsed all embedded JavaScript in both HTML files successfully.
- Confirmed the fallback body exactly matches the canonical Stage 1 硃83 body in both files.
- Confirmed the fallback blocks are identical and `git diff --check` passed.

Remaining:
- Reload the StoryMap `file://` page to confirm the in-app browser renders the embedded panels after this fallback is applied.

### 2026-07-27 20:31 HKT — Codex — Started HTTP serving for the intro website

Summary:
- Started a static project-root server at `http://127.0.0.1:8765` for the intro StoryMap website.
- Kept the review-tool/API server running at `http://127.0.0.1:8766`.
- Updated the StoryMap review iframe to use the running sample review server when the StoryMap is opened over HTTP, while retaining its local relative path for direct `file://` use.

Files:
- `intro Website/storymap-example.html`
- `PROJECT_LOG.md`

Verified:
- The HTTP StoryMap URL and the embedded sample URL both returned HTTP 200.

Remaining:
- Open the HTTP StoryMap URL in the browser instead of the old `file://` tab.

### 2026-07-27 20:43 HKT — Codex — Prevented the StoryMap iframe from making an initial wrong-origin request

Summary:
- Removed the eager iframe `src` from the StoryMap review section so the static intro server does not first request the sample page from port 8765.
- The StoryMap now assigns the iframe URL directly: the file-relative sample page for `file://`, or the running review server at port 8766 for HTTP.
- Added an inline empty favicon to avoid the static server's unnecessary favicon 404.

Files:
- `intro Website/storymap-example.html`
- `PROJECT_LOG.md`

Verified:
- Parsed the StoryMap JavaScript successfully.
- Confirmed the iframe has no eager `src` and has both file-mode and HTTP routing paths.
- Confirmed the HTTP StoryMap still returned HTTP 200 and `git diff --check` passed.

Remaining:
- Refresh the HTTP StoryMap tab so the old failed iframe request is discarded.

### 2026-07-28 11:54 HKT — Codex — Restored the specified 硃83 AI card in the StoryMap embed

Summary:
- Fixed chat-state normalisation so saved AI conversations represented as numeric-keyed objects are retained instead of being replaced by an empty array.
- Added an embed-time server-state refresh and explicit AI-panel re-render so the example receives the saved sample data after the review card is opened.
- Updated the embed cache-buster and made the demonstration prefer the requested 「常青催令福寧鎮等兵繼進」 card when displaying the single example result.

Files:
- `intro Website/Website/storymap-example.html`
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Live HTTP StoryMap loaded at `127.0.0.1:8765` with the review iframe served by `127.0.0.1:8766`.
- The embedded AI panel displayed one visible 硃83 card containing the requested subtitle and quotation.
- The full original 硃83 document panel loaded, and browser error/warning logs were empty.
- `git diff --check` passed.

Remaining:
- Refresh the user's existing StoryMap tab once so it picks up the cache-busted iframe URL.

### 2026-07-28 15:12 HKT — Codex — Loaded the Content.docx introduction into the StoryMap website

Summary:
- Read `intro Website/Outline/Content.docx` as the source of truth for the visible introduction title, six subtitles, paragraphs, slash-separated breaks, and the 1.4 comparison table.
- Replaced the generic StoryMap copy with the DOCX introduction and created ten independent card-plus-backdrop parts: one for each subtitle, with 1.3 and 1.6 split at the supplied `/` markers.
- Kept the real sample review-tool embed as the backdrop for 1.5 and preserved the extracted Traditional Chinese wording.

Files:
- `intro Website/Website/storymap-example.html`
- `PROJECT_LOG.md`

Verified:
- The embedded script parsed successfully and `git diff --check` passed.
- Live browser inspection found 10 cards, 10 backdrops, the four table body rows, and the 1.5 review iframe with no browser errors or warnings.
- Checked the hero, 1.1 card, 1.4 table, and review-tool section visually; cards and backdrops fit their sections.

Remaining:
- None for the requested introduction-content load.

### 2026-07-28 15:12 HKT — Codex — Corrected the 1.4 table wording to match the DOCX

Summary:
- Changed the AI Skills row from「再由研究者核對、審核及修正」to the source wording「並由研究者核對、審核及修正」.

Files:
- `intro Website/Website/storymap-example.html`
- `PROJECT_LOG.md`

Verified:
- Rechecked the source table text and the website's embedded script; the source wording now matches.

Remaining:
- None.

### 2026-07-28 15:24 HKT — Codex — Added a folder-specific introduction website change log

Summary:
- Added `intro Website/INTRO_WEBSITE_CHANGE_LOG.md` to record every coherent
  change made inside the introduction website folder.
- Recorded the folder's pre-existing uncommitted files as a baseline without
  attributing or altering them.

Files:
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Confirmed the local log is directly inside `intro Website/` and contains the
  required author, summary, files, verification, and remaining-work fields.
- Confirmed the pre-existing uncommitted website-folder changes remain
  untouched.

Remaining:
- Keep the local log current after each coherent change in that folder.

### 2026-07-28 15:26 HKT — Codex — Added an AI working guide for the introduction website

Summary:
- Added `intro Website/README.md` with the website purpose, file map, source
  and language rules, review-tool embed instructions, local serving/testing
  workflow, and handoff requirements.
- Documented that `intro Website/INTRO_WEBSITE_CHANGE_LOG.md` must be updated
  after every coherent website-folder change.

Files:
- `intro Website/README.md`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Reviewed the current StoryMap and standalone embed implementation before
  writing the guide.
- Confirmed the documented paths, ports, and validation commands match the
  current project layout.

Remaining:
- Keep the README and both change logs current as the website evolves.

### 2026-07-28 15:26 HKT — Codex — Split the introduction website into separate HTML, CSS, and JavaScript files

Summary:
- Removed the large inline style and script blocks from both introduction website pages.
- Kept page structure in HTML and moved page-specific presentation and logic/data into separate files under `intro Website/Website/assets/`.

Files:
- `intro Website/Website/storymap-example.html`
- `intro Website/Website/review-tool-embed.html`
- `intro Website/Website/assets/storymap.css`
- `intro Website/Website/assets/storymap.js`
- `intro Website/Website/assets/review-tool-embed.css`
- `intro Website/Website/assets/review-tool-embed.js`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Both extracted JavaScript files pass `node --check`.
- Browser inspection confirmed the introduction cards/table and review embed render from the split files.
- Browser interaction confirmed quote highlighting still works; `git diff --check` passed.

Remaining:
- The separate review-tools server could not be started in the restricted shell, so the StoryMap iframe's server-backed route remains to be rechecked when that server is available.

### 2026-07-28 15:27 HKT — Codex — Added typography hierarchy examples

Summary:
- Added a standalone comparison page with three simple card treatments for the four text layers: subtitle, pretext, body, and clickable APA-like reference.
- Included a same-content comparison so the typographic differences are easy to evaluate before changing the main StoryMap cards.

Files:
- `intro Website/Website/typography-hierarchy-options.html`
- `PROJECT_LOG.md`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`

Verified:
- Confirmed the standalone HTML contains three options and three reference links targeting the example reference position.
- Browser inspection showed all three cards rendered side by side at desktop width; `git diff --check` passed.

Remaining:
- Choose one option before applying the hierarchy to the main introduction website.

### 2026-07-28 15:29 HKT — Codex — Added local AI agent rules for the introduction website

Summary:
- Added `intro Website/AGENT.md` with folder-specific rules derived from the
  parent project instructions.
- Documented the website architecture, source and research boundaries,
  review-tool isolation, validation, logging, handoff, and safety requirements.
- Added the new rules file to the introduction website README.

Files:
- `intro Website/AGENT.md`
- `intro Website/README.md`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Compared the local rules with `AGENTS.md` before writing them.
- Confirmed the documented paths, server ports, and validation commands match
  the current introduction website layout.
- Preserved the concurrent typography comparison change and its existing log
  entries.

Remaining:
- Keep the local rules, README, and both change logs current as the website
  evolves.

### 2026-07-28 15:34 HKT — Codex — Split the website into StoryMap and embedded-tool folders

Summary:
- Moved the StoryMap page and its CSS/JavaScript into `intro Website/Website/storymap/`.
- Moved the standalone embedded review tool and its CSS/JavaScript into `intro Website/Website/embedded-tool/`.
- Updated active page references, the file-mode iframe fallback path, README guidance, and agent instructions.

Files:
- `intro Website/Website/storymap/`
- `intro Website/Website/embedded-tool/`
- `intro Website/AGENT.md`
- `intro Website/README.md`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Confirmed active code and documentation no longer use the old mixed `Website/assets/` layout.
- Confirmed the nested StoryMap file-mode fallback points to the review-tools directory.

Remaining:
- A concurrent uncommitted `storymap.js` edit removes section 1.5, so the moved StoryMap iframe was not independently checked; that edit was preserved. The moved embedded-tool page passed browser verification.

### 2026-07-28 15:36 HKT — Codex — Applied Option C card hierarchy and inline reference

Summary:
- Applied the selected Option C typography to the introduction StoryMap cards,
  using Option A's 30px subtitle size.
- Moved the Dai citation into the 1.3 body immediately after
  `超過二萬七千頁。` and linked it to an anchored reference-page entry.
- Updated the standalone typography comparison page and preserved the requested
  omission of the 1.5 research-results section.

Files:
- `intro Website/Website/storymap/storymap.js`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/typography-hierarchy-options.html`
- `intro Website/Website/references.html`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Both website JavaScript files pass `node --check`.
- `git diff --check` passes.
- Confirmed the inline citation and reference anchor paths in the edited HTML
  and JavaScript. A fresh visual browser check was blocked for the local file
  page by the browser security policy.

Remaining:
- Review visual spacing in the normal local HTTP preview when available.

### 2026-07-28 15:50 HKT — Codex — Removed card number labels

Summary:
- Removed the orange number line above each introduction StoryMap subtitle,
  such as `1.3 / 01`.
- Removed the associated number styling and tightened the subtitle's top
  spacing.
- Restored the linked reference page after finding it deleted in the working
  tree, preserving the existing inline citation destination.

Files:
- `intro Website/Website/storymap/storymap.js`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/Website/references.html`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- `node --check intro Website/Website/storymap/storymap.js` passes.
- Confirmed the card renderer no longer outputs the number element.
- `git diff --check` passes.

Remaining:
- Review updated card spacing in the normal local HTTP preview when available.

### 2026-07-28 16:30 HKT — Codex — Restored the 1.5 research-results section

Summary:
- Restored `1.5 / 研究成果` between 1.4 and 1.6 with the exact three
  paragraphs supplied for the introduction.
- Reconnected the existing 硃83 sample review interface as the section's
  backdrop.
- Added 1.5 to the introduction workflow navigation and extended its route to
  1.6.

Files:
- `intro Website/Website/storymap/storymap.js`
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- `node --check intro Website/Website/storymap/storymap.js` passes.
- Confirmed the 1.5 card data, review iframe, navigation node, and section
  anchor are present.
- `git diff --check` passes.

Remaining:
- Review the restored section and embedded review interface in the normal
  local HTTP preview when available.

### 2026-07-28 15:37 HKT — Codex — Added the automatic checkpoint rule for the introduction website

Summary:
- Updated `intro Website/AGENT.md` to require an immediate local commit after
  every validated coherent non-log change.
- Clarified that log edits belong with the related change and must not create a
  separate log-only commit.

Files:
- `intro Website/AGENT.md`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Confirmed the rule distinguishes non-log changes from log-only edits,
  preserves unrelated concurrent work, and prohibits automatic pushing.

Remaining:
- Follow this checkpoint rule for subsequent introduction-website changes.

### 2026-07-28 15:54 HKT — Codex — Set whole-project commit scope for automatic checkpoints

Summary:
- Updated `intro Website/AGENT.md` so automatic checkpoints commit the entire
  DH Project repository rather than only files changed inside the introduction
  website folder.
- Specified `git add -A` from the repository root, with a status and secret
  check before staging.

Files:
- `intro Website/AGENT.md`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Confirmed the rule requires whole-repository staging and preserves the
  prohibition on automatic pushing and destructive operations.
- Inspected the current repository status before applying the scope change.

Remaining:
- Apply whole-repository staging for the checkpoint created by this change.

### 2026-07-28 16:07 HKT — Codex — Add StoryMap display settings

Summary:
- Added an unboxed gear settings button at the far right of the StoryMap top
  bar.
- Added persistent A−/A＋ font-size controls with a wide 55%–220% range,
  outside-click and Escape-to-close behavior, and disabled endpoint buttons.

Files:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/Website/storymap/storymap.js`

Verified:
- Confirmed the gear path matches the canonical project settings icon.
- Passed `node --check intro Website/Website/storymap/storymap.js` and
  `git diff --check`.
- Browser-verified the no-border button, panel toggle, 105% scaling, 55% and
  220% limits, reload persistence, and reset to 100%.

Remaining:
- None for this change.

### 2026-07-30 16:39 HKT — Codex — Preserve edited original text with stale divisions

Summary:
- Fixed the document-panel renderer in both formal and sample tools so an edited original body still renders when saved division boundaries are longer than the current text.
- Clamped division render ranges to the current body length, preventing the out-of-range highlight renderer error that hid 原文 for 硃22 after its body was edited.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`

Verified:
- Reproduced the failure in the sample 硃22 panel and identified the `buildRuns` out-of-range exception.
- Reloaded the sample tool and confirmed 硃22 shows 摘要, 原文, and all four divisions after the saved body was shortened from 798 to 788 characters.
- Reloaded the formal tool and confirmed 硃22 still shows 原文 and all four divisions.
- Passed `git diff --check`.

Remaining:
- None for this change.

### 2026-07-30 16:15 HKT — Codex — Refined the 第一部分 interface overview

Summary:
- Changed the proposed `第一部分` overview to one sample-tool replica with
  four clickable highlight areas and floating function labels.
- Kept detailed explanations for later cards so the overview can focus on
  spatial orientation and basic function recognition.

Files:
- `intro Website/Website/UI Idea/03-第一部分.md`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Passed `git diff --check`.

Remaining:
- Choose the implementation format for the replica.

### 2026-07-30 16:00 HKT — Codex — Refined research-result and case-study visuals

Summary:
- Updated the `引言` UI notes so `研究成果` uses a full-interface GIF.
- Assigned the three `林爽文事件` cards to the Qing war drawing, the
  Taiwan-to-Beijing information-route map, and the two source-book covers.

Files:
- `intro Website/Website/UI Idea/02-引言.md`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Passed `git diff --check`.

Remaining:
- Select and document the actual image assets before implementation.

### 2026-07-30 15:47 HKT — Codex — Added per-tab UI brainstorming notes

Summary:
- Created one markdown brainstorming file for each top-level introduction
  website tab.
- Captured the proposed interactive map for `引言`, including document stages,
  source images, the Taiwan-to-Beijing route, and the Forbidden City map.
- Split the three research-difficulty concepts into separate UI treatments.

Files:
- `intro Website/Website/UI Idea/01-主頁.md`
- `intro Website/Website/UI Idea/02-引言.md`
- `intro Website/Website/UI Idea/03-第一部分.md`
- `intro Website/Website/UI Idea/04-第二部分.md`
- `intro Website/Website/UI Idea/05-第三部分.md`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Confirmed the five notes correspond to the current top-level website tabs.
- Passed `git diff --check`.

Remaining:
- Select ideas for implementation after source-image and historical-framing
  review.

### 2026-07-30 15:15 HKT — Codex — Reformatted the independent StoryMap card-layout CSS

Summary: Reformatted all 49 StoryMap card rules into readable multi-line blocks with explanatory comments and blank lines between cards, without changing layout values.

Files:
- `intro Website/Website/storymap/storymap-cards.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`

Verified:
- Confirmed all 49 card blocks remain present.
- Passed `git diff --check`.

Remaining:
- None for this change.

### 2026-07-30 15:00 HKT — Codex — Added the shared StoryMap card-layout synchronization rule

Summary: Added a common project rule requiring every StoryMap card creation, edit, or subtitle/title change to update the matching labelled block in `intro Website/Website/storymap/storymap-cards.css`, including its Traditional Chinese identification comment.

Files:
- `AGENTS.md`
- `CLAUDE.md`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`

Verified:
- Confirmed `AGENTS.md` and `CLAUDE.md` are byte-for-byte identical.
- Passed `git diff --check`.

Remaining:
- None for this change.

### 2026-07-30 15:05 HKT — Codex — Remove oversized backdrop characters

Summary:
- Removed the large decorative Chinese character from every story-card backdrop while preserving the existing colors, imagery, and content.

Files:
- `intro Website/Website/storymap/storymap.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`

Verified:
- Passed `git diff --check`.

Remaining:
- None for this change.

### 2026-07-30 15:03 HKT — Codex — Simplify the intro workflow header

Summary:
- Renamed the workflow node 奏折上諭研究價值 to 研究價值.
- Removed the three numbered 研究難處 nodes from the intro workflow header while retaining the general 研究難處 section link.

Files:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Confirmed the old header label and all three numbered difficulty nodes are absent from the workflow markup.
- Passed `git diff --check`.

Remaining:
- None for this change.

### 2026-07-30 14:40 HKT — Codex — Added an independent StoryMap card-layout stylesheet

Summary: Added a separately labelled CSS block for every StoryMap card so card position, width, and section height can be manually adjusted without searching the page markup. Each block includes the card's Traditional Chinese subtitle/title for identification.

Files:
- `intro Website/Website/storymap/storymap-cards.css`
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`

Verified:
- Confirmed 49 StoryMap sections have 49 matching CSS layout blocks.
- Passed `git diff --check`.
- Browser-verified the first card at desktop width and at a 390px mobile width; desktop position/width and mobile stacked positioning both render as expected.

Remaining:
- None for this change.

### 2026-07-30 14:40 HKT — Codex — Remove the introductory cover tab

Summary:
- Removed the 引言 cover panel headed `從奏摺與上諭理解清代通信`, leaving the 引言 content cards and workflow navigation as the direct entry point.

Files:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`

Verified:
- Confirmed the removed heading and intro cover markup no longer appear in the page.
- Passed `git diff --check`.

Remaining:
- None for this change.

### 2026-07-30 14:36 HKT — Codex — Preserve the website’s original cover palette

Summary:
- Kept the competition cover’s spacing and hierarchy as the layout reference, but restored the introduction website’s deep-teal and restrained-coral background palette.

Files:
- `intro Website/Website/storymap/storymap.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`

Verified:
- Passed `git diff --check`.

Remaining:
- None for this change.

### 2026-07-30 14:31 HKT — Codex — Accent the start-reading button

Summary:
- Changed `開始閱讀` to the website’s coral-orange text and border, with a matching hover state.

Files:
- `intro Website/Website/storymap/storymap.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`

Verified:
- Passed `git diff --check`.

Remaining:
- None for this change.

### 2026-07-30 14:24 HKT — Codex — Build the cover-page competition links

Summary:
- Replaced the introduction website cover-page label with `2026 理大人工智能 X 數位人文獎・工具型作品示例`, enlarged the cover hierarchy, and added three square-cornered links: `比賽網站`, `下載工具代碼`, and `開始閱讀`.
- Linked the first two buttons to the supplied competition website and the project GitHub repository; the third switches to 引言.

Files:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/Website/storymap/storymap.js`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`

Verified:
- Passed `node --check intro Website/Website/storymap/storymap.js` and `git diff --check`.
- Browser-verified the labels, destinations, 1px white borders, square corners, and the `開始閱讀` switch to `#intro`.

Remaining:
- None for this change.

### 2026-07-30 14:29 HKT — Codex — Refine the cover competition label

Summary:
- Reduced the competition label size and changed it to the website’s coral-orange accent so the main platform title remains dominant.

Files:
- `intro Website/Website/storymap/storymap.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`

Verified:
- Passed `git diff --check`.

Remaining:
- None for this change.

### 2026-07-30 15:16 HKT — Codex — Fit the intro dropdown to its content

Summary:
- Reduced the intro workflow canvas to one content row instead of reserving unused branch rows.
- Kept the dropdown height content-driven, with its existing upper and lower padding providing the surrounding margins.

Files:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Confirmed the workflow canvas has a 54px content row and the dropdown has no fixed height.
- Passed `git diff --check`.

Remaining:
- None for this change.

### 2026-07-30 15:13 HKT — Codex — Center and equalize the intro workflow chain

Summary:
- Reflowed the six workflow buttons into consecutive centered columns.
- Equalized all five connector dashes and removed the unused gap caused by the former empty branch column.

Files:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Confirmed the workflow uses six consecutive columns and the SVG connector coordinates form five equal-length horizontal segments.
- Passed `git diff --check`.

Remaining:
- None for this change.

### 2026-07-30 15:11 HKT — Codex — Restore the straight intro workflow line

Summary:
- Restored the 研究難處 workflow button.
- Removed the unnecessary branch lines and connected 研究價值, 研究難處, and 數位方法 along one straight horizontal line.

Files:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Confirmed the 研究難處 button is present and the SVG contains only straight horizontal connectors for the main workflow.
- Passed `git diff --check`.

Remaining:
- None for this change.

### 2026-07-30 15:09 HKT — Codex — Remove the third intro workflow button

Summary:
- Removed the third workflow button, 研究難處, from the intro header.
- Preserved the connector line by joining it across the former button position to the existing branch and 數位方法 connector.

Files:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Confirmed the 研究難處 workflow button is absent and the SVG connector path remains continuous.
- Passed `git diff --check`.
- Browser visual refresh was not possible because the in-app browser blocks the local `file://` preview.

Remaining:
- None for this change.

### 2026-07-30 15:12 HKT — Codex — Preserve the workflow connector line

Summary:
- Kept the three numbered 研究難處 buttons removed from the intro workflow header.
- Extended the existing middle connector line across the empty branch area to 數位方法, while preserving the vertical branch line and upper/lower arms.

Files:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Confirmed the connector path remains in the SVG and reaches the 數位方法 connector.
- Passed `git diff --check`.

Remaining:
- None for this change.

### 2026-07-29 17:56 HKT — Codex — Added the 4. 收取上諭的資訊 cover bar

Summary:
- Applied the thin backdrop-and-large-text cover bar to `4. 收取上諭的資訊`.
- Kept its three detailed imperial-edict subsections in the content card below.

Files:
- `intro Website/Website/storymap/storymap.js`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Passed `node --check` for both website JavaScript files.
- Passed `git diff --check`.
- Confirmed `part-2-yu-info` now uses `coverBar: true` and the cover-bar card
  placement.

Remaining:
- Review cover-bar height and long-card spacing in the normal local HTTP
  preview when available.

### 2026-07-29 17:52 HKT — Codex — Loaded the expanded Part 2 DOCX content

Summary:
- Re-read the current `intro Website/Outline/Part 2.docx`, which had expanded
  to 64 non-empty source paragraphs.
- Replaced the abbreviated Part 2 data with the complete workflow, structured
  input, AI Skills, communication-pairing, event-extraction, source-tracing,
  imperial-edict, and visualization content.
- Added separate cards for detailed nested workflows so long sections are not
  hidden inside one overflowing card.
- Mapped every DOCX `(cover bar UI)` marker to the thin cover-bar renderer.

Files:
- `intro Website/Outline/Part 2.docx` (read-only source)
- `intro Website/Website/storymap/storymap.js`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Compared all 64 non-empty DOCX paragraphs against the website source; zero
  exact source strings are missing.
- Passed `node --check` for both website JavaScript files.
- Passed `git diff --check`.

Remaining:
- Review the complete Part 2 sequence and long-card spacing in the normal local
  HTTP preview when available.

### 2026-07-29 17:45 HKT — Codex — Added thin cover bars to selected Part 2 sections

Summary:
- Applied the thin, non-full-screen cover-bar treatment to `1. 平台的運作流程`
  and `3. 運作流程圖`.
- Added backdrop-backed large title text while keeping detailed content in the
  readable card layer below.
- Left `4. 輸入結構化資料` and `5. 使用AI從原文中抽取資訊` as detailed card
  layouts.

Files:
- `intro Website/Website/storymap/storymap.js`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Passed `node --check` for both website JavaScript files.
- Passed `git diff --check`.
- Confirmed only the two selected Part 2 sections receive the `cover-bar`
  renderer and styling.

Remaining:
- Review cover-bar height, backdrop contrast, and card placement in the normal
  local HTTP preview when available.

### 2026-07-28 20:11 HKT — Codex — Loaded Part 2.docx into the website

Summary:
- Read `intro Website/Outline/Part 2.docx` and preserved its operating-process
  content and nested AI-analysis headings.
- Replaced the Part 2 placeholder hero with `1. 平台的運作流程` and its
  introductory statement.
- Added four independent card-and-backdrop sections for the overall process,
  workflow diagram, structured-data input, and AI extraction.
- Kept the three AI subsections inside the AI-extraction card.

Files:
- `intro Website/Outline/Part 2.docx` (read-only source)
- `intro Website/Website/storymap/storymap.js`
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Rendered the DOCX to two page images and inspected both pages.
- Extracted and checked the DOCX paragraph text with the bundled document
  runtime.
- Passed `node --check` for both website JavaScript files and `git diff --check`.

Remaining:
- Review Part 2 in the normal local HTTP preview when available.

### 2026-07-28 18:45 HKT — Codex — Loaded Part 1.docx into the website

Summary:
- Read `intro Website/Outline/Part 1.docx` and preserved its platform-overview
  text and six interface subsections.
- Replaced the Part 1 placeholder hero with `1. 平台的整體介面` and its
  introductory paragraph.
- Added independent card-and-backdrop sections for the four platform areas,
  導覽列, 時間與關係圖表, 節點資訊區, 原始史料區, and 人工智能分析區.
- Added subsection headings inside the relevant cards to retain the DOCX
  hierarchy.

Files:
- `intro Website/Outline/Part 1.docx` (read-only source)
- `intro Website/Website/storymap/storymap.js`
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Rendered the DOCX to two page images and inspected both pages.
- Extracted and checked the DOCX paragraph text with the bundled document
  runtime.
- Passed `node --check` for both website JavaScript files and `git diff --check`.

Remaining:
- Review Part 1 in the normal local HTTP preview when available.

### 2026-07-28 16:34 HKT — Codex — Rebuild 引言 workflow as full-width horizontal chart

Summary:
- Reworked the 引言 workflow into a full-width translucent deep-teal panel
  beneath the top bar.
- Replaced the previous route with a horizontal sequence: 清代奏折上諭、奏折
  上諭研究價值、three separate 研究困難 bubbles, 數位方法, and 案例：林爽文事件.
- Added white connector lines and text, coral difficulty labeling, and hover,
  focus, and selected-bubble states.

Files:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/Website/storymap/storymap.js`

Verified:
- Passed `node --check intro Website/Website/storymap/storymap.js` and
  `git diff --check`.
- Browser-verified the full-width panel geometry, deep translucent styling,
  seven horizontal workflow nodes, connector path, and direct section targets.

Remaining:
- None for this change.

### 2026-07-28 16:25 HKT — Codex — Redesign 引言 submenu as workflow map

Summary:
- Replaced the plain vertical 引言 submenu with a paper-toned workflow
  window containing five subtitle bubbles connected by a routed line.
- Kept each bubble as a direct link to its corresponding introduction section,
  with hover/focus motion and coral-accent interaction states.

Files:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/Website/storymap/storymap.js`

Verified:
- Passed `node --check intro Website/Website/storymap/storymap.js` and
  `git diff --check`.
- Browser-verified the five workflow nodes, their section links, chart layout,
  connector path, and themed submenu dimensions.

Remaining:
- None for this change.

### 2026-07-28 16:11 HKT — Codex — Center top-bar navigation

Summary:
- Centered the section buttons as a group in the desktop top bar while
  keeping the settings button as the only right-aligned control.
- Preserved the existing compact mobile top-bar behavior.

Files:
- `intro Website/Website/storymap/storymap.css`

Verified:
- Passed `node --check intro Website/Website/storymap/storymap.js` and
  `git diff --check`.
- Browser-verified that the navigation group is centered at 1280px and the
  settings control remains aligned to the right edge.

Remaining:
- None for this change.

### 2026-07-28 16:43 HKT — Codex — Refine 引言 flowchart branch layout

Summary:
- Removed all extra dropdown headings and step-number labels.
- Rebuilt the chart to match the requested algorithm-style flow: two left
  nodes, a three-way vertical 研究困難 branch, then 數位方法 and 案例：林爽文事件.
- Changed the bubbles to transparent ellipses with white outlines/text and
  coral hover, focus, and selected states.

Files:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.css`

Verified:
- Passed `node --check intro Website/Website/storymap/storymap.js` and
  `git diff --check`.
- Browser-verified seven bubbles, no extra menu text, white text styling,
  elliptical borders, and branch connector geometry.

Remaining:
- None for this change.

### 2026-07-28 16:49 HKT — Codex — Compress workflow bubbles and preserve hover area

Summary:
- Reduced the workflow canvas and ellipse height so the dropdown occupies much
  less vertical space.
- Kept the full-width chart and branch geometry intact.
- Changed dropdown closing to wait until the pointer has left both the 引言
  trigger and the full workflow panel.

Files:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/Website/storymap/storymap.js`

Verified:
- Passed `node --check intro Website/Website/storymap/storymap.js` and
  `git diff --check`.
- Browser-verified 54px bubbles, a 220px chart canvas, and the fixed full-width
  panel position.

Remaining:
- None for this change.

### 2026-07-28 16:49 HKT — Codex — Split the introduction website into independent top-level tabs

Summary:
- Changed the introduction website from one continuous list into independent
  主頁, 引言, 第一部分, and 第二部分 views.
- Added reduced-height cover-style mastheads to the non-cover views and kept
  the existing introduction cards inside 引言.

Files:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/Website/storymap/storymap.js`

Verified:
- Passed `node --check intro Website/Website/storymap/storymap.js` and
  `git diff --check`.
- Browser-verified independent panel visibility, active tab highlighting,
  compact masthead height, and direct introduction deep links.

Remaining:
- 第一部分 and 第二部分 have mastheads only until their substantive content
  is supplied.

### 2026-07-28 16:59 HKT — Codex — Extend 引言 flow with research difficulty and results

Summary:
- Removed the orange active underline from the top navigation.
- Added 研究難處 before the three difficulty bubbles and 研究成果 after
  數位方法, preserving the horizontal branch flow.
- Kept the compact ellipse bubbles and white connector styling.

Files:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.css`

Verified:
- Passed `node --check intro Website/Website/storymap/storymap.js` and
  `git diff --check`.
- Browser-verified nine bubbles, three branch rows, 54px bubble height, the
  220px chart canvas, and no active underline pseudo-element.

Remaining:
- None for this change.

### 2026-07-28 17:11 HKT — Codex — Change workflow bubbles to thin-border rectangles

Summary:
- Replaced the ellipse bubbles with compact, lightly rounded rectangular
  bubbles using a 1px white border and restrained shadow.

Files:
- `intro Website/Website/storymap/storymap.css`

Verified:
- Passed `node --check intro Website/Website/storymap/storymap.js` and
  `git diff --check`.
- Browser-verified 1px border, 8px corner radius, and compact 54px node height.

Remaining:
- None for this change.

### 2026-07-28 17:15 HKT — Codex — Remove workflow bubble corner rounding

Summary:
- Set the workflow rectangles to square corners with no border radius.

Files:
- `intro Website/Website/storymap/storymap.css`

Verified:
- Passed `node --check intro Website/Website/storymap/storymap.js` and
  `git diff --check`.
- Browser-verified `border-radius: 0px`, a 1px border, and 54px height.

Remaining:
- None for this change.

### 2026-07-28 17:17 HKT — Codex — Narrow workflow rectangles

Summary:
- Reduced the horizontal width of each workflow rectangle while preserving
  square corners, thin borders, and the existing flow layout.

Files:
- `intro Website/Website/storymap/storymap.css`

Verified:
- Passed `node --check intro Website/Website/storymap/storymap.js` and
  `git diff --check`.
- Browser-verified 137px rendered width at the current desktop viewport,
  54px height, 1px border, and zero corner radius.

Remaining:
- None for this change.

### 2026-07-30 03:47 HKT — Codex — Load complete Part 3 DOCX content

Summary:
- Added a new `第三部分` panel to the intro website and loaded the complete content from `intro Website/Outline/Part 3.docx`.
- Preserved the source hierarchy as independent cards, including thin cover bars for the three marked sections.

Files:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.js`
- `intro Website/Website/storymap/storymap.css`

Verified:
- Rendered and visually inspected all 5 pages of `intro Website/Outline/Part 3.docx`.
- Passed `node --check intro Website/Website/storymap/storymap.js`.
- Exact-string coverage found all 69 non-empty Part 3 source paragraphs in the website; the three DOCX cover markers are represented as UI cover bars.

Remaining:
- The in-app browser blocked reloading the local `file://` preview, so live visual refresh remains to be checked through the normal local HTTP preview.

### 2026-07-30 14:10 HKT — Codex — Simplify cover page backdrop

Summary:
- Removed the `SCROLL TO EXPLORE` prompt from the cover page.
- Removed the decorative 奏・摺・諭 text from the cover backdrop.

Files:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.css`

Verified:
- Passed `node --check intro Website/Website/storymap/storymap.js` and
  `git diff --check`.
- Confirmed neither cover decoration remains in the HTML or CSS.

Remaining:
- None for this change.

### 2026-07-30 14:12 HKT — Codex — Show settings on hover and rename font control

Summary:
- Made the introduction website settings dropdown open on hover over the gear.
- Renamed its font-control wording from 字級 to 字體 while preserving click,
  focus, and Escape behavior.

Files:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/Website/storymap/storymap.js`

Verified:
- Passed `node --check intro Website/Website/storymap/storymap.js` and
  `git diff --check`.
- Browser-verified the gear opens the panel and the panel shows 字體.

Remaining:
- None for this change.

### 2026-07-30 14:13 HKT — Codex — Move StoryMap content into HTML

Summary:
- Moved the authored StoryMap card text, headings, notes, citations, tables, cover bars, and backdrop labels from JavaScript data arrays into static HTML.
- Reduced the StoryMap JavaScript to interaction and presentation behavior while preserving the existing navigation and card hierarchy.

Files:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.js`

Verified:
- Passed HTML parsing, `node --check intro Website/Website/storymap/storymap.js`, and `git diff --check`.
- Exact-string coverage remains complete for Part 2 (64/64) and Part 3 (69/69) source paragraphs.
- Browser-verified the HTTP preview at `#part-3`, including the Third Part navigation link, headings, paragraphs, and thin cover-bar sections.

Remaining:
- None for this change.

### 2026-07-30 17:05 HKT — Codex — Mark Taiwan-war report routes on the visual reference map

Summary:
- Created a marked copy of the 賴福順 route-map PDF for the introduction website, distinguishing the main mainland-to-Taiwan report route from the auxiliary 江西–潮州 route.
- Preserved the original source PDF and recorded that the marked page is 圖十二, while the Taiwan-war text refers to 圖十三 for the precise route figure.

Files:
- `intro Website/Website/Visual Material/情報路線/2乾隆重要戰爭之軍需硏究. 賴福順. 國立故宮博物院, 1984 (dragged) - marked Taiwan routes.pdf`

Verified:
- Rendered and visually inspected the marked PDF; Traditional Chinese annotation labels display correctly.

Remaining:
- Verify 圖十三 before using the marked route as precise historical cartography.

### 2026-07-30 — Codex — Created a clear 硃40—諭24 demonstration data set

Summary: Added a self-contained data set under `intro Website/Website/Clear Data`
for a reduced timeline demonstration. It keeps 10 硃40 event dots, 13 諭24
emperor-action dots, their retained AI output data, only the two relevant source
documents, and the requested 諭24-to-硃40 demonstration response connection.

Files:
- `intro Website/Website/Clear Data/clear-demo.data`
- `intro Website/Website/Clear Data/source-documents.json`
- `intro Website/Website/Clear Data/confirmed-pairs.json`
- `intro Website/Website/Clear Data/README.md`
- `intro Website/Website/Clear Data/build_clear_demo.py`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`

Verified:
- All JSON files parse successfully; the builder compiles.
- The overlay contains 23 events and no event source outside 硃40 or 諭24.
- Every retained 諭24 emperor action has structured AI detail and source data.
- The response pair is explicitly marked demonstration-only and canonical
  formal/sample state was not changed.

Remaining:
- Import and visually check the clear overlay in the sample review page if an
  interactive presentation is required.

### 2026-07-30 — Codex — Consolidated the clear demonstration into one export JSON

Summary: Combined the clear demonstration overlay, the complete 硃40 and 諭24
source records, and the requested demonstration pair into one export-style
JSON file. Removed the redundant companion JSON files.

Files:
- `intro Website/Website/Clear Data/clear-demo.data`
- `intro Website/Website/Clear Data/README.md`
- `intro Website/Website/Clear Data/build_clear_demo.py`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`

Verified:
- The single JSON file parses successfully and includes both source documents
  under `__sourceDocuments` and the response connection under `__docPairs`.
- The 10 硃40 event dots and 13 諭24 emperor-action dots remain unchanged.
- The formal and sample canonical states were not modified by this change.

Remaining:
- Import and visually check the single export JSON in the sample review page if
  an interactive presentation is required.

### 2026-07-30 — Codex — Keep all dots visible with a two-document interaction allowlist

Summary: Updated `intro Website/Website/Clear Data/clear-demo.data` to retain all
225 existing event and emperor-action dots. Added `__clearDemo` metadata that
separates the selected 硃40 and 諭24 event IDs and marks only those two document
dots as clickable for future code; all other document dots remain visible. The
single 諭24-to-硃40 demonstration pair and selected AI output cards remain.

Files:
- `intro Website/Website/Clear Data/clear-demo.data`
- `intro Website/Website/Clear Data/README.md`
- `intro Website/Website/Clear Data/build_clear_demo.py`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`

Verified:
- No `__hidden` overlay is present; the allowlist is exactly 硃40 and 諭24.
- Confirmed 225 total event/action dots, 10 selected 硃40 events, 13 selected
  諭24 emperor actions, and 10/9 selected AI output cards.
- JSON parsing and `git diff --check` passed.

Remaining:
- Add the runtime click guard to the review page when the interaction behavior
  is ready to be implemented.

### 2026-07-30 17:56 HKT — Codex — Preserve the Preview-drawn Taiwan route as an HTML line layer

Summary:
- Converted the researcher’s four red Preview route annotations into one reusable SVG path for future HTML animation.
- Kept the source PDF’s hand-drawn annotations and added optional draw-on animation plus reduced-motion handling in the SVG layer.

Files:
- `intro Website/Website/storymap/taiwan-war-report-route.svg`
- `intro Website/Website/Visual Material/情報路線/2乾隆重要戰爭之軍需硏究. 賴福順. 國立故宮博物院, 1984 (dragged).pdf`

Verified:
- SVG parsing passed; all route coordinates remain within the map viewBox.
- Confirmed the four Preview annotation segments were joined in the correct visual order.

Remaining:
- Insert the SVG path into the StoryMap map container when the HTML interaction is implemented.

### 2026-07-30 18:27 HKT — Codex — Add the map backdrop and location pins to the first two intro cards

Summary: Rendered the supplied `Fizzy Background.pdf` crop box as a web-ready PNG,
used it as the backdrop for the first two StoryMap intro cards, and added separate
SVG pin layers marking Beijing and Taiwan at the existing route endpoints. The pin
layer remains independent from the future animated route SVG.

Files:
- `intro Website/Website/storymap/fizzy-background.png`
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/Website/Visual Material/情報路線/Fizzy Background.pdf`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`

Verified: The PNG is 2106 × 1489 and matches the map's A4 crop-box ratio; both cards
contain two red pins at the Beijing and Taiwan route endpoint coordinates; `node --check`
and `git diff --check` passed. Browser visual validation was unavailable because the
local preview address was rejected by the browser security policy.

Remaining: Add the standalone route SVG as an HTML layer when the line animation
interaction is ready.

### 2026-07-30 18:36 HKT — Codex — Keep non-Yu click focus on the clicked Zhu's Yu relationship

Summary: Changed both review tools so clicking a non-Yu document keeps only its
directly paired Yu/document endpoints and the clicked document's own event/action
evidence. A shared Yu no longer causes all sibling Zhu pair lines, green
`yu_source` rings, or unrelated sibling emperor actions to be highlighted. Clicking
the Yu itself retains its existing expansion to all directly paired Zhu documents.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- All inline JavaScript blocks parsed in both HTML files.
- Focused-pair assertions passed in both renderers.
- `git diff --check` passed.

Remaining:
- Human browser confirmation with one Yu paired to multiple Zhu documents.

### 2026-07-30 18:36 HKT — Codex — Replace map spots with interactive Google-style pins

Summary: Replaced the oversized red polygon spots in both first StoryMap cards
with compact red teardrop pins and white centers. Added hover and keyboard-focus
information popovers for 北京 and 臺灣（鹿仔港／鹿耳門）. The pin geometry remains
in the shared map SVG coordinate system for future route animation.

Files:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`

Verified: Four pins, four accessible labels, and four hover popovers are present
across the two cards. `node --check` and `git diff --check` passed.

Remaining: Browser visual validation and the route-line animation remain pending
because the local preview address is blocked by the browser security policy.

### 2026-07-30 19:13 HKT — Codex — Build the Taiwan-to-Beijing interactive route map

Summary: Applied the same `Fizzy Background.pdf`-derived map backdrop to the first
two cards and built a Taiwan-first click sequence. Taiwan starts alone; clicking
it opens a three-page gallery, draws the supplied route from Taiwan to Beijing in
one second, and then reveals Beijing with its information window. Reaching the
third gallery page replays the route animation. The supplied route SVG is loaded at
runtime and its point sequence is reversed for the requested direction.

Files:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.js`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/Website/storymap/taiwan-route-source-page.png`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`

Verified: The route source has 4,261 points; the reversed sequence begins at the
Taiwan endpoint `(730.24, 510.39)` and ends at Beijing `(627.41, 207.15)`. Both
cards contain the route map and gallery structure, all referenced assets resolve,
and `node --check` plus `git diff --check` passed. Browser visual validation
remains unavailable because the local preview address is blocked by the browser
security policy.

Remaining: Perform a human browser pass when the local preview can be opened,
especially checking the information-window position at the smallest mobile width.

### 2026-07-30 19:47 HKT — Codex — Make the supplied route SVG work in local preview and update the first card text

Summary: Replaced the `fetch()`-dependent route loader with a native embedded
object using the supplied `Visual Material/情報路線/taiwan-war-report-route.svg`.
The embedded path is reversed at activation time and animated from Taiwan to
Beijing over one second. Replaced the first card's previous explanatory prose
with the four supplied chronological paragraphs about 柴大紀、乾隆帝硃批、軍機處
登記 and the廷寄諭旨.

Files:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.js`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`

Verified: Both map instances directly reference the supplied route SVG through
`route-line-object`; StoryMap and embedded-tool JavaScript syntax checks and
`git diff --check` passed.

Remaining: Perform a human browser pass to confirm the embedded SVG's
`contentDocument` is accessible in the user's local preview browser.

### 2026-07-30 19:56 HKT — Codex — Remove file-preview route and review-tool cross-origin failures

Summary: Generated `taiwan-war-report-route-reverse.svg` from the supplied route
SVG by reversing its 4,261-point path sequence. The map now loads this local
reverse derivative directly, with its own one-second draw animation, so it does
not access an embedded document. The review iframe now uses the existing local
HTTP review server on port 8766 even when the StoryMap itself is opened as a file.

Files:
- `intro Website/Website/storymap/taiwan-war-report-route-reverse.svg`
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.js`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`

Verified: The reverse route starts at Taiwan `(730.24, 510.39)` and ends at
Beijing `(627.41, 207.15)` with 4,261 points. StoryMap JavaScript no longer uses
`fetch()` or `contentDocument` for the route. Both JavaScript syntax checks and
`git diff --check` passed.

Remaining: Open the StoryMap through the local HTTP workflow and confirm the
review server is running on port 8766.

### 2026-07-30 20:05 HKT — Codex — Move route gallery to Beijing and repair bidirectional playback

Summary: Replaced the old Taiwan three-page popup with a concise Taiwan
starting-point information card, moved the three-page image gallery to the
Beijing popup, and added separate SVG route layers for the outbound Taiwan →
Beijing animation and the return Beijing → Taiwan replay after page 3. The
route loader no longer depends on an embedded-object load event, removing the
failure that prevented the Beijing reveal in the preview.

Files:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.js`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`

Verified: `node --check "Website/storymap/storymap.js"` and `git diff --check`
passed. Both route-map instances contain the Taiwan information card, hidden
Beijing pin, Beijing three-page gallery, and two direction-specific SVG layers.

Remaining: The in-app browser blocked localhost inspection in this turn; reopen
the local preview and test Taiwan click → Beijing reveal → gallery page 3 →
return animation.

### 2026-07-30 20:20 HKT — Codex — Bring route pins above the map popups

Summary: Raised the interactive route layer above the StoryMap card stacking
layer and raised the pin SVG above both information windows, so the Taiwan and
Beijing pins remain visible while their cards are open. The line layer remains
behind the information windows and pins.

Files:
- `intro Website/Website/storymap/storymap.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`

Verified: `git diff --check` passed. The route layer is z-index 5, the pin SVG
is z-index 4, and the information windows remain z-index 3 within the route
layer.

Remaining: Reload the local preview and confirm both red pins remain visible at
Beijing and Taiwan while the Beijing gallery is on any of its three pages.

### 2026-07-30 20:23 HKT — Codex — Use supplied route narrative and reveal the SVG Beijing pin

Summary: Replaced the Beijing gallery copy with the three supplied passages
about relay-station delivery, military-office registration, and the imperial
edict sent to 柴大紀. The red outbound route remains visible after appearing;
the return layer replays without first removing the already-visible red line.
Fixed the Beijing marker reveal by removing the SVG `<g>` element's `hidden`
attribute directly instead of assigning an unsupported SVG `hidden` property.

Files:
- `intro Website/Website/storymap/storymap.js`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`

Verified: `node --check "Website/storymap/storymap.js"` and `git diff --check`
passed. All three gallery strings match the supplied Traditional Chinese text.

Remaining: Hard-refresh the local preview and click the Taiwan pin once; the
Beijing pin should appear after the one-second route animation, with the three
supplied passages available through its gallery.

### 2026-07-30 20:44 HKT — Codex — Add source image and reference link to the research-difficulty card

Summary: Changed `intro-1-3-a` to use `Visual Material/img2_4_2.jpg` as its full
backdrop. Added a compact upper-corner `參考來源 ↗` button linking to the
supplied National Palace Museum page, with the complete citation in its
accessible title. Updated the card paragraph to refer directly to
《欽定剿平三省邪匪方略》 and removed the stale 戴英從 citation from this card.

Files:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`

Verified: `node --check "intro Website/Website/storymap/storymap.js"` and
`git diff --check` passed. The image path and supplied external reference URL
are present in the section.

Remaining: Hard-refresh the local preview and open 引言 → 3. 研究清代奏折的主要困難
to check the image crop and corner-button contrast.

### 2026-07-30 20:46 HKT — Codex — Add the 林爽文 demonstration-case artwork and source link

Summary: Updated `intro-1-6-a` with the supplied introductory sentence,
`為展示本網站的研究方法及各項功能。`, replaced its backdrop with
`Visual Material/印版平定台湾战图册6.png`, and added the same upper-corner
`參考來源 ↗` treatment linking to the supplied 國家文化記憶庫 record for
〈平定臺灣戰圖（七）生擒逆首林爽文〉.

Files:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`

Verified: `node --check "intro Website/Website/storymap/storymap.js"` and
`git diff --check` passed. The supplied image path, sentence, and source URL
are present in `intro-1-6-a`.

Remaining: Hard-refresh the local preview and open 引言 → 案例：林爽文事件
to check the artwork crop and reference-button contrast.

### 2026-07-30 20:49 HKT — Codex — Add the route map to the information-delay case card

Summary: Updated `intro-1-6-b` to use the `Fizzy Background` map backdrop and
the full red Taiwan-to-Beijing route line. Kept the requested text,
`第一，資訊傳遞是戰時軍事決策形成的重要環節。`, and added a corner
`參考來源 ↗` link to the local PDF for 賴福順《乾隆重要戰爭之軍需研究》（1984）.
The card remains a focused introduction so the map and route are the main
visual evidence for the information-delay point.

Files:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`

Verified: `node --check "intro Website/Website/storymap/storymap.js"` and
`git diff --check` passed. The static route uses
`taiwan-war-report-route-reverse.svg`, and the reference link targets the exact
local source PDF.

Remaining: Hard-refresh the local preview and open 引言 → 案例：林爽文事件 →
the first reason card to check the red-line crop and PDF button.

### 2026-07-30 20:59 HKT — Codex — Add the 諭24／硃110 second-level communication comparison

Summary: Reworked `intro-1-3-b` for the requested second layer of communication,
with the supplied explanation about 乾隆帝's 1月2日上諭 and 常青's 13日後
回奏. Added two side-by-side embedded sample review-tool panels, 諭24 on the
left and 硃110 on the right. Added sample-only URL highlight support so each
panel marks exact source wording corresponding to the summarized commands and
response, and moved the StoryMap card below the comparison panels.

Files:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/Website/storymap/storymap-cards.css`
- `review-tools/(2) sample/index.html` (sample-only embed behavior explicitly requested)
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`

Verified: `node --check "intro Website/Website/storymap/storymap.js"` and
`git diff --check` passed. Canonical source records for 諭24 and 硃110 were
checked before selecting exact highlight spans.

Remaining: Hard-refresh the local preview and open `#intro-1-3-b` to confirm both
review panels load from port 8766 and the highlighted passages are visible. The
review service was not running during this check and could not be started from
the restricted session; keep the normal review server running on port 8766 for
the embedded panels.

### 2026-07-30 21:06 HKT — Codex — Add the 硃119 source-network evidence panel

Summary: Reworked `intro-1-3-c` for the requested “事件、消息來源與資訊網絡”
example. Added one embedded sample review-tool panel for 硃119, labelled
`同日｜常青亦奏報臺灣軍情與四名消息來源`, with exact-source highlights for the
four passages concerning 廈門蚶江員弁、署守備陳邦光、易連／王增錞, and
廈門同知劉嘉會. Added a three-column evidence table for source, report content,
and quotation, and corrected the duplicated “的” in the explanatory paragraph.

Files:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/Website/storymap/storymap-cards.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`

Verified: `node --check "intro Website/Website/storymap/storymap.js"`, inline
sample-script parsing, and `git diff --check` passed. The canonical 硃119 record
was checked before selecting exact highlight spans.

Remaining: Hard-refresh the local preview and open `#intro-1-3-c` with the review
server running on port 8766 to check the highlighted passages and table layout.

### 2026-07-31 15:11 HKT — Codex — Restore omitted introduction prose in separate source cards

Summary: Restored the omitted `Outline/Content.docx` introduction prose in
independent source-text cards, while preserving the newer visual/demo cards and
their backdrops. Added three 1.1 source cards, the missing 1.3 source
paragraphs, and the missing 1.6 case-introduction and first-reason paragraphs.
Restored the inline Dai citation immediately after `超過二萬七千頁`, linked to
the existing reference entry.

Files:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap-cards.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`

Verified: Bundled JavaScript syntax checks and `git diff --check` passed. The
browser HTTP preview confirmed 17 intro sections/cards, no empty cards, no card
overflow, and the inline reference link targets
`../references.html#ref-dai-2019`.

Remaining: Review the new source-card backdrop positioning at the preferred
browser width; the embedded review panels still require the separate port-8766
server for their content.

### 2026-07-31 15:11 HKT — Codex — Replace StoryMap sample iframes with local review-panel replicas

Summary: Replaced the StoryMap's embedded review-tool iframes for 硃83,
諭24／硃110, and 硃119 with local HTML/CSS mock review windows. Recreated the
document header, metadata, tab strip, scrollable original-text area, and static
evidence highlights. The standalone sample review tool remains unchanged.

Files:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/Website/storymap/storymap.js`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`

Verified: `node --check "intro Website/Website/storymap/storymap.js"` and
`git diff --check` passed. No `iframe`, `8766`, or `setReviewFrameSource`
reference remains under `intro Website/Website/storymap/`.

Remaining: Hard-refresh the local preview and visually check the three mock
panels at `#intro-1-3-b`, `#intro-1-3-c`, and `#intro-1-5`. The in-app browser's
local-page security policy prevented live visual inspection in this session.

### 2026-07-31 15:26 HKT — Codex — Rebuild the 諭24／硃110 StoryMap panels from sample-tool UI and canonical records

Summary: Replaced the abbreviated comparison mockups with panels following the
sample review tool's document-card anatomy: document header, metadata table,
controls, tab strip, scrollable original-text pane, and highlighted evidence.
Embedded the complete canonical source bodies for 諭24 and 硃110 from
`review-tools/shared data/stage1_original_text.json`, corrected the metadata to
the source records' dates, and added local tab switching for 原文、AI 摘要、關係.

Files:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/Website/storymap/storymap.js`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`

Verified: `node --check "intro Website/Website/storymap/storymap.js"` and
`git diff --check` passed. Canonical body prefixes and all requested highlight
phrases for 諭24 and 硃110 are present.

Remaining: Hard-refresh the local preview and compare the panels against the
supplied sample-tool screenshot at `#intro-1-3-b`. Live browser inspection
remains blocked by the local-page security policy in this session.

### 2026-07-31 15:48 HKT — Codex — Match the StoryMap comparison panels to the sample review-tool document UI

Summary: Rebuilt the 諭24／硃110 replicas around the sample review tool's actual
document-card anatomy: ghost move/minimize/close controls, centered header resize
grip, type badge, compact metadata rows, filter/settings strip, and scrollable
原文 pane. Kept the complete canonical source bodies and requested evidence
highlights, and added local minimize, close, filter, and settings affordances.

Files:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/Website/storymap/storymap.js`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`

Verified: `node --check "intro Website/Website/storymap/storymap.js"`, HTML
nesting validation, and `git diff --check` passed. Both sample panels are
present and no StoryMap iframe/8766 references remain.

Remaining: Hard-refresh the local preview and compare `#intro-1-3-b` against the
supplied sample screenshot; live browser inspection remains blocked by the
local-page security policy.

### 2026-07-31 16:00 HKT — Codex — Consolidate source card text and remove duplicate intro copy

Summary: Removed the four route/demo paragraphs from the `清代奏折制度` visual
card; combined the three `原文補回` source cards into one; removed the specified
1.3-b paragraphs, the 1.3-c 同日奏報 sentence, and its source-network table;
removed the short duplicate `示範案例：林爽文事件` card while keeping the longer
case-background card and updated the workflow link.

Files: `intro Website/Website/storymap/storymap-example.html`,
`intro Website/Website/storymap/storymap-cards.css`,
`intro Website/INTRO_WEBSITE_CHANGE_LOG.md`.

Verified: Bundled Node syntax checks and `git diff --check` passed. Live preview
contains 14 intro sections; the requested removed phrases and table are absent,
the combined source card has three paragraphs, the longer case card remains, and
no card has internal overflow.

Remaining: Review the updated intro card spacing during the next visual pass.

### 2026-07-31 16:32 HKT — Codex — Add standalone UI upgrade options prototype

Summary: Added `intro Website/Website/UI Idea/06-UI-upgrade-options.html` as a
self-contained comparison page for three UI directions: 展示優先、左右分欄、研究
工作臺. Each option uses a hand-built review-tool mock panel with a separate
long-text reading area. Restored the temporary iframe experiment in `intro-1-5`
to the existing mock panel and preserved the current StoryMap content.

Files: `intro Website/Website/UI Idea/06-UI-upgrade-options.html`,
`intro Website/Website/storymap/storymap-example.html`,
`intro Website/Website/storymap/storymap.css`,
`intro Website/Website/storymap/storymap.js`,
`intro Website/Website/storymap/storymap-cards.css`, and
`intro Website/INTRO_WEBSITE_CHANGE_LOG.md`.

Verified: `node --check "intro Website/Website/storymap/storymap.js"`,
`git diff --check`, and local browser preview with three option sections, three
mock panels, and zero `<iframe>` elements in the new page.

Remaining: Choose one direction for the next implementation pass; the current
page is a visual comparison prototype only.

### 2026-07-31 16:51 HKT — Codex — Refine the standalone UI options page

Summary: Updated only `intro Website/Website/UI Idea/06-UI-upgrade-options.html`.
Made its opening cover viewport-height, converted each option heading into a
compact full-width cover block, removed pill-style labels, kept desktop option
subtitles on one line, and moved each explanatory paragraph below its subtitle.
Simplified Option 02 by removing `Text zone / 02`, the numbered reading index,
and the `版面重點` sub-card while retaining its subtitle, sub-subtitle, and point
list. No other HTML file was edited for this adjustment.

Files: `intro Website/Website/UI Idea/06-UI-upgrade-options.html` and
`intro Website/INTRO_WEBSITE_CHANGE_LOG.md`.

Verified: `git diff --check` passed. Local browser preview confirmed the
viewport-height opening cover, compact Option 02 cover, one-line desktop
subtitle, three mock panels, zero `<iframe>` elements, and no pill
selectors/text remnants.

Remaining: Choose one of the three refined layout directions for implementation
in the main intro website.

### 2026-07-31 17:07 HKT — Codex — Polish the standalone options page workflow presentation

Summary: Updated only `intro Website/Website/UI Idea/06-UI-upgrade-options.html`;
no other HTML file was edited. Removed the dark option-subtitle backdrop and the
outer backdrop around the hand-built review-tool panels, reduced body/stage
spacing, and changed the frozen option row into a normal in-page navigation row.
Each option tab now reveals a branching workflow preview on hover or keyboard
focus. Added polished workflow structures for 展示優先、左右分欄、研究工作臺 and
比較 with alternate routes, decision branches, and return loops inspired by the
supplied workflow reference.

Files: `intro Website/Website/UI Idea/06-UI-upgrade-options.html` and
`intro Website/INTRO_WEBSITE_CHANGE_LOG.md`.

Verified: `git diff --check` passed. Local browser preview confirmed the plain
option headings, transparent review-tool stage, reduced padding, four workflow
preview blocks, and non-sticky option row.

Remaining: Review the hover workflow previews in the target browser and choose
the final layout direction for the main intro website.

### 2026-07-31 17:24 HKT — Codex — Replace option navigation with a whole-tab workflow chart

Summary: Updated only `intro Website/Website/UI Idea/06-UI-upgrade-options.html`;
no other HTML file was edited. Moved the 展示優先 text into the plain subtitle
content area and removed its separate reading card. Replaced the four-option bar
and its per-option mini workflows with one whole-page workflow chart below the
cover. Top-bar hover/focus on 主頁、引言、第一部分、第二部分、設定 opens the
chart; the chart remains reachable while the pointer moves into it, and its
bubbles link to corresponding page sections. Each bubble has a short one-line
label with no visible explanatory text outside the chart.

Files: `intro Website/Website/UI Idea/06-UI-upgrade-options.html` and
`intro Website/INTRO_WEBSITE_CHANGE_LOG.md`.

Verified: `git diff --check` passed. Local browser preview confirmed the chart
is hidden on load, opens after a top-bar interaction, contains nine clickable
bubbles, and a chart bubble navigates to `#option-b`. Confirmed the Option 01
reading card is removed and its text appears directly beneath the subtitle.

Remaining: Review the final workflow-chart spacing on a narrow mobile viewport.

### 2026-07-31 17:59 HKT — Codex — Apply the selected UI directions to the intro website

Summary: Kept the full-screen cover and existing independent top-tab shell,
then applied the selected layouts to the intro StoryMap. 清代奏折制度 now uses
an Option 03 text-left/map-right presentation with the institutional reading
text consolidated before the next 清代奏折上諭的研究價值 card. 研究價值 and
研究成果：「清代奏摺與上諭分析平台」 use visual-left/reading-right Option 02
layouts; 以數位方法研究清代奏折和上諭 uses a table-first Option 01 layout.
The research-difficulty and 林爽文 event groups now use three clickable folder
cards, each expanding a full text panel and a paired photo, route, or review-tool
visual. The 引言 hover chart was polished and its links updated for the new
section structure; workbench click and keyboard behavior was added.

Files: `intro Website/Website/storymap/storymap-example.html`,
`intro Website/Website/storymap/storymap.css`,
`intro Website/Website/storymap/storymap.js`,
`intro Website/Website/storymap/storymap-cards.css`,
`intro Website/INTRO_WEBSITE_CHANGE_LOG.md`.

Verified: both requested `node --check` commands passed; `git diff --check`
passed; local browser preview confirmed the cover, independent tabs, workflow
chart navigation, preserved map interaction, split panels, table-first flow,
both folder workbenches, folder switching, the `字體` settings label, and zero
`<iframe>` elements.

Remaining: The repeated difficulty instruction was interpreted as the final,
more specific Option 03 three-folder workbench. Revisit only if the first
difficulty card should separately use Option 02. Narrow viewport visual review
remains to be done in the target browser.

### 2026-07-31 17:29 HKT — Codex — Polish the whole-tab workflow chart

Summary: Updated only `intro Website/Website/UI Idea/06-UI-upgrade-options.html`;
no other HTML file was edited. Tightened the chart into a centered hierarchy
with fixed, consistent bubble widths, smaller spacing, a shorter reveal area,
clearer branch rails, and a connected path to 比較. Rebalanced the dark chart
surface and node colors so it reads as one deliberate navigation map rather than
a stretched row of cards.

Files: `intro Website/Website/UI Idea/06-UI-upgrade-options.html` and
`intro Website/INTRO_WEBSITE_CHANGE_LOG.md`.

Verified: `git diff --check` passed. Local browser preview at desktop width
showed the compact centered chart, nine clickable bubbles, no horizontal
overflow, and the Option 01 copy directly beneath its subtitle.

Remaining: Review the final chart spacing on a narrow mobile viewport.

### 2026-07-31 18:23 HKT — Codex — Refine intro workbench cards and visual divisions

Summary: Replaced the two visible Option 03 folder workbenches with fixed mock
review panels and right-side one-card reading tracks. Added click/scroll active
state handling, mobile card expansion, clearer introduction section surfaces and
dividers, and a contained card for `研究成果：「清代奏摺與上諭分析平台」`.

Files: `intro Website/Website/storymap/storymap-example.html`,
`storymap.css`, `storymap.js`, `storymap-cards.css`, and this log plus
`intro Website/INTRO_WEBSITE_CHANGE_LOG.md`.

Verified: Both JavaScript syntax checks and targeted `git diff --check` passed;
the local HTTP response includes the fixed panels, card tracks, and platform
result card. The current in-app browser session blocked navigation from its
open UI-idea file to the local StoryMap URL, so visual browser QA remains open.

Remaining: Reopen the local StoryMap in an allowed local-HTTP browser session
and review desktop scroll tracking and mobile card expansion.

### 2026-07-31 18:36 HKT — Codex — Align intro StoryMap with UI-upgrade prototype

Summary: Compared the UI-study prototype with the live StoryMap and applied its
warm paper visual system, compact ruled section headings, contained editorial
reading surfaces, mock-tool toolbar anatomy, and compact intro top screen.
Changed both visible workbenches to page-flow cards beside sticky mock panels so
page scrolling advances the text without losing the desktop demonstration.

Files: `intro Website/Website/storymap/storymap-example.html`,
`storymap.css`, `storymap.js`, `storymap-cards.css`, and this log plus
`intro Website/INTRO_WEBSITE_CHANGE_LOG.md`.

Verified: Both JavaScript syntax checks and targeted `git diff --check` passed;
the local HTTP response contains the new section-heading, mock-toolbar,
workbench, and intro-cover markup. Fresh browser screenshot verification was not
available because the browser session no longer exposed the open StoryMap tab.

Remaining: Reopen the StoryMap in the browser and review desktop spacing and
mobile stacked-card behavior.

### 2026-07-31 19:04 HKT — Codex — Refine intro StoryMap section hierarchy

Summary: Removed the redundant `從文書制度到研究工具` bar, replaced orange option labels and visible UI-description copy with numbered headings, and redesigned the first two sections as a shared-map reading sequence. Added cumulative click/scroll opening for the three-card workbenches, separate visual panels, stronger section backgrounds/dividers, the requested AI-method sentence, and a contained platform-result card.

Files: `intro Website/Website/storymap/storymap-example.html`,
`intro Website/Website/storymap/storymap.css`,
`intro Website/Website/storymap/storymap.js`,
`intro Website/Website/storymap/storymap-cards.css`, and this log plus
`intro Website/INTRO_WEBSITE_CHANGE_LOG.md`.

Verified: `node --check` passed for the changed StoryMap JavaScript;
targeted `git diff --check` passed; local HTTP browser QA showed the shared map,
separated section surfaces, no first/second-part overlap, folded initial cards,
and cumulative card opening after click/scroll.

Remaining: Desktop behavior is verified locally. A narrow-mobile visual pass
remains optional; no deployment or push was performed.

### 2026-07-31 19:07 HKT — Codex — Restore the previous header version

Summary: Restored the header markup and header styling from the commit immediately before the latest StoryMap prototype commit, while preserving the latest content-panel and StoryMap section changes outside the header.

Files:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`

Verified: Confirmed the first 75 lines of the HTML and first 70 lines of the CSS match the previous commit’s header; passed `git diff --check`.

Remaining: None for this change.

### 2026-08-01 — Claude — Rewrite the StoryMap stylesheet and restructure the introduction tab

Summary: Rewrote `intro Website/Website/storymap/storymap.css` as a single
stylesheet, replacing four layered override passes that had accumulated from
earlier redesign attempts (original scrollytelling, option-1/2/3 experiment
layer, a second `:root` palette, and an `#intro-content` override layer). The
introduction tab was restructured so reading text and visual elements sit side
by side instead of translucent cards floating over backdrops. Header tabs are
centred, the settings control stays on the right, and the dropdown spans the
window width as a chain-style chapter chart.

Files: `intro Website/Website/storymap/storymap.css`,
`intro Website/Website/storymap/storymap-cards.css`,
`intro Website/Website/storymap/storymap-example.html`,
`intro Website/Website/storymap/storymap.js`, eight new option-study files in
`intro Website/Website/UI Idea/`, plus this log and
`intro Website/INTRO_WEBSITE_CHANGE_LOG.md`.

Verified: `node --check` passed for the changed StoryMap JavaScript;
`git diff --check` passed; HTML tag balance verified programmatically. Browser
QA was not performed in this session.

Remaining: Parts 1–3 retain the previous card markup and are held by a marked
transitional block in the stylesheet; restructure them next and then delete
that block. Browser validation of the introduction tab is outstanding. No
formal or sample review state was touched; no push was performed.

### 2026-08-01 17:52 HKT — Codex — Replace the first gallery placeholders with supplied source documents

Summary: Updated the 清代奏摺制度 card with the exact requested two-paragraph
Traditional Chinese text. Replaced its placeholder gallery with three supplied
sources: 常青奏摺影像, the 十全武功軍報傳遞路線圖, and the 軍機處隨手登記檔
image. Rendered selected PDF pages into web-ready PNG assets, linked each source
label to its local PDF, and corrected the inherited `data-photo-gallery-data`
attribute typo.

Files:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/gallery-npmpdf-page1.png`
- `intro Website/Website/storymap/gallery-route-map.png`
- `intro Website/Website/storymap/gallery-register-page2.png`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`

Verified: StoryMap JavaScript syntax, `git diff --check`, HTML tag balance,
gallery JSON, asset existence, requested text, local source links, and selected
PDF-page rendering/visual inspection all passed.

Remaining: Browser visual and interaction QA remains to be performed in the
local HTTP preview.

### 2026-08-01 18:13 HKT — Codex — Refine the research-difficulty cards

Summary: Removed the 參考來源 link and visible mock-panel labels from the
研究清代奏折的主要困難 section, and replaced its three accordion cards with
the requested headings and Traditional Chinese text.

Files: `intro Website/Website/storymap/storymap-example.html`,
`intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Passed StoryMap and embedded-tool JavaScript syntax checks,
`git diff --check`, targeted label/text checks, and HTML tag-balance validation.

Remaining: Browser visual and interaction QA remains to be performed in the
local HTTP preview. No formal or sample review state was touched; no push was
performed.

### 2026-08-02 09:51 HKT — Codex — Unify StoryMap photo galleries and enlarged-image interaction

Summary: Converted the standalone research-difficulty and case-background
photos to the shared image-plus-information gallery UI; added tap/click
enlargement for route-gallery images; and isolated per-image fit, position, and
zoom settings so switching images cannot carry over another image's size or
crop.

Files: `intro Website/Website/storymap/storymap-example.html`,
`intro Website/Website/storymap/storymap.css`,
`intro Website/Website/storymap/storymap.js`,
`intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Passed `node --check` for the StoryMap and embedded-tool JavaScript,
`git diff --check`, targeted gallery/lightbox/settings checks, and HTML
tag-balance validation.

Remaining: Browser visual and interaction QA remains to be performed in the
local HTTP preview. No formal or sample review state was touched; no push was
performed.

### 2026-08-02 10:00 HKT — Codex — Reset gallery area when switching pages

Summary: Fixed the gallery page-switch state so a touch-expanded information
panel is collapsed before the next image is rendered. The panel scroll
position and optional per-page body-height override are also reset, preventing
a longer page from leaving its expanded area on a shorter page.

Files: `intro Website/Website/storymap/storymap.js`,
`intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Passed `node --check Website/storymap/storymap.js` and
`git diff --check`; confirmed the page-switch reset logic is present.

Remaining: Browser visual and touch interaction QA remains to be performed in
the local HTTP preview. No formal or sample review state was touched; no push
was performed.

### 2026-08-02 10:03 HKT — Codex — Make expanded gallery height page-specific

Summary: Removed the shared fixed `32%` expanded-body height that forced every
gallery page to occupy the same area. Expanded panels now use each page's
natural description height with a configurable maximum, while the image stage
remains fixed. The page-switch reset remains in place.

Files: `intro Website/Website/storymap/storymap.css`,
`intro Website/Website/storymap/storymap.js`,
`intro Website/Website/storymap/storymap-cards.css`,
`intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Passed `node --check Website/storymap/storymap.js` and
`git diff --check`; confirmed the shared `32%` rule is removed and the
page-specific max-height rule is active.

Remaining: Browser visual and touch interaction QA remains to be performed in
the local HTTP preview. No formal or sample review state was touched; no push
was performed.

### 2026-08-02 10:13 HKT — Codex — Merge the research-difficulty table category

Summary: Merged the four research-tool rows under one vertically merged
category label, 通信關係、資訊流向複雜. The AI, AI Skills, Python 文本搜尋,
and 互動式網站 tools and explanations were preserved, and the merged label is
vertically centered.

Files: `intro Website/Website/storymap/storymap-example.html`,
`intro Website/Website/storymap/storymap.css`,
`intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Confirmed the old table labels are removed and `rowspan="4"` is
present; passed StoryMap JavaScript syntax and `git diff --check` validation.

Remaining: Browser visual QA remains to be performed in the local HTTP
preview. No formal or sample review state was touched; no push was performed.

### 2026-08-02 10:15 HKT — Codex — Split the research-difficulty table into two merged groups

Summary: Corrected the table to use two separate two-row groups:
史料數量龐大 for rows 1–2, and 通信關係、資訊流向複雜 for rows 3–4.

Files: `intro Website/Website/storymap/storymap-example.html`,
`intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Confirmed exactly two `rowspan="2"` category cells are present;
passed StoryMap JavaScript syntax and `git diff --check` validation.

Remaining: Browser visual QA remains to be performed in the local HTTP
preview. No formal or sample review state was touched; no push was performed.

### 2026-08-02 10:22 HKT — Codex — Standardize inline citations in the reference UI

Summary: Converted the inline citations for 莊吉發, 戴英從, and 許毓良 to the
requested parenthetical format `(作者，《書名》，年份)`, linked each citation
to `references.html` through the existing `inline-reference` styling, and added
the missing 莊吉發 and 許毓良 reference entries.

Files: `intro Website/Website/storymap/storymap-example.html`,
`intro Website/Website/references.html`,
`intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Confirmed all three citation links and reference anchors are present;
passed StoryMap JavaScript syntax and `git diff --check` validation.

Remaining: Browser visual QA of the citation links remains to be performed in
the local HTTP preview. No formal or sample review state was touched; no push
was performed.

### 2026-08-02 10:31 HKT — Codex — Add gallery image references

Summary: Added the supplied Chinese-style bibliographic references to gallery 1
image 1 and image 3, the National Palace Museum reference to 研究清代奏折的
主要困難 image 1, and the National Cultural Memory Bank reference to
示範案例：林爽文民變 image 1. External links and the supplied 2026/08/02
browsing date were preserved.

Files: `intro Website/Website/storymap/storymap-example.html`,
`intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Confirmed all four gallery source objects contain citation text and a
link; passed StoryMap JavaScript syntax and `git diff --check` validation.

Remaining: Browser visual QA of the expanded gallery references remains to be
performed in the local HTTP preview. No formal or sample review state was
touched; no push was performed.

### 2026-08-02 09:36 HKT — Codex — Widen the research-results and case-study introductions

Summary: Extended the title and introductory text block in 研究成果：「清代奏摺與
上諭分析平台」 and the title/introduction block in 示範案例：林爽文民變
（1786-1788） to the full content width. Visual panels and expandable cards were
preserved.

Files: `intro Website/Website/storymap/storymap-cards.css`,
`intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Confirmed both section-specific full-width rules; passed StoryMap and
embedded-tool JavaScript syntax checks and `git diff --check`.

Remaining: Browser visual and interaction QA remains to be performed in the
local HTTP preview. No formal or sample review state was touched; no push was
performed.

### 2026-08-02 09:20 HKT — Codex — Fix collapsed gallery information height

Summary: Changed the gallery image stage to fill the available height when the
information panel is collapsed. The information panel is now auto-height by
default and restores its expanded height only on hover, focus, or touch
expansion.

Files: `intro Website/Website/storymap/storymap.css`,
`intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Confirmed the collapsed and expanded gallery flex rules; passed
StoryMap and embedded-tool JavaScript syntax checks and `git diff --check`.

Remaining: Browser visual and interaction QA remains to be performed in the
local HTTP preview. No formal or sample review state was touched; no push was
performed.

### 2026-08-02 09:18 HKT — Codex — Make the second-card spacing explicit

Summary: Added an explicit responsive `margin-top` directly to the `清代奏折的研究價值`
card and reinforced it with a section-specific `!important` rule, making the
visible separation independent of the shared grid-gap styling.

Files: `intro Website/Website/storymap/storymap-example.html`,
`intro Website/Website/storymap/storymap-cards.css`,
`intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Confirmed both margin rules are present; passed StoryMap and embedded-
tool JavaScript syntax checks and `git diff --check`.

Remaining: Browser visual and interaction QA remains to be performed in the
local HTTP preview. No formal or sample review state was touched; no push was
performed.

### 2026-08-02 09:16 HKT — Codex — Strengthen the section 4 full-width override

Summary: Strengthened the section 4 rule so both the introductory block and its
body explicitly use `width: 100%` and no `max-width` constraint.

Files: `intro Website/Website/storymap/storymap-cards.css`,
`intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Confirmed both section-specific width rules are present; passed
StoryMap and embedded-tool JavaScript syntax checks and `git diff --check`.

Remaining: Browser visual and interaction QA remains to be performed in the
local HTTP preview. No formal or sample review state was touched; no push was
performed.

### 2026-08-02 09:14 HKT — Codex — Widen the digital-methods introduction

Summary: Extended the `因此，研究奏摺時` introductory text in section 4 to
the full content width of the website while leaving the title and comparison
table unchanged.

Files: `intro Website/Website/storymap/storymap-cards.css`,
`intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Confirmed the section-specific full-width rule; passed StoryMap and
embedded-tool JavaScript syntax checks and `git diff --check`.

Remaining: Browser visual and interaction QA remains to be performed in the
local HTTP preview. No formal or sample review state was touched; no push was
performed.

### 2026-08-02 09:13 HKT — Codex — Add spacing above the research-value card

Summary: Added dedicated responsive top margin above the `清代奏折的研究價值`
card.

Files: `intro Website/Website/storymap/storymap-cards.css`,
`intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Confirmed the second-card margin rule; passed StoryMap and embedded-
tool JavaScript syntax checks and `git diff --check`.

Remaining: Browser visual and interaction QA remains to be performed in the
local HTTP preview. No formal or sample review state was touched; no push was
performed.

### 2026-08-02 09:11 HKT — Codex — Combine the制度與研究價值 cards under one gallery

Summary: Moved `清代奏折的研究價值` into the `清代奏折制度` section as a
second stacked text card, reused the existing three-image gallery for both
cards, and removed the separate research-value gallery section. The navigation
target now points to the moved card.

Files: `intro Website/Website/storymap/storymap-example.html`,
`intro Website/Website/storymap/storymap.css`,
`intro Website/Website/storymap/storymap-cards.css`,
`intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Passed StoryMap and embedded-tool JavaScript syntax checks,
`git diff --check`, combined-section/gallery/navigation checks, and HTML
tag-balance validation.

Remaining: Browser visual and interaction QA remains to be performed in the
local HTTP preview. No formal or sample review state was touched; no push was
performed.

### 2026-08-01 18:37 HKT — Codex — Remove hand-built mock-panel labels

Summary: Removed all visible `HAND-BUILT MOCK PANEL / 文書研究平台` labels from
the StoryMap page while preserving the underlying document-panel content and
interactions.

Files: `intro Website/Website/storymap/storymap-example.html`,
`intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Confirmed zero matching labels remain; passed StoryMap and embedded-
tool JavaScript syntax checks, `git diff --check`, and HTML tag-balance
validation.

Remaining: Browser visual and interaction QA remains to be performed in the
local HTTP preview. No formal or sample review state was touched; no push was
performed.

### 2026-08-01 18:29 HKT — Codex — Rewrite the 林爽文民變 demonstration case

Summary: Updated the case-study heading to `示範案例：林爽文民變（1786-1788）`,
added the requested introduction, and replaced the three expandable cards with
the supplied 林爽文民變、資訊傳遞、 and 史料來源 content. Older duplicate case
cards were synchronized to the same wording.

Files: `intro Website/Website/storymap/storymap-example.html`,
`intro Website/Website/storymap/storymap-cards.css`,
`intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Passed StoryMap and embedded-tool JavaScript syntax checks,
`git diff --check`, requested-content and old-title removal checks, and HTML
tag-balance validation.

Remaining: Browser visual and interaction QA remains to be performed in the
local HTTP preview. No formal or sample review state was touched; no push was
performed.

### 2026-08-01 18:24 HKT — Codex — Revise the digital-methods introduction

Summary: Replaced the introductory sentence in 以數位方法研究清代奏折和上諭
with the requested explanation of analysing individual documents, communication
relationships, and information networks. The comparison table is unchanged.

Files: `intro Website/Website/storymap/storymap-example.html`,
`intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Passed StoryMap and embedded-tool JavaScript syntax checks,
`git diff --check`, requested-text validation, and HTML tag-balance validation.

Remaining: Browser visual and interaction QA remains to be performed in the
local HTTP preview. No formal or sample review state was touched; no push was
performed.

### 2026-08-01 18:20 HKT — Codex — Add the research-difficulty introduction

Summary: Added `然而，研究奏折與上諭有不少困難。` directly beneath the
研究清代奏折的主要困難 heading and before the accordion cards.

Files: `intro Website/Website/storymap/storymap-example.html`,
`intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Passed StoryMap and embedded-tool JavaScript syntax checks,
`git diff --check`, targeted sentence-presence validation, and HTML
tag-balance validation.

Remaining: Browser visual and interaction QA remains to be performed in the
local HTTP preview. No formal or sample review state was touched; no push was
performed.

### 2026-08-03 12:24 HKT — Codex — Center the route line in the case-study second image

Summary: Adjusted the second 林爽文民變 image to crop toward the eastern map area, placing the red route line nearer the panel center with cover positioning and 1.85× zoom.

Files: `intro Website/Website/storymap/storymap-cards.css`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Passed `git diff --check`.

Remaining: Reload the local HTTP preview to confirm the red line visually; no formal or sample review state was touched; no push was performed.

### 2026-08-03 12:09 HKT — Codex — Add controls for the case-study second image

Summary: Added a dedicated card-CSS selector for the `case-route` panel, the second image in 示範案例：林爽文民變, with independent fit, left, top, and zoom controls.

Files: `intro Website/Website/storymap/storymap-cards.css`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Passed `git diff --check`.

Remaining: Browser visual QA remains to be performed in the local HTTP preview. No formal or sample review state was touched; no push was performed.

### 2026-08-03 11:49 HKT — Codex — Add independent gallery image positioning controls

Summary: Added card-CSS controls for each image's shown area and position: `--photo-fit`, `--photo-left`, `--photo-top`, and `--photo-zoom`, with matching group defaults.

Files: `intro Website/Website/storymap/storymap-cards.css`, `intro Website/Website/storymap/storymap.css`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Passed StoryMap JavaScript syntax checking, `git diff --check`, and variable-reference validation.

Remaining: Browser visual QA remains to be performed in the local HTTP preview. No formal or sample review state was touched; no push was performed.

### 2026-08-03 11:42 HKT — Codex — Use the supplied intro_1 image directly

Summary: Updated the first 清代奏折制度 gallery image to load directly from `Visual Material/Done/intro_1.png`, preserving its descriptive alt text.

Files: `intro Website/Website/storymap/storymap-example.html`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Passed StoryMap JavaScript syntax checking, `git diff --check`, and supplied-image path validation.

Remaining: Browser visual QA remains to be performed in the local HTTP preview. No formal or sample review state was touched; no push was performed.

### 2026-08-03 11:36 HKT — Codex — Add hover explanations to information-source labels

Summary: Added the five requested event explanations beneath 情報來源1–5 in the 硃119 source-flow panel, with hover/focus expansion and connector refresh behavior.

Files: `intro Website/Website/storymap/storymap-example.html`, `intro Website/Website/storymap/storymap.css`, `intro Website/Website/storymap/storymap.js`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Passed StoryMap JavaScript syntax checking, `git diff --check`, and targeted source-detail validation.

Remaining: Browser visual and hover interaction QA remains to be performed in the local HTTP preview. No formal or sample review state was touched; no push was performed.

### 2026-08-03 11:26 HKT — Codex — Replace intro images with Done assets

Summary: Replaced the intro's non-GIF images with the requested `Visual Material/Done` set: `intro_1–3` for 清代奏折制度, `intro_4` for the research-difficulty card, and `intro_7–10` for the 林爽文民變 case. The GIF and route SVG remain unchanged.

Files: `intro Website/Website/storymap/storymap-example.html`, `intro Website/Website/storymap/storymap.css`, the eight rendered `done-intro-*` assets, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Passed StoryMap JavaScript syntax checking, `git diff --check`, and targeted image-reference validation. No formal or sample review state was touched; no push was performed.

Remaining: Browser visual QA remains to be performed in the local HTTP preview.

### 2026-08-03 10:54 HKT — Codex — Use Fizzy Background PDF in the information-transmission panel

Summary: Rendered the supplied `Fizzy Background.pdf` as a web-ready PNG for the `林爽文民變中的資訊傳遞` gallery panel and kept the original PDF as its source link.

Files: `intro Website/Website/storymap/storymap-example.html`, `intro Website/Website/storymap/fizzy-background-from-pdf.png`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Passed StoryMap JavaScript syntax checking, `git diff --check`, and targeted asset/link validation.

Remaining: Reload the local HTTP preview to confirm the backdrop visually. No formal or sample review state was touched; no push was performed.

### 2026-08-03 10:41 HKT — Codex — Fix row-spanned table column styling

Summary: Added explicit classes to all `數位工具` and `如何協助研究` body cells, preventing the row-spanned layout from applying the orange first-column style to the tool cells.

Files: `intro Website/Website/storymap/storymap-example.html`, `intro Website/Website/storymap/storymap.css`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Passed StoryMap JavaScript syntax checking, `git diff --check`, and targeted class-count validation.

Remaining: Reload the local HTTP preview to confirm the corrected table visually. No formal or sample review state was touched; no push was performed.

### 2026-08-03 10:40 HKT — Codex — Match the table body column backgrounds

Summary: Applied the 人工智能技能（AI Skills） grey background to all body cells in 數位工具 and 如何協助研究, while leaving the header row unchanged.

Files: `intro Website/Website/storymap/storymap.css`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Passed `git diff --check`.

Remaining: Browser visual QA remains to be performed in the local HTTP preview. No formal or sample review state was touched; no push was performed.

### 2026-08-03 10:36 HKT — Codex — Restyle the digital-tools table column

Summary: Applied the table's grey backdrop to the 數位工具 column and changed its text to the standard dark colour.

Files: `intro Website/Website/storymap/storymap.css`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Passed `git diff --check`.

Remaining: Browser visual QA remains to be performed in the local HTTP preview. No formal or sample review state was touched; no push was performed.

### 2026-08-02 21:08 HKT — Codex — Scale the intro GIF proportionally

Summary: Replaced the fixed GIF height with `--visual-scale`; the frame now scales width and height together using the original 2048×1080 aspect ratio.

Files: `intro Website/Website/storymap/storymap-cards.css`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Passed `git diff --check`.

Remaining: Reload the local HTTP preview to confirm proportional scaling visually. No formal or sample review state was touched; no push was performed.

### 2026-08-02 21:01 HKT — Codex — Widen the intro GIF container

Summary: Removed the shared 1560px content-width cap for the research-results section only, allowing the GIF to fill the available page width.

Files: `intro Website/Website/storymap/storymap-cards.css`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Passed `git diff --check`.

Remaining: Reload the local HTTP preview to confirm the wider frame visually. No formal or sample review state was touched; no push was performed.

### 2026-08-02 20:59 HKT — Codex — Make the intro GIF height variable effective

Summary: Fixed the more-specific intro GIF frame rule that forced `height: auto`, so the `--visual-h` setting now changes the displayed frame height.

Files: `intro Website/Website/storymap/storymap-cards.css`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Passed `git diff --check`.

Remaining: Reload the local HTTP preview to confirm the enlarged frame visually. No formal or sample review state was touched; no push was performed.

### 2026-08-02 10:45 HKT — Codex — Remove browsing dates from gallery references

Summary: Removed all browsing-date text from the five StoryMap gallery source labels while preserving their citation details and clickable links.

Files: `intro Website/Website/storymap/storymap-example.html`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Confirmed no `瀏覽日期` remains in the gallery references and passed `git diff --check`.

Remaining: Browser visual QA remains to be performed in the local HTTP preview. No formal or sample review state was touched; no push was performed.

### 2026-08-02 10:37 HKT — Codex — Apply PolyU full-reference format to gallery sources

Summary: Reformatted all five StoryMap gallery source labels according to the supplied PolyU Chinese thesis style, preserving the supplied links and browsing date.

Files: `intro Website/Website/storymap/storymap-example.html`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Passed StoryMap JavaScript syntax checking, `git diff --check`, and targeted validation confirming all five reference strings.

Remaining: Browser visual QA of expanded gallery references remains to be performed in the local HTTP preview. No formal or sample review state was touched; no push was performed.

### 2026-08-01 18:15 HKT — Codex — Match the communication-difficulty point form

Summary: Changed the two questions in 通信關係複雜 from a numbered list to the
dash-led point form used in `13-combined-preview.html`, with matching list
indentation and spacing.

Files: `intro Website/Website/storymap/storymap-example.html`,
`intro Website/Website/storymap/storymap.css`,
`intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Passed StoryMap and embedded-tool JavaScript syntax checks,
`git diff --check`, targeted point-list and wording checks, and HTML
tag-balance validation.

Remaining: Browser visual and interaction QA remains to be performed in the
local HTTP preview. No formal or sample review state was touched; no push was
performed.
### 2026-08-02 11:25 HKT — Codex — Load the 硃40 review capture into the research-results card

Summary: Replaced the hand-built research-results placeholder with the current light-mode 硃40 review-tool GIF, added it as a local StoryMap asset, and preserved the 2048×1080 aspect ratio.

Files: `intro Website/Website/storymap/zhu40-review-tool-capture.gif`, `intro Website/Website/storymap/storymap-example.html`, `intro Website/Website/storymap/storymap-cards.css`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Passed StoryMap and embedded-tool JavaScript syntax checks and `git diff --check`. Browser QA confirmed one visible GIF image in the section, loaded successfully at its expected 2048×1080 natural dimensions, with the intended wide light-mode presentation.

Remaining: None for this insertion. No formal or sample review state was touched; no push was performed.

### 2026-08-02 23:45 HKT — Codex — Refine 硃119 panel spacing, metadata, and source marks

Summary: Added more space above the light 硃119 document panel, limited it to a 700px document window with internal scrolling, and rebalanced the title/metadata/body typography. Replaced the long date metadata with `乾隆五十二年發出、硃批。`, simplified the four labels to `情報來源1`–`情報來源4`, and narrowed the visual marks to the five requested source-reporting phrases.

Files: `intro Website/Website/storymap/storymap-example.html`, `intro Website/Website/storymap/storymap.css`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Confirmed all five phrases are exact substrings of canonical 硃119, passed JavaScript syntax checking and `git diff --check`, and completed local browser QA with a scrollable panel, 4 bubbles, 4 connectors, 5 requested highlights, and no console warnings/errors.

Remaining: None for this refinement. No formal or sample review state was touched; no push was performed.

### 2026-08-03 00:10 HKT — Codex — Balance the source-flow number labels

Summary: Added a left-side `03` visual-element marker to the 硃119 document panel to balance the existing right-side `03 資訊流向複雜` accordion marker, with a small-screen position adjustment.

Files: `intro Website/Website/storymap/storymap-example.html`, `intro Website/Website/storymap/storymap.css`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Browser QA confirmed matching `03` markers on the left panel and right accordion, preserved `情報來源1` visibility behavior, and no console warnings/errors. Passed `git diff --check`.

Remaining: None for this visual-balance adjustment. No formal or sample review state was touched; no push was performed.

### 2026-08-02 23:59 HKT — Codex — Hide off-screen source labels and expose panel controls

Summary: Updated the 硃119 source-annotation layer so labels and connector lines are shown only while their highlighted phrase is inside the document scroll viewport and visible page viewport; `前據各口岸探明` is grouped with 情報來源1. Added card-level variables in `intro Website/Website/storymap/storymap-cards.css` for panel width, height, margins, offsets, source-label space, and mobile top gap, and connected the shared panel styles to those variables.

Files: `intro Website/Website/storymap/storymap.js`, `intro Website/Website/storymap/storymap.css`, `intro Website/Website/storymap/storymap-cards.css`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Passed JavaScript syntax checking and `git diff --check`; targeted validation confirmed 4 bubbles, 5 requested highlights with `前據各口岸探明` assigned to 情報來源1, and the documented card controls. Browser QA confirmed only the visible initial source label/connector is shown, with no console warnings/errors.

Remaining: None for this refinement. No formal or sample review state was touched; no push was performed.

### 2026-08-02 11:30 HKT — Codex — Improve the 硃40 review capture clarity

Summary: Re-encoded the research-results GIF at the same 2048×1080 size, frame count, and duration with controlled sharpening and optimized palette dithering, preserving the interface text and interaction sequence.

Files: `intro Website/Website/storymap/zhu40-review-tool-capture.gif`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Confirmed the GIF remains 2048×1080, 74 frames, and 9.26 seconds. Browser QA confirmed the sharpened GIF loads visibly in the research-results section at 2048×1080 natural dimensions and the intended wide layout. Passed `git diff --check`.

Remaining: None for this clarity improvement. No formal or sample review state was touched; no push was performed.

### 2026-08-02 20:57 HKT — Codex — Restore the original light color balance

Summary: Replaced the darker clarity pass with a new re-encode based directly on the original light-mode GIF, using full-frame palette preservation and gentler sharpening so the original website colors remain faithful.

Files: `intro Website/Website/storymap/zhu40-review-tool-capture.gif`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Confirmed the GIF remains 2048×1080, 74 frames, and 9.26 seconds. Browser QA confirmed the color-balanced GIF loads visibly in the research-results section at 2048×1080 natural dimensions with the original light presentation. Passed `git diff --check`.

Remaining: None for this correction. No formal or sample review state was touched; no push was performed.

### 2026-08-02 21:02 HKT — Codex — Match the brighter unsolved-state capture

Summary: Brightened the GIF’s midtones from the original light-mode capture so the unsolved and panel-open states match the supplied screenshot’s brighter cream background and pale chart lines, while preserving highlight colors, text, dimensions, and timing.

Files: `intro Website/Website/storymap/zhu40-review-tool-capture.gif`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Confirmed the GIF remains 2048×1080, 74 frames, and 9.26 seconds. Browser QA confirmed the brighter GIF loads visibly in the research-results section at 2048×1080 natural dimensions, with the lighter unsolved/panel-open presentation. Passed `git diff --check`.

Remaining: None for this brightness correction. No formal or sample review state was touched; no push was performed.

### 2026-08-02 23:08 HKT — Codex — Add the light 硃119 source-flow document panel

Summary: Replaced the old `資訊流向複雜` mock visual with a light review-tool document-panel replica containing the canonical 硃119 metadata and full original text. Added four external source bubbles and dynamic connector lines to five exact highlighted spans across the four requested source categories, with no unrelated filter dataset. Scoped the panel controls to the teaching-site replica.

Files: `intro Website/Website/storymap/storymap-example.html`, `intro Website/Website/storymap/storymap.css`, `intro Website/Website/storymap/storymap.js`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Confirmed every highlight span is an exact substring of canonical 硃119, passed StoryMap JavaScript syntax checking and `git diff --check`, and completed local browser QA with 4 bubbles, 5 highlights, 4 connectors, full original text, and no console warnings/errors.

Remaining: None for this insertion. No formal or sample review state was touched; no push was performed.

### 2026-08-03 00:15 HKT — Codex — Align the left source-flow number with the document panel

Summary: Fixed the light 硃119 panel’s mirrored `03` marker so it aligns with the top of the document panel instead of floating in the gap beneath the section heading. Added `--source-panel-number-top` beside the other card-level panel controls, keeping the marker position easy to adjust from `storymap-cards.css`.

Files: `intro Website/Website/storymap/storymap.css`, `intro Website/Website/storymap/storymap-cards.css`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Browser QA confirmed the marker top and document-panel top are aligned exactly, the right-side `03` accordion remains active, and only the currently visible `情報來源1` label remains shown. No browser console warnings/errors were reported. Passed JavaScript syntax checking and `git diff --check`.

Remaining: None for this alignment fix. No formal or sample review state was touched; no push was performed.

### 2026-08-03 00:23 HKT — Codex — Keep only the sample 情報來源 callouts

Summary: Removed the mistaken mirrored `03` marker from the light 硃119 document panel. Kept the intended `情報來源1`–`情報來源4` callout labels and their left-side connector layout; offscreen labels remain hidden until their highlighted text is visible.

Files: `intro Website/Website/storymap/storymap-example.html`, `intro Website/Website/storymap/storymap.css`, `intro Website/Website/storymap/storymap-cards.css`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Browser QA confirmed no `.source-flow-panel-number` remains, `情報來源1` is visible on the left of the document, and `情報來源2`–`情報來源4` remain hidden at the initial scroll position. No browser console warnings/errors were reported. Passed JavaScript syntax checking and `git diff --check`.

Remaining: None for this correction. No formal or sample review state was touched; no push was performed.

### 2026-08-03 00:33 HKT — Codex — Mirror five numbered 情報來源 callouts

Summary: Split the five requested highlighted phrases into five distinct sources: `前據各口岸探明`, `據廈門蚶江員弁稟到`, `署守備陳邦光稟稱`, `據北淡水署都司易連、新莊巡檢王增錞來稟`, and `據廈門同知劉嘉會稟稱`. Added matching single-number `情報來源1`–`情報來源5` callout labels on both the left and right sides of the document panel, with independent stacking and connectors for each side.

Files: `intro Website/Website/storymap/storymap-example.html`, `intro Website/Website/storymap/storymap.css`, `intro Website/Website/storymap/storymap.js`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Browser QA confirmed 5 distinct highlights, 10 mirrored callout labels, 4 initially visible connectors for the first two visible sources, and no console warnings/errors. Passed JavaScript syntax checking and `git diff --check`.

Remaining: None for this source-label balance change. No formal or sample review state was touched; no push was performed.

### 2026-08-03 00:44 HKT — Codex — Use one alternating-side label per source

Summary: Removed the duplicated mirrored labels so each of the five sources has exactly one callout. Kept odd-numbered labels `情報來源1`, `情報來源3`, and `情報來源5` on the left, and even-numbered labels `情報來源2` and `情報來源4` on the right.

Files: `intro Website/Website/storymap/storymap-example.html`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Browser QA confirmed 5 total callout labels, 5 unique source keys, the first label on the left, the second on the right, and no console warnings/errors. Passed `git diff --check`.

Remaining: None for this alternating-label correction. No formal or sample review state was touched; no push was performed.

### 2026-08-03 00:46 HKT — Codex — Add requested case-study source images

Summary: Updated the introduction website's 林爽文民變 demonstration so the 02「林爽文民變中的資訊傳遞」card shows one route-map image linked to `Fizzy Background.pdf`, and the 03「史料來源」card shows a two-image gallery with the requested《明清臺灣檔案彙編》and《天地會》（一）cover previews.

Files: `intro Website/Website/storymap/storymap-example.html`, `intro Website/Website/storymap/storymap-cards.css`, the two new preview PNGs under `intro Website/Website/storymap/`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Rendered and visually inspected the first pages of the requested PDFs; confirmed the gallery data contains 1 image for 02 and 2 images for 03; passed StoryMap and embedded-tool JavaScript syntax checks and `git diff --check`.

Remaining: Local HTTP/browser visual QA passed and local checkpoint `06ce1d6` was created. Formal and sample review data remain untouched; no push was performed.

### 2026-08-03 10:37 HKT — Codex — Hide source labels at the document header

Summary: Updated the 硃119 source-label visibility test so a callout hides as soon as its highlight reaches the fixed document header, including the title/metadata area and filter bar.

Files: `intro Website/Website/storymap/storymap.js`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Browser QA confirmed labels disappear when their highlights move into the panel header zone and reappear for later body highlights; no browser console warnings/errors were reported. Passed JavaScript syntax checking and `git diff --check`.

Remaining: None for this header-visibility fix. No formal or sample review state was touched; no push was performed.

### 2026-08-03 11:32 HKT — Codex — Clarify StoryMap image-panel references

Summary: Replaced the image-gallery prompt `將滑鼠移到此處查看完整說明` with `閱讀更多` when explanatory paragraphs are available. For source-only image panels, the full linked reference now displays directly below the title without a prompt or hidden description area.

Files: `intro Website/Website/storymap/storymap.js`,
`intro Website/Website/storymap/storymap.css`,
`intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Local HTTP browser QA confirmed the description-gallery prompt is
`閱讀更多`, the source-only difficulty gallery has no prompt and has a visible
full source reference, and no browser warnings/errors were reported. Passed
both StoryMap JavaScript syntax checks and `git diff --check`.

Remaining: None for this image-panel behavior. No formal or sample review data
were touched; no push was performed.

### 2026-08-03 11:49 HKT — Codex — Show emperor actions from a clicked document origin

Summary: Extended both review-tool click-network renderers so emperor-action events are connected to and included with a clicked document when their `emperorDetail.doc_id` or `emperorDetail.edict_id` identifies that document's emperor-side origin. Existing source links remain unchanged and duplicate origin lines are suppressed.

Files: `review-tools/(1) formal/index.html`, `review-tools/(2) sample/index.html`, and this log.

Verified: Both HTML files' inline scripts parse successfully and `git diff --check` passes. Browser visual validation remains to be performed.

Remaining: Human browser validation of a clicked document and its emperor-action dot/line.

### 2026-08-03 16:06 HKT — Codex — Rebuild the introduction website's third-part workshop layout

Summary: Reorganized 第三部分 around three retained cover bars—`1. OCR 並結構化原始史料`, `2. 運用AI抽取資訊`, and `3. 後續功能：LLM Wiki`—and divided the long content into alternating card layouts and interactive charts.

Files: `intro Website/Website/storymap/storymap-example.html`, `intro Website/Website/storymap/storymap.css`, `intro Website/Website/storymap/storymap.js`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Passed StoryMap JavaScript syntax checking, balanced the HTML section tags, and passed `git diff --check`. Local HTTP browser QA confirmed the three cover bars, OCR toggle, printed-page labels, JSON field labels, and AI Chain interaction with no browser warnings/errors. A 390px responsive check found and corrected page-wide overflow from the AI Chain; the default viewport was restored. Formal and sample review data remain untouched; no push was performed.

Remaining: Review the complete third-part page content and spacing in the normal browser preview with the existing Part 1 changes included.

### 2026-08-03 15:08 HKT — Codex — Add 硃113 communication document panel

Summary: Replaced the second subcard of `研究清代奏折的主要困難` with the light review-tool document-panel replica for 硃113. Added four single source callouts—`收發時間`, `回覆先前上諭1`, `回覆先前上諭2`, and `回覆先前上諭3`—with the latter three linked on hover to the canonical 諭20、諭24、諭28 titles and issue dates. Both send/receive dates use the shared `收發時間` highlight key, and the connector logic now supports multiple highlights per label and page-scroll refreshes.

Files: `intro Website/Website/storymap/storymap-example.html`, `intro Website/Website/storymap/storymap-cards.css`, `intro Website/Website/storymap/storymap.css`, `intro Website/Website/storymap/storymap.js`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Confirmed the rendered 硃113 body text matches the canonical `review-tools/shared data/stage1_original_text.json` record exactly. Browser QA confirmed the second subcard, requested highlights, header-hidden labels, lower-date label reveal, and hover metadata. Passed StoryMap JavaScript syntax checking and `git diff --check`.

Remaining: None for this 硃113 panel. Formal and sample review data remain untouched; no push was performed.

### 2026-08-03 15:16 HKT — Codex — Correct document dates and shorten 硃113 preview

Summary: Replaced the generic header date text for 硃113 and 硃119 with their canonical send and 硃批 dates. Shortened the 硃113 panel after the third `欽此。` to `⋯⋯`, retaining the dated footer beginning at 乾隆五十二年正月十四日.

Files: `intro Website/Website/storymap/storymap-example.html`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Confirmed both header dates against `review-tools/shared data/stage1_original_text.json`. Browser QA confirmed both headers, the requested ellipsis, the retained dated footer, and removal of the previously displayed continuation text. Passed StoryMap JavaScript syntax checking and `git diff --check`.

Remaining: None for this date and preview correction. Formal and sample review data remain untouched; no push was performed.

### 2026-08-03 15:52 HKT — Claude — Add the Part 1 interactive interface replica

Summary: Built the introduction website's 第一部分「平台的整體介面」demonstration. The six placeholder `part-1-*` sections were restructured into one sticky `lay-acc` layout holding a persistent interactive replica of the sample review tool, with the existing approved explanation cards beside it. The replica has four clickable regions (`導覽列`, `時間與關係圖表`, `原始史料區`, `AI 分析區`) with numbered hotspots and floating labels, four fixed lane dots that open 節點資訊區, an AI-Skill filter that marks extracted ranges in the 硃42 original text, and a four-step AI sequence ending with 加入圖表 creating a new lane dot whose quotation resolves back to the highlighted original text. Demonstration content lives in a separate hand-editable module regenerated from the canonical Stage 1 file and the current sample state. In the 時間與關係圖表 card, `奏報事件` was corrected to `戰場事件` to match the real lane label in the sample tool.

Files: `intro Website/Website/storymap/storymap-example.html`, the new `intro Website/Website/storymap/part-1-interface.css`, `part-1-interface.js` and `part-1-interface-data.js`, the new `tool/scripts py/build_part1_interface_data.py`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Provenance audit confirmed the replica's 硃42 body, title, send/receive dates and rescript are byte-for-byte identical to `review-tools/shared data/stage1_original_text.json`, and that every dot and AI candidate matches its record in `review-tools/(2) sample/sample_all.data`. Headless jsdom QA passed 22 interaction checks with no runtime errors. Passed `node --check` on all three StoryMap JavaScript files and `git diff --check`.

Remaining: Human browser QA is outstanding — the Claude in Chrome extension was not connected, so visual layout, sticky behaviour and responsive breakpoints were not confirmed in a real browser. Confirm the `戰場事件` lane terminology. No formal or sample review state was touched; no push was performed.

### 2026-08-03 16:33 HKT — Codex — Establish the Part 1 sample-tool visual base

Summary: Reworked the 第一部分「平台的整體介面」replica shell to follow the sample review tool's basic anatomy: a control toolbar, horizontal four-lane time/relationship chart, and docked document and AI/tool windows. Replaced the oversized document preview with a bounded scroll area. Kept the separate `part-1-interface-data.js` source boundary and existing interaction hooks for later refinement; this pass prioritizes the visual base.

Files: `intro Website/Website/storymap/part-1-interface.js`, `intro Website/Website/storymap/part-1-interface.css`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Browser preview shows the sample-style toolbar, four horizontal lanes, compact docked panels, and a scrollable document body; no browser warning/error console entries. Passed `node --check Website/storymap/part-1-interface.js` and `git diff --check`.

Remaining: Later refine the click sequence, callout placement, and exact sample-tool control behavior after the visual base is approved. Formal and sample review data remain untouched; no push was performed.
### 2026-08-03 16:49 HKT — Codex — Align Part 3 with UI template and vertical card sequence

Summary: Replaced the previous third-part workshop treatment with the layout structure from `intro Website/Website/UI Idea/13-combined-preview.html`. Preserved all original 第三部分 headings and paragraphs verbatim, retained the three main step bars, and changed all Part 3 cards to one vertical reading sequence. The OCR and AI Chain label controls remain interactive.

Files: `intro Website/Website/storymap/storymap-example.html`, `intro Website/Website/storymap/storymap.css`, `intro Website/Website/storymap/storymap.js`, `intro Website/Website/storymap/storymap-cards.css`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Original-content comparison found all 45 paragraphs and 23 headings in the new Part 3. Browser QA confirmed the template-style bars, vertical card sequence, full-width flow, and interactive OCR/AI Chain labels. Passed StoryMap JavaScript syntax checking and `git diff --check`. Formal and sample review data remain untouched; no push was performed.

Remaining: None for this layout correction.

### 2026-08-03 16:49 HKT — Codex — Rebuild Part 1 around the real sample-tool workspace

Summary: Replaced the approximate Part 1 chart treatment with the sample tool's actual visual anatomy: toolbar controls, four vertical type columns, a vertical date ruler, dense relationship-line texture, a linked-information panel, and a right-hand original-document panel. Matched the 硃42 document header's compact date and source line. Removed the replica's JavaScript listeners that opened, closed, or retargeted the right-side explanation cards; those cards remain independent StoryMap content.

Files: `intro Website/Website/storymap/part-1-interface.js`, `intro Website/Website/storymap/part-1-interface.css`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Browser preview shows the three internal sample-tool columns, four vertical lane headers, dense background relationship lines, scrollable document text, and the real sample-style toolbar order. DOM check confirmed 4 lane columns, 112 presentation-only network lines, and a scrollable document panel; browser console had no warning/error entries. Passed `node --check Website/storymap/part-1-interface.js` and `git diff --check`.

Remaining: Exact chart data density and later guided interactions can be refined after this visual structure is approved. Formal and sample review data remain untouched; no push was performed.

### 2026-08-03 17:08 HKT — Codex — Split the remaining Part 3 sections into individual vertical parts

Summary: Divided `3. 選用的AI Model` and `4. Google Cloud` into separate vertical parts, divided the three LLM Wiki paragraphs into three individual parts, and positioned the research-question visual and JSON structure visual on the right beside their cards. Preserved the cover bar, three main step bars, template UI, and all original Part 3 text without adding explanatory copy or visual material.

Files: `intro Website/Website/storymap/storymap-example.html`, `intro Website/Website/storymap/storymap.css`, `intro Website/Website/storymap/storymap-cards.css`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Original-content comparison found all 45 paragraphs and 23 headings present. Confirmed the new model, cloud, and three LLM Wiki sections exist and the research visual uses the right grid column. Passed StoryMap JavaScript syntax checking and `git diff --check`. Formal and sample review data remain untouched; no push was performed.

Remaining: None for this requested Part 3 layout adjustment.

### 2026-08-03 17:18 HKT — Codex — Apply 林方／清方 event-and-source result UI

Summary: Reworked the Part 1 AI result area to follow the sample tool's 林方／清方 extraction anatomy: actor-group headers, event candidate cards, location/person/date facts, source quotation blocks, and nested source-chain blocks. Kept the confirmed 林方 event separate from the two reviewable 清方 candidates, with actor-specific red/blue styling and green confirmed state. Added quotation定位, source-date demonstration, add, skip, source-chain reveal, and reset behaviour without coupling the replica to the independent explanation cards.

Files: `intro Website/Website/storymap/part-1-interface.js`, `intro Website/Website/storymap/part-1-interface.css`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Browser QA confirmed two groups and three event cards, all three source quotations locate the 硃42 original, a confirmed 清方 candidate creates a new chart dot and reveals its source chain, skip leaves the candidate out of the chart, and reset restores the initial linked-document panel. Passed `node --check intro Website/Website/storymap/part-1-interface.js` and `git diff --check`. Formal and sample review data remain untouched; pre-existing StoryMap Part 3 edits were preserved.

Remaining: None for this event-and-source UI pass. No push was performed.

### 2026-08-03 17:59 HKT — Codex — Add a five-photo resource-card sample for 所需的工具與資源

Summary: Kept all five resource descriptions in one `2. 所需的工具與資源` part and reworked them into a stacked creative layout with alternating photo placement, a subtitle, a title, and the original paragraph text in each card. Reused five existing local project photos for the five cards.

Files: `intro Website/Website/storymap/storymap-example.html`, `intro Website/Website/storymap/storymap.css`, `intro Website/Website/storymap/storymap-cards.css`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Browser preview confirmed five stacked cards, five photos, and five subtitles inside the single tools part. Static check confirmed all five original tools paragraphs remain present. Passed StoryMap JavaScript syntax checking and `git diff --check`. Formal and sample review data remain untouched; pre-existing Part 1 changes were preserved; no push was performed.

Remaining: None for this requested resource-card sample.

### 2026-08-03 17:52 HKT — Claude — Replace 適合的研究問題 text boxes with an interactive swimlane gallery

Summary: Replaced the two prose `.relationship-node` boxes in Part 3's `1. 適合的研究問題` with a two-slide interactive four-line diagram, reusing the Part 1 replica's lane colours. Slide 1 shows three colour-coded response chains along the real 硃42 → 諭24 → 硃113 chain already used elsewhere on the site (events → official memorial, emperor actions → memorial/edict, later memorial → earlier edict), each with a floating Text callout, a legend, hover/click highlighting, and per-dot tooltips. Slide 2 reuses the same structure and adds five real events (from 硃56/硃60/硃71/硃57/硃61, dated between 硃42's send and 諭24's issue) plus a computed 15-day gap annotation, demonstrating the transmission-delay research question. Content is generated by a new script that fails the build if any quotation isn't a literal substring of its source document.

Files: `intro Website/Website/storymap/storymap-example.html`, the new `part-3-question-gallery.css`, `part-3-question-gallery.js` and `part-3-question-gallery-data.js`, the new `tool/scripts py/build_part3_question_data.py`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Provenance audit confirmed all three documents and every dot's quotation match `stage1_original_text.json` / `sample_all.data` exactly. Headless jsdom QA passed 17 interaction checks with no runtime errors. Passed `node --check` on all new JS and `git diff --check`.

Remaining: Real browser QA could not be completed — the Claude in Chrome extension cannot script `file://` pages without the user enabling file-URL access for the extension first. Visual layout (label/dot overlap, callout collisions) needs human confirmation via a served page. `.relationship-visual`/`.relationship-node` CSS is now unreferenced and could be cleaned up later. No formal or sample review state was touched; no push was performed.

### 2026-08-03 18:11 HKT — Codex — Add an alternate HTML option for 所需的工具與資源

Summary: Added a standalone Option 02 sample at `intro Website/Website/UI Idea/part3-tools-option-02.html`; the current StoryMap layout remains unchanged. The option uses an asymmetric archive wall with one large feature card, three compact cards, and one full-width backup card. Each card includes a subtitle, original paragraph text, and an existing local project photo.

Files: `intro Website/Website/UI Idea/part3-tools-option-02.html`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Browser preview confirmed five cards, five subtitles, five loaded photos, responsive grid layout, and no broken images. Passed `git diff --check`. No production StoryMap content or research data was changed; no push was performed.

Remaining: None for this standalone layout option.

### 2026-08-03 18:21 HKT — Codex — Add a checklist-and-information-panel HTML option

Summary: Added `intro Website/Website/UI Idea/part3-tools-option-03-checklist.html` as a separate checklist-style sample; the current StoryMap layout remains unchanged. The left window lists all five tools with checkboxes, while one right-side information window updates to show the selected tool's photo first and original information text below the photo.

Files: `intro Website/Website/UI Idea/part3-tools-option-03-checklist.html`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Browser preview confirmed five checklist rows, five information views, five loaded photos, and no broken images. Interaction test confirmed selecting `Agentic AI` updates the right panel and checked state. Passed `git diff --check`. No production StoryMap content or research data was changed; no push was performed.

Remaining: None for this standalone checklist option.

### 2026-08-03 18:24 HKT — Codex — Refine checklist row alignment

Summary: Moved the item number to a dedicated left column and the tick box to the far right of each checklist row in the standalone Option 03 HTML sample.

Files: `intro Website/Website/UI Idea/part3-tools-option-03-checklist.html`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Browser preview confirmed the number-left / title-middle / tick-right alignment and checked-state styling. No production StoryMap content or research data was changed; no push was performed.

Remaining: None for this checklist alignment refinement.

### 2026-08-03 18:37 HKT — Codex — Apply the checklist tools window to Part 3

Summary: Replaced the five-photo resource cards in the live `2. 所需的工具與資源` section with the checklist-and-information-panel layout. The left window lists tools `1` through `5`, with a smaller subtitle beneath each title and a far-right tick; the right window shows the selected tool's photo first and original information text below it. Count/status labels were removed.

Files: `intro Website/Website/storymap/storymap-example.html`, `intro Website/Website/storymap/storymap.css`, `intro Website/Website/storymap/storymap.js`, `intro Website/Website/storymap/storymap-cards.css`, `intro Website/Website/UI Idea/part3-tools-option-03-checklist.html`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: Browser preview confirmed five checklist rows, five subtitles, far-right tick alignment, five information views, and loaded photos. Selecting `Agentic AI` updates the right panel and active row; the live section contains no count/status labels. Passed StoryMap JavaScript syntax checking and `git diff --check`. Existing Part 3 question-gallery changes were preserved; no push was performed.

Remaining: None for the applied checklist tools window.

### 2026-08-03 18:44 HKT — Codex — Enlarge text in the Part 3 tools information panel

Summary: Increased the selected tool title and original information paragraph inside the `所需的工具與資源` visual panel in the live StoryMap section and standalone checklist sample; removed the sample's unused status reference.

Files: `intro Website/Website/storymap/storymap.css` and `intro Website/Website/UI Idea/part3-tools-option-03-checklist.html`.

Verified: Browser preview showed the enlarged panel text; StoryMap JavaScript syntax checking and `git diff --check` passed. Existing Part 3 question-gallery changes were preserved.

Remaining: None for this text-size adjustment.

### 2026-08-03 18:51 HKT — Codex — Add adjustable dimensions to the Part 3 tools window

Summary: Added centralized CSS layout controls for the `所需的工具與資源` checklist and information panel. The live StoryMap and standalone sample now expose overall width, checklist-column width, overall height, checklist-row height, and information-photo height as variables.

Files: `intro Website/Website/storymap/storymap.css` and `intro Website/Website/UI Idea/part3-tools-option-03-checklist.html`.

Verified: Live browser preview showed all five checklist rows and five information views; selecting a row still changes the information panel. The standalone sample also loaded all five rows and views. Passed StoryMap JavaScript syntax checking and `git diff --check`.

Remaining: None for the adjustable tools-window layout.

### 2026-08-03 18:55 HKT — Codex — Enlarge Part 3 tools-window typography

Summary: Increased the text size for the five checklist rows, row numbers, subtitles, tick marks, the `工具清單` and `工具資訊` window headings, and the selected tool's information panel. Increased row height to keep the larger labels readable.

Files: `intro Website/Website/storymap/storymap.css` and `intro Website/Website/UI Idea/part3-tools-option-03-checklist.html`.

Verified: Browser preview showed the enlarged checklist and information-panel text with all five rows and both window headings visible. Passed StoryMap JavaScript syntax checking and `git diff --check`.

Remaining: None for this typography adjustment.

### 2026-08-03 19:01 HKT — Codex — Move Part 3 tools sizing controls into card CSS

Summary: Added the checklist and information-panel sizing variables to the `#part-3-tools` block in `intro Website/Website/storymap/storymap-cards.css`, covering overall width, checklist-column width, overall height, row height, and information-photo height.

Files: `intro Website/Website/storymap/storymap-cards.css`.

Verified: StoryMap browser preview loaded the card with one checklist, five rows, one information panel, and two window headings. Passed StoryMap JavaScript syntax checking and `git diff --check`.

Remaining: None for the card-specific sizing controls.

### 2026-08-03 19:11 HKT — Codex — Use fixed px and percentage sizing for Part 3 tools card

Summary: Changed the Part 3 tools card to use a fixed `px` height for the complete checklist and information window, a `%` width for the checklist column, and percentage rows for the information photo and text panel. Added internal scrolling so a smaller fixed height remains usable.

Files: `intro Website/Website/storymap/storymap.css`, `intro Website/Website/storymap/storymap-cards.css`, and `intro Website/Website/UI Idea/part3-tools-option-03-checklist.html`.

Verified: Browser preview rendered the fixed-height card and percentage photo/info split. Existing user-edited Part 3 content changes were preserved. Passed StoryMap JavaScript syntax checking and focused `git diff --check` for the three edited sizing files.

Remaining: None for the requested sizing-unit adjustment.

### 2026-08-03 19:20 HKT — Codex — Refresh StoryMap card CSS version for adjustable sizing

Summary: Updated the `storymap-cards.css` query version in the StoryMap HTML so changes made in the `#part-3-tools` sizing block are loaded instead of the cached defaults. The current card settings now apply `1000px` overall height, `25%` checklist width, and `70% / 30%` photo/info proportions.

Files: `intro Website/Website/storymap/storymap-example.html` and `intro Website/Website/storymap/storymap-cards.css`.

Verified: Browser inspection identified the stale values before the cache refresh; after changing the stylesheet version, the StoryMap card loaded the updated stylesheet. Existing Agentic AI animation and content edits were preserved.

Remaining: None for the CSS cache-refresh fix.

### 2026-08-03 19:24 HKT — Codex — Let card-level sizing variables override component defaults

Summary: Removed the component-level dimension variables that were overriding `#part-3-tools`. The checklist now uses fallback values only, so the card stylesheet controls the actual layout. Refreshed the StoryMap base stylesheet version as well.

Files: `intro Website/Website/storymap/storymap.css` and `intro Website/Website/storymap/storymap-example.html`.

Verified: Browser preview rendered the current `1000px` card with the `70%` photo / `30%` information split, and the Agentic AI animation remained active after selecting its row. Existing animation and content edits were preserved.

Remaining: None for the card-variable inheritance fix.

### 2026-08-04 13:19 HKT — Codex — Make 工具清單 row height adjustable

Summary: Stopped the checklist grid from stretching every row to fill the full card height. `--part3-tools-row-height` now controls the grid track height, with content-required expansion for long labels; the standalone sample uses the same behavior.

Files: `intro Website/Website/storymap/storymap.css`, `intro Website/Website/storymap/storymap-cards.css`, `intro Website/Website/storymap/storymap-example.html`, and `intro Website/Website/UI Idea/part3-tools-option-03-checklist.html`.

Verified: Browser preview showed compact rows with readable long labels, and the standalone sample loaded all five rows and five information views. Passed StoryMap JavaScript syntax checking and focused `git diff --check`.

Remaining: None for the adjustable row-height fix.

### 2026-08-04 13:24 HKT — Codex — Add per-section Part 3 card controls

Summary: Added clearly labelled per-section variables to `intro Website/Website/storymap/storymap-cards.css` so every Part 3 content card can independently adjust title/body font size, width, height, minimum height, padding, and line height. Added matching controls for the Part 3 chart cards, workflow cards, tools window typography, and OCR/AI/LLM Wiki stage bars. Refreshed the StoryMap stylesheet query version.

Files: `intro Website/Website/storymap/storymap-cards.css`, `intro Website/Website/storymap/storymap-example.html`, and `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`.

Verified: HTTP browser preview loaded the new stylesheet; all 21 Part 3 content sections reported the card-width control, representative cards had non-zero dimensions and the expected computed font sizes, all three stage bars reported the new sizing layer, and the browser reported no errors or warnings. StoryMap JavaScript syntax checks passed. `git diff --check` still reports a pre-existing trailing-space line in the current user-edited StoryMap HTML; that unrelated line was preserved.

Remaining: None for the requested per-section Part 3 controls. Adjust the variables in the labelled `#part-3-...` blocks when tuning a specific section.

### 2026-08-04 13:34 HKT — Codex — Give each Part 3 card an independent selector

Summary: Added stable IDs to the actual Part 3 multi-card and visual-card elements, including the two OCR definition cards, two AI Skills cards, two AI Chain cards, charts, workflow cards, the tools window, and the three LLM Wiki cards. Added one matching CSS control block per card ID, using the same direct-edit pattern as `#intro-1-2`; single-card sections remain directly adjustable by their section IDs.

Files: `intro Website/Website/storymap/storymap-example.html`, `intro Website/Website/storymap/storymap-cards.css`, and `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`.

Verified: Confirmed 52 unique Part 3 IDs; every new `-card` and `-chart` ID has a matching selector block. Browser preview loaded `storymap-cards.css?v=20260804-part3-individual-cards`, rendered representative cards with non-zero dimensions, and reported no errors or warnings. StoryMap JavaScript syntax checks passed. `git diff --check` still reports the pre-existing trailing-space line in the current user-edited StoryMap HTML; it was preserved.

Remaining: None for individual Part 3 card adjustment.

### 2026-08-04 13:36 HKT — Codex — Match Part 3 basic-flow text to the full-width method layout

Summary: Removed the card treatment from `3. 重用平台的基本流程` and expanded its heading and explanatory paragraph to the full StoryMap content width, matching the text-above-table layout used by `以數位方法研究清代奏折`. The workflow diagram remains below the text as the visual block.

Files: `intro Website/Website/storymap/storymap-example.html`, `intro Website/Website/storymap/storymap-cards.css`, `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`, and this log.

Verified: HTTP browser preview showed the section heading and paragraph outside a card, with transparent background, no border or padding, and the same 1193px content width as the workflow frame. The browser reported no errors or warnings. StoryMap JavaScript syntax checks passed. `git diff --check` still reports the pre-existing trailing-space line at `intro Website/Website/storymap/storymap-example.html:1000`; it was preserved.

Remaining: None for the requested Part 3 basic-flow layout.

### 2026-08-04 13:37 HKT — Codex — Show full text in 工具資訊 without inner scrolling

Summary: Changed the Part 3 tools information pane to a 50% photo / 50% text split and removed the inner text scrollbar, so each current item’s full description remains visible in the information panel. Applied the same behavior to the standalone checklist sample.

Files: `intro Website/Website/storymap/storymap.css`, `intro Website/Website/storymap/storymap-cards.css`, `intro Website/Website/storymap/storymap-example.html`, and `intro Website/Website/UI Idea/part3-tools-option-03-checklist.html`.

Verified: Browser preview loaded `storymap-cards.css?v=20260804-full-info-01`; all four current StoryMap item views and all five standalone sample views reported visible information content with `overflow: visible`. The Agentic AI animation remained active.

Remaining: None for the full-information-pane adjustment.

### 2026-08-04 13:45 HKT — Codex — Organize Part 3 CSS with numbered card controls

Summary:
- Added a numbered Part 3 CSS index from Part 3.0 through Part 3.7.
- Renamed section-default, stage-bar, visual-card, and individual-card blocks so each adjustment has a precise label such as Part 3.1.2 or Part 3.4.2.1.
- Preserved all existing selectors and sizing values; this change only improves navigation and editing clarity.

Files changed:
- `intro Website/Website/storymap/storymap-cards.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Confirmed the numbered index maps to the matching `#part-3-*` selectors.
- Focused `git diff --check` passes for `intro Website/Website/storymap/storymap-cards.css`.

Remaining:
- None for the CSS organization request.

### 2026-08-04 13:48 HKT — Codex — Make 工具資訊 height content-driven

Summary: Changed the active tool information view to use an automatic text row. Each item’s information panel now sizes itself from its own description, while the photo fills the remaining height of the fixed tools window. The standalone checklist sample uses the same layout.

Files: `intro Website/Website/storymap/storymap.css`, `intro Website/Website/storymap/storymap-cards.css`, `intro Website/Website/storymap/storymap-example.html`, and `intro Website/Website/UI Idea/part3-tools-option-03-checklist.html`.

Verified: Browser measurements showed different information heights for repository (340px), Agentic AI (384px), AI API (296px), and the backup item (296px), with no inner scrolling. The standalone sample also reported content-driven heights across all five views, and the Agentic AI animation remained active.

Remaining: None for the content-driven information height adjustment.

### 2026-08-04 13:59 HKT — Codex — Put OCR card controls in website order

Summary:
- Reordered the Part 3.4 OCR controls in `intro Website/Website/storymap/storymap-cards.css` to follow the actual StoryMap sequence from the OCR stage through structured-material import.
- Simplified each CSS heading to the visible card title; untitled OCR definition cards use the first ten-word paragraph excerpt, and paired visual blocks are labelled as text card or chart.
- Kept all selectors and sizing declarations unchanged while moving the matching card-control blocks beside their displayed section.

Files changed:
- `intro Website/Website/storymap/storymap-cards.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Confirmed the CSS Part 3.4 sequence matches the OCR section order in `intro Website/Website/storymap/storymap-example.html`.
- `node --check intro Website/Website/storymap/storymap.js` and `node --check intro Website/Website/storymap/part-3-question-gallery.js` passed.
- Focused `git diff --check` passes for `intro Website/Website/storymap/storymap-cards.css`.

Remaining:
- None for the OCR CSS organization request.

### 2026-08-04 14:10 HKT — Codex — Make OCR scanning animation width and height adjustable

Summary:
- Fixed the Part 3.4.2.3 OCR animation sizing control. The animation was capped by the parent grid at `440px`, so changing its child `--ocr-scene-max-w` alone could not make it wider.
- Added `--ocr-scene-column-w` to the same numbered control block and connected the parent grid to it; increased the default animation column to `620px` and the JSON output window to `12em`.

Files changed:
- `intro Website/Website/storymap/storymap-cards.css`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Browser measurement confirmed the live OCR scene renders at `620px` wide with the updated `1000px` maximum and a visible `12em` output panel.
- `node --check intro Website/Website/storymap/storymap.js` and `node --check intro Website/Website/storymap/part-3-question-gallery.js` passed.
- Focused `git diff --check` passes for the edited CSS files.

Remaining:
- None for the OCR animation sizing fix.

### 2026-08-04 14:13 HKT — Codex — Set OCR animation width to 65 percent

Summary:
- Changed `--ocr-scene-column-w` in Part 3.4.2.3 from a fixed `620px` to `65%`, so the OCR animation scales with the Part 3.4 content width.

Files changed:
- `intro Website/Website/storymap/storymap-cards.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Browser measurement confirmed a `775.43px` animation width inside a `1192.97px` Part 3.4 content area, exactly `65%`.

Remaining:
- None for the percentage-based OCR width adjustment.

### 2026-08-04 14:16 HKT — Codex — Add OCR animation text font controls

Summary:
- Added direct controls for the OCR animation’s JSON text font size, line height, font family, and filename label size in Part 3.4.2.3.
- Preserved the current rendered defaults: `11.5px` JSON text and `11px` filename text.

Files changed:
- `intro Website/Website/storymap/storymap-cards.css`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Browser measurement confirmed the new controls are active: JSON text `11.5px` with `20.125px` line height, and filename text `11px`.
- Focused `git diff --check` passes for the edited CSS files.

Remaining:
- None for the OCR animation font-control request.

### 2026-08-04 14:22 HKT — Codex — Add OCR output-window width control

Summary:
- Added `--ocr-output-w` to Part 3.4.2.3 so the JSON output window can be adjusted independently from the overall OCR animation width.
- Kept the default at `100%` of the animation area and documented percentage or fixed-pixel values.

Files changed:
- `intro Website/Website/storymap/storymap-cards.css`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Browser measurement confirmed the output window is using `--ocr-output-w: 100%` and measures `661.78px` inside the `715.78px` animation scene.
- Focused `git diff --check` passes for the edited CSS files.

Remaining:
- None for the OCR output-window width request.

### 2026-08-04 14:28 HKT — Codex — Center OCR output window

Summary:
- Centered the OCR JSON output window horizontally inside the animation scene when its configured width is narrower than the scene.
- Kept the existing output-window width and vertical flow unchanged.

Files changed:
- `intro Website/Website/storymap/storymap.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Browser measurement confirmed the output window is centered within the animation scene.
- Focused `git diff --check` passes for the edited CSS file.

Remaining:
- None for the OCR output-window alignment request.

### 2026-08-04 14:39 HKT — Codex — Add full-screen OCR PDF page viewer

Summary:
- Added click-to-open full-screen viewing for both OCR document previews: the 硃25 handwritten PDF sequence and the printed PDF sequence.
- Added description text below the page, X/outside-click/Escape close behavior, page counter, left/right buttons, and keyboard ArrowLeft/ArrowRight navigation through each document’s pages.

Files changed:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.js`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- `node --check intro Website/Website/storymap/storymap.js` passes.
- `git diff --check` passes for the edited StoryMap files.
- The animation output window remains horizontally centered at its configured width.

Remaining:
- Full-screen click navigation should receive a final in-app visual check after the StoryMap scroll position is focused on the OCR section.

### 2026-08-04 14:46 HKT — Codex — Increase basic-flow step spacing and height

Summary: Increased the vertical gap between each workflow number and its title, and increased the minimum height of every chevron step in `3. 重用平台的基本流程`. The values are controlled by the workflow card’s CSS variables.

Files: `intro Website/Website/storymap/storymap.css`, `intro Website/Website/storymap/storymap-cards.css`, `intro Website/Website/storymap/storymap-example.html`, and this log.

Verified: Browser preview loaded `storymap-cards.css?v=20260804-flow-step-01`; all eight steps measured 170px high with a 22px number-to-title gap. Existing workflow content remained intact.

Remaining: None for the basic-flow spacing and height adjustment.

### 2026-08-04 14:50 HKT — Codex — Correct OCR enlarged-window source references

Summary: Updated the enlarged OCR page viewer so both document sequences show the shared article title, author, and sent date, while the handwritten pages show the full 《宮中檔奏摺—乾隆朝》 reference and both Qing archive links. The printed pages now use the website's concise `明清台檔30, 80, 硃25` reference.

Files: `intro Website/Website/storymap/storymap.js` and this log.

Verified: `node --check intro Website/Website/storymap/storymap.js` and `git diff --check` pass. Existing uncommitted workflow, OCR animation, CSS, PDF, and image changes were preserved.

Remaining: None for the OCR enlarged-window reference text.

### 2026-08-04 14:51 HKT — Codex — Rebuild Agentic AI scene with Codex pet and four real-data windows

Summary:
- Replaced the two-window Agentic AI animation in Part 3 with four independently positioned windows: the official AI loop terminal, review-tool HTML writing, 硃25 OCR output, and the official-document review skill.
- Used real project commands, file paths, source-record fields, OCR snippets, and skill steps in the animated window data.
- Restyled the blue robot toward the supplied Codex pet reference, including the fluffy blue head, dark terminal face with `> _`, and a cropped lower body so the full robot does not need to be shown.
- Added independent CSS controls for each window's width, height, left/top position, font size, and 傾斜角度.

Files changed:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/Website/storymap/storymap.js`
- `intro Website/Website/storymap/storymap-cards.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Four embedded Agentic AI data blocks parse successfully.
- `node --check` passes for both StoryMap scripts.
- HTTP browser preview shows all four windows animating behind the Codex pet; the configured dimensions, positions, font sizes, and angles are active, with no browser errors or warnings.
- Focused `git diff --check` passes for all four edited StoryMap files.

Remaining:
- None for the Agentic AI four-window animation request.

### 2026-08-04 14:54 HKT — Codex — Smooth and reduce the Agentic AI pet

Summary:
- Replaced the segmented blue-part outlines with continuous radial blue gradients and soft inset shading across the Codex pet’s head, body, and arms.
- Removed the remaining hard borders from the pet components, including the terminal face panel, and reduced the pet container to `27%` width by `50%` height while keeping the lower body cropped.

Files changed:
- `intro Website/Website/storymap/storymap.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- HTTP browser preview shows the smaller, borderless, gradient-shaded pet centered in front of the four animated windows.
- Browser measurement reports `0px` borders for all eleven pet components and no console errors or warnings.
- Focused `git diff --check` passes for the edited StoryMap CSS.

Remaining:
- None for the Agentic AI pet refinement request.

### 2026-08-04 15:22 HKT — Codex — Resize Agentic AI pet and expand work-window source content

Summary:
- Replaced the window titles with the requested task labels: `Run Python`, `Create Website`, `Process OCR`, and `Write Skills`.
- Expanded all four animation sequences with longer source-backed content: the actual Python loop command and outputs, sample review-tool loading code, the 硃25 metadata and original-text excerpts, and the full official-document review Skill stages.
- Added responsive pet-size variables and capped the Codex pet at a readable smaller size; longer terminal content now scrolls without showing a scrollbar.

Files changed:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/Website/storymap/storymap-cards.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Four JSON animation blocks parse with 11, 11, 12, and 12 lines; titles match the requested labels.
- HTTP browser preview shows the longer content animating in all four windows; the pet measures `235px × 255.95px` at the checked viewport and no browser errors or warnings were reported.
- `node --check` passes for both StoryMap scripts and focused `git diff --check` passes for the edited StoryMap files.

Remaining:
- None for the Agentic AI title, source-content, and pet-size update.

### 2026-08-04 15:01 HKT — Codex — Align Part 3 workflow steps and OCR cards

Summary:
- Replaced the three detailed Part 3 stage numbers with workflow labels: `步驟二`, `步驟三至五`, and `步驟八`.
- Made all eight basic-flow chevrons buttons. Step 1 now scrolls to `1. 適合的研究問題`, and the other buttons target their corresponding Part 3 content.
- Changed Part 3 card headings to use the intro tab's coloured number squares. Moved `1. 甚麼是 OCR？` into the OCR definition card, added `2. 使用OCR的原因`, and renumbered the remaining OCR cards.
- Added sticky-header scroll offsets for direct card and stage-bar targets.

Files changed:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.js`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/Website/storymap/storymap-cards.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- `node --check intro Website/Website/storymap/storymap.js` and `node --check intro Website/Website/storymap/part-3-question-gallery.js` pass.
- `git diff --check` passes.
- In the HTTP browser preview, clicking the first flow button reaches the `適合的研究問題` card and clicking the second reaches the OCR definition card; the cards show 49px coloured squares and the OCR stage bar shows `步驟二`.
- Reloading the nested Part 3 hash keeps the Part 3 panel active; browser console reports no errors or warnings.

Remaining:
- None for this requested Part 3 numbering and navigation adjustment.

### 2026-08-04 15:23 HKT — Codex — Make 工具清單 row height adjustable

Summary:
- Changed the Part 3 `工具清單` grid from content-driven `minmax(..., max-content)` rows to the documented fixed `--part3-tools-row-height` value.
- Removed the duplicate row-height override from `#part-3-tools-card`, so the value in the card CSS control block now reaches the live list items.
- Added a cache-busting version for the updated StoryMap stylesheets while preserving the existing width and Agentic AI sizing changes.

Files changed:
- `intro Website/Website/storymap/storymap.css`
- `intro Website/Website/storymap/storymap-cards.css`
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- At the normal 1280px preview width, the current `--part3-tools-row-height: 100px` produces four 100px list items.
- At the 700px responsive breakpoint, all four rows retain the 100px minimum height.
- Reloaded the cache-busted stylesheet URLs and confirmed no browser errors or warnings.
- `git diff --check` passes.

Remaining:
- None for the adjustable `工具清單` row-height control.

### 2026-08-04 15:11 HKT — Codex — Added the Chinese reference-style rule

Summary:
- Added a rule to `intro Website/AGENT.md` requiring agents to consult the
  PolyU Chinese writing-format PDF before writing or revising Chinese
  footnotes, citations, or bibliographies.
- Recorded the PDF's key conventions for Chinese quotation marks, title marks,
  footnote placement, first/subsequent citations, and bibliography forms.

Files:
- `intro Website/AGENT.md`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Extracted and visually reviewed the nine-page PDF before writing the rule.
- Confirmed the rule preserves unresolved source details instead of inventing
  citation metadata.

Remaining:
- Apply this reference rule to future Chinese citations and bibliography edits.

### 2026-08-04 15:15 HKT — Codex — Complete OCR enlarged-window Chinese references

Summary: Completed the printed OCR citation from the intro-tab source record as `《明清台灣檔案匯編》，第30冊，頁80，硃25。` and converted the handwritten archive and PDF destinations into embedded links on descriptive text. Adjusted the lightbox image height so the full reference remains visible below the enlarged page.

Files changed:
- `intro Website/Website/storymap/storymap.js`
- `intro Website/Website/storymap/storymap.css`
- `PROJECT_LOG.md`

Verified: The local preview shows the printed full reference and the handwritten caption shows clickable `《清代檔案檢索系統》` and `PDF影像` links. Both captions remain visible below the image; `node --check` passes for `storymap.js`.

Remaining: None for the OCR enlarged-window citation display.

### 2026-08-04 15:18 HKT — Codex — Apply Chinese reference-style ordering

Summary: Reordered the handwritten OCR citation to follow the PolyU Chinese reference rule: author, article title, source collection, date, archive number and item, then institution/database and access date. The existing embedded archive and PDF links were retained.

Files changed:
- `intro Website/Website/storymap/storymap.js`
- `PROJECT_LOG.md`

Verified: The citation now begins `黃仕簡，〈奏聞臺灣彰化縣賊匪殺官陷城及奴才辦理赴剿緣由事〉，《宮中檔奏摺—乾隆朝》` and preserves all verified source details.

Remaining: Browser recheck and local checkpoint.

### 2026-08-04 15:28 HKT — Codex — Keep Agentic AI pet size fixed across viewport widths

Summary:
- Changed the Codex pet width and height controls from viewport-relative `clamp()` values to fixed `235px × 256px` values.
- Fixed the terminal-face and body-face font sizes as well, so the robot’s visual scale does not change when the screen width changes.

Files changed:
- `intro Website/Website/storymap/storymap-cards.css`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Browser measurements at 1280px and 800px viewport widths both report `235px × 256px` for the pet and `22px` for the face text.
- No browser errors or warnings were reported.
- Focused `git diff --check` passes for the edited CSS files.

Remaining:
- None for the fixed-size Codex pet update.

### 2026-08-04 15:31 HKT — Codex — Show the complete summary Skill in Write Skills

Summary:
- Replaced the short stage list in the `Write Skills` window with the full source-backed `tool/skills md/quick-summary.md` content.
- The animated window now shows the Skill name, `Kind: summary`, the complete Traditional-Chinese Website Prompt, purpose, distinction from richer schema Skills, and its terminal, website, and proxy usage paths.

Files changed:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- The four Agentic AI data blocks parse successfully; `Write Skills` contains 18 animated lines.
- HTTP browser preview completed all 18 lines with scrolling and reported no browser errors or warnings.
- Focused `git diff --check` passes for the updated StoryMap HTML.

Remaining:
- None for the full summary Skill display.

### 2026-08-04 15:23 HKT — Codex — Remove repeated OCR caption prefix

Summary: Removed the repeated article title, author, sent date, and `第 N 頁` label from both OCR enlarged-image captions. The handwritten and printed source references remain below the image, while the separate page counter and left/right navigation remain available.

Files changed:
- `intro Website/Website/storymap/storymap.js`
- `PROJECT_LOG.md`

Verified: Browser preview captions now show only the source references: the handwritten archive citation and the printed `《明清台灣檔案匯編》，第30冊，頁80，硃25。` entry.

Remaining: Local checkpoint.

### 2026-08-04 15:26 HKT — Codex — Restore title and date inside OCR references

Summary: Added `黃仕簡，〈為奏彰化失陷已調兵赴臺事〉（1786/12/10）` to both OCR source references while keeping the article’s archival citation order and existing embedded links.

Files changed:
- `intro Website/Website/storymap/storymap.js`
- `PROJECT_LOG.md`

Verified: The reference now contains the requested title, author, and Gregorian date without restoring the repeated caption prefix.

Remaining: Browser recheck and local checkpoint.

### 2026-08-04 15:44 HKT — Codex — Add PaddleOCR point-form card and GitHub visual

Summary:
- Converted the three PaddleOCR advantages into the intro website's dash-led point-form list UI.
- Added the supplied `PaddleOCR.png` as a visual box on the left of the PaddleOCR text card, with a linked info panel labelled `PaddleOCR GitHub`.
- Used the visible repository identity in the image (`PaddlePaddle/PaddleOCR`) to link to the canonical GitHub repository.

Files changed:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/Website/storymap/storymap-cards.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- HTTP browser preview shows the visual box on the left, the PaddleOCR text card on the right, three point-form items, and the `PaddleOCR GitHub` link.
- The image path, alt text, GitHub href, three list items, and two-column grid were checked in the live page; no browser errors or warnings were reported.
- Focused `git diff --check` passes for the updated StoryMap files.

Remaining:
- None for the PaddleOCR point-form and visual-link update.

### 2026-08-04 15:52 HKT — Codex — Move PaddleOCR text left and make the visual photo-only

Summary:
- Reversed the PaddleOCR two-column layout so the text card is on the left and the image is on the right.
- Replaced the custom repository visual and `PaddleOCR GitHub` info panel with the StoryMap's standard photo-gallery component, using only the supplied photo and no visible title, description, or source panel.
- Kept the image in `contain` mode so the full screenshot remains visible.

Files changed:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/Website/storymap/storymap-cards.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Browser preview shows the PaddleOCR text card on the left and the photo-only gallery on the right at 1280px width.
- Live-page checks confirm the gallery body is hidden, the image loads from `PaddleOCR.png`, and the gallery JSON contains only one image entry.
- `node --check`, gallery JSON parsing, file existence, and `git diff --check` all pass.

Remaining:
- None for this layout adjustment.

### 2026-08-04 15:57 HKT — Codex — Restore the linked PaddleOCR info panel

Summary:
- Restored the visible info panel beneath the PaddleOCR photo.
- Made the panel text exactly `PaddleOCR GitHub` and embedded the PaddleOCR GitHub URL directly in that label.
- Added a reusable gallery `titleHref` field so linked gallery titles render as accessible links.

Files changed:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/Website/storymap/storymap.js`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Browser preview shows the text card on the left, the photo on the right, and one visible linked info-panel label reading `PaddleOCR GitHub`.
- Live-page checks confirm the label text, GitHub href, image path, and panel visibility; no browser errors or warnings were reported.
- `node --check`, gallery metadata parsing, and `git diff --check` pass.

Remaining:
- None for this panel correction.

### 2026-08-04 16:19 HKT — Codex — Add independent PaddleOCR photo-width control

Summary:
- Added `--paddleocr-photo-width` to control only the PaddleOCR GitHub gallery width in `storymap-cards.css`.
- Made the gallery image stage use the supplied image's 2:1 aspect ratio, so changing the width automatically changes the image height.
- Fixed the text-card track at `74ch`, so adjusting the photo width does not resize the text card on desktop.

Files changed:
- `intro Website/Website/storymap/storymap.css`
- `intro Website/Website/storymap/storymap-cards.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Browser preview reports a 668.9px text card and a 501.0px photo at the default `--paddleocr-photo-width: 42%`; the photo stage ratio is 2.00 and the info panel remains visible.
- Browser preview shows no errors or warnings.
- `node --check` and `git diff --check` pass.

Remaining:
- To resize the photo, edit `--paddleocr-photo-width` in the `#part-3-paddleocr` block.

### 2026-08-04 16:26 HKT — Codex — OCR 明清台灣檔案匯編 30 PDF

Summary:
- Ran PaddleOCR on the specified two-page PDF and created a structured JSON output.
- Preserved the three-row header on printed page 80, page numbers 80 and 81, and the final two 硃批-containing regions on printed page 81.
- Kept raw OCR regions, confidence scores, polygons, and right-to-left vertical-column reading order in the JSON; no researcher correction or silent deletion was applied.

Files changed:
- `intro Website/Website/Visual Material/3.4/明清台灣檔案匯編 30 (dragged).ocr.json`
- `PROJECT_LOG.md`

Verified:
- Rendered and visually inspected both source PDF pages with Poppler.
- PaddleOCR 3.7.0 / PaddlePaddle 3.3.1 completed both pages using `chinese_cht` on CPU.
- JSON parses successfully and reports two pages, header rows, page numbers `80`/`81`, and two preserved 硃批 lines.

Remaining:
- OCR text remains an OCR candidate and should be image-checked before being treated as researcher-confirmed transcription.

### 2026-08-04 16:29 HKT — Codex — Cap PaddleOCR gallery width by Part 3 percentage

Summary:
- Added `--paddleocr-photo-max-width` so the adjustable PaddleOCR GitHub gallery cannot exceed a chosen percentage of the Part 3 width.
- Clamped the gallery against both that percentage cap and the remaining space beside the fixed text card.

Files changed:
- `intro Website/Website/storymap/storymap.css`
- `intro Website/Website/storymap/storymap-cards.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Browser preview reports `--paddleocr-photo-width: 42%`, `--paddleocr-photo-max-width: 60%`, a 2.00 image aspect ratio, and the visible `PaddleOCR GitHub` label.
- `node --check` and `git diff --check` pass.
- Existing concurrent Agentic AI edits remain preserved and uncommitted.

Remaining:
- Change `--paddleocr-photo-width` or `--paddleocr-photo-max-width` in the `#part-3-paddleocr` block to adjust the current width or its maximum.

### 2026-08-04 16:40 HKT — Codex — Fix the invisible Agentic AI × PaddleOCR animation

Summary:
- Fixed the Part 3 Agentic AI × PaddleOCR animation frame so its absolutely positioned windows receive a real inner height.
- Preserved the existing `.visual-frame` height control and the independent window size/position variables.

Files changed:
- `intro Website/Website/storymap/storymap.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Browser geometry now reports a 266.8px visible `.agentic-scene` with rendered PaddleOCR Python and Codex windows; both animation sequences contain generated `.line` elements.
- Browser console reports no errors or warnings.
- `node --check` and `git diff --check` pass.

Remaining:
- None for the visibility bug. Existing concurrent Agentic AI HTML, JavaScript, and card-control edits remain preserved and uncommitted.

### 2026-08-04 16:48 HKT — Codex — Place and enlarge the Agentic AI × PaddleOCR visual

Summary:
- Restored the Part 3 text-card/visual two-column layout, placing the animation on the right of its text card on desktop.
- Added an independently adjustable `--agentic-frame-height` control, enlarged the overlapping windows, and made the animation frame backdrop transparent.
- Added a cache-busting stylesheet version so the updated card controls load reliably after CSS edits.

Files changed:
- `intro Website/Website/storymap/storymap.css`
- `intro Website/Website/storymap/storymap-cards.css`
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Browser geometry reports a 501.9px text column beside a 668.1px visual column; the transparent frame is 665.6px tall and the inner scene is 612.4px tall.
- Both PaddleOCR Python and Codex windows fit within the scene, and the browser console reports no errors or warnings.
- `node --check` and `git diff --check` pass.

Remaining:
- Adjust `--agentic-frame-height` and the window variables in `#part-3-agentic-ocr-chart` if a different desktop composition is preferred. The mobile override keeps the card above the visual.

### 2026-08-04 16:57 HKT — Codex — Make Agentic AI windows clickable and remove the frame border

Summary:
- Removed the border from the transparent Agentic AI × PaddleOCR visual frame.
- Made the whole Codex and PaddleOCR Python windows clickable so the selected window is brought to the front; the exposed title bars remain available when the windows overlap.

Files changed:
- `intro Website/Website/storymap/storymap.css`
- `intro Website/Website/storymap/storymap.js`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Browser reports `0px none` for the frame border and a transparent frame background.
- Clicking the visible `PaddleOCR Python` and `Codex` window labels switches z-index between `3` and `2` as intended.
- Browser console reports no errors or warnings; `node --check` and `git diff --check` pass.

Remaining:
- None for this interaction and frame styling change.

### 2026-08-04 17:00 HKT — Codex — Add Codex working and completed-result phases

Summary:
- Removed the incorrect static `Worked for 10m 1s` text.
- Split the Codex animation into a larger-text working/thinking phase and a completed-result phase.
- When the work phase finishes, it is hidden and only the PaddleOCR installation result remains visible; re-entering the scene starts the work phase again.

Files changed:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.js`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/Website/storymap/storymap-cards.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- During playback, `Working…` is visible, the thinking font computes to `16px`, and the result phase is hidden.
- After completion, the thinking phase is hidden and six result lines are visible; `Worked for 10m 1s` is absent.
- Browser console reports no errors or warnings; `node --check` and `git diff --check` pass.

Remaining:
- None for the Codex phase behavior.

### 2026-08-04 17:11 HKT — Codex — Add Codex completion footer and window transitions

Summary:
- Added `Worked for 5m 44s` to the completed Codex output footer.
- Added linked `PaddleOCR quick start` and `OCR pipeline guide` file items plus four compact Codex/Python/PaddlePaddle/PaddleOCR brand marks.
- Matched the user prompt and output text at `16px` and added card-like transform, opacity, and shadow transitions when switching windows.

Files changed:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.js`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/Website/storymap/storymap-cards.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- During thinking, the footer is hidden, the prompt and thinking text both compute to `16px`, and the result is hidden.
- After completion, the footer displays with the requested duration, two guide links, four logos, and six result lines; the thinking phase is hidden.
- Window switching toggles the front class and z-index for both windows; transitions compute as `transform .32s`, `opacity .24s`, and `box-shadow .32s`.
- Browser console reports no errors or warnings; `node --check` and `git diff --check` pass.

Remaining:
- None for this Codex output-footer and switching transition change.

### 2026-08-04 17:32 HKT — Codex — Simplify the completed Codex output

Summary:
- Removed the Files links, file icons, and four logo marks from the completed Codex state.
- Moved `Worked for 5m 44s` into the result body above the PaddleOCR installation-complete message.
- Kept the working phase free of the completion line and preserved the matching `16px` prompt/output typography.

Files changed:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.js`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- During playback, the result is hidden and `Worked for 5m 44s` is not visible.
- After completion, the result begins with `Worked for 5m 44s`, followed by `PaddleOCR is now installed and verified on your Apple Silicon Mac.`
- No footer, Files links, file icons, or brand-logo elements remain; browser console reports no errors or warnings.
- `node --check` and `git diff --check` pass.

Remaining:
- None for this output simplification.

### 2026-08-04 17:48 HKT — Codex — Remove the Python-code section and expand format guidance

Summary:
- Removed the `執行 OCR 的Python 代碼` section from Part 3.
- Renumbered the following Part 3 OCR sections from 6 through 11.
- Rebuilt `檢視史料的版面及格式` as a no-card, full-width text section matching the research-results presentation.
- Split the content into the requested two paragraphs: using PaddleOCR and checking font/layout characteristics.

Files changed:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap-cards.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Browser confirms `#part-3-code` is absent, `#part-3-format` has two paragraphs, and the title/body article spans the full 1192.97px website content width.
- The format article has transparent background and no border.
- Browser console reports no errors or warnings; `git diff --check` passes.

Remaining:
- None for this Part 3 sequence and full-width text change.

### 2026-08-04 16:59 HKT — Codex — Add book-scanner gallery to OCR materials preparation

Summary:
- Replaced the text-only `OCR 前的材料準備` layout with a two-column card and the shared single-image gallery UI used by `研究清代奏折的主要困難`.
- Added `intro Website/Website/Visual Material/book_scanner_202401.png`, the title `理大圖書館中的掃描器`, a Traditional-Chinese description, and an embedded source link to the PolyU Library book-scanning page.
- Added card CSS controls for gallery width, height, mobile height, image fit, image position, zoom, and expanded-description height.

Files changed:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/Website/storymap/storymap-cards.css`
- `intro Website/Website/Visual Material/book_scanner_202401.png`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Browser loaded the supplied 860×639 PNG and rendered the title, description, source link, and `閱讀更多` gallery behavior.
- Desktop computed layout is a two-column `597.297px 572.625px` card/gallery arrangement with a 620px gallery height.
- Gallery CSS controls compute to `contain`, centered image position, and 1× zoom; the official PolyU source URL is present in the link.
- Gallery JSON parses successfully, the image asset exists, `node --check` passes, and `git diff --check` passes.

Remaining:
- None for this requested gallery addition.

### 2026-08-04 17:46 HKT — Codex — Style the materials copyright note

Summary:
- Marked the copyright and database-terms reminder in `OCR 前的材料準備` as a separate note.
- Styled it as smaller orange text without changing the wording or the other body paragraph.

Files changed:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap-cards.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Browser computes the note as `rgb(196, 93, 56)`, 12px, weight 600, with the original Traditional-Chinese text intact.
- `node --check` and `git diff --check` pass.

Remaining:
- None for this styling adjustment.

### 2026-08-04 19:46 HKT — Codex — Make Part 3.7 backdrop white

Summary:
- Changed the `辨識印刷字` section backdrop from the shared beige `surface-c` color to white.
- Used a higher-specificity card CSS override so the shared Part 3 surface rule cannot replace it.

Files changed:
- `intro Website/Website/storymap/storymap-cards.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Browser computes `#part-3-printed` background as `rgb(255, 255, 255)` while the title and interactive explorer remain present.
- `node --check` and `git diff --check` pass.

Remaining:
- None for this backdrop adjustment.

### 2026-08-05 12:58 HKT — Codex — Expand Part 3.8 handwritten-text body

Summary:
- Expanded only the `辨識手寫字` article and body paragraph to the full website content width.
- Left Part 3.7 `辨識印刷字` and the handwritten interactive explorer unchanged.

Files changed:
- `intro Website/Website/storymap/storymap-cards.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Browser computes the Part 3.8 article, body, and paragraph at `1192.97px`, matching the website content width.
- The handwritten explorer remains present below at `1152px`.
- `node --check` and `git diff --check` pass.

Remaining:
- None for this Part 3.8 width adjustment.

### 2026-08-05 13:09 HKT — Codex — Enhance OCR handwritten page clarity

Summary:
- Created clearer, higher-resolution versions of the four `硃25` handwritten OCR pages while preserving the archival page composition, text, annotations, seals, watermark, and paper texture.
- Saved the originals unchanged and updated the live StoryMap OCR animation and Part 3 feature data to use the enhanced assets.

Files changed:
- `intro Website/Website/storymap/ocr-zhu25-handwritten-1-enhanced.png`
- `intro Website/Website/storymap/ocr-zhu25-handwritten-2-enhanced.png`
- `intro Website/Website/storymap/ocr-zhu25-handwritten-3-enhanced.png`
- `intro Website/Website/storymap/ocr-zhu25-handwritten-4-enhanced.png`
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Browser loads `ocr-zhu25-handwritten-1-enhanced.png` at `1466×1073` from the updated gallery path.
- All four enhanced files exist and the gallery metadata references the enhanced filenames.
- The enhanced outputs were visually inspected for clearer ink edges, page texture, red annotations, seals, watermark, and margins.

Remaining:
- The original four page images remain available under their original filenames for comparison or rollback.

### 2026-08-05 13:20 HKT — Codex — Enhance OCR printed page clarity

Summary:
- Created clearer, higher-resolution versions of the two `硃25` printed OCR pages while preserving the printed characters, headings, page numbers, margins, and clean page composition.
- Saved the originals unchanged and updated the live StoryMap OCR animation and Part 3 printed-text panel to use the enhanced assets.

Files changed:
- `intro Website/Website/storymap/ocr-zhu25-printed-1-enhanced.png`
- `intro Website/Website/storymap/ocr-zhu25-printed-2-enhanced.png`
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Browser loads `ocr-zhu25-printed-1-enhanced.png` at `995×1580` in both the OCR animation and the Part 3 printed-text panel.
- The OCR page list references both enhanced printed assets.
- The enhanced outputs were visually inspected for sharper type edges, preserved headings, page numbers, margins, and page layout.

Remaining:
- The original two printed page images remain available under their original filenames for comparison or rollback.

### 2026-08-04 16:40 HKT — Codex — Clear OCR JSON data at user request

Summary:
- Replaced the contents of the derived OCR JSON with an empty JSON object `{}`.
- Kept the source PDF and OCR script unchanged; the previous OCR JSON remains recoverable from local commit `0c63cf2`.

Files changed:
- `intro Website/Website/Visual Material/3.4/明清台灣檔案匯編 30 (dragged).ocr.json`
- `PROJECT_LOG.md`

Verified:
- The cleared file parses as valid JSON and contains `{}`.
- No source PDF or unrelated StoryMap file was changed by this action.

Remaining:
- Regenerate the OCR JSON with the saved OCR code if the extracted data is needed again.

### 2026-08-04 16:49 HKT — Codex — Re-OCR PDF with paragraph-preserving JSON

Summary:
- Added a reusable PaddleOCR Python script under `tool/scripts py/ocr_pdf_paragraphs.py`.
- Re-OCRed the two-page PDF and regenerated the JSON with one object per source paragraph.
- Kept paragraph 1 across the page break from `竊照` through `等情前來。`, paragraph 2 from `查，奴才原擬` through `謹奏。`, plus all raw OCR regions, header rows, page numbers, and 硃批 lines.

Files changed:
- `tool/scripts py/ocr_pdf_paragraphs.py`
- `intro Website/Website/Visual Material/3.4/明清台灣檔案匯編 30 (dragged).ocr.json`
- `PROJECT_LOG.md`

Verified:
- Python compilation passed.
- OCR completed using PaddleOCR 3.7.0 / PaddlePaddle 3.3.1 with `chinese_cht` on CPU.
- JSON parses successfully with schema version `2.0`, two paragraph parts, and all 31 raw OCR regions retained.
- Source PDF pages were rendered and visually inspected before paragraph grouping.

Remaining:
- The paragraph text remains OCR evidence and should be image-checked before researcher-confirmed transcription.

### 2026-08-04 16:58 HKT — Codex — Add function-purpose comments to OCR script

Summary:
- Added `#` comments naming the function of each major function in the paragraph-preserving OCR script.

Files changed:
- `tool/scripts py/ocr_pdf_paragraphs.py`
- `PROJECT_LOG.md`

Verified:
- Python compilation passed.
- Comments are limited to function-purpose labels; OCR behavior and output format are unchanged.

Remaining:
- None for this documentation-only adjustment.

### 2026-08-04 17:04 HKT — Codex — Reshape OCR JSON into readable document sections

Summary:
- Changed the OCR output to expose a three-row header, sentence-by-sentence paragraph parts, a separate final-two-line 硃批 area, page numbers, and footer date.
- Kept raw OCR pages and source-region references for traceability; removed the inline 硃批 annotation from paragraph display sentences while retaining its source region.

Files changed:
- `tool/scripts py/ocr_pdf_paragraphs.py`
- `intro Website/Website/Visual Material/3.4/明清台灣檔案匯編 30 (dragged).ocr.json`
- `PROJECT_LOG.md`

Verified:
- Python compilation passed.
- OCR regenerated successfully with schema version `3.0`, 2 paragraphs, 16 and 6 sentences, 2 page numbers, 2 硃批 lines, and all 31 raw OCR regions.
- Source PDF pages were re-rendered and visually inspected.

Remaining:
- The text remains OCR evidence and should be image-checked before researcher-confirmed transcription.

### 2026-08-05 16:12 HKT — Codex — Increase transparency of handwritten folded bars

Summary:
- Reduced the opacity of collapsed `.part3-fx-panel` bars to `0.56`, affecting the folded bars on either side while leaving the two open scanned pages unchanged.
- Refreshed the StoryMap CSS cache key so the opacity adjustment loads immediately.

Files changed:
- `intro Website/Website/storymap/storymap.css`
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Browser preview shows the `辨識手寫字` visual with 10 collapsed panels at computed opacity `0.56`.
- The visual remains visible and the browser reports no console errors or warnings.
- `git diff --check` passes.

Remaining:
- None for the folded-bar transparency adjustment.

### 2026-08-05 13:48 HKT — Codex — Rework Part 3 printed-text feature guidance

Summary:
- Replaced the printed-text explorer labels with `文本資訊`, `橫排單欄`, `分段`, `頁碼`, `標題符號`, `夾批`, and `落款與尾批`.
- Rewrote the paired feature descriptions, AI prompts, Python snippets, and JSON examples around 《明清臺灣檔案彙編》 metadata, right-to-left single-column reading, indentation-based paragraphs, page-number capture, title-symbol review, inline emperor 硃批, and separate footer dates.
- Added matching per-feature label and highlight coordinate overrides; preserved the handwritten explorer because its requested replacements were not specified.

Files changed:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap-cards.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Embedded Part 3 JSON parses; the printed explorer has seven requested features and no old unrequested labels.
- Browser verification passed for first-page labels, page-two `夾批`, `落款與尾批`, highlight changes, and handwritten-section preservation.
- `node --check`, `git diff --check`, and browser console error checks pass.

Remaining:
- Provide a separate handwritten feature replacement list before changing `辨識手寫字`.

### 2026-08-05 13:54 HKT — Codex — Remove Part 3 page badges and reposition printed 硃批 labels

Summary:
- Removed the `p.2` suffix from off-page Part 3 feature labels.
- Moved the printed `夾批` and `落款與尾批` labels to the left side of the document explorer.
- Updated the StoryMap JavaScript cache key to ensure the revised label renderer is loaded.

Files changed:
- `intro Website/Website/storymap/storymap.js`
- `intro Website/Website/storymap/storymap-cards.css`
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Page-two labels render without page badges and both computed to the left side.
- JavaScript syntax, `git diff --check`, and browser console checks pass.

Remaining:
- None for this label adjustment.

### 2026-08-05 15:19 HKT — Codex — Separate handwritten labels to prevent overlap

Summary:
- Re-spaced the handwritten labels on both sides so labels from different pages do not occupy the same vertical position.
- Refreshed the CSS cache key after the position adjustment.

Files changed:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap-cards.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Browser reports zero intersecting label rectangles.
- Labels display without `第 x 摺` text and without console errors.

Remaining:
- None for this label adjustment.

### 2026-08-05 14:00 HKT — Codex — Preserve handwritten fold indicators while removing printed page badges

Summary:
- Kept the printed explorer free of `p.2` suffixes while preserving handwritten fold indicators such as `第 4 摺`.
- Bumped the StoryMap JavaScript cache key and rechecked both explorers in the local browser.

Files changed:
- `intro Website/Website/storymap/storymap.js`
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Printed labels have no page suffixes; handwritten labels retain fold numbers.
- `夾批` and `落款與尾批` compute on the left side, with no browser console errors.

Remaining:
- None for this correction.

### 2026-08-05 14:04 HKT — Codex — Remove the remaining printed page suffix

Summary:
- Confirmed that printed Part 3 labels should use plain feature names with neither `p.1` nor `p.2`.
- Refreshed the StoryMap script cache key so the browser loads the no-badge renderer consistently.
- Preserved handwritten fold indicators such as `第 4 摺` and the existing left-side placement of `夾批` and `落款與尾批`.

Files changed:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Browser output: printed labels are `文本資訊`, `直排單欄`, `分段`, `頁碼`, `標題符號`, `夾批`, and `落款與尾批`, with no page suffix.
- Handwritten labels retain their fold indicators.
- Browser console has no errors or warnings.

Remaining:
- None for this label adjustment.

### 2026-08-05 14:37 HKT — Codex — Add source-text samples to printed OCR JSON

Summary:
- Added short original-text excerpts to the OCR JSON windows for `直排單欄`, `分段`, and `標題符號`.
- Used source wording from the OCR evidence so the examples demonstrate reading order, paragraph grouping, and punctuation in context.
- Refreshed the StoryMap script cache key for the updated JSON windows.

Files changed:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- The embedded data for the three feature windows contains the new original-text samples in their JSON panels.
- The embedded page data remains valid, JavaScript syntax passes, and diff whitespace checks pass.

Remaining:
- The displayed excerpts remain OCR evidence and should not be treated as researcher-confirmed transcription without image checking.

### 2026-08-05 15:07 HKT — Codex — Rework handwritten OCR feature labels

Summary:
- Removed `首行「奏為奏聞事」`, `摺縫`, and the old combined seal feature.
- Added `正文字體`, `上奏官員`, `浮水印`, and `印章`; revised `直排單欄`, `臣字款`, `抬頭`, and `硃批（草書）` guidance.
- Assigned the features to the requested first, third, and sixth pages and placed their labels on the requested left or right sides.

Files changed:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap-cards.css`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Handwritten labels now render as `直排單欄`, `正文字體`, `上奏官員`, `臣字款`, `抬頭`, `硃批`, `浮水印`, and `印章`.
- Feature data contains matching AI prompts, Python examples, and OCR JSON output; removed feature keys are absent.
- Browser placement checks and console checks pass.

Remaining:
- OCR guidance remains a teaching example; the scan should still be image-checked before treating extracted text as confirmed transcription.

### 2026-08-05 15:18 HKT — Codex — Remove fold numbers from handwritten labels

Summary:
- Removed the `第 x 摺` badge text from handwritten Part 3 labels.
- Kept the feature names and their page/side positions unchanged.
- Refreshed the StoryMap script cache key.

Files changed:
- `intro Website/Website/storymap/storymap.js`
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Handwritten labels display only `直排單欄`, `正文字體`, `上奏官員`, `臣字款`, `抬頭`, `硃批`, `浮水印`, and `印章`.
- Printed labels remain without page badges.
- JavaScript syntax and browser console checks pass.

Remaining:
- None for this label adjustment.

### 2026-08-05 15:22 HKT — Codex — Map features to website pages

Summary:
- Corrected the handwritten feature assignments to use the website's six accordion pages rather than PDF pages or individual scan subparts.
- Kept page 1 features on panels 0–1, moved `抬頭` and `硃批（草書）` to website page 3, and moved `浮水印` and `印章` to website page 6.

Files changed:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Browser indicators progress through `頁 1 / 6` to `頁 6 / 6`.
- Feature mapping resolves to website pages 1, 3, and 6 as requested; labels remain non-overlapping and contain no fold-number text.

Remaining:
- None for this page-mapping adjustment.

### 2026-08-05 15:30 HKT — Codex — Remove JSON field names from handwritten guidance

Summary:
- Removed explicit JSON field and column names from the handwritten Part 3 版面特徵 and AI Prompt text only.
- Preserved the user's current handwritten feature adjustments and left the Python and OCR JSON examples unchanged.

Files changed:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- The rendered handwritten feature data contains no technical field names in any `desc` or `prompt` value.
- All eight handwritten labels remain visible without overlap, and the browser reports no errors or warnings.

Remaining:
- The OCR examples remain instructional evidence and should still be checked against the scanned images before being treated as confirmed transcription.

### 2026-08-05 15:39 HKT — Codex — Add source-text samples to printed OCR features

Summary:
- Replaced the printed-feature JSON keys `text_sample` and `paragraph_samples` with direct `text` and `paragraphs` entries.
- Added the source sequence beginning with `福建水師提督…`, followed by two paragraph samples under `分段`; each displayed sample shows four sentences followed by `……`.
- Added original punctuation-bearing text to `標題符號` while preserving the existing OCR guidance.

Files changed:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Browser-rendered printed feature data contains no `_sample` keys in the three requested features.
- The live page shows the expected source text and printed labels without console errors or warnings.

Remaining:
- The displayed excerpts remain source-text teaching examples and should be checked against the scanned page when used as evidence.

### 2026-08-05 15:56 HKT — Codex — Add source-text examples to handwritten OCR features

Summary:
- Added direct source text under `text` in the handwritten `直排單欄` and `正文字體` JSON windows.
- Used the same four-sentence source excerpt followed by `……`, without changing the existing handwritten layout and script metadata.

Files changed:
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Browser-rendered handwritten features contain the new text examples and ellipsis.
- The live page reports no console errors or warnings.

Remaining:
- The handwritten excerpt remains an OCR teaching example and should be checked against the scan before being treated as confirmed transcription.

### 2026-08-05 16:05 HKT — Codex — Arrange handwritten labels in one right-side sequence

Summary:
- Repositioned all handwritten Part 3 labels to the right side in the requested order: `直排單欄`, `正文字體`, `上奏官員`, `臣字款`, `抬頭`, `硃批`, `浮水印`, `印章`.
- Refreshed the StoryMap CSS cache key so the new label positions load immediately.

Files changed:
- `intro Website/Website/storymap/storymap-cards.css`
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Browser geometry shows all eight handwritten labels on the right with no overlap.
- Browser console reports no errors or warnings.

Remaining:
- At narrow widths, the existing responsive layout continues to place labels in the normal tag row.

### 2026-08-05 16:09 HKT — Codex — Move later handwritten labels to the left

Summary:
- Kept `直排單欄`, `正文字體`, `上奏官員`, and `臣字款` on the right.
- Moved `抬頭`, `硃批`, `浮水印`, and `印章` to the left in their existing vertical sequence.
- Refreshed the StoryMap CSS cache key.

Files changed:
- `intro Website/Website/storymap/storymap-cards.css`
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- Browser geometry confirms the two-sided label arrangement has no overlap.
- Browser console reports no errors or warnings.

Remaining:
- At narrow widths, the existing responsive layout continues to place labels in the normal tag row.

### 2026-08-05 16:13 HKT — Codex — Widen Part 3.7 and 3.8 feature boxes

Summary:
- Increased the combined visual-plus-text box width for `辨識印刷字` and `辨識手寫字` from 90vw to 96vw.
- Refreshed the StoryMap CSS cache key while keeping the two-column visual/text balance unchanged.

Files changed:
- `intro Website/Website/storymap/storymap-cards.css`
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/INTRO_WEBSITE_CHANGE_LOG.md`
- `PROJECT_LOG.md`

Verified:
- At a 1280px desktop viewport, both feature boxes render at 1228.8px wide with equal visual and text columns.
- Browser console reports no errors or warnings.

Remaining:
- The existing responsive breakpoint continues to stack the two columns on narrow screens.

### 2026-08-04 18:10 HKT — Codex — OCR npmpdf-2 with watermark and red-ink filtering

Summary:
- Added `tool/scripts py/ocr_filtered_pdf.py` for landscape archival scans.
- OCRed `npmpdf-2.pdf` in right-to-left, top-to-bottom column order.
- Filtered the 國立故宮博物院 / NATIONAL PALACE MUSEUM watermark, red handwritten/red-ink OCR, and the scanner calibration strip.

Files changed:
- `tool/scripts py/ocr_filtered_pdf.py`
- `intro Website/Website/Visual Material/3.4/npmpdf-2.ocr.json`
- `PROJECT_LOG.md`

Verified:
- Python compilation passed.
- JSON parses successfully with 4 pages and no watermark, calibration-label, or red-handwriting text in the page output.
- The final pass kept the printed text overlapping the page-2 red annotation.
- All four source PDF pages were rendered and visually inspected.

Remaining:
- The text remains OCR evidence and should be image-checked before researcher-confirmed transcription.

### 2026-08-04 17:36 HKT — Codex — Simplify JSON to paragraph-and-sentence text arrays

Summary:
- Changed each paragraph to a plain object with `paragraph_number`, `printed_pages`, and a `sentences` array of text strings.
- Changed the header and 硃批 area to plain text arrays and kept technical region metadata out of the visible JSON.

Files changed:
- `tool/scripts py/ocr_pdf_paragraphs.py`
- `intro Website/Website/Visual Material/3.4/明清台灣檔案匯編 30 (dragged).ocr.json`
- `PROJECT_LOG.md`

Verified:
- Python compilation passed.
- OCR completed successfully with schema version `5.0`.
- JSON contains 2 paragraph objects with 16 and 6 plain sentence strings, plus the header, page numbers, 硃批 lines, and footer date.
- Source PDF pages were re-rendered and visually inspected.

Remaining:
- The text remains OCR evidence and should be image-checked before researcher-confirmed transcription.

### 2026-08-04 17:10 HKT — Codex — Remove region-by-region fields from visible OCR JSON

Summary:
- Removed region objects, boxes, confidences, and raw page-region arrays from the saved JSON presentation.
- Kept the readable header, paragraph sentences, 硃批 area, page numbers, and footer date with page-level references only.

Files changed:
- `tool/scripts py/ocr_pdf_paragraphs.py`
- `intro Website/Website/Visual Material/3.4/明清台灣檔案匯編 30 (dragged).ocr.json`
- `PROJECT_LOG.md`

Verified:
- Python compilation passed.
- OCR regenerated with schema version `4.0`.
- JSON contains no `region_index`, `box`, `confidence`, `regions`, `source_region`, or `raw_ocr_pages` fields.
- The two source PDF pages were re-rendered and visually inspected.

Remaining:
- The text remains OCR evidence and should be image-checked before researcher-confirmed transcription.

### 2026-08-05 16:13 HKT — Claude — Add real JSON viewer to "9. 輸出格式：JSON"

Summary:
- Drafted and applied a VS Code–style JSON viewer to `#part-3-json` in the intro website, replacing the abstract schema-field toggle diagram. Shows a simplified, real 8-field JSON for 硃25 (source, title, official_post, author, sent_date, zhu_date, zhu_text, page_numbers, paragraphs with 3 entries), all verbatim from the dataset.
- Label toolbar sits outside/above the window (not in the titlebar); each button is a JSON field's Chinese name and scrolls/flashes the matching line via `initJsonViewer()` in storymap.js.
- Paragraph 2 (段落二) truncates after "...罪惡至此已極，殊堪痛恨。" with a single toggle button that reads "..." when collapsed and "收合" when expanded.
- Removed the leftover descriptive paragraph below the window per user request.
- Sizing/position controls documented and exposed in storymap-cards.css (`--json-labels-gap`, `--json-label-font-size`, `--json-body-h`, `--json-body-font-size`).

Files changed:
- `intro Website/Website/UI Idea/20-json-output-viewer-draft.html` (draft, iterated through several rounds before approval)
- `intro Website/Website/storymap/storymap-example.html`
- `intro Website/Website/storymap/storymap.css`
- `intro Website/Website/storymap/storymap.js`
- `intro Website/Website/storymap/storymap-cards.css`
- `PROJECT_LOG.md`

Verified:
- Brace/tag balance checks passed for all four storymap files (Python brace count, div/span/button tag count) and the draft HTML.
- `node --check storymap.js` passed.
- All JSON field values cross-checked against `review-tools/shared data/stage1_original_text.json` and `Visual Material/3.4/明清台灣檔案匯編 30 (dragged).ocr.json` — no invented content.

Remaining:
- Local git commit for these files not yet made.
