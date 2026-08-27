---
title: "Reinstate Error status"
aliases:
  - Reinstate Error status
tags:
  - servicenow-dev-program
  - code-snippet
  - reinstate-error-status
  - client-scripts
---

Table: Time Worked [task_time_worked]
Type: onsubmit

#Objective :
Ensure that time entries (represented by the work_date field) are not submitted after 8:00 PM CST on two key dates:
The 16th of the month and The last day of the month
If a user tries to submit time for a current or past date after the cut-off time, the submission is blocked and a clear error message is displayed.

#Business Scenario
Imagine a consulting firm where employees log billable hours against customer cases. There are internal controls in place that lock the timekeeping system after a certain cut-off time to ensure accurate payroll and billing.

The finance department requires that:
On the 16th and last day of each month, submissions must be in before 8:00 PM CST.
If employees miss the deadline, they can only log time for future dates (not today or the past).

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort action when description is empty/ReadMe|Abort action when description is empty]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort direct incident closure without Resolve State/readme|Abort direct incident closure without Resolve State]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Field Decoration/README|Add Field Decoration]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Image to Field Based on Company/README|Add Image to Field Based on Company]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Adding Placeholder on Resolution Notes/README|Adding Placeholder on Resolution Notes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Auto Update Priority based on Impact and Urgency/readme|Auto Update Priority based on Impact and Urgency]]
