---
title: "Check if Fiscal Year is safe for deletion"
aliases:
  - Check if Fiscal Year is safe for deletion
tags:
  - servicenow-dev-program
  - code-snippet
  - check-if-fiscal-year-is-safe-for-deletion
  - fix-scripts
---

You can do a lot of damage related to data corruption and impacted financials if you delete your Fiscal Periods/Fiscal Year when it's already in use with live data like Cost Plans and Benefit Plans. 

This will validate a single Fiscal Year to validate it's not used yet and safe for deletion if your Fiscal Periods have Validation issues.

Use this in the [System Definition > Scripts - Background] module. Enter in the Fiscal Year by display name on line 2.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Fields On All List Views/README|Add Fields On All List Views]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Variable set to multiple catalog items/README|Add Variable set to multiple catalog items]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add bulk users to VTB/README|Add bulk users to VTB]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Adjust Variable Order on Catalog Item/README|Adjust Variable Order on Catalog Item]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Anonymise Data/README|Anonymise Data]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Assign user list to a specific group/README|Assign user list to a specific group]]
