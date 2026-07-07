---
title: "Validate Checklist items"
aliases:
  - Validate Checklist items
tags:
  - servicenow-dev-program
  - code-snippet
  - validate-checklist-items
  - business-rules
---

A business rule that verifies all checklist items are completed before allowing the record to progress to the next status.

The business rule consists of three main parts:

Part A: Looks up all checklists (checklist table) tied to the current record (document = current.sys_id).

Part B: For each checklist, query the checklist_item records:

        Only items in that checklist.

        Only items that are not complete (complete = false).
        
Part C: If any incomplete items exist, an error message is displayed and the action is aborted.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
