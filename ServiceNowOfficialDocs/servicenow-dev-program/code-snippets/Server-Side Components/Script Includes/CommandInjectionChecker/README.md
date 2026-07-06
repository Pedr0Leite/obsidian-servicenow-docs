---
title: "CommandInjectionChecker"
aliases:
  - CommandInjectionChecker
tags:
  - servicenow-dev-program
  - code-snippet
  - commandinjectionchecker
  - script-includes
---

The CommandInjectionChecker is a ServiceNow Script Include designed to detect potential command injection attacks in user-supplied strings. It scans for common shell metacharacters and patterns (e.g., ;, |, &, $(), `) using regex, providing a boolean result to flag suspicious inputs. This utility enhances security in server-side automation without relying on external libraries, following ServiceNow best practices for input validation.

Example on how to use it:

var checker = new CommandInjectionChecker();

// Safe input
if (!checker.containsCommandInjection('Normal text')) {
    gs.info('Input is clean.');
}

// Suspicious input
if (checker.containsCommandInjection('ls; rm -rf /')) {
    gs.error('Command injection detected - blocking action.');
}

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
