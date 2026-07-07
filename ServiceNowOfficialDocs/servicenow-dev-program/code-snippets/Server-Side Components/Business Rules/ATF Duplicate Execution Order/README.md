---
title: "ATF Duplicate Execution Order"
aliases:
  - ATF Duplicate Execution Order
tags:
  - servicenow-dev-program
  - code-snippet
  - atf-duplicate-execution-order
  - business-rules
---

Usage : Executes a business rule to find duplicate execution orders in ATF.
Executes on table sys_atf_test

The business rule consists of two main parts:

executeRule Function:
  Executes the business rule logic when a specific event occurs.
  It checks for duplicate execution orders within ATF and generates an error message if duplicates are found.

testDuplicateTestStepExectionOrder Function:
  A helper function responsible for identifying duplicate execution orders.
  Returns an array of active tests that contain at least two active test steps with the same execution order.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add woknotes for 75 percent SLA/README|Add woknotes for 75 percent SLA]]
