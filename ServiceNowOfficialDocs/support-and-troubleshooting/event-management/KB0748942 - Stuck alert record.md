---
title: "Stuck alert record"
aliases:
  - KB0748942
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748942
kb_number: KB0748942
last_modified: 2024-04-07
---

## Stuck alert record

  

### Issue

# Description

Event Management Dashboard shown a red tile. When click on the red tile, a relevance Alert record display. When click on the Alert record, it redirected to "Record Not Found" page.

This could happen if a customer accidentally delete the alert record from "em\_alert" table via background script.

Event Management Dashboard is referring to "em\_alert\_history" table.

# Procedure

Go to "em\_alert\_history" table and find the matching Alert number record. Delete the record from "em\_alert\_history" table

# Applicable Versions

Any
