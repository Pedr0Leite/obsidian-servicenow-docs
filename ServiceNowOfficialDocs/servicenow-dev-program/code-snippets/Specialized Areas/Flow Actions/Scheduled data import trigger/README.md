---
title: "Scheduled data import trigger"
aliases:
  - Scheduled data import trigger
tags:
  - servicenow-dev-program
  - code-snippet
  - scheduled-data-import-trigger
  - flow-actions
---

This action script will execute the scheduled import via a flow action.

Inputs are  - 'importSet'  - the sys_id of the scheduled import set  - mandatory

Outputs are - 'returnerror'- true if no import set found             - mandatory

We found this useful when triggering a data import from a catalog item. User attaches the import file to catalog item and submit, which triggers flow, which then
had this action to import the file using the right import set.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Add signature and update fields to a fillable PDF document/README|Add signature and update fields to a fillable PDF document]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Adhoc Assessment Generator Flow Action/README|Adhoc Assessment Generator Flow Action]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Assign Role/README|Assign Role]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Calculate Ticket Age/README|Calculate Ticket Age]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Check MID Server Availability/README|Check MID Server Availability]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Create Student Weekday Pickup Schedule/README|Create Student Weekday Pickup Schedule]]
