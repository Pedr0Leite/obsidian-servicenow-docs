---
title: "Table Growth Analysis"
aliases:
  - Table Growth Analysis
tags:
  - servicenow-dev-program
  - code-snippet
  - table-growth-analysis
  - background-scripts
---

# Table Size Analysis Script

This script checks the number of records in selected ServiceNow tables and shows how many were created in the last 30 days.

## Tables Checked
- `task`
- `cmdb_ci`
- `sc_cat_item`

## What It Does
- Logs the start of the analysis.
- Counts total records in each table.
- Counts records created in the last 30 days.
- Logs both counts to the system log.

## How to Use
1. Add or remove table names in the `tablesToCheck` list.
2. Run the script in a background script or scheduled job.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
