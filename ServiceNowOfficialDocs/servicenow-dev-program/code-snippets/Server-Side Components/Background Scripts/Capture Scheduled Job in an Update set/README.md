---
title: "Capture Scheduled Job in an Update set"
aliases:
  - Capture Scheduled Job in an Update set
tags:
  - servicenow-dev-program
  - code-snippet
  - capture-scheduled-job-in-an-update-set
  - background-scripts
---

Scheduled Job Update Set Capture Script

This ServiceNow background script addresses a critical deployment challenge by programmatically capturing scheduled jobs in update sets. 
By default, ServiceNow scheduled jobs are not automatically captured in update sets, making them difficult to migrate between environments. 
This script uses the GlideUpdateManager2 API to force a scheduled job record into the current update set, enabling seamless deployment through standard update set processes.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
