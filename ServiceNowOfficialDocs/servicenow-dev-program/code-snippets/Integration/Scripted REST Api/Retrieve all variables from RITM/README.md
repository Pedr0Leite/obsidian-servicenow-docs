---
title: "Retrieve all variables from RITM"
aliases:
  - Retrieve all variables from RITM
tags:
  - servicenow-dev-program
  - code-snippet
  - retrieve-all-variables-from-ritm
  - scripted-rest-api
---

# Retrieve all variables (including multi-row) from any Request Item or Catalog Task - and push JSON for use in a Scripted REST API
It's really not that hard to do using existing APIs, but if you want to pull a list of variables and their values, it gets a little messy. 
If you want values from a Multi-Row Variable Set, it gets even messier.  So, we set about building a Scripted REST API our partners can use. 

 1. [Build a Scripted REST API- resource configuration in the comments of the script](scripted_rest_api.js) 
 2. [Build a script include (the one referenced in the resource script above)](CHVarUtils_ScriptInclude.js)
 3. [Sample Output return in JSON format](output_example.js)

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Scripted REST API/sys_ws_definition_config|sys_ws_definition_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Scripted REST API/sys_ws_operation/sys_ws_operation_config|sys_ws_operation_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Scripted REST Api/Approval APIs/README|Approval APIs]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Scripted REST Api/Approval on Behalf/README|Approval on Behalf]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Scripted REST Api/CMDB API/README|CMDB API]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Scripted REST Api/CURL Script to create incident via tableAPI/README|CURL Script to create incident via tableAPI]]
