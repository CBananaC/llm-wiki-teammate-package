# Skill: NLP Analysis

## Purpose

Use this skill to create structured, reviewable NLP outputs from Sinitic / Chinese humanities texts. NLP outputs should be saved as artifacts that a human can inspect, such as CSV files, Markdown summaries, or tagged TEI-derived tables.

## When To Use

Use this skill when the task asks for:

- Topic summaries or thematic labels.
- Text classification.
- Keyword or controlled-vocabulary tagging.
- TEI-derived entity/tag inventories.
- Comparison between model-generated analysis and source evidence.

## Rules

- Do not treat a one-document output as a statistical topic model.
- Preserve source wording in Chinese.
- Separate rule-based tags, model-generated labels, and human-reviewed judgments.
- Include evidence for every label or topic.
- Mark uncertain classifications instead of forcing a clean label.
- Keep raw text, TEI, and NLP-derived outputs in separate files.

## Recommended Outputs

- `*.nlp-segments.csv`: document sections or passages extracted from TEI or cleaned text.
- `*.nlp-tags.csv`: TEI tags, controlled terms, or model-generated tags with counts and evidence.
- `*.nlp-topics.csv`: topic labels with matched terms, evidence, method, and limitations.
- `*.nlp-classification.csv`: document-level labels with evidence and uncertainty.
- `*.nlp-summary.md`: short human-readable explanation of method and findings.

## TEI + NLP Workflow

1. Validate or inspect the TEI file.
2. Extract title, body sections, paragraphs, keywords, and existing TEI tags.
3. Apply a transparent method, such as rule-based term matching or a documented model prompt.
4. Save structured outputs as CSV.
5. Add a Markdown note explaining method and limitations.
6. Review labels before using them as research evidence.

## Common Errors

- Calling a controlled topic list a topic model.
- Dropping the original Chinese evidence.
- Mixing source-derived facts with model interpretation.
- Creating relationship edges from co-occurrence alone.
- Treating unreviewed tags as verified research data.

## Related Wiki Pages

- [[workflows]]
- [[extraction-rules]]
- [[known-errors]]
- [[source-materials]]
