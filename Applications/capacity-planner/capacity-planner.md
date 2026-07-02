---
title: Capacity Management Overview (x_u4bsh_capmgmt)
tags: [servicenow, fluent-sdk, capacity-planning, internal-tool]
date: 2026-07-02
---

# Capacity Management Overview

## 1. Overview

**Capacity Management Overview** is a custom ServiceNow application, scoped as `x_u4bsh_capmgmt` (scope ID `0aaadae787e50b10d939a7573cbb353c`), built with the **Now SDK (Fluent)**, SDK version `@servicenow/sdk` 4.8.0. It lets planners and engineering leads plan projects, BAU work, and enhancements against team capacity (FTE — full-time equivalents) across the year.

It's aimed at people who need to answer "which teams are over- or under-allocated in a given month, and which projects are driving that" — engineering managers, resource planners, and leadership doing quarterly/annual planning.

The app ships a custom single-page frontend (a vanilla-JS SPA, not Angular/React) served at `x_u4bsh_capmgmt_planner.do`, plus standard ServiceNow list views for administrative table access (teams, headcount, periods).

## 2. Purpose / Problem It Solves

Before this app, capacity planning lived in a manual spreadsheet nicknamed **"Soft & Hard Planning"** — a wide grid of projects vs. months vs. teams, updated and reconciled by hand. That approach had the usual spreadsheet problems: no audit trail per edit, no enforced relationship between "how much FTE is available" and "how much FTE is committed," and no easy way to link a planning row back to the real project/initiative record living in the intake system.

This app replaces that spreadsheet with:
- A normalized data model (one row per allocation "cell" rather than one wide row per project) — cleaner auditing and roll-ups.
- A live link to the actual initiative-intake system, so status/priority/sizing fields can flow in automatically instead of being retyped.
- A single interactive UI (heatmap, per-team drill-down, pipeline/kanban view) built directly on top of that data model.
- Role-gated editing (viewer / planner / admin) instead of an open spreadsheet anyone can edit.

## 3. Data Model

Five custom tables, all prefixed `x_u4bsh_capmgmt_`.

### x_u4bsh_capmgmt_initiative ("Capacity Plan Item")

A project, BAU item, enhancement, or absence entry being planned.

| Field | Type | Notes |
|---|---|---|
| `u_name` | string | Plan item name. Mandatory. |
| `u_initiative` | reference → `x_u4bsh_initiati_0_initiative` (external scope) | "Linked Initiative" — optional link to the real intake-system record. |
| `u_area` | choice | "Business Area Function": CCO / Sales / Finance / Legal / People Experience / Marketing / cross function / Global IT / EA-IT / Cloud Ops. |
| `u_priority` | choice | "Business Priority": P0 BAU / P1 / P2 / P3 / P4. |
| `u_tshirt_size` | choice | "High-Level Sizing": S / M / L / XL. |
| `u_type` | choice | "Type of work": Project / BAU / Enhancement / Absences. |
| `u_start`, `u_end` | string (`YYYY-MM`) | **Derived only** — computed by a Business Rule from linked allocations/periods. Not manually editable, not even by admin. |
| `u_snow_ref`, `u_ado_ref` | string | External references (ServiceNow ticket, Azure DevOps ref). |
| `u_snow_status` | choice | Approved / Screening / Qualified / Pending / New / Completed / Canceled. |
| `u_ado_status` | choice | In Progress / Done / New / On Hold. |
| `u_initiative_group` | string | "Plan item group" — free-text grouping label. |
| `u_comments` | multi-line text | Free-text notes. |
| `u_review_ready` | boolean | Lightweight "ready for review" flag — not a workflow/state machine. |
| `u_review_comment` | string (500) | Free-text review note. |
| `u_plan_status` | choice | Candidate / Committed / Removed. Default: Committed. |

Index: non-unique on `u_initiative`.

> [!note] Historical field removed
> `u_steerco_status` was fully removed from the schema, server code, and client code. It's mentioned here only so it doesn't get re-added out of habit.

### x_u4bsh_capmgmt_team ("Capacity Team")

An engineering or business team that capacity is planned against.

| Field | Type | Notes |
|---|---|---|
| `u_name` | string, unique | Mandatory. |
| `u_order` | integer | Display sequence in the UI. |
| `u_active` | boolean | Default `true`. |
| `u_is_role_team` | boolean | Default `false`. Marks "role" teams (e.g. BA, Architecture, PM) used for missing-role warnings in the UI. |
| `u_business_app` | reference → `cmdb_ci_business_app` (global scope, cross-scope read) | Resolves a business application name for the team. |

