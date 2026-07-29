---
title: "Reusable glideajax table query"
aliases:
  - Reusable glideajax table query
tags:
  - servicenow-dev-program
  - code-snippet
  - reusable-glideajax-table-query
  - glideajax
---

# glideAjax-table-column

A Client Callable script include which will query to the table and will return the set of columns. Below is the example of this code.
Client Side Usage Example:

var tableName = 'sys_user';
var user = g_user.userID;
var query = 'sys_id='+user;
var col = 'user_name,email';
var ga = new GlideAjax('getTableColumnsClientSide');
ga.addParam('sysparm_name','getColumns');
ga.addParam('sysparm_tableName',tableName);
ga.addParam('sysparm_encodedQuery',query);
ga.addParam('sysparm_columns',col);
ga.getXML(HelloWorldParse);

function HelloWorldParse(response) {
var answer = response.responseXML.documentElement.getAttribute("answer");
alert(answer);
}
Server Side usage example:

var si = new getTableColumnsClientSide();
var user = gs.getUserID();
var query = 'sys_id='+user;
var col = 'user_name,email';
gs.print(si.getColumns('sys_user',query,col));

Benefit: We can share this scripts usage examples with the regional developer, who don't have access to write custom scripts for catalog client script.
Benefit: Client Call and Server Call both use the same Script Include Function.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAjax/AjaxAsyncOnSubmit/README|AjaxAsyncOnSubmit]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAjax/Check Weekend - Client Side/README|Check Weekend - Client Side]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAjax/EfficientGlideRecord (Client-side)/README|EfficientGlideRecord (Client-side)]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAjax/Fetch Multiple Values in GlideAjax without JSON/README|Fetch Multiple Values in GlideAjax without JSON]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAjax/Get Field Values/README|Get Field Values]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAjax/Get choices from Decision Table/README|Get choices from Decision Table]]
