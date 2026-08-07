---
title: "Changing the user password through an import invalidates the user's session"
aliases:
  - KB0550648
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0550648
kb_number: KB0550648
last_modified: 2024-04-07
---

## Issue

When running an import (scheduled or manual) that loads user data and includes the password field in the transform map, the logged-in user's session is invalidated after changing the user's password through the import.

## Resolution

This issue occurs, because whenever a user's password is changed, the base system **Flush Change Password** business rule is run, which invalidates the user's session in the v\_user\_session virtual table. When the user's session is invalidated, the next time this user performs any action in ServiceNow, they are logged out and forced to re-login. Any updates the user was trying to enter into ServiceNow are lost when the session is invalidated and must be reentered.

To work around this issue, always exclude the password field from scheduled imports or run these imports outside of business hours only.
