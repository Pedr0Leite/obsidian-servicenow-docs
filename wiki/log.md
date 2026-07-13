# Wiki Log

Append-only. One entry per ingest/query/lint. Format: `## [YYYY-MM-DD] <type> | <title>`. Types: `ingest`, `query`, `lint`, `bootstrap`.

Tail with: `grep "^## \[" wiki/log.md | tail -5`

## [2026-07-13] bootstrap | LLM Wiki pattern instantiated

Adopted Karpathy's LLM Wiki pattern into this vault. Created `wiki/` as the synthesized layer (index.md, log.md, entities/, concepts/, syntheses/, queries/) and `raw/inbox/` as the landing zone for new sources. Existing folders (`ServiceNowOfficialDocs/`, `Notion/`, `Applications/`, `chats/`) kept as-is — they already serve as raw/curated sources.

First-pass integration: registered [[capacity-planner]] as an entity page, stubbed 6 core concept pages ([[acls]], [[gliderecord-patterns]], [[flow-designer]], [[scoped-apps]], [[ai-agents]], [[ai-search]]) linking back to existing Notion/now-assist-ai content, cataloged remaining 24 Notion topic folders in `wiki/index.md` without creating stub pages for them (no source material synthesized yet — created on first real query/ingest touching them). Nothing existing was deleted or rewritten.

Schema documented in `CLAUDE.md` under "LLM Wiki".

## [2026-07-13] auto-ingest | 2026-07-13.md
- Source: `raw/sessions/2026-07-13.md`
- Pages created: none
- Pages updated: none
- Note: Only session was `fake-project-alpha` (`/tmp/fake-project-alpha`) — non-ServiceNow test project, explicitly flagged `FLUSH_OK - Nothing worth saving`. Skipped per schema rule (non-SN sessions not compiled into this wiki).

## [2026-07-13] auto-ingest | 2026-07-13.md (pass 2 — session 18:13)
- Source: `raw/sessions/2026-07-13.md`
- Pages created: none
- Pages updated: [[acls]] — added `## Debugging gotchas` section: elevate to `security_admin` before ACL troubleshooting (provenance: `hook-test-1783962746` at `/tmp/hook-test-1783962746`)

## [2026-07-13] lint | smoke-test cleanup
- The two `auto-ingest` entries above came from smoke-testing the newly-installed global hooks (`fake-project-alpha`, `hook-test-1783962746` — both throwaway `/tmp` dirs, not real projects).
- Cleaned up: removed all 3 test session blocks from `raw/sessions/2026-07-13.md` (now header-only), removed the test-added `## Debugging gotchas` section from [[acls]].
- These log entries are left as-is per the append-only convention — this entry documents that their content no longer exists in the wiki, for anyone reading the log later.
