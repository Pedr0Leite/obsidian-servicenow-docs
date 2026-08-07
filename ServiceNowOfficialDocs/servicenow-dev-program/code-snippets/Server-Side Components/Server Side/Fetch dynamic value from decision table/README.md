---
title: "Fetch dynamic value from decision table"
aliases:
  - Fetch dynamic value from decision table
tags:
  - servicenow-dev-program
  - code-snippet
  - fetch-dynamic-value-from-decision-table
  - server-side
---

Fetch dynamic value from decision table

Use case: Map relevant values of field1 to field2 with large list of choices and often changing and needs to be editable by specific admin team.

Solution: If we want to have a scenario like based on "Field1" of big list of comma separated values, We need to provide its relevant "Field2" value, Which need not to be repeated again and the key value pair is huge and often changing, In that case we can make use of decision table to fetch key value pair without interrupting any scripts and saving value in "Field2" which will get changed according to "Field1" value as it is a calculated field.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/CallScriptIncludeWithParameters/README|CallScriptIncludeWithParameters]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/CheckTableExtension/README|CheckTableExtension]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/Create Admin Users/README|Create Admin Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/Create Tiny Url with API's/README|Create Tiny Url with API's]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/CreateUpdateCIThroughIRE/README|CreateUpdateCIThroughIRE]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/Custom Relationship/README|Custom Relationship]]
