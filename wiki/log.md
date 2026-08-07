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

## [2026-07-14] auto-ingest | 2026-07-14.md
- Source: `raw/sessions/2026-07-14.md`
- Pages created: [[sn-instance-scan]], [[genai-prompt-vs-ai-agent]]
- Pages updated: [[scoped-apps]] — added `now-sdk` nvm/zsh gotcha (Node version mismatch causes `Unexpected token '?'` in subcommands using modern JS)
- Sessions skipped: `pedro` (12:11) — Docker permission issue, non-SN. `pedro` (12:25) — now-sdk Node fix partially SN-related; dev tooling gotcha extracted into [[scoped-apps]].

## [2026-07-13] lint | smoke-test cleanup
- The two `auto-ingest` entries above came from smoke-testing the newly-installed global hooks (`fake-project-alpha`, `hook-test-1783962746` — both throwaway `/tmp` dirs, not real projects).
- Cleaned up: removed all 3 test session blocks from `raw/sessions/2026-07-13.md` (now header-only), removed the test-added `## Debugging gotchas` section from [[acls]].
- These log entries are left as-is per the append-only convention — this entry documents that their content no longer exists in the wiki, for anyone reading the log later.

## [2026-07-14] query | Catalog item prefill + modal in Service Portal
- Created [[catalog-item-prefill-and-modal]] — URL-based variable prefill (`sysparm_variable_values`, confirmed) vs. opening a catalog item in a modal via `spModal.open` with prefilled data (synthesized, not vault-confirmed which prefill path the base widget honors from `widgetInput`).
- Pages updated: [[service-catalog]], [[service-portal]] — added `## Related queries` backlink.

## [2026-07-14] lint | routing rule added, sn-instance-scan corrected
- Schema updated in `CLAUDE.md`: app-specific compiled facts now route to `Applications/<app>/` (thin pointer only in `wiki/entities/<app>.md`), matching the existing [[capacity-planner]] pattern. Applies to both manual ingest and `compile.py` auto-ingest.
- Corrected [[sn-instance-scan]]: moved "Open design questions" out of the wiki entity page into `Applications/sn-instance-scan/architecture.md`, slimmed the wiki page to a pointer.

## [2026-07-14] auto-ingest | 2026-07-14.md (pass 2 — session 14:22)
- Source: `raw/sessions/2026-07-14.md`
- Pages created: none
- Pages updated: none
- Note: SN-relevant content (sessions 12:02, 12:25) already compiled in pass 1 above. Remaining sessions (14:20, 14:21, 14:22) are `claude-memory-compiler` meta sessions covering compiler operational decisions (empty-log handling, duplicate log detection, routing rules) — not ServiceNow knowledge, not compiled into this wiki.

## [2026-07-15] auto-ingest | 2026-07-14.md (pass 3)
- Source: `raw/sessions/2026-07-14.md`
- Pages created: none
- Pages updated: none
- Note: All SN-relevant content already compiled in passes 1 and 2 (see entries above). Sessions 12:02 and 12:25 were fully extracted; compiler meta sessions (14:20–14:29) are operational noise, not SN knowledge. No new pages warranted.

## [2026-07-15] ingest | Capacity Planner — Epic 10 (Overview period-reactivity, By Project tab)
- Source: user request 2026-07-15 (3 issues: Total Projects/Planned/Unplanned not period-reactive, no click-to-filter on Total Projects, replace "All plan allocations" tab with "By Project").
- Pages updated: [[capacity-planner-backlog-2026-07]] — added Epic 10 (CAPMGMT-10/11/12), Wave 5 sequencing rows, OQ-18.
- No wiki/entities or wiki/concepts changes — app-specific detail routed to `Applications/capacity-planner/` per the routing rule.

## [2026-07-15] auto-ingest | 2026-07-15.md
- Source: `raw/sessions/2026-07-15.md`
- Pages created: none
- Pages updated:
  - [[catalog-item-prefill-and-modal]] — appended iframe pattern (standalone `$sce.trustAsResourceUrl` + `ng-src`) and button-triggered Bootstrap modal variant (jQuery `.modal('show')` + `$timeout`); session 14:21 action item.
  - [[server-client-scripts]] — added `## Gotchas` section: `global.GlideAjax` does not exist client-side (scoped app misuse fails silently); session 16:58.
  - [[sn-instance-scan]] (entity pointer) — updated status to "built, not yet deployed"; added session 16:58 source reference.
