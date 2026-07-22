---
title: "Capacity Planner — Fix Prompt: Projects panel Start/End don't match allocation"
aliases:
  - capacity-planner-fix-dates-vs-allocation
  - capmgmt-dates-vs-allocation
area: Applications/capacity-planner
tags:
  - servicenow
  - capacity-planning
  - internal-tool
  - scoped-app
  - rest-api
  - business-rules
  - bug-fix
  - fix-prompt
date: 2026-07-21
---

# Capacity Planner — Fix Prompt: Projects panel Start/End don't match allocation

> Claude Code prompt, 2026-07-21. Source repo not on the doc machine — apply in
> the real `capacitymanagementoverview/` repo.
> Grounding: [[capacity-planner]]

## The issue (validated)

INTV0001072: allocations are Apr–Jun 2026, but the Projects panel shows
START 2026-02 / END 2026-06. The Feb start does NOT come from the allocation
(earliest allocation is Apr) — it comes from the LINKED initiative's planning dates.

Not a BR bug and not a data-fix script. The `derive-initiative-dates` BR already
computes `u_start`/`u_end` correctly as min/max of the allocated periods. The
mismatch is in the REST handler `getData` (`capacity-handler.ts`): it maps the
client fields `st`/`en` so the linked initiative's planning dates WIN over the
allocation-derived `u_start`/`u_end`:

- `st` ← `u_start` OR `u_soft_planning_start_date` (linked) — **linked wins**
- `en` ← `u_end` OR `u_release_date_month` / `u_hard_planning_release_date` /
  `u_release_date` (linked) — **linked wins**

So a linked plan item always shows the source's planning window, never the actual
allocation span.

## The prompt

```markdown
# Capacity Planner — Projects panel Start/End show planning dates, not allocation span

App: x_u4bsh_capmgmt. REST handler `src/server/capacity-handler.ts` (`getData`).
BR `src/server/business-rules/derive-initiative-dates.ts` (already derives u_start/u_end
as min/max of allocated periods — leave it working). Frontend `src/client/app.js`
(Projects detail panel renderer).

## Issue
For a LINKED plan item, `getData` maps `st`/`en` so the source initiative's planning
dates win over the allocation-derived `u_start`/`u_end`:
  st = u_start || <linked u_soft_planning_start_date>
  en = u_end   || <linked u_release_date_month || u_hard_planning_release_date || u_release_date>
Result: the panel shows the source planning window (e.g. Feb–Jun), not what's actually
allocated (Apr–Jun). Confirmed on INTV0001072.

## Fix (primary — recommended)
Flip the precedence so the allocation-derived, system-owned dates win, and the linked
planning dates are only a fallback when there are no allocations yet:
  st = u_start || <linked u_soft_planning_start_date>   // u_start already derived by BR
  en = u_end   || <linked release-date fallbacks>
i.e. keep the SAME fallback chain, just prefer `u_start`/`u_end` first.
- When the plan item has no allocations, `u_start`/`u_end` are blank → fall back to the
  linked planning dates (unchanged behaviour for un-allocated items).
- Do this in `getData` only; don't touch the deny-write ACL on u_start/u_end or the BR.

## Also verify (secondary — the derivation can be stale)
`derive-initiative-dates` only counts allocations that have a `u_period` reference; bare
`u_month`-only rows are ignored (known migration debt). Confirm INTV0001072's allocations
actually have `u_period` set so `u_start`/`u_end` are correct (Apr / Jun). If some are
bare-month only, that's why a date could still look off after the flip — see the
period-migration known issue. Report if any allocations lack u_period.

## Alternative (only if the business wants both)
Instead of flipping, show BOTH in the panel, labelled "Planned" (linked planning dates)
and "Allocated" (u_start/u_end). This needs a small UI change in app.js and a new field
in the getData response. Recommend the flip unless product asks for both — don't build
both without sign-off.

## Constraints
- No new deps, match existing style; escape any data fields rendered to innerHTML.
- This changes what the dates MEAN in the panel — state the choice made and flag it for
  Filipa/product sign-off; don't silently change semantics beyond the flip.
- npm run build, Update-Set commit + hard-refresh. Verify INTV0001072 shows START 2026-04
  (matching its earliest allocation), and an un-allocated linked item still shows its
  planning dates. Don't claim fixed from code alone.
```

## Related

- [[capacity-planner]] — getData st/en mapping, derive-initiative-dates BR, period-migration known issue
- [[capacity-planner-projects-panel-link-priority-dates]] — original 3-point panel feedback (this is point 3)
- [[capacity-planner-set-start-and-end-date-to-plan-items]] — the u_start/u_end backfill fix script
- [[capacity-planner-future-analysis]] — dates / allocation open questions
