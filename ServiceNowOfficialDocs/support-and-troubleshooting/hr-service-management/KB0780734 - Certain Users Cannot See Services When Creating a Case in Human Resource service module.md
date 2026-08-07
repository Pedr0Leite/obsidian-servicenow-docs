---
title: "Certain Users Cannot See Services When Creating a Case in Human Resource service module"
aliases:
  - KB0780734
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0780734
kb_number: KB0780734
last_modified: 2025-09-03
---

## Issue

\- When anyone with HR Basic access attempts to create a new case they can only see certain services. - Users with HR Admin access can see them all.

## Resolution

 We modified this below ACL and it started working:  
  
The hr services (sn\_hr\_core\_service records) that are not displayed are from "Human Resources: Service Portal" scope.  
  
The ACL that grants the read access to hr services is in "Human Resources: Core" scope:  
[https://instacnename.service-now.com/nav\_to.do?uri=sys\_security\_acl.do?sys\_id=ccaa98b69f131200d9011977677fcf75](https://vrtxdev.service-now.com/nav_to.do?uri=sys_security_acl.do?sys_id=ccaa98b69f131200d9011977677fcf75)  
  
This ACL doesn't get triggered for the sn\_hr\_core\_service records that are not in "Human Resources: Core" scope . The current issue is because there is no ACL that grants read access for hr services from "Human Resources: Service Portal".  
  
To fix this, the same read ACL needs to be created in "Human Resources: Service Portal" scope as well.  
  
Created the same ACL in "Human Resources: Service Portal" scope and it started working:  
[https://instacnename.service-now.com/nav\_to.do?uri=sys\_security\_acl.do?sys\_id=de791fe61b93fb00117497d58d4bcbb5](https://vrtxdev.service-now.com/nav_to.do?uri=sys_security_acl.do?sys_id=de791fe61b93fb00117497d58d4bcbb5)
