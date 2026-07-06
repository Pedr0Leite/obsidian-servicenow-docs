---
title: "All Application CI of a particular type changed names (example: Weblogic CIs)"
aliases:
  - KB0688226
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0688226
kb_number: KB0688226
last_modified: 2024-04-07
---

## All Application CI of a particular type changed names (example: Weblogic CIs)

  

### Issue

# Symptoms

* * *

All Application of a particular CI Type changed their names at the same time.

# Release

* * *

All Releases

# Cause

* * *

-   There is a Business Rule called 'Rename' on the 'discovery\_classy\_proc' table which runs on update to the Classifier's name.
-   The Business Rule's code will query all Application CI Type linked to the Classifier and changed their names accordingly
-   New names have the the following format: <new classifier name>@host

# Resolution

* * *

Do not rename Process Classifiers. If you must do it, disable the 'Rename' business rule first before doing so.
