---
title: "Metrics for \"Actual end date\" (work_end) are not getting triggered once the parent Project is closed"
aliases:
  - KB0716548
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0716548
kb_number: KB0716548
last_modified: 2024-04-07
---

## Metrics for "Actual end date" (work\_end) are not getting triggered once the parent Project is closed

  

### Issue

 

# Symptoms

* * *

-   Metrics for "Actual end date" (work\_end) field are not firing when "Actual end date" field value is changed after the parent Project is closed

# Release

* * *

Kingston Patch 9

# Cause

* * *

The metric is being set on the pm\_project table, rather than on the pm\_project\_task table. This is the issue.

# Resolution

* * *

To test the above, a metric was created in an OOB (Out of Box) Kingston instance for the "Actual end date" (work\_end) field on the pm\_project table. Both a Project and a child Project Task were then created.  
  
When the newly created Project Task was closed, a value was populated in the "Actual end date" field on the Project Task. This is expected. A "metric.update" entry was created in the Event Logs, as the parent Project was still open and active (it closed just after the child Project Task was closed).  
  
After the Project was closed (active = false), the value within the "Actual end date" field was manually changed to see if another "metric.update" entry would be created in the Event Logs. While the change did save to the Project Task and was reflected in the parent Project after a short delay, no "metric.update" entry was created in the Event Logs as the parent Project was active = false.  
  
This is expected behavior for the Platform.

To properly create a metric for "Actual end date" which fires even if the parent Project is active = false, create the metric on pm\_project\_task rather than on pm\_project. This will allow changes to the "Actual end date" field to fire the metric properly, and reporting can be done off of said metric.
