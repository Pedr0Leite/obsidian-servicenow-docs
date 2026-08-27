---
title: "Spaces are not showing as available in after creating the AutoCAD tags for the Floor Plan"
aliases:
  - KB0954332
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0954332
kb_number: KB0954332
last_modified: 2024-01-27
---

## Spaces are not showing as available in after creating the AutoCAD tags for the Floor Plan

  

### Issue

Spaces are not showing as available in after creating the AutoCAD tags for the Floor Plan

### Cause

Cause - Block Reference has a Text field and Attribute Definition. We don't process Text field. Attribute Definition is too small.

### Resolution

Issue 1 - DXF file was not loading in AutoCad, fixed it by saving dwg file in dxf format.  
Issue 2 - After dxf import, we can see space has got created in space table. After selecting the floor in 'Reserve Space for a Day', created space is displayed on the map but not selectable and green.  
  
Fix - Deleted Text field from Block Reference ad increased Attribute Definition's height from 0.2 to 200.
