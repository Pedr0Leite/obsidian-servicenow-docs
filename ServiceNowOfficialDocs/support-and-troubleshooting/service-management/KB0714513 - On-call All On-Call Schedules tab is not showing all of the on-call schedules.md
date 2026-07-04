---
title: "On-call \"All On-Call Schedules\" tab is not showing all of the on-call schedules"
aliases:
  - KB0714513
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0714513
kb_number: KB0714513
last_modified: 2024-04-07
---

## On-call "All On-Call Schedules" tab is not showing all of the on-call schedules

  

### Issue

# Symptoms

* * *

When viewing the "All On-call Schedules" tab on the on-call calendar page, not all of the schedules are seen

# Release

* * *

Kingston Patch 7

# Cause

* * *

On OOB default is set to display 20 schedules but if the user has greater than or less than 19 schedules pinned, it will not load

# Resolution

* * *

For now, users should pin either greater than or less than but not equal to 19 schedules

# Additional Information

* * *

This issue is being addressed in PRB1291076
