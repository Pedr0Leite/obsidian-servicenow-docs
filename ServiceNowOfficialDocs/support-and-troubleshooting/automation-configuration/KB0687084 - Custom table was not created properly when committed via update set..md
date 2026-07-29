---
title: "Custom table was not created properly when committed via update set."
aliases:
  - KB0687084
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0687084
kb_number: KB0687084
last_modified: 2024-04-07
---

## Custom table was not created properly when committed via update set.

  

### Issue

# Symptoms

* * *

Custom table was not created properly when committed via update set.

# Release

* * *

All

# Cause

* * *

-   Manually modifying <system\_xml\_records> and moving them between update sets is a consistent source of errors. 
-   The table was originally created in another update set and then the update records were manually moved to the other update set.

# Resolution

* * *

Delete and re-capture the table creation. If the creation of a table or column is accidentally captured in the wrong update set, delete it and recreate it in the correct update set instead of attempting to move it manually.
