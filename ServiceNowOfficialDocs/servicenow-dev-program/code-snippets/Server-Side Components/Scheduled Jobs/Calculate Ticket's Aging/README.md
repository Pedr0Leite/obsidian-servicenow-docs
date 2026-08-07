---
title: "Calculate Ticket's Aging"
aliases:
  - Calculate Ticket's Aging
tags:
  - servicenow-dev-program
  - code-snippet
  - calculate-tickets-aging
  - scheduled-jobs
---

This script helps is calculating the aging of the ticket/cases and define them in bucket of category aging like '0-2 Days','3-4 Days'
Based on this you can get the reporting on cases aging. How old is the case. It calculates the aging from the creation date.

It works on all cases except the cases which are on resolved,cancelled and closed state.
With this script you can decide whether to show that case in red/orange or yellow colour so that agent will know just by seeing the case
that aging has increased. So if aging is greater than 30 we can make the case highlighted as red by using field styles conditions.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/API Token Expiry Warning/Readme|API Token Expiry Warning]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Approval Reminder/README|Approval Reminder]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto Disable account/Readme|Auto Disable account]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto close changes requests updated 30 days prior/README|Auto close changes requests updated 30 days prior]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto upgrade store applications/Readme|Auto upgrade store applications]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto-Assign Unassigned Incidents Older Than 30 Minutes/Readme|Auto-Assign Unassigned Incidents Older Than 30 Minutes]]
