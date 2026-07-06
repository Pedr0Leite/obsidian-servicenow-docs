---
title: "End Date can't be before Start Date"
aliases:
  - End Date can't be before Start Date
tags:
  - servicenow-dev-program
  - code-snippet
  - end-date-cant-be-before-start-date
  - client-scripts
---

This script is for an onChange client script

This is using an example where you have two date variables and need to ensure the user does not choose an end date that's before the start date

1. replace 'start_date' in the script with your actual start date field name
2. replace 'end_date' in the script with yoru actual start date field name
3. replace showFieldMsg and showErrorBox messages with your own message, if applicable

This script works for both the standard (desktop) UI and Service Portal

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort action when description is empty/ReadMe|Abort action when description is empty]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort direct incident closure without Resolve State/readme|Abort direct incident closure without Resolve State]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Field Decoration/README|Add Field Decoration]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Image to Field Based on Company/README|Add Image to Field Based on Company]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Adding Placeholder on Resolution Notes/README|Adding Placeholder on Resolution Notes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Auto Update Priority based on Impact and Urgency/readme|Auto Update Priority based on Impact and Urgency]]
