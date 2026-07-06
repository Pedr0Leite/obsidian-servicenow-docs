---
title: "When 'Admin Overrides' is unchecked and the requirement is to allow a specific roled users (but not admin) to access a field, need to make to use of ACL script."
aliases:
  - KB0782082
tags:
  - servicenow
  - support-kb
  - acl
  - admin-overrides
  - high-security-settings
  - acl-script
  - system-properties
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0782082
kb_number: KB0782082
last_modified: 2024-01-28
---

## Issue

If the requirement is to make some sensitive data/field to be available only for a specific role and to get it restricted for others including 'admin', we need to make use of 'Admin Overrides' concept (need to untick Admin Overrides) and at the same time we need to have ACL Script in place that allows the specific roled users to have access to the field.

NOTE: This is not possible if you have a specific role present in the 'Roles' embedded list. This has to be explicitly done on the ACL script level.

## Resolution

For admin overrides to work effectively and restrict 'Admin' users from PASSING an ACL, 'High-Security Settings' plugin needs to be active and the system property ''glide.security.admin.override.accessterm' should be set as true.

Below product documentation can be referred:

[High Security Settings](<https://docs.servicenow.com/csh?topicname=t_ActivateHighSecuritySettings.html&version=latest"\>Activate High Security Settings> "High Security Settings")

[Evaluate the admin override at the access level](https://community.servicenow.com/community?id=community_question&amp;sys_id=b3ff52bcdb361b00b2102926ca961943 "Evaluate the admin override at the access level")

But to allow specific role users to have access (the ACL to be passed) we need to have a script in place explicitly that checks the role of the logged-in user and allows access accrordingly. (Having the custom role in 'Roles' embedded list will not serve the purpose here)

## Related

- [[KB0816018 - Admin role does not pass an ACL when Admin Overrides is selected]] — the counterpart scenario where Admin Overrides is expected to be true and consistent
- [[KB0750886 - ACL script is failing at script include function call]] — syntax pitfalls when writing the required ACL script
- [[KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow]] — background on how Admin Overrides is evaluated across the ACL chain
- [[t_ActivateHighSecuritySettings]] — official docs on activating High-Security Settings
- [[t_EvalAdmOverrideAccLevel]] — official docs on evaluating the admin override at the access level
