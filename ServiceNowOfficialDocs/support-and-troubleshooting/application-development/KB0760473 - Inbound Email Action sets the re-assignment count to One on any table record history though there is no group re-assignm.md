---
title: "Inbound Email Action sets the re-assignment count to \"One\" on any table record history though there is no group re-assignment "
aliases:
  - KB0760473
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0760473
kb_number: KB0760473
last_modified: 2026-05-15
---

## Inbound Email Action sets the re-assignment count to "One" on any table record history though there is no group re-assignment

  

### Issue

When email inbound action triggers for creating any ticket in the platform, the field re-assignment count is incremented by 1 instead of 0 and this is leading to incorrect Business rules being executed.

![](/sys_attachment.do?sys_id=22c4ec291bc90dd0ccc253da234bcbe2)

### Release

London Patch 8 Hot Fix 2

### Cause

i) When we create the incident through email by assigning it to a group , the re-assignment count stays as One. This is because there is an update activity logged on the incident at the time of creating. Check this from incident record -> context menu -> history -> calendar 

ii) When we create the incident manually by assigning a group, the update count in the calendar menu of the incident stays as 0 and is all good

Actual Flow from this KB perspective:

i) An inbound action named "Create/Update Call " which creates/update the records in call table  
  
ii)  When an email is received and processed by this inbound action, the insert doesn't hold the email details initially as there were few fields set by ServiceNow during the insert and the actual call ticket gets created as an update.

  
iii) As you were setting the assignment group during the update, the re-assignment count is incremented to 1 by the default BR which triggers on Call update and increasing the re-assignment count to 1 whereas in reality there is no re-assignment happened at all once the call is assigned to a group.

### Resolution

This behaviour is expected when we try to fill the assignment group through an inbound email.Here is what you need to perform to make sure the reassignment count stays as "0" when the assignment group is assigned the very first time when records are inserted through email.  
  
i) Logon to instance  
ii) Go to the following Business rule named "reassignment counter"  
iii) Go to the Advanced tab  
iV) Modify the condition field to - current.assignment\_group.changes() && JSUtil.notNil(previous.assignment\_group)  --> Increment the re-assignment counter only when the previous assignment group is not NULL  
V) Save the BR  
Vi) Try sending the email once again and you should be all good with the reassignment count value.  
  
Note: The issue doesn't happen when we create the incident manually from the list view.
