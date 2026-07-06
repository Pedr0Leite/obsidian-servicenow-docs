---
title: "sys_ui_action_config"
aliases:
  - sys_ui_action_config
tags:
  - servicenow-dev-program
  - code-snippet
  - ui-action
  - open-record-in-alternate-instance
---

!! If your instances use vanity urls, or otherwise do not end in `.com`, the `split()` in code.js will need to be edited

Name: Open Record in [Target Instance]
Table: Global [global]
Action Name: Open Record in [Target Instance]

Client: true
List v2 Compatible: true
List v3 Compatible: true

Isolate script: false

Onclick: openInInstance()

Condition:

    gs.getProperty('[Target Instance]') != '[target instance name]' && !current.isNewRecord() && new CrossInstanceHelper().exists('[Target Instance]', current.getTableName(), current.sys_id.toString())

Script: See `sys_ui_action.js` for code.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/README|Open Record in Alternate Instance]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/RESTMessageV2/sys_rest_message_config|sys_rest_message_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/RESTMessageV2/sys_rest_message_fn_config|sys_rest_message_fn_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Scripted REST API/sys_ws_definition_config|sys_ws_definition_config]]
