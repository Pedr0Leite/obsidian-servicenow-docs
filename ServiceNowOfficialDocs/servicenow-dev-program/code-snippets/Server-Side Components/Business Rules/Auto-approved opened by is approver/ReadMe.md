---
title: "Auto-approved opened by is approver"
aliases:
  - Auto-approved opened by is approver
tags:
  - servicenow-dev-program
  - code-snippet
  - auto-approved-opened-by-is-approver
  - business-rules
---

>**When a new Approval record (sysapproval_approver table) is created**

1. Create a Before Business Rule on the Approval (sysapproval_approver) table.

2. Check if the table of the record being approved is the Requested For table.

3. If it does:

	Verify whether the Approver (approver) is the same as the Opened by (opened_by) field on the related Requested For record.

	If both match:

		Automatically approve the approval record.

		Add appropriate approval comments (e.g., “Auto-approved since approver is the requestor (Opened By).”)

		Use setWorkflow(false) to prevent triggering additional workflows or business rules.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
