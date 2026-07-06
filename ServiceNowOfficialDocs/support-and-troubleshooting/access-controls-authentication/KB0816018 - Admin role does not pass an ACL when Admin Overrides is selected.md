---
title: "Admin role does not pass an ACL when Admin Overrides is selected"
aliases:
  - KB0816018
tags:
  - servicenow
  - support-kb
  - acl
  - admin-overrides
  - system-properties
  - access-control
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0816018
kb_number: KB0816018
last_modified: 2026-06-18
---

## Admin role does not pass an ACL when Admin Overrides is selected

  

### Issue

Users with the admin role do not pass an access control list (ACL) permissions check on a field, even though the Admin Overrides option is selected (set to true).

### Release

All supported releases

### Cause

When a field has multiple ACLs and the Admin Overrides option is not selected (set to false) on any one of them, the effective Admin Overrides value for all ACLs on that field is treated as false.

### Resolution

The system property glide.security.admin.override.accessterm controls this behavior. When set to true, it forces ACL evaluation for admin overrides at the access term level. The default value is true for new instances and false for upgraded instances.

To resolve the issue, verify the property and set it to true:

1\. Go to the System Properties \[sys\_properties\] table.  
2\. If the property does not exist, create it with the following values:

Name: glide.security.admin.override.accessterm

Description: When it is set to true, it evaluates the admin overridable condition at access term level.

Type: true | false

Value: true

3\. If the property exists but is set to false, change the value to true.

### Related Links

[Evaluate the admin override at the access level](https://docs.servicenow.com/csh?topicname=t_EvalAdmOverrideAccLevel.html&version=latest "Evaluate the admin override at the access level")

## Related

- [[KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow]] — the two-gate ACL model and Admin Overrides consistency requirement
- [[KB0782082 - When 'Admin Overrides' is unchecked and the requirement is to allow a specific roled users (but not admin) to access a f]] — the inverse scenario, restricting admin via Admin Overrides
- [[t_EvalAdmOverrideAccLevel]] — official docs on evaluating admin override at the access level
