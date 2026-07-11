#!/usr/bin/env python3
"""Local file server/API for the LLM Wiki review app.

This server is deliberately small. It reads and writes only inside the local
llm-wiki tree so the review UI can sync skills, load review bundles, and export
human-reviewed artifacts without hosting the corpus online.
"""

from __future__ import annotations

import json
import mimetypes
import os
import re
import subprocess
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse


APP_DIR = Path(__file__).resolve().parent
WIKI_DIR = APP_DIR.parent
STATIC_DIR = APP_DIR / "static"
SKILLS_DIR = WIKI_DIR / "skills"
BUNDLES_DIR = WIKI_DIR / "outputs" / "review-bundles"
ATTEMPT_DIR = WIKI_DIR / "outputs" / "attempt-002"
# The timeline page's working state (events, notes, AI chat history -- everything under the
# in-browser `EDITS` object) used to live ONLY in the browser's localStorage, which has a hard
# ~5-10MB/origin cap. A research corpus this size (full quote text, provenance chains, chat
# history) outgrows that fairly easily, and once it does every future edit silently fails to
# save. Disk has no such practical limit, so this file becomes the primary persisted copy;
# localStorage is kept only as a fast local cache/fallback for when this server isn't running
# (e.g. the page opened directly as file://).
EDITS_PATH = ATTEMPT_DIR / "timeline-edits.local.json"

# Section heading a skill file can use to mark the short, single-string
# version of itself that the browser sends as-is to the Gemini proxy for
# quick single-document use. The rest of the skill file (Purpose, Output
# Layout, Common Errors, etc.) stays as the full spec a terminal agent
# reads when running the skill across many documents. Same file, two
# consumers, no duplicated instructions.
WEBSITE_PROMPT_RE = re.compile(
    r"^##\s*Website Prompt[ \t]*\n(.*?)(?=\n##\s|\Z)", re.S | re.M
)


def extract_website_prompt(text: str) -> str:
    m = WEBSITE_PROMPT_RE.search(text)
    if not m:
        return ""
    body = m.group(1).strip()
    # allow the prompt to be wrapped in a fenced code block for readability
    fence = re.match(r"^```[a-zA-Z]*\n(.*?)\n```$", body, re.S)
    if fence:
        body = fence.group(1).strip()
    return body


# A skill file can self-declare how its results should be shown on the
# website, e.g.:
#   **Kind:** events
#   **Actor:** qing
#   **Category:** plan
# so a brand-new skill can wire itself into an existing display (event
# dots, zhupi cards, edict-match cards) without anyone editing the HTML.
# Recognized Kind values match gemini-proxy modes: summary, divide,
# events, zhupi, edict_match.
METADATA_RE = re.compile(r"^\*\*(Kind|Actor|Category):\*\*\s*(.+)$", re.M | re.I)


def extract_metadata(text: str) -> dict:
    out = {"kind": "", "actor": "", "category": ""}
    for m in METADATA_RE.finditer(text):
        key = m.group(1).lower()
        out[key] = m.group(2).strip().strip("`").lower()
    return out


def safe_child(root: Path, rel: str) -> Path:
    target = (root / rel).resolve()
    if root.resolve() not in target.parents and target != root.resolve():
        raise ValueError("path outside allowed root")
    return target


def read_json(path: Path, fallback):
    if not path.exists():
        return fallback
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def git_auto_commit(paths: list[Path], message: str) -> None:
    """Best-effort snapshot of the given paths. Never raises: a git problem
    (no repo, no identity configured, nothing changed) should not break the
    save the user is waiting on. Runs from WIKI_DIR, which is the llm-wiki
    git repo root."""
    try:
        rels = [str(p.relative_to(WIKI_DIR)) for p in paths]
        subprocess.run(["git", "add", *rels], cwd=WIKI_DIR, check=False,
                        capture_output=True, timeout=10)
        status = subprocess.run(["git", "diff", "--cached", "--quiet", *rels],
                                 cwd=WIKI_DIR, capture_output=True, timeout=10)
        if status.returncode == 0:
            return  # nothing staged, avoid an empty commit
        subprocess.run(["git", "commit", "-m", message, *rels], cwd=WIKI_DIR,
                        check=False, capture_output=True, timeout=10)
    except Exception:
        pass


