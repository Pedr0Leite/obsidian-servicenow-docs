---
title: "Copy table fields from one table to another"
aliases:
  - Copy table fields from one table to another
tags:
  - servicenow-dev-program
  - code-snippet
  - copy-table-fields-from-one-table-to-another
  - background-scripts
---

# Copy Fields from One Table to Another

This script facilitates copying fields from one table to another. It accepts Table A and Table B as input along with the field names to copy.

## Use-Cases

- This is particularly useful for building demos/POCs on PDI instances when you frequently need to create new tables. In most cases, instead of creating fields one by one, you can copy common fields from one table to another.

**Note:** This is a sample script. Please run this script in a non-production environment first and test for all scenarios. The execution time of this script may vary depending on the number of fields to copy.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
