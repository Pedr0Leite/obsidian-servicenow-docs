---
title: "The product shows compliance even though there is a license deficit (negative license requirement)."
aliases:
  - KB2688384
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2688384
kb_number: KB2688384
last_modified: 2025-12-18
---

## The product shows compliance even though there is a license deficit (negative license requirement).

  

### Issue

In SAM Workspace, observed product shows complaint even though we have the a negative count on the license required.

### Release

N/A

### Resolution

This behavior is expected when an Enterprise License Agreement (ELA) is in place. Under an ELA, license compliance is not evaluated in real time based on usage versus owned licenses. Instead, compliance is assessed at the end of the contract period, allowing temporary over-usage during the term. As a result, products may appear compliant even when the required license count exceeds the owned quantity.
