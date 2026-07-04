---
title: "Assessment instances are not moving to Canceled"
aliases:
  - KB0676810
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0676810
kb_number: KB0676810
last_modified: 2024-04-07
---

## Assessment instances are not moving to Canceled

  

### Issue

Assessment Instances are not being moved to Canceled state after their due date has passed.

### Release

All releases.

### Cause

The Schedule Job **Cancel Expired Assessments** only runs every 30 days.

### Resolution

The Out of Box Schedule Job called **Cancel Expired Assessments** runs every 30 days. It goes through the list of assessment instances and it moves every instance that has a due date before the date the job runs to the Cancelled state.

This runs every 30 days. This is why you may see assessment instances for which the due date has passed but it has not been cancelled.  
  
To adjust the frequency in which this job runs, navigate to the Schedule Job and change the "Repeat" to something less than 30 days.
