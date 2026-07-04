---
title: "HR Assignment Rules getting created in the Global Scope and not in HR scope."
aliases:
  - KB0820690
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0820690
kb_number: KB0820690
last_modified: 2025-09-03
---

## HR Assignment Rules getting created in the Global Scope and not in HR scope.

  

### Issue

HR Assignment Rules getting created in the Global Scope and not HR. Due to this, the users responsible for maintaining the IT application have access to update the HR assignment rules which is a serious concern. 

### Resolution

Unless user selects application from application picker, records in metadata tables can not be created with scope. Application picker will be there only if user is added as developer for an application (OR) user have delegated developer role.  
Once data is created with appropriate scope, logic in scoped acl can restrict the data.  
  
Read more about delegated developer role here -  

[https://docs.servicenow.com/csh?topicname=t\_HRAdminRoles.html&version=latest](https://docs.servicenow.com/csh?topicname=t_HRAdminRoles.html&version=latest)

[https://docs.servicenow.com/csh?topicname=t\_AddADeveloper.html&version=latest](https://docs.servicenow.com/csh?topicname=t_AddADeveloper.html&version=latest)
