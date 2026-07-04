---
title: " Standard change template causes an error when opening a change from it as description is too long"
aliases:
  - KB0722999
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0722999
kb_number: KB0722999
last_modified: 2024-04-07
---

## Standard change template causes an error when opening a change from it as description is too long

  

### Issue

When the standard change template is selected it shows an error page

### Release

ALL

### Cause

The customizations made to the processor named "StdChangeProcessor"

### Resolution

The issue is with the "std\_change\_processor" not returning any response.  
The "StdChangeProcessor"(std\_change\_processor) and it was customized entirely.
