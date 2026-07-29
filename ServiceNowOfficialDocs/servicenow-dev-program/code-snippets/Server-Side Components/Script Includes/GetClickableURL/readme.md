---
title: "GetClickableURL"
aliases:
  - GetClickableURL
tags:
  - servicenow-dev-program
  - code-snippet
  - getclickableurl
  - script-includes
---

Function that generates clickable HTML links to records in different UI contexts (Native UI, Workspace or Portal)




Sample background Script:

var record_sysid = '';// add the record sys_id here.
gs.info(new global.GetRecordDetails().getClickableURL('incident', record_sysid, 'INC- Workspace', 'workspace', 'cwf/agent'));

gs.info(new global.GetRecordDetails().getClickableURL('incident', record_sysid, 'INC- Portal', 'portal', 'sp'));

gs.info(new global.GetRecordDetails().getClickableURL('incident', record_sysid, 'INC - NativeUI', 'native'));

gs.info(new global.GetRecordDetails().getClickableURL('', record_sysid, 'INC - NativeUI', 'native'));

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
