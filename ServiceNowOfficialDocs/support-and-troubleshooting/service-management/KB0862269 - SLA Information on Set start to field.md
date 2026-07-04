---
title: "SLA: Information on \"Set start to\" field"
aliases:
  - KB0862269
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0862269
kb_number: KB0862269
last_modified: 2026-06-24
---

## SLA: Information on "Set start to" field

  

### Summary

  
  
You are looking for the details/link for documentation which can explain the details of "Set start to" field options under SLA conditions.  
To be precise you are looking for details/meaning for each option under "Set start to" field under SLA configuration.  
  

ANSWER:  
  
By default a task\_sla which attaches starts calculating when the task\_sla is created.  
So by default the start time field on the Task\_sla will be set to when it got created.  
  
The field 'set start to' comes into play when you enable Retroactive Start. When you enable Retroactive Start the 'set start to' becomes available.  
It displays a dropdown field with available Date Time fields from the task record defined on the sla definition.  
To elaborate; if the sla definition is mapped to Incident Table then the 'set start to' will show available Date Time fields from Incident table etc.  
  
By setting the 'set start to' field to an available value in the dropdown you are basically determining an alternative Start Time for the Task sla when it attaches. for e.g  
A user opens an Incident Form to create a new Incident at 10:00, assuming the User takes their time filling the Incident values and submits the form at 10:10. The Incident record will have the values Opened: 10:00, Created: 10:10.  
If you select 'opened' in 'set start to' field on the sla definition; and a Task\_sla attaches to the above Incident at 10.30 after having met the start condition, the Start Time on the Task\_sla record will be 10:00.  
  
Note: If you select a field in 'set start to' which has not been populated with a value at the time the task\_sla attaches the Start Time on the task\_sla will default to it's created time.  
  
There is no documentation that explains the fields in the dropdown as these fields will vary depending on the table the sla Definition is mapped to. The meaning of each of these fields will be relative to the Table in which they are located.  
  
  

### Related Links

The below documentation below explains in general the field and how it is used:  
https://docs.servicenow.com/csh?topicname=t\_CreateAnSLADefinition.html&version=latest  
  
Retroactive start: to choose a date and time field from the task that provides the start time of the task SLA. If you select the Retroactive start check box, the Set start to field and the Retroactive pause time check box appear.  
Set start to field: Offers the date and time fields available on the task type that this SLA definition applies to. For example, if you select Retroactive start on a Priority 1 SLA definition and choose Created in the Set start to field, then the SLA is attached with the start time that is the date and time from the Created field on the incident.
