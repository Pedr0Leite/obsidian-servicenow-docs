---
aliases: [SN Instance Scan, Instance Architecture Scanner]
area: entity
tags: [entity, scoped-app, genai, atf]
---
In-house scoped app (real prefix `x_335329_iscan_*` — the vault's spec docs still say `x_snis_iscan`, a naming mismatch that predates the actual build; don't reintroduce `x_snis_iscan` into the repo) that scans a ServiceNow instance app-by-app: walks `sys_db_object` → per-app tables, falls back to Application Files (`sys_metadata`) when ACL-denied. Built with the ServiceNow SDK/Fluent in `sn-instance-scan` (separate repo from this vault). **Deployed** to a dev instance (`dev296062.service-now.com`) as of 2026-07-22. v2 improvements (LLM copy-paste context export, Activity-stream `comments` journal field) are built; the Activity-stream **formatter** still needs a manual Form Layout add on any newly-deployed instance (that step was always spec'd as form config, not code). The v3 instance-assessment extension (4 sub-specs: Modes → Counting → Cross-refs → Report) is **fully implemented** — see `sn-instance-scan` repo's `CLAUDE.md` and `docs/superpowers/INSTANCE_ASSESSMENT_STATUS.md` for the authoritative current status; this vault's spec docs below are historical build prompts, not a live status tracker — check the repo, not this page, for "is X built yet." Wiki entity page — a pointer + summary, not a copy. Source of truth for *why* is `Applications/sn-instance-scan/`; source of truth for *what's actually built* is the `sn-instance-scan` repo.

**"Download Report" confirmed (2026-07-22 code-trace investigation)**: this
is a real PDF export, not an HTML-only view — `IscanReportGenerator._convertToPdf()`
calls the platform's actual PDF Generation Utilities plugin
(`sn_pdfgeneratorutils.PDFGenerationAPI().convertToPDFWithHeaderFooter(...)`),
producing a `sys_attachment` on the same Run/Result record the button was
clicked from, opened via `sys_attachment.do?sys_id=...`. It's a plain form
action button (not a related link), visible only on an already-saved
Run/Result record to users with the `x_335329_iscan.scanner` role — Run
form: after "Run Scan"; Result form: first button. This settles the
`architecture.md` 2026-07-15 note below ("PDF generator built but not yet
deployed to any instance") — the code path is complete and correct as of
2026-07-22; the one still-unconfirmed variable is whether
`com.snc.apppdfgenerator` is active on the target instance (see
`sn-instance-scan/DEPLOY.md`'s flagged dependency) — a missing plugin fails
loudly (client error banner + `gs.error`), not silently. See
`sn-instance-scan/CLAUDE.md`'s "Download Report" section for the full trace.

Seen in: `obsidian-servicenow-docs`, `sn-instance-scan`

## Source notes
- `Applications/sn-instance-scan/architecture.md` — full v1 design, table schema, dev instructions, 2026-07-15 implementation decisions (GlideAjax fix, scan_findings field [renamed from `activities` 2026-07-22], verbose logging); journal-field write-loss bug fix (2026-07-22); global-scope customization gap analysis
- `Applications/sn-instance-scan/test-plan.md` — ATF plan (superseded going forward — the repo's standing instruction as of the v3 extension is no new ATF entries; this file is v1/v2 history only)
- `Applications/sn-instance-scan/architecture-v2.md` — v2 design detail: LLM copy-paste context export + Activity-stream comments field. Built (2026-07-22), except the Activity formatter form-config step.
- `Applications/sn-instance-scan/reusable-prompt-to-process-scan-results.md` — reusable prompt for processing scan output
- The v3 instance-assessment extension (modes widened to true full-instance, count everything including roles/groups/properties, cross-reference map, exportable status-flagged + narrative report) is **fully implemented** as of 2026-07-22 — see the `sn-instance-scan` repo's own spec/plan docs under `docs/superpowers/specs/` and `docs/superpowers/plans/` for the actual implementation record (build-prompt docs for this and later versions were kept in the repo, not duplicated in this vault).
- [[raw/sessions/2026-07-14#Session 12:02 — obsidian-servicenow-docs]]
- [[raw/sessions/2026-07-15#Session 16:58 — sn-instance-scan]]
- [[raw/sessions/2026-07-22#Session 14:15 — sn-instance-scan]]

## Related
- [[scoped-apps]]
- [[acls]]
- [[ai-agents]] — see [[genai-prompt-vs-ai-agent]] for the decision to use flat prompt instead
- [[wiki/index|Wiki Index]]
