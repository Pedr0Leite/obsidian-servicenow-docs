---
title: "Milliseconds to Duration"
aliases:
  - Milliseconds to Duration
tags:
  - servicenow-dev-program
  - code-snippet
  - milliseconds-to-duration
  - flow-actions
---

When you use flow designer to calcualte the difference between two duration fields, these duration fields need to be changed into milliseconds using dateNumericValue(). This can be done in a flow variable similar to the example below:

var timeWorked = fd_data.trigger.current.u_total_time_worked;
timeWorked =  timeWorked.dateNumericValue();

var estimatedTime = fd_data.trigger.current.change.u_impact_assessment.u_change_request_effort_total;
estimatedTime =  estimatedTime.dateNumericValue()

var remainingTime = estimatedTime - timeWorked;

return remainingTime;

To be able to convert the millisections back into a duration fields, this flow designer action uses:

- the milliseconds (reaminingTime) from the calculation as the input in an integer value
- the the code will add the milliseconds to the ServiceNow Epoch DateTime which the duration fields uses and then returns the time difference back into a string that can be added to a duration field
- the output of the action needs to be set to the time as a duration type field

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Add signature and update fields to a fillable PDF document/README|Add signature and update fields to a fillable PDF document]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Adhoc Assessment Generator Flow Action/README|Adhoc Assessment Generator Flow Action]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Assign Role/README|Assign Role]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Calculate Ticket Age/README|Calculate Ticket Age]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Check MID Server Availability/README|Check MID Server Availability]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Create Student Weekday Pickup Schedule/README|Create Student Weekday Pickup Schedule]]
