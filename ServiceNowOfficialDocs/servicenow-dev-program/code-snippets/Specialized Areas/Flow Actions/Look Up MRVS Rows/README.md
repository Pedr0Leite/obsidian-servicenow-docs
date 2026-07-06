---
title: "Look Up MRVS Rows"
aliases:
  - Look Up MRVS Rows
tags:
  - servicenow-dev-program
  - code-snippet
  - look-up-mrvs-rows
  - flow-actions
---

## Overview
To be used within an action to retrieve the unique **Row indexes** for each row within a MRVS

## Inputs
Pass in the sys_id of the record the MRVS is associated with.  E.g., the sys_id of a RITM record.

## Script Step
Create a script step with the code provided to look up each unique **Row index** associated with the MRVS

## Outputs
Returns an array of strings with each string representing the **Row index**

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Add signature and update fields to a fillable PDF document/README|Add signature and update fields to a fillable PDF document]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Adhoc Assessment Generator Flow Action/README|Adhoc Assessment Generator Flow Action]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Assign Role/README|Assign Role]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Calculate Ticket Age/README|Calculate Ticket Age]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Check MID Server Availability/README|Check MID Server Availability]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Create Student Weekday Pickup Schedule/README|Create Student Weekday Pickup Schedule]]
