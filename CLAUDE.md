# AI Agent Guide — obsidian-servicenow-docs

This file is for any AI assistant (Claude, Copilot, Codex, Gemini, etc.) that has access to this vault.
Read it before touching anything else. It will save you tokens.

---

## What this vault is

A ServiceNow knowledge base maintained by a ServiceNow developer at Unit4 (an ERP/HCM vendor running ServiceNow as its platform).

Two layers of content:

| Layer | Where | What |
|-------|-------|------|
| Official docs | `markdown/` (mirrored as flat dirs at root) | ~46,000 ServiceNow product documentation files, covering every platform area from ITSM to AI to security |
| Custom knowledge | `now-assist-ai/` | Curated notes from real implementations: K26 labs, support cases, production incidents |

The custom layer is more valuable for implementation questions. The official layer is the authoritative reference.

---

## How to navigate efficiently (read this before opening files)

**Do not scan directories blindly. Use the index.**

1. Read `INDEX.md` — one file, maps every directory to a description + keywords. Find the right path in seconds.
2. Go directly to that directory and read only what you need.
3. For `now-assist-ai/` specifically, read `now-assist-ai/llms.txt` — it lists every custom note with a description.

**Keyword shortcuts** (common questions → where to look):

| Topic | Directory |
|-------|-----------|
| Scripting, GlideRecord, GlideSystem, APIs | `api-reference/` |
| Flow Designer, subflows, actions | `build-workflows/` |
| AI Agents, ReAct loop, sn_aia_* tables | `now-assist-ai/ai-agents/` |
| AI Search, vector/semantic search, AIS | `now-assist-ai/ai-search/` |
| Now Assist skills, Skill Kit, prompts | `intelligent-experiences/` |
| CMDB, CI classes, discovery, CSDM | `servicenow-platform/` |
| ATF, test generation, SDK, CLI | `application-development/` |
| ITSM, incidents, changes, problems | `it-service-management/` |
| Security, ACLs, encryption, SSO | `platform-security/` |
| Performance Analytics, reports | `now-intelligence/` |

---

## ServiceNow domain context

Load this into your context — it prevents hallucination and reduces the need to look up basics.

**Platform fundamentals:**
- Everything runs server-side as JavaScript (Rhino engine). GlideRecord is the ORM. Business Rules, Script Includes, and Flow Designer are the main extension points.
- Scoped apps isolate code in a namespace (`x_vendor_appname`). Global scope has no prefix.
- Tables extend `task` (incident, change, problem, sc_request, etc.). CMDB extends `cmdb_ci`.
- The MID Server bridges ServiceNow to on-premise systems.

**Release naming** (most recent → oldest): Zurich → Yokohama → Xanadu → Washington DC → Vancouver → Utah → Tokyo. Files in `delta-*` dirs track changes between releases.

**Now Assist / AI specifics:**
- AI Agents use a ReAct (Reason + Act) loop. Runtime state lives in `sn_aia_execution_plan` / `sn_aia_execution_task` tables.
- Skills are the AI capability unit. The Skill Kit (`now-assist-ai/`) lets you build custom ones.
- AI Search (AIS) is vector/semantic search. Filters apply *after* ANN similarity — adding filters increases traversal cost, it does not reduce it.
- Generative AI features go through the Generative AI Controller (`intelligent-experiences/generative-ai-controller/`).

**Unit4 context:**
- Unit4 is an ERP/HCM SaaS vendor. Their ServiceNow implementation is customer-facing (CSM/ESM) with heavy use of AI Search for case deflection and AI Agents for automation.

---

## When writing or generating ServiceNow code

- Prefer Flow Designer over Business Rules for new logic where possible.
- Scoped app code must not use `GlideRecord` without proper ACL checks.
- Use `gs.getProperty()` for configurable values, never hard-code sys_ids.
- ATF tests should cover happy path + at least one negative case.
- Check `application-development/servicenow-sdk/` for local dev tooling (TypeScript, now-sdk).

---

## Adding new custom knowledge

1. Create note in `now-assist-ai/<topic>/`
2. Add entry to `now-assist-ai/llms.txt` (pattern in `now-assist-ai/llms_template.txt`)
3. Add row to relevant section in `INDEX.md` if it's a new area
