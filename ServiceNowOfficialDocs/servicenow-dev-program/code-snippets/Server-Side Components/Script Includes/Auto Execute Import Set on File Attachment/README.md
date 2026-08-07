---
title: "Auto Execute Import Set on File Attachment"
aliases:
  - Auto Execute Import Set on File Attachment
tags:
  - servicenow-dev-program
  - code-snippet
  - auto-execute-import-set-on-file-attachment
  - script-includes
---

# Auto Execute Import Set on File Attachment
You have to create a data source and a transform map first. After that you can use Flow Designer with the trigger condition Attachment is added to the data source. Once the flow triggers, it will call the action which in turn will trigger the Script Include to create an Import Set and Transform Map.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
