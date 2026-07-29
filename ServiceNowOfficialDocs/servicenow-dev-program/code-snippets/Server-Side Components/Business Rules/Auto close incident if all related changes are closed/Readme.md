---
title: "Auto close incident if all related changes are closed"
aliases:
  - Auto close incident if all related changes are closed
tags:
  - servicenow-dev-program
  - code-snippet
  - auto-close-incident-if-all-related-changes-are-closed
  - business-rules
---

Business Rule: Auto-Close Incident When All Related Changes Are Closed
Table : change_request
When to Run: After update
Condition: state changes to Closed (or your equivalent "Closed" state number, e.g. state == 3)

Detailed Working
1. Trigger Point
This After Business Rule runs after a Change Request record is updated.
Specifically, it checks when the state changes to “Closed”.

2. Check for Related Incident
The script retrieves the incident reference field (incident) from the current change request.
If there’s no linked incident, it skips execution.

3. Check for Any Remaining Open Change Requests
A new GlideRecord query checks for other Change Requests linked to the same incident where:
If any such records exist, it means not all change requests are closed — so the incident remains open.

4. Close the Incident Automatically
If no open Change Requests remain, the script:
Fetches the linked incident.
Sets:	state = 7 (Closed)
	close_code = Auto Closed
	close_notes = Auto closure as all changes are closed.
Updates the record.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
