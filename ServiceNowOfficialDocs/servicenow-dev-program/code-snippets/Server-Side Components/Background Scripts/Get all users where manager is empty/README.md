---
title: "Get all users where manager is empty"
aliases:
  - Get all users where manager is empty
tags:
  - servicenow-dev-program
  - code-snippet
  - get-all-users-where-manager-is-empty
  - background-scripts
---

# Get all users without manager

Use the script in script.js file to get the list of all users in sys_user table who do not have an manager.
This GlideRecord script can be used in multiple places. For example in background scripts.

### Did some optimization in the code
1. Used different variable name instead of gr to reference a GlideRecord object.
2. Used addActiveQuery() method to filter out just the active records.
3. Used getDisplayValue() method to push string values in the array instead of using dot notation.
4. Used self executing function to wrap the code in a function for reducing variable scoping issues.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
