---
title: "ReturnMultipleProperties"
aliases:
  - ReturnMultipleProperties
tags:
  - servicenow-dev-program
  - code-snippet
  - returnmultipleproperties
  - glideajax
---

## Use values from returned object in Ajax call
- With this code snippet, make the ajax call from a client script.
- Replace `HM_Task_Details` with script include name of your choosing.
- Replace `sysparm_tableName` & `sysparm_recordID` with variable names from script include function. (can add as many as needed).
- Replace second argument (next to `sysparm_name`) with name of funtion from script include you would like to call. 
- In callback function use obj to access the property values of that object as shown in snippet.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAjax/AjaxAsyncOnSubmit/README|AjaxAsyncOnSubmit]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAjax/Check Weekend - Client Side/README|Check Weekend - Client Side]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAjax/EfficientGlideRecord (Client-side)/README|EfficientGlideRecord (Client-side)]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAjax/Fetch Multiple Values in GlideAjax without JSON/README|Fetch Multiple Values in GlideAjax without JSON]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAjax/Get Field Values/README|Get Field Values]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAjax/Get choices from Decision Table/README|Get choices from Decision Table]]
