---
title: "How Access Control List (ACL) evaluation works in ServiceNow"
aliases:
  - KB0541355
tags:
  - servicenow
  - support-kb
  - acl
  - access-control
  - roles
  - security
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0541355
kb_number: KB0541355
last_modified: 2026-04-30
---

## How Access Control List (ACL) evaluation works in ServiceNow

  

### Issue

Access Control List (ACL) configuration can produce unexpected results when the evaluation order is not well understood. This article explains how ServiceNow evaluates ACLs using a two-gate system—table-level access checked before field-level access—and describes how to configure ACLs to avoid common access issues.

### Symptoms

-   Users are unexpectedly denied or granted access to fields despite ACLs being in place
-   Field-level ACLs appear to be ignored even when defined
-   Admin override behavior is inconsistent or does not work
-   Dot-walked fields do not display correctly in list views

### Facts

-   ACLs must pass all three checks: roles, condition, and script
-   Table-level ACLs must be in place before field-level ACLs are evaluated
-   The Admin Overrides check box must be selected consistently across all ACLs in the chain for the override to apply
-   List views do not load all columns by default; only visible fields are retrieved

### Release

All supported releases. Behavior confirmed as of the Yokohama release.

### Cause

When the ACL evaluation order is not correctly understood, security rules may be configured incorrectly, resulting in unexpected access denials or overly permissive behavior.

### Resolution

ServiceNow uses a two-gate ACL evaluation system. Table-level access is evaluated first (Gate 1), followed by field-level access (Gate 2).

**Gate 1: Table-level ACLs**

Table-level ACLs determine whether the user can access the record. These ACLs have the following attributes:

-   ACL Name: table
-   Field: --None--
-   Type: record

If no matching table-level ACL is found, the system checks the parent table. If no parent table ACL exists, the system falls back to a wildcard (`*`) rule.

**Gate 2: Field-level ACLs**

After the user passes the table-level check, field-level ACLs control access to specific fields. These ACLs have the following attributes:

-   ACL Name: table.field
-   Type: record

![incident\_record\_read.png](sys_attachment.do?sys_id=f5d4fc8a47204f14b7832920326d4389 "Record Read")

The system evaluates field-level ACLs in the following order:

1.  table.field
2.  parent\_table.field
3.  table.\*
4.  parent\_table.\*
5.  \*.\*

**Admin overrides**

If the Admin Overrides check box is selected on all relevant ACLs in the evaluation chain, users with the admin role bypass ACL conditions. If any ACL in the chain does not have this setting selected, the admin override does not apply.

**List view considerations**

Field ACLs that reference other fields through dot-walking require the referenced field to be visible in the list view and placed before the evaluated field in the column order.

### Related Links

-   [ACL debugging tools](https://docs.servicenow.com/csh?topicname=c_AccessControlRulesDebug.html&version=latest)
-   [Customization Considerations for Access Controls (ACLs)](https://support.servicenow.com/kb_view.do?sysparm_article=KB0749174 "KB0749174 - Customization Considerations for Access Controls (ACLs)")
-   [Access control list rules](https://docs.servicenow.com/csh?version=latest&topicname=access-control-rules.html "Access control list rules")

## Related

- [[KB0749738 - SLA Definition field value is not displaying on task sla list or related lists for some users]] — real-world example of a table-level read ACL blocking a field
- [[KB0753582 - The non-admin users are not able to access to a table]] — table ACL rule matching order (table, parent table, wildcard)
- [[KB0816018 - Admin role does not pass an ACL when Admin Overrides is selected]] — Admin Overrides must be consistent across all ACLs in the chain
- [[KB0656366 - Relationship between Business Rules and Access Control Rules (ACLs)]]
- [[KB0685046 -  How the Admin overrides option works in an access control (ACL) rule]]
- [[KB0691976 - The users with SOAP role not able to view the incident table data even though the ACLs return true.]]
- [[KB0691989 - Ui ActionButton does not display for a user even when the ACLs and the UI action conditions grant the access to that use]]
- [[access-control-rules]] - official docs on access control rules
- [[permission-evaluation]] - official docs on permission evaluation order

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0656366 - Relationship between Business Rules and Access Control Rules (ACLs)|Relationship between Business Rules and Access Control Rules (ACLs)]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0686244 - When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window show|When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window shows an error Failed API level ACL Validation]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0691989 - Ui ActionButton does not display for a user even when the ACLs and the UI action conditions grant the access to that use|Ui Action/Button does not display for a user even when the ACLs and the UI action conditions grant the access to that user]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0687701 - Admin user is being asked to elevate to admin role after logging in|Admin user is being asked to elevate to \"admin\" role after logging in]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0688916 - When Vendor Core plugin is installed, unable to view assigned_to and caller_id fields on the incident form|When Vendor Core plugin is installed, unable to view assigned_to and caller_id fields on the incident form]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0688981 - Certain users are unable to sc_cat_item_producer records in Service Portal|Certain users are unable to sc_cat_item_producer records in Service Portal ]]
