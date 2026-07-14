"""Clean batch LLM entity extraction results into entity and error CSV files."""

import csv
import json
import re
from pathlib import Path


SOURCE_ID = "source-001"
WIKI_DIR = Path(__file__).resolve().parent.parent
INPUT_PATH = WIKI_DIR / "outputs/source-001/source-001.entities.vertex.csv"
CLEANED_PATH = WIKI_DIR / "outputs/source-001/source-001.entities.cleaned.csv"
ERRORS_PATH = WIKI_DIR / "outputs/source-001/source-001.entities.errors.csv"

CLEANED_COLUMNS = [
    "source_id",
    "input_row",
    "original_input",
    "entity_text",
    "entity_type",
    "uncertain",
    "evidence",
    "notes",
]

ERROR_COLUMNS = [
    "source_id",
    "input_row",
    "original_input",
    "raw_response",
    "error",
]


def normalize_header(header):
    """Convert a CSV header into a simple form for comparison."""
    return re.sub(r"[^a-z0-9]+", "_", (header or "").strip().lower()).strip("_")


def find_column(fieldnames, possible_names, required=True):
    """Find a CSV column using a list of common header names."""
    normalized_fields = {
        normalize_header(fieldname): fieldname for fieldname in fieldnames or []
    }

    for possible_name in possible_names:
        matching_field = normalized_fields.get(normalize_header(possible_name))
        if matching_field:
            return matching_field

    if required:
        names = ", ".join(possible_names)
        raise ValueError(f"Could not find a required CSV column. Expected one of: {names}")

    return None


def remove_markdown_code_fences(response):
    """Remove surrounding Markdown code fences from a model response."""
    cleaned = response.strip()
    cleaned = re.sub(r"^\s*```(?:json)?\s*", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\s*```\s*$", "", cleaned)
    return cleaned.strip()


def format_uncertain(value):
    """Write Boolean uncertainty values consistently in the output CSV."""
    if value is True:
        return "true"
    if value is False:
        return "false"
    if value is None:
        return ""
    return str(value)


def make_error_row(input_row, original_input, raw_response, error):
    """Create one error CSV row."""
    return {
        "source_id": SOURCE_ID,
        "input_row": input_row,
        "original_input": original_input,
        "raw_response": raw_response,
        "error": error,
    }


def main():
    """Read the batch CSV and write cleaned entity and error CSV files."""
    CLEANED_PATH.parent.mkdir(parents=True, exist_ok=True)

    entity_rows = []
    error_rows = []
    input_count = 0

    with INPUT_PATH.open("r", encoding="utf-8-sig", newline="") as input_file:
        reader = csv.DictReader(input_file)

        row_column = find_column(
            reader.fieldnames,
            ["row number", "row", "row_number", "input row", "input_row"],
            required=False,
        )
        input_column = find_column(
            reader.fieldnames,
            ["original input", "original_input", "input", "prompt input", "prompt"],
        )
        response_column = find_column(
            reader.fieldnames,
            ["model response", "model_response", "response", "output", "result"],
        )

        for sequential_row, input_record in enumerate(reader, start=1):
            input_count += 1
            input_row = (
                (input_record.get(row_column) or "").strip()
                if row_column
                else str(sequential_row)
            )
            original_input = input_record.get(input_column) or ""
            raw_response = input_record.get(response_column) or ""
            cleaned_response = remove_markdown_code_fences(raw_response)

            try:
                parsed_response = json.loads(cleaned_response)
            except (json.JSONDecodeError, TypeError) as error:
                error_rows.append(
                    make_error_row(
                        input_row,
                        original_input,
                        raw_response,
                        f"JSON parsing failed: {error}",
                    )
                )
                continue

            if not isinstance(parsed_response, list):
                error_rows.append(
                    make_error_row(
                        input_row,
                        original_input,
                        raw_response,
                        "Parsed JSON is not an array.",
                    )
                )
                continue

            # An empty array is valid and produces no entity rows.
            if not parsed_response:
                continue

            invalid_entity = next(
                (
                    position
                    for position, entity in enumerate(parsed_response, start=1)
                    if not isinstance(entity, dict)
                ),
                None,
            )
            if invalid_entity is not None:
                error_rows.append(
                    make_error_row(
                        input_row,
                        original_input,
                        raw_response,
                        f"Array item {invalid_entity} is not an entity object.",
                    )
                )
                continue

            for entity in parsed_response:
                entity_rows.append(
                    {
                        "source_id": SOURCE_ID,
                        "input_row": input_row,
                        "original_input": original_input,
                        "entity_text": entity.get("entity_text", ""),
                        "entity_type": entity.get("entity_type", ""),
                        "uncertain": format_uncertain(entity.get("uncertain")),
                        "evidence": entity.get("evidence", ""),
                        "notes": entity.get("notes", ""),
                    }
                )

    # utf-8-sig adds a BOM so Excel and Numbers recognize Chinese text correctly.
    with CLEANED_PATH.open("w", encoding="utf-8-sig", newline="") as cleaned_file:
        writer = csv.DictWriter(cleaned_file, fieldnames=CLEANED_COLUMNS)
        writer.writeheader()
        writer.writerows(entity_rows)

    with ERRORS_PATH.open("w", encoding="utf-8-sig", newline="") as errors_file:
        writer = csv.DictWriter(errors_file, fieldnames=ERROR_COLUMNS)
        writer.writeheader()
        writer.writerows(error_rows)

    print(f"Input rows read: {input_count}")
    print(f"Entity rows written: {len(entity_rows)}")
    print(f"Error rows written: {len(error_rows)}")


if __name__ == "__main__":
    main()
