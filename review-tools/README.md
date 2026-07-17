# Review Tools

This directory contains four numbered review surfaces. The two editing modes
are related but data-isolated.

- `(1) formal/`: complete research review tool and durable formal state.
- `(2) sample/`: presentation/sample tool and isolated sample state.
- `(3) model-output-comparison/`: side-by-side interface for comparing review bundles from different models.
- `(4) workflow/`: interactive map of the review and LLM workflow.
- `shared data/stage1_original_text.json`: the only shared source dataset.
- `shared data/review-bundles/`: batch/model runs available to both tools.

Each editing mode owns its own relationship files. The server root `/` opens
the formal tool and also exposes `/formal`,
`/sample`, `/model-output-comparison`, `/workflow/`, and the APIs needed to
save state, inspect skills, and load shared review bundles.

## Confirmed relationship schema

`confirmed-pairs.json` uses two current relationship values:

- `official_reply_to_yu`: an official memorial replying to an imperial 上諭.
- `official_reply_to_emperor_zhu`: an official memorial replying to the emperor's 硃批.

The retired `prior_report` relationship is not loaded. When an older review
bundle is imported, the HTML converts `reply_to_yu` and `reply_to_zhu` to the
current names and ignores retired `prior_report` records. Historical bundle
files themselves remain unchanged as run provenance.
