---
title: "Synchronize RITM comments to Active tasks"
aliases:
  - Synchronize RITM comments to Active tasks
tags:
  - servicenow-dev-program
  - code-snippet
  - synchronize-ritm-comments-to-active-tasks
  - business-rules
---

This is an Async Update Business rule written on the Requested Item table.
This code works as a comment synchronization mechanism.

What the code does:
-Comment is added to the parent record(which in this case is a Requested Item)
-Creates an HTML link to the parent record using its number.
-Queries and finds all active SCTASKs associated with the Reuqested item.
-Loops through each SCTASK, adds the copied comment along with a link to the Requested Item.

Let's explain with an example:

RITM: RITM001001
Task 1: SCTASK001001
Task 2: SCTASK001002
-User adds new comment into the RITM: 'This is a test comment.'
-Record link is created and stored inside a clickable RITM number.
-The RITM comment is updated on both the SCTASKs with the comment looking like:
 
    Updated comments on: [RITM001001]
    This is a test comment.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
