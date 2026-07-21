---
title: "Capacity Planner — Fix Prompt: Pipeline lanes hidden (unescaped HTML injection)"
aliases:
  - capacity-planner-fix-pipeline-html-injection
  - capmgmt-pipeline-html-injection
area: Applications/capacity-planner
tags:
  - servicenow
  - capacity-planning
  - internal-tool
  - scoped-app
  - byoui
  - bug-fix
  - fix-prompt
  - security
date: 2026-07-21
---

# Capacity Planner — Fix Prompt: Pipeline lanes hidden (unescaped HTML injection)

> Claude Code prompt built from dev3 (unit4dev1) debugging on 2026-07-20/21.
> This is the **confirmed root cause** of the earlier "Pipeline missing lanes
> under All SNOW/All areas" symptom — not a loop/layout bug.
> Grounding: [[capacity-planner]]

## Root cause (confirmed)

`renderPipeline()` in `src/client/app.js` builds each lane's HTML by interpolating
record fields directly into a template string (e.g.
`<div class="pl-card-name">${p.n}</div>`) then assigns the full board via
`innerHTML` — with **no HTML-escaping**.

A real project is named `Swiper js modification to aid with <style> element tags`.
The unescaped `<style>` is parsed as a real tag; with no matching `</style>`, the
browser swallows everything after it as inert stylesheet text — the rest of the
cards AND all subsequent lane columns (Screening, Qualified, Pending, New, …), so
they never enter the DOM. Only lanes built before that card render.

**Reproduction:** filtering to any single area that EXCLUDES that project (e.g.
IT, Finance) → all 5–6 lanes render. "All areas" (includes it) → board collapses
to a single visible lane.

## The prompt

```markdown
# Capacity Planner — Pipeline lanes hidden: unescaped HTML injection in render (dev3)

App: x_u4bsh_capmgmt. UI page `x_u4bsh_capmgmt_planner.do`. Frontend `src/client/app.js`.

## Root cause (confirmed)
`renderPipeline()` builds Kanban lane HTML by interpolating record fields straight
into a template string, then assigns it via `innerHTML` — with NO escaping, e.g.:

    <div class="pl-card-name">${p.n}</div>

A real project is named:  `Swiper js modification to aid with <style> element tags`
The unescaped `<style>` is parsed as a real tag. With no matching `</style>`, the
browser swallows everything after it as inert stylesheet text — the rest of the
cards AND all later lanes (Screening, Qualified, Pending, New, …). Only lanes
built before that card render.

Reproduction: filter to any single area that EXCLUDES that project (e.g. IT,
Finance) → all 5–6 lanes render. "All areas" (includes it) → board collapses to
one lane. This is the same "Pipeline missing lanes under All SNOW/All areas"
symptom reported earlier — not a loop/layout bug, an HTML-injection bug.

## Fix
1. Add an `escapeHtml()` helper (escape `& < > " '`). Vanilla JS, no deps.
2. Wrap EVERY record-derived string interpolated into an `innerHTML` template with
   it — start with `renderPipeline()`: project name `p.n`, area `p.a`, team names,
   size `p.s`, status labels, comments, review comment `p.rc`, group `p.ig`, etc.
3. Sweep the other render functions that share this pattern and fix them too:
   `renderOverview`, `renderAllPlanItems`, the Heatmap, By Team (`_teamDetailHTML`,
   `renderAllTeams`), By Project, and the Projects detail panel. Any `${...}` that
   comes from record data must go through `escapeHtml()`.
   - grep `innerHTML` and `` ${ `` to find them; treat all record fields as untrusted.
   - Attribute contexts (`title="${...}"`, `value="${...}"`) need escaping too —
     the same helper covering quotes handles it.

## Constraints
- No new deps, match existing vanilla-JS style.
- Don't escape hardcoded static markup — only data-supplied fields.
- Report: which functions/fields were wrapped.
- `npm run build`, Update-Set commit + hard-refresh. Verify in-browser: "All areas"
  now shows all lanes, and the "Swiper js … <style>" project renders as literal
  text. Don't claim fixed from code alone.
```

## Related

- [[capacity-planner]]
- [[capacity-planner-fix-500-scope-dependency]]
- [[capacity-planner-future-analysis]]
- [[capacity-planner-backlog-2026-07]]
