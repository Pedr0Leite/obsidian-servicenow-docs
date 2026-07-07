---
title: "Get the current version of an application"
aliases:
  - Get the current version of an application
tags:
  - servicenow-dev-program
  - code-snippet
  - get-the-current-version-of-an-application
  - background-scripts
---

- Set the appName variable to the exact name of the application you’re checking (in this case as an example, Project Workspace).
- This script queries the Application [sys_app] table for a record with the specified name.
- If the application is found, it retrieves and prints the version. If not, it prints a message stating the application wasn’t found.
- This script will find the version of a specific application and output the version in the Scripts - Background logs.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
