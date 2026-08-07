---
title: "Incident is closed but does not show this in the activity log or audit history. As a result, SLAs are not working as expected."
aliases:
  - KB0695960
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695960
kb_number: KB0695960
last_modified: 2024-04-07
---

## Incident is closed but does not show this in the activity log or audit history. As a result, SLAs are not working as expected.

  

### Issue

# Symptoms

* * *

The incident record is closed, but this state transition is not showing in the activity log or audit history. As a result, relevant SLAs are not transitioning stage and are still showing as "Paused" (when they should be "Completed")

# Release

* * *

Jakarta Patch 7

# Cause

* * *

Two _after_ Business Rules with the name execution Order are why this intermittent behavior is happening (depending on which of the two runs first).

# Resolution

* * *

The user has the following _after_ Business Rules running:  
  

-   incident autoclose
-   Create Problem when state is Resolved

  
Both of these _after_ Business Rules have an execution Order of 100. This is the issue, and why this behavior is intermittent.  
  
Looking at INC0010000, the incident was moved to a state of "Resolved" at 2018-07-13 22:11:47 by James.  
  
Similarly, per the user's Business Rule "Create Problem when state is Resolved", PRB0010000 was opened at 2018-07-13 22:11:47 (the same time).  
  
Unfortunately, within Business Rule "Create Problem when state is Resolved", the user has the following snippet of code: `current.setWorkflow(false);` This is not bad in-and-of itself. It is only causing an issue because the two Business Rules are racing to see which one will execute first (again, hence the inconsistency of the behavior).  
  
The above piece of code will prohibit all Business Rules from executing after it runs (in this case, it prevented "incident autoclose" from running), which is why the moving of State to "Closed" was never tracked, and thus, never passed down to the task\_sla records to progress them to a "Completed" stage.  
  
Again, the issue here is that both of these Business Rules, "Create Problem when state is Resolved" and "incident autoclose" are executing on the same Order # (100).   
  
Suggest that the user modify their "Create Problem when state is Resolved" to execute on a higher order number than "incident autoclose".  
  
Making the above modification will ensure that the "incident autoclose" Business Rule runs first and succesfully passes down that closure to the task\_sla records, resolving this intermittent SLA behavior. Then, the PRBs will be safely created after "incident autoclose" has already run.
