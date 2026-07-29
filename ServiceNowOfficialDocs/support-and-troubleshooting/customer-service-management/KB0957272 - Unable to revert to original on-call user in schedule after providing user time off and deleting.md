---
title: "Unable to revert to original on-call user in schedule after providing user time off and deleting"
aliases:
  - KB0957272
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0957272
kb_number: KB0957272
last_modified: 2026-06-24
---

## Unable to revert to original on-call user in schedule after providing user time off and deleting

  

### Issue

When a user has successfully scheduled a time off, and got another User to cover, it's not possible to be reverted to the original user after deleting the time-off.

Below error is generated:  
Time off - In approval request for user overlaps with existing Coverage request  
  
STEPS TO REPRODUCE/OBSERVE BEHAVIOR:  
\*\* property: com.snc.on\_call\_rotation.pto.configuration = without\_approval

  
1- Impersonate User  
2- In filter navigator go to on-call - > schedules -> choose relevant Group  
3- go to an on-call date  
4- Right click -> actions -> manage shift  
5- Choose schedule time-off, choose the member of that day (mem 1), choose another member as replacement (mem 2)-> schedule  
6- Right click the time off span -> actions -> delete time off (created for mem1)  
7- go to the on-call date which had the time off removed  
8- Right click -> actions -> manage shift  
9- Choose schedule time-off, choose the member of that day (mem2), choose the initial user that was replaced as replacement (mem 1)-> schedule  
10- We then get the error.  
  
![](sys_attachment.do?sys_id=96f00aa3472dc3103542f24c736d4359)

### Release

All

### Cause

This is working as expected. Process followed above in steps to reproduce which generated the error is incorrect.  
  
  
Error is coming from "RotaScheduleEntryValidation" : sys\_script\_include.do?sys\_id=74168ee49f2020008f88ed93ee4bcca4  
  
line no.83  
  
if (rosterScheduleSpanGr.next()) {  
this.\_valid = false;  
if (this.cmn\_schedule\_span.type == 'time\_off')  
this.\_displayMessage(gs.getMessage("Time off request for user overlaps with existing Coverage request"));

Before providing time off for the user who is doing the coverage, the coverage should be deleted

### Resolution

  
To resolve this issue and place the original user (in step 5 who went on timeoff) back to provide coverage, follow the below steps  
  
After step 7, as per above repro steps  
8- Right click on the Users span- currently in purple showing the User (mem 2) providing coverage for time-off user  
9\. Select from the drop down Actions -> Delete coverage  
  
The coverage is deleted and the original User (mem 1) that was replaced is shown as providing coverage.  
You do not need to do anything else.  
See the attached screenshots showing the correct steps to revert to the original on-call user. (date 30th)  
  
  

![](sys_attachment.do?sys_id=42f0c6a3472dc3103542f24c736d435a)

Right click on User span

![](sys_attachment.do?sys_id=d2f0c6a3472dc3103542f24c736d435f)

Select Action > Delete coverage

![](sys_attachment.do?sys_id=def00aa3472dc3103542f24c736d4311)

After deleting it reverts to the previous original user

![](sys_attachment.do?sys_id=5af00aa3472dc3103542f24c736d4316)
