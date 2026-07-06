---
title: "Bulk Change of Incident Priority Based on Category"
aliases:
  - Bulk Change of Incident Priority Based on Category
tags:
  - servicenow-dev-program
  - code-snippet
  - bulk-change-of-incident-priority-based-on-category
  - background-scripts
---

# Bulk Change of Incident Priority Based on Category

A background script that updates incident priorities for active incidents based on predefined category-to-priority mappings.

## Usage

1. Navigate to **System Definition → Scripts - Background**
2. Copy and paste the script content
3. Modify the `priorityMapping` object with your category-to-priority rules
4. Click "Run script"

## What It Does

The script:
1. Defines a mapping between incident categories and priority levels (e.g., 'Network': 1)
2. Queries all active incidents
3. Checks each incident's category against the mapping
4. Updates the incident priority if a match is found
5. Logs each updated incident number and new priority

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
