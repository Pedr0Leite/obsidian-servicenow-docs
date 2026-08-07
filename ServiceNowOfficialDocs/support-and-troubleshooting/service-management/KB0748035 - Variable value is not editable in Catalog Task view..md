---
title: "Variable value is not editable in Catalog Task view."
aliases:
  - KB0748035
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748035
kb_number: KB0748035
last_modified: 2024-04-07
---

## Variable value is not editable in Catalog Task view.

  

### Issue

Unable to change the value of a variable within a Catalog Task

### Release

ALL

### Cause

In this case, the behavior experienced is due to a UI Policy which is setting the variable to read-only (a Client Script can cause the same kind of behavior). Hence, the value cannot be changed/edited.

### Resolution

If it is required that the variable value be modifiable, the user can either make the UI Policy active false or place some condition upon it whereby the variable is read-only to a select group of users and editable to another group of users - whatever best meets the business needs of the user.
