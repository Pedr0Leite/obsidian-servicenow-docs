---
title: "Custom Script Include is throwing the JavaScript Error \"Cannot convert null to an object\""
aliases:
  - KB0717159
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0717159
kb_number: KB0717159
last_modified: 2024-04-07
---

## Custom Script Include is throwing the JavaScript Error "Cannot convert null to an object"

  

### Issue

A custom script include is throwing an error after London upgrade: "Cannot convert null to an object"

### Release

All release since London

### Cause

Error occurs when creating a var with getGlideObject().getQuestion().getLabel() for variable data or having it inside an if statement.

### Resolution

Add a null check for getGlideObject() or write the variable as v.getGlideObject()+v.getQuestion.getLabel()
