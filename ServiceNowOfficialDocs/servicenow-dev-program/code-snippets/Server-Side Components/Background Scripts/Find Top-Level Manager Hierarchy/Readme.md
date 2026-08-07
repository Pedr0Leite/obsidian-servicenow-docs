---
title: "Find Top-Level Manager Hierarchy"
aliases:
  - Find Top-Level Manager Hierarchy
tags:
  - servicenow-dev-program
  - code-snippet
  - find-top-level-manager-hierarchy
  - background-scripts
---

The script retrieves the top-level manager for the currently logged-in user  by traversing the manager hierarchy in the sys_user table.

It starts from the current user and moves up through each manager until it reaches a user who does not have a manager.

The script starts with the current user (e.g., Employee).

It checks if the user has a manager.

If yes, it moves up the hierarchy to the manager.

It repeats this process until it reaches a user who does not have a manager.

That user is considered the Top-Level Manager.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
