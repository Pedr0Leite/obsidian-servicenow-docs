---
title: "SLA Timeline not visible"
aliases:
  - KB0966916
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0966916
kb_number: KB0966916
last_modified: 2026-06-24
---

## SLA Timeline not visible

  

### Issue

  
SLA Timeline not visible for some Task SLAs

Also the whole sla disappears after clicking the "Repair SLA Link"

### Release

All

### Cause

  
This occurs when there is no valid Audit history, this would most likely be as a result of the instance being a clone.  
Note that by default when cloning an instance over another instance audit tables are excluded.  
  
If Audit was not copied over during Cloning, this kind of issues occur.  
  
As a result the timeline is not able to recreate the task sla using the audit information.  
Please note this is the same behavior Repair Sla will have as it also relies on audit data. So if you were to attempt to repair the record the sla repair will delete it but will not be able to recreate it.

### Resolution

  
The reported behavior is by design. SLA Timeline is a feature which is heavily dependent on the relevant Tasks Audit history and the Sla definition.  
The Timeline data is built just intime when you click the UI Action. It is using the Audit history of the Task record and the Sla definition to create the Task Sla in memory.  
  
To resolve your issue, clone your instance and ensure that you select the option to include the Audit Tables when cloning. This is necessary if you require the instance for Task Sla investigative purposes.  
With valid audit entries you will be able to view SLA Timeline and also Repair SLA.  
  
  

### Related Links

Please reference the below documentation  
  
https://docs.servicenow.com/bundle/quebec-it-service-management/page/product/service-level-management/concept/c\_SLATimeline.html  
Note:  
The SLA timeline receives information about the task from the audit history and refers to the current SLA definition to pull data for the SLA timeline. The SLA timeline displays task SLA information as though the SLA repair is already executed, irrespective of whether it is executed or not.
