---
title: "Scripts actions are triggered by \"Guest\" user instead of \"System\" user."
aliases:
  - KB0785010
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0785010
kb_number: KB0785010
last_modified: 2024-04-25
---

## Scripts actions are triggered by "Guest" user instead of "System" user.

  

### Issue

When the notifications are triggered by script actions, these script actions are usually created by System, but in some cases, these are triggered by the Guest user.

### Cause

The script actions are triggered as Guest if there is already a user with the sys\_id "system".

Check for the user record with the sys\_id system:

/nav\_to.do?uri=sys\_user.do?sys\_id=system

### Resolution

The instance should not have the user id with the sys\_id system even if it is deactivated. The User record should be deleted.
