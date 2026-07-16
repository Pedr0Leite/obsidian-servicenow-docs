---
aliases: [SN Instance Scan, Instance Architecture Scanner]
area: entity
tags: [entity, scoped-app, genai, atf]
---
In-house scoped app (`x_snis_iscan_*`) that scans a ServiceNow instance: walks `sys_db_object` → per-app tables, falls back to Application Files (`sys_metadata`) when ACL-denied. Designed 2026-07-14; built 2026-07-15; not yet deployed to any instance. Wiki entity page — a pointer + summary, not a copy. Source of truth is `Applications/sn-instance-scan/`.

Seen in: `obsidian-servicenow-docs`, `sn-instance-scan`

## Source notes
- `Applications/sn-instance-scan/prompt.md` — original spec
- `Applications/sn-instance-scan/architecture.md` — full design, table schema, dev instructions, 2026-07-15 implementation decisions (GlideAjax fix, activities field, verbose logging)
- `Applications/sn-instance-scan/test-plan.md` — ATF plan
- [[raw/sessions/2026-07-14#Session 12:02 — obsidian-servicenow-docs]]
- [[raw/sessions/2026-07-15#Session 16:58 — sn-instance-scan]]

## Related
- [[scoped-apps]]
- [[acls]]
- [[ai-agents]] — see [[genai-prompt-vs-ai-agent]] for the decision to use flat prompt instead
- [[wiki/index|Wiki Index]]
