---
title: "Webhook receiver with HMAC SHA-256 validation"
aliases:
  - Webhook receiver with HMAC SHA-256 validation
tags:
  - servicenow-dev-program
  - code-snippet
  - webhook-receiver-with-hmac-sha-256-validation
  - scripted-rest-api
---

# Webhook receiver with HMAC SHA-256 validation

## What this solves
Inbound webhooks should be verified to ensure the payload really came from the sender. This receiver validates an `X-Signature` header containing an HMAC SHA-256 of the request body using a shared secret. Invalid signatures return HTTP 401.

## Where to use
- Scripted REST API resource script
- Include the `HmacUtils` Script Include in the same app or global

## How it works
- Reads raw request body and the `X-Signature` header
- Computes HMAC SHA-256 using the shared secret
- Compares in constant time to avoid timing attacks
- If valid, inserts the payload into a target table or queues it for processing

## Configure
- Set `SHARED_SECRET` (prefer credentials or encrypted properties)
- Update `TARGET_TABLE` for successful inserts

## References
- Scripted REST APIs  
  https://www.servicenow.com/docs/bundle/zurich-application-development/page/build/applications/task/create-scripted-rest-api.html
- REST API request/response objects  
  https://www.servicenow.com/docs/bundle/zurich-api-reference/page/app-store/dev_portal/API_reference/GlideHTTPRequest/concept/c_scripted-rest-api-request.html
- Java crypto (used server-side)  
  https://www.servicenow.com/docs/bundle/zurich-api-reference/page/app-store/dev_portal/API_reference/Script/server_apis/concept/java-use.html

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Scripted REST API/sys_ws_definition_config|sys_ws_definition_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Scripted REST API/sys_ws_operation/sys_ws_operation_config|sys_ws_operation_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Scripted REST Api/Approval APIs/README|Approval APIs]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Scripted REST Api/Approval on Behalf/README|Approval on Behalf]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Scripted REST Api/CMDB API/README|CMDB API]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Scripted REST Api/CURL Script to create incident via tableAPI/README|CURL Script to create incident via tableAPI]]
