---
title: "Resume case for HR LE case failing/not working"
aliases:
  - KB2534557
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2534557
kb_number: KB2534557
last_modified: 2025-12-15
---

## Issue

Resume case UI action is not working as expected in HR cases.

## Resolution

Workaround:

Updating the below line in invokeErroredActivitySetWorkflow method in sn\_hr\_le.hr\_ActivitySet script include fixes the issue.

inputs\['subject\_person'\] = grCase.subject\_person;  
\->  
inputs\['subject\_person'\] = grCase.subject\_person.sys\_id;

Refer to PRB1942195
