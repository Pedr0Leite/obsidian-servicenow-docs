---
title: "Customization considerations for Access Controls (ACLs)"
aliases:
  - KB0749174
tags:
  - servicenow
  - support-kb
  - acl
  - access-control-list
  - customization
  - upgrade
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749174
kb_number: KB0749174
last_modified: 2025-11-11
---

## Issue

When you want to make changes to access controls (ACLs) there are some things to be aware of.

This article discusses those considerations and how to best approach them.

## Resolution

To begin with, it is important to remember that for any given operation (read, write, delete, etc), the user in question is only required to pass one ACL for that particular record or field security evaluation. This has a couple of impacts on administrators who want to tighten or loosen security. 

When you need to make access more restrictive you can create your own access control(s) and then disable the existing ones that are in place by setting active to false in those ACLs. This will allow administrators to tighten the level of security for a particular operation on a table without having to edit each access control and add additional security. By creating a new custom ACL you ensure that if an upgrade were to alter one or more of the out of box access controls it would not affect you since you will have disabled those ACLs and then will be marked as having been changed and therefore not be replaced with the newer version of the ACL from the upgrade.

When you want to loosen security or add access to additional users/groups/roles it is recommended that you create a new ACL that grants the desired access. This will ensure your ACL will not change when an upgrade occurs since only out of box objects would be potentially impacted by an upgrade. Since access controls only require one passing ACL for the table and one passing ACL for the field level access your new ACL(s) will be all that is necessary to enable access for the desired users.

If you do rely on existing out of box access controls please do be aware that these may change on upgrade and can alter the way the table security will work for users. Even if you change an out-of-box access control keep in mind that the roles of that ACL are stored in a separate table. The ACL is stored in sys\_security\_acl but the associated roles are stored in sys\_security\_acl\_role. For this reason, it is possible that an out of box ACL that you customized can have roles added/removed as part of the upgrade since they live in a separate table and would not be prohibited based on sys\_update\_xml records for changes to the parent ACL.

## Additional Information

[Access Control List Rules](https://docs.servicenow.com/bundle/vancouver-platform-security/page/administer/contextual-security/concept/access-control-rules.html "Access Control List Rules")

[ACL rule types](https://docs.servicenow.com/bundle/vancouver-platform-security/page/administer/contextual-security/concept/acl-rule-types.html "ACL rule types")

[ACL debugging tools](https://docs.servicenow.com/bundle/vancouver-platform-security/page/administer/contextual-security/concept/c_AccessControlRulesDebug.html "ACL debugging tools")

## Related

- [[KB0695387 - For users with the itil, catalog, or approval_admin role, when they attempt to access the My Approvals module, they get ]]
- [[KB0718052 - Non-admin users unable to viewedit assignment groups and assignment rules]]
- [[KB0721299 - Additional Comments field missing for Watch List users]]
- [[KB0727211 - FAQ Can an ACL work on the list view and be bypassed on the related list (or vice versa)]]
- [[access-control-rules]] - official docs on ACL rule evaluation
- [[c_AccessControlRulesDebug]] - official ACL debugging tools docs
- [[acl-rule-types]] - official docs on ACL rule types

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538769 - Determining if SAML issues are occurring due to customer scripts no longer working after upgrade|Determining if SAML issues are occurring due to customer scripts no longer working after upgrade]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0695387 - For users with the itil, catalog, or approval_admin role, when they attempt to access the My Approvals module, they get |For users with the itil, catalog, or approval_admin role, when they attempt to access the My Approvals module, they get message Security constraints prevent access to requested page]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538786 - Determining if the user has an older version of SAML|Determining if the user has an older version of SAML]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow|How Access Control List (ACL) evaluation works in ServiceNow]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0656366 - Relationship between Business Rules and Access Control Rules (ACLs)|Relationship between Business Rules and Access Control Rules (ACLs)]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0686244 - When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window show|When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window shows an error Failed API level ACL Validation]]
