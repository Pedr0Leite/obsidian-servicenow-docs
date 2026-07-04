---
title: "SLA Actual elapsed time and Actual elapsed percentage are at '0' even when the task_sla Stage is \"In progress\" - why?"
aliases:
  - KB0778509
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0778509
kb_number: KB0778509
last_modified: 2025-11-17
---

## SLA Actual elapsed time and Actual elapsed percentage are at '0' even when the task\_sla Stage is "In progress" - why?

  

### Issue

The user has an incident record and a task\_sla on that incident record. The task\_sla record, in both the related list and task\_sla record itself, is showing that the Actual elapsed time and Actual elapsed percentage are at '0' even when the task\_sla Stage is "In progress".

### Cause

System property "glide.sla.calculate\_on\_display" is set to a value of "false".

### Resolution

As mentioned above, it was found that by setting the above system property to a value of "true", the behavior no longer occurs.  
  
This is because setting the system property to a value of "true" ensures that the timings in the Task SLAs are updated each time the task form is viewed.

Otherwise, the user has to manually go into the task\_sla and click the "Refresh" UI Action to see updated timings (e.g. when the system property is set to "false").
