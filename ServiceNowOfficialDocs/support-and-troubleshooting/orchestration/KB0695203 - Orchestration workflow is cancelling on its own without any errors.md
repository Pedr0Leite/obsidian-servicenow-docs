---
title: "Orchestration workflow is cancelling on its own without any errors "
aliases:
  - KB0695203
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695203
kb_number: KB0695203
last_modified: 2024-04-07
---

## Orchestration workflow is cancelling on its own without any errors

  

### Issue

## Description

Orchestration workflow is being canceled on its own without any errors seen in the activities. 

## Probable Cause:

It could be that max\_activity\_count workflow variable has been reached either because it has been customized with a low number or the workflow has a loop somewhere that keeps on adding to the activity count.

Increasing this variable beyond the default value (100) is not the optimal solution as it is created to prevent infinite loops. 

## Suggestion:

Identify where the loop is and ask the customer to change their design to avoid wasting resources.

For example, if the workflow has a timer activity that controls the loop then maybe suggest "Wait for WF Event" event to be implemented instead.
