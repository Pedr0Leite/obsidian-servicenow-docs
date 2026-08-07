---
title: "In the 'Facilities Request', records are showing Updated by 'guest' user"
aliases:
  - KB0859858
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0859858
kb_number: KB0859858
last_modified: 2024-04-08
---

## In the 'Facilities Request', records are showing Updated by 'guest' user

  

### Issue

In the Facility Request, under the   
     
       **Facilities >> Request >> All Facilities** 

  

The 'Autoclose facilities requests' Scheduler Job triggers the 'Request Autoclose' business rule to 'Close' the Requests which are in 'Resolved' state for defined time.

       **System Scheduler >> Scheduled Jobs >> Autoclose facilities requests**

  

However, the 'Autoclose facilities requests' Scheduler Job trigger the BR as follows:  
  
        **fcRunAs=admin**  
        **fcScriptName=Request Autoclose**  

  

It will runs/triggers as 'admin' and if 'admin' record is not present in the 'sys\_user' table, then it will pick 'Guest' as a default user.

Since, there is no 'admin' record in the sys\_user' table, 'Guest' appeared in the 'updated\_by' field.

  

**![](/sys_attachment.do?sys_id=e44a3081db80f8d066e0a345ca9619c1)**

**![](/sys_attachment.do?sys_id=6c4a3081db80f8d066e0a345ca9619c2)**

  

### Cause

The 'Admin' record is deleted from the 'sys\_user' record, which is being used by the 'Autoclose facilities requests' Scheduler Job and this is responsible for triggering the 'Request Autoclose' business rule.

### Resolution

There are two possible ways to solve the issue,

-   Please ensure that you bring that 'admin' user record back into the 'sys\_user' table.

    **OR**

-   In the Scheduler Job, you need to modify the existing code. (Again this will be the customisation).  
         This is the code which will trigger/run the 'Request Autoclose' BR as 'admin'  
                      fcRunAs=admin  
                      fcScriptName=Request Autoclose
