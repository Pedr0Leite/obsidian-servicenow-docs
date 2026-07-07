---
title: "ListFieldUtil"
aliases:
  - ListFieldUtil
tags:
  - servicenow-dev-program
  - code-snippet
  - listfieldutil
  - script-includes
---

# ListFieldUtil
Script Include that helps with handling list fields, like for example "Watch List" on the task table.

It doesn't use the typical `Class.create`, instead it is a simple javascript function.
Check out this blog post for more info about the "Function Pattern": https://codecreative.io/blog/interface-design-patterns-function-pattern/

## Example Script
```javascript
var watchListVal = grMyIncident.getValue("watch_list");
//add current user to watch list
var newWatchListVal = ListFieldUtil(watchListVal).add(gs.getUserID());
grMyIncident.setValue("watch_list", newWatchListVal);

//remove current user from watch list
var newWatchListVal = ListFieldUtil(watchListVal).remove(gs.getUserID());
grMyIncident.setValue("watch_list", newWatchListVal);

//check if current user exists in watch list
var currentUserInWatchList = ListFieldUtil(watchListVal).exists(gs.getUserID());
gs.debug("Current user is in watch list: " + currentUserInWatchList);
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
