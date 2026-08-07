---
title: "After installing Employee Relations application, HR admins or admin users are unable to access the components of the application"
aliases:
  - KB2624815
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2624815
kb_number: KB2624815
last_modified: 2025-11-13
---

## After installing Employee Relations application, HR admins or admin users are unable to access the components of the application

  

### Issue

After installing Human Resources: Employee Relations Store Application, users with HR admin role or admin role are unable to access the components of the application like the roles

### Symptoms

When trying to access one of the roles definitions, for example sn\_hr\_er.admin the following error shows:

"Security constraints prevent access to requested page"

### Release

Any

### Cause

sn\_hr\_core.admin role does not contain  sn\_hr\_er.admin role

This happened because the sn\_hr\_er.admin role was removed from the instance and/or imported from another instance and this removed the relationship. The versions of the role in fact reflected this:

![](/sys_attachment.do?sys_id=6f0fc40c47d532d4f64de825126d43e1 "Role versions.png")

### Resolution

  
Add sn\_hr\_er.admin role to sn\_hr\_core.admin role as follows:   
  
1\. Go to sn\_hr\_core.admin role definition:  
https://<instance>.service-now.com/nav\_to.do?uri=sys\_user\_role.do?sys\_id=725370019f22120047a2d126c42e705e  
  
(You may need to move to Human Resources: Core)  
  
2\. Select "Contains Roles' tab  
  
3\. Select 'Edit'  
  
4\. In Collection box, enter sn\_hr\_er.admin , select it and move it to the right.  
  
5\. Save

![Add to contained role](/sys_attachment.do?sys_id=d75f04cc47d532d4f64de825126d4300 "add to contained.png")
