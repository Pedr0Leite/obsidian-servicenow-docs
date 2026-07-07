---
title: "Session"
aliases:
  - Session
tags:
  - servicenow-dev-program
  - code-snippet
  - session
  - glidesystem
---

GlideSystem (referred as "gs") is used to get the current user session which we are using to set the custom key and value which are used in client side scripts.

Example client script used to retrieve it

```
function onLoad(){
 var value = g_user.getClientData("custom_key");
 console.log("Client data "+value);
}
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideSystem/Impersonate/README|Impersonate]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideSystem/Table/README|Table]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideSystem/Trigger Event/README|Trigger Event]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideSystem/User Display Name/README|User Display Name]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideSystem/User/README|User]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideSystem/date-time/README|date-time]]
