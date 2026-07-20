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

### 2026-07-20 19:28 — Codex — Added pair-grounded official-loop proxy contracts

Summary: Defined the official-document-centred review loop and added Gemini-proxy modes that analyze existing pair edges without re-searching the corpus.

Changed:
- Added `confirmed_yu_response` to explain how an official document answers already-confirmed earlier 上諭.
- Added `combined_emperor_actions` to merge equivalent 硃批 and paired-上諭 expressions into multi-source emperor actions and compare them with earlier emperor actions.
- Added a `confirmed_pairs_only` path to the existing official-response mode.
- Added canonical skill specifications for the new loop and its two new analysis stages.

Files:
- `tool/proxy/gemini-proxy/main.py`
- `tool/skills md/confirmed-yu-response-analysis.md`
- `tool/skills md/combine-confirmed-emperor-actions.md`
- `tool/skills md/official-document-review-loop.md`
- `tool/skills md/official-response.md`

Verified:
- `main.py` passes Python bytecode compilation.
- Confirmed-pair data provides the required `official_reply_to_yu` and `yu_source` graph directions.
- Runtime endpoint smoke testing remains pending because the local workspace runtime does not currently include the proxy's Flask/Google dependencies.

Remaining:
- Wire the new graph-grounded stages into both review UIs, add the one-click official-document loop, update the workflow map, and run browser/JavaScript parity checks.

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

### 2026-07-20 18:45 HKT — Codex — Unhid the click-network settings button

Summary: Moved `點擊後顯示範圍` out of the closed Tools popover and into the
always-visible main toolbar in both formal and sample UIs. It still opens the
same lane-first network settings panel, while the connection opacity sliders
remain under Tools.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Embedded JavaScript parsed successfully in both HTML files.
- Each HTML file has exactly one network-settings button in the main toolbar.
- `git diff --check` passed.

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

### 2026-07-20 16:31 HKT — Codex — Replace document-info summary/table filters with reviewed AI-output labels (formal + sample)

Summary:
- Replaced the document-info filter's legacy embedded-summary collector with a collector over saved, quoted AI-chat output, covering event extraction categories, source chains, official responses, timing checks, 硃批／上諭 outputs, information sources, consolidation, 上諭 review-loop outputs, emperor actions, and document-pair evidence.
- Added Traditional Chinese filter labels, including `清軍事：已執行`, `清軍事：待執行`, `清方：非軍事`, `上諭回應的奏折`, `回應的先前上諭`, and `回應的先前硃批`; removed the old 摘要 label path and the document-info table/AI-original toggles.
- Applied the equivalent change to both HTML tools and preserved the document metadata table and raw source data.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Embedded JavaScript parsed successfully: 5 scripts in formal and 6 in sample.
- `git diff --check` passed.
- Browser-loaded both local pages, opened a document panel in each, and confirmed no legacy table, page toggle, AI-original toggle, overall-summary pane, summary table, or old visible pair labels; browser error logs were empty.

Remaining:
- Human confirmation of the final Chinese label wording and visual grouping in the real research workflow.

### 2026-07-20 16:35 HKT — Codex — Expanded header search results with matching excerpts (formal + sample)

Summary:
- Removed the 60-result render cap and the old 「僅顯示前 60 筆」 notice; the dropdown now renders the complete matching set and keeps the copy-all action over all matches.
- Added a second, centered source-text line for every result. It shows the first matching occurrence, highlights the query in red, and appends the document-level occurrence count.
- Added a readable original-source index while preserving the existing lowercase search index, so timeline filtering behavior remains unchanged.

Files:
- review-tools/(1) formal/index.html
- review-tools/(2) sample/index.html
- PROJECT_LOG.md

Verified:
- Embedded JavaScript parsed successfully in both HTML files.
- git diff --check passed.
- Browser-tested both local pages with 常: each rendered 256 result rows, no old limit notice, a second excerpt line, red .search-hit text, and a scrollable dropdown containing all rows.
- Formal and sample search-dropdown blocks are identical.

Remaining:
- Human confirmation of the excerpt wording and spacing in the real research workflow.

### 2026-07-20 16:47 HKT — Codex — Simplify document-info body and segmented-part presentation (formal + sample)

