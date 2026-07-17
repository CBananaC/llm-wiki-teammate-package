#!/bin/sh
set -eu

project_dir=$(CDPATH= cd -- "$(dirname -- "$0")/../.." && pwd)
cmp -s "$project_dir/AGENTS.md" "$project_dir/CLAUDE.md" || {
  echo "AGENTS.md and CLAUDE.md differ" >&2
  exit 1
}
echo "AGENTS.md and CLAUDE.md are identical"
