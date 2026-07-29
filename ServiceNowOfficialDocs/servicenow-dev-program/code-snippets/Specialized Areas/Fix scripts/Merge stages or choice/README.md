---
title: "Merge stages or choice"
aliases:
  - Merge stages or choice
tags:
  - servicenow-dev-program
  - code-snippet
  - merge-stages-or-choice
  - fix-scripts
---

# Merge Stages/choices into one choice

Sometimes we start with flow/process where we have multiple stages for a particular document.
After the document is in production and we merge multiple stages into one to refine process we may need to modify stale data to keep it in sync with new process.

Use old stages and new stages (or choice values)
E.g.
Old Stage: New(new), Open(open), Draft(draft)
New Stage: Initiate(initiate)

This script will help to correct data and will update old stages data with new stage value.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Fields On All List Views/README|Add Fields On All List Views]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Variable set to multiple catalog items/README|Add Variable set to multiple catalog items]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add bulk users to VTB/README|Add bulk users to VTB]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Adjust Variable Order on Catalog Item/README|Adjust Variable Order on Catalog Item]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Anonymise Data/README|Anonymise Data]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Assign user list to a specific group/README|Assign user list to a specific group]]
