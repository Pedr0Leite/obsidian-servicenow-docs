---
title: "Return Asset(s) for User"
aliases:
  - Return Asset(s) for User
tags:
  - servicenow-dev-program
  - code-snippet
  - return-assets-for-user
  - glideajax
---

Client Callable GlideAjax script include to return one of the Following based on passed user's sys_id:

-Single Asset for User

-Single Asset for User with Model Category filtering

-All Assets for User

Script queries the "alm_hardware" table. Intended to be called from a client script/catalog client script, one use case would be to populate a users asset on a catalog item form.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAjax/AjaxAsyncOnSubmit/README|AjaxAsyncOnSubmit]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAjax/Check Weekend - Client Side/README|Check Weekend - Client Side]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAjax/EfficientGlideRecord (Client-side)/README|EfficientGlideRecord (Client-side)]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAjax/Fetch Multiple Values in GlideAjax without JSON/README|Fetch Multiple Values in GlideAjax without JSON]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAjax/Get Field Values/README|Get Field Values]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAjax/Get choices from Decision Table/README|Get choices from Decision Table]]
