---
title: "Set User Field Values on Load"
aliases:
  - Set User Field Values on Load
tags:
  - servicenow-dev-program
  - code-snippet
  - set-user-field-values-on-load
  - catalog-client-script
---

On Load Catalog client script is created to auto set the field values and make that field read only
 - Navigate to your instance -> App Navigator > Open Catalog CLient Script [catalog_script_client]
 - Set following field Values
        - Name: xyz
        - Applies to: A Catalog item
        - Type: onLoad
        - Catalog item: Select your Catalog item
        - UI Type: All
        - Isolated script: Checked
  -  Create the script as per script.js file.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Add Label For Attachment/README|Add Label For Attachment]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Add Rows in MRVS/README|Add Rows in MRVS]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Auto Save Draft Feature/README|Auto Save Draft Feature]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Auto-populate field from URL/README|Auto-populate field from URL]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Autofilling the request details from previous request/Readme|Autofilling the request details from previous request]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Autopopulate Department/README|Autopopulate Department]]
