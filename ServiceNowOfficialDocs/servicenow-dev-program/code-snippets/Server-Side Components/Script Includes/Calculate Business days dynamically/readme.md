---
title: "Calculate Business days dynamically"
aliases:
  - Calculate Business days dynamically
tags:
  - servicenow-dev-program
  - code-snippet
  - calculate-business-days-dynamically
  - script-includes
---

# Business Day Calculator for ServiceNow

This JavaScript function calculates a future date by adding a specified number of **business days** (excluding weekends) to a given date.


##  Features
- Skips weekends (Saturday and Sunday)
- Works with any number of business days
- Uses ServiceNow's `GlideDateTime` API

##  Usage
1. Copy the function into a **Script Include**, **Business Rule**, or **Scheduled Job** in ServiceNow.
2. Call the function with:
   - A valid date string (e.g., `'2025-10-24 12:00:00'`)
   - The number of business days to add (e.g., `5`)

##  Example
```javascript
gs.print(add_business_days('2025-10-24 12:00:00', 5));
// Output: 2025-10-31 (skips weekend)

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
