---
title: "Capturing a record in to the current update set"
aliases:
  - Capturing a record in to the current update set
tags:
  - servicenow-dev-program
  - code-snippet
  - capturing-a-record-in-to-the-current-update-set
  - background-scripts
---

Using this script present in "Capturing a record in to the current update set using background script.js" file we can capture a record from a table (eg; groups, approval configurations) to the current update set

We have to provide the table name and the sys_id of the record properly as mentioned in the script.

When using the GlideUpdateManager2 API, a record is created in the sys_update_version table, and an XML file is created under the customer update folder because it is a part of the mechanism that allows adding records to an update set.

GlideUpdateManager2() will only work in global scope. If you try to create an update sect in scoped application and try to use GlideUpdateManager2 API then it will capture the update in the crrent scoped update set but the update will be in global scope. So there will be conflict while moving the update set.

Note: GlideUpdateManager2 API is undocumented API.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
