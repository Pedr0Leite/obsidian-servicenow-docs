---
title: "Sync Integer Field"
aliases:
  - Sync Integer Field
tags:
  - servicenow-dev-program
  - code-snippet
  - sync-integer-field
  - business-rules
---

Scenario: Synchronize integer field that will put records in sequential order.

Example: When you have an integer field on a table and want to be able to add records and have it rearrange order its order sequentially.

Script Logic: An before-update business rule that grabs all the records that currently have an integer field value and puts them into an array. It then adds the new value and puts it into the correct position in the array and updates value so they are in a sequence order.

**You will have to create a custom integer field to be able to use this business rule.**

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
