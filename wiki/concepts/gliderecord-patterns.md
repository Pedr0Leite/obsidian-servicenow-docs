---
aliases: [GlideRecord, GlideRecord Patterns]
area: concept
tags: [concept, scripting, gliderecord]
---
Server-side GlideRecord/GlideSystem idioms — query patterns, cross-table loops, dedup, restore, bulk ops.

## Sources
- `Notion/ServiceNow/Scripts/` — ~21 scripts, incl. `Loop a list of users over another table`, `loop info from one table in another table`, `Remove duplicates_various ways`, `restore archive records`, `searchBySysId`, `searchForUserInAllRecord`.
- `Notion/ServiceNow/Server and Client Side Scripts/`
- `Notion/ServiceNow/Random Scripts/`
- `ServiceNowOfficialDocs/api-reference/` — official GlideRecord/GlideSystem API docs.

## Gotchas

### Journal fields silently drop repeated writes on the same GlideRecord instance

Journal fields (Glide type `journal` / `glide_list`) silently discard appends when the same `GlideRecord` instance is reused across multiple writes. The platform commits only the last append on that handle; earlier ones are lost with no error.

Fix: re-query a fresh `GlideRecord` per journal write.

Seen in: `sn-instance-scan` (`IscanScanOrchestrator._appendActivity()` — `comments` journal field drops after first append when the same run record is reused across loop iterations)
Source: [[raw/sessions/2026-07-22#Session 14:15 — sn-instance-scan]]

## Related concepts
- [[scoped-apps]]
- [[server-client-scripts]]

## Related
- [[wiki/index|Wiki Index]]
