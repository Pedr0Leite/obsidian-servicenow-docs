---
title: "MRVS Interact With Parent Form"
aliases:
  - MRVS Interact With Parent Form
tags:
  - servicenow-dev-program
  - code-snippet
  - mrvs-interact-with-parent-form
  - catalog-client-script
---

Use this code snippet to interact with the parent form (i.e the main Cataloge Item) from within a Catalog Client Script that applies to a multi-row variable set.

The g_service_catalog object allows for accessing the "parent" GlideForm (g_form) object for getValue only (for now?)
To affect a variable in the main catalogue item using setValue, clearValue, etc. parent.g_form... is available in the native UI, and this.cat_g_form... can be used for Service Portal, etc if an additional Catalog Client Script is used, this one onLoad that Applies to the Catalog Item (not the MRVS).

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Add Label For Attachment/README|Add Label For Attachment]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Add Rows in MRVS/README|Add Rows in MRVS]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Auto Save Draft Feature/README|Auto Save Draft Feature]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Auto-populate field from URL/README|Auto-populate field from URL]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Autofilling the request details from previous request/Readme|Autofilling the request details from previous request]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Autopopulate Department/README|Autopopulate Department]]
