---
title: "getGlideRecordObject"
aliases:
  - getGlideRecordObject
tags:
  - servicenow-dev-program
  - code-snippet
  - getgliderecordobject
  - script-includes
---

# CustomUtils

A Script utils containing utility functions, patterns and coding standards.

> Notes:

-   Utility method names starts with "\_"
-   each method is followed by an example code snippet displaying usage of the method.

---

### \_getGlideRecordObject

> \_getGlideRecordObject(sysID, tableName)

parameters:

-   sysID: sys_id of the record
-   tableName: table name of the record

returns:

-   GlideRecord object of the record OR false if record could not be found

Usage:

-   Instead of having multiple GlideRecord code (when you have access ro record sys_id) in different places in your code, call this method to get the record.
-   This method will return false if record could not be found.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
