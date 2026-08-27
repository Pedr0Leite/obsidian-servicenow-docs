---
title: "SCIM Custom Mapping Handler"
aliases:
  - SCIM Custom Mapping Handler
tags:
  - servicenow-dev-program
  - code-snippet
  - scim-custom-mapping-handler
  - script-includes
---

This is a script include to handle custom mapping, covering a specific case where the SCIM client is using the entitlement attribute to store the user-group-memberships. 

Usage: the script must be invoked from the "SCIM User" ETL definition (installed with the SCIM v2 plugin). 

The main function accepts an array with group names and a user sys_id:

var handler = new SCIMCustomMappingHandler(true);

var ctx = sn_auth.SCIM2Util.getScimProviderCustomizationContext();

var entitlements = ctx.scimResource.entitlements;

var entitlementsList = [];
for (entitlement in entitlements){
entitlementsList.push(entitlements[entitlement].value);
}

handler.handleGroupMemberships(entitlementsList, source.id);

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
