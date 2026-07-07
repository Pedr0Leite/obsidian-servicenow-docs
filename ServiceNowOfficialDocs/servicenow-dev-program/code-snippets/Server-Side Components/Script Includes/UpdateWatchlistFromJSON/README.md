---
title: "UpdateWatchlistFromJSON"
aliases:
  - UpdateWatchlistFromJSON
tags:
  - servicenow-dev-program
  - code-snippet
  - updatewatchlistfromjson
  - script-includes
---

UseCase - 

Update the watchlist of any table record with the provided JSON payload which should maintain the previous watchlist user and add new one from the payload

Payload can be Array, String, List of String

//Passing List of String of SysId of users
var payload = '43435efdsre4t5953439434,43434343436fdfsd343,frtgr6565hg676767gt';
updateWatchlistFromJSON('incident','a1b2c3d4e5f678901234567890abcdef', payload);

//Passing Array of String of SysId of users
var payload = '[43435efdsre4t5953439434,43434343436fdfsd343]';
updateWatchlistFromJSON('incident','a1b2c3d4e5f678901234567890abcdef', payload);

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
