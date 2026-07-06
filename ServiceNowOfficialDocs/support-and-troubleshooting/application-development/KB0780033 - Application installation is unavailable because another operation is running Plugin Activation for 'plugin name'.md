---
title: "Application installation is unavailable because another operation is running: Plugin Activation for 'plugin name'"
aliases:
  - KB0780033
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0780033
kb_number: KB0780033
last_modified: 2024-04-08
---

## Application installation is unavailable because another operation is running: Plugin Activation for 'plugin name'

  

### Issue

Admin users on domain separated instances with domain delegated administration enabled can see the following when trying to install a plugin although no plugin is currently being installed:

![](/sys_attachment.do?sys_id=67c92b70db0874d04cfbeeb5ca9619c6)

### Release

Seen in New York

### Cause

When 'Domain delegated administration' is enabled the user must comply with the following constraints in order to activate plugins:

1.  Have the 'Admin' role
2.  Not be a read-only user
3.  Must be in the 'global' domain

### Resolution

If the 'Domain delegated administration' property is set to true, make sure that the administrative user is in the 'global' domain.

### Related Links

PRB1363926 is currently being reviewed to correct the message
