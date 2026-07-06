---
title: "Data Lookup Table Utils"
aliases:
  - Data Lookup Table Utils
tags:
  - servicenow-dev-program
  - code-snippet
  - data-lookup-table-utils
  - script-includes
---

# Data Lookup Table Utils

This script include provides a quick method of looking up data from any table extended from dl_matcher (Data Lookup Matcher Rules).  

It will build a list of the columns for the specified table and then allow you to query based on an array of values.

For example, using the dl_u_priority table we could lookup the Urgency values for a given Impact as follows;

```javascript
var lib = new global.DataLookupUtils("dl_u_priority")

var lookupData = lib.getLookupData("1");
gs.info(lookupData);
```
This will return *1,2,3*.

By also passing in a second value we can filter on Urgency and Impact;

```javascript
var lib = new global.DataLookupUtils("dl_u_priority")

var lookupData = lib.getLookupData(["1", "2"]);
gs.info(lookupData);
```
This will return *2*.

We could also ignore the Impact column and lookup Priority for a given Urgency by setting our own lookup columns;

```javascript
var lib = new global.DataLookupUtils("dl_u_priority")
lib.setColumns(["urgency", "priority"]);

var lookupData = lib.getLookupData(["3"]);
gs.info(lookupData);
```
This will return *3,4,5*

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
