---
title: "DynamicOutboundEnpoints"
aliases:
  - DynamicOutboundEnpoints
tags:
  - servicenow-dev-program
  - code-snippet
  - dynamicoutboundenpoints
  - restmessagev2
---

This is a server-side Script Include that contains the core logic. It reads the endpoint configurations from a System Property, parses the JSON, and returns the appropriate URL based on the current instance's name.

System Property: x_my_scope.api.endpoints
This property stores a JSON object containing the endpoint URLs for each environment. It must be created and populated in each instance that uses the utility.

Sample JSON object:
{
  "dev": "https://dev-instance.example.com/api",
  "test": "https://test-instance.example.com/api",
  "prod": "https://prod-instance.example.com/api"
}

Usage:
var endpointConfig = new EndpointConfig();
var endpointUrl = endpointConfig.getEndpoint();    
if (endpointUrl) 
{
gs.info("Endpoint URL: " + endpointUrl);  
//Use the endpointUrl in your REST call
  var request = new sn_ws.RESTMessageV2();
  request.setEndpoint(endpointUrl);
// ... rest of your integration logic        
} else 
{
gs.error("Failed to retrieve endpoint URL.");
}
    

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/RESTMessageV2/sys_rest_message_config|sys_rest_message_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/RESTMessageV2/sys_rest_message_fn_config|sys_rest_message_fn_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/RESTMessageV2/API for Automatic Group creation/README|API for Automatic Group creation]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/RESTMessageV2/Aadhaar Verification/Readme|Aadhaar Verification]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/RESTMessageV2/Auth2 client credentials token cache with auto-refresh/README|Auth2 client credentials token cache with auto-refresh]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/RESTMessageV2/AzureDevOps/README|AzureDevOps]]