class Handler(BaseHTTPRequestHandler):
    server_version = "LLMWikiReview/0.1"

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        path = parsed.path
        try:
            if path == "/api/health":
                return self.json({"ok": True})
            if path == "/api/edits":
                return self.json(read_json(EDITS_PATH, {}))
            if path == "/api/skills":
                return self.json(self.skills())
            if path == "/api/bundles":
                return self.json(self.bundles())
            if path.startswith("/api/bundles/"):
                name = unquote(path.removeprefix("/api/bundles/"))
                return self.json(self.bundle(name))
            if path == "/api/current-timeline":
                return self.json({
                    "html": str((ATTEMPT_DIR / "stage1-timeline.html").relative_to(WIKI_DIR)),
                    "data": str((ATTEMPT_DIR / "stage1-date-adjusted.json").relative_to(WIKI_DIR)),
                })
            if path == "/app" or path == "/app/":
                return self.attempt_file("stage1-timeline.html")
            if path.startswith("/attempt-002/"):
                rel = unquote(path.removeprefix("/attempt-002/"))
                return self.attempt_file(rel)
            return self.static(path)
        except Exception as exc:
            return self.json({"error": str(exc)}, 500)

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        path = parsed.path
        try:
            data = self.body_json()
            if path == "/api/edits":
                # No git_auto_commit here on purpose: this saves on essentially every click
                # (much higher frequency than a deliberate skill/bundle edit), so committing
                # every write would flood history with noise. Deliberately snapshot it yourself
                # (git add/commit outputs/attempt-002/timeline-edits.local.json) when you want
                # a checkpoint.
                write_json(EDITS_PATH, data)
                return self.json({"ok": True})
            if path.startswith("/api/skills/"):
                slug = unquote(path.removeprefix("/api/skills/"))
                return self.save_skill(slug, data)
            if path.startswith("/api/bundles/") and path.endswith("/export"):
                name = unquote(path.removeprefix("/api/bundles/").removesuffix("/export"))
                return self.export_bundle(name)
            if path.startswith("/api/bundles/"):
                name = unquote(path.removeprefix("/api/bundles/"))
                return self.save_bundle(name, data)
            return self.json({"error": "unknown endpoint"}, 404)
        except Exception as exc:
            return self.json({"error": str(exc)}, 500)

    def skills(self):
        SKILLS_DIR.mkdir(exist_ok=True)
        out = []
        for path in sorted(SKILLS_DIR.glob("*.md")):
            text = path.read_text(encoding="utf-8")
            title = text.splitlines()[0].lstrip("# ").strip() if text.splitlines() else path.stem
            out.append({
                "slug": path.stem,
                "title": title,
                "path": str(path.relative_to(WIKI_DIR)),
                "text": text,
                "prompt": extract_website_prompt(text),
                **extract_metadata(text),
            })
        return out

    def save_skill(self, slug: str, data):
        if not slug.endswith(".md"):
            slug = slug + ".md"
        path = safe_child(SKILLS_DIR, slug)
        text = str(data.get("text", ""))
        path.write_text(text, encoding="utf-8")
        git_auto_commit([path], f"skills: update {slug}")
        return self.json({"ok": True, "path": str(path.relative_to(WIKI_DIR))})

    def bundles(self):
        BUNDLES_DIR.mkdir(parents=True, exist_ok=True)
        out = []
        for path in sorted(p for p in BUNDLES_DIR.iterdir() if p.is_dir()):
            manifest = read_json(path / "manifest.json", {})
            out.append({"name": path.name, "manifest": manifest})
        return out

    def bundle(self, name: str):
        root = safe_child(BUNDLES_DIR, name)
        files = {}
        for path in sorted(root.rglob("*")):
            if path.is_file():
                rel = path.relative_to(root).as_posix()
                if path.suffix == ".json":
                    files[rel] = read_json(path, None)
                elif path.suffix in {".md", ".txt"}:
                    files[rel] = path.read_text(encoding="utf-8")
        return {"name": name, "files": files}

    def save_bundle(self, name: str, data):
        root = safe_child(BUNDLES_DIR, name)
        files = data.get("files", {})
        written = []
        for rel, content in files.items():
            path = safe_child(root, rel)
            if path.suffix == ".json":
                write_json(path, content)
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(str(content), encoding="utf-8")
            written.append(path)
        if written:
            git_auto_commit(written, f"bundles: update {name}")
        return self.json({"ok": True, "name": name})

    def export_bundle(self, name: str):
        """Write outputs/review-bundles/<name>/wiki-export/<step>.md, one file
        per pipeline step in manifest.chain, combining that step's raw
        outputs/*.json with any matching human-edits, so the LLM Wiki sees
        the human-reviewed version of each research problem separately."""
        root = safe_child(BUNDLES_DIR, name)
        manifest = read_json(root / "manifest.json", {})
        steps = manifest.get("chain") or []
        if not steps:
            return self.json({"error": "manifest.json has no 'chain' steps to export"}, 400)
        notes = read_json(root / "human-edits" / "notes.json", [])
        export_dir = root / "wiki-export"
        export_dir.mkdir(parents=True, exist_ok=True)
        step_file = {
            "summary": "summary.json",
            "divide": "division-parts.json",
            "lin-events": "lin-events.json",
            "source-chain": "source-chain.json",
        }
        written = []
        for step in steps:
            fname = step_file.get(step, f"{step}.json")
            rows = read_json(root / "outputs" / fname, [])
            step_notes = [n for n in notes if n.get("step") == step]
            md = [f"# {step}", "", f"Bundle: `{name}`  ", f"Docs: {', '.join(manifest.get('doc_ids') or [])}", ""]
            if not rows:
                md.append("_(no output recorded for this step)_")
            for row in rows:
                doc_id = row.get("doc_id", "?")
                md.append(f"## {doc_id}")
                md.append("")
                md.append("```json")
                md.append(json.dumps(row, ensure_ascii=False, indent=2))
                md.append("```")
                md.append("")
            if step_notes:
                md.append("## Human notes")
                for n in step_notes:
                    md.append(f"- {n.get('text', n)}")
            out_path = export_dir / f"{step}.md"
            out_path.write_text("\n".join(md) + "\n", encoding="utf-8")
            written.append(out_path)
        git_auto_commit(written, f"wiki-export: {name}")
        return self.json({"ok": True, "name": name, "files": [str(p.relative_to(WIKI_DIR)) for p in written]})

    def attempt_file(self, rel: str):
        target = safe_child(ATTEMPT_DIR, rel)
        if not target.exists() or not target.is_file():
            return self.json({"error": "attempt file not found"}, 404)
        ctype = mimetypes.guess_type(target.name)[0] or "application/octet-stream"
        self.send_response(200)
        self.send_header("Content-Type", ctype + "; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(target.read_bytes())

    def body_json(self):
        length = int(self.headers.get("Content-Length", "0") or "0")
        raw = self.rfile.read(length).decode("utf-8")
        return json.loads(raw) if raw else {}

    def static(self, path: str):
        rel = "index.html" if path in {"/", ""} else path.lstrip("/")
        target = safe_child(STATIC_DIR, rel)
        if not target.exists() or not target.is_file():
            return self.json({"error": "not found"}, 404)
        ctype = mimetypes.guess_type(target.name)[0] or "application/octet-stream"
        self.send_response(200)
        self.send_header("Content-Type", ctype + "; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(target.read_bytes())

    def json(self, data, status: int = 200):
        payload = json.dumps(data, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(payload)


def main() -> None:
    BUNDLES_DIR.mkdir(parents=True, exist_ok=True)
    port = int(os.environ.get("LLM_WIKI_PORT", "8766"))
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print(f"LLM Wiki Review App: http://127.0.0.1:{port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
