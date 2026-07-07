---
title: "Automatically Throttle Incidents Raised by Same User Within Short Timeframe"
aliases:
  - Automatically Throttle Incidents Raised by Same User Within Short Timeframe
tags:
  - servicenow-dev-program
  - code-snippet
  - automatically-throttle-incidents-raised-by-same-user-within-short-timeframe
  - business-rules
---

This business rule prevents users from submitting too many incidents in a short time, acting as a rate-limiting mechanism to reduce spam or misuse of the incident form.

What It Does:
-Checks how many incidents the same caller has submitted in the last 10 minutes.
-If the number of incidents is 3 or more, the rule:
-Blocks the current incident from being submitted.
-Displays an error message:
"You have submitted too many incidents in a short time. Please wait before submitting more."

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
