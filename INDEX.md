---
aliases: [Vault Index, Second Brain Index]
area: vault-index
tags: [index, routing, navigation]
---

# Vault INDEX — where everything lives

Top-level routing map for `obsidian-servicenow-docs`. **Read this to decide
*where* to look; read the linked layer index or note to get the answer.**

This file is deliberately named `INDEX.md` (uppercase). sn-rag skips `index.md`
(lowercase) as a navigation dump, but indexes `INDEX.md` — so this document is
retrievable and is meant to surface as a routing hit when a query does not match
content directly.

## The layers, and when to use each

| Layer | Files | What it is | Go here when |
|---|---|---|---|
| **[[ServiceNowOfficialDocs/INDEX\|ServiceNowOfficialDocs/]]** | ~51,250 | ServiceNow vendor documentation, curated and effectively immutable | "How does the platform do X?" — APIs, tables, plugins, configuration, release notes |
| **[[Notion/INDEX\|Notion/]]** | ~287 | Personal ServiceNow notes migrated from Notion | "How did *we* do X?" — practical recipes, gotchas, client-specific patterns |
| **[[wiki/index\|wiki/]]** | ~39 | LLM-compiled synthesis layer (entities, concepts, queries, syntheses) | Fastest route to a *synthesized* answer across sources. Written by claude-memory-compiler, continuously |
| **[[Applications/INDEX\|Applications/]]** | ~15 | In-house applications we designed or built | "Has this been solved before?" — architecture, data models, decisions, backlogs |
| **[[other-applications/INDEX\|other-applications/]]** | ~1 | Third-party / vendor system documentation that is not ServiceNow's | ERP and other external system internals — endpoints, limits, governance |
| **ClaudeAgents/** | ~9 | Agent definitions for the delivery pipeline — see `ClaudeAgents/README.md` | Choosing which agent runs a task (ba-agent, architect, governance, developer, tester, bug-hunter) |
| **ClaudeSkills/** | ~2 | Reusable skill definitions (`agent-dispatch`, `todo-fixer`) | Extending or invoking a packaged workflow |
| **raw/** | ~41 | Unprocessed capture — `raw/inbox/` (drop zone) and `raw/sessions/` (daily logs, auto-archived after ~30 days) | Recovering what happened on a specific date, or finding material not yet compiled into `wiki/` |
| **graphify/** | ~2 | Generated code-graph reports, regenerated wholesale | Structural view of a codebase (`capacity-planner`, `sn-instance-scan`) |
| **Dashboards/**, **Clippings/** | ~2 | Dashboard notes; saved web clippings | Rarely a first stop |

## Choosing between the two doc sets

`ServiceNowOfficialDocs/` says what the platform *can* do. `Notion/` and `wiki/`
say what *we* did and what went wrong. When they disagree, the vendor doc wins on
capability and ours wins on practice — cite both and say which is which.

## Retrieval hints for sn-rag

- Agent `servicenow` → `ServiceNowOfficialDocs/` only
- Agent `personal` → `Notion/`, `wiki/`, `Applications/`, `other-applications/`, `ClaudeAgents/`, `ClaudeSkills/`, `raw/`, `graphify/`, `Dashboards/`, `Clippings/`
- Agent `general` → both

Use `sn_lexical` for exact identifiers (table names, API names, error strings);
dense search paraphrases and will miss a literal `sn_install_base_sold_product`.

`index.md` files are **excluded from the index by design** — 54 of them, 19.5 MB
of link dumps. Semantic search replaces them. Do not reintroduce them as content.

## Writing conventions

- App-specific facts go to `Applications/<app>/`, **not** `wiki/entities/`. The
  wiki entity page is a thin pointer to the app folder.
- A new app with no folder yet → create `Applications/<app>/<app>.md` as the
  overview note, then add the pointer page under `wiki/entities/`.
- Every top-level directory containing `.md` must be classified in sn-rag's
  `SOURCE_BY_TOP_DIR`, or ingest fails loudly. Adding a new top-level folder
  means updating `config.py` in the `second-brain` repo.

See `CLAUDE.md` at the vault root for the full AI Agent Guide.
