---
title: "Log Utils"
aliases:
  - Log Utils
tags:
  - servicenow-dev-program
  - code-snippet
  - log-utils
  - script-includes
---

This is a lightweight utility for managing logging within Script Includes.
It provides a simple, configurable way to enable or disable debug logs during development and to exclude specific methods from logging when necessary.

This approach helps maintain clean logs, reduces noise during debugging, and allows for quick toggling of logging behavior once development is complete.

Usage:
You can call the log method anywhere inside your Script Include to record a log message:
this.log(<method_name>, <message>);

Example:
this.log('processData', 'Starting data processing...');

Initialization Parameters:
Logging behavior is controlled through the parameters passed to the initialize method when creating the Script Include instance.

var utils = new scope.utils(true, 'methodName1,methodName2');

Parameters:
======================================================================================================================	
|debug           |	Boolean	false |	Enables or disables logging. Set to true to allow logs, false to suppress them.  |
|noDebugMethods  |	String	""	  | A comma-separated list of method names that should not produce logs.             |
======================================================================================================================

Example Use Case:
If you’re developing a new method that depends on existing, stable methods, you can temporarily disable logging for the known-good methods.
For example:

var utils = new scope.utils(true, 'validatedMethod');

This enables logs for all methods except validatedMethod, keeping your system logs focused on what you’re currently debugging.

When development is complete, you can remove the parameters (or set debug to false) to disable all logs.

Notes:
The script uses gs.debug() for logging to keep logs easily filterable within the system logs.
You can switch to gs.info(), gs.warn(), or gs.error() depending on your needs.

Logging should typically remain disabled (debug = false) in production to avoid unnecessary system overhead.

This utility is flexible and can be dropped into almost any Script Include with minimal setup.

Example in Context:

var example_utils = Class.create();
example_utils.prototype = Object.extendsObject(global.AbstractAjaxProcessor, {
    initialize: function(debug, noDebugMethods) {
        this.logger = new log_utils(debug, noDebugMethods);
    },

    processData: function() {
        this.logger.log('processData', 'Starting process...');
        // ...your logic here...
        this.logger.log('processData', 'Process completed successfully.');
    }
});

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
