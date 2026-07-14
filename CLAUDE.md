# AI Agent Guide — obsidian-servicenow-docs
This file is for any AI assistant (Claude, Copilot, Codex, Gemini, etc.) that has access to this vault.
Read it before touching anything else. It will save you tokens.
---
## Communication style (caveman mode)
Terse replies only. No filler words (the, is, am, are). 3-6 word sentences. Run tools first, show results, stop. No narration.
---
## What this vault is
A ServiceNow knowledge base maintained by a ServiceNow developer at Unit4 (an ERP/HCM vendor running ServiceNow as its platform).
Three layers of content:
| Layer | Where | What |
|-------|-------|------|
| Official docs | `markdown/` (mirrored as flat dirs at root) | ~46,000 ServiceNow product documentation files, covering every platform area from ITSM to AI to security |
| Custom knowledge | `now-assist-ai/` | Curated notes from real implementations: K26 labs, support cases, production incidents |
| Agent memory | `logs/`, `chats/`, `graphify/` | Session logs, imported conversations, and auto-generated codebase knowledge graphs — persistent memory across sessions |
The custom layer is more valuable for implementation questions. The official layer is the authoritative reference. The memory layer is how you pick up where the last session left off.
---
## How to navigate efficiently (read this before opening files)
**Do not scan directories blindly. Use the index.**
1. Read `INDEX.md` — one file, maps every directory to a description + keywords. Find the right path in seconds.
2. Go directly to that directory and read only what you need.
3. For `now-assist-ai/` specifically, read `now-assist-ai/llms.txt` — it lists every custom note with a description.
4. For questions about a codebase that has a graph in `graphify/<project>/`, query the graph (or the repo's `graphify-out/graph.json`) before opening raw source files.
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
| Past sessions, decisions, pending work | `logs/` |
| Code structure of a mapped project | `graphify/<project>/` |
---
## Session memory (persistent context across sessions)
This vault is your long-term memory. Two commands keep it alive:
### /resume
When you receive this command:
1. Read the 3 most recent session logs in `logs/`
2. Read the relevant project/application notes (`Applications/`, `now-assist-ai/`) for open decisions
3. Summarize: current state, decisions in force, what's left to do
### /save
When you receive this command:
1. Create a session log at `logs/YYYY-MM-DD-<short-description>.md`
2. Record: what was done, decisions made, pending items
3. Add `[[wikilinks]]` to every note created or modified this session
4. If the vault is a git repo, commit and push
### Log note rules
- Frontmatter per vault convention (`aliases`, `area: session-log`, `tags`)
- Never delete or rewrite past logs — append new ones
---
## Graphify (codebase knowledge graphs)
`graphify/<project>/` holds auto-generated notes mapping a codebase (one note per function/module). The source of truth is the `graphify-out/` folder inside each project repo.
### 3-layer query rule (when working on a mapped codebase)
1. **First:** query `graphify-out/graph.json` in the repo (or the notes in `graphify/<project>/`) to understand structure and connections
2. **Second:** check this vault for decisions, progress, and context (`logs/`, `Applications/`, `now-assist-ai/`)
3. **Third:** only read raw source files when editing, or when layers 1–2 don't have the answer
### Rebuilding
- After structural changes: `graphify . --update` from the repo root (only reprocesses modified files)
- New project: `graphify . --obsidian --obsidian-dir <vault>/graphify/<project>`
- The graph is persistent — do NOT rebuild every session
### Do NOT
- Edit anything under `graphify/` or `graphify-out/` manually — it gets regenerated
- Add frontmatter, tags, or wikilinks to graphify notes (the generator owns them)
- Re-read an entire codebase when the graph already has the answer
- Run graphify against this vault itself — it is for code repos, not the docs
---
## Chat imports
`chats/code/` holds Claude Code conversations exported via `claude-conversation-extractor`. They are reference material, tagged `chat-import`.
- Treat them as read-only history — do not edit
- When a chat contains a durable decision, promote it: create a proper note in the relevant topic folder and wikilink back to the chat
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
## Everything in this vault is Markdown
This is an Obsidian vault — non-`.md` files (raw `.js` scripts, exports, etc.) don't get tags, frontmatter, or graph/backlink connections, so they're invisible to search and easy to lose track of. Convert them:
1. Use the `obsidian-markdown` skill for syntax (frontmatter, wikilinks, callouts) and the `obsidian-cli` skill to verify the result is indexed (`obsidian search`, `obsidian read`).
2. One `.md` note per source file, same base name, in the same folder. Delete the original non-md file — don't keep both.
3. Frontmatter: `aliases` (clean title), `area`, `tags` (topical, matching the vault's existing tag vocabulary where possible).
4. Body: a short description of what it does/is, then the original content — code goes in a fenced block (` ```javascript `), not an embed.
5. A `## Related` section of `[[wikilinks]]` to topically-overlapping existing notes, and update those notes' own `## Related` sections to link back (bidirectional).
6. Add a row to `INDEX.md` (new section if it's a new area, per the pattern above).
This matches the convention already used across `Notion/ServiceNow/` — see any note there for a worked example.
**Exception:** the conversion rules above do not apply to `graphify/`, `logs/`, or `chats/` — those are machine-generated/imported and follow their own rules (see their sections above). Do not add them to `INDEX.md`.
---
## LLM Wiki (Karpathy pattern)
This vault runs the [LLM Wiki pattern](https://github.com/karpathy): raw sources feed a persistent, LLM-maintained synthesis layer at `wiki/`, instead of re-deriving synthesis on every question.
### The three layers
| Layer | Where | Owner |
|-------|-------|-------|
| Raw sources | `ServiceNowOfficialDocs/`, `Notion/ServiceNow/`, `Applications/`, `chats/` | You (human) — curated, immutable. Never edit these as part of wiki maintenance. New drops land in `raw/inbox/` first. |
| Wiki | `wiki/` (`entities/`, `concepts/`, `syntheses/`, `queries/`, `index.md`, `log.md`) | The LLM — owns this entirely, keeps it current. |
| Schema | This file | Co-evolved by both. |
`wiki/entities/` = concrete things (custom apps, integrations, script includes). `wiki/concepts/` = cross-cutting ServiceNow topics (ACLs, GlideRecord patterns, Flow Designer, scoped apps, AI Agents, AI Search, ...). `wiki/syntheses/` = evolving cross-source theses. `wiki/queries/` = good answers filed back so they compound instead of vanishing into chat history.
#### Application-specific facts route to `Applications/<app>/`, not `wiki/entities/`
If a source (session, ingest, or compile) is about a specific in-house app that already has (or should have) an `Applications/<app>/` folder, its **detail** belongs in that folder, not in `wiki/entities/<app>.md`. `wiki/entities/<app>.md` stays a thin pointer + one-paragraph summary — see [[capacity-planner]] for the pattern: architecture, schema, decisions, ACLs, etc. all live under `Applications/capacity-planner/`, and the wiki entity page just links to them.
- New app, no folder yet → create `Applications/<app>/<app>.md` as the overview note (same shape as `capacity-planner.md`) and put detail there; the wiki entity page links to it.
- Existing app folder → append to (or update) the most relevant existing note in that folder rather than duplicating into the wiki page.
- Non-app-specific facts from the same source (a general ServiceNow gotcha, a platform concept) still route to `wiki/concepts/` as normal — only the app-specific portion moves to `Applications/`.
### Ingest (new source arrives)
1. Read the source (from `raw/inbox/` or wherever it landed).
2. Discuss key takeaways with the user; don't just summarize silently.
3. Write/update the relevant page(s): app-specific detail → `Applications/<app>/` (see above, thin pointer only in `wiki/entities/`), everything else → `wiki/entities/` or `wiki/concepts/`. Link to the source, don't copy its content in full.
4. Update `wiki/index.md`.
5. Append an entry to `wiki/log.md` (`## [YYYY-MM-DD] ingest | <title>`).
6. Move the source out of `raw/inbox/` into its proper home (e.g. `Notion/ServiceNow/<topic>/`, `Applications/<app>/`) if it's staying in the vault long-term.
### Query (user asks a question)
1. Read `wiki/index.md` first to find relevant pages.
2. Drill into the linked wiki pages, then the raw sources they point to, as needed.
3. Synthesize an answer with citations (file paths / wikilinks).
4. If the answer is reusable (a comparison, an analysis, a connection), offer to file it into `wiki/queries/` or `wiki/syntheses/` and append a `query` entry to `wiki/log.md`.
### Lint (periodic health check, on request)
Check for: orphan wiki pages (no inbound links), concept pages that are now stale vs. newer sources, Notion topic folders in `wiki/index.md`'s "not yet promoted" list that have accumulated enough material to deserve a real concept page, missing cross-references between concept pages. Append a `lint` entry to `wiki/log.md` summarizing findings — don't fix silently, propose first.
### Rules
- Never delete existing vault content while maintaining the wiki. Promote/link, don't rewrite.
- Don't pre-create concept stub pages for topics nobody has asked about — create them the first time a query/ingest actually needs to synthesize across sources on that topic (see `wiki/index.md`'s Notion topic folder list).
- `wiki/` pages use the same frontmatter convention as the rest of the vault (`aliases`, `area: entity|concept|synthesis|query|wiki-index`, `tags`) plus a `## Related` section.

---
## Self-evolving memory (claude-memory-compiler)
This vault's wiki also self-updates from live Claude Code sessions — in *any* project, not just this vault — via **[Pedr0Leite/claude-memory-compiler](https://github.com/Pedr0Leite/claude-memory-compiler)** (a fork of [coleam00/claude-memory-compiler](https://github.com/coleam00/claude-memory-compiler) with vault-specific customizations — see that fork's README "This Install's Customizations" section; **do not install from the upstream repo**, it lacks the `Applications/<app>/` routing fix and any other local patches), installed globally at `~/.claude/claude-memory-compiler/` and wired to this vault as its one shared ServiceNow "second brain". Compiler code + operational state (`state.json`, logs) live entirely outside the vault; only compiled knowledge lands here.

**Setup on a new machine:** run `scripts/install-memory-compiler.sh` from this repo. It clones the fork (not upstream) into `~/.claude/claude-memory-compiler/`, runs `uv sync`, and prints the two remaining manual steps (confirm `config.py`'s `VAULT_DIR`, wire hooks into `~/.claude/settings.json`).
### The new raw layer: automatic session capture
`raw/sessions/YYYY-MM-DD.md` is a **new, automatic** raw-source type, distinct from the manual `/save` → `logs/` flow above:
| | `logs/` (existing) | `raw/sessions/` (new) |
|---|---|---|
| Written by | You, via `/save` | The compiler's hooks, automatically, every session |
| Scope | This vault only | Any project, any repo — tagged by project slug |
| Curation | Manual, reviewed | Raw, unreviewed until compiled |
| Committed/pushed | Yes (`/save` does this) | No — stays local until `compile.py` promotes it into `wiki/` |
Each session block is tagged with a project slug (derived from the session's `cwd`) and absolute path, e.g.:
```markdown
### Session 14:32 — capacity-planner
- **Project:** `capacity-planner`
- **Path:** `/home/pedro/Documents/Programacao/Github/capacity-planner`
- **Session ID:** `abc123`
- **Started:** `2026-07-13 14:32`

...extracted facts/decisions/gotchas, each prefaced with the project slug...
```
### How it connects to the existing ingest/query/lint flow
- **Ingest** — `compile.py` runs this automatically (after 6 PM local time, once a day, if that day's `raw/sessions/` log changed) or on demand (`uv run python scripts/compile.py` from `~/.claude/claude-memory-compiler/`). It follows the *exact same* ingest steps as the manual flow above, **including the `Applications/<app>/` routing rule above** — a session tagged as being about a specific in-house app files its detail there, not into `wiki/entities/`. It reads this file as schema, writes pages, updates `wiki/index.md`, appends to `wiki/log.md` — but uses log-entry type `auto-ingest` instead of `ingest` to distinguish machine-driven compiles from human-directed ones.
- **Query** — `uv run python scripts/query.py "question" --file-back` runs the same query flow as above, non-interactively, and can file the answer into `wiki/queries/`.
- **Lint** — `uv run python scripts/lint.py` adds 7 automated structural/LLM checks on top of the manual lint pass already described above (broken links, orphans, stale articles, contradictions, sparse articles, missing backlinks, uncompiled sources).
- Session logs are tagged by project (via `cwd` → slug), so a concept/entity page compiled from multiple projects' sessions should carry a "Seen in: `<slug>`, `<slug>`" line — same spirit as this file's existing sourcing convention, just with project attribution added.
### Day-to-day commands
Run from `~/.claude/claude-memory-compiler/` (not from this vault):
```bash
uv run python scripts/compile.py                    # compile new/changed raw/sessions/ logs into wiki/
uv run python scripts/compile.py --dry-run           # show what would be compiled, no writes
uv run python scripts/query.py "question"            # ask the wiki a question
uv run python scripts/query.py "question" --file-back  # ask + file the answer into wiki/queries/
uv run python scripts/lint.py                        # full health check (has LLM cost)
uv run python scripts/lint.py --structural-only      # free structural-only health check
uv run python scripts/prune.py                       # archive fully-compiled logs older than 30 days
uv run python scripts/prune.py --dry-run             # preview what would be archived
```
`prune.py` only moves (never deletes) a `raw/sessions/YYYY-MM-DD.md` log into `raw/sessions/archive/`, and only once it's both older than the retention window and confirmed fully compiled (its hash matches what `compile.py` last recorded in `state.json`) — anything not yet compiled is left alone and reported. Archived files keep their filename, so existing `[[raw/sessions/<date>#anchor]]` provenance backlinks from `wiki/` pages still resolve (Obsidian links by basename, not folder).
Everything else — SessionStart context injection, SessionEnd/PreCompact capture — is automatic once the global hooks are installed in `~/.claude/settings.json` (see that file for the current hook block).
### Rules specific to this layer
- Never edit `raw/sessions/` entries by hand — treat them like any other raw source, immutable once written.
- `compile.py`'s schema input is *this file* (`CLAUDE.md`), not the compiler's own `AGENTS.md` — keep the "LLM Wiki" and "Self-evolving memory" sections here accurate, since they're what the compiler actually reads.
- If a session's project isn't ServiceNow-related, its facts still land in `raw/sessions/` (capture is global/automatic) but should generally *not* get compiled into this ServiceNow-specific `wiki/` — use judgment at compile time, or skip that day's non-SN sessions when running `compile.py --file`.
