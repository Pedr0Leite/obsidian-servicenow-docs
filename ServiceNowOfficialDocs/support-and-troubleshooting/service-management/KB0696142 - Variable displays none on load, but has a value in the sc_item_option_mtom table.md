---
title: "Variable displays none on load, but has a value in the sc_item_option_mtom table"
aliases:
  - KB0696142
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696142
kb_number: KB0696142
last_modified: 2024-04-07
---

## Variable displays none on load, but has a value in the sc\_item\_option\_mtom table

  

### Issue

# Symptoms

* * *

When loading a catalog task, a variable displays 'None'; however, the value of the variable on the sc\_item\_option\_mtom table is saved and updated correctly. 

# Release

* * *

Istanbul Patch 11, Kingston Patch 7

# Cause

* * *

The format of the double quotation marks (curly quotations) for the lookup select box are unsupported and is causing the issue when returning the value to the form.

# Resolution

* * *

Replace the unsupported characters with the supported format.
