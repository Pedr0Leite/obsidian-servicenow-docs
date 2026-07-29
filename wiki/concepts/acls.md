---
aliases: [ACLs, Access Control]
area: concept
tags: [concept, security, acl]
---
Access control rules — table/field-level ACLs, scoped-app ACL patterns, encryption-adjacent security notes.

## Sources
- `Notion/ServiceNow/Security & ACL/` — Report View ACLs, GlideEncrypter alternatives/replacement.
- `ServiceNowOfficialDocs/platform-security/`, `ServiceNowOfficialDocs/security-management/` — official reference.
- [[capacity-planner]] — real ACL implementation in a scoped app.

## Gotchas

### GlideAjax + zero server logs — two-stage diagnostic

If a GlideAjax call produces **zero** server-side logs — including the very first `gs.info` at the top of the target method — the Script Include body never ran. Two distinct causes produce this symptom; separate them by checking the calling user first:

**Stage 1 — non-admin user: execute ACL denial**
The execute ACL silently blocked the call before the script ran. Diagnostic steps:
1. Confirm the Script Include has an execute ACL (`sys_security_acl`, type=`execute`).
2. Verify the ACL is active and its role/condition resolves to `true` for the current user.
3. In a scoped app the execute ACL role must be namespaced (e.g. `x_snis_iscan.scanner`).

**Stage 2 — admin user: client-side problem (request never sent)**
`admin` bypasses ACL evaluation entirely in ServiceNow — if the calling user is `admin` and server logs are still empty, the ACL is NOT the blocker. The HTTP request likely never left the browser. Diagnostic steps:
1. Open browser DevTools **Console** tab — look for a JS error before or during the click handler (e.g. `runScanAsync is not defined`, `TypeError`).
2. Open **Network** tab, filter for `xmlhttp.do` — confirm whether a POST with `sysparm_processor=<ScriptInclude>` and `sysparm_name=<method>` is actually sent, and inspect the response body if it is.

Seen in: `sn-instance-scan` (`IscanScanOrchestrator` / `runScanAjax` — 2026-07-20)
Sources: [[raw/sessions/2026-07-20#Session 21:28 — sn-instance-scan]], [[raw/sessions/2026-07-20#Session 21:33 — sn-instance-scan]]

## Related concepts
- [[scoped-apps]]
- [[server-client-scripts]]

## Related
- [[wiki/index|Wiki Index]]
