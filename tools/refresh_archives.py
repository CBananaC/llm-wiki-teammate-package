#!/usr/bin/env python3
"""Rebuild this package's UTF-8-safe archives from the full llm-wiki tree.

Usage: python3 tools/refresh_archives.py /path/to/llm-wiki
"""

from __future__ import annotations

import sys
import zipfile
from pathlib import Path


PACKAGE = Path(__file__).resolve().parents[1]
SKIP_NAMES = {".DS_Store", "__pycache__"}


def archive(source_root: Path, targets: list[Path], destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(destination, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as output:
        for target in targets:
            paths = [target] if target.is_file() else sorted(path for path in target.rglob("*") if path.is_file())
            for path in paths:
                if any(part in SKIP_NAMES for part in path.parts):
                    continue
                # pathlib/zipfile marks non-ASCII entry names as UTF-8, which
                # preserves names such as 台297 across macOS, Windows, and Linux.
                output.write(path, path.relative_to(source_root).as_posix())


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python3 tools/refresh_archives.py /path/to/llm-wiki")
    source = Path(sys.argv[1]).resolve()
    if not (source / "outputs" / "review-bundles").is_dir():
        raise SystemExit("Expected an llm-wiki directory containing outputs/review-bundles")

    archive(source, [source / "outputs" / "review-bundles"], PACKAGE / "archives" / "review-bundles.zip")
    # `scripts` is intentionally NOT archived here: the runners now live as a
    # loose, git-tracked `scripts/` folder in this package (edited directly), so
    # zipping them too would duplicate and risk divergence.
    research_targets = [
        source / name
        for name in ("raw", "ocr", "cleaned", "corpora", "background", "research-attempts")
        if (source / name).exists()
    ]
    research_targets.extend(sorted(source.glob("*.md")))
    archive(source, research_targets, PACKAGE / "archives" / "research-workspace.zip")
    print("Archives refreshed.")


if __name__ == "__main__":
    main()
