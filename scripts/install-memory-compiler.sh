#!/usr/bin/env bash
# Bootstraps claude-memory-compiler (the LLM Wiki self-evolving memory layer
# documented in CLAUDE.md) on a fresh machine. Idempotent: safe to re-run.
#
# Clones from Pedr0Leite/claude-memory-compiler, a fork of coleam00's original
# with vault-specific customizations (see that repo's README "This Install's
# Customizations" section) — NOT the upstream repo, which lacks them.
set -euo pipefail

REPO_URL="git@github.com:Pedr0Leite/claude-memory-compiler.git"
INSTALL_DIR="${HOME}/.claude/claude-memory-compiler"
VAULT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if [ -d "$INSTALL_DIR/.git" ]; then
  echo "claude-memory-compiler already present at $INSTALL_DIR — pulling latest."
  git -C "$INSTALL_DIR" pull --ff-only origin main
else
  echo "Cloning claude-memory-compiler into $INSTALL_DIR"
  git clone "$REPO_URL" "$INSTALL_DIR"
fi

if ! command -v uv >/dev/null 2>&1; then
  echo "uv not found. Install it first: https://docs.astral.sh/uv/getting-started/installation/" >&2
  exit 1
fi

(cd "$INSTALL_DIR" && uv sync)

echo
echo "Installed. Two manual steps remain:"
echo "1. Confirm config.py's VAULT_DIR points at this vault:"
echo "     $VAULT_DIR"
echo "   (edit $INSTALL_DIR/scripts/config.py if it doesn't)"
echo "2. Wire the hooks into ~/.claude/settings.json — merge the SessionStart/"
echo "   PreCompact/SessionEnd blocks from $INSTALL_DIR/.claude/settings.json"
echo "   (see AGENTS.md's 'Hook System' section for the exact format)."
