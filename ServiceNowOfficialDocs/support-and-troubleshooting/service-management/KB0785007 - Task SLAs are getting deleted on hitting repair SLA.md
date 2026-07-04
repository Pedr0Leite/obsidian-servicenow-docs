---
title: "Task SLAs are getting deleted on hitting repair SLA"
aliases:
  - KB0785007
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0785007
kb_number: KB0785007
last_modified: 2026-06-24
---

## Task SLAs are getting deleted on hitting repair SLA

  

### Issue

While repairing the SLA for INC records, its deleting the attached SLA records.

**Steps to Reproduce:** 

  
Navigate to a list of SLA records or task records.  
Check the records to repair against.  
Select the Repair SLAs for selected list action.

### Release

All

### Cause

We found that the SLA definition that is needed to recreate the new task sla record during the repair sla functionality is INACTIVE.  
  
  
Please note it is the expected behavior that repair sla deletes existing records and then recreates them using the audit history of the task AND the current sla definition  
  
\--> https://docs.servicenow.com/csh?topicname=c\_RepairSLAs.html&version=latest  
  
Repair of SLAs is useful to determine accurate timing information if your system has SLA records that contain incorrect values. For example, you may need to repair SLA records as a result of:  
poorly defined schedules  
poorly defined conditions on an SLA Definition  
some other system anomaly  
The repair function removes the SLA record, then recreates and recalculates it from the start, including recreating the workflow. The repair uses the history from the Task and if appropriate will also create new Task SLAs that did not previously exist. For example, a new Task SLA may be needed if a new SLA Definition has been added since an associated Incident was created or updated.

### Resolution

  
1\. If you need to repair sla on task records, you need to ensure that for every task record it has audit data available.  
In addition, ensure the expected sla definition is active, because when the sla repair deletes the record it needs to reference the sla definition to rebuild it..  
  
  
2\. In this customer case the task sla records which have been deleted was still available and could be recovered from the deleted records modules.   
Please review the documentation on how to restore deleted records  
https://docs.servicenow.com/csh?topicname=c\_TableAdministration.html&version=latest
