# DH Project

This is the working folder for the 林爽文 digital-history project and its
student-facing digital-humanities teaching exemplar.

The project has two connected deliverables: the completed review system for
奏摺／硃批／上諭 materials, and a dynamic companion website that introduces the
research problem, teaches students how to use the system, and explains how to
recreate its data, AI-review, and visualisation workflow.

## Start here

- `review-tools/(1) formal/` — complete research review tool and durable review state.
- `review-tools/(2) sample/` — isolated presentation/sample tool and sample state.
- `review-tools/(3) model-output-comparison/` — side-by-side comparison of model review outputs.
- `review-tools/(4) workflow/` — interactive map of the review and LLM workflow.
- `wiki/` — the LLM Wiki used by humans and AI agents as the research-thinking layer.
- `2nd Material & FYP/` — secondary research, FYP writing and research design,
  maps/GIS material, and the manuscript used as historical and methodological
  context. These are not a replacement for the canonical primary-source data.
- `Competition Info/` — the local competition brief and its documentation notes.
  The supplied brief is a bilingual public draft, so its placeholders and
  provisional details must be confirmed before publication.
- `tool/` — proxy services, Markdown skills, and Python scripts grouped by file type and role.
- `tool/proxy/PROXY_WEBSITES.md` — all deployed proxy URLs and copy-pasteable redeployment commands.
- GitHub repository: <https://github.com/CBananaC/llm-wiki-teammate-package>
- `PROJECT_LOG.md` — current state and the chronological human/agent change record.

Run the review tools with:

```bash
cd "/Users/creamybanana/Downloads/DH Project"
python3 run-local.py
```

Then open:

- Formal (default): <http://127.0.0.1:8766/>
- Formal: <http://127.0.0.1:8766/formal>
- Sample: <http://127.0.0.1:8766/sample>
- Model comparison: <http://127.0.0.1:8766/model-output-comparison>
- Workflow: <http://127.0.0.1:8766/workflow/>
- Project log: <http://127.0.0.1:8766/status>

## Context for the teaching website

The FYP and secondary materials frame the system around wartime information
flow and delayed control: reconstructing how reports, imperial responses,
official replies, military movement, logistics, and place-based events fit
together. The teaching website should present this as a reproducible chain:

`source extraction -> data organisation and annotation -> relationship and timing analysis -> human review -> digital presentation`

The competition brief aligns with this direction because it accepts research,
tool, education, and exhibition-oriented work and asks participants to explain
their AI use, human revision, source acknowledgement, and limitations. See
[`Competition Info/README.md`](<Competition Info/README.md>) and
[`2nd Material & FYP/README.md`](<2nd Material & FYP/README.md>) for the working
context and cautions.

The two review tools share only `review-tools/shared data/stage1_original_text.json`
and `review-tools/shared data/review-bundles/`. Their relationship files and editable
state are deliberately separate.

This folder is prepared for the GitHub repository above. Follow the GitHub push
protocol in `AGENTS.md`; agents never execute `git push` for the user.
