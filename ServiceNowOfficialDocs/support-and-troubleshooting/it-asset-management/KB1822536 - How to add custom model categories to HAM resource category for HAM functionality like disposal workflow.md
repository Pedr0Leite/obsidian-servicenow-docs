---
title: "How to add custom model categories to HAM resource category for HAM functionality  like disposal workflow"
aliases:
  - KB1822536
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1822536
kb_number: KB1822536
last_modified: 2025-01-31
---

## Issue

Selecting a HAM enabled existing category as the parent of your custom category will allow its assets to use HAM functionality

A new field has been added in the Model Categories called "Parent Category" that when populated with HAM enabled category will enable the custom category as well.

## Resolution

1.  Navigate to: HAM Resource Categories

Only Resource Categories with Opt in = true will allow HAM functionality.  
Note: not all of these categories can be used as a parent to enable HAM functionality  
Printers and consumables are still eligible for HAM features, but they're children are not.  
  

2\. Navigate to a custom model category

  
Update the Parent Category to network gear or appropriate Resource Category  
It is possible to have a hierarchy of model categories:  
CustomCatA is a child of CustomCatB which is a child of Network Gear.

As long as the final parent is HAM enabled non consumable it should recursively apply to all the children.

3\. Wait 24 hours there are scheduled jobs that will update the changes

4\. Now check assets that are in those custom categories and they should be enabled for HAM functionality
