---
title: "Knowledge Category Picker is opening a list view instead of picker UI"
aliases:
  - KB0715643
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0715643
kb_number: KB0715643
last_modified: 2024-04-07
---

## Knowledge Category Picker is opening a list view instead of picker UI

  

### Issue

# Symptoms

* * *

The knowledge category field is displaying a list view rather than the category picker ui popup.

# Release

* * *

London Patch 1 Hot Fix 2 

# Cause

* * *

A new version of the kb\_category\_reference\_lookup ui macro was added to your instance; however, the older (duplicate) version is causing a conflict.

# Resolution

* * *

Delete the duplicate version of the ui macro.
