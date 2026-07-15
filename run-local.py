#!/usr/bin/env python3
"""Unpack the bundled review history once, then start the local review app."""

from __future__ import annotations

import os
import runpy
import socket
import subprocess
import sys
import time
import urllib.error
import urllib.request
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
ARCHIVE = ROOT / "archives" / "review-bundles.zip"
BUNDLES = ROOT / "outputs" / "review-bundles"
AI_PROXY = ROOT / "gemini-proxy" / "main.py"


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


def available_port() -> int:
    requested = os.environ.get("LLM_WIKI_AI_PORT")
    if requested:
        return int(requested)
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def ai_python() -> Path:
    configured = os.environ.get("LLM_WIKI_AI_PYTHON")
    if configured:
        return Path(configured)
    local = ROOT / ".venv" / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    return local if local.is_file() else Path(sys.executable)


def start_ai_proxy() -> subprocess.Popen | None:
    port = available_port()
    url = f"http://127.0.0.1:{port}"
    os.environ["LLM_WIKI_AI_URL"] = url
    env = os.environ.copy()
    env["PORT"] = str(port)
    flags = subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0
    process = subprocess.Popen(
        [str(ai_python()), str(AI_PROXY)],
        cwd=AI_PROXY.parent,
        env=env,
        creationflags=flags,
    )
    deadline = time.monotonic() + 8
    while time.monotonic() < deadline:
        if process.poll() is not None:
            print(
                "AI service is unavailable. Install its dependencies with:\n"
                f'  "{ai_python()}" -m pip install -r "{AI_PROXY.parent / "requirements.txt"}"'
            )
            return None
        try:
            with urllib.request.urlopen(url, timeout=0.4):
                print("Local AI service: available through /api/ai")
                return process
        except (urllib.error.URLError, TimeoutError):
            time.sleep(0.15)
    process.terminate()
    print("AI service did not become ready; the review UI will still run without AI.")
    return None


if __name__ == "__main__":
    install_review_bundles()
    ai_process = start_ai_proxy()
    try:
        runpy.run_path(str(ROOT / "review-app" / "server.py"), run_name="__main__")
    finally:
        if ai_process and ai_process.poll() is None:
            ai_process.terminate()
