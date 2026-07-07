---
title: "Captures the time it took to assign a task"
aliases:
  - Captures the time it took to assign a task
tags:
  - servicenow-dev-program
  - code-snippet
  - captures-the-time-it-took-to-assign-a-task
  - business-rules
---

This script tracks the time it took to assign a task (like an Incident, Change, etc.) by calculating the difference
between when the record was created and when it was assigned (assigned_to was set).
It checks if the assigned_to field has changed and is not empty.
If it's the first time the record is being assigned (u_assignment_time is empty), it captures the current time.
It then calculates the time difference between when the record was created and when it was assigned.
This time difference (in minutes) is stored in a custom field u_time_to_assign.
The goal is to track how long it took for the record to be assigned after creation


## While this is possible to do via Metrics in ServiceNow (https://www.servicenow.com/docs/bundle/xanadu-platform-administration/page/use/reporting/concept/c_SampleFieldValueDurationScript.html), 
## the script is being provided to potentially solve some edge cases.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
