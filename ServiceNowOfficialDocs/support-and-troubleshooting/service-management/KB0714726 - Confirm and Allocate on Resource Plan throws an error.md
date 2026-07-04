---
title: "Confirm and Allocate on Resource Plan throws an error"
aliases:
  - KB0714726
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0714726
kb_number: KB0714726
last_modified: 2024-04-07
---

## Confirm and Allocate on Resource Plan throws an error

  

### Issue

# Symptoms

* * *

When selecting Confirm & Allocate on a requested resource plan the following error is displayed:

User \[User\_Name\] could not be allocated for the period \[date\_range\] as the user is not available for one or more days in the period

This occurs with all resource plans.

# Release

* * *

London Patch 1

# Cause

* * *

Customized ResourcePlan script include is causing the error. 

# Resolution

* * *

Revert to out of box ResourcePlan script include.
