---
title: "Capacity Planner — Fix Prompt: /data & /available 500 (self-referential scope dependency)"
aliases:
  - capacity-planner-fix-500-scope-dependency
  - capmgmt-500-scope-dependency
area: Applications/capacity-planner
tags:
  - servicenow
  - capacity-planning
  - internal-tool
  - scoped-app
  - cross-scope
  - bug-fix
  - fix-prompt
date: 2026-07-21
---

# Capacity Planner — Fix Prompt: /data & /available 500 (self-referential scope dependency)

> Claude Code prompt built from dev3 (unit4dev1) debugging on 2026-07-20/21.
> Grounding: [[capacity-planner]]

## Context / symptom

Both `GET /api/x_u4bsh_capmgmt/capacity/data` and `.../available` returned **500**.
UI showed 0 projects / 0 KPIs. Console: `Load failed: 500` at
`loadFromServiceNow` (app.js:2330) and `loadAvailable` (app.js:2370). The
`NODE_ENV` console error is unrelated injected-script noise.

500 response body revealed the real cause:

```json
{
  "error": {
    "message": "Error: Error: App \"x_u4bsh_capmgmt\" does not declare a dependency on \"x_u4bsh_capmgmt\". (sys_ws_operation.19ff98c7b60f4beb9f1f5f5a1aa80ce2.operation_script; line 9)",
    "detail": ""
  },
  "status": "failure"
}
```

Self-referential scope dependency — the app is told it must depend on itself to
run its own REST script. Almost always a cross-scope privilege (or generated
scope sys_id) pointing at `x_u4bsh_capmgmt` instead of the external initiative
scope.

## The prompt

```markdown
# Capacity Planner — /data & /available 500: self-referential scope dependency

App: x_u4bsh_capmgmt. Fluent cross-scope decls `src/fluent/acls/cross-scope.now.ts`,
generated scope sys_ids `src/fluent/generated/keys.ts`, handler
`src/server/capacity-handler.ts`, REST def `src/fluent/restapi/capacity-api.now.ts`.

## Exact error (from the 500 body)
    App "x_u4bsh_capmgmt" does not declare a dependency on "x_u4bsh_capmgmt".
    (sys_ws_operation.19ff98c7b60f4beb9f1f5f5a1aa80ce2.operation_script; line 9)

- sys_ws_operation `19ff98c7b60f4beb9f1f5f5a1aa80ce2` is the /data GET operation.
- Line 9 is the first cross-scope resource access in the generated op script.
- Both /data and /available 500 (app.js:2330 loadFromServiceNow, 2370 loadAvailable).

=> Something the handler touches resolves to scope `x_u4bsh_capmgmt` itself but is
being accessed AS IF cross-scope, so the runtime demands a self-dependency (which
can't exist) and throws. NOT a data/null bug.

## Root cause to find (most → least likely)
1. **Wrong target scope on a CrossScopePrivilege.** In `cross-scope.now.ts` the
   privilege for the initiative table must target scope `x_u4bsh_initiati_0`
   (sys_id c126b5741bb5a690f004dc6fe54bcb67), NOT `x_u4bsh_capmgmt`. Check every
   CrossScopePrivilege — any whose target scope == own scope is the bug.
2. **Bad scope sys_id in `generated/keys.ts`.** A placeholder/duplicated sys_id
   (this repo already has known placeholder-sys_id issues) may make the initiative
   scope key resolve to the app's own scope. Compare the initiative scope sys_id
   used against c126b5741bb5a690f004dc6fe54bcb67.
3. **Handler queries the wrong table name.** Confirm `getData`/`getAvailableInitiatives`
   query `x_u4bsh_initiati_0_initiative` (external), not a same-scope alias that
   got renamed. A table whose sys_scope is wrong on the instance triggers this too.
4. **Stale/duplicate `sys_scope_privilege` rows on dev3** from a prior deploy —
   check the instance for a privilege row with source AND target = x_u4bsh_capmgmt
   and delete it.
5. Diff against last known-good deploy — this broke after a recent push (pipeline
   fix / handler edit). Find what changed the scope wiring.

## Fix
Correct the target scope / sys_id so the cross-scope access points at
`x_u4bsh_initiati_0` (and global for cmdb_ci_business_app), remove any
self-referential privilege, rebuild.

## Constraints
- No new deps. Match existing Fluent style.
- Report: which decl/sys_id was wrong, the diff, and any instance record deleted.
- `npm run build`, Update-Set commit + hard-refresh. Then confirm `/data` returns
  200 with projects in the browser — don't claim fixed from code alone.
```

## Related

- [[capacity-planner]]
- [[capacity-planner-future-analysis]]
- [[capacity-planner-backlog-2026-07]]
