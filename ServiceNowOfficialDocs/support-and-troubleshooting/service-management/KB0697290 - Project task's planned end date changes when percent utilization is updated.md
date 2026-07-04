---
title: "Project task's planned end date changes when percent utilization is updated"
aliases:
  - KB0697290
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0697290
kb_number: KB0697290
last_modified: 2024-04-07
---

## Project task's planned end date changes when percent utilization is updated

  

### Issue

# Symptoms

* * *

Planned end date changes when modifying percent complete on a Project Task.

# Release

* * *

Kingston Patch 3a, Kingston Patch 4, Kingston Patch 6, Kingston Patch 7

# Cause

* * *

This recalculation is expected behavior.

# Resolution

* * *

The Actual Start Date is set when a Business Rule changes the state from Open to Work in Progress.  
  
Planned End Date = Actual Start Date + Duration   
  
This is why a change is seen when percent is updated, because when the user updates percent, the project task moves from "Open" to "Work in Progress", causing "Actual Start Date" to be populated.  
  
Once "Actual Start Date" is populated, then the calculation happens which says, "Take the Actual Start Date, add the duration, and take that value and set it as 'Planned end date'".  
  
\--   
  
If an immutable point of reference is needed, the user can utilize the Original Start Date and Original End Date fields.  
  
\--  
  
If the user does not want the OOB calculation to take place at all, there is a way to accomplish that (though it is unsupported). The user can add the "pm\_project\_task" table as an entry to the "planned\_task\_recalculation\_exclusions" table. This way, whenever the user updates a percentage on a project task, the expected recalculation will not happen.   
  
Please note that making this change could cause other potential issues with natural recalculation of projects/tasks.
