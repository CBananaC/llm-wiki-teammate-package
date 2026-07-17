"""Create transparent TEI-derived NLP artifacts for source-001.

This script intentionally uses rule-based summaries rather than a statistical
topic model. The current corpus is a single abstract, so auditable CSV outputs
are more useful than pretending that one document can support corpus-level NLP.
"""

import csv
import re
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from xml.etree import ElementTree as ET


SOURCE_ID = "source-001"
WIKI_DIR = Path(__file__).resolve().parent.parent.parent
OUTPUT_DIR = WIKI_DIR / "outputs" / SOURCE_ID
TEI_PATH = OUTPUT_DIR / f"{SOURCE_ID}.tei.xml"

SEGMENTS_PATH = OUTPUT_DIR / f"{SOURCE_ID}.nlp-segments.csv"
TAGS_PATH = OUTPUT_DIR / f"{SOURCE_ID}.nlp-tags.csv"
TOPICS_PATH = OUTPUT_DIR / f"{SOURCE_ID}.nlp-topics.csv"
CLASSIFICATION_PATH = OUTPUT_DIR / f"{SOURCE_ID}.nlp-classification.csv"
SUMMARY_PATH = OUTPUT_DIR / f"{SOURCE_ID}.nlp-summary.md"

NS = {"tei": "http://www.tei-c.org/ns/1.0"}

TAG_ELEMENTS = {
    "persName": "person",
    "placeName": "place",
    "roleName": "role",
    "date": "date",
    "term": "concept",
    "title": "title",
}

TOPIC_RULES = [
    {
        "topic_id": "topic-001",
        "topic_label": "Revolutionary alliance and rupture",
        "terms": ["反滿革命", "革命同道", "思想上的差異", "爭執", "齟齬", "分裂"],
    },
    {
        "topic_id": "topic-002",
        "topic_label": "Personality and political authority",
        "terms": ["元首", "國師", "高度自信", "直言無忌", "屈己相從"],
    },
    {
        "topic_id": "topic-003",
        "topic_label": "Nationalism and anti-Qing politics",
        "terms": ["民族主義", "國族主義", "推翻滿清政權", "排滿", "清政府"],
    },
    {
        "topic_id": "topic-004",
        "topic_label": "Imperialism and Western influence",
        "terms": ["西方文化", "歐美", "列強", "帝國主義", "西潮", "反帝"],
    },
    {
        "topic_id": "topic-005",
        "topic_label": "Asia, Russia, and communism",
        "terms": ["亞洲", "俄", "赤化", "聯俄容共", "外力"],
    },
]


def text_content(element):
    """Return normalized text content for a TEI element."""
    if element is None:
        return ""
    return re.sub(r"\s+", "", "".join(element.itertext())).strip()


def find_first(root, query):
    """Find the first TEI element matching an XPath query."""
    return root.find(query, NS)


def count_term(text, term):
    """Count non-overlapping occurrences of a source term."""
    return text.count(term)


def make_snippet(text, term, radius=24):
    """Return a short evidence snippet around the first occurrence of term."""
    index = text.find(term)
    if index < 0:
        return ""

    start = max(0, index - radius)
    end = min(len(text), index + len(term) + radius)
    prefix = "..." if start > 0 else ""
    suffix = "..." if end < len(text) else ""
    return f"{prefix}{text[start:end]}{suffix}"


