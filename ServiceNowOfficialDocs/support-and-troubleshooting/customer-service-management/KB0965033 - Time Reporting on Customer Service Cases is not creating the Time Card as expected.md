---
title: "Time Reporting on Customer Service Cases is not creating the Time Card as expected"
aliases:
  - KB0965033
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0965033
kb_number: KB0965033
last_modified: 2026-02-04
---

## Time Reporting on Customer Service Cases is not creating the Time Card as expected

  

### Issue

When using the **"Record Time" Button** on your **Customer Service Case Records** you are finding that the **Time Cards** are not being created as expected.

This is happening even though the **Task Time Worked Records** are still being generated.

### Cause

This was happening because the **"TimeRecordingHelper" Script Include** had been **customised** and had some **Skipped Upgrades**.

You should also check the **"Update time card for TimeRecording" Business Rule** for **customisations** since this is the **Business Rule** which calls the above **Script Include.**

### Resolution

Please ensure you **revert** the **"TimeRecordingHelper" Script Include** and **"Update time card for TimeRecording" Business Rule** to **Out Of Box.**

Any customisations can be re-applied as necessary after this.
