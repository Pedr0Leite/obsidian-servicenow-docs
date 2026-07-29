---
aliases: [sn-instance-scan, Instance Scanner App]
area: application-spec
tags: [scoped-app, application-development, cmdb, acls, ai-agents, spec]
---

Build prompt for a custom ServiceNow scoped app that scans an instance
application-by-application and returns an architecture summary per app.
Not yet built — this is the spec to hand to a dev agent / architect.

## Build prompt

```
Build a ServiceNow scoped application called "sn-instance-scan"
(suggested scope: x_<vendor>_iscan).

GOAL
Given a ServiceNow instance, produce a per-application architecture summary:
tables owned, key relationships, business rules/script includes/flows present,
and a brief plain-English description of what the application does.

SCOPE SELECTION (user picks one at run time)
1. Full scan — every application in sys_app.
2. Custom-only scan — applications whose scope starts with `x_` (exclude OOB/store apps).
3. Manual scan — user picks specific sys_app records from a list.

ALGORITHM
For each application in scope:
1. Resolve the app's scope prefix from sys_app (source/scope field).
2. Query sys_db_object where the table's `sys_scope` (or `name` prefix)
   matches the app, to enumerate tables owned by that application.
   - GlideRecord on sys_db_object, not a hardcoded table list — apps vary.
   - Flag tables that extend `task`, `cmdb_ci`, or other well-known bases;
     that alone tells you a lot about the app's purpose (ITSM extension,
     CMDB extension, standalone data model, etc.).
3. For each owned table, attempt a lightweight profile, not a full data dump:
   - Row count (GlideAggregate COUNT, not GlideRecord.getRowCount() — cheaper).
   - Field list + type from sys_dictionary (skip OOB fields already on the
     parent table; only report fields added by this app).
   - Reference fields → gives you the relationship graph between this app's
     tables and everything else.
4. If the running user lacks read access to sys_db_object/sys_dictionary
   rows for that scope (ACL denial, no security_admin/app read role), FALL
   BACK to sys_app → related list "Application Files" (sys_metadata /
   sys_app_module_source, exposed via GlideRecord on sys_metadata filtered
   by sys_scope). This still yields: script includes, business rules, ACLs,
   UI actions, flows — enough to infer architecture even with zero data
   access. Always check GlideRecord.canRead() before attempting the primary
   path so the fallback triggers deterministically, not via a caught error.
5. Synthesize a short architecture write-up per app from what was gathered:
   purpose (inferred from table names + extends + business rule labels),
   data model shape (# custom tables, key relationships), integration
   points (REST/SOAP/outbound messages if any sys_web_service or
   sys_rest_message records reference the scope), and automation surface
   (# business rules / flows / script includes).

OUTPUT
- One record per scanned application (custom table, e.g. x_<scope>_iscan_result)
  storing: app reference, scan date, scan mode used (full-access vs
  Application-Files-fallback), table list, and the generated summary text.
- A form/list view to browse results per app.
- Optionally, hand the gathered facts (table list, field list, business
  rule/flow names) to a Now Assist AI Agent or a single GenAI prompt to
  generate the "brief architecture explanation" text — this is a
  summarization task, not a reasoning/ReAct task, so a single skill/prompt
  call is enough; don't build a multi-step AI Agent for it.

CONSTRAINTS
- Scoped app, ACL-aware: never assume security_admin. Every GlideRecord
  query must run under the user's actual access and check canRead()/isValidRecord()
  before use.
- Use gs.getProperty() for the x_ prefix filter and any configurable
  thresholds (e.g. row-count sample size) — don't hardcode.
- No destructive operations; this app only reads.
- ATF test coverage: happy path (full access, custom app, tables found),
  and negative case (ACL-denied app, falls back to Application Files path
  cleanly with no error thrown).

NON-GOALS
- Not a data quality or CMDB health scanner.
- Not a full source-code static analyzer — reads metadata records, doesn't
  parse script bodies.
- No auto-remediation or cross-instance comparison in v1.
```

## Design notes (why it's shaped this way)

- **sys_db_object → sys_app, not the reverse.** Tables carry `sys_scope`
  directly, so filtering sys_db_object by scope is one query per app,
  no join gymnastics.
- **GlideAggregate over GlideRecord.getRowCount()** — see [[gliderecord-patterns]],
  standard perf idiom in this vault for count-only queries.
- **Application Files fallback exists because table-level ACLs and
  metadata-level ACLs are governed separately** — a role can read sys_app
  and its related Application Files list (sys_metadata) without having
  read access to sys_dictionary/sys_db_object for a locked-down scope.
  This is the same asymmetry documented in [[acls]].
- **x_ prefix detection belongs in scoped-app namespacing, not a special
  case** — see [[scoped-apps]]. Store-installed apps also get scoped
  prefixes, so "custom-only" should filter on `sys_app.vendor` /
  `sys_app.source` = internal/private, not purely the `x_` string match,
  or store apps will leak into the "custom" bucket.
- **Summary generation is a single-shot GenAI prompt, not an AI Agent.**
  [[ai-agents]] covers the ReAct loop for multi-step tool use; this task
  is "here are facts, write a paragraph" — no iteration needed, so it's
  a Generative AI Controller call, not sn_aia_* infrastructure. Skipped
  building a full Agent for it — add one only if you later want the
  scanner to ask follow-up questions or branch its own investigation.

## Related
- [[sn-instance-scan/architecture|sn-instance-scan Architecture]]
- [[sn-instance-scan/test-plan|sn-instance-scan Test Plan]]
- [[scoped-apps]]
- [[acls]]
- [[gliderecord-patterns]]
- [[ai-agents]]
- [[wiki/index|Wiki Index]]
