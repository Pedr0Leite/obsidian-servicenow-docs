---
title: "CURL Script to create incident via tableAPI"
aliases:
  - CURL Script to create incident via tableAPI
tags:
  - servicenow-dev-program
  - code-snippet
  - curl-script-to-create-incident-via-tableapi
  - scripted-rest-api
---

## Use the attached script to create a incident via CURL script execution 

You need to update the username, password and instancename in the URL section of the script -> username:password https://instance_name.service-now.com/api/now/table/incident

Also, This script can be modified to work for any table in ServiceNow by changing the table_name in the URL/Endpoint and updating the required attributtes as per the table in the payload.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Scripted REST API/sys_ws_definition_config|sys_ws_definition_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Scripted REST API/sys_ws_operation/sys_ws_operation_config|sys_ws_operation_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Scripted REST Api/Approval APIs/README|Approval APIs]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Scripted REST Api/Approval on Behalf/README|Approval on Behalf]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Scripted REST Api/CMDB API/README|CMDB API]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Scripted REST Api/CopyAI Generative AI example/README|CopyAI Generative AI example]]
