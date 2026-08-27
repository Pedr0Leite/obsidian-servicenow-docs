---
title: "Auto Create Problem Records for Recurring Incidents"
aliases:
  - Auto Create Problem Records for Recurring Incidents
tags:
  - servicenow-dev-program
  - code-snippet
  - auto-create-problem-records-for-recurring-incidents
  - business-rules
---

This "after" business rule automatically creates a Problem record when a particular Configuration Item (CI) has had 5 or more incidents in the last 24 hours, and no open Problem already exists for that CI.
This helps in proactive problem management, aiming to address recurring issues.
Here’s the working of the code explained:

 - Check if CI is present in the current Incident (current.cmdb_ci).
 - Count incidents created in the last 24 hours for the same CI using GlideAggregate.

If 5 or more incidents are found for that CI:
 - Query the Problem table to check if an open Problem (not closed) already exists for that CI.
 - If no open Problem exists, create a new Problem record with: The same CI, A predefined short description And set its state to New (1).
 - Log a message indicating that a Problem has been created.
This automates Problem creation for frequent incidents on the same CI.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
