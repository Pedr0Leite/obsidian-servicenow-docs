---
title: "Reference field is hidden from layout "
aliases:
  - KB0746724
tags:
  - servicenow
  - support-kb
  - acl
  - reference-field
  - form-layout
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0746724
kb_number: KB0746724
last_modified: 2024-04-07
---

## Reference field is hidden from layout

  

### Issue

# Overview

A reference field can be hidden in form layout even though the ACLs on that reference field allow read access.

# Reference Table ACL

If the read ACL on the reference table prevents the access, then the field becomes hidden in form layout. 

# Example

-   Go to any incident with an itil-user. Make sure the Company field is visible.
-   Create a read ACL on core\_company table and allow access for only admin-role users. (Make sure this is the only read ACL on core\_company)
-   Go to any incident with an itil-user again. The Company field is no longer visible.

# Additional Information

Applicable in all versions

## Related

- [[KB0725874 - Reference Fields like 'Requestor', 'Assignment group', and 'Assigned to' that are referencing to sys_user, sys_user_grou]] - same reference-table ACL mechanism
- [[KB0720507 - Caller and Assigned to fields are missing on forms for tables extended from Task]]
- [[KB0748114 - Users see a No Matches Found on catalog item variable]]
- [[access-control-rules]] - official docs on ACL rule evaluation

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0720034 - Non-role (ESS) users are not able to see group (sys_user_group) records|Non-role (ESS) users are not able to see group (sys_user_group) records]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0720507 - Caller and Assigned to fields are missing on forms for tables extended from Task|Caller and Assigned to fields are missing on forms for tables extended from Task]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0725874 - Reference Fields like 'Requestor', 'Assignment group', and 'Assigned to' that are referencing to sys_user, sys_user_grou|Reference Fields like 'Requestor', 'Assignment group', and 'Assigned to' that are referencing to sys_user, sys_user_group are not available on the form.]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0748114 - Users see a No Matches Found on catalog item variable|Users see a \"No Matches Found\" on catalog item variable]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow|How Access Control List (ACL) evaluation works in ServiceNow]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0656366 - Relationship between Business Rules and Access Control Rules (ACLs)|Relationship between Business Rules and Access Control Rules (ACLs)]]