Summary:
- Made the saved division view the only active document-info body filter by default when divisions exist; other annotation groups remain available through the filter control.
- Renamed both plain and segmented body headings to `原文` and removed the separate bottom `硃批 rescript` block.
- Removed the segmented-part left rail and its green hover behavior, made the outer body surface transparent, and gave each part its own surface with 28px spacing.
- Reduced the default segmented-part subtitle size to 12px.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Embedded JavaScript parsed successfully: 5 scripts in formal and 6 in sample.
- `git diff --check` passed.
- Browser-loaded both local pages, opened document panels, confirmed `原文` is the only body heading, confirmed no separate rescript block or legacy summary/table panes, and found no browser console errors.
- Confirmed the renderer/CSS rules are synchronized in both files for the default division state, independent part surfaces, removed hover rail, larger inter-part spacing, and smaller subtitles.

Remaining:
- Human confirmation of the segmented-card spacing in a saved-division document with the research data loaded.

### 2026-07-20 16:52 HKT — Codex — Scope pair filters by document type (formal + sample)

Summary:
- Hid `上諭回應的奏折` AI-output filters from official documents (`硃批` and `上奏`).
- Hid `回應的先前上諭` from 上諭 documents, where that response relationship is not applicable.
- Kept the underlying saved AI-chat output intact; this change only controls document-info filter visibility and highlights.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Embedded JavaScript parsed successfully: 5 scripts in formal and 6 in sample.
- `git diff --check` passed before the log update.
- Browser-loaded both local pages, opened document panels, confirmed no pair labels appeared in the available blank preview state, and found no browser console errors.
- Confirmed the same document-type filtering rules are present in both HTML files.

Remaining:
- Human confirmation with the full saved AI pair outputs loaded in the research workflow.

### 2026-07-20 17:03 HKT — Codex — Refine document-type filter visibility for AI/event projections (formal + sample)

Summary:
- For `硃批` and `上奏`, hid `相關上諭`, `回應時效`, `事件整合`, and `皇帝行動` filter groups, in addition to the previously hidden 上諭-pair group.
- For 上諭, hid `事件整合` and `回應的先前上諭`, while retaining `皇帝行動` items whose source is the 上諭.
- Applied the visibility rule after combining saved AI items and event projections, so excluded groups cannot reappear through either path.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Embedded JavaScript parsed successfully: 5 scripts in formal and 6 in sample.
- `git diff --check` passed.
- Browser-loaded both local pages, opened document panels, confirmed the new logic produced no runtime errors, and found no forbidden pair labels in the available blank preview state.
- Confirmed the same final-list visibility rules are present in both HTML files.

Remaining:
- Human confirmation with the complete saved AI/event outputs loaded in the research workflow.

### 2026-07-20 17:03 HKT — Codex — Refined header people/search filters and result controls (formal + sample)

Summary:
- Removed the （等） suffix from every 人物 option and normalized filtering so the bare-name options still match the underlying records.
- Changed header search and timeline filtering to search field values only; serialized JSON property names such as volume are no longer searchable.
- Moved the result count and controls above the full result list, added a document-type filter, and changed 複製全部編號 to a copy-symbol button that copies the currently filtered results.
- Kept only the first matching excerpt and now show the occurrence count when a document has more than one match.

Files:
- review-tools/(1) formal/index.html
- review-tools/(2) sample/index.html
- PROJECT_LOG.md

Verified:
- Embedded JavaScript parsed successfully: 5 scripts in formal and 6 in sample.
- git diff --check passed.
- Browser-tested both pages: 人物 options contain no （等）; volume returns 0 筆符合; 常 shows the top result header, all document types, red hits, and multi-match counts; selecting 硃批 shows 110 rows and only 硃 badges.
- Formal and sample search blocks are identical.

Remaining:
- Human confirmation of the final header spacing and labels in the full research workflow.

### 2026-07-20 17:13 HKT — Codex — Added reviewed summary card above 原文 (formal + sample)

Summary:
- Added a separate 摘要 card at the top of each document-info body, before 原文.
- The card reads saved reviewed summary output (`overallAdj` first, then structured 摘要 output or saved summary responses) and does not use the legacy embedded `r.summary` table.
- Kept the card out of the filter chips and hid it when no reviewed summary output exists.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Embedded JavaScript parsed successfully: 5 scripts in formal and 6 in sample.
- `git diff --check` passed.
- Browser-tested both local pages, opened document panels, confirmed the `ix-summary` container precedes `ix-cols`, the body label is 原文, and no separate 硃批/rescript block is rendered; no browser errors were reported.

Remaining:
- Human confirmation with the complete saved reviewed-summary outputs loaded in the research workflow.

