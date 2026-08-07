---
title: "Task SLAs are not transitioning correctly based on custom State field (u_state)"
aliases:
  - KB0859736
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0859736
kb_number: KB0859736
last_modified: 2024-04-08
---

## Task SLAs are not transitioning correctly based on custom State field (u\_state)

  

### Issue

The user was facing an issue where thousands of task SLAs were not transitioning properly based on the conditions in the SLA Definition. Namely, the user had configured the SLA Definition to transition to the task SLA to a Stage of "Completed" when the user's custom State (u\_state) field was set to a value of "Closed".

### Cause

It was found that the SLA Definition was not looking at the custom State (u\_state) field, but rather the Out of Box (OOB) State field.

### Resolution

After noticing this, the user created a custom Business Rule to sync the custom State (u\_state) field to the OOB State field. After this, the user inquired of how to fix the impacted records.  
  
It was recommended to the user, after taking counsel with ServiceNow Developers, that they should update the incidents to the correct OOB State value (as would allow the custom State \[u\_state\] field to sync with the OOB State field), and to do this mass script update in a Scheduled Job. The user was advised to ensure that their query for the thousands of records was spot on. Doing the update this way would trigger an update on the task SLAs, run critical Business Rules, and transition the task SLAs to the expected Stage value of "Completed".