- App-specific detail (activities field, `_appendActivity` helper, verbose logging, deploy status) already compiled into `Applications/sn-instance-scan/architecture.md` by an earlier run this session. Sessions: `sn-instance-scan` (16:58).
- Session skipped: `obsidian-servicenow-docs` (09:47) — explicit `FLUSH_OK`.

## [2026-07-15] lint | full lint pass (structural + LLM)
- 61 issues: 0 errors, 12 warnings, 49 suggestions. Full report: `~/.claude/claude-memory-compiler/reports/lint-2026-07-15.md`.
- Warnings worth acting on (not fixed here, proposing):
  - INDEX stale: `sn-instance-scan` listed as "In design as of 2026-07-14" but its entity page says "built 2026-07-15; not yet deployed" — index needs a one-line update.
  - Contradiction in [[catalog-item-prefill-and-modal]]: troubleshooting section validates `sysparm_id` as correct, but the working fix (attempt 2) uses `sys_id` inside `embeddedWidgetOptions` instead — guidance and working solution disagree, needs reconciling.
  - 10 orphan concept pages (ciwf, cta, email, flow-designer, integrations-diagrams, migrations, platform-analytics, random-scripts, server-client-scripts, tips-and-tricks) — no inbound links yet.
- Suggestions: 16 missing-backlink auto-fixes, 33 sparse-article flags (mostly the older Notion-derived concept pages under ~15-70 words) — not actioned, left for a future lint-fix pass.



## [2026-07-20] auto-ingest | 2026-07-15.md (pass 2 — session 22:25)
- Source: `raw/sessions/2026-07-15.md`
- Pages created: none
- Pages updated:
  - [[catalog-item-prefill-and-modal]] — appended same-origin CSS injection pattern (hide portal header in iframe via `contentDocument` style injection) and `$interval` URL-poll pattern for auto-closing Bootstrap modal on catalog item submit (`widget-sc-cat-item-v2` uses Angular `$location`, `onload` never refires).
  - [[service-portal]] — added gotcha: `widget-sc-cat-item-v2` submits via `$location` client-side routing (not full page load); `contentWindow.location` throws transiently during navigation; cancel `$interval` on close and `$scope.$destroy`.
- Session skipped (already compiled in pass 1 at 19:04): `obsidian-servicenow-docs` (09:47, FLUSH_OK), `obsidian-servicenow-docs` (14:21), `sn-instance-scan` (16:58), `claude-memory-compiler` (19:04).

## [2026-07-20] auto-ingest | 2026-07-16.md
- Source: `raw/sessions/2026-07-16.md`
- Pages created: none
- Pages updated: [[server-client-scripts]] — added Business Rule gotcha: never call `current.update()` inside a BR (causes loop + duplicate notifications + extra DB writes; reusable logic → Script Includes)
- Sessions skipped: `linuxsnippingtool` (17:32, clippick Linux app — non-SN), `documents` (17:33, GNOME extension fix — non-SN), all FLUSH_ERROR/FLUSH_OK flushes (no content)
- capacity-planner Epic 10 backlog (CAPMGMT-10/11/12) already reflected in `Applications/capacity-planner/capacity-planner-backlog-2026-07.md`; period-scoping fix direction already documented in the backlog ACs and architecture note — no net-new content to compile

## [2026-07-20] ingest | sn-instance-scan v2 improvements build prompt
- Source: user request (chat), not a raw source drop.
- Pages created: [[Applications/sn-instance-scan/prompt-v2-improvements]] — build prompt for two additive v2 changes: (1) `x_snis_iscan_result.llm_context` field + refactored `IscanSummaryGenerator.buildPrompt()` to emit a self-contained, copy-paste-ready architecture context block for external LLMs (names not just counts for business rules/script includes/flows/ACLs/UI actions); (2) new `x_snis_iscan_run.comments` Journal field + Activity formatter on the run form, additive alongside the existing String `activities` field (not a replacement — journal ACL complications were the original reason `activities` is String).
- Pages updated: [[sn-instance-scan]] (entity pointer) — added source-note link to the v2 prompt, one-line status update in the summary.
- Not yet built — spec only, per existing v1 prompt.md convention (Applications/<app>/ holds the spec; wiki entity stays a thin pointer).

