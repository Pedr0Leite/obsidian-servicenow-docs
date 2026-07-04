---
title: "Generated PDF contract font is white in color"
aliases:
  - KB0955108
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0955108
kb_number: KB0955108
last_modified: 2026-06-25
---

## Generated PDF contract font is white in color

  

### Issue

Generated PDF documents have white font set

### Release

Any

### Cause

Misconfiguration of the iTextPDFUtil script include 

### Resolution

Ensure that the script include has the following value set on line #143  
  
  
"

 var color = (new iTextPDFUtil.Color('0xff000000'));  
"
