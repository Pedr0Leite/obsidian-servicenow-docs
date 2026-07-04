---
title: "Unable to select sys_attachment as an input on flow action within scope"
aliases:
  - KB0820528
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0820528
kb_number: KB0820528
last_modified: 2024-04-08
---

## Unable to select sys\_attachment as an input on flow action within scope

  

### Issue

Go to Flow Designer  
Select application other than global  
Create a new Action.  
Add an input parameter called Document, select Reference.sys\_attachment  
None is found.

### Release

On all versions that has flow designer plugin installed

### Cause

due to the system property - sn\_flow\_designer.allowed\_system\_tables

### Resolution

  
This was done on purpose by internal team so that users will be very careful when updating the action.

Please be very careful when using sys\_attachments in action and flow.

So, its needs to be connected with sys\_attachment\_doc to work. 

Open the below property and remove sys\_attachment from the property sn\_flow\_designer.allowed\_system\_tables.

https://<instance\_name>.service-now.com/nav\_to.do?uri=sys\_properties.do?sys\_id=66faaabec31213002841b63b12d3ae36  
  

### Related Links

As such there property which has a very confusing name sn\_flow\_designer.allowed\_system\_tables which in reality is the opposite of its name. (Something we need to change).
