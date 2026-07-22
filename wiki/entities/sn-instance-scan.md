---
aliases: [SN Instance Scan, Instance Architecture Scanner]
area: entity
tags: [entity, scoped-app, genai, atf]
---
In-house scoped app (real prefix `x_335329_iscan_*` — the vault's spec docs still say `x_snis_iscan`, a naming mismatch that predates the actual build; don't reintroduce `x_snis_iscan` into the repo) that scans a ServiceNow instance app-by-app: walks `sys_db_object` → per-app tables, falls back to Application Files (`sys_metadata`) when ACL-denied. Built with the ServiceNow SDK/Fluent in `sn-instance-scan` (separate repo from this vault). **Deployed** to a dev instance (`dev296062.service-now.com`) as of 2026-07-22. v2 improvements (LLM copy-paste context export, Activity-stream `comments` journal field) are built; the Activity-stream **formatter** still needs a manual Form Layout add on any newly-deployed instance (that step was always spec'd as form config, not code — see `prompt-v2-improvements.md` Improvement 2, item 3). The v3 instance-assessment extension (4 sub-specs: Modes → Counting → Cross-refs → Report) is **fully implemented** — see `sn-instance-scan` repo's `CLAUDE.md` and `docs/superpowers/INSTANCE_ASSESSMENT_STATUS.md` for the authoritative current status; this vault's spec docs below are historical build prompts, not a live status tracker — check the repo, not this page, for "is X built yet." Wiki entity page — a pointer + summary, not a copy. Source of truth for *why* is `Applications/sn-instance-scan/`; source of truth for *what's actually built* is the `sn-instance-scan` repo.

Seen in: `obsidian-servicenow-docs`, `sn-instance-scan`

## Source notes
- `Applications/sn-instance-scan/prompt.md` — original v1 spec
- `Applications/sn-instance-scan/architecture.md` — full v1 design, table schema, dev instructions, 2026-07-15 implementation decisions (GlideAjax fix, activities field, verbose logging)
- `Applications/sn-instance-scan/test-plan.md` — ATF plan (superseded going forward — the repo's standing instruction as of the v3 extension is no new ATF entries; this file is v1/v2 history only)
- `Applications/sn-instance-scan/prompt-v2-improvements.md` — v2 spec: LLM copy-paste context export + Activity-stream comments field. Built (2026-07-22), except the Activity formatter form-config step.
- `Applications/sn-instance-scan/architecture-v2.md` — v2 design detail for the above. Built.
- `Applications/sn-instance-scan/prompt-v3-assessment-report.md` — v3 spec: the instance-assessment extension (modes widened to true full-instance, count everything including roles/groups/properties, cross-reference map, exportable status-flagged + narrative report). **Fully implemented** as of 2026-07-22 — decomposed into 4 sub-specs, see the `sn-instance-scan` repo's own spec/plan docs under `docs/superpowers/specs/` and `docs/superpowers/plans/` for the actual implementation record (that decomposition and its design decisions are NOT mirrored back into this vault).
- [[raw/sessions/2026-07-14#Session 12:02 — obsidian-servicenow-docs]]
- [[raw/sessions/2026-07-15#Session 16:58 — sn-instance-scan]]

## Related
- [[scoped-apps]]
- [[acls]]
- [[ai-agents]] — see [[genai-prompt-vs-ai-agent]] for the decision to use flat prompt instead
- [[wiki/index|Wiki Index]]
