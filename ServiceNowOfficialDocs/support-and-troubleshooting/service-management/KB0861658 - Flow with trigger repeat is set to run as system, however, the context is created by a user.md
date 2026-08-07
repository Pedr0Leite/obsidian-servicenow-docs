---
title: "Flow with trigger \"repeat\" is set to run as system, however, the context is created by a user"
aliases:
  - KB0861658
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0861658
kb_number: KB0861658
last_modified: 2024-04-08
---

## Flow with trigger "repeat" is set to run as system, however, the context is created by a user

  

### Issue

-   Flow with trigger "repeat" is set to run as system, however, the context is created by a user

  

**Steps to Reproduce:**   
  

1.  impersonate Fred Luddy  
    
2.  create a flow with a trigger set to "repeat" every 10 seconds  
    
3.  and in the property set to run as system  
    
4.  add 'log' action, and activate the flow  
    
5.  look at the flow executions, and notice how the flow contexts are created as fred luddy  
      
    since the flow is set to run as system, it should say system

### Cause

-   the \[sys\_flow\_trigger\_auto\_script\] record that gets created is set to "run as" as fredd luddy
-   however, this is not a defect because flow designer makes use of attributes that tell the engine how a flow should execute
-   if you open the \[sys\_flow\_context\] that was created in the attribute column, you'll see a JSON object, in this object you'll see the attribute "run\_as" set to "system"
-   this can be further verified by running the following script in a log action:  
    
    "flow running as user: " + gs.getUserName();
