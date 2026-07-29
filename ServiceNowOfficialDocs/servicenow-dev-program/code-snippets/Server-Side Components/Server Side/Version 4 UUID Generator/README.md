---
title: "Version 4 UUID Generator"
aliases:
  - Version 4 UUID Generator
tags:
  - servicenow-dev-program
  - code-snippet
  - version-4-uuid-generator
  - server-side
---

# Description

When creating events for any message buses it might happen that you have to provide a so-called UUID within the payload. However you cannot just use any ServiceNow Sys ID as unique identifier as a version 4 UUID has to follow a certain format (see [Wikipedia](https://en.wikipedia.org/wiki/Universally_unique_identifier)). 

As I could not find any helper method within the ServiceNow API library I decided to implement my own version.

# Usage

Just call the function `generateUUID()` as often as you want. It will always generate a different UUID.

Example Result:

01ce5586-db98-1837-91cd-739e63c895b2

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/CallScriptIncludeWithParameters/README|CallScriptIncludeWithParameters]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/CheckTableExtension/README|CheckTableExtension]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/Create Admin Users/README|Create Admin Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/Create Tiny Url with API's/README|Create Tiny Url with API's]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/CreateUpdateCIThroughIRE/README|CreateUpdateCIThroughIRE]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/Custom Relationship/README|Custom Relationship]]
