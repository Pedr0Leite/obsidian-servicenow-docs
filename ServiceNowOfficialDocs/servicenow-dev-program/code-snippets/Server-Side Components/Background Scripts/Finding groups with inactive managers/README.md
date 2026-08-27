---
title: "Finding groups with inactive managers"
aliases:
  - Finding groups with inactive managers
tags:
  - servicenow-dev-program
  - code-snippet
  - finding-groups-with-inactive-managers
  - background-scripts
---

This script is designed to identify all active user groups in ServiceNow where:
	The group has no manager assigned, OR
	The assigned manager is inactive.
This script helps administrators easily locate and notify the management about this inconsistancy.

Administrators can also use this script in their fix scripts and add a mailing functionality to the group members by calling an event to trigger the mail.

All you need to do is use the call the function : "Checkgrps()" and it will check for the groups with inactive or no managers and stores the names of the groups in an array "arr".

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
