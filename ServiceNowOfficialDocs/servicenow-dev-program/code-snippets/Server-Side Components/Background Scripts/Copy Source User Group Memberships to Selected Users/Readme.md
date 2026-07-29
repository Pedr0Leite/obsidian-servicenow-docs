---
title: "Copy Source User Group Memberships to Selected Users"
aliases:
  - Copy Source User Group Memberships to Selected Users
tags:
  - servicenow-dev-program
  - code-snippet
  - copy-source-user-group-memberships-to-selected-users
  - background-scripts
---

Background Script — Copy Source User’s Groups to Specific Users

Working:
It retrieves all groups of the source user.
Loops through all active users (except the source).
Checks whether the user is already a member of that group.
If not, it inserts a new record in sys_user_grmember.

Note:
sourceUserSysId → sys_id of the user whose groups you want to copy.
The 3 entries in targetUserSysIds → sys_ids of the target users.
It checks for duplicates, so no errors even if the user is already in that group.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
