---
title: "Generate unique value based on sequence"
aliases:
  - Generate unique value based on sequence
tags:
  - servicenow-dev-program
  - code-snippet
  - generate-unique-value-based-on-sequence
  - flow-actions
---

# Generate Unique Value Based on Sequence

The `execute()` function in action is generates a unique sequence value based on the existing sequence in a column of a table. This function inside a action script is designed to be used in database environments. It takes the following input parameters:

- `table`: The name of the table to generate the unique value for.
- `column`: The name of the column to generate the unique value for.
- `default_value`: The default value to use if there are no records in the table.
- `useLowerUpperBoth`: A Boolean value indicating whether to use both lower and upper case characters when generating the next sequence value.

## Function Behavior

1. The function begins by querying the specified table to retrieve all the values in the specified column.

2. If there are records in the table:
   - The function then generates the next sequence value based on the last value in the column.
   - It automatically detects the type of sequence value to generate based on the postfix of the last value in the column:
     - If the postfix ends with digits, the function generates a numeric sequence value.
     - If the postfix ends with alphabetic characters, the function generates an alphabetic sequence value.
   - If the `useLowerUpperBoth` parameter is set to `true`, the function will use both lower and upper case characters when generating alphabetic sequence values.
   - If the `useLowerUpperBoth` parameter is set to `false`, the function will only use upper case characters when generating alphabetic sequence values.

3. If there are no records in the table, the function returns the `default_value`.

4. The function handles any exceptions by setting the output value to `null`.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Add signature and update fields to a fillable PDF document/README|Add signature and update fields to a fillable PDF document]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Adhoc Assessment Generator Flow Action/README|Adhoc Assessment Generator Flow Action]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Assign Role/README|Assign Role]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Calculate Ticket Age/README|Calculate Ticket Age]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Check MID Server Availability/README|Check MID Server Availability]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Create Student Weekday Pickup Schedule/README|Create Student Weekday Pickup Schedule]]
