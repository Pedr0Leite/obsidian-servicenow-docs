---
title: "Sla Timezone Source field value added in sys_choice value as invalid"
aliases:
  - KB0957011
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0957011
kb_number: KB0957011
last_modified: 2026-06-24
---

## Sla Timezone Source field value added in sys\_choice value as invalid

  

### Issue

You have added a new sys\_choice value for element "timezone\_source" for Table 'contract\_sla'  
  
Value: task.assignment\_group.manager.location.time\_zone  
Label: The assignment group's manager's location's time zone  
  
On the sla definition record when we have selected from the timezone source dropdown choice as 'The assignment group's manager's location's time zone', we find that the dropdown displays a value that does not appear to be correct 'task.assignment\_group.manager.location.t'. It is truncated.  
You can see that it displays as blue, which means it is an invalid choice.  
  
STEPS TO REPRODUCE/OBSERVE BEHAVIOR:  
1\. Add the new sys\_choice value for element "timezone\_source" for Table 'contract\_sla'  
Value: task.assignment\_group.manager.location.time\_zone  
Label: The assignment group's manager's location's time zone  
2\. Add the new choice value in script include SLATimezone  
3\. Navigate to an Sla definition or create a new sla definition  
In timezone source select the choice label 'The assignment group's manager's location's time zone',  
Enter other values on the sla and try to save or submit.  
  
Result is the truncated value is displayed in the dropdown. The truncated value is also saved in the field.

![](sys_attachment.do?sys_id=4820caa747e9c3103542f24c736d4391)

![](sys_attachment.do?sys_id=c820caa747e9c3103542f24c736d438c)

### Release

All

### Cause

By design Choice list values allow a maximum length of 40 characters.  
This choice value task.assignment\_group.manager.location.time\_zone exceeds this platform limit.  
  
https://docs.servicenow.com/bundle/paris-platform-administration/page/administer/field-administration/task/t\_ViewChoiceListDefinitions.html  
View choice list definitions  
Choice list values allow a maximum length of 40 characters. The range of allowable numerical values is \[-999, 999\].

### Resolution

  
To resolve the issue you can modify the sys\_choice value and shorten it to ensure it is less that 40 characters.  
  
1\. As an e.g. open the sys\_choice definition  
Change it from  
value: task.assignment\_group.manager.location.time\_zone  
to  
value: task.amt\_group.mgr.location.time\_zone  
  
The label does not matter.  
  
2\. In script include, modify it as below  
  
case 'task.amt\_group.mgr.location.time\_zone':  
return taskGr.assignment\_group.manager.location.time\_zone;  
  
Note the choice list value is defined in the script include 'case' object  
while the 'return' object is the full dot walked path to the record 'task.assignment\_group.manager.location.time\_zone'  
  
see my attached screenshots showing we done this.

  
This resolves the issue; the value no longer gets truncated and does not display an invalid entry in the dropdown.

![](sys_attachment.do?sys_id=c020caa747e9c3103542f24c736d433d)  
  
  

![](sys_attachment.do?sys_id=0820caa747e9c3103542f24c736d4337)
