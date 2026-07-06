---
title: "Adhoc Assessment Generator Flow Action"
aliases:
  - Adhoc Assessment Generator Flow Action
tags:
  - servicenow-dev-program
  - code-snippet
  - adhoc-assessment-generator-flow-action
  - flow-actions
---

Use Case: Lets say you would like to trigger/create an assessment in your flow designer flow for any taregt record? 

Eiither you have to create a custom logic/script in your flow or update appropriate assessment condition and update target to meet the assessment condition.

Here is the generic action where you just have to select appropriate records and it just triggers assessment.

This generic action takes following inputs to create assessment record.

1)Metric type: Assessment name

2)Metric Category : Category of the assessment (this includes Assessment questions)

3)Target Table : Select target table (ex: RITM or any custom table)

4)Assessment Assignment user: Select user whom do you like to assign the assessment

5)Target record sys_id: provide sys_id of the target record , you can input dynamic value from the flow data pills

![image](https://github.com/user-attachments/assets/e1a034b3-cfef-4793-b559-dee2905da70e).

![image](https://github.com/user-attachments/assets/16ddf545-4a0c-47e0-981d-dd524047a7ed)

![image](https://github.com/user-attachments/assets/e8c9b431-0980-47f9-b598-a8d4640f42d4)

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Add signature and update fields to a fillable PDF document/README|Add signature and update fields to a fillable PDF document]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Assign Role/README|Assign Role]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Calculate Ticket Age/README|Calculate Ticket Age]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Check MID Server Availability/README|Check MID Server Availability]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Create Student Weekday Pickup Schedule/README|Create Student Weekday Pickup Schedule]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Data Stream/README|Data Stream]]
