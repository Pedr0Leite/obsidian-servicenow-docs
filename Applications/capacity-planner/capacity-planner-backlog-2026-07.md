---
title: Capacity Planner — Sprint Backlog (July 2026)
aliases:
  - capacity-planner-backlog
  - capmgmt-backlog-2026-07
area: Applications/capacity-planner
tags:
  - servicenow
  - capacity-planning
  - internal-tool
  - scoped-app
  - backlog
  - business-analysis
  - now-sdk
date: 2026-07-13
source: Meeting notes 2026-07-09 "Capacity planner - brainstorm"
---

# Capacity Planner — Sprint Backlog (July 2026)

> Source: Meeting notes 2026-07-09 "Capacity planner - brainstorm" (8 decisions)
> App scope: `x_u4bsh_capmgmt` | Instance: unit4dev1.service-now.com
> Grounding: [[capacity-planner]], [[generate-capacity-plan-items]], [[capacity-planner-set-start-and-end-date-to-plan-items]]

---

## Related

- [[capacity-planner]] — full app overview (data model, roles/ACLs, BRs, REST API, known issues)
- [[generate-capacity-plan-items]] — bulk Plan Item creation script; field-mapping assumptions flagged here
- [[capacity-planner-set-start-and-end-date-to-plan-items]] — u_start/u_end backfill; ACL-bypass pattern referenced in allocation import stories

---

## Sequencing Roadmap

| Wave | Story ID | Title | Epic (Decision) | Coupling(s) that drove placement |
|---|---|---|---|---|
| **1 — Spikes + Foundation** | SPIKE-01 | Identify allocation import mechanism | Epic 2/3/8 | 2↔3↔8: nothing in the allocation workstream can be scoped without this answer |
| 1 | SPIKE-02 | Identify parent/child field on source initiative | Epic 6 | 1↔6: cannot scope hierarchy fix without field name; 2↔3↔8 is parallel |
| 1 | DATA-01 | DEV3 allocation data quality baseline | Epic 2/3/8 | 3↔8: duplicate-detection tooling must exist BEFORE further import iterations run |
| **2 — Core Build** | CAPMGMT-01 | Total Projects — Committed filter | Epic 1 | 1↔8 (testable only at status-import stable checkpoint); 1↔6 (partial fix until hierarchy lands) |
| 2 | CAPMGMT-04 | Persist period selection to localStorage | Epic 4 | 4↔5, 4↔7: period-range policy must be stated before Global view and Overview stories are built on top |
| 2 | CAPMGMT-05 | Improve Overview Teams column | Epic 7 | 5↔7: scope must be disambiguated from CAPMGMT-06 before either is estimated |
| 2 | CAPMGMT-03 | Harden allocation import — u_period stamping | Epic 2/3/8 | 2↔3↔8; **BLOCKED BY SPIKE-01** — placed Wave 2 because spike is Wave 1 |
| 2 | CAPMGMT-02 | Allocation import validation — anomaly detection | Epic 2/3/8 | 3↔8; **BLOCKED BY SPIKE-01 + DATA-01** |
| **3 — Dependent / Blocked** | CAPMGMT-06 | Global management view | Epic 5 | 5↔7 (scope overlap with CAPMGMT-05 must be resolved first); 4↔5 (inherits CAPMGMT-04's period policy) |
| 3 | CAPMGMT-07 | Parent/child hierarchy — defensive counting | Epic 6 | 1↔6; **BLOCKED BY SPIKE-02** |

> [!note] Decision 8 (ongoing data migration)
> Decision 8 ("more allocation data still needs validation and import") is an operational workstream, not a single deliverable. It is represented by DATA-01 (current-state assessment), CAPMGMT-02 (hardening the import path), CAPMGMT-03 (validation tooling), and subsequent manual import iterations that follow those. No separate story is created for "run the import" — that is an operator action, not a build item.

---

## Epic 1 — Total Projects Metric (Decision 1)

> Decision 1: Total Projects should only represent active planning work — driven by Committed Plan Items, not all initiatives.

### CAPMGMT-01 — Total Projects: filter to Committed plan items only

**As a** capacity planning manager, **I want** the "Total Projects" count in the planner UI to reflect only Committed plan items **so that** leadership sees actionable committed work, not the full pipeline of Candidates and Removed items.

**Acceptance Criteria:**

1. ASSUMPTION (locate first): "Total Projects" is a numeric count displayed in the planner SPA (app.js). Its exact render location, DOM element, and variable name are NOT documented in [[capacity-planner]]. Before any code change, the developer must search `app.js` for count-related display elements (patterns: `'Total'`, `totalProj`, `projects.length`, count render in overview/heatmap section headers) and confirm the element. If it does not exist, this story is redefined as "add a Total Projects count to the Overview header." **[Open Question — see §OQ-1]**

2. The filter expression for Committed plan items, using the client-side `projects` array: `projects.filter(p => p.pls === 'Committed' && p.ty === 'Project').length`

3. CRITICAL CONSTRAINT — getData normalisation: `capacity-handler.ts` `getData` already normalises empty `u_plan_status` to `'Committed'` server-side: `'pls': pi.getValue('u_plan_status') || 'Committed'`. This means client-side `p.pls === 'Committed'` will match **both** genuinely Committed records AND records with `u_plan_status = ''` (those still pending the status import from [[generate-capacity-plan-items]]). The count will over-count pending-import rows until the status Transform Map ("Capmgmt Plan Status Transform") has been applied to all of them. This limitation must be documented as a UI tooltip or adjacent label: "Count includes items pending status assignment." Verify the normalisation is still in place in `capacity-handler.ts` before implementing.

4. CONSTRAINT — propagate-initiative-changes INACTIVE: If a source initiative's real status changes in `x_u4bsh_initiati_0_initiative`, its linked Plan Item's `u_plan_status` does NOT automatically update (the `propagate-initiative-changes` BR has `active: false`). The count reflects stale cached data until a planner manually re-saves or a background script forces a refresh. Document this staleness risk in the tooltip.

5. Only `u_type = 'Project'` items are counted. BAU, Enhancement, and Absences are excluded. ASSUMPTION — confirm with business that "Total Projects" explicitly excludes non-Project types. **[Open Question — see §OQ-2]**

6. The count is derived from the in-memory `projects` array (already loaded from `GET /data`) — no new REST endpoint or additional round-trip is introduced.

7. PARTIAL CORRECTNESS: Even after this story lands, hierarchy-driven double-counting (decision 6, CAPMGMT-07) remains unresolved. If a parent and a child initiative both have Committed Plan Items, both appear in the count. This is a documented known limitation until CAPMGMT-07 ships. Add an inline code comment: `// ponytail: Committed filter only — hierarchy double-counting remains until CAPMGMT-07`.

8. 1↔8 coupling: the count is not meaningfully accurate until the status import (see Epic 2/3/8) has reached a stable checkpoint where most Plan Items have an explicit `u_plan_status` value rather than the empty default.

**ServiceNow Implementation Notes:**
- Client file: `src/client/app.js` (or equivalent compiled asset)
- Projects array: `projects` (in-memory, populated from `GET /api/x_u4bsh_capmgmt/capacity/data`)
- Plan status field: `p.pls` = `u_plan_status` (normalised to `'Committed'` if empty by `getData` in `capacity-handler.ts`)
- Type field: `p.ty` = `u_type` (choices: Project / BAU / Enhancement / Absences)
- No changes to `capacity-handler.ts` required if the normalisation in `getData` is confirmed
- No new ACL, BR, or REST endpoint required

**Story Points:** 2 | **Priority:** High | **Dependencies:** DATA-01 (for accurate baseline understanding of u_plan_status distribution)
**Coupling:** 1↔8 (not meaningfully testable until status import stable), 1↔6 (partial fix only)

---

## Epic 2/3/8 — Allocation Import Workstream (Decisions 2, 3, 8 — Shared Epic)

> Decisions 2, 3, and 8 are one workstream, not three independent tickets. Decision 2: Start/End dates should come from allocations. Decision 3: Allocation import must become source of truth for dates, with validation. Decision 8: Ongoing data migration iterations must be validated.
> **These three decisions cannot be scoped, sequenced, or estimated independently — they share SPIKE-01 as a prerequisite.**

### SPIKE-01 — Identify the actual allocation import mechanism

**As a** data migration owner and developer, **I want** to document exactly how allocation data is (or should be) imported in bulk **so that** CAPMGMT-03 (hardening) and CAPMGMT-02 (validation) can be scoped against the real mechanism rather than a guessed one.

**Acceptance Criteria:**

1. Document which mechanism is currently used for bulk allocation imports. Options to investigate:
   - a) A **Transform Map** targeting `x_u4bsh_capmgmt_allocation` (check: System Import Sets > Transform Maps, filter by target table)
   - b) A **Background Script** that calls `GlideRecord.insert()` on `x_u4bsh_capmgmt_allocation` directly
   - c) Manual HTTP calls to `POST /api/x_u4bsh_capmgmt/capacity/allocations` (the `saveAllocations` endpoint)
   - d) None yet exists — allocations have been entered manually via the UI
   - e) A combination

