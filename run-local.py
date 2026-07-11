#!/usr/bin/env python3
"""Unpack the bundled review history once, then start the local review app."""

from __future__ import annotations

import runpy
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
ARCHIVE = ROOT / "archives" / "review-bundles.zip"
BUNDLES = ROOT / "outputs" / "review-bundles"


def install_review_bundles() -> None:
    if BUNDLES.is_dir():
        return
    if not ARCHIVE.is_file():
        raise SystemExit(f"Missing required archive: {ARCHIVE}")
    print("Installing saved review bundles (one-time local extraction)...")
    with zipfile.ZipFile(ARCHIVE) as bundle:
        bundle.extractall(ROOT)
    if not BUNDLES.is_dir():
        raise SystemExit("The review-bundle archive has an unexpected folder layout.")


if __name__ == "__main__":
    install_review_bundles()
    runpy.run_path(str(ROOT / "review-app" / "server.py"), run_name="__main__")
