---
title: "The $knowledge.do page (Knowledge homepage) is locked for all users except those with the admin role."
aliases:
  - KB0781912
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0781912
kb_number: KB0781912
last_modified: 2024-04-08
---

## The $knowledge.do page (Knowledge homepage) is locked for all users except those with the admin role.

  

### Issue

The user wanted to know why the /$knowledge.do page (Knowledge homepage) is locked for all users except those with the admin role.

### Cause

Upon installing "Customer Service Base Entities" (com.snc.cs\_base) plugin, a new ui\_page ACL was entered into the user's system which restricts viewership of the $knowledge.do homepage to users with the "sn\_esm\_user" role.

### Resolution

As per the above, the reason admins are able to see the knowledge homepage fine is because the ACL is set to have admins override it.  
  
Here is the ACL:  
  

-   /sys\_security\_acl.do?sys\_id=15d22e53d7210200bef20ee60e61039

  
Tests were performed in the user's sub-Production environment and confirmed that disabling (making "active" = "false") this ACL and clearing the cache (typing "cache.do" in the left navigator) does resolve this issue.  
  
Alternatively, the user could simply change the roles required to pass this ACL to meet their business needs.