2. For whichever mechanism is identified: document whether it sets `u_period` on each allocation row (the year-aware `x_u4bsh_capmgmt_period` sys_id reference) alongside the legacy `u_month` bare string. **This is the single most important fact — `derive-initiative-dates` only processes allocations that have `u_period` set.**

3. Document whether the mechanism executes with `runBusinessRules = true` (or equivalent) or with `setWorkflow(false)`. This determines whether `derive-initiative-dates` and `derive-dates-on-item-insert` fire during import and whether `u_start`/`u_end` are auto-computed.

4. Document whether the mechanism creates `x_u4bsh_capmgmt_initiative` (Plan Item) records as a side effect — or exclusively writes to `x_u4bsh_capmgmt_allocation`. This directly addresses decision 3's concern about "unexpectedly creating Plan Items."

5. Document the source data format: column headers, sheet structure, any existing template file.

6. Deliverable: a written summary (update this backlog or create/update `Applications/capacity-planner/allocation-import.md`) covering all of the above, plus a recommended implementation path for CAPMGMT-03.

**ServiceNow Implementation Notes:**
- Check Transform Maps: `System Import Sets > Administration > Transform Maps` — filter by `Target table` contains "allocation"
- Check Data Sources: `System Import Sets > Administration > Data Sources` — filter by `Import set table` contains "allocation"
- Check Background Scripts in scope `x_u4bsh_capmgmt`: Studio > Script Files or `sys_script_fix_list.do?sysparm_query=application.nameSTARTSWITHCapacity`
- Relevant endpoint: `POST /api/x_u4bsh_capmgmt/capacity/allocations` → `saveAllocations` in `capacity-handler.ts`. Note: `saveAllocations` already stamps `u_period` when the period map has an entry for the month key — if this is the import path, `u_period` stamping is already handled provided `periodIdByMonthKey` is populated.
- Cross-scope note: admin must select scope `x_u4bsh_capmgmt` in Background Scripts to access allocation table

**Story Points:** 2 | **Priority:** Critical | **Dependencies:** None

---

### DATA-01 — DEV3 allocation data quality baseline

**As a** data migration owner, **I want** a structured assessment of the allocation data currently in DEV3 **so that** we know what has been imported, how complete it is, and whether any anomalous Plan Items were created as side effects, before running further import iterations.

**Acceptance Criteria:**

1. Count `x_u4bsh_capmgmt_allocation` rows where `u_period IS NULL` (legacy `u_month`-only, invisible to `derive-initiative-dates`) vs. rows where `u_period IS NOT NULL` (year-aware, correctly drive date derivation).

