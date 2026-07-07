# obsidian-servicenow-docs

Obsidian vault and AI-navigable knowledge base for ServiceNow platform development, plus a Claude Code agent pipeline for building ServiceNow scoped apps.

## Structure

```
obsidian-servicenow-docs/
│
├── CLAUDE.md                     # AI agent guide (Claude, Copilot, Codex, etc.) — read this first
├── README.md                     # This file
│
├── ServiceNowOfficialDocs/       # Official ServiceNow docs, converted to markdown
│   ├── INDEX.md                  # Master navigation index — start here
│   ├── <product-area>/           # ~50 product directories (e.g. it-service-management/, api-reference/)
│   ├── delta-*/                  # Per-release delta docs (Washington DC/Yokohama/Zurich → Australia)
│   ├── roles-by-product/         # Role & permission reference by product
│   ├── support-and-troubleshooting/  # ~3,900 official KB troubleshooting articles, by product area
│   ├── servicenow-dev-program/   # Vendored community code-snippets repo (~1,470 files)
│   └── now-assist-ai/            # Custom curated notes (K26 labs, support cases, production)
│       └── llms.txt              # LLM-optimized index for this section
│
├── Notion/                       # Personal Notion export (ServiceNow workspace)
│   └── ServiceNow/                # Topic folders: AI & VA, CMDB, Flow Designer, Security & ACL, etc.
│
├── Applications/                 # Notes on in-house/custom ServiceNow applications
│   └── capacity-planner/
│
├── ClaudeAgents/                 # Claude Code agent team for end-to-end ServiceNow dev (see its README)
│   └── orchestrator, ba-agent, architect, governance, developer, tester, bug-hunter
│
├── ClaudeSkills/                 # Claude Code skills (agent-dispatch, todo-fixer)
│
└── scripts/                      # One-off maintenance scripts (tagging, cross-linking)
```

## Content types

| Location | Content |
|----------|---------|
| `ServiceNowOfficialDocs/<product-area>/` | Official ServiceNow product documentation, ~46,000 files |
| `ServiceNowOfficialDocs/delta-*/` | Per-release delta docs tracking what changed between versions |
| `ServiceNowOfficialDocs/roles-by-product/` | Role definitions and permission reference by product |
| `ServiceNowOfficialDocs/support-and-troubleshooting/` | Official KB articles, tagged and cross-linked by product area |
| `ServiceNowOfficialDocs/servicenow-dev-program/` | Vendored community code snippets (client/server scripts, integrations, SDK) |
| `ServiceNowOfficialDocs/now-assist-ai/` | Custom curated notes — not official docs |
| `Notion/ServiceNow/` | Exported personal notes from Notion, organized by topic |
| `Applications/` | Notes on custom in-house ServiceNow applications |
| `ClaudeAgents/` | Multi-agent pipeline (BA → Architect → Governance → Developer → Tester) for building ServiceNow features |
| `ClaudeSkills/` | Claude Code skills invoked during agent work |
| `scripts/` | Standalone Python scripts for vault maintenance (tagging, cross-linking) |

## Navigation

Use **`ServiceNowOfficialDocs/INDEX.md`** to find any official-docs topic without browsing directories.

For custom `now-assist-ai/` content, use **`ServiceNowOfficialDocs/now-assist-ai/llms.txt`**.

For personal notes, browse `Notion/ServiceNow/` by topic folder.

For building a new ServiceNow feature end-to-end, see **`ClaudeAgents/README.md`** and start with the `orchestrator` agent.

---

*Official documentation content sourced from ServiceNow. `Notion/`, `Applications/`, and `now-assist-ai/` content is independently authored.*
