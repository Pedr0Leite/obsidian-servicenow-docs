---
title: "Set fields from URL Parameters"
aliases:
  - Set fields from URL Parameters
tags:
  - servicenow-dev-program
  - code-snippet
  - set-fields-from-url-parameters
  - catalog-client-script
---

# Set fields on a catalog item from URL parameters.

This only works on both the classic ui and service portal.

To use this you must provide the technical name as a url parameter and then provide the value you would like set. This script is also console logging the techcnical names if you don't have them handy. Reference fields require using the sys_id.


### Example

For the OOTB Password Reset catalog item it has a field "Whose password needs to be reset?" with a technical value of "caller_id" after adding this script you could use the below url parameter to auto populate the form with Abel Tuter.

/sp?id=sc_cat_item&sys_id=29a39e830a0a0b27007d1e200ad52253&**caller_id=62826bf03710200044e0bfc8bcbe5df1**

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Add Label For Attachment/README|Add Label For Attachment]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Add Rows in MRVS/README|Add Rows in MRVS]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Auto Save Draft Feature/README|Auto Save Draft Feature]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Auto-populate field from URL/README|Auto-populate field from URL]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Autofilling the request details from previous request/Readme|Autofilling the request details from previous request]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Autopopulate Department/README|Autopopulate Department]]
