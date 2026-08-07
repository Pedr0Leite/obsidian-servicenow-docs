---
title: "Prevent adding user to group if manager is inactive"
aliases:
  - Prevent adding user to group if manager is inactive
tags:
  - servicenow-dev-program
  - code-snippet
  - prevent-adding-user-to-group-if-manager-is-inactive
  - business-rules
---

# Prevent adding user to group

**Use case** : Whenever any user is getting added to any group, if the group manager is inactive then it should prevent the adding of user to the group

*info* : This method is to achieve the above use-case just with business rule

**Solution** : Create a `Before` business rule on `sys_user_grmember` table with `insert` checkbox checked. Follow the script present in [Script.js](https://github.com/ServiceNowDevProgram/code-snippets/blob/main/Business%20Rules/Prevent%20adding%20user%20to%20group%20if%20manager%20is%20inactive/Script.js)

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
