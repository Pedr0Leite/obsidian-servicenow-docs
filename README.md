# obsidian-servicenow-docs

Obsidian vault and AI-navigable knowledge base for ServiceNow platform development.

## Structure

```
obsidian-servicenow-docs/
│
├── CLAUDE.md                     # AI agent guide (Claude, Copilot, Codex, etc.)
├── README.md                     # This file
│
├── ServiceNowOfficialDocs/       # Official ServiceNow docs, converted to markdown
│   ├── INDEX.md                  # Master navigation index — start here
│   ├── <product-area>/           # ~50 product directories (e.g. it-service-management/, api-reference/)
│   ├── delta-*/                  # Per-release delta docs (Washington DC/Yokohama/Zurich → Australia)
│   ├── roles-by-product/         # Role & permission reference by product
│   └── now-assist-ai/            # Custom curated notes (labs, support cases, production)
│       └── llms.txt              # LLM-optimized index for this section
│
└── Notion/                       # Personal Notion export (ServiceNow workspace)
    └── ServiceNow/                # Topic folders: AI & VA, CMDB, Flow Designer, Security & ACL, etc.
```

## Content types

| Location | Content |
|----------|---------|
| `ServiceNowOfficialDocs/<product-area>/` | Official ServiceNow product documentation, ~46,000 files |
| `ServiceNowOfficialDocs/delta-*/` | Per-release delta docs tracking what changed between versions |
| `ServiceNowOfficialDocs/roles-by-product/` | Role definitions and permission reference by product |
| `ServiceNowOfficialDocs/now-assist-ai/` | Custom curated notes — not official docs |
| `Notion/ServiceNow/` | Exported personal notes from Notion, organized by topic |

## Navigation

Use **`ServiceNowOfficialDocs/INDEX.md`** to find any official-docs topic without browsing directories.

For custom `now-assist-ai/` content, use **`ServiceNowOfficialDocs/now-assist-ai/llms.txt`**.

For personal notes, browse `Notion/ServiceNow/` by topic folder.

---

*Official documentation content sourced from ServiceNow. `Notion/` and `now-assist-ai/` content is independently authored.*
