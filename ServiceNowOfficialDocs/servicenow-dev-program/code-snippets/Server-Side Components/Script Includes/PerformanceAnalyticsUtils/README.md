---
title: "PerformanceAnalyticsUtils"
aliases:
  - PerformanceAnalyticsUtils
tags:
  - servicenow-dev-program
  - code-snippet
  - performanceanalyticsutils
  - script-includes
---

# Performance Analytics Utils

A Script Include to gather methods for handling Performance Analytics subjects. Typical use case is to be invoked by PA Scripts (for custom aggregation or breakdown mappings).

## getCmdbClassTableNames

Returns sys_id's of all the tables (sys_db_object) starting -and including- a start class. This is very useful to build a PA Breakdown on CMDB Classes. This method is fast as it uses the sys_class_path field to query sys_db_object.

This is a replacement for SNC.CMDBUtil.getAllChildrenOfAsCommaList() that I did not manage to invoke from Breakdown Source record Condition Builder (was getting an illegal access error because of the SNC scope).

I understand this also could be in an CMDBUtil Script Include, but I found very useful for building a PA Breakdown Source.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
