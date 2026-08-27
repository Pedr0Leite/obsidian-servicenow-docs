---
title: "Not able to create flow action within the scoped Application"
aliases:
  - KB0832736
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0832736
kb_number: KB0832736
last_modified: 2024-04-08
---

## Not able to create flow action within the scoped Application

  

### Issue

Login as user who is part of an application.

Go to flow designer and try to create a new action -

Notice the application while creating the action is set to the application, user is in.

However when you save the flow - notice the application goes back to "global".

### Release

Every instance that has flow designer plugin installed.

### Cause

Due to the user not have access to write on sys\_scope table.

### Resolution

  
The root cause of this case task is an ACL issue; users who does not have ACL writes to read and write on application (sys\_scope) table.

If a user who does not have access to write, the action is saved as Global application/scope when saved because Global application is the default application if no application is available.
