---
title: "Get MRVS Values from Parent"
aliases:
  - Get MRVS Values from Parent
tags:
  - servicenow-dev-program
  - code-snippet
  - get-mrvs-values-from-parent
  - catalog-client-script
---

# Get Multi-row Variable Set Values from parent form

Sometimes you need to query the current set of values for a MRVS from the actual MRVS or another MRVS. 
This requires getting the data from the parent form, the method to retrieve and the format of the data is different
when running on the platform or portal.

This script gives a way of getting the values regardless of the platform in use.

On the platform (backend) this could be moved to a global UI Script, but that is not available to portal scripts.

Make sure the UI Type is All, and Isolate Script is false (unchecked).

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Add Label For Attachment/README|Add Label For Attachment]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Add Rows in MRVS/README|Add Rows in MRVS]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Auto Save Draft Feature/README|Auto Save Draft Feature]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Auto-populate field from URL/README|Auto-populate field from URL]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Autofilling the request details from previous request/Readme|Autofilling the request details from previous request]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Autopopulate Department/README|Autopopulate Department]]
