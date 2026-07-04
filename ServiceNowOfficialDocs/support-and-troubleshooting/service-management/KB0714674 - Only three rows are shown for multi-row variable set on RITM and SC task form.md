---
title: "Only three rows are shown for multi-row variable set on RITM and SC task  form"
aliases:
  - KB0714674
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0714674
kb_number: KB0714674
last_modified: 2024-04-07
---

## Only three rows are shown for multi-row variable set on RITM and SC task form

  

### Issue

# Symptoms

* * *

Only three rows are shown for multi-row variable set on RITM and SC task form. Any new rows added to the variable set on RITM and SC task form are not visible.

we can see all the rows added by inspecting the variable set element on browser tools.

# Release

* * *

London

# Environment

* * *

List V3

# Cause

* * *

This issue is caused by List V3. 

The following problem has been created to address this issue:

PRB1352911 Variable Editor only displays three records of a multi-row variable set when List v3 is active

# Resolution

* * *

As a workaround please use list v2. Follow below steps to disable List v3 globally

-   Navigate to System Properties > List v3.
-   Locate the property called Enable List v3 (glide.ui.list\_v3.enable) and clear the check box.
-   Click Save.
