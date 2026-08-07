---
title: "Get Display Value of MRVS"
aliases:
  - Get Display Value of MRVS
tags:
  - servicenow-dev-program
  - code-snippet
  - get-display-value-of-mrvs
  - catalog-client-script
---

## Get Display Value of MultiRow Variableset (MRVS)

While there are different ways to do this, the easiest of them is to leverage an out of box script named **'VariableUtil'**. 

The script is present in the global scope and contains an function named getDisplayValue aptly. This function seems to work on both the normal variable as well as multirow variableset. You just need to pass the sysid of the variable or the multirow variableset and its corresponding value.

**new VariableUtil().getDisplayValue('sys_id of variable or MRVS','value of variable/MRVS');**

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Add Label For Attachment/README|Add Label For Attachment]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Add Rows in MRVS/README|Add Rows in MRVS]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Auto Save Draft Feature/README|Auto Save Draft Feature]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Auto-populate field from URL/README|Auto-populate field from URL]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Autofilling the request details from previous request/Readme|Autofilling the request details from previous request]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Autopopulate Department/README|Autopopulate Department]]
