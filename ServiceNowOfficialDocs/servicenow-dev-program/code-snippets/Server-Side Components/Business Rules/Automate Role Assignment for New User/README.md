---
title: "Automate Role Assignment for New User"
aliases:
  - Automate Role Assignment for New User
tags:
  - servicenow-dev-program
  - code-snippet
  - automate-role-assignment-for-new-user
  - business-rules
---

# Overview
This snippet for ServiceNow developers automate the process of assigning roles to users based on their department. It helps to simplify user role management, especially useful in organizations where specific departments require predefined access levels. 

# How It Works
In Business Rule settings within ServiceNow: 
- Trigger: runs the script "before" an update to the `sys_user` table when a user’s department changes.
- Condition: Only triggers when `current.department.changes()` - ensures that the script only runs when the department field is modified.
- Role Mapping: Uses the `rolesByDepartment` dictionary to assign roles based on the user’s department.
    
# Implementation

Edit `rolesByDepartment` to match your organization’s needs.

```
var rolesByDepartment = {
        <department_name> : [role_1, role_2]
    };
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
