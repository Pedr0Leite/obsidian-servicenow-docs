---
title: Capacity Management Overview (x_u4bsh_capmgmt)
tags:
  - servicenow
  - fluent-sdk
  - capacity-planning
  - internal-tool
  - scoped-app
  - now-sdk
  - business-rules
  - access-control
  - rest-api
  - cross-scope
  - update-sets
  - byoui
  - cmdb
aliases:
  - x_u4bsh_capmgmt
  - Capacity Planner
date: 2026-07-03
---

# Capacity Management Overview

## 1. Overview

**Capacity Management Overview** is a custom ServiceNow application, scoped as `x_u4bsh_capmgmt` (scope ID `0aaadae787e50b10d939a7573cbb353c`), built with the [[servicenow-sdk|Now SDK (Fluent)]], SDK version `@servicenow/sdk` 4.8.0. It lets planners and engineering leads plan projects, BAU work, and enhancements against team capacity (FTE — full-time equivalents) across the year.

It answers the question: *which teams are over- or under-allocated in a given month, and which projects are driving that* — for engineering managers, resource planners, and leadership doing quarterly/annual planning.

The app ships a custom single-page frontend (vanilla JS SPA) served at `x_u4bsh_capmgmt_planner.do`, plus a Scripted REST API for all data operations, and standard ServiceNow list views for administrative table access.

## 2. Purpose / Problem It Solves

Before this app, capacity planning lived in a manual spreadsheet nicknamed **"Soft & Hard Planning"** — a wide grid of projects vs. months vs. teams, updated by hand. Problems: no audit trail, no enforcement of available-vs-committed FTE, and no live link to the real initiative intake system.

This app replaces that spreadsheet with:
- A normalized data model (one row per allocation cell rather than one wide row per project).
- A live reference to the actual initiative intake table, so status/priority/sizing flow in automatically.
- A single interactive UI (heatmap, per-team drill-down, pipeline/kanban view, overview) built directly on that data model.
- Role-gated editing (viewer / planner / admin).
- A plan status concept (Candidate / Committed / Removed) fed by an Excel import pipeline.

## 3. Data Model

Five custom tables, all prefixed `x_u4bsh_capmgmt_`, defined via the Fluent [[table-api-now-ts|Table API]].

### x_u4bsh_capmgmt_initiative ("Capacity Plan Item")

A project, BAU item, enhancement, or absence entry being planned.

| Field | Type | Notes |
|---|---|---|
| `u_name` | string, max 255 | Plan item name. Mandatory. Display field. |
| `u_initiative` | reference → `x_u4bsh_initiati_0_initiative` | "Linked Initiative" — optional cross-scope link to the real intake record. Non-unique index on this field. |
| `u_area` | choice | CCO / Sales / Finance / Legal / People Experience / Marketing / cross function / Global IT / EA / IT / Cloud Ops. dropdown_with_none. Writable by planner only when `u_initiative` is empty (field ACL). |
| `u_priority` | choice (string) | '0' (P0 BAU) / '1' (P1) / '2' (P2) / '3' (P3) / '4' (P4). dropdown_with_none. ACL-locked when linked. |
| `u_tshirt_size` | choice | XS / S / M / L / XL. dropdown_with_none. ACL-locked when linked. |
| `u_type` | choice | Project / BAU / Enhancement / Absences. dropdown_with_none. |
| `u_start`, `u_end` | string YYYY-MM | **System-derived only** — computed by Business Rule from linked period dates. Hard deny-write ACL (`adminOverrides: false`) — no one, not even admins, can manually edit these. |
| `u_snow_ref` | string, max 100 | SNOW reference number (e.g. INIT0001234). ACL-locked when linked. |
| `u_ado_ref` | string, max 100 | Azure DevOps reference. ACL-locked when linked. |
| `u_snow_status` | choice | Approved / Screening / Qualified / Pending / New / Completed / Canceled. ACL-locked when linked. |
| `u_ado_status` | choice | In Progress / Done / New / On Hold. ACL-locked when linked. |
| `u_initiative_group` | string, max 255 | Free-text grouping label for the planner sidebar. |
| `u_comments` | multi-line text | Free-text notes. |
| `u_review_ready` | boolean | Lightweight "ready for review" flag — not a workflow/state machine. Shown as green "R" badge in sidebar. |
| `u_review_comment` | string, max 500 | Free-text review note, paired with `u_review_ready`. |
| `u_plan_status` | choice | Candidate / Committed / Removed. Default: **Committed** (table-level default). Set to `''` (empty) during bulk imports so the Transform Map can set it explicitly. |
| `u_steerco_status` | string, max 100 | "SteerCo status" — field still exists in the Fluent schema but has no active server logic or UI bindings. Do not re-implement. |

