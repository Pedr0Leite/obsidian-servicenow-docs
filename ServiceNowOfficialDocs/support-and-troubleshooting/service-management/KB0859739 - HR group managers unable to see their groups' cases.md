---
title: "HR group managers unable to see their groups' cases"
aliases:
  - KB0859739
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0859739
kb_number: KB0859739
last_modified: 2024-04-08
---

## HR group managers unable to see their groups' cases

  

### Issue

The user was facing an issue where HR group managers, who should be able to see all cases which pertain to their assignment group, are not able to see all of their groups' cases.

### Cause

There was a custom query Business Rule which was causing the issue.

### Resolution

As shared above, the issue was that the user had a custom, query Business Rule that was causing the HR group manager to only see 47 of their group's 1,100+ HR cases.  
  
Disabling the custom Business Rule until it could be further reviewed internally by the user's development team solved the issue.

The user was gently reminded that Support engineers are experts in OOB behavior and specialize in resolving OOB break-fix behaviors. The debugging and implementation of customizations are out of scope for Support.
