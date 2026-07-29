---
title: "Check Valid Choice"
aliases:
  - Check Valid Choice
tags:
  - servicenow-dev-program
  - code-snippet
  - check-valid-choice
  - script-includes
---

Introduction :

This script include is a client callable script include which can be used to check if the value of a choice field is valid, optionally given a dependent value. This is helpful when you do transforms and when you want to do some validations in your REST inbound messages.

Inputs and Outputs :
     * @param {object} current - GlideRecord object containing the current record
     * @param {string} The name of the choice field
     * @returns {bool}         - Boolean indicating whether the value of a choice field is valid

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