Index: non-unique on `u_initiative`.

> [!warning] u_plan_status default
> The table default for `u_plan_status` is `'Committed'`. Any GlideRecord `initialize()` call will pre-populate this. Scripts that need to leave it empty (e.g. bulk import) must explicitly call `setValue('u_plan_status', '')` after `initialize()` and before `insert()`.

> [!note] u_steerco_status
> The field is still present in `src/fluent/tables/initiative.now.ts` but has been removed from all server logic and client rendering. It should not be re-added to any handler, BR, or UI component.

### x_u4bsh_capmgmt_team ("Capacity Team")

An engineering or business team that capacity is planned against.

| Field | Type | Notes |
|---|---|---|
| `u_name` | string, max 100, unique | Mandatory. Display field. |
| `u_order` | integer | Display sequence used in the UI (ordered ascending by this field in `getData`). |
| `u_active` | boolean | Default `true`. Inactive teams are excluded from the teams array returned by `getData`. |
| `u_is_role_team` | boolean | Default `false`. Marks "role" teams (BA, Architecture, PM). The server returns these in a separate `roleTeams` array. The client uses `ROLE_TEAMS` (hardcoded `['BA-BusinessAnalyst', 'Architecture', 'PM']`) to flag plan items with zero allocation to any role team as a red "!" warning badge. |
| `u_business_app` | reference → `cmdb_ci_business_app` (global, cross-scope read) | Resolves a business application name for the team. Also indexed (non-unique) on this field. |

Unique index on `u_name`. Non-unique index on `u_business_app`.

### x_u4bsh_capmgmt_period ("Capacity Period")

One row per calendar month (e.g. "Jan 2025"). Year-aware companion to the legacy bare-month `u_month` field on allocation/headcount.

| Field | Type | Notes |
|---|---|---|
| `u_label` | string, max 10 | Mandatory, e.g. `"Jan 2025"`. Display field. |
| `u_start_date` | date | Mandatory. Used to derive the year-qualified month key (`YYYY-Jan`) by the server. |
| `u_end_date` | date | Mandatory. Used to compute initiative `u_end` dates. |
| `month_sequence` | integer, unique | Unique integer. Ordered ascending (`orderBy('month_sequence')`) in `loadPeriodMaps()` to produce `orderedPeriods`. This is the correct ordering key for period pickers and month-range UI across year boundaries — not `u_label` or `u_start_date`. |

> [!tip] Period ordering
> Always sort periods by `month_sequence` ascending, not by label or date. The server's `loadPeriodMaps()` does this already. Client-side, the `periods` array returned by `/data` is already sorted chronologically.

### x_u4bsh_capmgmt_allocation ("Capacity Allocation")

The core editable fact table: FTE assigned to one initiative, for one team, for one month. Tall/normalized — one row per grid cell.

| Field | Type | Notes |
|---|---|---|
| `u_initiative` | reference → initiative | Mandatory. `cascadeRule: delete` — deleting the initiative deletes all its allocations. |
| `u_team` | reference → team | Mandatory. |
| `u_month` | choice (Jan–Dec) | Mandatory. Legacy, year-unaware bare month string. Still the primary key path. |
| `u_period` | reference → period | Optional. Year-aware companion. When present, takes precedence over `u_month` in the server's `resolveMonthKey()` function. |
| `u_fte` | decimal, scale 2 | The allocated FTE amount. |

Unique index on `(u_initiative, u_team, u_month, u_period)`.

> [!important] Delete-on-zero
> `saveAllocations` deletes the allocation row when the FTE value is 0 or blank. It does **not** update the row to 0 and leave it. This keeps the table clean — only non-zero allocations have rows.

### x_u4bsh_capmgmt_headcount ("Team Headcount")

Available FTE per team per month.

| Field | Type | Notes |
|---|---|---|
| `u_team` | reference → team | Mandatory. |
| `u_month` | choice (Jan–Dec) | Mandatory. Same legacy field as allocation. |
| `u_period` | reference → period | Optional. Same year-aware companion as allocation. |
| `u_available_fte` | decimal, scale 2 | Available FTE for that team/month. |

