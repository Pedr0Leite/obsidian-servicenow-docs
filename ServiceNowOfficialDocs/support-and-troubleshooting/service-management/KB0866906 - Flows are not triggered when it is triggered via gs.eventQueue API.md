---
title: "Flows are not triggered when it is triggered via gs.eventQueue API"
aliases:
  - KB0866906
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0866906
kb_number: KB0866906
last_modified: 2023-10-31
---

## Issue

Flows are not triggered when it is triggered via gs.eventQueue API

## Resolution

create a new property "trigger\_engine.ignore.set\_workflow" and set the value as "true"
