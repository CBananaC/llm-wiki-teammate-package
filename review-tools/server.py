#!/usr/bin/env python3
"""Local file server/API for the formal and sample review tools.

This server is deliberately small. It reads and writes only inside the local
DH Project tree so the review UI can sync skills, load review bundles, and export
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
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urlparse
from urllib.request import Request, urlopen


REVIEW_DIR = Path(__file__).resolve().parent
PROJECT_DIR = REVIEW_DIR.parent
WIKI_DIR = PROJECT_DIR  # retained as the git/project-root name used below
WORKFLOW_DIR = REVIEW_DIR / "(4) workflow"
SHARED_DIR = REVIEW_DIR / "shared data"
FORMAL_DIR = REVIEW_DIR / "(1) formal"
SAMPLE_DIR = REVIEW_DIR / "(2) sample"
MODEL_COMPARISON_DIR = REVIEW_DIR / "(3) model-output-comparison"
SKILLS_DIR = PROJECT_DIR / "tool" / "skills md"
BUNDLES_DIR = SHARED_DIR / "review-bundles"
STAGE1_PATH = SHARED_DIR / "stage1_original_text.json"
PROJECT_LOG_PATH = PROJECT_DIR / "PROJECT_LOG.md"
# The timeline page's working state (events, notes, AI chat history -- everything under the
# in-browser `EDITS` object) used to live ONLY in the browser's localStorage, which has a hard
# ~5-10MB/origin cap. A research corpus this size (full quote text, provenance chains, chat
# history) outgrows that fairly easily, and once it does every future edit silently fails to
# save. Disk has no such practical limit, so this file becomes the primary persisted copy;
# localStorage is kept only as a fast local cache/fallback for when this server isn't running
# (e.g. the page opened directly as file://).
EDITS_PATH = FORMAL_DIR / "formal_all.data"
# Separate, disk-backed working state for the isolated sample page
# (`review-tools/(2) sample/index.html`). Kept in its own
# file so sample/presentation data auto-loads and persists across reloads WITHOUT
# ever touching the formal timeline overlay above. Served via /api/edits-sample.
BLANK_EDITS_PATH = SAMPLE_DIR / "sample_all.data"
AI_PROXY_URL = os.environ.get("LLM_WIKI_AI_URL", "http://127.0.0.1:8767").rstrip("/")

# Source files shown by the interactive AI-loop map.  Keep this list explicit:
# the browser can inspect the real workflow implementation without gaining a
# general-purpose file-reading endpoint.
WORKFLOW_SOURCE_FILES = (
    "tool/skills md/zhu-response-pairing.md",
    "tool/scripts py/run_zhu_pairing.py",
    "tool/skills md/yu-response-pairing.md",
    "tool/scripts py/run_yu_pairing.py",
    "tool/skills md/quick-summary.md",
    "tool/skills md/divide-into-parts.md",
    "tool/scripts py/summarize_stage1_shangzou_vertex.py",
    "tool/skills md/zhu-review-loop.md",
    "tool/scripts py/run_zhu_review_loop.py",
    "tool/scripts py/run_review_bundle_test.py",
    "tool/skills md/extract-lin-actions.md",
    "tool/skills md/extract-qing-actions-done.md",
    "tool/skills md/extract-qing-actions-planned.md",
    "tool/skills md/extract-qing-nonmilitary-actions.md",
    "tool/skills md/trace-source-chain.md",
    "tool/skills md/extract-zhupi.md",
    "tool/skills md/edict-match.md",
    "tool/skills md/extract-emperor-action.md",
    "tool/skills md/official-response.md",
    "tool/skills md/shangyu-review-loop.md",
    "tool/skills md/response-timeliness.md",
    "tool/scripts py/run_shangyu_loop_prompt.py",
    "tool/scripts py/merge_pairs.py",
    "review-tools/README.md",
    "review-tools/server.py",
)

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
            if path.startswith("/api/ai/"):
                return self.ai_proxy("GET", path.removeprefix("/api/ai"), parsed.query)
            if path == "/api/health":
                return self.json({"ok": True})
            if path == "/api/status":
                return self.json({"text": PROJECT_LOG_PATH.read_text(encoding="utf-8")})
            if path in {"/api/edits", "/api/edits-formal"}:
                return self.json(read_json(EDITS_PATH, {}))
            if path in {"/api/edits-blank", "/api/edits-sample"}:
                return self.json(read_json(BLANK_EDITS_PATH, {}))
            if path == "/api/skills":
                return self.json(self.skills())
            if path == "/api/workflow-sources":
                return self.json(self.workflow_sources())
            if path == "/api/bundles":
                return self.json(self.bundles())
            if path.startswith("/api/bundles/"):
                name = unquote(path.removeprefix("/api/bundles/"))
                return self.json(self.bundle(name))
            if path == "/api/current-timeline":
                return self.json({
                    "html": str((FORMAL_DIR / "index.html").relative_to(PROJECT_DIR)),
                    "data": str(STAGE1_PATH.relative_to(PROJECT_DIR)),
                })
            if path in {"/", "/app", "/app/", "/formal", "/formal/"}:
                return self.review_file(FORMAL_DIR, "index.html")
            if path.startswith("/formal/"):
                return self.review_file(FORMAL_DIR, unquote(path.removeprefix("/formal/")))
            if path in {"/sample", "/sample/"}:
                return self.review_file(SAMPLE_DIR, "index.html")
            if path.startswith("/sample/"):
                return self.review_file(SAMPLE_DIR, unquote(path.removeprefix("/sample/")))
            if path in {"/model-output-comparison", "/model-output-comparison/"}:
                return self.review_file(MODEL_COMPARISON_DIR, "index.html")
            if path.startswith("/model-output-comparison/"):
                return self.review_file(MODEL_COMPARISON_DIR, unquote(path.removeprefix("/model-output-comparison/")))
            if path.startswith("/shared/"):
                return self.review_file(SHARED_DIR, unquote(path.removeprefix("/shared/")))
            if path in {"/status", "/status/"}:
                return self.text(PROJECT_LOG_PATH.read_text(encoding="utf-8"), "text/markdown; charset=utf-8")
            if path in {"/workflow", "/workflow/", "/workflow.html"}:
                return self.workflow_file("index.html")
            if path.startswith("/workflow/"):
                rel = unquote(path.removeprefix("/workflow/"))
                return self.workflow_file(rel)
            return self.json({"error": "not found"}, 404)
        except Exception as exc:
            return self.json({"error": str(exc)}, 500)

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        path = parsed.path
        try:
            if path.startswith("/api/ai/"):
                return self.ai_proxy("POST", path.removeprefix("/api/ai"), parsed.query)
            data = self.body_json()
            if path in {"/api/edits", "/api/edits-formal"}:
                # No git_auto_commit here on purpose: this saves on essentially every click
                # (much higher frequency than a deliberate skill/bundle edit), so committing
                # every write would flood history with noise. Deliberately snapshot it yourself
                # (git add/commit "review-tools/(1) formal/formal_all.data") when you want
                # a checkpoint.
                write_json(EDITS_PATH, data)
                return self.json({"ok": True})
            if path in {"/api/edits-blank", "/api/edits-sample"}:
                # isolated sample-page state; never commits, never touches the real overlay
                BLANK_EDITS_PATH.parent.mkdir(parents=True, exist_ok=True)
                write_json(BLANK_EDITS_PATH, data)
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

    def workflow_sources(self):
        files = {}
        for rel in WORKFLOW_SOURCE_FILES:
            path = safe_child(WIKI_DIR, rel)
            if path.is_file():
                files[rel] = {
                    "path": rel,
                    "language": "python" if path.suffix == ".py" else "markdown",
                    "text": path.read_text(encoding="utf-8"),
                }
        return {"files": files}

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
        manifest = read_json(root / "manifest.json", {})
        files = {}
        for path in sorted(root.rglob("*")):
            if path.is_file():
                rel = path.relative_to(root).as_posix()
                if rel == "manifest.json":
                    continue
                if path.suffix == ".json":
                    files[rel] = read_json(path, None)
                elif path.suffix in {".md", ".txt"}:
                    files[rel] = path.read_text(encoding="utf-8")
        return {"name": name, "manifest": manifest, "files": files}

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

    def review_file(self, root: Path, rel: str):
        target = safe_child(root, rel)
        if not target.exists() or not target.is_file():
            return self.json({"error": "review-tool file not found"}, 404)
        ctype = mimetypes.guess_type(target.name)[0] or "application/octet-stream"
        self.send_response(200)
        self.send_header("Content-Type", ctype + "; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(target.read_bytes())

    def workflow_file(self, rel: str):
        target = safe_child(WORKFLOW_DIR, rel)
        if not target.exists() or not target.is_file():
            return self.json({"error": "workflow file not found"}, 404)
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

    def ai_proxy(self, method: str, path: str, query: str = ""):
        target = AI_PROXY_URL + path + (("?" + query) if query else "")
        body = None
        if method == "POST":
            length = int(self.headers.get("Content-Length", "0") or "0")
            body = self.rfile.read(length)
        upstream = Request(
            target,
            data=body,
            method=method,
            headers={"Content-Type": self.headers.get("Content-Type", "application/json")},
        )
        try:
            with urlopen(upstream, timeout=150) as response:
                payload = response.read()
                status = response.status
                content_type = response.headers.get("Content-Type", "application/json; charset=utf-8")
        except HTTPError as exc:
            payload = exc.read()
            status = exc.code
            content_type = exc.headers.get("Content-Type", "application/json; charset=utf-8")
        except (URLError, TimeoutError) as exc:
            return self.json({
                "error": "本機 AI 服務未啟動。請重新執行 run-local.py，並確認已安裝 gemini-proxy/requirements.txt。",
                "detail": str(exc),
            }, 503)
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(payload)

    def text(self, value: str, content_type: str = "text/plain; charset=utf-8"):
        payload = value.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(payload)

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
    print(f"DH Project review tools: http://127.0.0.1:{port}")
    print(f"  Formal: http://127.0.0.1:{port}/formal")
    print(f"  Sample: http://127.0.0.1:{port}/sample")
    print(f"  Model comparison: http://127.0.0.1:{port}/model-output-comparison")
    server.serve_forever()


if __name__ == "__main__":
    main()
