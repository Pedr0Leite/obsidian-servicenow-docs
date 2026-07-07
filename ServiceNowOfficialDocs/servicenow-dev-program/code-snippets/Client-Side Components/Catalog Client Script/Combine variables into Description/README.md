---
title: "Combine variables into Description"
aliases:
  - Combine variables into Description
tags:
  - servicenow-dev-program
  - code-snippet
  - combine-variables-into-description
  - catalog-client-script
---

OnSUbmit Catalog Client script is created to Combine all variable values required and display in Description field.
Steps:
1. Navigate to your instance open catalog client script table [catalog_script_client]
2. Create new catalog client script -> click new
3. Provide following values:
      - Name: Any relevant to your script
      - Applies to: A catalog Item
      - UI Type: All
      - Isolated script: checked
      - Application: Application scope applies to
      - Type: onSubmit
      - Catalog item: select your catalog item
 4. create the script as per script.js file.  

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Add Label For Attachment/README|Add Label For Attachment]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Add Rows in MRVS/README|Add Rows in MRVS]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Auto Save Draft Feature/README|Auto Save Draft Feature]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Auto-populate field from URL/README|Auto-populate field from URL]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Autofilling the request details from previous request/Readme|Autofilling the request details from previous request]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Autopopulate Department/README|Autopopulate Department]]
