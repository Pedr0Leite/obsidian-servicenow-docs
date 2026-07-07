---
title: "Dynamic Catalog Task Creation"
aliases:
  - Dynamic Catalog Task Creation
tags:
  - servicenow-dev-program
  - code-snippet
  - dynamic-catalog-task-creation
  - server-side
---

**Dynamic Catalog Task Generator**

This Script Include provides a flexible, maintainable way to create one or more Service Catalog Tasks (sc_task) on a Request Item (sc_req_item). Instead of relying on complex, branching logic within a single Workflow or Flow, this script determines which tasks to create based on the value selected by the user in a single variable on the catalog form.


**Centralizes Task Logic**: Keeps all task definitions (short descriptions, assignment groups, order) in one easy-to-read script.

**Improves Maintainability**: You only update this single script when task requirements change, not a sprawling visual flow.

**Increases Flow Reusability**: The core Flow/Workflow remains simple, focused only on calling this generator.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/CallScriptIncludeWithParameters/README|CallScriptIncludeWithParameters]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/CheckTableExtension/README|CheckTableExtension]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/Create Admin Users/README|Create Admin Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/Create Tiny Url with API's/README|Create Tiny Url with API's]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/CreateUpdateCIThroughIRE/README|CreateUpdateCIThroughIRE]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/Custom Relationship/README|Custom Relationship]]
