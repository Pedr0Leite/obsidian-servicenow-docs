---
title: "GRC - Published Policy not showing text when KB is created"
aliases:
  - KB0692105
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0692105
kb_number: KB0692105
last_modified: 2024-04-07
---

## GRC - Published Policy not showing text when KB is created

  

### Issue

GRC - Published Policy not showing text when KB is created

### Release

KP4

### Cause

The properties "glide.html.sanitize\_all\_fields" and "glide.ui.escape\_all\_script" is set to "false" 

### Resolution

The properties "glide.html.sanitize\_all\_fields" and "glide.ui.escape\_all\_script" is set to "false". Due to this reason, whenever the HTML field was parsed, we were seeing the "Parse Exception" as the fields were not sanitized.

  

So enabling the properties to true would resolve this issue.
