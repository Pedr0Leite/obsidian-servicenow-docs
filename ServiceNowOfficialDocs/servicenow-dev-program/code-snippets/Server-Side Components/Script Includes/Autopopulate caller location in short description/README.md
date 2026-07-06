---
title: "Autopopulate caller location in short description"
aliases:
  - Autopopulate caller location in short description
tags:
  - servicenow-dev-program
  - code-snippet
  - autopopulate-caller-location-in-short-description
  - script-includes
---

GlideAjax: This is a ServiceNow-specific class used to make asynchronous calls to server-side scripts (Script Includes).
Script Include: 'getCallerLocation' is the name of the Script Include being called.
Parameters:
'sysparm_name': The name of the function to be called in the Script Include ('getLocation').
'sysparm_user': The user parameter being passed to the function, which is the new value of the control (newValue).
getXML: This method sends the request to the server and specifies a callback function (setLocation) to handle the response.
Function: setLocation
This function processes the response from the server.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
