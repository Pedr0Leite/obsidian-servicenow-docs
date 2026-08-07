---
title: "Is there a timeout to close the window after user changes password in the Password Reset Windows Application?"
aliases:
  - KB0781681
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0781681
kb_number: KB0781681
last_modified: 2024-05-21
---

## Is there a timeout to close the window after user changes password in the Password Reset Windows Application?

  

### Issue

Customers might notice that after changing the password, using the Password Reset Windows Application, the password will get exposed to the screen right after.

The following screenshot shows from the normal Password Reset documentation an example of what will appear when using the Windows Application as well.

![](sys_attachment.do?sys_id=8b010e4fdbb8b4102dc24f7813961991)

  

The **question** some customers can have is:  
Is there any property where we can set a timeout to get rid of this screen after X minutes or seconds?

### Release

All

### Resolution

The **answer** is:  
There's an internal timeout value, which is not exposed to the customers, where this screen/window with the password will be auto closed after 10 minutes.  
  
As this is hardcoded, there's no way to change this time.  
Customers can raise an Idea about it and we can hope this gets implemented in the future.