Unique index on `(u_team, u_month, u_period)`.

### Relationships sketch

```
              linked to (optional, cross-scope READ)
initiative ───────────────────────────────────────► x_u4bsh_initiati_0_initiative
    │  1
    │ N (cascadeRule: delete)
    ▼
allocation ── u_team ──► team ──► u_business_app ──► cmdb_ci_business_app (cross-scope READ)
    │
    └── u_period ──► period   (optional; u_month is still the primary key path)

headcount ── u_team ──► team
headcount ── u_period ──► period   (optional; u_month is still the primary key path)
```

Capacity gap for a given team/month:

```
gap = headcount.u_available_fte − SUM(allocation.u_fte WHERE team=T AND month=M)
```

### Month key format

The server uses **year-qualified month keys** in the format `'YYYY-Jan'` (e.g. `'2025-Jan'`) throughout `capacity-handler.ts` — in all lookup maps, in the `headcount` response object, in `p.ta`, and in changes sent from the client. The legacy `u_month` field stores bare abbreviations (`'Jan'`). `saveAllocations` extracts the bare month with a `lastIndexOf('-')` split when storing to `u_month`.

## 4. Roles & Permissions

Roles nest: `admin` ⊃ `planner` ⊃ `viewer`. Defined via the Fluent [[role-api-now-ts|Role API]] and enforced with table- and field-level [[access-control-rules|ACLs]].

| Role | Full name | containsRoles | scopedAdmin | Grants |
|---|---|---|---|---|
| Viewer | `x_u4bsh_capmgmt.viewer` | — | false | READ on all 5 tables (initiative, allocation, team, headcount, period). |
| Planner | `x_u4bsh_capmgmt.planner` | viewer | false | WRITE + CREATE on initiative and allocation. DELETE is admin-only on both. |
| Admin | `x_u4bsh_capmgmt.admin` | planner | true | Full write/create/delete on all 5 tables (config tables team, headcount, period are admin-only for writes). |

### Table-level ACL matrix

| Table | READ | WRITE | CREATE | DELETE |
|---|---|---|---|---|
| `x_u4bsh_capmgmt_initiative` | viewer | planner | planner | **admin** |
| `x_u4bsh_capmgmt_allocation` | viewer | planner | planner | **admin** |
| `x_u4bsh_capmgmt_team` | viewer | **admin** | **admin** | **admin** |
| `x_u4bsh_capmgmt_headcount` | viewer | **admin** | **admin** | **admin** |
| `x_u4bsh_capmgmt_period` | viewer | **admin** | **admin** | **admin** |

All ACLs use `adminOverrides: true` **except** the field-level ACLs below.

### Field-level ACLs on `x_u4bsh_capmgmt_initiative`

These use `adminOverrides: false` — the restriction applies to everyone without exception.

| Field | Rule | Condition |
|---|---|---|
| `u_snow_ref` | WRITE allow for planner | `answer = (current.u_initiative == '')` — locked once linked |
| `u_snow_status` | WRITE allow for planner | same condition |
| `u_area` | WRITE allow for planner | same condition |
| `u_priority` | WRITE allow for planner | same condition |
| `u_tshirt_size` | WRITE allow for planner | same condition |
| `u_ado_ref` | WRITE allow for planner | same condition |
| `u_ado_status` | WRITE allow for planner | same condition |
| `u_start` | WRITE **deny** — `answer = true` | No one can write this, not even admin |
| `u_end` | WRITE **deny** — `answer = true` | No one can write this, not even admin |

The rationale: once a plan item is linked to a real initiative, the `sync-initiative-fields` BR owns those classification fields. Direct edits would be silently overwritten on the next save anyway.

## 5. Business Logic

All Business Rules live in `src/fluent/business-rules/*.now.ts` with server logic in `src/server/business-rules/*.ts`. Execution order matters — lower `order` values fire first.

### BR execution chain on `x_u4bsh_capmgmt_initiative` (BEFORE INSERT/UPDATE)

