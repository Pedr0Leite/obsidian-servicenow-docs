---
title: "Transfer order flows are not getting triggered post zurich upgrade"
aliases:
  - KB2554475
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2554475
kb_number: KB2554475
last_modified: 2025-10-08
---

## Transfer order flows are not getting triggered post zurich upgrade

  

### Issue

The transfer order and transfer order line workflows are deprecated from the workflows and migrated to flow designers in Zurich version, post which the flows are not getting triggered on creation of transfer order

### Release

Zurich

### Cause

These flows will be triggered by "Transfer Order Flow Trigger" and "Transfer Order Line Flow Trigger" Business Rules, where it will check if the below listed properties are enabled or not. In this particular case, these properties were set to "false".

**com.sn\_itam.enable\_flow\_designer.transfer\_order**  
**com.sn\_itam.enable\_flow\_designer.transfer\_order\_line**

### Resolution

We need to navigate to system properties and set the above mentioned properties to "true".
