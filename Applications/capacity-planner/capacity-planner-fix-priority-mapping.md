---
title: "Capacity Planner — Fix Prompt: priority mapping inverted in sync-initiative-fields (P2 → P4)"
aliases:
  - capacity-planner-fix-priority-mapping
  - capmgmt-priority-mapping-bug
area: Applications/capacity-planner
tags:
  - servicenow
  - capacity-planning
  - internal-tool
  - scoped-app
  - business-rules
  - bug-fix
  - fix-prompt
date: 2026-07-21
---

# Capacity Planner — Fix Prompt: priority mapping inverted in sync-initiative-fields (P2 → P4)

> Claude Code prompt, 2026-07-21. Source repo not on the doc machine — apply in
> the real `capacitymanagementoverview/` repo.
> Grounding: [[capacity-planner]], [[generate-capacity-plan-items]]

## The bug (validated)

The source `priority` field on `x_u4bsh_initiati_0_initiative` uses a REVERSED
stored-value-vs-label scale (proof in the bulk script's `PRIORITY_MAP`,
[[generate-capacity-plan-items]]):

| stored value | label | target |
|---|---|---|
| `5` | 1 - Exceptional | P1 |
| `4` | 2 - High | P2 |
| `3` | 3 - Medium | P3 |
| `2` | 4 - Low | P4 |
| `1` | 5 - Minimal | P4 |

The live `sync-initiative-fields` BR uses a naive leading-digit regex `/^(\d+)/`
on the stored value. A "2 - High" (P2) initiative has stored value `4` → regex
returns `4` → `u_priority = '4'` = **P4**. That is the observed P2→P4 bug.

The regex can't work: the stored scale is inverted, and P5 ("5 - Minimal") must
collapse to P4 (target has no P5). Only the explicit crosswalk handles both.

## The prompt

```markdown
# Capacity Planner — sync-initiative-fields sets P2 initiatives to P4 (priority map inverted)

App: x_u4bsh_capmgmt. BR server logic `src/server/business-rules/sync-initiative-fields.ts`
(Fluent def `src/fluent/business-rules/*.now.ts`). Bulk script that already has the
correct crosswalk: the Background Script generating plan items (PRIORITY_MAP).

## Bug
`sync-initiative-fields` copies source `priority` → `u_priority` using a leading-digit
regex `/^(\d+)/`. The source `x_u4bsh_initiati_0_initiative.priority` STORED value is
inverted vs its label:
  stored '5' = "1 - Exceptional" = P1
  stored '4' = "2 - High"        = P2
  stored '3' = "3 - Medium"      = P3
  stored '2' = "4 - Low"         = P4
  stored '1' = "5 - Minimal"     = P4
So a P2 ("2 - High", stored '4') initiative → regex returns 4 → u_priority = P4. Wrong.
The two lowest source ranks must collapse to P4 (target has no P5), which a regex
also can't express.

## Fix
Replace the regex with the explicit crosswalk (same one the bulk generate script
uses — keep them identical):

    // Source stored priority scale is INVERTED vs label; two lowest ranks -> P4.
    var PRIORITY_MAP = { '5': '1', '4': '2', '3': '3', '2': '4', '1': '4' };
    var src = String(sourceGR.getValue('priority') || '');   // STORED value, not display
    var mapped = PRIORITY_MAP[src];
    if (mapped) current.setValue('u_priority', mapped);       // unmapped -> leave existing, don't blank

- Confirm the BR reads the STORED value (`getValue('priority')`), not the display value.
- Do NOT blank `u_priority` when the source value is unmapped/empty — skip, matching the
  BR's "never blank existing local data" rule.
- De-duplicate: if practical, export one shared PRIORITY_MAP constant used by BOTH
  `sync-initiative-fields` and the bulk generate script so they can't drift again.
  (ponytail: if there's no shared module, just copy the same literal into both and add
  a comment cross-referencing — don't build a config table for 5 entries.)

## Verify / caveats
- PRIORITY_MAP is still marked "not business-confirmed" in the bulk script. This fix makes
  P2→P2; confirm with the business that the two-lowest-ranks→P4 collapse is intended.
- After deploy, re-sync affected plan items (open+save, or the resync background script)
  and check INTV0001072 shows P2, not P4.

## Constraints
- No new deps. Match existing BR style.
- Report: the exact before/after of the mapping line and which files changed.
- npm run build, Update-Set commit + hard-refresh. Verify a known P2 initiative's
  linked plan item reads P2 in the Projects panel — don't claim fixed from code alone.
```

## Related

- [[capacity-planner]] — sync-initiative-fields BR, field mapping table
- [[generate-capacity-plan-items]] — source of the correct PRIORITY_MAP crosswalk
- [[capacity-planner-projects-panel-link-priority-dates]] — where the P2→P4 symptom surfaced
- [[capacity-planner-future-analysis]] — OQ-3 (propagation), related sync questions
