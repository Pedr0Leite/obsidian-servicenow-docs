---
title: "Add Standard Change Model"
aliases:
  - Add Standard Change Model
tags:
  - servicenow-dev-program
  - code-snippet
  - add-standard-change-model
  - background-scripts
---

Add the OOTB "Standard Change" model to an existing change record. OOTB, the Standard Change model is applied through an onDisplay business rule, and is not an available choice from the Model field. If you have migrated to use Change Models and generate some change requests with scripts, you may need to add the model with a background script if there is already an existing workflow context or if the model is not set by the generation script. The setter portion can be added to an existing generation script to prevent future need for this background script.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Adding bookmark to Favorites tab/README|Adding bookmark to Favorites tab]]