1. **`resolve-initiative-link`** (order 90, BEFORE insert/update, condition: `u_initiative == '' && u_snow_ref != ''`)
   - Auto-resolves `u_initiative` from `u_snow_ref` when the link is missing.
   - Queries `x_u4bsh_initiati_0_initiative` by `number` field matching `u_snow_ref`.
   - Only fires if `u_initiative` is currently empty and `u_snow_ref` is not. Allows the planner to type a SNOW number and have the link auto-populated.
   - Status: **active**

2. **`sync-initiative-fields`** (order 100, BEFORE insert/update, condition: `u_initiative != ''`)
   - Fires after `resolve-initiative-link`, so it can consume a freshly resolved link.
   - Reads the linked `x_u4bsh_initiati_0_initiative` and copies fields onto the local plan item.
   - Field mapping:

   | Source field | Target field | Transform |
   |---|---|---|
   | `business_area` | `u_area` | verbatim |
   | `number` | `u_snow_ref` | verbatim |
   | `state` | `u_snow_status` | `STATE_BUCKET` map: `-5→Pending`, `1→New`, `-3→Screening`, `-4→Qualified`, `2→Approved`, `3→Completed`, `7→Canceled` |
   | `high_level_sizing` (display value) | `u_tshirt_size` | `SIZE_MAP`: `X-Small→XS`, `Small→S`, `Medium→M`, `Large→L`, `X-Large→XL` (prefix match) |
   | `priority` | `u_priority` | Leading digit extracted via regex `/^(\d+)/` |
   | `u_ado_ref` | `u_ado_ref` | verbatim (pass-through) |
   | `u_ado_status` | `u_ado_status` | verbatim (pass-through) |

   - Skips empty source values — never blanks out existing local data.
   - Status: **active**

### BR on `x_u4bsh_capmgmt_allocation` (AFTER INSERT/UPDATE/DELETE)

