---
aliases: [Server and Client Side Scripts]
area: concept
tags: [concept, scripting, gliderecord]
---
Server/client scripting snippets: distance calc, CMDB change-parent-table, impersonation, mandatory attachments, Scripted Extension Points, Script Include inheritance, GlideDateTime.

## Sources
- `Notion/ServiceNow/Server and Client Side Scripts/`

## Gotchas

### `global.GlideAjax` does not exist client-side
In a scoped app, server-side code references global-scope classes with the `global.` prefix (e.g. `global.SomeScriptInclude`). This prefix must NOT carry over to client scripts. `GlideAjax` is always a plain global client API — use `new GlideAjax(...)`, never `new global.GlideAjax(...)`. The latter throws a `ReferenceError` silently in the browser, causing the UI action to do nothing with no visible error.

Seen in: `sn-instance-scan` (`RunScan.client.js`) — [[raw/sessions/2026-07-15#Session 16:58 — sn-instance-scan]]

## Related concepts
- [[gliderecord-patterns]]
- [[cmdb]]
- [[scoped-apps]]

## Related
- [[wiki/index|Wiki Index]]
