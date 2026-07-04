---
title: "HR Profile Update Fails in Clone – Duplicate Role Entries"
aliases:
  - KB2657283
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2657283
kb_number: KB2657283
last_modified: 2026-01-01
---

## HR Profile Update Fails in Clone – Duplicate Role Entries

  

### Issue

Users are unable to save changes to the HR profile in a Clone instance due to performance issues and multiple errors.  
Attempts to update HR profile details in both list and form views fail with database errors.  
The issue is specific to the Clone environment and does not occur in other instances.

### Release

Any

### Cause

Duplicate entries exist in the sys\_user\_has\_role table for certain roles. These duplicates cause "Unique Key violation detected by database" errors when updating HR profiles or user roles.  
The issue originated after activating the Contextual Security: Role Management V2 plugin (`com.glide.role_management.inh_count`). Legacy V1 records were not removed, resulting in a mix of V1 and V2 data.

### Resolution

-   Do not import or restore pre-V2 sys\_user\_has\_role records into environments where V2 is active.
-   Perform a fresh clone from Production to the sub-production instance to ensure no legacy data is retained.
-   Optionally, run a role recalculation, but effectiveness may vary due to mixed data state.
-   Verify that HR profile updates work correctly after cleanup.
