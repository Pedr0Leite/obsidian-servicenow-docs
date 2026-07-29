---
title: "window.location.replace() in IE does not work"
aliases:
  - KB0684478
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0684478
kb_number: KB0684478
last_modified: 2024-08-28
---

## Issue

Global UI Scripts (redirect scripts) using window.location.replace() do not work in Internet Explorer.

## Resolution

Use window.location=<URL> instead of window.location.replace().
