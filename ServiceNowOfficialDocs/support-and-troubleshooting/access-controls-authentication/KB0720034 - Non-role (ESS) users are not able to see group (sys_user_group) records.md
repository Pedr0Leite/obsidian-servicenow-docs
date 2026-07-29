---
title: "Non-role (ESS) users are not able to see group (sys_user_group) records"
aliases:
  - KB0720034
tags:
  - servicenow
  - support-kb
  - acl
  - sys_user_group
  - ess
  - reference-field
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0720034
kb_number: KB0720034
last_modified: 2024-01-28
---

## Non-role (ESS) users are not able to see group (sys\_user\_group) records

  

### Issue

# Symptoms

* * *

Non-role (ESS) users are not able to see group (sys\_user\_group) records when trying to select a group from any fields or variables that reference the group (sys\_user\_group) table.

# Release

* * *

All releases

# Cause

* * *

The users are failing the table level read ACL on sys\_user\_group table.

The OOB ACL: /sys\_security\_acl.do?sys\_id=811f2ddec0a801666be07f00f34794c7

# Resolution

* * *

The OOB ACL checks for:

-   If the group has the admin role attached to it. If yes, then only users with admin role can view that group
-   If the group has the security\_admin role attached to it. If yes, then only users with security\_admin role can view that group
-   Otherwise, if the group doesn't have any of the roles above and if the user has any roles in the instance then grant that user read access to the group record

The OOB ACL can be modified as appropriate to grant non-role users access, or a new similar ACL can be created altogether for the same requirement.

# Additional Information

* * *

[Access control list rules](https://docs.servicenow.com/csh?topicname=access-control-rules.html&version=latest "Access control list rules")

## Related

- [[KB0725874 - Reference Fields like 'Requestor', 'Assignment group', and 'Assigned to' that are referencing to sys_user, sys_user_grou]] - same sys_user_group ACL root cause blocking reference fields
- [[KB0748114 - Users see a No Matches Found on catalog item variable]]
- [[access-control-rules]] - official docs on ACL rule evaluation

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0725874 - Reference Fields like 'Requestor', 'Assignment group', and 'Assigned to' that are referencing to sys_user, sys_user_grou|Reference Fields like 'Requestor', 'Assignment group', and 'Assigned to' that are referencing to sys_user, sys_user_group are not available on the form.]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0720507 - Caller and Assigned to fields are missing on forms for tables extended from Task|Caller and Assigned to fields are missing on forms for tables extended from Task]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0746724 - Reference field is hidden from layout|Reference field is hidden from layout ]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0748114 - Users see a No Matches Found on catalog item variable|Users see a \"No Matches Found\" on catalog item variable]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow|How Access Control List (ACL) evaluation works in ServiceNow]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0656366 - Relationship between Business Rules and Access Control Rules (ACLs)|Relationship between Business Rules and Access Control Rules (ACLs)]]
