---
title: "Custom Relationship"
aliases:
  - Custom Relationship
tags:
  - servicenow-dev-program
  - code-snippet
  - custom-relationship
  - server-side
---

Instead of duplicating attachment by use of GlideSysAttachment.copy() simplest approach is to create a relationship from System Definition >> Relationship & then display it as a Related list on required set of Tables were attachments are to be shown.

So, for a case where attachments from REQ (sc_request) are to be on RITM (sc_req_item) table then a relationship as below would suffice.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/CallScriptIncludeWithParameters/README|CallScriptIncludeWithParameters]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/CheckTableExtension/README|CheckTableExtension]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/Create Admin Users/README|Create Admin Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/Create Tiny Url with API's/README|Create Tiny Url with API's]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/CreateUpdateCIThroughIRE/README|CreateUpdateCIThroughIRE]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/Dynamic Catalog Task Creation/README|Dynamic Catalog Task Creation]]
