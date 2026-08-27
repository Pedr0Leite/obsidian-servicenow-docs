---
title: "Get The Last Journal Comment Date"
aliases:
  - Get The Last Journal Comment Date
tags:
  - servicenow-dev-program
  - code-snippet
  - get-the-last-journal-comment-date
  - background-scripts
---

# Timestamp Extraction from Comment

This code snippet demonstrates how to extract a timestamp from a comment text and create a 'GlideDateTime' object from it.
It may be useful if you don't want to drill down to the 'sys_journal_field' table.

## How it Works

1. It retrieves the last comment from the journal using `record.comments.getJournalEntry(1)`.
2. It then uses regular expressions to search for a timestamp in the format `DD-MM-YYYY hh:mm:ss`.
3. If a timestamp is found, it creates a new `GlideDateTime` object from the matched timestamp.

```javascript
/* If your date has a different format you can replace the regex pattern with a new one */
var timestampMatch = commentText.match(/YOUR_REGEX_PATTERN/);

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
