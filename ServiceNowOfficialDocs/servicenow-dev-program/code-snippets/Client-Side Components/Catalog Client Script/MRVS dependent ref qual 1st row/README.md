---
title: "MRVS dependent ref qual 1st row"
aliases:
  - MRVS dependent ref qual 1st row
tags:
  - servicenow-dev-program
  - code-snippet
  - mrvs-dependent-ref-qual-1st-row
  - catalog-client-script
---

This Catalog Client Script and Script Include are used with a reference qualifier similar to
javascript: 'disable=false' + session.getClientData('selected_dept');

The scenario is a MRVS with a reference variable to the customer account table.  When an (active) account is selected in the first row, subsequent rows should only be able to select active accounts in the same department as the first account.

The Catalog Client Script will pass the first selected account (if there is one) to a Script Include each time a MRVS row is added or edited.  The Script Include will pass the department name to the reference qualifier.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Add Label For Attachment/README|Add Label For Attachment]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Add Rows in MRVS/README|Add Rows in MRVS]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Auto Save Draft Feature/README|Auto Save Draft Feature]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Auto-populate field from URL/README|Auto-populate field from URL]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Autofilling the request details from previous request/Readme|Autofilling the request details from previous request]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Autopopulate Department/README|Autopopulate Department]]