### 2026-07-20 17:20 HKT — Codex — Center search excerpts and preserve visible match counts (formal + sample)

Summary:
- Replaced the fixed search excerpt radius with a responsive excerpt limit based on the dropdown width and interface font size.
- Kept early matches in a balanced clause-sized excerpt, so searching 二 now shows 為奏聞事。本年十二月初九日接提臣黃仕簡 with the match centered rather than starting at the document header.
- Moved multi-match counts outside the clipped excerpt text so counts such as (9) remain visible whenever a document has more than one match.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Embedded JavaScript parsed successfully: 5 scripts in formal and 6 in sample.
- `git diff --check` passed.
- Browser-tested both pages with 二: 363 rows, centered target excerpt, visible (9), and identical output.
- Rechecked volume as 0 筆符合, 常 as 256 筆符合 with 138 multi-match counts and red hits, and no browser console errors.
- Confirmed the search JavaScript and CSS blocks remain identical between formal and sample.

Remaining:
- Human confirmation of final search excerpt spacing in the full research workflow.

### 2026-07-20 17:25 HKT — Codex — Avoid forced centering at excerpt boundaries (formal + sample)

Summary:
- Center the first matching word only when the responsive excerpt window has enough source text before and after it.
- Keep matches near the beginning or end anchored naturally to the available text instead of forcing a centered clause.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Embedded JavaScript parsed successfully: 5 scripts in formal and 6 in sample.
- `git diff --check` passed.
- Browser-tested both pages with 二: the early 硃26 match is naturally anchored at the beginning, while a separate result still centers when both sides have enough text; multi-match counts remain visible.
- Rechecked volume as 0 筆符合 in both pages and found no browser console errors.

Remaining:
- Human confirmation of the final boundary behavior in the full research workflow.

### 2026-07-20 17:31 HKT — Codex — Lighten search example sentences (formal + sample)

Summary:
- Changed the search dropdown's second-line sentence to a lighter theme-aware colour.
- Preserved the red matching word and readable multi-match count styling.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Embedded JavaScript parsed successfully: 5 scripts in formal and 6 in sample.
- `git diff --check` passed.
- Browser-tested both pages with 二: 363 rows, lighter sentence text, red hit, visible counts, and no browser console errors.

Remaining:
- Human confirmation of the final search text contrast in the full research workflow.

### 2026-07-20 17:23 HKT — Codex — Made 原文 editing inline (formal + sample)

Summary:
- Replaced the old click-to-textarea original-text editor with an inline `contenteditable` editor at the exact 原文 location.
- Wrapped each divided source segment in its own inline editor while keeping division titles and summaries as their existing inline editors.
- Saved edited source text on focusout, excluding annotation notes and generated superscript numbers from the stored body text.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Embedded JavaScript parsed successfully in both HTML files.
- `git diff --check` passed.
- Browser-tested both local pages: each document panel has a `contenteditable` `.body-inline-edit`, no `.ip-bodyedit` textarea is created, and no browser warnings or errors were reported.

Remaining:
- Human confirmation of caret placement and editing feel with the complete saved research state.

### 2026-07-20 17:31 HKT — Codex — Matched document-panel headings and division-card styling

Summary:
- Matched the `摘要` and `原文` headings in font family, size, weight, line height, letter spacing, colour, and alignment in both review UIs.
- Changed each division-of-part card to a white surface with only the thin brown border used by the summary card; removed the card shadow and hover border variation.
- Preserved a readable light-gold heading colour in dark mode.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Embedded JavaScript parsed successfully in both HTML files.
- `git diff --check` passed.
- Browser-tested the document-panel styling path and finalized the browser check without console errors.

Remaining:
- Human confirmation of the final visual treatment in the full saved research state.

### 2026-07-20 17:35 HKT — Codex — Enlarged division subtitles

Summary:
- Increased the subtitle text beneath each division-of-part title from its compact default to `14px` with a more readable line height.
- Applied the same rule to the formal and sample review UIs.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Embedded JavaScript parsed successfully in both HTML files.
- `git diff --check` passed.
- Browser smoke check completed for both local pages without console errors.

Remaining:
- Human confirmation of the subtitle size in the full saved research state.

### 2026-07-20 17:39 HKT — Codex — Aligned summary and division-card geometry

Summary:
- Standardized the summary card's inner padding to match each division card's `14px` horizontal inset.
- Kept the `摘要` heading aligned to the shared outer edge while aligning summary text and division subtitles to the same inner text start.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Embedded JavaScript parsed successfully in both HTML files.
- `git diff --check` passed.
- Browser-loaded the sample UI and confirmed the alignment rules are present; no populated document was selected in the smoke view.

