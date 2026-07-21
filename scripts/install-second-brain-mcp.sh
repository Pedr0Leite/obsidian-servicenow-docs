#!/usr/bin/env bash
# Bootstraps smart-connections-mcp, the semantic-search MCP server the
# ClaudeAgents pipeline (BA/Architect/Developer) uses to query this vault as
# a "second brain" before planning or executing. Idempotent: safe to re-run.
#
# Clones dan6684/smart-connections-mcp, which reads the local embedding index
# built by the Smart Connections Obsidian plugin (already installed in this
# vault at .obsidian/plugins/smart-connections/).
set -euo pipefail

REPO_URL="https://github.com/dan6684/smart-connections-mcp.git"
INSTALL_DIR="${HOME}/.claude/smart-connections-mcp"
VAULT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if [ -d "$INSTALL_DIR/.git" ]; then
  echo "smart-connections-mcp already present at $INSTALL_DIR — pulling latest."
  git -C "$INSTALL_DIR" pull --ff-only origin main
else
  echo "Cloning smart-connections-mcp into $INSTALL_DIR"
  git clone "$REPO_URL" "$INSTALL_DIR"
fi

if ! command -v uv >/dev/null 2>&1; then
  echo "uv not found. Install it first: https://docs.astral.sh/uv/getting-started/installation/" >&2
  exit 1
fi

(cd "$INSTALL_DIR" && uv venv && uv pip install -r requirements.txt)

echo
echo "Installed. Manual steps remain:"
echo "1. Open this vault in Obsidian at least once with the Smart Connections"
echo "   plugin enabled, so it builds the local embedding index"
echo "   (.smart-env/multi/*.ajson) — that's what this MCP server reads."
echo "   On a ~46k-file vault the first embedding pass takes a while; let it finish."
echo "2. Register the server globally in ~/.mcp.json (merge this block):"
echo
cat <<EOF
{
  "mcpServers": {
    "smart-connections": {
      "command": "$INSTALL_DIR/.venv/bin/python",
      "args": ["$INSTALL_DIR/server.py"],
      "env": {
        "OBSIDIAN_VAULT_PATH": "$VAULT_DIR"
      }
    }
  }
}
EOF
echo
echo "3. Verify: claude mcp list"
echo "   Expected: smart-connections: .venv/bin/python server.py - Connected"
