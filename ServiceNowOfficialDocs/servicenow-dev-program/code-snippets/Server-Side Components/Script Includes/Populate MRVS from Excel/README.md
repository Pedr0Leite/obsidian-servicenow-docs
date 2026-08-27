---
title: "Populate MRVS from Excel"
aliases:
  - Populate MRVS from Excel
tags:
  - servicenow-dev-program
  - code-snippet
  - populate-mrvs-from-excel
  - script-includes
---

This script allows to parse the excel file attached to the attachment variable and populate the MRVS present in the
catalog item / record producer.
Use this script in a client-callable script include along with an onChange client script on the attachment variable.

When a file is uploaded as an attachment, it's metdata is stored in the sys_attachment table and sys_attachment_doc contains
the actual binary content.

**getContentStream()** converts the binary content in a way so that it can be parsed by GlideExcelParser API.

**Example used-**

The excel has two columns "Id" and "Name" to store employee details. MRVS also has the variable name as "employee_id" and "employee_name".

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
