---
title: "API for Automatic Group creation"
aliases:
  - API for Automatic Group creation
tags:
  - servicenow-dev-program
  - code-snippet
  - api-for-automatic-group-creation
  - restmessagev2
---

1.The after insert business rule on sys_user_group in the source instance, will create a group in target instance when a new group is created in source instance.
2.It passes the required fields like group name, manager, type of the group to target instance.
3.End point to create group in target instance is https://instance_name.service now.com/api/now/table/sys_user_group
4.A HTTP POST method should should be used to create a record in the target instance.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/RESTMessageV2/sys_rest_message_config|sys_rest_message_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/RESTMessageV2/sys_rest_message_fn_config|sys_rest_message_fn_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/RESTMessageV2/Aadhaar Verification/Readme|Aadhaar Verification]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/RESTMessageV2/Auth2 client credentials token cache with auto-refresh/README|Auth2 client credentials token cache with auto-refresh]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/RESTMessageV2/AzureDevOps/README|AzureDevOps]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/RESTMessageV2/Currency Conversion - Using CurrencyFreaks API/README|Currency Conversion - Using CurrencyFreaks API]]
