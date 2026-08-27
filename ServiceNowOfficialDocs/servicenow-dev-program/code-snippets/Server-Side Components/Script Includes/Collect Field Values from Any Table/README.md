---
title: "Collect Field Values from Any Table"
aliases:
  - Collect Field Values from Any Table
tags:
  - servicenow-dev-program
  - code-snippet
  - collect-field-values-from-any-table
  - script-includes
---

# Universal Field Collector (Ajax Version Script Include)
- This SI allows for users to request any field values from any table (except if security restrictions prevent) for any one particular record
- In Client script, instantiate GlideAjax with this script include
- Call function `getDetails`
- Pass in the following parameters in this order
- (Table_Name, Sys_id, "field_Name_1,field_name_2")
- Note: fields requested from record need to be the format of a commas seperated string
- XMLAnswer will return stringified JSON object which can then be parsed in client script callback function

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
