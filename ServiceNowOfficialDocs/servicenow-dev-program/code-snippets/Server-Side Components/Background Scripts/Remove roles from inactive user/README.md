---
title: "Remove roles from inactive user"
aliases:
  - Remove roles from inactive user
tags:
  - servicenow-dev-program
  - code-snippet
  - remove-roles-from-inactive-user
  - background-scripts
---

# Remove all roles from inactive user

Code Snippet : Remove all roles from an inactive user 
When a user in an instance is inactive, it's a good practice to remove all roles assigned to that user. Following piece of code helps to remove all the roles from the inactive user.
~~~ 
var gr = new GlideRecord('sys_user_has_role');
gr.addEncodedQuery('user.active=false');
gr.query();
gr.deleteMultiple();
~~~
This piece of code can be used in scheduled jobs under scheduled script execution tab. This can be run weekly once to check the last one week inactive users and remove them from all assigned roles (if exist).

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
