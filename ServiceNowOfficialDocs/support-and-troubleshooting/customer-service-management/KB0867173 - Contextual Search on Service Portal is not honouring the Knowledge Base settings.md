---
title: "Contextual Search on Service Portal is not honouring the  Knowledge Base settings"
aliases:
  - KB0867173
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0867173
kb_number: KB0867173
last_modified: 2023-11-04
---

## Issue

csm portal is configured to only show knowledge articles from custom knowledge base. The portal is honouring this setting, but the Contextual Search embedded in Record Producers is showing articles from other Knowledge Bases, which are not linked to the csm portal.

## Resolution

OOB widget -  **_Contextual Search - Inline Results_** was customized.Reverting it to OOB , fixed the issue.
