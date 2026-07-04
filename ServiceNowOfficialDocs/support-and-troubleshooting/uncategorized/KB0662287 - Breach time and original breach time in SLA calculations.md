---
title: "Breach time and original breach time in SLA calculations"
aliases:
  - KB0662287
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0662287
kb_number: KB0662287
last_modified: 2026-06-29
---

## Breach time and original breach time in SLA calculations

  

### Issue

The Original Breach Time and Planned End Time fields on a task SLA record show different values.

### Release

All Supported Releases

### Cause

When an SLA is attached to a task, the Original Breach Time is calculated at that moment. If the task moves to _Pending_, the SLA may pause. The time saved during the pause is not reflected in the Original Breach Time because that field captures the end time as it was first calculated. The Planned End Time is updated to account for the pause, so it reflects the adjusted end time.

### Resolution

**Original Breach Time** is the SLA end time calculated when the SLA first attaches to the task. It does not change, even if the SLA is later paused.

**Planned End Time** adds the pause duration to the Original Breach Time and returns the actual adjusted end time based on one of the following:

-   The business pause duration, for task SLAs with a specified schedule 
-   The pause duration, for task SLAs with no schedule 

When the task moves to _Pending_ and the SLA pauses, the **Planned End Time** updates to show the new expected breach time. The **Original Breach Time** remains unchanged as a reference to the initial calculation.

### Related Links

[Task SLA table](https://www.servicenow.com/docs/r/it-service-management/service-level-management/r_TaskSLATable.html "Task SLA table")
