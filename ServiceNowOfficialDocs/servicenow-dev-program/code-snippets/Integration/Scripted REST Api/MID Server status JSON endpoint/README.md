---
title: "MID Server status JSON endpoint"
aliases:
  - MID Server status JSON endpoint
tags:
  - servicenow-dev-program
  - code-snippet
  - mid-server-status-json-endpoint
  - scripted-rest-api
---

# MID Server status JSON endpoint

## What this solves
Operations teams often need a quick machine-readable view of MID Server health for dashboards and monitors. This Scripted REST API returns a compact JSON array of MID Servers with their status, last update time, and a simple "stale" flag if the record has not changed recently.

## Where to use
Create a Scripted REST API with a single Resource and paste this script as the Resource Script. Call it from monitoring tools, dashboards, or widgets.

## How it works
- Queries `ecc_agent` for active MID Servers
- Returns `name`, `status`, `sys_id`, `sys_updated_on`, and a computed `stale` boolean based on a configurable `minutes_stale` query parameter (default 15)
- Uses `gs.dateDiff` to compute minutes since last update

## Configure
- Pass `minutes_stale` as a query parameter to override the default, for example `...?minutes_stale=30`
- Extend the payload as needed (for example add `version`, `ip_address`) if available in your instance

## References
- Scripted REST APIs  
  https://www.servicenow.com/docs/bundle/zurich-application-development/page/build/applications/task/create-scripted-rest-api.html
- MID Server overview  
  https://www.servicenow.com/docs/bundle/zurich-servicenow-platform/page/product/mid-server/concept/c_MIDServer.html
- GlideRecord API  
  https://www.servicenow.com/docs/bundle/zurich-api-reference/page/app-store/dev_portal/API_reference/GlideRecord/concept/c_GlideRecordAPI.html
- GlideDateTime and dateDiff  
  https://www.servicenow.com/docs/bundle/zurich-api-reference/page/app-store/dev_portal/API_reference/GlideDateTime/concept/c_GlideDateTimeAPI.html

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Scripted REST API/sys_ws_definition_config|sys_ws_definition_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Scripted REST API/sys_ws_operation/sys_ws_operation_config|sys_ws_operation_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Scripted REST Api/Approval APIs/README|Approval APIs]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Scripted REST Api/Approval on Behalf/README|Approval on Behalf]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Scripted REST Api/CMDB API/README|CMDB API]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Scripted REST Api/CURL Script to create incident via tableAPI/README|CURL Script to create incident via tableAPI]]
