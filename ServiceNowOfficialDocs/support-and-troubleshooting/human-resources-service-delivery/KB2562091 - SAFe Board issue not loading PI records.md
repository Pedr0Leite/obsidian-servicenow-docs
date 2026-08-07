---
title: "SAFe Board issue not loading PI records"
aliases:
  - KB2562091
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2562091
kb_number: KB2562091
last_modified: 2026-06-19
---

## SAFe Board issue not loading PI records

  

### Issue

When trying to open an ART record from the SAFe Board, the system keeps loading infinitely.

### Release

-   Any supported release.

### Cause

This can happen if there are duplicate sprints in the \[sn\_safe\_program\_sprint\] table with the same start and end dates for the selected Program Increment (PI). The correct sprint records for the PI are located in the \[sn\_safe\_sprint\] table.

### Resolution

First suggestion is to remove the duplicated entries from \[sn\_safe\_program\_sprint\]

If you want to change the program sprints on some of them, please check:

1.  As it is not possible to directly update the program sprints on SAFe sprints, which are read-only, consider updating the fields using a background script. Note: Rollup fields like capacity will not be correctly updated.
2.  We have a Business Rule, "Rollup capacity to program sprint", which handles the rollup on \[sn\_safe\_sprint\], but its condition will not be met when updating only the program sprints. I suggest creating a temporary replica of this Business Rule with a condition that executes when the program sprint changes.
3.  Please test these in any test instance first.

Additional Business Rules related to this process to consider:

-   Rollup capacity to program incr insert: We need to execute this Business Rule to update Program Sprint Capacity. It's the same as "Rollup capacity to program sprint".
-   Rollup capacity for update or delete: No need to execute on program increment update. Updating the team points with the above Business Rule on the \[sn\_safe\_program\_sprint\] table will trigger it.
-   Rollup capacity to program sprint: No need to execute on program increment update.
-   Sync Team Sprint with Program Sprint: Need to be executed to update planned dates on safe sprints where program increment is updated.