Remaining:
- Human confirmation of the final visual alignment in the full saved research state.

### 2026-07-20 17:41 HKT — Codex — Rebalanced division title and summary sizes

Summary:
- Made each division title moderately larger (`16px`) so it is the largest text within its part.
- Reduced the summary line below it to a still-readable `12.5px`, keeping the main source text between the two sizes.
- Applied the same hierarchy to formal and sample UIs.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Embedded JavaScript parsed successfully in both HTML files.
- `git diff --check` passed.
- Browser-loaded the sample UI and confirmed the final `.seg-label`/`.seg-summary` rules are present.

Remaining:
- Human confirmation of the final text hierarchy in the full saved research state.

### 2026-07-20 17:44 HKT — Codex — Reduced division summaries and padded 摘要 heading

Summary:
- Reduced each division summary line to `12px` so it remains the smallest text in the part without becoming too small.
- Removed the negative left offset from `摘要`, restoring the card's normal inner padding so the heading no longer touches the border.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Embedded JavaScript parsed successfully in both HTML files.
- `git diff --check` passed.

Remaining:
- Human confirmation of the final spacing and text hierarchy in the full saved research state.

### 2026-07-20 17:46 HKT — Codex — Aligned 原文 with the summary subtitle inset

Summary:
- Added the same `14px` left inset to the `原文` heading used by the summary subtitle and division subtitles.
- Applied the adjustment to both formal and sample UIs.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Embedded JavaScript parsed successfully in both HTML files.
- `git diff --check` passed.

Remaining:
- Human confirmation of the final heading alignment in the full saved research state.

### 2026-07-20 18:21 HKT — Codex — Exported verified sample 上諭—奏折 data

Summary: Exported all verified `yu_source` 上諭—奏折 records from the sample
state into the requested `review-tools/(2) sample/yu-source.json` file. The
export contains 213 records, all with relation `yu_source`.

Files:
- `review-tools/(2) sample/yu-source.json`
- `review-tools/shared data/review-bundles/yu-source-sample-verified/`
- `PROJECT_LOG.md`

Verified:
- Exported pair keys exactly match the 213 verified `__docPairs` source pairs
  in `review-tools/(2) sample/sample_all.data`.
- No records are missing or extra; all 213 source documents were found in the
  canonical corpus.
- The generated review bundle also contains 213 pairs.
- `git diff --check` passed.

Remaining:
- None for this export.

### 2026-07-20 18:36 HKT — Codex — Grouped relationship prompts in the AI-chat menu

Summary: Added a section boundary after the four relationship prompts—回應的先前上諭、回應的先前上諭（無引文）、上諭回應的奏折、回應的先前硃批—so they form one individual part before 摘要／分段 in both review UIs.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Confirmed both menus keep the four requested prompts together and place the separator immediately before 摘要／分段.
- Parsed all embedded scripts in both HTML files successfully.
- `git diff --check` passed.

Remaining:
- Human confirmation of the new AI-chat menu grouping.

### 2026-07-20 18:39 HKT — Codex — Replaced global click-network reach controls with lane-first profiles

Summary:
- Replaced the old relationship-type depth controls for normal dot clicks with four source-lane sections, each containing four target-lane depth controls (`0`-`4` and `∞`).
- Rebuilt normal click traversal as a mixed dot-to-dot graph covering event sources, event responses, document pairs, 硃批 send/receive endpoints, matched 上諭—奏摺 links, and emperor-action information sources.
- Preserved the clicked 硃批 endpoint side and kept selected network endpoint dots visible even when their ordinary dot filter is off. The separate event-line/show-network path remains independent.
- Added persisted presets and opened the new panel from the header Tools > 連線 group in both formal and sample UIs.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Embedded JavaScript parsed successfully in both HTML files.
- `git diff --check` passed.
- Browser smoke-tested the formal and sample pages: the new panel renders 4 source sections and 16 target rows; changing 第一線 → 第二線 to `0` reduced the clicked event network to the seed event; a document click highlighted the selected 硃批 send/receive pair.

Remaining:
- Human confirmation of the default lane depths and final visual grouping.

### 2026-07-20 18:41 HKT — Codex — Defined the AI loop process

Summary: Documented the end-to-end AI loop from terminal model execution to
human review and chart integration.

