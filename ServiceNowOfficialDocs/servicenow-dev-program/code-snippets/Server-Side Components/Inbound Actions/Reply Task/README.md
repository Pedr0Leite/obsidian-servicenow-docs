---
title: "Reply Task"
aliases:
  - Reply Task
tags:
  - servicenow-dev-program
  - code-snippet
  - reply-task
  - inbound-actions
---

#contribution

An SC Task is assigned to the requester. When the requester replies with the following format:

Are you good to proceed? Yes
Date: 20-10-2025

…the reply information is automatically extracted and populated into custom fields on the SC Task record.

Two custom fields have been created for this purpose:

Date:20/10/2025

Process: Yes

Inbound Email Action:
---------------------
Created Reply Inbound email action on sc_task table.
Table - sc_task
Type - Reply
Condition - Subject : has been assigned for Satiesfiction.

Objective of the code:
-----------------------

When a requester replies to an SC Task email with specific text (like "Are you good to Processed? Yes" and "Date: 2025-10-20"), this script:

Updates task comments with the reply
Uses regex to search for date and tries to extract a Yes/No response from a line like:

Are you good to proceed? Yes
Date: 20-10-2025

Populates two custom fied the SC Task (u_date, u_processed)

Sets the task's state to 3 (Completed) once reply done & extract and auto population performed.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Inbound Actions/Advanced Scripts/README|Advanced Scripts]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Inbound Actions/Auto Incident Creation from Case Email/README|Auto Incident Creation from Case Email]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Inbound Actions/Auto Reply Email/README|Auto Reply Email]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Inbound Actions/Automate creation of incidents through inbound actions/README|Automate creation of incidents through inbound actions]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Inbound Actions/Duplicate Incident Detection and Creation/README|Duplicate Incident Detection and Creation]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Inbound Actions/Email Text as Attachment/README|Email Text as Attachment]]
