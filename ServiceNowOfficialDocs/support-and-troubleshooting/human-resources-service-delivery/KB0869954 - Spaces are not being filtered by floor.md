---
title: "Spaces are not being filtered by floor"
aliases:
  - KB0869954
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0869954
kb_number: KB0869954
last_modified: 2024-01-31
---

## Spaces are not being filtered by floor

  

### Issue

When selecting the catalog item “Reserve a Shift and Space for a Day”, spaces from all floors are available to select.

### Cause

When 'Area' variable is not used, the reference qualifier for 'Space' variable needs to be updated.

### Resolution

This is related to the configuration of removing or not using the 'Area' variable. In this scenario, the reference qualifier needs to be updated on the 'Space' variable:

Out of box code

_if(current.variables.area != '')_ 

Change to  

_if(current.variables.area)_
