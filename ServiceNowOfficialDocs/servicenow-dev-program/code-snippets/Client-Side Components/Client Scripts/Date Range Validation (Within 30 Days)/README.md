---
title: "Date Range Validation (Within 30 Days)"
aliases:
  - Date Range Validation (Within 30 Days)
tags:
  - servicenow-dev-program
  - code-snippet
  - date-range-validation-within-30-days
  - client-scripts
---

Date Range Validation (Within 30 Days) in Client Side

This ServiceNow client script provides real-time date validation for form fields, ensuring users can only select dates within a specific 30-day window from today's date. The script runs automatically when a user changes a date field value, providing immediate feedback and preventing invalid date submissions.

The script validates that any date entered in a form field meets these criteria:
Minimum Date: Today's date (no past dates allowed)
Maximum Date: 30 days from today's date
Real-time Validation: Instant feedback as users type or select dates
User-friendly Errors: Clear error messages explaining the valid date range
Automatic Field Clearing: Invalid dates are automatically cleared to prevent submission

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort action when description is empty/ReadMe|Abort action when description is empty]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort direct incident closure without Resolve State/readme|Abort direct incident closure without Resolve State]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Field Decoration/README|Add Field Decoration]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Image to Field Based on Company/README|Add Image to Field Based on Company]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Adding Placeholder on Resolution Notes/README|Adding Placeholder on Resolution Notes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Auto Update Priority based on Impact and Urgency/readme|Auto Update Priority based on Impact and Urgency]]
