---
title: "Prevent loop-based workflows with timers from hitting maximum activity count"
aliases:
  - KB0662341
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0662341
kb_number: KB0662341
last_modified: 2025-11-19
---

## Prevent loop-based workflows with timers from hitting maximum activity count

  

### Issue

A loop in a workflow occasionally fails to complete, and the workflow is canceled after a certain number of iterations. Why should a looping design with a timer activity be avoided? 

![workflow timer loop design](sys_attachment.do?sys_id=13735271935db2d0f2167de86cba1032)

### Release

All

### Cause

Workflows have a maximum activity count (default 100). When this limit is reached, the workflow is automatically canceled.

### Resolution

The maximum activity count can be increased in the workflow properties under the Activities tab. However, this looping design should generally be avoided. Increasing the activity limit only masks the underlying issue and can create additional problems:

-   Scheduler impact: Repeated loop executions can overwhelm the scheduler if many workflows follow this pattern.
-   Excessive data growth: Continuous looping generates large amounts of data in the wf\_history and wf\_transition\_history tables, especially when multiple workflows run for extended periods.
-   Design flaw: The workflow loops because it does not know when to proceed. This pattern often appears when a REST call is waiting for a specific response before allowing the workflow to continue.

### Recommended approach

Instead of looping with a timer activity:

-   Use a Wait for condition activity to pause the workflow.
-   Have an external REST (Table API) call update the record the workflow is running against. This update should satisfy the condition and allow the workflow to proceed naturally.

### If an external REST call is not possible

Implement a scheduled job that periodically performs the REST call, retrieves the needed response, and updates _all_ records where workflows are waiting. This approach avoids continuous looping while ensuring workflows progress efficiently.

### Related Links

When a workflow reaches the maximum number of allowed activity executions, it stops. The default limit is 100. Set this value to at least 10% higher than the total number of activity executions you expect the workflow to perform.
