---
title: "Catalog item form value does not captured into RITM after form submission"
aliases:
  - KB0720634
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0720634
kb_number: KB0720634
last_modified: 2024-10-09
---

## Catalog item form value does not captured into RITM after form submission

  

### Issue

Few of the variables values are missing on the request item form, when submitting the catalog item.

### Release

ALL

### Cause

customized catalog client script which is running on load, resetting the values of the variables.

### Resolution

The issue is happening due to the customized catalog client script. 

Suggested to uncheck the 'Applies to Request item' field on the catalog client script to avoid resetting the variable values on the RITM
