---
title: "Process classifier not triggering pattern or probe"
aliases:
  - KB0783614
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783614
kb_number: KB0783614
last_modified: 2024-04-08
---

## Process classifier not triggering pattern or probe

  

### Issue

Process classifier not triggering pattern or probe.

### Release

All currently supported releases.

### Cause

The ApplicationDependencyMapping, ADM, script include checks if there are any process handlers for the process before classifying it. The ApplicationDependencyMapping checks discovery\_proc\_handler table for process handlers, see ApplicationDependencyMapping.shouldSkipCondition() for reference. The process handlers has a "classify" field. The ADM will not trigger probes/patterns if "classify" = false for a process.

To confirm

1.  open the cmdb\_running\_process and check that the field "classify" = false.

### Resolution

Set the process handler field "active" = false.