2. Count `x_u4bsh_capmgmt_initiative` (Plan Item) records where `u_start IS NULL` or `u_end IS NULL`, broken down by:
   - Has period-linked allocations but dates not derived (suggests `derive-initiative-dates` did not fire during import)
   - Has no allocations at all (recently created, no allocation yet)
   - Has only legacy `u_month`-only allocations (dates cannot be derived until those rows are migrated)

3. Identify Plan Items with anomalous creation characteristics: `u_plan_status = ''` (empty, pending the status import), created within a narrow timestamp window (suggesting bulk creation), and `u_name` matching a `short_description` pattern from the source initiative table.

4. Count duplicate Plan Items: two or more `x_u4bsh_capmgmt_initiative` rows sharing the same `u_initiative` sys_id value. CONSTRAINT: `u_initiative` has a **non-unique** index — duplicates are possible and not blocked at the schema level.

5. Deliverable: a written findings report (plain text in this vault or attached to this story) — not a code change. No writes to any table. Read-only diagnostic only.

6. ASSUMPTION: "more allocation data still needs validation and import" (decision 8) refers to additional rows for already-imported initiatives, not a new batch of previously-unknown initiatives. If it refers to net-new initiatives, this story's scope and DATA-01's baseline count changes. **[Open Question — see §OQ-8]**

**ServiceNow Implementation Notes:**
- All queries run as Background Scripts in scope `x_u4bsh_capmgmt` (read-only)
- Legacy rows: `var a = new GlideAggregate('x_u4bsh_capmgmt_allocation'); a.addNullQuery('u_period'); a.addAggregate('COUNT'); a.query();`
- Period-linked rows: same with `addNotNullQuery('u_period')`
- Duplicate detection: `var dup = new GlideRecord('x_u4bsh_capmgmt_initiative'); dup.addNotNullQuery('u_initiative'); dup.groupBy('u_initiative'); dup.addHaving('COUNT', 'u_initiative', '>', 1); dup.query();` (use GlideAggregate for cross-reference)
- No write operations; no deploy required

**Story Points:** 2 | **Priority:** High | **Dependencies:** None (can run in parallel with SPIKE-01 and SPIKE-02)
**Coupling:** 3↔8

---

### CAPMGMT-03 — Harden allocation import: u_period stamping and date derivation

**BLOCKED BY: SPIKE-01**

**As a** data migration owner, **I want** every allocation row imported in bulk to have both `u_month` and `u_period` populated, and `derive-initiative-dates` to fire on insert **so that** `u_start`/`u_end` on the linked Plan Item are automatically computed from allocation dates, making the import the source of truth for dates.

**Acceptance Criteria:**

1. **BLOCKED BY SPIKE-01**: the exact implementation path is unknown until the spike confirms the mechanism. The criteria below are the required outcomes regardless of path.

2. After this story, any new allocation row created by the import mechanism must have:
   - `u_month`: bare month string (e.g. `'Jan'`) — required for the unique index `(u_initiative, u_team, u_month, u_period)`
   - `u_period`: sys_id reference to the matching `x_u4bsh_capmgmt_period` record for that month and year — required for `derive-initiative-dates` to process it

3. CONSTRAINT — date derivation chain: `derive-initiative-dates` (AFTER INSERT/UPDATE/DELETE on `x_u4bsh_capmgmt_allocation`) fires only when `u_period` is set on the row. If the import sets only `u_month`, dates are not derived. The hardened import must guarantee `u_period` is set.

4. CONSTRAINT — BR execution: `derive-initiative-dates` only fires if the import mechanism does NOT call `setWorkflow(false)`. If the mechanism uses `setWorkflow(false)`, the import must trigger date derivation manually as a post-import step (call `derive-initiative-dates` logic against all affected Plan Items, following the same `setWorkflow(false)` pattern used by the BR itself — using plain `GlideRecord`, not `GlideRecordSecure` or a Scripted REST endpoint, since `u_start`/`u_end` have a deny-write field ACL that is only bypassed by plain server-side GlideRecord).

5. CONSTRAINT — ACL bypass: `u_start`/`u_end` carry a hard deny-write field ACL (`adminOverrides: false`) that blocks writes via `GlideRecordSecure`, Scripted REST endpoints, GlideAjax, and UI submissions. Only plain server-side `GlideRecord` (as used by `derive-initiative-dates` with `setWorkflow(false)`) can write these fields. Any import path that routes through `POST /api/x_u4bsh_capmgmt/capacity/allocations` will NOT directly update `u_start`/`u_end` via the REST layer — it must rely on `derive-initiative-dates` firing server-side.

6. After this story, importing N allocation rows for M distinct initiatives should result in: all N rows having `u_period` set, all M Plan Items having `u_start` and `u_end` derived from the min/max of their linked period dates.

7. Legacy rows (existing in DEV3 with `u_period = NULL`) are NOT retroactively fixed by this story. Those are handled by [[capacity-planner-set-start-and-end-date-to-plan-items|backfillPlanItemDates]] and/or a one-time migration pass.

8. ASSUMPTION: one `x_u4bsh_capmgmt_period` record exists per calendar month (1:1 month-to-period). Verify against the period table before implementation — if multiple period records exist per month (e.g. different fiscal calendars), the lookup logic must be more specific.

**ServiceNow Implementation Notes (to be detailed after SPIKE-01):**
- If **Transform Map path**: add an `onBefore` transform script that looks up `x_u4bsh_capmgmt_period` where `u_start_date` falls in the target month/year, and sets `u_period` on the target allocation row before insert
- If **`POST /allocations` (saveAllocations) path**: `saveAllocations` in `capacity-handler.ts` already stamps `u_period` via `periodIdByMonthKey` when the month key has a matching period — verify the period map is populated (it is loaded by `loadPeriodMaps()` which queries `x_u4bsh_capmgmt_period` ordered by `month_sequence`). If the month key format from the import doesn't match (`'YYYY-Jan'`), fix the key format
- If **direct GlideRecord path**: after `.initialize()` and field sets, look up the `x_u4bsh_capmgmt_period` sys_id by month+year and call `setValue('u_period', periodSysId)` before `.insert()`
- `derive-initiative-dates` is located in `src/fluent/business-rules/*.now.ts` (AFTER INSERT/UPDATE/DELETE on `x_u4bsh_capmgmt_allocation`)
- `derive-dates-on-item-insert` handles the first-allocation case (AFTER INSERT only)
- Both BRs write to `x_u4bsh_capmgmt_initiative` using `setWorkflow(false)` to avoid re-triggering the initiative's own BRs

