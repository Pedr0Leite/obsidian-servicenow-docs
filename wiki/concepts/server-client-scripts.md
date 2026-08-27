---
aliases: [Server and Client Side Scripts]
area: concept
tags: [concept, scripting, gliderecord]
---
Server/client scripting snippets: distance calc, CMDB change-parent-table, impersonation, mandatory attachments, Scripted Extension Points, Script Include inheritance, GlideDateTime.

## Sources
- `Notion/ServiceNow/Server and Client Side Scripts/`

## Gotchas

### Never call `current.update()` inside a Business Rule

Calling `current.update()` inside a BR that fires on insert or update causes an infinite loop (the update re-triggers the same BR), produces duplicate notifications, and generates extra DB writes. Reusable logic shared across multiple BRs belongs in a Script Include — not inline in the rule body.

Seen in: `obsidian-servicenow-docs`
Source: [[raw/sessions/2026-07-16#Session 17:33 — obsidian-servicenow-docs]]

### `global.GlideAjax` does not exist client-side
In a scoped app, server-side code references global-scope classes with the `global.` prefix (e.g. `global.SomeScriptInclude`). This prefix must NOT carry over to client scripts. `GlideAjax` is always a plain global client API — use `new GlideAjax(...)`, never `new global.GlideAjax(...)`. The latter throws a `ReferenceError` silently in the browser, causing the UI action to do nothing with no visible error.

Seen in: `sn-instance-scan` (`RunScan.client.js`) — [[raw/sessions/2026-07-15#Session 16:58 — sn-instance-scan]]

### `current.update()` + `setAbortAction(true)` in a UI Action causes "Invalid update"

Calling `current.update()` mid-execution of a UI Action and then `setAbortAction(true)` afterward produces an "Invalid update" error — the explicit `update()` increments `sys_mod_count`, and the platform's subsequent natural save sees a stale count.

Fix: do not call `current.update()` inside a UI Action; let the platform do one natural save at the end.

Seen in: `sn-instance-scan`
Source: [[raw/sessions/2026-07-22#Session 14:15 — sn-instance-scan]]

## Related concepts
- [[gliderecord-patterns]]
- [[cmdb]]
- [[scoped-apps]]

## Related
- [[wiki/index|Wiki Index]]
