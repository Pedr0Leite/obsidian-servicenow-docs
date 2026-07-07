---
title: "Dynamic Business Rule to Update User Roles Based on Department Changes"
aliases:
  - Dynamic Business Rule to Update User Roles Based on Department Changes
tags:
  - servicenow-dev-program
  - code-snippet
  - dynamic-business-rule-to-update-user-roles-based-on-department-changes
  - business-rules
---

**Purpose**

This business rule automatically updates user roles in ServiceNow whenever a user's department changes. By ensuring that users have the appropriate roles based on their current department, the rule helps maintain data integrity and enhances access control within the organization.



**Complete Business Rule Configuration**

**Name**: "Update User Roles Based on Department Changes"

**Table**: sys_user

**When**: Before

**Insert**: Checked

**Update**: Checked


**Condition**:

**javascript**

'''current.department.changes();'''

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
