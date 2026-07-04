---
title: "Knowledge Templates have no option to delete"
aliases:
  - KB0712605
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0712605
kb_number: KB0712605
last_modified: 2024-08-13
---

## Knowledge Templates have no option to delete

  

### Issue

Unable to delete the article templates.

### Release

All Versions

### Cause

ACL has a role 'nobody' which does not allow to delete the article template.

### Resolution

This is OOB restriction done through ACL.(kb\_article\_template.delete)  
  
There is a role named 'nobody' on this ACL.  
  
The nobody role means that no user has access - not even admin or maint. The nobody role takes precedence over the admin override option on ACLs, so even admins cannot have access.   
  
Reference to this is in the below link:   
[https://docs.servicenow.com/csh?topicname=r\_BaseSystemRoles.html&version=latest](https://docs.servicenow.com/csh?topicname=r_BaseSystemRoles.html&version=latest)   
  
Admin users pass regardless of what script or role restrictions apply. However, the nobody role takes precedence over the admin override option. If an ACL is assigned the nobody role, admin users cannot access the resource even when Admin overrides is selected.   
  
Reference to this is in the below link:   
[https://docs.servicenow.com/csh?topicname=t\_CreateAnACLRule.html&version=latest#t\_CreateAnACLRule](https://docs.servicenow.com/csh?topicname=t_CreateAnACLRule.html&version=latest#t_CreateAnACLRule)   
  
Hence "kb\_article\_template" cannot be deleted. If you want the delete option on the article template,you may have to change the ACL adding desired roles.
