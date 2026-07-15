#!/usr/bin/env python3
"""Run the existing review skills over every 硃批 in a terminal date window.

The stage implementations remain in run_review_bundle_test.py and continue to
read their prompts from skills/*.md. This entry point only selects the 硃批
records by date, invokes that proven runner, and annotates its bundle with the
period-specific loop metadata.

Example:
  python3 scripts/run_zhu_review_loop.py \
    --proxy https://gemini-proxy-v2ewrxq4sq-de.a.run.app \
    --date-from 1786-12-01 --date-to 1786-12-31
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from run_review_bundle_test import (  # noqa: E402
    ROOT,
    SOURCE,
    STEP_SKILL,
    SKILLS_DIR,
    all_record_dates,
    parse_date,
    primary_date,
    split_csv,
)


DEFAULT_STEPS = (
    "summary,divide,lin-events,source-chain,qing-events-done,qing-events-plan,"
    "qing-events-nonmil,zhupi,edict-match"
)


def normalized_bound(value: str, label: str) -> tuple[str, date]:
    parsed = parse_date(value)
    if not parsed:
        raise SystemExit(f"{label} must be YYYY-MM-DD or YYYY/MM/DD: {value}")
    return parsed.isoformat(), parsed


def select_zhu(records: list[dict], start: date, end: date, mode: str) -> list[dict]:
    selected = []
    for record in records:
        if record.get("doc_type") != "硃批":
            continue
        values = [primary_date(record)] if mode == "primary" else all_record_dates(record)
        dates = [parse_date(value) for value in values]
        if any(value and start <= value <= end for value in dates):
            selected.append(record)
    selected.sort(key=lambda record: (primary_date(record) or "9999-99-99", str(record.get("doc_id") or record.get("id") or "")))
    return selected


def write_json(path: Path, data: object) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--proxy", default=os.environ.get("GEMINI_PROXY_URL", ""), help="AI proxy base URL")
    parser.add_argument("--model", default=os.environ.get("GEMINI_MODEL", "gemini-2.5-flash"))
    parser.add_argument("--date-from", required=True, help="Period start: YYYY-MM-DD")
    parser.add_argument("--date-to", required=True, help="Period end: YYYY-MM-DD")
    parser.add_argument(
        "--date-mode",
        choices=("primary", "any"),
        default="primary",
        help="primary uses 硃批／收受日 first; any uses any normalized document date",
    )
    parser.add_argument("--steps", default=DEFAULT_STEPS, help="Comma-separated subset of the loop stages")
    parser.add_argument("--bundle", default="", help="Review-bundle name; stable by default for this period")
    parser.add_argument("--timeout", type=int, default=300)
    parser.add_argument("--retries", type=int, default=6)
    parser.add_argument("--retry-sleep", type=int, default=20)
    parser.add_argument("--skip-done", action="store_true", help="Resume completed stages in the same bundle")
    parser.add_argument("--dry-run", action="store_true", help="List selected 硃批 without calling the proxy")
    args = parser.parse_args()

    start_text, start = normalized_bound(args.date_from, "--date-from")
    end_text, end = normalized_bound(args.date_to, "--date-to")
    if start > end:
        raise SystemExit("--date-from must not be later than --date-to")

    records = json.loads(SOURCE.read_text(encoding="utf-8"))
    docs = select_zhu(records, start, end, args.date_mode)
    if not docs:
        raise SystemExit(f"No 硃批 found in {start_text} to {end_text} ({args.date_mode} mode).")

    steps = split_csv(args.steps)
    allowed = set(split_csv(DEFAULT_STEPS))
    unknown = [step for step in steps if step not in allowed]
    if unknown:
        raise SystemExit("Unsupported loop stage(s): " + ", ".join(unknown))

    missing_skills = [
        f"{step} -> {STEP_SKILL.get(step, '')}"
        for step in steps
        if not STEP_SKILL.get(step) or not (SKILLS_DIR / STEP_SKILL[step]).is_file()
    ]
    if missing_skills:
        raise SystemExit("Missing skill file(s): " + ", ".join(missing_skills))

    bundle_name = args.bundle or f"zhu-review-loop-{start_text.replace('-', '')}-{end_text.replace('-', '')}"
    print(f"Selected 硃批: {len(docs)} | period: {start_text} to {end_text} | mode: {args.date_mode}")
    for record in docs:
        doc_id = record.get("doc_id") or record.get("id") or ""
        print(f"  {doc_id} | {primary_date(record) or '未明'} | {record.get('author_name') or '未明'} | {record.get('title') or ''}")

    if args.dry_run:
        print("\n(dry run — no proxy calls)")
        return 0
    if not args.proxy:
        raise SystemExit("Set --proxy or use --dry-run.")

    # Reuse the established per-document runner so every stage continues to
    # use the same payloads, retry behavior, output shapes, and website skill
    # prompts as the existing terminal and browser workflows.
    from run_review_bundle_test import main as run_review_bundle_main  # noqa: E402

    forwarded = [
        "run_review_bundle_test.py",
        "--proxy", args.proxy,
        "--model", args.model,
        "--doc-ids", ",".join(str(record.get("doc_id") or record.get("id")) for record in docs),
        "--steps", ",".join(steps),
        "--bundle", bundle_name,
        "--timeout", str(args.timeout),
        "--retries", str(args.retries),
        "--retry-sleep", str(args.retry_sleep),
    ]
    if args.skip_done:
        forwarded.append("--skip-done")

    old_argv = sys.argv
    try:
        sys.argv = forwarded
        run_review_bundle_main()
    finally:
        sys.argv = old_argv

    bundle_root = ROOT / "outputs" / "review-bundles" / bundle_name
    manifest_path = bundle_root / "manifest.json"
    if not manifest_path.exists():
        raise SystemExit(f"Runner finished without a manifest: {manifest_path}")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest.update({
        "loop_skill": "skills/zhu-review-loop.md",
        "loop_type": "zhu-review-loop",
        "doc_type": "硃批",
        "date_from": start_text,
        "date_to": end_text,
        "date_mode": args.date_mode,
        "doc_ids": [str(record.get("doc_id") or record.get("id")) for record in docs],
        "chain": ["zhu-review-loop", *steps],
        "skill_files": {step: STEP_SKILL[step] for step in steps},
    })
    write_json(manifest_path, manifest)
    print(f"\nZhu review loop bundle: {bundle_root}")
    print("Open the website and choose: 資料 → 載入技能輸出")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
