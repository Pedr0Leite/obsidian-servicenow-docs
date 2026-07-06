---
title: "ACL script is failing at script include function call"
aliases:
  - KB0750886
tags:
  - servicenow
  - support-kb
  - acl
  - access-control
  - script-includes
  - server-side
  - scripting
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0750886
kb_number: KB0750886
last_modified: 2024-05-03
---

## Issue

# Symptoms

ACL script is failing at script include function call, and an error is logged in system logs.

log19:26:48.439: Evaluator: org.mozilla.javascript.EcmaError: undefined is not a function. Caused by error in Access Control: '<table\_name>' at line 1   
answer = (new <script>.<functionName>(<parameters>)); 

# Release

All

# Cause

This kind of error occurs when there is a syntactical error in the function calls. Missing parentheses after script include is the cause for this error.

  

# Resolution

To call a function which is defined in a script include, follow the below syntax.

  

Syntax: answer = (new <scriptInclude\>().<functionName\>(<parameters>)); 

Example: answer= new ACLUtils().isDelegateOfUser(current.caller\_id)); 

  

# Additional Information

Refer [ACL Product Docs](#mce_temp_url#) for more information about ACL.

## Related

- [[KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow]] — how ACL scripts fit into the overall evaluation chain
- [[KB0782082 - When 'Admin Overrides' is unchecked and the requirement is to allow a specific roled users (but not admin) to access a f]] — another case requiring a custom ACL script
- [[acl-function-fields]] — official docs on using script includes/functions in ACL rules
- [[c_BusinessRules]] — server-side scripting API reference (script include calling conventions)
