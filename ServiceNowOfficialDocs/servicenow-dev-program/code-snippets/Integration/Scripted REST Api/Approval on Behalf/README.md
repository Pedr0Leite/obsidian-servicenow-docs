---
title: "Approval on Behalf"
aliases:
  - Approval on Behalf
tags:
  - servicenow-dev-program
  - code-snippet
  - approval-on-behalf
  - scripted-rest-api
---

# Approve On Behalf - Scripted REST API

## Overview
This REST API allows authorized users to approve or reject tasks on behalf of another user. The script handles impersonation, performs action on approval records, and returns appropriate responses based on the success or failure of the request.

### API Definition
- **Name**: Approve On Behalf
- **Application**: Global
- **Active**: Yes
- **HTTP Method**: POST
- **Relative Path**: /
- **Resource Path**: /api/aueis/approve_on_behalf

## Request Format
The API accepts `application/json` as the input format.

### Sample Request
```json
{
    "approvalRecId": "1234567890abcdef",
    "userId": "user.name",
    "action": "approve",
    "comments": "Approving on behalf of the user"
}


### Sample Success Response
json
Copy code
{
    "success": true,
    "message": "Action 'approve' performed successfully on approval record."
}
### Sample Error Response
json
Copy code
{
    "success": false,
    "message": "Invalid approval record ID: 1234567890abcdef"
}

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Scripted REST API/sys_ws_definition_config|sys_ws_definition_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Scripted REST API/sys_ws_operation/sys_ws_operation_config|sys_ws_operation_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Scripted REST Api/Approval APIs/README|Approval APIs]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Scripted REST Api/CMDB API/README|CMDB API]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Scripted REST Api/CURL Script to create incident via tableAPI/README|CURL Script to create incident via tableAPI]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Scripted REST Api/CopyAI Generative AI example/README|CopyAI Generative AI example]]
