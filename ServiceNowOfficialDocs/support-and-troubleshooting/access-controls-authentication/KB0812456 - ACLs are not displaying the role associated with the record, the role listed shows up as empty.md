---
title: "ACLs are not displaying the role associated with the record, the role listed shows up as \"empty\""
aliases:
  - KB0812456
tags:
  - servicenow
  - support-kb
  - acl
  - roles
  - sys_security_acl_role
  - data-integrity
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0812456
kb_number: KB0812456
last_modified: 2024-04-08
---

## ACLs are not displaying the role associated with the record, the role listed shows up as "empty"

  

### Issue

When you navigate to a particular ACL in your instance, you can see the roles in the list of roles are not displaying for some of them, they are displayed as "empty"

### Release

All supported releases

### Cause

The role that was associated with this ACL no longer exists in the instance.  If you click on the reference icon and open the record, you will see a "sys\_security\_acl\_role" record where the "sys user role" field is empty. When you click on the reference icon of "sys user role" you will see the message "No Preview Available", because the record does not exist. 

### Resolution

Import the missing role from another instance or remove the bad reference from the ACL if the role is no longer used in your company.

## Related

- [[KB0753001 - Some roles are not  visible and cannot be exported from the [sys_user_role] list table]] — another sys_user_role data/visibility issue
- [[KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow]] — background on how roles participate in ACL evaluation
