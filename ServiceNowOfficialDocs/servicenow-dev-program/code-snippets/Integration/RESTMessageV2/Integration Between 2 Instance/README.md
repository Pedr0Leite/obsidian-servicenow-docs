---
title: "Integration Between 2 Instance"
aliases:
  - Integration Between 2 Instance
tags:
  - servicenow-dev-program
  - code-snippet
  - integration-between-2-instance
  - restmessagev2
---

This code helps in integrating two ServiceNow instances using Rest Message - in that HTTP Post method, where I also included in the code that, once an incident is created in the source instance same record will be created in the target instance and the target record's sys_id and incident number will be auto-populated in the source instance's incident record's Correlation ID& Display field's respectively.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/RESTMessageV2/sys_rest_message_config|sys_rest_message_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/RESTMessageV2/sys_rest_message_fn_config|sys_rest_message_fn_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/RESTMessageV2/API for Automatic Group creation/README|API for Automatic Group creation]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/RESTMessageV2/Aadhaar Verification/Readme|Aadhaar Verification]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/RESTMessageV2/Auth2 client credentials token cache with auto-refresh/README|Auth2 client credentials token cache with auto-refresh]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/RESTMessageV2/AzureDevOps/README|AzureDevOps]]
