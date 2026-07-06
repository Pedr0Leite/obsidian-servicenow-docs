---
title: "Reference Fields in a form are not visible if the user does not have read access on the Referenced table's record/display field"
aliases:
  - KB0785309
tags:
  - servicenow
  - support-kb
  - acl
  - reference-fields
  - dot-walking
  - display-field
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0785309
kb_number: KB0785309
last_modified: 2024-04-08
---

## Reference Fields in a form are not visible if the user does not have read access on the Referenced table's record/display field

  

### Issue

Reference Fields in a form are not visible if the user does not have read access on the Referenced table's record/display field. For example: if a form contain the field "cpu\_manufacturer", the field will not be visible if the user does not have read access to the "core\_company" table

### Release

All release

### Cause

User does not have read access to the Referenced table's record/display field

### Resolution

User needs to have read access to the referenced table's record/display field.

## Related

- [[KB0755717 - Non-itil users cannot see a read-only field on the catalog task which is extended from the request table.]] — same dot-walk/reference read-access pattern
- [[KB0759218 - Certain fields are visible to non-admin users only when the fields not empty.]] — related reference-row-check ACL behavior
- [[r_ContScriptCondAppRefFld]] — official docs on applying ACL script conditions to reference fields

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0755717 - Non-itil users cannot see a read-only field on the catalog task which is extended from the request table.|Non-itil users cannot see a read-only field on the catalog task which is extended from the request table.]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0759218 - Certain fields are visible to non-admin users only when the fields not empty.|Certain fields are visible to non-admin users only when the fields not empty.]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow|How Access Control List (ACL) evaluation works in ServiceNow]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0656366 - Relationship between Business Rules and Access Control Rules (ACLs)|Relationship between Business Rules and Access Control Rules (ACLs)]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0686244 - When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window show|When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window shows an error Failed API level ACL Validation]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0688916 - When Vendor Core plugin is installed, unable to view assigned_to and caller_id fields on the incident form|When Vendor Core plugin is installed, unable to view assigned_to and caller_id fields on the incident form]]
