---
title: "Slow Loading of Reference Variables to HR Profile Table for Non-HR Users"
aliases:
  - KB1733232
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1733232
kb_number: KB1733232
last_modified: 2025-09-03
---

## Issue

Catalog variables pointing to the "sn\_hr\_core\_profile" table might take long time to load.

## Resolution

To resolve this issue, consider the following options:  
  
1\. Grant the "sn\_hr\_core.profile\_reader" role to the affected users.  
2\. Adjust the reference qualifier of the variable to reduce the number of HR Profiles being returned.  
3\. Customize the Read ACL on sn\_hr\_core\_profile.\* with sys\_id = 3e5370019f22120047a2d126c42e7001 to remove/reduce its logic (not recommended).
