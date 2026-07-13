# Backlinks Log

Append-only memory of backlink health checks and cross-link improvements to the wiki graph. Format: `## [YYYY-MM-DD] <check-type>`.

Validation method: grep all `[[wikilink]]` targets under `wiki/` and confirm a matching file exists (Obsidian desktop app / CLI wasn't running for a live `obsidian backlinks` check — grep is the cheap fallback and vault-agnostic).

## [2026-07-13] full pass | 23 new concept pages + orphan fixes

- Created concept pages for all remaining Notion topic folders: cis, ciwf, cmdb, integrations-diagrams, email, event-management, frameworks-libraries, install-stuff, itom, knowledge-base-articles, logics-and-creations, mid-server, migrations, platform-analytics, random-scripts, roles-per-module, server-client-scripts, service-catalog, service-portal, service-portfolio-management, system-properties, tips-and-tricks, workspace, cta, integrations.
- **Found 2 orphans** (folders never referenced anywhere in `wiki/index.md`): `Notion/ServiceNow/Integrations/` (7 files) and `Notion/ServiceNow/CTA/` (19 files, CTA cert track). Fixed — added [[integrations]] and [[cta]] concept pages, linked from index.
- Skipped a dedicated page for `Notion/ServiceNow/Applications/` — content already covered by [[scoped-apps]]; linking instead of duplicating.
- Added deliberate cross-links between related concept pages to strengthen the graph (not just index → page, but page → page):
  - [[install-stuff]] ↔ [[logics-and-creations]] (both cover SSO)
  - [[roles-per-module]] ↔ [[acls]], [[service-catalog]], [[service-portfolio-management]]
  - [[mid-server]] ↔ [[itom]], [[integrations]]
  - [[service-portal]] ↔ [[frameworks-libraries]], [[service-catalog]]
  - [[cis]] ↔ [[cta]] (both certification tracks)
  - [[system-properties]] ↔ [[workspace]]
- Validated all `[[wikilinks]]` under `wiki/` resolve to an existing file — 0 broken links found.
- Not checked this pass: backlinks from non-wiki vault content (Notion/, Applications/) into wiki/ pages — none expected yet since wiki/ is new; revisit once ingest workflow starts pointing raw notes back at wiki pages.
