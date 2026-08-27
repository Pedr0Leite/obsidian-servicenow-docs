---
title: "Get choice field value (mitigating known error)"
aliases:
  - Get choice field value (mitigating known error)
tags:
  - servicenow-dev-program
  - code-snippet
  - get-choice-field-value-mitigating-known-error
  - flow-actions
---

# Get choice field value (mitigating known error)

This Flow Action serves as a solution for addressing a recognized problem within Flow Designer ([known error](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813846)). The issue involves copying of a choice field from one record to another through the drag-and-drop functionality of the data pill. In this scenario, the copied choice field's label is incorrectly set instead of the actual underlying value. Consequently, this leads to the emergence of the "missing choice value" error, indicated by the choice value appearing in blue, disrupting subsequent logic that relies on this field.
To resolve this issue, I have written a simple generic Flow Designer Action “Get choice field label and value”. This action provides a reusable and effective workaround for addressing the problem in any instance where copying a choice field is required.

## Instruction

Create a Flow Action with the following inputs and outputs:
- inputs: table, record_id, choice_field_name
- outputs: choice_value, choice_label

In your Flow you can then access the choice_value via the data pill and drag and drop it to set the choice value of another record. If the display value is needed as well, it can also be accessed via the choice_label output. 

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Add signature and update fields to a fillable PDF document/README|Add signature and update fields to a fillable PDF document]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Adhoc Assessment Generator Flow Action/README|Adhoc Assessment Generator Flow Action]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Assign Role/README|Assign Role]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Calculate Ticket Age/README|Calculate Ticket Age]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Check MID Server Availability/README|Check MID Server Availability]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Create Student Weekday Pickup Schedule/README|Create Student Weekday Pickup Schedule]]
