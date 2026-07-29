---
aliases: [sn-instance-scan v2 Improvements, Instance Scanner Copy-Paste Context + Comments Field]
area: application-spec
tags: [scoped-app, application-development, cmdb, acls, ai-agents, spec, journal-fields]
---

Build prompt for two v2 improvements to [[sn-instance-scan]] (see [[sn-instance-scan/prompt|original build prompt]] and [[sn-instance-scan/architecture|architecture]] for the v1 baseline this extends).

**STATUS (2026-07-22): Built and deployed**, except Improvement 2 item 3 (the Activity formatter form-config step — that one's manual, per-instance, not code, so it needs redoing on any newly-deployed instance). This is a historical build prompt, not a live status tracker — the `sn-instance-scan` repo is authoritative for current build state.

## Build prompt

```
Extend the existing ServiceNow scoped application "sn-instance-scan"
(scope x_snis_iscan) with two v2 improvements. Both are additive — do not
change v1 table names, existing field names, or the scan algorithm.

IMPROVEMENT 1 — Copy-pasteable LLM context export

GOAL
Today IscanSummaryGenerator.buildPrompt() assembles gathered facts into a
prompt string, but it is only ever used internally for the in-instance
GenAI call (IscanSummaryGenerator.generate()) and is not persisted or
exposed. Users need a self-contained block of text they can copy out of
the record and paste into any external LLM (ChatGPT, Claude, etc.) to get
a well-documented architecture write-up — without needing Now Assist /
Generative AI Controller active on the instance at all.

CHANGES
1. Add a new field x_snis_iscan_result.llm_context (String, full text/HTML
   or Journal — plain full-text field, not Journal, matching the
   'queryable, no journal ACL complications' rationale already used for
   x_snis_iscan_run.activities) that stores the FULL assembled context
   block, not just the summary. This is a superset of what
   IscanSummaryGenerator.buildPrompt() currently builds for the internal
   GenAI call.
2. Refactor IscanSummaryGenerator.buildPrompt(facts) so it returns a
   structured, LLM-ready document, not a terse prompt line. Required
   sections, in order:
   - App identity: name, scope, vendor/source, scan date, scan mode used
     (full_access vs app_files_fallback — call this out explicitly so the
     receiving LLM knows whether table/field data is present or only
     metadata).
   - Data model: full table list with extends_table and well_known_base
     classification, per-table field list (name + type), and the
     reference_field_list relationship graph (table -> target table).
     Omit entirely (not just zero-filled) when scan_mode_used =
     app_files_fallback, and say so in one line instead.
   - Automation surface: counts and NAMES (not just counts — v1 only
     stored counts) of business rules, script includes, flows, ACLs, UI
     actions. This requires IscanAppFilesScanner.scanApp() and
     IscanTableScanner to also return the underlying name lists, not just
     the aggregate counts currently written to x_snis_iscan_result.
   - Integration points: REST messages / web services referencing the
     scope (name + endpoint if available), matching table_count sibling
     integration_count already tracked.
   - Explicit instruction footer: a fixed closing paragraph asking the
     receiving LLM to produce a well-documented architecture summary from
     the above (purpose, data model shape, integration points, automation
     surface) — this is what makes the block copy-paste-and-go rather
     than requiring the user to also supply their own instructions.
3. IscanSummaryGenerator.generate(facts) keeps calling the in-instance
   GenAI Controller as today (v1 behavior unchanged, still optional /
   degrades gracefully if unavailable) but now builds its prompt FROM the
   same llm_context block via buildPrompt(), so the two paths (in-instance
   summary vs external copy-paste) never drift out of sync — one fact
   assembly, two consumers.
4. Form UI: add a UI Action or form button 'Copy LLM Context' on
   x_snis_iscan_result that copies llm_context to clipboard (client
   script, standard clipboard API) — mirrors the existing summary_text
   display pattern, no new tables needed.
5. IscanTableScanner and IscanAppFilesScanner: extend their return shapes
   to include name lists (business_rule_names[], script_include_names[],
   flow_names[], acl_names[], ui_action_names[]) alongside the existing
   counts, since buildPrompt() now needs names, not just counts. Existing
   *_count fields on x_snis_iscan_result are unchanged and still
   populated from the same data.

CONSTRAINT
llm_context must be complete and self-contained without requiring the
reader to open any other ServiceNow record — that is the whole point of
'copy and paste that info and an LLM can return a well-documented
architecture summary.'

IMPROVEMENT 2 — Comments field on x_snis_iscan_run for the Activity stream

GOAL
x_snis_iscan_run already has an 'activities' field (String, 8000 chars,
per [[sn-instance-scan/architecture|architecture]] deliberately NOT a
Journal field to stay queryable and avoid journal ACL complications). That
decision is still correct for the *queryable* log, but it means
x_snis_iscan_run gets no entry in ServiceNow's native Activity
formatter/stream on the form — journal-type fields (Comments/Work notes)
are what the OOB Activity formatter renders, and this run record has none.

CHANGES
1. Add x_snis_iscan_run.comments (Journal field, standard 'Comments'
   field, same type ServiceNow uses OOB on task-derived tables) so the
   form's Activity formatter has a journal field to render.
2. _appendActivity(run, message) in IscanScanOrchestrator (see
   Implementation Decisions, 2026-07-15) currently only prepends to the
   String 'activities' field and calls run.update(). Extend it to ALSO
   append the same message to the new Journal 'comments' field via
   run.comments.setJournalEntry(message) — or the standard journal-append
   pattern (gr.comments = message; before update()) — so every progressive
   milestone still lands in 'activities' (queryable, unchanged) AND now
   also shows up live in the Activity stream via 'comments' (journal,
   user-facing).
3. Add the Activity formatter to the x_snis_iscan_run form view (Form
   Layout > add related list/formatter 'Activity' — standard ServiceNow
   form config, not code) so 'comments' journal entries are visible where
   users expect them.
4. Do not remove or repurpose the existing 'activities' String field —
   it stays the queryable/exportable log (also feeds into llm_context's
   scan-mode narrative for Improvement 1 if useful); 'comments' is
   additive, purely for native Activity stream visibility.

CONSTRAINT
Do not swap 'activities' to Journal type — the v1 architecture note
explicitly chose String for queryability and to avoid journal field ACL
complications; that reasoning still holds. 'comments' is a second,
new field, not a replacement.

NON-GOALS (both improvements)
- No new tables.
- No change to scan algorithm, ACL fallback logic, or scan modes.
- No external LLM API call added to the app itself — llm_context is
  exported for the USER to paste elsewhere, the app does not call out to
  a third-party LLM API (in-instance GenAI Controller call in
  IscanSummaryGenerator.generate() is unchanged, still internal/optional).
```

## Design notes (why it's shaped this way)

- **One fact assembly, two consumers** — llm_context and the in-instance GenAI summary must be built from the same buildPrompt() output so they can't silently drift (e.g. summary_text saying something llm_context doesn't support). Cheaper than maintaining two prompt-assembly code paths.
- **Names, not just counts, is the actual v1 gap.** [[sn-instance-scan/architecture|v1 architecture]] stores business_rule_count etc. as integers only — sufficient for the in-instance one-paragraph summary, but useless for an external LLM asked to reason about architecture (a count with no names is not enough context to copy-paste). This is the core reason Improvement 1 needs a scanner return-shape change, not just a new field.
- **comments stays additive, not a replacement for activities** — see [[gliderecord-patterns]]/[[acls]] precedent already noted in the architecture doc: Journal fields carry their own ACL semantics distinct from a plain String, which is exactly why v1 avoided Journal for the queryable log. The fix for 'no Activity stream entry' is to add a second, purpose-built Journal field, not to change the type of the existing one.

## Related
- [[sn-instance-scan]]
- [[sn-instance-scan/prompt|sn-instance-scan v1 Build Prompt]]
- [[sn-instance-scan/architecture|sn-instance-scan Architecture]]
- [[sn-instance-scan/architecture-v2|sn-instance-scan Architecture v2 (this spec's design)]]
- [[sn-instance-scan/test-plan|sn-instance-scan Test Plan]]
- [[scoped-apps]]
- [[acls]]
- [[gliderecord-patterns]]
- [[wiki/index|Wiki Index]]
