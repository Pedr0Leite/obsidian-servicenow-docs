---
title: "Non-itil users cannot see a read-only field on the catalog task which is extended from the request table."
aliases:
  - KB0755717
tags:
  - servicenow
  - support-kb
  - acl
  - dot-walking
  - reference-fields
  - catalog-task
  - table-acl
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0755717
kb_number: KB0755717
last_modified: 2024-04-07
---

## Non-itil users cannot see a read-only field on the catalog task which is extended from the request table.

  

### Issue

Non-itil users cannot see a read-only field on the catalog task which is extended from the request table.

### Cause

If users do not have read access to the table that is being dot-walked to, then they will not be able to see the extended field either.

### Resolution

Create a read access ACL at the table level that will provide access to non itil users.

### Related Links

When creating  this read access ACL at table level don't use an asterisk (\*) for the field option because that will still be considered as field level access, instead leave the field choice as --None-- and just choose the table you are applying it to.

## Related

- [[KB0785309 - Reference Fields in a form are not visible if the user does not have read access on the Referenced table's recorddisplay]] — same dot-walk/reference read-access root cause
- [[KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow]] — explains why dot-walked fields require read access on the referenced table
- [[acl-rule-types]] — official docs distinguishing table-level vs field-level ACLs

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0785309 - Reference Fields in a form are not visible if the user does not have read access on the Referenced table's recorddisplay|Reference Fields in a form are not visible if the user does not have read access on the Referenced table's record/display field]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0753582 - The non-admin users are not able to access to a table|The non-admin users are not able to access to a table]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0759218 - Certain fields are visible to non-admin users only when the fields not empty.|Certain fields are visible to non-admin users only when the fields not empty.]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0813250 - User with no read access to a Table see a blank form instead of a security message (Security constraints prevent access |User with no read access to a Table see a blank form instead of a security message (Security constraints prevent access to requested page)]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow|How Access Control List (ACL) evaluation works in ServiceNow]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0656366 - Relationship between Business Rules and Access Control Rules (ACLs)|Relationship between Business Rules and Access Control Rules (ACLs)]]
