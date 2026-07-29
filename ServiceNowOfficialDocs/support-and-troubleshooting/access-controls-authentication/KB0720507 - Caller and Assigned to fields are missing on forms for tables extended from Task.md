---
title: "Caller and Assigned to fields are missing on forms for tables extended from Task"
aliases:
  - KB0720507
tags:
  - servicenow
  - support-kb
  - acl
  - sys_user
  - reference-field
  - task
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0720507
kb_number: KB0720507
last_modified: 2024-04-07
---

## Caller and Assigned to fields are missing on forms for tables extended from Task

  

### Issue

# Symptoms

* * *

Caller and Assigned to fields are missing on forms for tables extended from Task

# Release

* * *

All

# Cause

* * *

The user is likely failing an ACL on 'sys\_user.name' which restricts them from seeing fields such as 'assigned\_to' and 'caller' that render 'sys\_user.name' as a value. (PFA)

# Resolution

* * *

Reconfigure the ACLs on 'sys\_user.name' to allow proper access to these records for your agents per your business requirements.

# Additional Information

* * *

You may need to clear the instance cache for the changes to take affect.

## Related

- [[KB0725874 - Reference Fields like 'Requestor', 'Assignment group', and 'Assigned to' that are referencing to sys_user, sys_user_grou]] - same root cause pattern (reference table ACL hides dependent fields)
- [[KB0746724 - Reference field is hidden from layout]]
- [[access-control-rules]] - official docs on ACL rule evaluation

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0725874 - Reference Fields like 'Requestor', 'Assignment group', and 'Assigned to' that are referencing to sys_user, sys_user_grou|Reference Fields like 'Requestor', 'Assignment group', and 'Assigned to' that are referencing to sys_user, sys_user_group are not available on the form.]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0688916 - When Vendor Core plugin is installed, unable to view assigned_to and caller_id fields on the incident form|When Vendor Core plugin is installed, unable to view assigned_to and caller_id fields on the incident form]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0717149 - Error message Record doesn't exist or ACL restricts the record retrieval appearing when ITIL users try to disallow notif|Error message \"Record doesn't exist or ACL restricts the record retrieval\" appearing when ITIL users try to disallow notifications]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0720034 - Non-role (ESS) users are not able to see group (sys_user_group) records|Non-role (ESS) users are not able to see group (sys_user_group) records]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0746724 - Reference field is hidden from layout|Reference field is hidden from layout ]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0748114 - Users see a No Matches Found on catalog item variable|Users see a \"No Matches Found\" on catalog item variable]]
