---
title: "User Unauthorized error when opening HR profile from case in agent workspace"
aliases:
  - KB0962927
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0962927
kb_number: KB0962927
last_modified: 2025-09-03
---

## User Unauthorized error when opening HR profile from case in agent workspace

  

### Issue

User isn't able to open HR profile from case in agent workspace - getting error in console: User unauthorized

### Release

Paris

### Cause

  
Access Control (ACL) for Table API was active --  
When clicking on the "Open HR Profile" icon, the /api/now/table/sn\_hr\_core\_profile API is executed. Because of above ACL, the user is not allowed to run it.

### Resolution

Deactivate the ACL for Table API as it is suggested that users should rely on ACLs defined on the underlying data being accessed rather than activating this ACL.  
You can review the ACL here:  
  

https://<yourinstancename>.service-now.com/nav\_to.do?uri=%2Fsys\_security\_acl.do%3Fsys\_id%3D9ef8bc918733320025fbd1a936cb0bdd

### Related Links

This ACL is deactive OOB