Files:
- `AGENTS.md`
- `CLAUDE.md`
- `PROJECT_LOG.md`

Verified:
- The AI loop is defined as a chained run of saved prompts and/or skills
  using a specified AI model on two or more original documents from the
  terminal.
- The definition requires JSON output and a review bundle loaded into the
  website's AI chat for user review and editing before chart addition.
- The definition was added identically to both agent instruction files.

Remaining:
- None.

### 2026-07-20 18:49 HKT — Codex — Scaled the visible network button with 介面字級

Summary: Applied the `--ui-fs` interface-font scale to the visible
`點擊後顯示範圍` button's text, horizontal padding, and toolbar height in both
formal and sample UIs.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Embedded JavaScript parsed successfully in both HTML files.
- The button's font and geometry reference `--ui-fs` in both HTML files.
- `git diff --check` passed.

Remaining:
- None.

### 2026-07-20 18:51 HKT — Codex — Hid the click-network settings button

Summary: Hid the visible `點擊後顯示範圍` toolbar control in both formal and
sample UIs while preserving the existing lane-first panel logic and handler.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `PROJECT_LOG.md`

Verified:
- Embedded JavaScript parsed successfully in both HTML files.
- The network-settings control is hidden by CSS in both HTML files.
- `git diff --check` passed.

Remaining:
- None.

### 2026-07-20 19:54 HKT — Codex — Implemented the official-document-first AI loop

Summary: Added a one-click official-document-centred sequence to formal and
sample review tools, updated the workflow map, and made confirmed pair JSON the
authoritative graph for all relationship-following stages.

Changed:
- The loop now runs summary, division, 林方 extraction, and combined three-class
  清方 extraction before relationship analysis.
- Event extraction reuses simultaneous source-chain tracing and cross-document
  duplicate detection; earliest matches are ordered by report date and retain
  merge-versus-separate controls.
- Existing `official_reply_to_yu` pairs feed response-focused earlier-上諭 cards
  without another corpus search or pair judgement.
- The selected document's 硃批 and confirmed `yu_source` 上諭 feed combined,
  multi-source emperor-action cards with repeated-action review controls.
- Every confirmed `yu_source` 上諭 is followed through confirmed
  `official_reply_to_yu` edges to later official responses, even if the model
  does not retain that 上諭 in an emperor-action card.
- The workflow source viewer now exposes the new specifications and Gemini
  proxy implementation.

Files:
- `review-tools/(1) formal/index.html`
- `review-tools/(2) sample/index.html`
- `review-tools/(4) workflow/index.html`
- `review-tools/(4) workflow/app.js`
- `review-tools/(4) workflow/README.md`
- `review-tools/server.py`
- `tool/skills md/official-document-review-loop.md`
- `PROJECT_LOG.md`

Verified:
- Formal and sample official-loop implementation blocks match.
- Embedded JavaScript parses in both review HTML files; workflow JavaScript and
  modified Python files compile.
- All 24 visible workflow nodes have English and Traditional Chinese detail
  records; relevant pair files remain valid JSON.
- Formal, sample, and workflow routes returned HTTP 200 on a temporary local
  server; `/api/workflow-sources` returned HTTP 200 and exposed all four new
  loop/proxy sources.
- `git diff --check` passed.

Remaining:
- Run a live Gemini request and human-review the generated cards when the proxy
  runtime dependencies and credentials are available.

### 2026-07-20 20:20 HKT — Codex — Added end-of-run spending table to mass prompt runner

Summary: Added per-loop-stage token and USD spending accounting for the
Gemini 3.5 Flash mass runner, including an all-stage total.

Changed:
- Grouped calls under the loop stages used by `run_mass_prompt_chain_test.py`.
- Added standard Gemini model rates, command-line price overrides, and a
  serializable `cost-summary.json` beside each generated bundle.
- Marked costs as approximate when the proxy does not return usage metadata;
  exact usage is used automatically if the proxy supplies it.

Files:
- `tool/scripts py/run_review_bundle_test.py`
- `tool/scripts py/run_mass_prompt_chain_test.py`
- `PROJECT_LOG.md`

Verified:
- Both runner files pass Python bytecode compilation.
- `git diff --check` passed.
- Offline replay of the supplied 硃25 token lines produced a total of
  approximately `$1.101750` at the standard Gemini 3.5 Flash rates.

Remaining:
- The current deployed proxy still returns no usage metadata, so the live
  table will remain estimated until that proxy is redeployed with usage data.
