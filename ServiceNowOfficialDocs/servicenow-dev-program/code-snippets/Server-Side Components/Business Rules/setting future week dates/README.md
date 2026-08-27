---
title: "setting future week dates"
aliases:
  - setting future week dates
tags:
  - servicenow-dev-program
  - code-snippet
  - setting-future-week-dates
  - business-rules
---

So the script "setting future week dates" is used to set a date field on a record to a future value and use that to trigger reminders to end users
or external customers. 

The script addresses the use case where the first reminder is expected to be sent 14 days from case create and the rest of the reminders every 3 days, and should be sent only on weekdays.

If the future computed date falls on a Sat 2 days are added, and if it falls on a Sunday 1 day is added.

Using this process a flow can be run each day to scan all the case records that have a notification date for the current day and a notification be sent
to the case contact.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
