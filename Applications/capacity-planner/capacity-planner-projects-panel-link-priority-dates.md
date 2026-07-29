---
title: "Capacity Planner — Fix Prompt: Projects panel link + priority + dates (INTV0001072)"
aliases:
  - capacity-planner-projects-panel-link-priority-dates
  - capmgmt-projects-panel-issues
area: Applications/capacity-planner
tags:
  - servicenow
  - capacity-planning
  - internal-tool
  - scoped-app
  - byoui
  - fix-prompt
  - ux
date: 2026-07-21
---

# Capacity Planner — Fix Prompt: Projects panel link + priority + dates (INTV0001072)

> Claude Code prompt from Filipa feedback (PT), 2026-07-21. Projects tab detail
> panel for "Partners Automation POs (Phase 1 – Co-Sell)", linked INTV0001072.
> Grounding: [[capacity-planner]]

## Original notes (PT)

1. Consigo ter o link para ir para a iniciativa?
2. Aqui diz que é P4 mas a iniciativa é P2.
3. O start e end date não faz match com a alocação atribuída.

## Context

Plan item linked to source initiative INTV0001072. Allocations: SALES +
BA-BusinessAnalyst, 0.5 each, Apr–Jun 2026. Panel shows P4 / START 2026-02 /
END 2026-06.

## The prompt

```markdown
# Capacity Planner — Projects tab detail panel: 3 issues (INTV0001072)

App: x_u4bsh_capmgmt. Frontend `src/client/app.js` (Projects/`projects` detail
panel renderer). Server `src/server/capacity-handler.ts` (`getData`). BRs in
`src/server/business-rules/`.

Context: viewing plan item "Partners Automation POs (Phase 1 – Co-Sell)", linked to
source initiative INTV0001072. Allocations: SALES + BA-BusinessAnalyst, 0.5 each,
Apr–Jun 2026. Panel shows P4 / START 2026-02 / END 2026-06.

## 1. Make the initiative reference a clickable link
The SNOW ref (INTV0001072, client field `snow`; the linked source sys_id is
`p.linkId` / `u_initiative`) is shown as plain text. Turn it into a link that opens
the source initiative record in a new tab:
`x_u4bsh_initiati_0_initiative.do?sys_id=${linkId}` (only when `linkId` exists;
plain text when not linked). Escape the value (see the escapeHtml work).

## 2. Priority mismatch — panel says P4, source initiative is P2
Plan-item priority `p.p` (`u_priority`) is copied from the source initiative by the
`sync-initiative-fields` BR (leading digit of `priority` via `/^(\d+)/`). The panel
shows P4 but the real initiative is P2 => the local value is STALE.
Known cause: `propagate-initiative-changes` BR is INACTIVE, so source-initiative
changes never re-sync to linked plan items — they only update on manual re-save.
- Confirm INTV0001072's current source `priority` vs stored `u_priority`.
- Decide the fix: either reactivate/repair propagation, OR (safer, per backlog
  OQ-3) show the LINKED source value live in the panel like `getData` already does
  for name/area/status (linked wins), so priority can't drift. Recommend the latter
  unless propagation is explicitly wanted. Report which and why before changing.

## 3. Start/End dates don't match the allocation span
Earliest allocation is Apr 2026 but panel START = 2026-02. Cause: `getData` maps
`st`/`en` so the LINKED initiative's dates win over the allocation-derived
`u_start`/`u_end` (st ← u_soft_planning_start_date from linked; en ← linked release
date fields). So the panel shows the initiative's planning dates, not the actual
allocation period — they diverge whenever allocations differ from the source plan.
- Confirm this is the mapping in play for INTV0001072.
- Decide which date the Projects panel SHOULD show: the allocation-derived span
  (`u_start`/`u_end`, i.e. min/max of allocated periods) or the linked planning
  dates. For "does the timeline match what's allocated?", the allocation-derived
  span is the right one — recommend showing that in this panel (or show both,
  labelled "Planned" vs "Allocated"). Report the choice before changing.

## Constraints
- No new deps, match existing vanilla-JS style; escape all data fields.
- These are partly design questions (2 & 3) — investigate, state the current
  behaviour and the recommended option, and flag what needs Filipa/product sign-off
  rather than silently changing semantics.
- `npm run build`, Update-Set commit + hard-refresh. Verify in-browser.
```

## Related

- [[capacity-planner]]
- [[capacity-planner-future-analysis]] — OQ-3 (reactivate propagation), dates
- [[capacity-planner-fix-pipeline-html-injection]] — escapeHtml helper referenced above
- [[capacity-planner-backlog-2026-07]]
