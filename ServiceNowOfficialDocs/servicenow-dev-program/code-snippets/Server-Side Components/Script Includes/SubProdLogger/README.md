---
title: "SubProdLogger"
aliases:
  - SubProdLogger
tags:
  - servicenow-dev-program
  - code-snippet
  - subprodlogger
  - script-includes
---

# ArtifactRank

Logger script include that helps you to specify the environments that you want create log records without commenting
your logging lines in your code. The logger will check if it is one of the sub-prod environments that you have specified
and log the line otherwise just ignore it. This means you just configure the logger once and then you don't have to
comment or remove your logging code at all!

## Usage

```javascript
var logger = new SubProdLogger(); // This will log for the default environments that is configured e.g. 'test', "uat", 'stage', 'qa', 'dev'. If you have other environment that you want to log for then register it in the line 35 if the SubProdLogger.js file i.e add new values here: this._subProdKeywords = ['test', "uat", 'stage', 'qa', 'dev'];

logger.warn('This is a warning.');
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