## [2026-07-20] auto-ingest | 2026-07-20.md
- Source: `raw/sessions/2026-07-20.md`
- Pages created: none
- Pages updated:
  - [[acls]] — added `## Gotchas` section: GlideAjax zero server logs = execute ACL denial fingerprint (Script Include body never ran); diagnostic steps; scoped execute ACL role does not auto-grant to `admin`.
  - `Applications/sn-instance-scan/architecture.md` — added `## Debugging Notes (2026-07-20)`: `IscanScanOrchestrator` execute ACL blocking GlideAjax for admin user; unresolved, action item to verify ACL record.
- Sessions skipped: all FLUSH_ERROR/FLUSH_OK flushes (14:14, 14:18, 14:46, 16:59, 21:25) — no content.

## [2026-07-20] auto-ingest | 2026-07-20.md (pass 2 — session 21:33)
- Source: `raw/sessions/2026-07-20.md`
- Pages created: none
- Pages updated:
  - [[acls]] — extended GlideAjax zero-logs gotcha into a two-stage diagnostic: stage 1 (non-admin) = execute ACL denial; stage 2 (admin) = client-side problem, request never sent. Admin bypasses ACL evaluation entirely — zero logs + admin user = look at browser DevTools (Console + Network / `xmlhttp.do`).
  - `Applications/sn-instance-scan/architecture.md` — updated debugging notes: admin confirmed → ACL hypothesis eliminated → new direction client-side; next action is DevTools check (Console for JS errors, Network for `xmlhttp.do` POST).
- Sessions skipped: all FLUSH_ERROR/FLUSH_OK flushes (already noted in pass 1); session 21:28 already compiled in pass 1.

## [2026-07-22] auto-ingest | 2026-07-21.md
- Source: `raw/sessions/2026-07-21.md`
- Pages created: none
- Pages updated: none
- Note: Both sessions (`pedro` at 17:11 and 23:29, path `/home/pedro`) flagged `FLUSH_OK - Nothing worth saving`. No ServiceNow knowledge to compile.

## [2026-07-22] auto-ingest | 2026-07-22.md
- Source: `raw/sessions/2026-07-22.md`
- Pages created: none
- Pages updated:
  - [[gliderecord-patterns]] — added `## Gotchas` section: journal fields silently drop repeated writes on same GlideRecord instance; must re-query fresh record per write. Source: `sn-instance-scan` (14:15).
  - [[server-client-scripts]] — added gotcha: `current.update()` + `setAbortAction(true)` in a UI Action causes "Invalid update" (sys_mod_count collision); let platform do one natural save. Source: `sn-instance-scan` (14:15).
  - `Applications/sn-instance-scan/architecture.md` — added: `activities` → `scan_findings` rename (2026-07-22); journal field bug fix (fresh GlideRecord per write); global-scope customization gap analysis (OOB tables miss `u_`/`x_*_` custom fields and customer-scoped BRs/ACLs targeting OOB tables).
  - [[sn-instance-scan]] (entity pointer) — updated architecture.md description to reflect rename and journal fix; added session 14:15 source reference.
- Sessions skipped:
  - `pedro` (11:00, 14:15, 14:36) — Obsidian crash debugging and CYD ESP32 device, non-SN.
  - `cyd-claudeusage` (14:20) — ESP32 firmware debugging, non-SN.
  - `sn-instance-scan` (09:09) — FLUSH_OK.
  - `obsidian-servicenow-docs` (14:28, 14:29, 14:33, 14:57, 17:09) — Obsidian Bases dashboards (vault tooling, not SN knowledge) and `smart-connections-mcp` setup (infrastructure); Business Rules question deferred per existing decision (no new page without Flow Designer decision synthesis pairing).
## [2026-07-22] ingest | Partner Case Summary Agent story
- Source: user request (chat), not a raw source drop.
- Pages created:
  - [[partner-case-summary-agent|Partner Case Summary Agent (Story)]] (`Applications/partner-case-summary-agent/partner-case-summary-agent.md`) — refined user story for a proposed Now Assist AI Agent (ReAct) that summarizes `sn_customerservice_case` cases for 5 named Partner Managers. Refined via the `ba-agent` from an original Microsoft Copilot Studio connector request into a ServiceNow-native design (Virtual Agent/Now Assist Panel surface, no external connector). Case table locked to `sn_customerservice_case`.
  - [[partner-case-summary-agent]] (wiki entity, thin pointer) — links back to the Applications/ source note.
- Pages updated: `wiki/index.md` — added entity row.
- Status: proposed only, not yet built.
