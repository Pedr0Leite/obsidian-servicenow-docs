---
title: "From the License WorkBench we have noticed this Error: Uncaught SyntaxError: Unexpected token '{'"
aliases:
  - KB0853571
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0853571
kb_number: KB0853571
last_modified: 2024-04-08
---

## Issue

While looking in the License Workbench and from the Inspect Element we have noticed this Syntax error "Unexpected token '{'".

However, there is no UI impact or any type functionality issues we have noticed.

  

## Resolution

Set sys\_property "glide.ui.escape\_all\_script" to "true"
