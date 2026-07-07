---
title: "Approval APIs"
aliases:
  - Approval APIs
tags:
  - servicenow-dev-program
  - code-snippet
  - approval-apis
  - scripted-rest-api
---

Approval API to Approve / Reject the Approval Record 

* Approve API

Request :
HTTP Method / URI
POST https://<instance name>.service-now.com/api/sr_approvals/<approval record sysid>/approve
  
Headers :
Acceptapplication/json
Content-Typeapplication/json
  
Request Body : 
{
'comment' : 'Please approve this record'
}
  
Response :
Status code : 200 OK 
  
 Response Body
{
  "result": "Record has been Approved!"
}
  
* Reject API
  
Request :
HTTP Method / URI
POST https://<instance name>.service-now.com/api/sr_approvals/<approval record sysid>/reject
  
Headers : 
Acceptapplication/json
Content-Typeapplication/json
  
Request Body : 
{
'comment' : 'Please reject this record'
}
  
Response :
Status code : 200 OK 
  
 Response Body
{
  "result": "Record has been Rejected!"
}

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Scripted REST API/sys_ws_definition_config|sys_ws_definition_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Scripted REST API/sys_ws_operation/sys_ws_operation_config|sys_ws_operation_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Scripted REST Api/Approval on Behalf/README|Approval on Behalf]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Scripted REST Api/CMDB API/README|CMDB API]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Scripted REST Api/CURL Script to create incident via tableAPI/README|CURL Script to create incident via tableAPI]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Scripted REST Api/CopyAI Generative AI example/README|CopyAI Generative AI example]]
