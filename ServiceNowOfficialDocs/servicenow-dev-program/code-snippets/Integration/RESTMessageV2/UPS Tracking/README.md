---
title: "UPS Tracking"
aliases:
  - UPS Tracking
tags:
  - servicenow-dev-program
  - code-snippet
  - ups-tracking
  - restmessagev2
---

This script calls the UPS tracking API.

UPS Developer Account:
Sign up at https://developer.ups.com
Create an App to get credentials
1. Client ID
2. Client Secret

How to use:
1. Replace YOUR_CLIENT_ID and YOUR_CLIENT_SECRET with your UPS credentials.
2. Use the sandbox URL (wwwcie.ups.com) for testing and production URL (onlinetools.ups.com) for live data.
3. You can move this logic into a Script Include and call it from a Flow, Business Rule, or Catalog Client Script.
4. For security, store credentials in a Connection & Credential Alias and reference them in the script instead of hardcoding.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/RESTMessageV2/sys_rest_message_config|sys_rest_message_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/RESTMessageV2/sys_rest_message_fn_config|sys_rest_message_fn_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/RESTMessageV2/API for Automatic Group creation/README|API for Automatic Group creation]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/RESTMessageV2/Aadhaar Verification/Readme|Aadhaar Verification]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/RESTMessageV2/Auth2 client credentials token cache with auto-refresh/README|Auth2 client credentials token cache with auto-refresh]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/RESTMessageV2/AzureDevOps/README|AzureDevOps]]
