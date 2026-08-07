---
title: "Create Student Weekday Pickup Schedule"
aliases:
  - Create Student Weekday Pickup Schedule
tags:
  - servicenow-dev-program
  - code-snippet
  - create-student-weekday-pickup-schedule
  - flow-actions
---

## Flow Action Script to Create Weekday student pickup schedule

This code is part of a scope app where we create a pickup schedule for active Students

This is part of a scheduled flow that runs on Sunday night and created a set of records for each active student and builds a pickup schedule accoreding to the School Start and end times.
It also accounts for early release days such as Wednesday at 2:00pm 

This script can be modified to fit your specific needs. 

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Add signature and update fields to a fillable PDF document/README|Add signature and update fields to a fillable PDF document]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Adhoc Assessment Generator Flow Action/README|Adhoc Assessment Generator Flow Action]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Assign Role/README|Assign Role]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Calculate Ticket Age/README|Calculate Ticket Age]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Check MID Server Availability/README|Check MID Server Availability]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Data Stream/README|Data Stream]]
