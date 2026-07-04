---
title: "New HR Case getting closed on being transferred via Transfer case option."
aliases:
  - KB0856355
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0856355
kb_number: KB0856355
last_modified: 2025-09-03
---

## Issue

Whenever there is any case transferred from any HR Service to another, the case automatically gets closed instead should be in ready state.

## Resolution

In this case there was a custom workflow where state = closed complete was explicitly set which was causing the issue.
