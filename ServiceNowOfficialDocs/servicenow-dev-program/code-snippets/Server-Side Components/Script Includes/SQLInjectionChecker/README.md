---
title: "SQLInjectionChecker"
aliases:
  - SQLInjectionChecker
tags:
  - servicenow-dev-program
  - code-snippet
  - sqlinjectionchecker
  - script-includes
---

 SQLInjectionValidator
 
 Script Include for detecting potential SQL injection attempts in user-provided strings.
 
 Purpose:
 Validates user input against a comprehensive list of SQL injection patterns including
 keywords, operators, comment syntax, and common attack vectors.
 
 Usage:
 var validator = new SQLInjectionValidator();
 var isSafe = validator.isSafeFromSQLInjection(userInput);
 
 Performance Considerations:
 - Uses efficient string methods (toLowerCase, includes) for keyword detection
 - Regex patterns are pre-compiled for performance
 - Early exit on first match to minimize processing
 - Suitable for high-volume input validation
 
 Security Note:
 This function provides pattern-based detection and should be used as ONE LAYER
 of defense. Always use parameterized queries and prepared statements in your
 database interactions as the PRIMARY defense against SQL injection.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
