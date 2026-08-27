---
title: "Table List Copy Context Options"
aliases:
  - Table List Copy Context Options
tags:
  - servicenow-dev-program
  - code-snippet
  - table-list-copy-context-options
  - script-includes
---

# Add "Copy Field Name, Value, Display Value" to context menu for list records

Add context menu options allowing for admins to be able to right click a record's field in the list view and choose "Copy Field Name", "Copy Field Value", and "Copy Field Display Value" to quickly get the column variable name and values to their clipboard.

## Setting up

- Create a script include and copy the .js file. Set it as `Client callable = true`
- Create sys_ui_context_menu (Context Menu) records, one each for:
    - Copy Field Value
    - Copy Field Name
    - Copy Field Display Value

## Context Menu records configuration

- Table: Global [global]
- Menu: List row
- Type: Action
- Name: Copy Field Value
- Order: Use 51, 52, and 53
- Acive: True
- Run onShow script: False
- Condition: `gs.hasRightsTo("ui/context_menu.copy_sysid/read", null)`
- Action Script: see .js files in this folder for each one

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
