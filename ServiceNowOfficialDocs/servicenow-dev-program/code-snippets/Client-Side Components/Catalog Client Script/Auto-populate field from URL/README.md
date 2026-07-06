---
title: "Auto-populate field from URL"
aliases:
  - Auto-populate field from URL
tags:
  - servicenow-dev-program
  - code-snippet
  - auto-populate-field-from-url
  - catalog-client-script
---

This piece of code is designed for an usecase where you might want to populate a field value that you're passing as a query in the URL which redirects to a catalog item.
In this case, a custom field 'u_date' is chosen as an example to be shown:

1. You open a catalog item record via a URL that carries a date in the query string.
Example:
https://your-instance.service-now.com/your_form.do?sysparm_u_date=2025-10-31
-(This URL includes a parameter named sysparm_u_date with the value 2025-10-31.)


2. The catalog client script reads the page URL and extracts that specific parameter which returns the value "2025-10-31".

3. If the parameter is present, the script populates the form field.
Calling g_form.setValue('u_date', '2025-10-31') sets the date field on the form to 31 October 2025.


Result:
The date field in the form is prefilled from the URL

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Add Label For Attachment/README|Add Label For Attachment]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Add Rows in MRVS/README|Add Rows in MRVS]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Auto Save Draft Feature/README|Auto Save Draft Feature]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Autofilling the request details from previous request/Readme|Autofilling the request details from previous request]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Autopopulate Department/README|Autopopulate Department]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Autopopulate user information fields/README|Autopopulate user information fields]]
