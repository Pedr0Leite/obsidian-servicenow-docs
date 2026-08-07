---
title: "Extract JSON Key without Flow Transformation"
aliases:
  - Extract JSON Key without Flow Transformation
tags:
  - servicenow-dev-program
  - code-snippet
  - extract-json-key-without-flow-transformation
  - flow-actions
---

This code will be helpful to those who are looking out to remove HTML tags and convert it to String variable within the Flow Designer. The Replace String transformation function doesn't works well with the HTML variable so to overcome this challenge, we can make use of a Run Script Flow action along with a regex and JavaScript replace method.

The function expects the input HTML string to be passed into and we get a string free from HTML tags and whitespaces as an output.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Add signature and update fields to a fillable PDF document/README|Add signature and update fields to a fillable PDF document]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Adhoc Assessment Generator Flow Action/README|Adhoc Assessment Generator Flow Action]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Assign Role/README|Assign Role]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Calculate Ticket Age/README|Calculate Ticket Age]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Check MID Server Availability/README|Check MID Server Availability]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Create Student Weekday Pickup Schedule/README|Create Student Weekday Pickup Schedule]]
