---
title: "Developer Debug Utility"
aliases:
  - Developer Debug Utility
tags:
  - servicenow-dev-program
  - code-snippet
  - developer-debug-utility
  - script-includes
---

# Developer Debug Utility (Controlled Logging)
Create a systemProperty - enable_debug_for_scripts (Boolean value)

# Overview
This utility provides a centralized, configurable debug logging mechanism for developers.  
Instead of using gs.info(), gs.log(), or gs.warn() - which create permanent logs in the system, developers can now log messages conditionally through a system property.

When the property 'enable_debug_for_scripts' is set to 'true', debug messages are logged; otherwise, all debug calls are ignored.  
This makes it ideal for debugging issues in Production without modifying code or flooding system logs.


# Objective
To provide a reusable, lightweight debugging utility that allows developers to:
- Enable/disable debug logs globally via a system property.  
- Avoid unnecessary system log entries when debugging is not needed.  
- Maintain clean, controlled, and consistent debug output across server-side scripts.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
