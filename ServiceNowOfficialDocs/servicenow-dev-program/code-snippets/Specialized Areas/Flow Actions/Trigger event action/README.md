---
title: "Trigger event action"
aliases:
  - Trigger event action
tags:
  - servicenow-dev-program
  - code-snippet
  - trigger-event-action
  - flow-actions
---

Useful for tasks like triggering notifications or to trigger asynchronous script actions from a flow. 

This flow action triggers the passed in event with optional parameters. Will work for most scenarios as the event record is passed in as a Document ID input.

Inputs:

event_name		- Reference.Event Record - Mandatory

event_record	- Document ID            - Mandatory

parm1					- String 

parm2					- String

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Add signature and update fields to a fillable PDF document/README|Add signature and update fields to a fillable PDF document]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Adhoc Assessment Generator Flow Action/README|Adhoc Assessment Generator Flow Action]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Assign Role/README|Assign Role]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Calculate Ticket Age/README|Calculate Ticket Age]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Check MID Server Availability/README|Check MID Server Availability]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Create Student Weekday Pickup Schedule/README|Create Student Weekday Pickup Schedule]]
