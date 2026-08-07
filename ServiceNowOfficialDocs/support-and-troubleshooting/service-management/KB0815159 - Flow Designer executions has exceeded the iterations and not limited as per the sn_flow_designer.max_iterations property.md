---
title: "Flow Designer executions has exceeded the iterations and not limited as per the sn_flow_designer.max_iterations property"
aliases:
  - KB0815159
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815159
kb_number: KB0815159
last_modified: 2025-04-08
---

## Flow Designer executions has exceeded the iterations and not limited as per the sn\_flow\_designer.max\_iterations property

  

### Issue

On the flow executions, there is a 'Do Until' action which has iteration for more than 200 times and not considering the property 'sn\_flow\_designer.max\_iterations' the value which was set to 50.

### Release

Madrid Patch 9

### Cause

When the flow designer properties are changed, the flows do not have a new snapshot and it will consider the old property values and continue to execute.

### Resolution

It is recommended to deactivate and activate the flow because the flows will have the latest snapshot and consider the latest property changes.
