---
title: "ConnectionCredentialsUtils"
aliases:
  - ConnectionCredentialsUtils
tags:
  - servicenow-dev-program
  - code-snippet
  - connectioncredentialsutils
  - script-includes
---

# Retrieve Connection and Credentials Information using Connection Alias (sys_id) in a Scoped Application
I've created a Script Include that enables users to retrieve connection and credentials details associated with a Scoped Application.

In addition to providing this information, the Script Include also decrypts and returns the value of the password2 field. It supports a wide range of credential types, including:

Basic Authentication credentials
API Key credentials
Windows credentials
SSH credentials, and more.

This tool simplifies access to important connection and credential data for all supported types in the scoped environment.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
