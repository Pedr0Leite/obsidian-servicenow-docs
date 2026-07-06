---
title: "State field on discovery status record says \"Completed\" even though the schedule is still running"
aliases:
  - KB0725879
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725879
kb_number: KB0725879
last_modified: 2024-04-07
---

## State field on discovery status record says "Completed" even though the schedule is still running

  

### Issue

The "state" field on discovery status record would say "Completed" even though the schedule is still running, and keeps adding records to the ECC queue

### Release

All Versions.

### Resolution

This can possibly happen because of the "Discovery - Complete" business rule, which is responsible for updating the the state field. This business rule is triggered when the "completed" field has a value greater than or equal to "started" field, and marks the state as "Completed"

This situation is possible sometimes when an output probe is re-processed, thereby having more than one input probe for an output.

**Note:** For multipage payloads, there is a check in place, to consider multiple input probes as the same as long as they are corresponding to the same output probe
