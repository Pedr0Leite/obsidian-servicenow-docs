---
title: "Send SMS workflow activity will not display assignment_group.name value in the SMS "
aliases:
  - KB0715283
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0715283
kb_number: KB0715283
last_modified: 2026-04-17
---

## Send SMS workflow activity will not display assignment\_group.name value in the SMS

  

### Issue

# Symptoms

* * *

SMS will have assignment\_group.name value as empty

# Release

* * *

Kingston Patch7

# Cause

* * *

This is a known issue in the platform and a PRB was logged PRB1253516 and the issue is fixed in London

# Resolution

* * *

The issue occurs because there is another workflow scratchpad variable named "assignment\_group" in the If activity of the workflow named "More escalation levels available". The "sys\_id" of the assignment group is assigned to that variable.

Due to this reason, the "Send SMS" activity will grab the value of the workflow scratchpad variable (which is the sys\_id) instead of the current record's field value.

So to avoid this issue, define another workflow scratchpad variable in the if activity "More escalation levels available" and assign that variable the name of the assignment group and reference that scratchpad variable in the "Send SMS" activity.
