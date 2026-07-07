---
title: "TinyURLHelper"
aliases:
  - TinyURLHelper
tags:
  - servicenow-dev-program
  - code-snippet
  - tinyurlhelper
  - script-includes
---

This utility Helps to make a tiny url in code. For example, lets say you are creating a custom link
to a long list of sys_idINa,b,c,etc and want the link to make the link look like this:
https://<instance>.service-now.com/some_table_list.do?sysparm_tiny=3a2bbf87dbdc8890e670d48a489619bf

Use this script include to do that, like below example usage:

```r
var myTable = 'some_table_list';
var myLongQueryStr = 'sysparm_query=sys_idIN' + encodeURIComponent('pretend,long,list,of,sys_id');
var myCustomUrl = new TinyUrlHelper().getSert(table=myTable, queryStr=myLongQueryStr);
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
