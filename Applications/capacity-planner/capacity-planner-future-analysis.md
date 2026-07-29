---
title: Capacity Planner — Open Business Questions (Future Analysis)
aliases:
  - capacity-planner-future-analysis
  - capmgmt-future-analysis
area: Applications/capacity-planner
tags:
  - servicenow
  - capacity-planning
  - internal-tool
  - scoped-app
  - open-questions
  - business-analysis
date: 2026-07-13
source: Repo FUTURE_ANALYSIS.md (generated during CAPMGMT-08/09 implementation, 2026-07-13)
---

# Capacity Planner — Open Business Questions (Future Analysis)

> Source: `FUTURE_ANALYSIS.md` in repo root (`capacitymanagementoverview/`). That file is the canonical source; this note is a searchable vault mirror.
> Grounding: [[capacity-planner]], [[capacity-planner-backlog-2026-07]]

Questions that arose during implementation and need product/business sign-off before they can be acted on. Each entry notes the context, the default assumption used in the current build, and the risk if the assumption is wrong.

---

## CAPMGMT-08 / CAPMGMT-09 — By Team view & Area sort

### 1. Should "All Projects" and "All Teams" eventually consolidate into one tile?

**Context:** The By Team tab currently has three tile categories:
- "All Projects" (existing stub, placeholder, not yet backed by real logic)
- Per-team tiles (one per active team record)
- "All Teams" (new synthetic tile — CAPMGMT-08)

They are currently two distinct code paths with no shared logic.

**Current assumption:** They remain separate and serve different purposes ("All Projects" = cross-team project list; "All Teams" = stacked per-team breakdowns).

**Risk if wrong:** UI becomes cluttered with overlapping concepts; users are confused about which to click.

---

### 2. Is the stacked-sections UX the right interpretation of "divided per team"?

**Context:** Clicking "All Teams" currently stacks every team's table vertically (one full per-team section per team, in u_order sequence). An alternative would be a single flat table with an extra "Team" column grouping rows.

**Current assumption:** Stacked sections is acceptable.

**Risk if wrong:** The stacked view is long and hard to scan; a flat grouped table may be more usable, but would require a new table renderer.

---

### 3. Is multi-team project duplication acceptable?

**Context:** A plan item with non-zero allocations to N teams appears N times in the "All Teams" view. There is no "primary team" field on the initiative table.

**Current assumption:** Duplication is expected and acceptable — it reflects that the project genuinely spans multiple teams.

**Risk if wrong:** Users mistake the repeated rows for duplicate plan items, or total-FTE figures look inflated.

---

### 4. Should the "All Teams" tile show any aggregate stat?

**Context:** The tile currently shows the label "All Teams" and a total project count. It does not show any blended utilisation or free-FTE figure — that would duplicate what CAPMGMT-06 is meant to do properly.

**Current assumption:** Label + count only. No blended stat.

**Risk if wrong:** The tile looks bare; or leadership expects a headline number there.

---

### 5. Should AREA sorting apply to both the Overview table and the per-team table, or only one?

**Current assumption:** Both tables are in scope for Area sort (CAPMGMT-09 implemented both).

**Risk if wrong:** Sorting in the per-team table may be unexpected or confusing if team sections are already implicitly grouped.

---

### 6. Where should blank Area values land when sorting?

**Context:** `u_area` is a `dropdown_with_none` field — blank is a valid, expected value. The current implementation places blank Area values at the **end** of the list in both ascending and descending sort directions.

**Current assumption:** Blanks always sort to the end (never to the top), regardless of sort direction.

**Risk if wrong:** Users may expect blanks to sort to the top on descending (the "unknown first" convention).

---

## Backlog open questions (from capacity-planner-backlog-2026-07.md)

The following were captured during BA/sprint planning and remain unresolved. Full context lives in [[capacity-planner-backlog-2026-07]].

| ID | Story | Question | Status |
|---|---|---|---|
| OQ-1 | CAPMGMT-01 | Where exactly is "Total Projects" displayed in app.js? | ✅ Resolved — `renderOverview()` KPI bar |
| OQ-2 | CAPMGMT-01 | Does "Total Projects" explicitly exclude BAU, Enhancement, and Absences? | Open |
| OQ-3 | CAPMGMT-01/07 | Should propagate-initiative-changes BR be reactivated? | Open |
| OQ-4 | CAPMGMT-04 | Is localStorage (single-device) sufficient for period persistence? | Open |
| OQ-5a | CAPMGMT-06 | Which role(s) should see the Global management view? | Open |
| OQ-5b | CAPMGMT-06 | Should the Global view show only a headcount-vs-allocation summary grid, or also per-initiative detail? | Open |
| OQ-6 | CAPMGMT-07 | Preferred local defensive strategy for child initiatives? | Open |
| OQ-7a | CAPMGMT-05 | Confirm "Overview" = the 'overview' switchView case | ✅ Resolved — confirmed |
| OQ-7b | CAPMGMT-05 | What "team-related information" beyond team names should appear in the Overview Teams column? | Open |
| OQ-7c | CAPMGMT-05 | Desired width for the Teams column? | Defaulted to min-width:180px |
| OQ-7d | CAPMGMT-05 | Should role teams be visually distinguished in the Overview Teams column? | Open |
| OQ-8 | DATA-01 | Does "more allocation data" refer to additional rows or net-new initiatives? | Open |
