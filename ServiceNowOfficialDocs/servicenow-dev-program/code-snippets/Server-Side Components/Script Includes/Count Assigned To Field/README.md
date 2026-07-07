---
title: "Count Assigned To Field"
aliases:
  - Count Assigned To Field
tags:
  - servicenow-dev-program
  - code-snippet
  - count-assigned-to-field
  - script-includes
---

Count Assigned To Field 

1. Create  a Script Include
2. Enable Client Callable
3. create a Function in the Script Include Class
4. Do Glide Aggregate to the Incident Table
5. Get the Parameter from the Client Script
6. Use the Aggregate - COUNT for the assigned_to field 
7. Use the While Loop
8. Get the COUNT of the assigned_to field
9. Return the COUNT to Client Script
10. Based on the COUNT we can add limit the assignment of the tickets to the assigned users.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Count Assigned To Field/README|Count Assigned To Field]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
