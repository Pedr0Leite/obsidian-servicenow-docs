---
title: "Adding a Software Entitlement does not allow you to select from the list of available Software Models"
aliases:
  - KB0749923
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749923
kb_number: KB0749923
last_modified: 2024-04-07
---

## Adding a Software Entitlement does not allow you to select from the list of available Software Models

  

### Issue

# Symptoms

When attempting to add a Software Entitlement, the selection for Software Model does not give any available software models that are referenced from the cmdb\_software\_product\_model table. It just comes up empty.

# Release

All

# Cause

Normally this would not be an issue, however if the customer decides to delete all of the current software models in cmdb\_software\_product\_model and create their own, there is a chance that they will neglect to create a category in cmdb\_model\_category. If the models that they create reference a category that does not exist in that table, the lookup will fail for that item. If every item left in the cmdb\_software\_product\_model table is referencing a non existent category, the list pulled up during record creation in Software entitlements will be blank

# Resolution

1.  Navigate to cmdb\_model\_category.LIST
2.  Add the missing categories to the table
