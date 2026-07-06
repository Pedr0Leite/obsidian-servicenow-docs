---
title: "Read Encoded Query"
aliases:
  - Read Encoded Query
tags:
  - servicenow-dev-program
  - code-snippet
  - read-encoded-query
  - background-scripts
---

This background script code to get the any encoded query in redable format.
You need to paste the encoded query in the quotes of the function API which you want to read in simple layman format 

Input Required as below

1. Table name on which the query is.
2. Any encoded query which you want to read

   Input Eg.

   Table Name- incident
   Encoded query  - 'active=true^short_descriptionLIKEtest'

   Output- Readable Query is Active = true .and. Short description contains test


   Please note that this API is allowed to worked in global application. It is not applicable in scoped application.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
