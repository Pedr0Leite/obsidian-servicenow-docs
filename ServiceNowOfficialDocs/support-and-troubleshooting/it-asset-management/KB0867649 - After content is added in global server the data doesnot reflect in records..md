---
title: "After content is added  in global server the data doesnot reflect in records."
aliases:
  - KB0867649
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0867649
kb_number: KB0867649
last_modified: 2023-11-17
---

## Issue

We got assistance from content team to update content and it has been added to the server but we do not see it update on the instance.

  

  

## Resolution

This usually happens when on the publisher record has stage column as empty. In this case there was a custom publisher created in samp\_sw\_publisher  which is incorrect. For custom publishers the table should be samp\_custom\_sw\_publisher.LIST

Once we ensure that the publisher in samp\_sw\_publisher table has stage column correctly populated, the schedule job "SAM - Apply latest content changes" runs across successfully and updates the records as expected.
