---
title: "Incorrect Overdue Count and State in Journeys After Scheduled Script Execution"
aliases:
  - KB2640007
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2640007
kb_number: KB2640007
last_modified: 2026-01-03
---

## Incorrect Overdue Count and State in Journeys After Scheduled Script Execution

  

### Issue

When the scheduled script “Update journey progress with count for overdue tasks” runs, the overdue count and state for journeys are incorrect on both the Journey page and list view.  
The issue occurs with the out-of-box (OOB) version of the script, even on the latest Journey Designer plugin, and impacts task visibility and status accuracy.

### Release

Any Release

### Cause

The scheduled job does not trigger the expected flow correctly, and the system admin user lacked access to certain lifecycle event cases and HR tasks.

### Resolution

-   Override the getAllJourneyInfo function in the non-SNC script include to call `updateJourneyLeProgress` before the SNC method, then return the result.
-   Move the code to the correct script include to ensure the workaround works as intended.
-   Problem record PRB1915543 tracks this issue and is scheduled for a permanent fix in Journey Designer v7.3 (December 2025).
