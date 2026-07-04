---
title: "Checklist Items Not Saving After Migrating to \"Case SRP\" Variant in HR Configurable Workspace"
aliases:
  - KB2633442
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2633442
kb_number: KB2633442
last_modified: 2026-01-03
---

## Checklist Items Not Saving After Migrating to "Case SRP" Variant in HR Configurable Workspace

  

### Issue

After migrating to the "Case SRP" variant of the Record Page in HR Configurable Workspace, checklist items are not saving when added or edited by HR Agents.  
The issue occurs during attempts to add or edit checklist items in active HR cases; changes are not retained after saving.

### Release

Any Release

### Cause

The supporting script include `hr_ChecklistUtil` in the Human Resource Core Family plugin did not have the latest code due to previous customization, causing the `addOrUpdateItemsInChecklist` method to be missing.

### Resolution

-   Reverted the code for `hr_ChecklistUtil` to the latest App Store version, restoring the missing method.
-   Verified that checklist item saving functionality was restored after reverting.
-   Implemented a preventative measure by setting "Replace on upgrade" to `true` in sys\_update\_xml to avoid future upgrade issues.
