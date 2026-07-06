---
title: "Access Analysis Utility"
aliases:
  - Access Analysis Utility
tags:
  - servicenow-dev-program
  - code-snippet
  - access-analysis-utility
  - background-scripts
---

In scenarios where it's necessary to verify Read/Write access for multiple users across various work items (such as Incidents, Tasks, etc.), traditional methods like impersonating individual users or using the Access Analyzer plugin can be time-consuming. This utility streamlines the process by enabling simultaneous access analysis for multiple users by impersonating them and can be executed efficiently via a background script.

userId- Array containing the user id of personas whose access to be analyzed.

workItems- Work items extending the 'task' table.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Adding bookmark to Favorites tab/README|Adding bookmark to Favorites tab]]
