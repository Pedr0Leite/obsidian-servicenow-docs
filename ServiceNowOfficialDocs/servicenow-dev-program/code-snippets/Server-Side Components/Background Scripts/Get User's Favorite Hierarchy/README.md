---
title: "Get User's Favorite Hierarchy"
aliases:
  - Get User's Favorite Hierarchy
tags:
  - servicenow-dev-program
  - code-snippet
  - get-users-favorite-hierarchy
  - background-scripts
---

This script will allow you to get Favorites Hierarchy of a specific user.
This means all nested groups and links.

Here is an example call with print out. You can replace gs.getUserID() with a User Name instead:

var favorites = getFavoritesHierarchyArray(gs.getUserID());
gs.info(JSON.stringify(favorites));


This will return an array of objects.
Each item in the array will have a "type" property which will be "group" for nested groups and "bookmark" for bookmarks/links

Other properties are named the same as the standard fields on the "sys_ui_bookmark_group" and "sys_ui_bookmark" tables for Groups and Bookmark types respectively

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
