---
title: "Group Sync Script"
aliases:
  - Group Sync Script
tags:
  - servicenow-dev-program
  - code-snippet
  - group-sync-script
  - fix-scripts
---

ServiceNow Fix Script - Group Role Synchronization
Overview

This Fix Script automatically validates and synchronizes user roles with their assigned groups in ServiceNow.
It checks if every user in the target groups has all the roles assigned to that group.
If any roles are missing, the script re-adds the user to the group, ensuring all inherited roles are correctly applied.

How It Works

Identify Groups
The script starts by reading the list of sys_ids of the target groups.

Fetch Group Roles
It retrieves all the roles assigned to each group from the sys_group_has_role table.

Check Each User
For each user in the group (sys_user_grmember), it fetches their assigned roles from sys_user_has_role.

Detect Missing Roles
Compares the user’s roles with the group’s roles.
If any group role is missing for a user:

Removes the user from the group.

Re-adds the user to the group, triggering ServiceNow’s role inheritance process.

Logs
The script logs all actions using gs.info() for easy monitoring in the system logs.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Fields On All List Views/README|Add Fields On All List Views]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Variable set to multiple catalog items/README|Add Variable set to multiple catalog items]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add bulk users to VTB/README|Add bulk users to VTB]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Adjust Variable Order on Catalog Item/README|Adjust Variable Order on Catalog Item]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Anonymise Data/README|Anonymise Data]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Assign user list to a specific group/README|Assign user list to a specific group]]
