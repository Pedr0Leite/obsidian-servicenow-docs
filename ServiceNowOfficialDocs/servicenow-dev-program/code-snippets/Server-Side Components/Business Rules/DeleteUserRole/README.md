---
title: "DeleteUserRole"
aliases:
  - DeleteUserRole
tags:
  - servicenow-dev-program
  - code-snippet
  - deleteuserrole
  - business-rules
---

Bussienss Rule to delete the User Role from table like 'Service Category User Roles [service_category_user_role]'
Steps:
 - Navigate to your instance 
 - Open Business Rule Table [sys_script] and click on New
 - Create After BR and provide below condition
 - When to Run
        - AFter
        - Order: 100
        - Operation: Delete
  - Provide the condition as:
   !current.user_role.nil()
  - Select Advance option and use the script

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
