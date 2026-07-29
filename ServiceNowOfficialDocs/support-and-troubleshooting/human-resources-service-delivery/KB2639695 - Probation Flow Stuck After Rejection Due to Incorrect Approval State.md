---
title: "Probation Flow Stuck After Rejection Due to Incorrect Approval State"
aliases:
  - KB2639695
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2639695
kb_number: KB2639695
last_modified: 2026-01-03
---

## Probation Flow Stuck After Rejection Due to Incorrect Approval State

  

### Issue

The probation flow intermittently fails when the approval state is set to "Not Yet Requested" after rejection, causing the flow to get stuck and blocking case resolution.  
Expected behavior: approval state should update to "Rejected" upon rejection so the flow continues.

### Release

Any Release

### Cause

The "Wait for condition" step does not re-trigger in some scenarios, especially when time-based conditions are used, which is not recommended per platform guidelines.

### Resolution

-   Remove time-based conditions from the "Wait for condition" logic.
-   Review and adjust any custom ACLs or query business rules that might affect flow execution.
-   Ensure approval state updates correctly to "Rejected" after rejection.
