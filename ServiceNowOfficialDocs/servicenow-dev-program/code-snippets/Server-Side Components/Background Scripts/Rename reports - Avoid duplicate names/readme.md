---
title: "Rename reports - Avoid duplicate names"
aliases:
  - Rename reports - Avoid duplicate names
tags:
  - servicenow-dev-program
  - code-snippet
  - rename-reports---avoid-duplicate-names
  - background-scripts
---

How often we come across cases where reports are created with same name by different users. Well to maintain some uniquenss across why not have some controls to get it unified. Below script can be used to suffix 'Created by' to the report to help uniquely identify report.
Execute it as a background script to update it in bulk.
For example Report named ABC will becom ABC - [PQR]v1 and ABC - [XYZ]v2 where PQR and XYZ are created by users 

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
