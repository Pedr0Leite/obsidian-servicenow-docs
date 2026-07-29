---
title: "Regenerate the draft document created for e-signature (or) regenerate the draft document if the field values changed after the draft document had created <br />"
aliases:
  - Regenerate the draft document created for e-signature (or) regenerate the draft document if the field values changed after the draft document had created <br />
tags:
  - servicenow-dev-program
  - code-snippet
  - employee-document-management
  - fix-scripts
---

# Regenerate the draft document created for e-signature (or) regenerate the draft document if the field values changed after the draft document had created <br />

***Use case:*** The document was generated with the dynamic fields selected in the document template. But if the field values changes after document generation then these changes will not be reflected in the generated document.<br /><br />
***Solution:*** Leverage EDM utils provided OOB and call these utilities to regenerate the documents. After this script runs, a new record will be created in draft_document table. The previous version of the document in draft_document will be set to inactive

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Fields On All List Views/README|Add Fields On All List Views]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Variable set to multiple catalog items/README|Add Variable set to multiple catalog items]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add bulk users to VTB/README|Add bulk users to VTB]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Adjust Variable Order on Catalog Item/README|Adjust Variable Order on Catalog Item]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Anonymise Data/README|Anonymise Data]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Assign user list to a specific group/README|Assign user list to a specific group]]
