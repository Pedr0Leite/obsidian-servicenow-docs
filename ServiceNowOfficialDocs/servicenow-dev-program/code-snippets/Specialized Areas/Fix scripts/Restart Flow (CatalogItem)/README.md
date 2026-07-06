---
title: "Restart Flow (CatalogItem)"
aliases:
  - Restart Flow (CatalogItem)
tags:
  - servicenow-dev-program
  - code-snippet
  - restart-flow-catalogitem
  - fix-scripts
---

# Restart a Catalog Item Flow

To be used as a fix script or background script to restart a flow for a catalog item or selection of catalog items.  Typically this might be used in a scenarion in which you've modified a Flow and need to ensure that existing items are running the current version of the flow.

Note: This will RESTART your flows from the beginning.  So if your item is in progress you may see some undesirable behavior.  Also keep in mind any notifications you may have set to fire from the Flow.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Fields On All List Views/README|Add Fields On All List Views]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Variable set to multiple catalog items/README|Add Variable set to multiple catalog items]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add bulk users to VTB/README|Add bulk users to VTB]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Adjust Variable Order on Catalog Item/README|Adjust Variable Order on Catalog Item]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Anonymise Data/README|Anonymise Data]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Assign user list to a specific group/README|Assign user list to a specific group]]
