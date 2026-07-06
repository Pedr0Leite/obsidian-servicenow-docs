---
title: "CheckTableExtension"
aliases:
  - CheckTableExtension
tags:
  - servicenow-dev-program
  - code-snippet
  - checktableextension
  - server-side
---

The snippet validates whether a child table is extended from a parent table. You could provide both the table names as input and it would respond back with a boolean output.

Sample Usage

gs.info(isTableExtended("cmdb_ci", "cmdb_ci_win_server"));  //true

gs.info(isTableExtended("cmdb_ci", "cmdb_ci_hardwares"));   //false

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/CallScriptIncludeWithParameters/README|CallScriptIncludeWithParameters]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/Create Admin Users/README|Create Admin Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/Create Tiny Url with API's/README|Create Tiny Url with API's]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/CreateUpdateCIThroughIRE/README|CreateUpdateCIThroughIRE]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/Custom Relationship/README|Custom Relationship]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/Dynamic Catalog Task Creation/README|Dynamic Catalog Task Creation]]
