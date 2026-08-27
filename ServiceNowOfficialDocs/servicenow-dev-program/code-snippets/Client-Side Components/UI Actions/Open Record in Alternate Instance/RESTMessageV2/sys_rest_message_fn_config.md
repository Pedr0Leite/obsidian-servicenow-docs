---
title: "sys_rest_message_fn_config"
aliases:
  - sys_rest_message_fn_config
tags:
  - servicenow-dev-program
  - code-snippet
  - restmessagev2
  - open-record-in-alternate-instance
---

Name: [Target Instance] Record Exists
HTTP Method: PATCH
Endpoint: [Target Instance Url]/api/[api subpath]/.../record_exists

HTTP Request Parameters:

    {
        "table": "${table}",
        "sysId": "${sysId}"
    }

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/RESTMessageV2/sys_rest_message_config|sys_rest_message_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/README|Open Record in Alternate Instance]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Scripted REST API/sys_ws_definition_config|sys_ws_definition_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/UI Action/sys_ui_action_config|sys_ui_action_config]]
