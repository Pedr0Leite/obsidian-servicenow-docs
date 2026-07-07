---
title: "SCIM Payload Generator"
aliases:
  - SCIM Payload Generator
tags:
  - servicenow-dev-program
  - code-snippet
  - scim-payload-generator
  - script-includes
---

A script include to generate payload for testing SCIM-based integration.

The script covers as specific case where user is added/removed to user groups based on the values in the 'entitlements' object of the SCIM payload.

The main function accepts 3 parameters:

groupsToRemove - will check all groups of which the user is currently member and will randomly remove the membership of groups equal to the number passed to the parameter
groupsToAdd - will check all groups to which the is not currently a member and will randomly create membershis for groups equal to the number passed to the parameter
newGroupsToCreate - will create new groups and add the user to them. Group names are concatenation of a prefix and randomly generated string.
The end result of the function is a JSON object that can be directly passed as a payload while testing via REST API explorer or Postman.

Usage: var groupsToRemove = 2; var groupsToAdd = 1; var newGroupsToCreate = 3;

var generator = new GenerateSCIMPayload(); var scimPayload = generator.generateEntitlements(jamesVittoloSysID, groupsToRemove, groupsToAdd, newGroupsToCreate); gs.info(JSON.stringify(scimPayload));

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
