---
title: "add member to groups"
aliases:
  - add member to groups
tags:
  - servicenow-dev-program
  - code-snippet
  - add-member-to-groups
  - background-scripts
---

**Script to Add a User to list of User Groups Where They Are Not Already a Member**

Purpose: we often recive requests add a single group member to multiple groups. that's a manual task. this script makes it very simple.

- **The first GlideRecord('sys_user_group')**: Creates a GlideRecord instance to query the `sys_user_group` table.
   
- **addEncodedQuery('')**: Add the required list of groups here, by copying filter from list of groups.

- We use while loop to loop through list of groups.

- **The second GlideRecord('sys_user_grmember')**: For each group, creates a new GlideRecord instance to query the `sys_user_grmember` table (user-group memberships).

- **addQuery('group', rec.sys_id)**: Filters the `sys_user_grmember` records by the current group’s `sys_id`.

- **addQuery('user', '7279f455939e71944c77b6b5fbba1033')**: Filters the records for the specific user's `sys_id` ( this is sample sys id. replace with the actual `sys_id` of the user).

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
