---
title: "Updating journal fields fails to trigger Flow Designer"
aliases:
  - KB0753763
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0753763
kb_number: KB0753763
last_modified: 2025-08-01
---

## Updating journal fields fails to trigger Flow Designer

  

### Issue

When updating fields, like work notes or additional comments, Flow Designer fails to start. 

### Release

Beginning with London release

### Cause

In Flow Designer, if the flow has trigger conditions **Record inserted or updated** on the incident table, the flow will not trigger with journal field updates.

### Resolution

To resolve this, change the **Run trigger** on the flow to **Only if not currently running**.
