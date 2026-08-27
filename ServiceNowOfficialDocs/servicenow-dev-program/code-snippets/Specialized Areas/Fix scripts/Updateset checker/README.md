---
title: "Updateset checker"
aliases:
  - Updateset checker
tags:
  - servicenow-dev-program
  - code-snippet
  - updateset-checker
  - fix-scripts
---

# Check all Work in Progress update-sets for Cross Application Scopes
If an update-set has more than one application scope it will cause issues when you are previewing the update-set in the target instance. Therefore, it is the best to check the update-sets before closing and retrieving them to the target instance. 

This sample script, checks all the WIP update-sets and find the update-sets that has more than one Application Scope in them. It will show which update-set and whose update is causing it.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Fields On All List Views/README|Add Fields On All List Views]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Variable set to multiple catalog items/README|Add Variable set to multiple catalog items]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add bulk users to VTB/README|Add bulk users to VTB]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Adjust Variable Order on Catalog Item/README|Adjust Variable Order on Catalog Item]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Anonymise Data/README|Anonymise Data]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Assign user list to a specific group/README|Assign user list to a specific group]]
