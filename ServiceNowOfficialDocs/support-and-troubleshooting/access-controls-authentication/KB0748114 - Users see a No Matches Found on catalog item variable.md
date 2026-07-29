---
title: "Users see a \"No Matches Found\" on catalog item variable"
aliases:
  - KB0748114
tags:
  - servicenow
  - support-kb
  - acl
  - service-catalog
  - catalog-variable
  - reference-field
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748114
kb_number: KB0748114
last_modified: 2024-04-07
---

## Users see a "No Matches Found" on catalog item variable

  

### Issue

Users see a "No Matches Found" message on Service catalog variable

### Release

Service Catalog

### Cause

User does not have read access to the table being referenced

### Resolution

Provide read access to the table the variable is referencing

## Related

- [[KB0746724 - Reference field is hidden from layout]]
- [[KB0720034 - Non-role (ESS) users are not able to see group (sys_user_group) records]]
- [[KB0746144 - Users do not see ticket information after ordering a catalog item]]
- [[access-control-rules]] - official docs on ACL rule evaluation

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0720034 - Non-role (ESS) users are not able to see group (sys_user_group) records|Non-role (ESS) users are not able to see group (sys_user_group) records]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0720507 - Caller and Assigned to fields are missing on forms for tables extended from Task|Caller and Assigned to fields are missing on forms for tables extended from Task]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0725874 - Reference Fields like 'Requestor', 'Assignment group', and 'Assigned to' that are referencing to sys_user, sys_user_grou|Reference Fields like 'Requestor', 'Assignment group', and 'Assigned to' that are referencing to sys_user, sys_user_group are not available on the form.]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0746144 - Users do not see ticket information after ordering a catalog item|Users do not see ticket information after ordering a catalog item]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0746724 - Reference field is hidden from layout|Reference field is hidden from layout ]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow|How Access Control List (ACL) evaluation works in ServiceNow]]
