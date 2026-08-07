---
title: "How to handle Flow Designer stages not working in For Each loops"
aliases:
  - KB0832544
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0832544
kb_number: KB0832544
last_modified: 2025-08-11
---

## How to handle Flow Designer stages not working in For Each loops

  

### Issue

When you use a For Each loop in Flow Designer, you cannot add stages in the user interface. This limitation does not affect Do Until loops or other flow logic. 

### Release

Any supported release

### Cause

This behavior occurs because Flow Designer does not support stages within For Each loops.

### Resolution

Using stages as part of a For Each loop is not supported and is not considered an error. There are no known workarounds.
