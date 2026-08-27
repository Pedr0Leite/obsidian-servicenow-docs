---
title: "News Feed Widget Displays \"Published Invalid Date\" in News Center"
aliases:
  - KB2650998
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2650998
kb_number: KB2650998
last_modified: 2026-01-01
---

## News Feed Widget Displays "Published Invalid Date" in News Center

  

### Issue

The News Feed widget in News Center displays “Published Invalid date” instead of the correct published date for articles. The issue occurs across multiple browsers and is reproducible on customer instances but inconsistently on OOB instances.

### Release

Any

### Cause

Known issue tracked under PRB1915724 related to date rendering in the News Feed widget for certain versions of Content Publishing.

### Resolution

-   Apply the workaround provided by ServiceNow for Content Publishing/sn\_cd version 35.0.12:
    -   Import the update set `update_set_workaround_v35.0.12.xml` into the affected instance.
    -   Commit the update set and validate that the News Feed widget displays correct published dates.
-   Upgrade to Content Experiences Bundle version 36.0.5 or later to receive the permanent fix.
-   Verify the widget behavior after upgrade to ensure the issue does not recur.
