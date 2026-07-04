---
title: "How to restrict users to stop creating HR cases from sn_hr_core_case_creation UI page"
aliases:
  - KB0952389
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0952389
kb_number: KB0952389
last_modified: 2025-09-03
---

## How to restrict users to stop creating HR cases from sn\_hr\_core\_case\_creation UI page

  

### Issue

Our current set-up of case management, it allows the agents to create cases from the HR Portal as well as the back-end. 

### Release

Paris Patch 4

### Resolution

This needs an update to ACL on UI page sn\_hr\_core\_case\_creation. 

  
https://OOBSERVICENOW.service-now.com/sys\_security\_acl.do?sys\_id=b9afef61ebb00300a9e7e26ac106fe3a  
  
Adding admin role to this ACL and now only users with ADMIN will be able to access the page sn\_hr\_core\_case\_creation  
  
\*\* This functionality is to stop HR users to not create a case from Platform View and users will be able to create cases from ESC portal
