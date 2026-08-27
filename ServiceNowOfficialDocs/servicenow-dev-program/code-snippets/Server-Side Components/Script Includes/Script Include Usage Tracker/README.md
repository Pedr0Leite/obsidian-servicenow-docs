---
title: "Script Include Usage Tracker"
aliases:
  - Script Include Usage Tracker
tags:
  - servicenow-dev-program
  - code-snippet
  - script-include-usage-tracker
  - script-includes
---

#  Script Include Usage Tracker

A utility Script Include to help ServiceNow developers identify where a specific Script Include is being referenced across the instance. This is especially useful during refactoring, cleanup, or impact analysis.

##  Features

- Scans multiple tables for references to a given Script Include.
- Outputs a list of locations including table name, record name, and sys_id.
- Easily extendable to include more tables or fields.

##  Installation

1. Navigate to **System Definition > Script Includes** in your ServiceNow instance.
2. Click **New** and paste the code from `ScriptIncludeUsageTracker.js`.
3. Save and make sure the Script Include is **Client Callable = false**.

##  Usage

You can run the Script Include from a background script or another Script Include like this:
var tracker = new ScriptIncludeUsageTracker();
tracker.findUsage('MyScriptInclude');

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
