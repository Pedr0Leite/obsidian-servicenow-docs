---
title: "Best Practices for Installing 'Explicit Roles' and 'High Security Settings' Plugins"
aliases:
  - KB0727017
tags:
  - servicenow
  - support-kb
  - explicit-roles
  - high-security-plugin
  - acl
  - contextual-security
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727017
kb_number: KB0727017
last_modified: 2026-01-13
---

## Issue

What Order should customer follow as best practice while installing 'Explicit Roles plugin' and 'The High Security Settings' plugins.

Although the plugins do not rely on each other, it is generally believed that the order of activation does not make a difference. However, our recommendation is to activate com.glide.high\_security first, then test it, and finally activate com.glide.explicit\_roles. The rationale behind this is that com.glide.high\_security implements a default-deny policy and generates/modifies extra ACLs.

Hence, if something stops working after its activation, it would be much easier to troubleshoot it without explicit roles.

Note:- Customer should do complete testing on their sub prod instances before implementing this on Production.

## Additional Information

-   High Security plugin is activated by default on all new instances. So installing this plugin first should not be problematic. 
-   Explicit Roles plugin requires "Contextual Security Rules" 
-   High Security plugin requires "Contextual Security: Role Management"

## Related

- [[KB0749268 - GlideRecord query on a specific table is not working for non-role (end user) user]] - Explicit Roles plugin state affecting GlideRecord queries
- [[KB0713543 - Admins have limited access to modules, tables, etc. (even though the ACLs are set in place, they fail)]] - High Security plugin elevated privilege interaction
- [[sc-high-security-plugin]] - official security hardening check for the High Security plugin
- [[sc-enable-explicit-roles-internal-denylist]] - official security hardening check for Explicit Roles

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0713543 - Admins have limited access to modules, tables, etc. (even though the ACLs are set in place, they fail)|Admins have limited access to modules, tables, etc. (even though the ACLs are set in place, they fail)]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow|How Access Control List (ACL) evaluation works in ServiceNow]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0656366 - Relationship between Business Rules and Access Control Rules (ACLs)|Relationship between Business Rules and Access Control Rules (ACLs)]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0686244 - When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window show|When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window shows an error Failed API level ACL Validation]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0688916 - When Vendor Core plugin is installed, unable to view assigned_to and caller_id fields on the incident form|When Vendor Core plugin is installed, unable to view assigned_to and caller_id fields on the incident form]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0688981 - Certain users are unable to sc_cat_item_producer records in Service Portal|Certain users are unable to sc_cat_item_producer records in Service Portal ]]
