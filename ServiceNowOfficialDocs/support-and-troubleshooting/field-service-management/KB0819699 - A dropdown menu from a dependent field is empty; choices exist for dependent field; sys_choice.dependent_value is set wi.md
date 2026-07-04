---
title: "A dropdown menu from a dependent field is empty; choices exist for dependent field; sys_choice.dependent_value is set with values"
aliases:
  - KB0819699
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0819699
kb_number: KB0819699
last_modified: 2024-10-12
---

## Issue

A dropdown menu in form empty. The dropdown is from a field that depends on a selection from another field.  For example, incident.subcategory depends on incident.category.  In this case, the dropdown from incident.subcategory is empty. 

After looking at the sys\_dictionary record for incident.subcategory, we see that there exists choices (sys\_choice entries).

We have also confirmed the entries have a value specified in

sys\_choice.depenent\_value 

The field corresponding to the correct sys\_choice.dependent\_value field above is being selected   and the dropdown is still empty.

## Resolution

Do not use invalid characters like ' in the sys\_choice.dependent\_value
