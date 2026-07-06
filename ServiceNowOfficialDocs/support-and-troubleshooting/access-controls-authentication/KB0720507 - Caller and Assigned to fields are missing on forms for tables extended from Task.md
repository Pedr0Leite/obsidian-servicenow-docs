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
