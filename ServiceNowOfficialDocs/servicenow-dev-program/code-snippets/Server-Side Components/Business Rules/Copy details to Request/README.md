---
title: "Copy details to Request"
aliases:
  - Copy details to Request
tags:
  - servicenow-dev-program
  - code-snippet
  - copy-details-to-request
  - business-rules
---

Script: Copy the Assignment group and Assign the details of sc_task to the Request table.

This script automates the process of assigning values from the first sc_task in a REQ to the parent REQ record. This is useful for keeping the request record in sync with its initial task(If multiple tasks are created for one request), allowing other workflows to use these values directly from the request.

Purpose of the Script:

End User Notification on Request Closure: When closing a service request, this script ensures that the Assignment Group and Assigned To details are copied to the REQ record, providing clarity for end users in the request closed notification. This is especially helpful to users who need to know who worked on their request.

Tracking in Survey Table: By maintaining the Assignment Group and Assigned To details on the REQ record, these details can be linked to surveys. This helps capture accurate data on the responsible group or individual when processing surveys and feedback, particularly if the survey process involves rewriting or transferring details.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
