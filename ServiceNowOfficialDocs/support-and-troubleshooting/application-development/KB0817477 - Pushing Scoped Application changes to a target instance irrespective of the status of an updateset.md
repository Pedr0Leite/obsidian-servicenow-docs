---
title: "Pushing Scoped Application changes to a target instance irrespective of the status of an updateset"
aliases:
  - KB0817477
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0817477
kb_number: KB0817477
last_modified: 2024-04-08
---

## Pushing Scoped Application changes to a target instance irrespective of the status of an updateset

  

### Issue

The changes of a Scoped Application can be pushed to a target instance via AppRepo, irrespective of the status of an updateset

### Release

ALL

### Resolution

-   The status of an updateset does not impact the ability to capture changes in a scoped Application.
-   That is, irrespective of the status of an updateset, despite it being in progress, changes can be captured in AppRepo.
-   The changes can then be installed on a target instance.
-   This is expected behavior
