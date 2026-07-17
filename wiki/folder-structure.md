# Folder Structure

```text
DH Project/
├── AGENTS.md / CLAUDE.md       # collaborator rules
├── PROJECT_LOG.md             # canonical progress record
├── review-tools/
│   ├── (1) formal/           # formal review UI and state
│   ├── (2) sample/           # isolated sample UI and state
│   ├── (3) model-output-comparison/
│   ├── (4) workflow/
│   └── shared data/         # canonical Stage 1 JSON and bundles
├── wiki/                     # compact research context and rules
├── tool/
│   ├── skills md/           # canonical reusable skills
│   ├── scripts py/          # reproducible processing scripts
│   └── proxy/               # optional AI proxies
└── Second hand material/FYP/
```

## Boundaries

- Do not duplicate canonical source data inside the wiki.
- Do not place generated review bundles beside the formal or sample HTML.
- Do not edit raw evidence in place.
- Keep formal and sample saved state separate.
- Record project changes only in `PROJECT_LOG.md`.

