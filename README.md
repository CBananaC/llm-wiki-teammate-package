# DH Project

This is the working folder for the 林爽文 digital-history project.

## Start here

- `review-tools/(1) formal/` — complete research review tool and durable review state.
- `review-tools/(2) sample/` — isolated presentation/sample tool and sample state.
- `review-tools/(3) model-output-comparison/` — side-by-side comparison of model review outputs.
- `review-tools/(4) workflow/` — interactive map of the review and LLM workflow.
- `wiki/` — the LLM Wiki used by humans and AI agents as the research-thinking layer.
- `Second hand material/FYP/` — the FYP manuscript and related second-hand material.
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

The two review tools share only `review-tools/shared data/stage1_original_text.json`
and `review-tools/shared data/review-bundles/`. Their relationship files and editable
state are deliberately separate.

This folder is prepared for the GitHub repository above. Follow the GitHub push
protocol in `AGENTS.md`; agents never execute `git push` for the user.
