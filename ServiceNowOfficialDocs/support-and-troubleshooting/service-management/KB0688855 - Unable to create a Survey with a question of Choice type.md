---
title: "Unable to create a Survey with a question of Choice type"
aliases:
  - KB0688855
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0688855
kb_number: KB0688855
last_modified: 2024-04-07
---

## Unable to create a Survey with a question of Choice type

  

### Issue

# Symptoms

* * *

When creating a new assessment with a 'choice' type question, an error is displayed on the screen: The value must be an integer.

# Release

* * *

Kingston Patch 4

# Cause

* * *

The AssessmentUtil script include was skipped during the Kingston upgrade.

# Resolution

* * *

Revert to the out of box version of the script include.