def write_csv(path, fieldnames, rows):
    """Write CSV with a BOM so spreadsheet apps recognize Chinese text."""
    with path.open("w", encoding="utf-8-sig", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def build_segments(root):
    """Extract the major TEI text units used by the NLP summaries."""
    body_title = find_first(root, ".//tei:text//tei:body//tei:head/tei:title")
    abstract = find_first(root, ".//tei:div[@type='abstract']/tei:p")
    keyword_items = root.findall(".//tei:div[@type='keywords']//tei:item", NS)

    segments = []
    for segment_id, segment_type, label, element in [
        ("seg-001", "title", "article title", body_title),
        ("seg-002", "abstract", "abstract paragraph", abstract),
    ]:
        text = text_content(element)
        if text:
            segments.append(
                {
                    "source_id": SOURCE_ID,
                    "segment_id": segment_id,
                    "segment_type": segment_type,
                    "label": label,
                    "text": text,
                    "character_count": len(text),
                    "tei_entity_count": sum(
                        1
                        for tag_name in TAG_ELEMENTS
                        for _ in element.findall(f".//tei:{tag_name}", NS)
                    ),
                    "notes": "Extracted from TEI body.",
                }
            )

    for index, item in enumerate(keyword_items, start=1):
        text = text_content(item)
        if text:
            segments.append(
                {
                    "source_id": SOURCE_ID,
                    "segment_id": f"kw-{index:03d}",
                    "segment_type": "keyword",
                    "label": "source keyword",
                    "text": text,
                    "character_count": len(text),
                    "tei_entity_count": sum(
                        1
                        for tag_name in TAG_ELEMENTS
                        for _ in item.findall(f".//tei:{tag_name}", NS)
                    ),
                    "notes": "Keyword transcribed from the source page.",
                }
            )

    return segments


def build_tag_rows(root, segments):
    """Aggregate TEI element tags and controlled source-term tags."""
    tag_rows = {}
    section_elements = [
        ("title", find_first(root, ".//tei:text//tei:body//tei:head/tei:title")),
        ("abstract", find_first(root, ".//tei:div[@type='abstract']/tei:p")),
        ("keywords", find_first(root, ".//tei:div[@type='keywords']")),
    ]

    for section_id, section_element in section_elements:
        if section_element is None:
            continue

        for tag_name, tag_type in TAG_ELEMENTS.items():
            for element in section_element.findall(f".//tei:{tag_name}", NS):
                tag_text = text_content(element)
                if not tag_text:
                    continue

                key = (tag_text, tag_type, tag_name)
                ref = element.attrib.get("ref", "")
                if key not in tag_rows:
                    tag_rows[key] = {
                        "source_id": SOURCE_ID,
                        "tag_text": tag_text,
                        "tag_type": tag_type,
                        "tei_element": tag_name,
                        "count": 0,
                        "sections": set(),
                        "refs": set(),
                        "evidence": tag_text,
                        "notes": "Extracted from explicit TEI markup.",
                    }

                tag_rows[key]["count"] += 1
                tag_rows[key]["sections"].add(section_id)
                if ref:
                    tag_rows[key]["refs"].add(ref)

    full_text = "".join(segment["text"] for segment in segments)
    controlled_terms = sorted({term for topic in TOPIC_RULES for term in topic["terms"]}, key=len, reverse=True)
    existing_tag_texts = {key[0] for key in tag_rows}

    for term in controlled_terms:
        occurrences = count_term(full_text, term)
        if occurrences == 0 or term in existing_tag_texts:
            continue

        tag_rows[(term, "controlled_topic_term", "rule")] = {
            "source_id": SOURCE_ID,
            "tag_text": term,
            "tag_type": "controlled_topic_term",
            "tei_element": "",
            "count": occurrences,
            "sections": {"abstract"},
            "refs": set(),
            "evidence": make_snippet(full_text, term),
            "notes": "Rule-based term tag from the TEI+NLP topic vocabulary.",
        }

    return [
        {
            **{key: value for key, value in row.items() if key not in {"sections", "refs"}},
            "sections": "|".join(sorted(row["sections"])),
            "refs": "|".join(sorted(row["refs"])),
        }
        for row in sorted(tag_rows.values(), key=lambda item: (item["tag_type"], item["tag_text"]))
    ]


def build_topics(full_text):
    """Create rule-based topic rows with source evidence."""
    rows = []
    for topic in TOPIC_RULES:
        term_counts = Counter(
            {term: count_term(full_text, term) for term in topic["terms"] if count_term(full_text, term)}
        )
        total_count = sum(term_counts.values())
        if total_count == 0:
            continue

        first_term = next(term for term in topic["terms"] if term_counts.get(term))
        evidence_terms = "|".join(f"{term}:{count}" for term, count in term_counts.items())
        rows.append(
            {
                "source_id": SOURCE_ID,
                "topic_id": topic["topic_id"],
                "topic_label": topic["topic_label"],
                "method": "rule-based term matching from TEI text",
                "matched_term_count": total_count,
                "matched_terms": evidence_terms,
                "evidence": make_snippet(full_text, first_term),
                "confidence": "medium",
                "notes": "Topic label is an analytical aid, not a statistical topic-model result.",
            }
        )

    return rows


def build_classifications(root, full_text, keyword_text):
    """Create document-level classification rows."""
    title = text_content(find_first(root, ".//tei:titleStmt/tei:title"))
    xml_lang = find_first(root, ".//tei:text")
    language = xml_lang.attrib.get("{http://www.w3.org/XML/1998/namespace}lang", "") if xml_lang is not None else ""

    rows = [
        {
            "source_id": SOURCE_ID,
            "dimension": "document_genre",
            "label": "journal article abstract page",
            "method": "TEI structure",
            "evidence": "TEI div type='abstract' and source keyword list.",
            "uncertain": "false",
            "notes": "Complete article page range remains unverified.",
        },
        {
            "source_id": SOURCE_ID,
            "dimension": "language_script",
            "label": "Traditional Chinese",
            "method": "TEI xml:lang",
            "evidence": language or "zh-Hant",
            "uncertain": "false",
            "notes": "The TEI text element is marked zh-Hant.",
        },
        {
            "source_id": SOURCE_ID,
            "dimension": "subject_area",
            "label": "modern Chinese intellectual history",
            "method": "title and keyword evidence",
            "evidence": title,
            "uncertain": "false",
            "notes": "The title frames a comparison of Zhang Taiyan and Sun Yat-sen's revolutionary thought.",
        },
        {
            "source_id": SOURCE_ID,
            "dimension": "historical_focus",
            "label": "late Qing revolutionary politics",
            "method": "rule-based evidence terms",
            "evidence": make_snippet(full_text, "清季革命時期") or make_snippet(full_text, "滿清政權"),
            "uncertain": "false",
            "notes": "Evidence comes from the abstract text, not from external historical inference.",
        },
        {
            "source_id": SOURCE_ID,
            "dimension": "central_comparison",
            "label": "章太炎 and 孫中山",
            "method": "TEI personal-name markup",
            "evidence": "章太炎與孫中山",
            "uncertain": "false",
            "notes": "CBDB identifiers are encoded in the TEI persName refs.",
        },
        {
            "source_id": SOURCE_ID,
            "dimension": "source_keywords",
            "label": keyword_text,
            "method": "TEI keyword list",
            "evidence": keyword_text,
            "uncertain": "false",
            "notes": "Preserves source keyword wording.",
        },
    ]

    return rows


def build_summary(topic_rows, classification_rows, tag_rows):
    """Create a compact Markdown summary of the generated artifacts."""
    topic_lines = "\n".join(
        f"- {row['topic_id']}: {row['topic_label']} ({row['matched_terms']})"
        for row in topic_rows
    )
    classification_lines = "\n".join(
        f"- {row['dimension']}: {row['label']}" for row in classification_rows
    )
    tag_counts = Counter(row["tag_type"] for row in tag_rows)
    tag_lines = "\n".join(f"- {tag_type}: {count}" for tag_type, count in sorted(tag_counts.items()))

    return f"""# TEI + NLP Summary: {SOURCE_ID}

## Method

Generated on {date.today().isoformat()} by `tool/scripts py/tei_nlp_summary.py`.

This is a TEI-derived, rule-based NLP pass. It extracts document segments, TEI tags, controlled topic terms, and document-level classifications from the checked TEI file. It does not claim to be a corpus-level topic model, POS tagger, or machine-learning classifier.

## Output Files

- `{SOURCE_ID}.nlp-segments.csv`
- `{SOURCE_ID}.nlp-tags.csv`
- `{SOURCE_ID}.nlp-topics.csv`
- `{SOURCE_ID}.nlp-classification.csv`

## Topic Outputs

{topic_lines}

## Classification Outputs

{classification_lines}

## Tagging Outputs

{tag_lines}

## Limitations

- The corpus currently contains one article abstract page, so the topic output is a controlled thematic inventory rather than a statistical topic model.
- The tags are based on existing TEI markup and explicit source terms; they should be checked before being used as research evidence.
- Bibliographic metadata remains incomplete where noted in `source-materials.md` and `processing-notes.md`.
"""


def main():
    """Build all TEI-derived NLP artifacts for source-001."""
    tree = ET.parse(TEI_PATH)
    root = tree.getroot()

    segments = build_segments(root)
    analysis_text = "".join(
        segment["text"]
        for segment in segments
        if segment["segment_type"] in {"title", "abstract"}
    )
    keyword_text = "|".join(
        segment["text"] for segment in segments if segment["segment_type"] == "keyword"
    )
    tag_rows = build_tag_rows(root, segments)
    topic_rows = build_topics(analysis_text)
    classification_rows = build_classifications(root, analysis_text, keyword_text)

    write_csv(
        SEGMENTS_PATH,
        [
            "source_id",
            "segment_id",
            "segment_type",
            "label",
            "text",
            "character_count",
            "tei_entity_count",
            "notes",
        ],
        segments,
    )
    write_csv(
        TAGS_PATH,
        [
            "source_id",
            "tag_text",
            "tag_type",
            "tei_element",
            "count",
            "sections",
            "refs",
            "evidence",
            "notes",
        ],
        tag_rows,
    )
    write_csv(
        TOPICS_PATH,
        [
            "source_id",
            "topic_id",
            "topic_label",
            "method",
            "matched_term_count",
            "matched_terms",
            "evidence",
            "confidence",
            "notes",
        ],
        topic_rows,
    )
    write_csv(
        CLASSIFICATION_PATH,
        [
            "source_id",
            "dimension",
            "label",
            "method",
            "evidence",
            "uncertain",
            "notes",
        ],
        classification_rows,
    )
    SUMMARY_PATH.write_text(
        build_summary(topic_rows, classification_rows, tag_rows),
        encoding="utf-8",
    )

    print(f"Segments written: {len(segments)}")
    print(f"Tags written: {len(tag_rows)}")
    print(f"Topics written: {len(topic_rows)}")
    print(f"Classifications written: {len(classification_rows)}")


if __name__ == "__main__":
    main()
