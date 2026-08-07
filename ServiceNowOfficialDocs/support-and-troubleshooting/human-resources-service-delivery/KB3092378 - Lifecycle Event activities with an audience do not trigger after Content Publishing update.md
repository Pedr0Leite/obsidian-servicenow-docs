---
title: "Lifecycle Event activities with an audience do not trigger after Content Publishing update "
aliases:
  - KB3092378
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3092378
kb_number: KB3092378
last_modified: 2026-06-16
---

## Lifecycle Event activities with an audience do not trigger after Content Publishing update

  

### Issue

Lifecycle Event activities that have an audience set do not trigger for employees who match the audience criteria.

### Symptoms

-   The target employees correctly appear when the HR condition is opened, and the activity set is not skipped (the subject person matches the user criteria).
-   However, when a LE case is created, the activity set advances directly to the Finished stage without launching the activities defined inside it.
-   Removing the audience field from an activity allows that activity to trigger normally.
-   The `Launch Activities` Run Script step in the `HR Activity Launcher` workflow leaves `workflow.scratchpad.activitiesLaunched = false` in all contexts.
-   The onset is sudden — activities worked until the Content Publishing application was updated.

In the `Evaluate Audience` subflow context (`sys_flow_context`), the following error is logged in the Flow log:

```
com.snc.process_flow.exception.OpException: Error: Cannot find function isPerfStatsEnabled in object [object Object].
... at com.snc.process_flow.operation.script.ScriptOperationBase.handleScriptResult(...)
```

thrown from the Flow Action "Evaluate Audience" - script step:

```
outputs.result = new sn_hr_le.hr_ActivitySet().evaluateAudience(inputs.audience, inputs.targetUserId, inputs.caseId);
```

### Release

All

### Cause

The `sn_cd.cd_Utils` Script Include had been customised against an older version and does not contain the `isPerfStatsEnabled()` function.

When the Content Publishing application is updated, a newer version of `cd_Audience.isUserInAudience()` script include is delivered which calls:

```
// Check if performance stats are enabled (cached)
var perfEnabled = this.cd_Utils.isPerfStatsEnabled();
```

Because the customised `cd_Utils` on the instance is "skipped/protected" and was never updated to the latest store version, it lacks `isPerfStatsEnabled()`. The call therefore fails.

Call chain:

1.  `hr_ActivitySet.evaluateAudience(audience, targetUserId, caseId)`
2.  → `sn_cd.cd_Audience().isUserInAudience()`
3.  → `this.cd_Utils.isPerfStatsEnabled()` → "Cannot find function isPerfStatsEnabled in object \[object Object\]"

The `Evaluate Audience` subflow throws, so `evaluateAudience()` / `launchActivities()` return `false`, the audience cannot be evaluated, and the activity set moves straight to Finished without launching its activities. This is why removing the audience field (which bypasses audience evaluation) lets the activity trigger.

### Resolution

Restore the customised `sn_cd.cd_Utils` Script Include to the latest store version — the version delivered with the updated Content Publishing application, which contains the `isPerfStatsEnabled()` function.

1.  Open the `sn_cd.cd_Utils` Script Include (`sys_script_include`) on the affected instance.
2.  Revert the customisation so it matches the latest store/base-system version (e.g. via Revert to Base System / reapplying the skipped store update), confirming the restored version contains `isPerfStatsEnabled()`.
3.  Re-run the affected lifecycle event and confirm the `Evaluate Audience` subflow no longer errors and the activities launch for employees who match the audience criteria.

> Note: Customising store-app Script Includes such as `cd_Utils` causes the customised version to be retained ("skipped") during store-app updates, which can break newer code that depends on functions added in the latest version. Where possible, avoid directly customising store Script Includes, or re-validate skipped customisations after each store-app update.