Unique index on `u_name`.

### x_u4bsh_capmgmt_period ("Capacity Period")

One row per calendar month (e.g. "Jan 2025"). Added later as **Phase 1 of an incomplete multi-year migration** intended to eventually replace the bare-month fields below with year-aware references — see [[#10. Known Issues / Architectural Debt]].

| Field | Type | Notes |
|---|---|---|
| `u_label` | string, max 10 | Mandatory, e.g. `"Jan 2025"`. |
| `u_start_date`, `u_end_date` | date | Mandatory. |

### x_u4bsh_capmgmt_allocation ("Capacity Allocation")

The core editable fact table: FTE assigned to **one initiative**, for **one team**, for **one month**. Deliberately tall/normalized (one row per grid cell edit) rather than a wide 12-column table, for cleaner auditing and roll-ups.

| Field | Type | Notes |
|---|---|---|
| `u_initiative` | reference → initiative | Mandatory. `cascadeRule: delete` — deleting the initiative deletes its allocations. |
| `u_team` | reference → team | Mandatory. |
| `u_month` | choice (Jan–Dec) | Mandatory. Legacy, year-unaware. |
| `u_period` | reference → period | Optional. Newer, year-aware field — partially wired in. |
| `u_fte` | decimal (scale 2) | The allocated FTE amount. |

Unique index on `(u_initiative, u_team, u_month, u_period)` — one allocation row per combination.

### x_u4bsh_capmgmt_headcount ("Team Headcount")

Available FTE per team per month.

| Field | Type | Notes |
|---|---|---|
| `u_team` | reference → team | Mandatory. |
| `u_month` | choice (Jan–Dec) | Mandatory. Same legacy field as allocation. |
| `u_period` | reference → period | Optional. |
| `u_available_fte` | decimal (scale 2) | Available FTE for that team/month. |

Unique index on `(u_team, u_month, u_period)`.

### Relationships sketch

```
              linked to (optional, cross-scope)
initiative ───────────────────────────────► x_u4bsh_initiati_0_initiative
    │  1
    │
    │ N
    ▼
allocation ── u_team ──► team ──► u_business_app ──► cmdb_ci_business_app (cross-scope)
    │
    └── u_period ──► period   (optional; u_month is still the primary key path)

headcount ── u_team ──► team
headcount ── u_period ──► period   (optional; u_month is still the primary key path)
```

The **capacity gap** shown in the heatmap for a given team/month is simply:

```
gap = headcount.u_available_fte − SUM(allocation.u_fte)
```

## 4. Roles & Permissions

Roles nest: `admin` ⊃ `planner` ⊃ `viewer`.

| Role | Full name | Grants |
|---|---|---|
| Viewer | `x_u4bsh_capmgmt.viewer` | Read access on all 5 tables (initiative, allocation, team, headcount, period). |
| Planner | `x_u4bsh_capmgmt.planner` | Contains viewer. Write + create on `initiative` and `allocation`. Delete on those two tables is **admin-only**. |
| Admin | `x_u4bsh_capmgmt.admin` | Contains planner. `scopedAdmin: true`. Full write/create/delete on the config tables (`team`, `headcount`, `period`), plus delete on `initiative`/`allocation`. |

### Field-level ACLs (finer-grained than table ACLs)

- `u_snow_ref`, `u_snow_status`, `u_area`, `u_priority`, `u_tshirt_size`, `u_ado_ref`, `u_ado_status` — writable by **planner only while `u_initiative` is empty** (ACL script: `current.u_initiative == ''`). Once a plan item is linked to a real initiative, the `sync-initiative-fields` Business Rule owns these fields, and direct user edits are blocked at the ACL layer.
- `u_start`, `u_end` — hard deny-all-writes (`answer = true`), with `adminOverrides: false`. These are 100% system-derived and cannot be hand-edited by anyone, including admins.

## 5. Business Logic

All Business Rules live in `src/fluent/business-rules/*.now.ts` with server logic in `src/server/business-rules/*.ts`.

| Business Rule | Trigger | What it does |
|---|---|---|
| **derive-initiative-dates** | After insert / update / delete on `allocation` | Recomputes the parent initiative's `u_start`/`u_end` as the min/max of its linked periods' start/end dates (formatted `YYYY-MM`) across all of its allocations. Batches period lookups in a single `addQuery('sys_id','IN',...)` call (previously N+1 — one GlideRecord query per allocation row). Handles delete correctly by reading the initiative reference from `previous` (it's blank on `current` during a delete). |
| **derive-dates-on-item-insert** | Insert-time companion to the above | Handles the initial date-derivation case when an allocation is first inserted. |
| **sync-initiative-fields** | Before insert / update on `initiative`, condition `current.u_initiative != ''` | When a plan item is linked to a real external initiative record, copies `u_snow_status`, `u_snow_ref`, `u_ado_ref`, `u_ado_status`, `u_area`, `u_priority`, `u_tshirt_size` from the source record onto the local plan item. Skips empty source values so it never blanks out existing local data. |
| **propagate-initiative-changes** | Companion to sync-initiative-fields | Propagates further changes between the local plan item and the linked external record. |
| **resolve-initiative-link** | — | Resolves/validates the initiative-link relationship. |

In short: **allocations drive dates, and the linked external initiative drives status/classification fields** — once a link exists, those classification fields become effectively read-only for planners (enforced by the field ACLs above, not just convention).

## 6. REST API Surface

Defined in `src/fluent/restapi/capacity-api.now.ts`, implemented in `src/server/capacity-handler.ts`, service id `"capacity"`.

| Endpoint | Method | Handler | Purpose |
|---|---|---|---|
| `/api/x_u4bsh_capmgmt/capacity/data` | GET | `getData` | Returns the full dataset in one call: initiatives (as `projects`), allocations (as a per-initiative team→month FTE map, `p.ta[team][month] = fte`), headcount, teams, and a `periods` array. Builds period label maps once per request (`loadPeriodMaps`); resolves month keys with graceful fallback to the raw `u_month` string when `u_period` is empty, so pre-migration records still work. Linked-initiative lookups are batched (previously N+1). |
| `/api/x_u4bsh_capmgmt/capacity/allocations` | POST | `saveAllocations` | Batch upsert of edited grid cells. Validates that each `initiativeId` actually exists before writing (previously accepted arbitrary sys_ids without validation). |
| `/api/x_u4bsh_capmgmt/capacity/available` | GET | `getAvailableInitiatives` | Lists real initiatives from the external intake table that are not yet linked into the planner — feeds the "add initiative" picker. |
| `/api/x_u4bsh_capmgmt/capacity/add` | POST | `addInitiative` | Creates a Project-type plan item linked to a chosen real initiative. |
| `/api/x_u4bsh_capmgmt/capacity/status` | POST | `setPlanStatus` | Updates `u_plan_status` (Candidate / Committed / Removed). |
| `/api/x_u4bsh_capmgmt/capacity/create` | POST | `createInitiative` | Creates a plan item with **no** external link — for ad hoc/manual entries such as Absences. |

## 7. Frontend / UX

The frontend is a vanilla-JS SPA (`src/client/app.js`, ~2,260 lines, plus `index.html`), served as a BYOUI static page via a `UiPage` at `x_u4bsh_capmgmt_planner.do`. The built JS asset is registered as a `sys_ux_lib_asset` (`x_u4bsh_capmgmt/app` + `x_u4bsh_capmgmt/app.js.map`).

### Views

A `curView` state machine (`switchView()`) toggles between:

- **projects** — single plan item detail/edit view.
- **heatmap** — team × month capacity heatmap (the core "where are we over/under" view).
- **team** — by-team drill-down: plan-item list plus an allocation-vs-headcount summary table per team/month. Negative remaining FTE is styled in red (`cap-over` class).
- **overview** — flat, sortable table of all projects (e.g. click the "Name" header to sort).
- **pipeline** — kanban-style board grouped by SNOW/ADO status.
- **allplanitems** — flat list of every plan item.

### Key client-side concepts

- `MONTHS` — a fixed 12-entry array `['Jan', ..., 'Dec']`.
- `monthS` / `monthE` — indices into `MONTHS` driving a month-range slider (`mtrack`/`mfill`/`mthumb-s`/`mthumb-e`), with a manual from/to `<select>` picker as an alternative input method.
- `activeMos()` = `MONTHS.slice(monthS, monthE + 1)` — the single source of truth for "which months are currently in view." It's month-index based, **not year-aware** (see Known Issues).
- `projects` — an in-memory array mirroring the server's `RAW_DATA`. Each plan item `p` carries `p.ta` (team-allocation map), `p.rv`/`p.rc` (review ready/comment), `p.pls` (plan status), `p.ty` (type), etc.
- `TEAMS` — array of team names driving all team-indexed tables.
- `ROLE_TEAMS` — hardcoded `['BA-BusinessAnalyst', 'Architecture', 'PM']`, used by `missingRoleTeams(p)` to flag plan items with zero allocation to any of these three role-teams across the active month range. Shown as a red "!" badge with a tooltip listing the missing roles.
- **Editable grid** — clicking a cell opens inline edit; `finishEdit()` commits the value on blur.
- **Save** — `saveToServiceNow()` diffs the in-memory `projects` array against the `RAW_DATA` baseline and POSTs only the changed cells to `/allocations`.
- **Export** — `doExport()` / `buildXLSX()` produce a client-side Excel export of the current plan. The XLSX library is now bundled locally (it was previously loaded from a CDN, which ServiceNow's Content-Security-Policy blocked).
- **Review workflow** — a lightweight checkbox (`u_review_ready`) plus a free-text comment (`u_review_comment`) per plan item, surfaced as a green "R" badge in the sidebar when marked ready. This is explicitly **not** a full approval workflow or state machine — just a flag and a note.

## 8. Cross-Scope Integration

Two `CrossScopePrivilege` declarations (`src/fluent/acls/cross-scope.now.ts`) grant read-only access into tables owned by other scopes:

- **`x_u4bsh_initiati_0_initiative`** (scope `x_u4bsh_initiati_0`, sys_id `c126b5741bb5a690f004dc6fe54bcb67`) — the external, authoritative initiative-intake table. This app overlays capacity/allocation data on top of records that live here; `u_initiative` on the local plan item links back to it.
- **`cmdb_ci_business_app`** (global scope) — used to resolve business application display names for a team's `u_business_app` reference, and for the "available to add" initiative filter.

## 9. Deployment Workflow

```bash
npm install          # one-time: install SDK and dependencies
npm run build        # now-sdk build — compiles Fluent source into dist/
npm run deploy       # now-sdk install — pushes dist/ to the authenticated instance
```

`npm run build` must always precede `npm run deploy` — a failed build leaves the prior artifacts in `dist/` in place, so deploying without rebuilding first ships stale output.

Two manual steps are required after every deploy, neither of which is automated by the SDK:

1. **Commit the Update Set.** In-browser, the Update Set for `x_u4bsh_capmgmt` must be manually taken through Complete → Preview → Commit before the change actually takes effect on the instance.
2. **Hard-refresh the browser** on `x_u4bsh_capmgmt_planner.do`. The BYOUI JS asset is cached aggressively, so a normal refresh can silently keep serving the previous build.

Authentication against the instance is managed via the SDK CLI (`npx now-sdk auth ...`), not via `now.config.json`, which only holds app identity (`scope`, `scopeId`, `name`).

## 10. Known Issues / Architectural Debt

These are documented here as context for future work, not as an active bug list.

1. **Multi-year period migration is incomplete.** The legacy `u_month` field (bare `"Jan"`–`"Dec"`, no year) is still the primary key path used throughout the app; the newer `u_period` reference (year-aware, pointing at the `Period` table) was added as an optional companion field, but the migration to make it authoritative was never finished. Two concrete consequences today:
   - Server-side, `loadPeriodMaps()` keys its lookup maps by bare month abbreviation, so two `Period` records that fall in the same calendar month in different years can silently collide/overwrite each other.
   - Client-side, `activeMos()` is a plain slice of the 12-entry `MONTHS` array with no year concept, so a month range spanning a year boundary (e.g. Oct 2025 → Mar 2026) produces an empty slice and the grid silently renders nothing.
   Both are deferred pending a proper multi-year data migration rather than being quick fixes.

2. **Save vs. Export are easy to conflate in the UI.** At one point the "export" button was accidentally wired to trigger a save-to-ServiceNow action instead of the XLSX export. This has been fixed, but it's a reminder that these are two genuinely distinct actions (`saveToServiceNow()` vs. `doExport()`/`buildXLSX()`) that look similar in the toolbar.

3. **N+1 query patterns have needed batching more than once.** Both the `derive-initiative-dates` Business Rule and `getData()`'s linked-initiative resolution originally issued one GlideRecord query per row; both were later rewritten to use a single batched `IN`-query. Worth checking any new per-row logic against this pattern before it ships.

4. **`u_steerco_status` no longer exists.** It was a legacy field, fully removed from the schema, server code, and client code. Noted here only so it isn't accidentally reintroduced out of habit when extending status-related fields.
