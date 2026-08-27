---
title: "Make Variable Editor Read Only for Catalog Items containing MRVS"
aliases:
  - Make Variable Editor Read Only for Catalog Items containing MRVS
tags:
  - servicenow-dev-program
  - code-snippet
  - make-variable-editor-read-only-for-catalog-items-containing-mrvs
  - client-scripts
---

# Make Variable Editor Read Only for Catalog Items which have a Multi Row Variable Set
Create an onLoad Client Script which would call a Script Include and pass in the Catalog Item sys_id to check if the Catalog Item contains a MRVS. The script has been tailored to work with the Requested Item table. To make it work for any other table which has the Variable Editor replace the field "cat_item" with the field containing the details of the Catalog Item

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort action when description is empty/ReadMe|Abort action when description is empty]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort direct incident closure without Resolve State/readme|Abort direct incident closure without Resolve State]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Field Decoration/README|Add Field Decoration]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Image to Field Based on Company/README|Add Image to Field Based on Company]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Adding Placeholder on Resolution Notes/README|Adding Placeholder on Resolution Notes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Auto Update Priority based on Impact and Urgency/readme|Auto Update Priority based on Impact and Urgency]]
