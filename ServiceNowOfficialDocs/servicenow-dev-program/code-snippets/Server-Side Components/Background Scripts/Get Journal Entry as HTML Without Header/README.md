---
title: "Get Journal Entry as HTML Without Header"
aliases:
  - Get Journal Entry as HTML Without Header
tags:
  - servicenow-dev-program
  - code-snippet
  - get-journal-entry-as-html-without-header
  - background-scripts
---

# Get Journal Entry as HTML

This script can be used in a Business Rule or background script, or any other server-side script. It assumes the presence of the `current` object, but can be used with any positioned GlideRecord. 

## Use

Simply change `current` to whatever GlideRecord variable you're using, and change the `journalFieldName` variable so it contains the name of the journal field you want to get the value for.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
