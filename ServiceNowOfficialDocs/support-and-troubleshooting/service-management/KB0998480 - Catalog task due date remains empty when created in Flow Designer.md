---
title: " Catalog task due date remains empty when created in Flow Designer"
aliases:
  - KB0998480
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0998480
kb_number: KB0998480
last_modified: 2025-08-28
---

## Catalog task due date remains empty when created in Flow Designer

  

### Issue

When a catalog task is created through Flow Designer, the due date field remains empty even when duration is configured. This article explains the cause and provides a solution.

### Release

All supported releases

### Cause

This is default system behavior. 

The due date is not automatically set on catalog tasks when using Flow Designer, unlike when using Workflow Editor. 

In Workflow Editor, when a user does not specify a due date, the system calculates it using the '\_setDueDate' function in the "WFCreateTaskActivityUtils" script include, based on the task's creation time. 

In Flow Designer, however, the system does not set a default due date unless the user explicitly specifies the due date field. This difference is intentional by design. 

### Resolution

To set the due date for catalog tasks created in Flow Designer, implement custom logic to populate the due date field in the catalog task.

Consider submitting an enhancement request through the [Idea Portal](https://community.servicenow.com/community?id=community_static&content_id=91acf933db9ff740d82ffb24399619f5). The product team evaluates these ideas for potential inclusion in future releases.
