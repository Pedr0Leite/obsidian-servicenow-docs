---
title: "Workflow timer taking excessive time, and as a result, the workflow is hung"
aliases:
  - KB0824553
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0824553
kb_number: KB0824553
last_modified: 2025-10-22
---

## Workflow timer taking excessive time, and as a result, the workflow is hung

  

### Issue

The user had a Requested Item with a Timer workflow activity in it. The workflow was hung at the Timer activity for excessive amounts of time (e.g. the Timer was for 2 seconds, and the Timer was still processing after days).

### Release

All

### Resolution

In this case, the issue was that the user had created a custom and _recursive_ async Business Rule that backed up the event queue by over 10 million records.  
  
The reason this is impactful for workflow Timers is that when a workflow Timer activity executes in a workflow, a sys\_trigger record is created with a "Next action" at the time when the Timer should end (current time + duration specified in the Timer activity = the "Next action" time).

If the event queue is backed up with many sys\_trigger jobs, workflow Timer sys\_trigger records will not be able to perform the action at the correct "Next action" time - this will be delayed.
