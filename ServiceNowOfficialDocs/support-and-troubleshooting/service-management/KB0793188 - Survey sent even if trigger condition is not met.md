---
title: "Survey sent even if trigger condition is not met"
aliases:
  - KB0793188
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0793188
kb_number: KB0793188
last_modified: 2025-02-04
---

## Issue

As survey trigger condition when incident resolution code is not "Closed/Resolved by Caller" Or "Converted to Request",

it should trigger survey, but the survey getting triggered always.

## Resolution

Modify the condition such as none of the closure code will be satisfied.  
  
Sample condition :

Resolution code is not one of: Closed/Resolved by Caller/ Converted to Request
