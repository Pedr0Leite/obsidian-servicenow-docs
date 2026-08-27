---
title: "Who can create Response Templates in HR Scope."
aliases:
  - KB2546407
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2546407
kb_number: KB2546407
last_modified: 2025-10-12
---

## Who can create Response Templates in HR Scope.

  

### Issue

Users with the role 'sn\_hr\_core.manager' are unable to create response templates, despite having the necessary access control list (ACL) permissions.

### Release

ALL

### Resolution

1\. To create a response template, users need the 'sn\_templated\_snip.template\_snippet\_writer' role and the ACL is checking for access: https://instance.service-now.com/sys\_security\_acl.do?sys\_id=01c796430b63320036e62c7885673ac4.  
2.Only the user with 'sn\_hr\_core.manager' can update the Response Template in HR Scope.  
3\. If you would like to provide access to other roles, you will have to customize the Script include as the validation is happening from the SI: https://instance.service-now.com/sys\_script\_include.do?sys\_id=56b9de830b32320036e62c7885673ae1.  
4\. The whole idea of having the manager role is for managers to have access to create the response templates. As per the functionality, only 'sn\_hr\_core.manager' will be able to create the response templates in the HR scope. The best practice is to have managers create the response templates.
