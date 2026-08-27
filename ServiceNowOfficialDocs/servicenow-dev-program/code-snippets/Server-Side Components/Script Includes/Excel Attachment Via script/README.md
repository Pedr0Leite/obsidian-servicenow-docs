---
title: "Excel Attachment Via script"
aliases:
  - Excel Attachment Via script
tags:
  - servicenow-dev-program
  - code-snippet
  - excel-attachment-via-script
  - script-includes
---

Using Excel Attachment feature you can export the table contents in excel. This script include can be use for making an excel sheet from ServiceNow script and adding it to a record as an attachment.
Usage Example:

```
var row = [{'number':'inc000001','short_description':'test'},{'number':'inc000002','short_description':'test2'}];

var table = 'incident'; //Table name
var recordId = '552c48888c033300964f4932b03eb092'; //sysid of the record
var fileName = 'ExampleEXL'; //File name
var headerColumns = ['Number','Summary']; //Excel Header Columns

var attach = new excelAttachment();
attach.addExcelAttachment(table, recordId, fileName, row, headerColumns);
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