**Story Points:** 5 (TBD after SPIKE-01) | **Priority:** High | **Dependencies:** SPIKE-01 (blocked)
**Coupling:** 2↔3↔8

---

### CAPMGMT-02 — Allocation import validation: anomaly detection and idempotency

**BLOCKED BY: SPIKE-01, DATA-01**

**As a** data migration owner, **I want** a validation diagnostic and a documented idempotency contract for the allocation import path **so that** we can detect unexpected Plan Item creation and duplicate allocations before each import iteration runs, rather than cleaning up bad data afterwards.

**Acceptance Criteria:**

1. **BLOCKED BY SPIKE-01**: whether the import mechanism creates Plan Items as a side effect is unknown until the spike. If the mechanism only writes to `x_u4bsh_capmgmt_allocation`, this story's scope narrows to duplicate allocation detection only.

2. CONSTRAINT — single idempotency check pattern: `u_initiative` has a **non-unique index** on `x_u4bsh_capmgmt_initiative`. Nothing at the schema level prevents two Plan Items linking to the same source initiative. At least two independent idempotency checks already exist (the `addInitiative` REST handler check, and the [[generate-capacity-plan-items]] script's inline check). This story must NOT create a third divergent implementation. Instead, it must: (a) identify all existing idempotency check implementations, (b) converge them on one shared pattern (e.g. a Script Include `CapMgmtPlanItemUtils.getExistingPlanItem(sourceInitiativeSysId)`) and (c) have the allocation import validation use that same shared check.

3. A pre-import validation script (Background Script, scope `x_u4bsh_capmgmt`) must report:
   - Duplicate Plan Items: any `u_initiative` value that appears more than once in `x_u4bsh_capmgmt_initiative`
   - Missing Plan Items: any `u_initiative` values present in the import source data that have no corresponding Plan Item (unexpected gap)
   - Orphaned allocations: allocation rows in `x_u4bsh_capmgmt_allocation` where the referenced `u_initiative` sys_id has no corresponding Plan Item record
   - Legacy-only rows: allocation rows with `u_period = NULL` that will be invisible to `derive-initiative-dates`

4. CONSTRAINT — propagate-initiative-changes INACTIVE: Plan Items may carry stale `u_area`, `u_priority`, `u_snow_status` values if the linked source initiative changed after the Plan Item was created. The validation should include a staleness flag: for each Plan Item with `u_initiative` set, compare local field values against the `sync-initiative-fields` BR mapping of the current source initiative values. Log discrepancies as warnings — do not auto-correct them (that is a separate operational step).

5. The deliverable is: (a) a diagnostic Background Script checked into `docs/validate-allocation-import.js` (or equivalent location), and (b) a written remediation procedure for each anomaly type (duplicate Plan Items → manual delete, orphaned allocations → manual delete or re-link, staleness → re-save Plan Item to trigger sync-initiative-fields).

6. The validation script runs in read-only mode by default (`DRY_RUN = true` pattern, consistent with [[generate-capacity-plan-items]] and [[capacity-planner-set-start-and-end-date-to-plan-items]]).

**ServiceNow Implementation Notes:**
- Duplicate detection: `var dup = new GlideAggregate('x_u4bsh_capmgmt_initiative'); dup.addNotNullQuery('u_initiative'); dup.groupBy('u_initiative'); dup.addAggregate('COUNT'); dup.query(); while (dup.next()) { if (dup.getAggregate('COUNT') > 1) gs.warn(...) }`
- Staleness check: batch-fetch linked `x_u4bsh_initiati_0_initiative` records (same `IN` query pattern as `getData` — never N+1), apply `STATE_BUCKET` and `SIZE_MAP` from `sync-initiative-fields`, compare to local Plan Item field values
- STATE_BUCKET and SIZE_MAP constants are defined in `src/server/business-rules/sync-initiative-fields.ts` — reference them, don't re-implement
- The shared idempotency Script Include (if created): `x_u4bsh_capmgmt.CapMgmtPlanItemUtils`, method `getExistingPlanItem(initiativeSysId)` → returns existing Plan Item GlideRecord or null
- Cross-scope READ privilege covers `x_u4bsh_initiati_0_initiative` for staleness comparison

**Story Points:** 3 (TBD after SPIKE-01) | **Priority:** High | **Dependencies:** SPIKE-01 (blocked), DATA-01 (informs scope)
**Coupling:** 3↔8

---

## Epic 4 — Period Persistence (Decision 4)

> Decision 4: Period selection must be preserved across page refreshes, persisted in the browser.

### CAPMGMT-04 — Persist period selection to localStorage

**As a** capacity planner, **I want** my selected period range (from/to months) to survive page refreshes **so that** I don't have to reconfigure my view after each navigation.

**Acceptance Criteria:**

1. When the user adjusts the period slider or the from/to pickers, the selected range is saved to `localStorage` under the key `x_u4bsh_capmgmt.periodRange`. ASSUMPTION: single-device persistence (localStorage) is sufficient. If cross-device sync is required, a user preference record in ServiceNow is needed — this story's scope changes. **[Open Question — see §OQ-4]**

2. CONSTRAINT — persisted format: the value stored in localStorage MUST use year-qualified period identifiers — specifically the `id` field (sys_id of `x_u4bsh_capmgmt_period`) from the `periods` array returned by `GET /data`. Storing raw `monthS`/`monthE` indices into the fixed `MONTHS` array is explicitly prohibited: those indices encode the existing year-unaware bug durably in the browser and will produce wrong results when the multi-year migration (see [[capacity-planner#12. Known Issues / Architectural Debt|Known Issues]]) is eventually fixed.

   Stored structure: `{ "startPeriodId": "<sys_id>", "endPeriodId": "<sys_id>" }`

3. On page load, after `GET /data` returns and the `periods` array is available (already sorted chronologically by `month_sequence` via `orderedPeriods`): read the stored period IDs from localStorage, find their positions in the `periods` array by matching the `id` field, and set `monthS`/`monthE` to those positions. If either stored ID is not found (period deleted or out of range), discard the stored value entirely and fall back to the default.

4. Default fallback (when no valid persisted value exists): honour the sys_property `x_u4bsh_capmgmt.slider_period_range` (reads `start_period_sysid,end_period_sysid` from `sliderRange` in the `/data` response). When `sliderRange` is empty, show the manual pickers with no pre-selected range — no change from current behaviour.

5. Period range changes (slider drag end, picker `change` event) trigger a localStorage write immediately. No save button required.

6. DOWNSTREAM POLICY DECISION — both CAPMGMT-05 (Overview Teams column) and CAPMGMT-06 (Global management view) must explicitly state their period-range behaviour relative to this persisted selection:
   - CAPMGMT-05 (Overview): **honours** the persisted range — active months are filtered to `monthS`/`monthE` as usual
   - CAPMGMT-06 (Global view): **ignores** the persisted range — always shows all periods (whole-year view by design). This must be documented in CAPMGMT-06's UI (e.g. "Showing all periods").

**ServiceNow Implementation Notes:**
- localStorage key: `x_u4bsh_capmgmt.periodRange` (scoped prefix avoids key collisions)
- Write: after any `monthS`/`monthE` change that originates from user interaction (slider `mouseup`, picker `change`): `localStorage.setItem('x_u4bsh_capmgmt.periodRange', JSON.stringify({ startPeriodId: periods[monthS].id, endPeriodId: periods[monthE].id }))`
- Read (on load, inside the data-load callback after `periods` is populated): lookup stored IDs in `periods` array using `.findIndex(p => p.id === stored.startPeriodId)` — if -1, discard and use default
- The slider rendering (`mtrack`/`mfill`/`mthumb-s`/`mthumb-e`) reads `monthS`/`monthE` — no change to slider render code if the indices are set correctly before first render
- `sliderRange` is already present in the `GET /data` response (populated from sys_property `x_u4bsh_capmgmt.slider_period_range`)
- No server-side changes; no new REST endpoint; no ACL or BR changes

**Story Points:** 3 | **Priority:** Medium | **Dependencies:** None (self-contained)
**Coupling:** 4↔5 (Global view must honour CAPMGMT-04's period policy), 4↔7 (Overview must honour persisted range)

---

## Epic 5 — Global Management View (Decision 5)

> Decision 5: Management needs a global, consolidated planning view across all teams/year, beyond the existing team-specific views.

### CAPMGMT-06 — Global management view: all teams × full year

**BLOCKED BY: CAPMGMT-04** (period persistence policy must be defined before this view's period behaviour is coded)

**As a** capacity planning manager, **I want** a consolidated view of all team allocations and headcount across all teams for the full year **so that** I can identify cross-team bottlenecks and resource gaps at a glance, without switching between per-team views.

**Acceptance Criteria:**

1. A new view key `'global'` is added to the `switchView()` state machine in `app.js`. A navigation button is added alongside the existing view toggle buttons (heatmap / team / overview / pipeline / allplanitems). ASSUMPTION: accessible to users with the `planner` or `admin` role — not `viewer`. Confirm with business — no "management" role exists in this app, and no new role should be created without explicit business sign-off. **[Open Question — see §OQ-5a]**

2. The view is a summary table where:
   - Rows = all active teams (from the `TEAMS` array, i.e. `u_active = true`) plus role teams from `ROLE_TEAMS`, sorted by `u_order`
   - Columns = all periods (full year), using the `periods` array from `GET /data` (sorted by `month_sequence`) — NOT `MONTHS.slice()` which is year-unaware
   - Each cell shows: available headcount FTE (from `headcount[team][monthKey]`) and total committed allocation FTE (sum of `p.ta[team][monthKey]` for all `p` where `p.pls === 'Committed'`)
   - Visual indicator for over-commitment: cell is styled with `cap-over` class (or equivalent) when committed allocation > available headcount (consistent with the existing `team` view's negative-remaining pattern)

3. PERIOD RANGE POLICY (defined by CAPMGMT-04): this view **ignores** the user's persisted period selection and always shows **all** periods. Add a label: "Showing all periods" or similar. Do NOT apply `activeMos()` or the `monthS`/`monthE` slice to this view's columns.

4. CONSTRAINT — year-aware columns: column headers must be the period `label` field (e.g. "Jan 2025", "Feb 2025") from the sorted `periods` array, not bare month names. This is required for multi-year correctness.

5. CONSTRAINT — committed allocation filter: use `p.pls === 'Committed'` to filter projects contributing to the allocation sum. SAME normalisation caveat as CAPMGMT-01: `getData` normalises empty `u_plan_status` to `'Committed'` server-side, so pending-import rows appear as Committed. Document the same tooltip.

6. CONSTRAINT — delete-on-zero: the absence of an allocation row means FTE = 0, not "unknown." A row's presence guarantees `u_fte > 0`. Do not treat absent cells as missing data.

7. 5↔7 DISAMBIGUATION: This view covers only the NEW global consolidated view. It does NOT modify the existing `overview` view, the `team` view, or the heatmap. CAPMGMT-05 covers improvements to the `overview` view — those changes must not be duplicated here.

8. ASSUMPTION: "consolidated planning view" means a headcount-vs-allocation summary grid only, not a per-initiative breakdown. If management also wants per-initiative detail in this view, the scope significantly increases. **[Open Question — see §OQ-5b]**

9. No new REST endpoint required — all data is available from `GET /data` (`headcount`, `teams`, `roleTeams`, `periods`, `projects` with `p.ta` and `p.pls`).

**ServiceNow Implementation Notes:**
- Data sources (all from the in-memory `GET /data` response):
  - `headcount` object: `headcount[teamName]['YYYY-Mon']` → available FTE
  - `teams` + `roleTeams` arrays: all active teams (sorted by `u_order` server-side)
  - `periods` array: already sorted by `month_sequence`, use `p.key` (`'YYYY-Mon'`) for map lookups and `p.label` for column headers
  - `projects` array: each `p.ta[teamName]['YYYY-Mon']` → allocated FTE; filter on `p.pls === 'Committed'`
- Committed allocation per team/month (client-side):
  ```js
  var committedByTeamMonth = {};
  projects.filter(function(p) { return p.pls === 'Committed'; }).forEach(function(p) {
    Object.keys(p.ta).forEach(function(team) {
      Object.keys(p.ta[team]).forEach(function(mk) {
        if (!committedByTeamMonth[team]) committedByTeamMonth[team] = {};
        committedByTeamMonth[team][mk] = (committedByTeamMonth[team][mk] || 0) + (p.ta[team][mk] || 0);
      });
    });
  });
  ```
- Over-commitment cell: `committedByTeamMonth[team][mk] > (headcount[team] && headcount[team][mk] || 0)` → apply `cap-over` class
- Navigation: add button alongside existing view toggles; call `switchView('global')`

**Story Points:** 8 | **Priority:** Medium | **Dependencies:** CAPMGMT-04 (period policy must be defined first)
**Coupling:** 5↔7 (scope disambiguated; does not duplicate CAPMGMT-05), 4↔5 (period range policy from AC3)

---

## Epic 6 — Parent/Child Hierarchy (Decision 6)

> Decision 6: Parent/Child initiative hierarchy is a data problem, not a tooling problem — source initiative data isn't consistently mapped, corrupting project counts and reporting.

### SPIKE-02 — Identify parent/child field on x_u4bsh_initiati_0_initiative

**As a** capacity planner and developer, **I want** to know the exact field(s) representing parent/child hierarchy on the source initiative table **so that** we can assess the scope of double-counting in local reporting and propose a defensible local handling strategy.

**Acceptance Criteria:**

1. Identify which field(s) on `x_u4bsh_initiati_0_initiative` represent the parent/child relationship (e.g. a reference field named `parent`, `u_parent`, `parent_initiative`, or similar).

2. Determine whether these fields are consistently populated: count active initiatives with a non-empty parent field vs. those without (use a Background Script in scope `x_u4bsh_capmgmt` — READ only via the existing CrossScopePrivilege).

3. Determine, for the initiatives that have Plan Items in `x_u4bsh_capmgmt_initiative`: how many child-initiative Plan Items also have a parent-initiative Plan Item in the same scope (i.e. the double-counted cases).

4. Determine whether the owning team (scope `x_u4bsh_initiati_0`, ID `c126b5741bb5a690f004dc6fe54bcb67`) can and will normalise the parent/child data in the source system, and on what timeline.

5. CONSTRAINT: this spike is READ-ONLY. No write operations to `x_u4bsh_initiati_0_initiative` (no write cross-scope privilege exists). No write operations to `x_u4bsh_capmgmt_initiative` either — this is purely investigative.

6. Deliverable: a written summary with (a) field name(s), (b) consistency percentage, (c) estimated double-counted Plan Item count today, (d) recommended local defensive strategy (one of: exclude children from counts, show children as sub-rows under parent, add a "child" badge without changing count), (e) escalation status to owning team.

**ServiceNow Implementation Notes:**
- Cross-scope READ privilege to `x_u4bsh_initiati_0_initiative` already exists in `src/fluent/generated/other/sys-scope-privilege/`
- Run as Background Script in scope `x_u4bsh_capmgmt` (must select this scope before running)
- Enumerate fields: `var gr = new GlideRecord('x_u4bsh_initiati_0_initiative'); gr.setLimit(1); gr.query(); if (gr.next()) { var fields = gr.getFields(); // iterate and look for reference fields }` — or use Schema Map in Studio
- Parent check: once field name is known, `gr.addNotNullQuery('<parent_field>'); gr.addActiveQuery(); gr.query(); gs.info('Initiatives with parent: ' + gr.getRowCount());`

**Story Points:** 2 | **Priority:** High | **Dependencies:** None (runs in parallel with SPIKE-01 and DATA-01)

---

### CAPMGMT-07 — Parent/child hierarchy: defensive counting and escalation

**BLOCKED BY: SPIKE-02**

**As a** capacity planning manager, **I want** the Total Projects count and the Global view to not double-count child initiatives alongside their parents **so that** leadership sees an accurate project count that reflects distinct initiatives, not implementation sub-items.

**Acceptance Criteria:**

1. **BLOCKED BY SPIKE-02**: the parent/child field name is unknown. All criteria below are conditional on SPIKE-02's findings.

2. CONSTRAINT: the app has **READ-ONLY** cross-scope access to `x_u4bsh_initiati_0_initiative`. This story cannot write to that table. The fix is purely defensive local handling in `capacity-handler.ts` and `app.js`.

3. Recommended defensive approach (ASSUMPTION — confirm after SPIKE-02): exclude Plan Items whose linked source initiative has a non-empty parent field from the "Total Projects" count, but still display them in all views with a visual badge or label indicating "child initiative." **[Open Question — see §OQ-6]**

4. Server-side change: in `getData` (`capacity-handler.ts`), include the parent field value in the batch-fetch of linked `x_u4bsh_initiati_0_initiative` records. Add a new key to the plan item response object, e.g. `parentInitId: <parent_initiative_sys_id or null>`. This follows the same pattern as existing overlay fields (`linkId`, `snowSize`, `softRelease`).

5. Client-side change: in `app.js`, a plan item is a "child" when `p.parentInitId` is non-null. Child plan items:
   - Are excluded from the CAPMGMT-01 Total Projects count
   - Are shown in all views with a visual badge ("child" or "↳" indicator)
   - Are NOT hidden — they remain visible for allocation tracking

6. CONSTRAINT — staleness: `propagate-initiative-changes` is INACTIVE. If a source initiative is re-parented after its Plan Item was created, the Plan Item's `parentInitId` will be stale until a planner re-saves it (triggering `sync-initiative-fields`, which would need to be extended to propagate the parent field). Add a UI note or tooltip acknowledging this limitation.

7. Escalation: an escalation task to the `x_u4bsh_initiati_0` owning team must be documented separately — the root fix is consistent parent/child data in the source system. This story only adds defensive local display logic.

8. 1↔6 coupling: once both CAPMGMT-01 and CAPMGMT-07 land, the Total Projects count is correct for both the Committed filter and the hierarchy double-count. Until both land, document which limitation remains.

**ServiceNow Implementation Notes:**
- `capacity-handler.ts` `getData`: in the linked-initiative batch fetch (`IN` query on `x_u4bsh_initiati_0_initiative`), add the parent field (name TBD from SPIKE-02) to the fields read. Add `parentInitId: linkedInit['<parent_field>'] || null` to the plan item response object.
- Client `app.js`: `var isChild = function(p) { return !!p.parentInitId; };` — use in count expression and badge render
- CAPMGMT-01 updated count: `projects.filter(function(p) { return p.pls === 'Committed' && p.ty === 'Project' && !isChild(p); }).length`
- No new REST endpoint; no ACL or BR changes; no write to `x_u4bsh_initiati_0_initiative`
- If `sync-initiative-fields` is extended to propagate the parent field: add the parent reference field read to the BR's linked-initiative query in `src/server/business-rules/sync-initiative-fields.ts`

**Story Points:** 5 (TBD after SPIKE-02) | **Priority:** Medium | **Dependencies:** SPIKE-02 (blocked)
**Coupling:** 1↔6

---

## Epic 7 — Overview Teams Column (Decision 7)

> Decision 7: Team visibility should improve on the Overview — wider Teams column, possibly more team-related information.

### CAPMGMT-05 — Improve Overview Teams column

**As a** capacity planner using the Overview, **I want** the Teams column to be wider and show which teams have allocations for each initiative in the active period range **so that** I can assess team involvement without switching to the team-specific view.

**Acceptance Criteria:**

1. ASSUMPTION: the Overview is the `'overview'` case of the `switchView()` state machine — a flat sortable table of all plan items. Confirm. **[See §OQ-7a]**

2. ASSUMPTION: "additional team-related information" means the list of teams that have at least one non-zero allocation for each Plan Item within the currently active period range (`monthS` to `monthE`). Confirm with the business — alternative interpretations (total allocated FTE, team count only, a heat indicator) are all plausible. **[Open Question — see §OQ-7b]**

3. The Teams column (or a new column immediately adjacent) is widened to comfortably display 1–4 team names without truncation. ASSUMPTION: a CSS `min-width: 160px` or similar — confirm the desired approximate column width. **[Open Question — see §OQ-7c]**

4. Teams with non-zero allocations in the active range are derived from `p.ta` client-side: `Object.keys(p.ta).filter(function(team) { return activeMos().some(function(m) { return (p.ta[team][m] || 0) > 0; }); })`. CONSTRAINT: `activeMos()` is year-unaware (known bug — `MONTHS.slice(monthS, monthE + 1)`). For this story, this limitation is acceptable — it matches all other views' current behaviour. Do NOT attempt to fix `activeMos()` in this story.

5. CONSTRAINT — delete-on-zero: `saveAllocations` deletes allocation rows when FTE ≤ 0. The presence of a key in `p.ta[team]` for a given month guarantees FTE > 0. Absent keys mean zero FTE — not missing data.

6. The column honours the period selection persisted by CAPMGMT-04 when that story lands (it reads `monthS`/`monthE`, which CAPMGMT-04 populates from localStorage). No explicit coupling code is required beyond this shared state.

7. 5↔7 DISAMBIGUATION: this story modifies the **existing** `overview` view only. It does NOT create a new view, add a new navigation element, or duplicate any feature from CAPMGMT-06 (Global view). The scope ends at the `overview` table's team column.

8. CONSTRAINT — role teams: the `u_is_role_team` boolean is available on team objects and the `roleTeams` array is returned by `getData`. If the business wants role teams visually distinguished in this column (e.g. italicised or grouped separately), that is in scope for this story. ASSUMPTION: no special role-team styling required unless confirmed. **[Open Question — see §OQ-7d]**

**ServiceNow Implementation Notes:**
- Client file: `app.js` — overview render function (search for `switchView` case `'overview'` or `'allplanitems'`)
- Team allocation data: `p.ta[teamName][monthKey]` — available in-memory from `GET /data`
- Active months: `activeMos()` → `MONTHS.slice(monthS, monthE + 1)` (year-unaware — acceptable for this story)
- Teams for a plan item: `Object.keys(p.ta).filter(team => activeMos().some(m => (p.ta[team][m]||0) > 0))`
- CSS: update the `.overview-teams` column class (or add one) with the desired `min-width`
- No server-side changes; no new REST endpoint; no ACL or BR changes

**Story Points:** 3 | **Priority:** Medium | **Dependencies:** CAPMGMT-04 (will automatically honour persisted range; no explicit dependency code required)
**Coupling:** 5↔7 (scoped to overview only, no overlap with CAPMGMT-06), 4↔7 (honours persisted period via shared monthS/monthE)

---

## Assumptions, Open Questions & Risks

### Open Questions (must be resolved before coding begins)

| ID | Decision | Question | Impact if unresolved |
|---|---|---|---|
| OQ-1 | 1 | Where exactly is "Total Projects" currently displayed in `app.js` — which view, which DOM element? | CAPMGMT-01 cannot be coded without locating the element first |
| OQ-2 | 1 | Does "Total Projects" explicitly exclude BAU, Enhancement, and Absences (i.e. only u_type = 'Project')? | Incorrect count if assumption is wrong |
| OQ-3 | 1/6 | Should propagate-initiative-changes be reactivated? Its blast radius at production data volumes is untested and the BR has `active: false` explicitly. Reactivation could silently trigger mass re-saves of Plan Items. | If not reactivated, all staleness caveats in CAPMGMT-01 and CAPMGMT-07 remain; if reactivated without testing, production data risk |
| OQ-4 | 4 | Is localStorage (single-device, single-browser) sufficient for period persistence, or is cross-device/cross-browser sync required? | If cross-device: need a user preference record in ServiceNow (admin-only write on a new preference table or sys_user_preference) — significant scope increase |
| OQ-5a | 5 | Which role(s) should see the Global management view? No "management" role exists — current options are viewer / planner / admin. | Cannot implement the navigation guard without this answer |
| OQ-5b | 5 | Should the Global view show only a headcount-vs-allocation summary grid, or also per-initiative detail (drill-down)? | Summary only = 8 pts; per-initiative detail = significantly higher |
| OQ-6 | 6 | Preferred local defensive strategy for child initiatives: (a) exclude from count + badge, (b) sub-row under parent, (c) badge only, no count change? | Determines CAPMGMT-07 implementation approach |
| OQ-7a | 7 | Confirm: "Overview" = the `'overview'` switchView case (flat sortable table). Or does it refer to a different view? | Must identify the correct view before changing CSS/render |
| OQ-7b | 7 | What "team-related information" should appear beyond team names? Options: team names only, team name + total FTE, team count only, a bar indicator. | Determines render complexity |
| OQ-7c | 7 | Desired width for the Teams column in the Overview table (approximate px or column-count)? | CSS change only — low risk, but needs confirmation |
| OQ-7d | 7 | Should role teams (BA-BusinessAnalyst, Architecture, PM) be visually distinguished in the Overview Teams column? | Minor styling change if yes |
| OQ-8 | 8 | "More allocation data still needs validation and import" — does this refer to (a) additional rows for already-imported initiatives, or (b) net-new initiatives not yet in DEV3? | If (b), DATA-01's scope expands and the Generate Plan Items script may need to be re-run first |

### Assumptions (inline in stories above, repeated here for visibility)

| ID | Story | Assumption | Consequence if wrong |
|---|---|---|---|
| A-1 | CAPMGMT-01 | "Total Projects" exists as a count element in the current SPA | Story becomes "add a count" rather than "fix a count" |
| A-2 | CAPMGMT-01 | The `getData` `u_plan_status || 'Committed'` normalisation is still present in `capacity-handler.ts` | If removed, client `p.pls` will be empty string for pending-import rows, and the filter `p.pls === 'Committed'` will under-count |
| A-3 | CAPMGMT-04 | localStorage (single-device) is sufficient for persistence | If wrong, significantly more complex (server-side user preference) |
| A-4 | CAPMGMT-06 | Global view shows summary grid only, not per-initiative breakdown | If wrong, story size increases |
| A-5 | CAPMGMT-06 | Planner and admin roles see the Global view; viewer does not | If wrong, route guard logic changes |
| A-6 | CAPMGMT-07 | Preferred strategy is exclude-from-count + badge | If sub-row strategy is preferred, render complexity increases |
| A-7 | CAPMGMT-05 | "Team information" means team names with allocations in active range | If FTE sums are required, aggregation logic is needed |
| A-8 | CAPMGMT-03 | One `x_u4bsh_capmgmt_period` record exists per calendar month (1:1) | If multiple period records per month, period lookup logic must be more specific |

### Risks

| Risk | Affected stories | Severity | Mitigation |
|---|---|---|---|
| **propagate-initiative-changes is INACTIVE**: stale Plan Item data silently undermines every metric that depends on u_plan_status (CAPMGMT-01), u_area/u_snow_status accuracy (CAPMGMT-02), and hierarchy data (CAPMGMT-07) | CAPMGMT-01, CAPMGMT-02, CAPMGMT-07 | Medium | Document limitation in each UI metric with a tooltip; raise reactivation question (OQ-3) with tech lead |
| **u_plan_status default over-counts**: getData normalises empty u_plan_status to 'Committed'; pending-import Plan Items appear committed | CAPMGMT-01, CAPMGMT-06 | Medium | Complete status import (Capmgmt Plan Status Transform) before relying on the count; document tooltip |
| **activeMos() year-unaware bug**: any feature that calls activeMos() for cross-year ranges produces wrong results | CAPMGMT-05 (team column), CAPMGMT-04 (period persistence indices) | Medium — low today, high when multi-year data arrives | CAPMGMT-04 explicitly avoids indices; CAPMGMT-05 accepts the limitation and documents it |
| **u_period migration incomplete**: legacy u_month-only allocation rows remain invisible to derive-initiative-dates | CAPMGMT-03 | High | CAPMGMT-03 hardens the forward path; backfillPlanItemDates handles legacy rows |
| **Duplicate Plan Items**: non-unique index on u_initiative means duplicates exist and no schema constraint prevents more | CAPMGMT-02 | Medium | DATA-01 counts existing duplicates; CAPMGMT-02 creates shared idempotency pattern |
| **Spike-01 finding: no allocation import mechanism exists** | CAPMGMT-03, CAPMGMT-02 | High | If no mechanism exists, CAPMGMT-03 becomes "build the allocation import pipeline from scratch" — significant scope increase; re-estimate before building |
| **Parent field not populated / owning team cannot fix** | CAPMGMT-07 | Medium | If source data is consistently unpopulated, the hierarchy bug is unmeasurable today — document and revisit when data quality improves |
| **Reactivating propagate-initiative-changes**: untested at production data volumes; could trigger mass re-saves | OQ-3 | High | Do NOT reactivate without load testing on a non-production instance first |

---

*Refine any story, resolve any open question, and I'll iterate.*