**`derive-initiative-dates`** (AFTER all three operations, no condition)
- Triggered by any allocation change (insert, update, or delete).
- On delete: reads `u_initiative` from `previous` (it's blank on `current` during a delete).
- Collects all `u_period` sys_ids from the parent initiative's allocations.
- Batch-fetches period records in a single `IN` query (not N+1).
- Computes `min(u_start_date)` and `max(u_end_date)` across those periods, formatted as `YYYY-MM`.
- Writes `u_start` and `u_end` on the parent `x_u4bsh_capmgmt_initiative` using `setWorkflow(false)` to avoid triggering the initiative's own BRs.
- **Only works when allocations have a `u_period` reference.** Allocations with only a bare `u_month` (no period link) do not contribute to date derivation.
- Status: **active**

**`derive-dates-on-item-insert`** (AFTER INSERT on allocation)
- Insert-time companion to `derive-initiative-dates`. Handles the first-allocation case.
- Status: **active**

### BR on `x_u4bsh_initiati_0_initiative` (AFTER UPDATE)

**`propagate-initiative-changes`** (AFTER update on the **external** source table)
- Fires on the source initiative table in the external scope.
- Loops all linked `x_u4bsh_capmgmt_initiative` records with `u_initiative = <sys_id>` and calls `setWorkflow(true)` + `update()` on each — which triggers `sync-initiative-fields` on each linked plan item, propagating changes automatically.
- Status: **INACTIVE** (`active: false` in the Fluent declaration). Changes to source initiatives are **not** automatically propagated to plan items. Manual re-save of the plan item, or an admin script, is required.

> [!warning] Propagation is disabled
> `propagate-initiative-changes` is currently inactive. If a source initiative's area, priority, status, or sizing changes, the linked plan items will NOT update automatically. A planner must open and re-save each plan item, or run a background script to trigger updates.

## 6. REST API Surface

Defined via the Fluent [[scripted-rest-api-api-now-ts|Scripted REST API]] in `src/fluent/restapi/capacity-api.now.ts`, service ID `"capacity"`. Implemented in `src/server/capacity-handler.ts`. Base path: `/api/x_u4bsh_capmgmt/capacity`.

### GET `/data` — `getData`

Returns the full dataset for the planner UI in a single call. Response shape:

```json
{
  "projects": [ { ...planItem, "ta": { "TeamName": { "YYYY-Mon": fte } } } ],
  "headcount": { "TeamName": { "YYYY-Mon": fte } },
  "teams": ["TeamA", "TeamB"],
  "roleTeams": ["BA-BusinessAnalyst", "Architecture"],
  "periods": [ { "key": "2025-Jan", "label": "Jan 2025", "seq": 202501, "id": "<sys_id>" } ],
  "sliderRange": "<start_period_sysid>,<end_period_sysid>"
}
```

Plan item fields in `projects`:

| Client key | Source | Notes |
|---|---|---|
| `id` | `sys_id` | |
| `n` | `u_name` (or `short_description` from linked initiative if linked) | Linked initiative name wins |
| `a` | `u_area` (or `business_area` from linked initiative) | Linked wins |
| `p` | `u_priority` | |
| `s` | `u_tshirt_size` | |
| `st` | `u_start` (or `u_soft_planning_start_date` from linked initiative) | Linked start wins |
| `en` | `u_end` (or `u_release_date_month` / `u_hard_planning_release_date` / `u_release_date` from linked) | Linked end wins |
| `ty` | `u_type` | |
| `snow` | `u_snow_ref` (or `number` from linked) | Linked wins |
| `ado` | `u_ado_ref` | |
| `ss` | `u_snow_status` (or derived from `state` via `STATE_BUCKET`, with `active=false` → 'Completed' fallback) | Linked wins |
| `as` | `u_ado_status` | |
| `ig` | `u_initiative_group` | |
| `comments` | `u_comments` | |
| `rv` | `u_review_ready` | boolean |
| `rc` | `u_review_comment` | |
| `pls` | `u_plan_status` | Defaults to `'Committed'` if empty |
| `ta` | allocations nested by team→month→fte | |
| `linkId` | `u_initiative` sys_id | Only present when linked |
| `snowSize` | `high_level_sizing` display value from linked initiative | Only present when linked |
| `softRelease` | `u_soft_planning_release_date` from linked initiative (YYYY-MM) | Only present when linked |

**`sliderRange`:** read from sys_property `x_u4bsh_capmgmt.slider_period_range` (value: `start_period_sysid,end_period_sysid` or empty). When empty, the slider is hidden and the UI uses manual from/to pickers only.

**Linked initiative batch fetch:** all linked `x_u4bsh_initiati_0_initiative` records are loaded in a single `IN` query — not per-row. Same pattern for allocations nested into `ta`.

**Source initiative fields read by `getData` (for overlay):**

| Source field | Used for |
|---|---|
| `short_description` | `n` (name) |
| `business_area` | `a` (area) |
| `number` | `snow` (reference) |
| `u_soft_planning_start_date` | `st` (start month) |
| `u_release_date_month` | `en` (end month, first choice) |
| `u_hard_planning_release_date` | `en` (end month, fallback) |
| `u_release_date` | `en` (end month, second fallback) |
| `u_soft_planning_release_date` | `softRelease` (soft release month) |
| `state` | `ss` via STATE_BUCKET |
| `active` | `ss` fallback when state not mapped |
| `high_level_sizing` (display) | `snowSize` |

### POST `/allocations` — `saveAllocations`

Batch upsert of edited grid cells.

Request body: `{ changes: [ { initiativeId, team, month, value } ] }`

- `month` may be year-qualified (`'2025-Jan'`) or bare (`'Jan'`). The bare form is stored in `u_month`; the year-qualified form is used to look up the `u_period` sys_id via `periodIdByMonthKey`.
- **Upsert logic:** if a row exists, update or delete (when value ≤ 0). If no row exists and value > 0, insert.
- **Delete-on-zero:** when an existing row is updated with value ≤ 0, the row is deleted — not zeroed.
- **Initiative validation:** all unique `initiativeId` values in the batch are validated in bulk before processing. Unknown IDs are rejected per-change with an error string.
- **Period stamping:** when a period is found for the month key, both `u_month` (bare) and `u_period` (sys_id) are written to new/updated rows. This progressively migrates old rows to the year-aware format.

Returns: `{ saved, created, updated, deleted, errors: [] }`

### GET `/available` — `getAvailableInitiatives`

Returns source initiatives (`x_u4bsh_initiati_0_initiative`) not yet linked to any plan item. Used by the "Available to add" picker sidebar.

- Filters out initiatives with `active = false`.
- Reads `applications_affected` (comma-separated sys_ids of `cmdb_ci_business_app` records) from each source initiative.
- Batch-fetches `cmdb_ci_business_app` names in one `IN` query.
- Returns `appNames` array per initiative (resolved display names).

Source fields included in the response: `id`, `n` (short_description), `a` (business_area), `ty` (initiative_type), `s` (high_level_sizing), `ss` (state via STATE_BUCKET), `snow` (number), `st` (soft planning start), `en` (release date), `pri` (priority value), `priLabel` (priority display value), `apps` (sys_ids), `appNames` (display names).

### POST `/add` — `addInitiative`

Creates a Project-type plan item linked to a chosen source initiative.

- Validates the source initiative exists (404 if not).
- Returns existing plan item sys_id if already linked (idempotent).
- On new insert: sets `u_name = short_description`, `u_type = 'Project'`, `u_initiative = initiativeId`, `u_plan_status = 'Candidate'`.
- The `sync-initiative-fields` BEFORE INSERT BR then populates all other synced fields.

### POST `/status` — `setPlanStatus`

Updates `u_plan_status` of a plan item. Accepts only `'Candidate'`, `'Committed'`, or `'Removed'`.

### POST `/create` — `createInitiative`

Creates a plan item with **no** link to a source initiative — for ad hoc entries (Absences, manual items). Accepts: `name`, `area`, `priority`, `size`, `type`, `start`, `end`. All fields except `name` are optional. Sets `u_plan_status = 'Candidate'`.

> [!note] SIZE_RANGE in capacity-handler
> `capacity-handler.ts` defines a `SIZE_RANGE` map (`X-Small: [0,1]`, `Small: [1,1]`, `Medium: [2,3]`, `Large: [3,5]`, `X-Large: [5,12]`) intended for flagging a mismatch between the source initiative's expected duration and the planner's actual allocation span. This is computed server-side but currently only referenced internally — it is not yet surfaced in the `/data` response.

## 7. Frontend / UX

Vanilla-JS SPA (`src/client/app.js`), served as a BYOUI static page via a `UiPage` at `x_u4bsh_capmgmt_planner.do`. The built JS asset is registered as a `sys_ux_lib_asset` (`x_u4bsh_capmgmt/app` + `x_u4bsh_capmgmt/app.js.map`).

### Views (`curView` state machine — `switchView()`)

| View key | Description |
|---|---|
| `projects` | Single plan item detail/edit view |
| `heatmap` | Team × month capacity heatmap (the main allocation-vs-headcount view) |
| `team` | Per-team drill-down: plan item list plus allocation-vs-headcount summary table. Negative remaining FTE styled red (`cap-over` class) |
| `overview` | Flat, sortable table of all plan items |
| `pipeline` | Kanban-style board grouped by SNOW/ADO status |
| `allplanitems` | Flat list of every plan item |

### Key client-side state

- **`MONTHS`** — fixed 12-entry array `['Jan', ..., 'Dec']`. Used for bare-month indexing throughout.
- **`monthS` / `monthE`** — indices into `MONTHS` driving the month-range slider (`mtrack`/`mfill`/`mthumb-s`/`mthumb-e`). A manual from/to `<select>` picker is the fallback input method.
- **`activeMos()`** = `MONTHS.slice(monthS, monthE + 1)` — single source of truth for which months are in view. Year-unaware (see Known Issues).
- **`projects`** — in-memory array mirroring server `RAW_DATA`. Each plan item `p` carries `p.ta` (team→month→fte), `p.rv`/`p.rc` (review ready/comment), `p.pls` (plan status), `p.ty` (type), `p.ss` (SNOW status), `p.as` (ADO status), etc.
- **`TEAMS`** — array of active team names driving all team-indexed tables.
- **`ROLE_TEAMS`** — hardcoded `['BA-BusinessAnalyst', 'Architecture', 'PM']`. Used by `missingRoleTeams(p)` to flag plan items with zero allocation to any of these three role-teams across the active month range. Displayed as a red "!" badge with tooltip.
- **Editable grid** — clicking a cell opens inline edit; `finishEdit()` commits on blur.
- **Save** — `saveToServiceNow()` diffs in-memory `projects` against `RAW_DATA` baseline and POSTs only changed cells to `/allocations`.
- **Export** — `doExport()` / `buildXLSX()` produce a client-side XLSX export. The XLSX library is bundled locally (previously loaded from CDN, which ServiceNow's CSP blocks).
- **Review workflow** — `u_review_ready` checkbox + `u_review_comment` text per plan item. Shown as green "R" badge in sidebar. Explicitly not a workflow/state machine — just a flag and a note.
- **Slider period range** — controlled by sys_property `x_u4bsh_capmgmt.slider_period_range` (value: `start_period_sysid,end_period_sysid`). When the property is empty, the slider is hidden and only the manual pickers are shown.

## 8. Import / Transform Pipeline

The app includes a plan-status import pipeline for bulk-setting `u_plan_status` on existing plan items from an Excel file.

### Data Source: "Capmgmt Plan Status Import DS"

- Type: File (Excel, attachment-based)
- Import set table: `x_u4bsh_capmgmt_u_capmgmt_plan_status_import` (commonly abbreviated `u_capmgmt_plan_status_import`)
- Sheet: first sheet, header row 1, batch size 1000

The Excel file is attached to the Data Source record. Running the import populates the staging table with one row per Excel row.

Key staging table fields:
- `u_number` — initiative SNOW reference number (INIT0001234 format)
- `u_value_to_load` — the plan status value to apply

### Transform Map: "Capmgmt Plan Status Transform"

- Source: `x_u4bsh_capmgmt_u_capmgmt_plan_status_import`
- Target: `x_u4bsh_capmgmt_initiative`
- Coalesce field: `u_snow_ref` ← `u_number` (matches existing plan items by SNOW reference)
- Mapped field: `u_plan_status` ← `u_value_to_load`
- `runBusinessRules: true` — BRs fire on transformed records.

> [!info] This is why bulk-create scripts set u_plan_status = ''
> Plan items created by the bulk Background Script are created with `u_plan_status = ''` (empty) so the Transform Map can later set it correctly from the Excel import. If the script set `u_plan_status = 'Committed'`, the transform would still overwrite it — but leaving it empty keeps intent explicit and avoids a confusing default.

## 9. Cross-Scope Integration

Two `CrossScopePrivilege` declarations in `src/fluent/acls/cross-scope.now.ts`:

| Target table | Target scope | Target scope sys_id | Operation | Used by |
|---|---|---|---|---|
| `x_u4bsh_initiati_0_initiative` | `x_u4bsh_initiati_0` | `c126b5741bb5a690f004dc6fe54bcb67` | READ | `capacity-handler.ts` (getData, getAvailableInitiatives, addInitiative), `sync-initiative-fields` BR, `resolve-initiative-link` BR |
| `cmdb_ci_business_app` | global | — | READ | `getAvailableInitiatives` (resolves app names from `applications_affected`) |

No write cross-scope privileges exist. The app never writes to the external initiative table.

> [!warning] Background Scripts need scope selection
> When running a Background Script that reads `x_u4bsh_initiati_0_initiative`, the administrator must select scope `x_u4bsh_capmgmt` in the Script Editor before running. The cross-scope privilege is scoped — it only applies when executing within `x_u4bsh_capmgmt`.

## 10. System Properties

| Property name | Default | Description |
|---|---|---|
| `x_u4bsh_capmgmt.slider_period_range` | `''` (empty) | Slider default range: `start_period_sysid,end_period_sysid`. When empty, the period slider is hidden and the UI shows only the manual from/to pickers. Managed via the `sys_properties` table by an admin. |

## 11. Deployment Workflow

```bash
npm install          # one-time: install SDK and dependencies
npm run build        # now-sdk build — compiles Fluent source into dist/
npm run deploy       # now-sdk install — pushes dist/ to the authenticated instance
```

`npm run build` must always precede `npm run deploy`. A failed build leaves prior artifacts in `dist/` so deploying without rebuilding ships stale output.

Authentication is managed via the SDK CLI:
```bash
npx now-sdk auth --list
npx now-sdk auth --add <instance-url> --type basic|oauth
npx now-sdk auth --use <alias>
```

Two manual steps are required after every deploy:

1. **Commit the Update Set.** In-browser, navigate to System Update Sets, find the `x_u4bsh_capmgmt` update set, and take it through Complete → Preview → Commit.
2. **Hard-refresh the browser** on `x_u4bsh_capmgmt_planner.do`. The BYOUI JS asset is aggressively cached — a normal refresh can silently serve the previous build.

### Instance URL conventions

Use `_list.do` / `.do` suffix format — NOT `.list` (which fails in the Next Experience shell):

```
https://unit4dev1.service-now.com/<table_name>_list.do
https://unit4dev1.service-now.com/x_u4bsh_capmgmt_planner.do
https://unit4dev1.service-now.com/<table>.do?sysparm_query=ORDERBYsys_created_on&sysparm_limit=1
```

## 12. Known Issues / Architectural Debt

> [!bug] Multi-year period migration incomplete
> The legacy `u_month` field (bare `"Jan"`–`"Dec"`, no year) is still the primary key path throughout. The newer `u_period` reference (year-aware) was added as an optional companion but the migration to make it authoritative is incomplete.
>
> **Consequences today:**
> - Allocations with only `u_month` (no `u_period`) do not contribute to `u_start`/`u_end` date derivation — `derive-initiative-dates` only processes period-linked rows.
> - Client-side `activeMos()` is a plain 12-entry slice with no year concept — a month range spanning a year boundary (e.g. Oct 2025 → Mar 2026) produces an empty or wrong slice.
> - `loadPeriodMaps()` uses year-qualified keys (`YYYY-Jan`) which avoids the collision problem server-side, but the client still receives period objects that need to be interpreted correctly.
>
> **Mitigation in place:** `month_sequence` (unique integer) on `x_u4bsh_capmgmt_period` is the correct sort key for cross-year ordering. `loadPeriodMaps()` orders by this and returns `orderedPeriods` to the client already sorted.

> [!bug] propagate-initiative-changes is inactive
> Changes to source initiative records (`x_u4bsh_initiati_0_initiative`) are not automatically propagated to linked plan items. The BR that would handle this (`propagate-initiative-changes`) has `active: false`. Plan item synced fields only update on manual re-save of the plan item.

> [!tip] N+1 query pattern — always check before adding per-row logic
> Both `derive-initiative-dates` and `getData`'s linked-initiative resolution originally issued one GlideRecord query per row; both were rewritten to use single batched `IN` queries. Any new per-row logic should follow the same pattern — collect IDs first, then batch-fetch.

> [!note] u_steerco_status field
> The field still exists in the Fluent table schema (`src/fluent/tables/initiative.now.ts`) but has been removed from all server handlers, BRs, and client rendering. The field definition in the schema is inert — it just means the database column exists. Do not re-add it to any logic.

> [!note] Save vs. Export distinction
> `saveToServiceNow()` and `doExport()` / `buildXLSX()` are two distinct actions. The export button was historically wired to save at one point. They must remain separate code paths.

## 13. Related Documentation

**Now SDK / Fluent (build tooling for this app):**
- [[servicenow-sdk]] — landing page for the Now SDK used to build this app
- [[fluent-constructs]] — the metadata-as-code model Fluent source files follow
- [[create-application-now-sdk]] / [[build-deploy-application-now-sdk]] — app scaffolding and the build → deploy CLI flow
- [[table-api-now-ts]] — Fluent API used to define the 5 custom tables
- [[business-rule-api-now-ts]] — Fluent API backing the Business Rules in [[#5. Business Logic]]
- [[scripted-rest-api-api-now-ts]] — Fluent API backing the [[#6. REST API Surface]]
- [[fluent-ui-page-api]] — Fluent API behind the BYOUI `UiPage` serving the SPA
- [[role-api-now-ts]] / [[acl-api-now-ts]] / [[cs-privileges-api-now-ts]] — Fluent APIs behind [[#4. Roles & Permissions]] and [[#9. Cross-Scope Integration]]

**Platform concepts referenced above:**
- [[access-control-rules]] — general ACL rule model underlying the viewer/planner/admin role design
- [[acl-function-fields]] — field-level ACL mechanics used for `u_start`/`u_end` and the sync-owned fields
- [[eaw-business-application-form]] — the `cmdb_ci_business_app` record type that `team.u_business_app` resolves against
- [[system-update-sets]] / [[t_CommitAnUpdateSet]] — the manual Update Set commit step required after every deploy

**One-time scripts run against this app's data (companion notes, same folder):**
- [[capacity-planner-set-start-and-end-date-to-plan-items]] — Fix Script backfilling `u_start`/`u_end` from linked Period dates
- [[generate-capacity-plan-items]] — Background Script bulk-creating Plan Items from active Initiatives, with the `u_area`/`u_priority`/`u_snow_status` choice-mapping rules

**Backlog & planning:**
- [[capacity-planner-backlog-2026-07]] — July 2026 sprint backlog (8 decisions from 2026-07-09 brainstorm): Committed-only metrics, allocation import hardening, period persistence, global management view, parent/child hierarchy, Overview Teams column
