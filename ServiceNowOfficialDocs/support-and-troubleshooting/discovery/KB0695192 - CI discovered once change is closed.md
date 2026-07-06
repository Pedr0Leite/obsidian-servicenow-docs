---
title: "CI discovered once change is closed"
aliases:
  - KB0695192
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695192
kb_number: KB0695192
last_modified: 2024-05-22
---

## CI discovered once change is closed

  

### Issue

# Overview

* * *

Change requests often have a configuration item associated with the change. A discovery of the configuration item will be triggered if discovery is installed and configured. The "created by" field in the discovery will reflect the user that closed the change.

# Solution

* * *

The business rule "Run rediscovery after change request" triggers the discovery. This business rule checks on sys\_property "sa.redisovery\_after\_change" to determine if the discovery should be triggered after a change is closed.

Such discoveries can be avoided by either:

1.  Disabling the business rule "Run rediscovery after change request"
2.  Set "sa.rediscovery\_after\_change" = false, the property may need to be created if it does not already exist in the environment

Conditions can be added to the business rule to limit the roles of users that can trigger such discoveries.

# Additional Information

* * *

The discovery will be triggered even if the user does not have the roles necessary to create a discovery. This is expected behavior, otherwise all users closing changes would need discovery admin roles. The behavior can be modified as described in the "Solution" section of this KB article.
