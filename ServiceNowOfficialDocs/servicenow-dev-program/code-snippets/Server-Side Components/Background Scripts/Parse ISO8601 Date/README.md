---
title: "Parse ISO8601 Date"
aliases:
  - Parse ISO8601 Date
tags:
  - servicenow-dev-program
  - code-snippet
  - parse-iso8601-date
  - background-scripts
---

# ISO8601 Date Parser Script

Some APIs commonly return dates in ISO8601 format. This script can help you parse the date and get `'GlideDateTime'` object in return.

## Usage

You can use this script to parse ISO8601 date strings in a Business Rule, Background Script, Script Include, etc.

### Function: `parseISO8601DateTime(isoDate)`

This function takes an ISO8601 date string as input and returns a GlideDateTime object.

#### Parameters

- `isoDate` (string): The ISO8601 date string to be parsed. It should be
in the following format: `'YYYY-MM-DDTHH:mm:ssZ'` (e.g., `'2022-05-01T14:30:00Z'`).

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
