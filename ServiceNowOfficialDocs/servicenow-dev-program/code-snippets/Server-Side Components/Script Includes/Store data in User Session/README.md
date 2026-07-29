---
title: "Store data in User Session"
aliases:
  - Store data in User Session
tags:
  - servicenow-dev-program
  - code-snippet
  - store-data-in-user-session
  - script-includes
---

The GlideSession API allows you to store the client data in session and retrieve it.

Following are the example of the usage:

```var sample = {'name':'xyz','email':'xyz@abc.com'};```

```var sessionUpdate = new storeDataInSession();```

```gs.print(sessionUpdate.putDataInSession(sample));```

```var session = gs.getSession();```

```gs.print(session.getClientData('name'));```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
