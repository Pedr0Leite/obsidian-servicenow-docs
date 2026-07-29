---
title: "HR Survey Assessment instances are not being created"
aliases:
  - KB0695356
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695356
kb_number: KB0695356
last_modified: 2024-04-07
---

## HR Survey Assessment instances are not being created

  

### Issue

# Symptoms

* * *

Survey instances are not being created in the asmt\_assessment\_instance table and no-one can access the survey. An error is seen: "Invalid URL"

# Release

* * *

Kingston Patch 6

# Cause

* * *

Custom Business Rule limiting access on the asmt\_assessment\_instance table

# Resolution

* * *

Disable the custom Business Rule that is on the asmt\_assessment\_table
