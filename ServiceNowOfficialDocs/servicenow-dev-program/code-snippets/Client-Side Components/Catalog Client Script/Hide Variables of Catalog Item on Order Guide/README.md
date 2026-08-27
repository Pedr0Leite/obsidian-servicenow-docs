---
title: "Hide Variables of Catalog Item on Order Guide"
aliases:
  - Hide Variables of Catalog Item on Order Guide
tags:
  - servicenow-dev-program
  - code-snippet
  - hide-variables-of-catalog-item-on-order-guide
  - catalog-client-script
---

1. The onLoad catalog client script can be used to hide the catalog varaibles on catalog form when the catalog item is being used on OrderGuide and cascade varaibles field is enabled on Order guide.
2. Cascading enables the transfer of values entered for variables in the initial order form to their corresponding variables in the catalog items that have been ordered.
3. Assume that the variables variable_name1, varaible_name2 are already present on the order guide form, hence hiding these variables on the catalog form when the catalog form is opened through an order guide using the function isOrderGuide().

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Add Label For Attachment/README|Add Label For Attachment]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Add Rows in MRVS/README|Add Rows in MRVS]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Auto Save Draft Feature/README|Auto Save Draft Feature]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Auto-populate field from URL/README|Auto-populate field from URL]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Autofilling the request details from previous request/Readme|Autofilling the request details from previous request]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Autopopulate Department/README|Autopopulate Department]]
