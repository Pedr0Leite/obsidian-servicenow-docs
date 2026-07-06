---
title: "AjaxAsyncOnSubmit"
aliases:
  - AjaxAsyncOnSubmit
tags:
  - servicenow-dev-program
  - code-snippet
  - ajaxasynconsubmit
  - glideajax
---

On submit client scripts do not support in making asynchronous calls to server on both platform and portal due to its nature of execution. This had always been a problem and there was a need to make validations work asynchronously on submitting a form/record. The support for getXMLWait() had also been removed which prevents the usage of synchronous GlideAjax call on a service portal. The snippet provides a workaround to execute async calls in both forms and catalog items, thus enabling server side validations during onsubmit.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAjax/Check Weekend - Client Side/README|Check Weekend - Client Side]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAjax/EfficientGlideRecord (Client-side)/README|EfficientGlideRecord (Client-side)]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAjax/Fetch Multiple Values in GlideAjax without JSON/README|Fetch Multiple Values in GlideAjax without JSON]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAjax/Get Field Values/README|Get Field Values]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAjax/Get choices from Decision Table/README|Get choices from Decision Table]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAjax/GlideAjax Example Template/README|GlideAjax Example Template]]
