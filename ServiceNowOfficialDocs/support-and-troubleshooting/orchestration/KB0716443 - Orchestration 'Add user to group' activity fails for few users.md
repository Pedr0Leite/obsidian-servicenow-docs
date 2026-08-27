---
title: "Orchestration: 'Add user to group' activity fails for few users"
aliases:
  - KB0716443
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0716443
kb_number: KB0716443
last_modified: 2024-04-07
---

## Orchestration: 'Add user to group' activity fails for few users

  

### Issue

# Symptoms

* * *

            1. For the failed users, the powershell response was -> Cannot find the AD group 

# Release

* * *

All

# Cause

* * *

1.  In this case, the workflow first creates an AD group, then starts adding users.
2.  Five users were being added to the group. The 'Add user to group' activity failed for first 3 users and worked for last 2 users.
3.  Cause: When an AD group is created, you need to wait for sometime before starting to add users to the newly created group.

# Resolution

* * *

1.  Leveraged workflow timer activity to add some delay after creating the AD group and before starting to add users.
