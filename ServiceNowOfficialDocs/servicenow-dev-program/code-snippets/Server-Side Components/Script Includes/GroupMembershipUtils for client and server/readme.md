---
title: "GroupMembershipUtils for client and server"
aliases:
  - GroupMembershipUtils for client and server
tags:
  - servicenow-dev-program
  - code-snippet
  - groupmembershiputils-for-client-and-server
  - script-includes
---

Utility Script Include for managing user-group relationships in ServiceNow (sys_user_grmember table). 

It provides methods to:
Retrieve users in a group (getGroupMembers)
Retrieve groups a user belongs to (getUserGroups)
Add users to a group (addGroupMembers)
Remove users from a group (removeGroupMembers)

Supports both client and server-side operations (where applicable), ensures no duplicate group memberships, and simplifies bulk updates.

Ideal for use in server scripts, GlideAjax calls, reference qualifiers, etc to streamline group membership management.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
