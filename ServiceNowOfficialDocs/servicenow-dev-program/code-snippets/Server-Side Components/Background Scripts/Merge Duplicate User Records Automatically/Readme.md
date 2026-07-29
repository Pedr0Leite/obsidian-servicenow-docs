---
title: "Merge Duplicate User Records Automatically"
aliases:
  - Merge Duplicate User Records Automatically
tags:
  - servicenow-dev-program
  - code-snippet
  - merge-duplicate-user-records-automatically
  - background-scripts
---

Merge Duplicate User Records Automatically


Automatically detects and merges duplicate User records in ServiceNow based on the email address.

Ensures data integrity and prevents duplicate entries.

Reassigns related records (e.g., incidents) to a master record.

Deactivates duplicate users.

In this UseCase
Multiple users exist with the same email address.

The first record found is treated as the master user.

All duplicates are: Reassigned in related records (e.g., tasks, incidents).

Marked inactive.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
