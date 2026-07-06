---
title: "Why do work_note field on incidents, created by reopened alert not have the correct task template?"
aliases:
  - KB0718112
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0718112
kb_number: KB0718112
last_modified: 2024-05-22
---

## Why do work\_note field on incidents, created by reopened alert not have the correct task template?

  

### Issue

# Symptoms

* * *

When customer has an auto open incident Alert rule that will apply a task template on the incident. The task template sets the incidents worknote field but when a new event comes in and reopens the alert, the newly created incident does not have the worknote field correctly updated per the task template.

# Cause

* * *

  
When a new Event comes in and reopens the alert, the "Reopen associated closed incident" Business Rule is triggered and create a new Incident which then invokes the application of task template. At the same time an update to work note field is triggered to update the message "The related alert {0} is now unlinked from the previous {1} {2}", \[alertNumber, type, taskNumber\]));"  
  

Both these entries are made to the work\_note Journal entry at the same time and hence we only update one of the records.

# Resolution

* * *

As a workaround to this behavior a gs.sleep(1001); can be introduced between the two inserts such that the inserts are a second apart and both reflect when an update is made on the field. In order to apply this workaround please follow the steps:

1\. In application navigator type business rule, click on "Reopen associated closed incident"   
2\. In step 185 , please type gs.sleep(1001); just before the call to below statement  
updateWorkNoteField(newTask, gs.getMessage("The related alert {0} is now unlinked from the previous {1} {2}",   
\[alertNumber, type, taskNumber\]));   
3\. Once you have done this please test the behavior on new incident creation. You should be able to see the worknotes update.
