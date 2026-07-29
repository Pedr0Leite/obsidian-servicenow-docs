---
title: "Count Assigned To Field"
aliases:
  - Count Assigned To Field
tags:
  - servicenow-dev-program
  - code-snippet
  - count-assigned-to-field
  - client-scripts
---

Count Assigned To Field

1. Write a Client Script name as getAssignedToCount
2. Glide the Incident Table
3. Use onChange Client Script
4. Use the Field name as "assigned_to" field
5. Glide the Script Include using "GlideAjax".
6. Call the function "getCount" from Script Include
7. Add the parameter for the newValue.
8. Use the getXML for asynchronous response.
9. Get the answer using the callback function
10. Use the logic for the more than how many tickets that error needs to populate
11. Use the addErrorMessage for marking the error message
12. Use the setValue for the "assigned_to" field.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort action when description is empty/ReadMe|Abort action when description is empty]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort direct incident closure without Resolve State/readme|Abort direct incident closure without Resolve State]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Field Decoration/README|Add Field Decoration]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Image to Field Based on Company/README|Add Image to Field Based on Company]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Adding Placeholder on Resolution Notes/README|Adding Placeholder on Resolution Notes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Auto Update Priority based on Impact and Urgency/readme|Auto Update Priority based on Impact and Urgency]]
