---
title: "Client Validation of Attachments by File Type and Count"
aliases:
  - Client Validation of Attachments by File Type and Count
tags:
  - servicenow-dev-program
  - code-snippet
  - client-validation-of-attachments-by-file-type-and-count
  - client-scripts
---

This ServiceNow client script is designed to validate file attachments on a form before submission. It's most likely used as a "Client Script" or "Client Script in a Catalog Item" that runs in the browser when a user tries to submit a form.

This client script runs when a form is submitted in ServiceNow. It checks if the user has:

Attached at least one file (shows an error if none).
Attached no more than three files (shows an error if more).
Only uploaded files of type PDF or PNG (shows an error for other types).
If any of these checks fail, the form submission is blocked and an appropriate error message is displayed.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort action when description is empty/ReadMe|Abort action when description is empty]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort direct incident closure without Resolve State/readme|Abort direct incident closure without Resolve State]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Field Decoration/README|Add Field Decoration]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Image to Field Based on Company/README|Add Image to Field Based on Company]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Adding Placeholder on Resolution Notes/README|Adding Placeholder on Resolution Notes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Auto Update Priority based on Impact and Urgency/readme|Auto Update Priority based on Impact and Urgency]]
