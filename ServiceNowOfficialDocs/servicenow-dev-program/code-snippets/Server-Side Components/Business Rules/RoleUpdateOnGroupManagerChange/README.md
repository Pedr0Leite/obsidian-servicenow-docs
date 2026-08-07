---
title: "RoleUpdateOnGroupManagerChange"
aliases:
  - RoleUpdateOnGroupManagerChange
tags:
  - servicenow-dev-program
  - code-snippet
  - roleupdateongroupmanagerchange
  - business-rules
---

This business rule will update the group manager role on group manager change on Insert, Update, Delete
Steps:
  1. When new manager is updated from for the current group
  2. Current role of the manager will be updated and removed
  3. New Manager detail provided will be validated and it will assign the role to new manager 
  4. Configuration Details:
    - When to run:
        - After
        - Order:100
        - Operation: Insert, Update, Delete
     - Condition:
          current.manager.changes() || current.operation() == "delete"
     - Table: Group [sys_user_group]

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
