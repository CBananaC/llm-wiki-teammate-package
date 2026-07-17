# Source Rules

## General rules

- Register a source before using it as evidence.
- Preserve titles, wording, page references, and date fields as supplied.
- Never invent bibliographic details, quotations, or page numbers.
- Distinguish primary sources, datasets, secondary scholarship, and external databases.
- Treat OCR and model-generated text as provisional until checked.
- Cite internal records by stable document identifier and the date field used.
- For formal writing, verify quotations and citations against the underlying publication.

## Active corpus

The canonical Stage 1 dataset is:

`../review-tools/shared data/stage1_original_text.json`

It contains structured records connected to the 林爽文事件. See [[corpora/lin-shuangwen-first-hand-json]] for schema and limitations.

The main printed source compilation is 臺灣史料集成編輯委員會編《明清臺灣檔案彙編》. Page-level use must be checked against the relevant volume.

## Reliability labels

- `raw`: not checked
- `OCRed`: machine-readable but error-prone
- `cleaned`: obvious errors corrected
- `verified`: checked against source evidence
- `analysis-ready`: suitable for structured analysis with recorded cautions

