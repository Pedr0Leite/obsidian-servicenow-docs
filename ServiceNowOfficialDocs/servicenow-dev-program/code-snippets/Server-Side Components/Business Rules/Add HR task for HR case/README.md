---
title: "Add HR task for HR case"
aliases:
  - Add HR task for HR case
tags:
  - servicenow-dev-program
  - code-snippet
  - add-hr-task-for-hr-case
  - business-rules
---

This business rule is configured to run after a record is inserted in the sn_hr_core_case table (which is parent table for HR cases). 
with conditions subjcet person is VIP and when a case priority is high.

we are simply checking the conditions at the script level. (this can be checked at the condition level as well.)
and creating hr task 

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add woknotes for 75 percent SLA/README|Add woknotes for 75 percent SLA]]
