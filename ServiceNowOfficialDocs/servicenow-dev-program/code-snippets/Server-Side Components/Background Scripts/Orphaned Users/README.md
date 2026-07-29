---
title: "Orphaned Users"
aliases:
  - Orphaned Users
tags:
  - servicenow-dev-program
  - code-snippet
  - orphaned-users
  - background-scripts
---

This script identifies active users in ServiceNow who have no group memberships and no roles assigned.
It queries the sys_user table for all active users, then checks each user against the sys_user_grmember table (groups) and the sys_user_has_role table (roles).
If a user has no associated groups and no assigned roles, their username is added to a list called orphanedUsers.
Finally, the script prints the list, which can be used for user cleanup, security audits, or compliance purposes to ensure proper user management.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
