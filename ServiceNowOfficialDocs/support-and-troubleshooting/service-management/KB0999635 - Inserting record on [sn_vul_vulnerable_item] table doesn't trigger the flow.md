---
title: "Inserting record on [sn_vul_vulnerable_item] table doesn't trigger the flow"
aliases:
  - KB0999635
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0999635
kb_number: KB0999635
last_modified: 2024-10-16
---

## Inserting record on \[sn\_vul\_vulnerable\_item\] table doesn't trigger the flow

  

### Issue

The flow trigger condition is set to Created or Updated of the record on \[sn\_vul\_vulnerable\_item\] table. Updating a record triggers the flow. Inserting a record doesn't seem to trigger the flow.

### Release

Paris

### Cause

The issue is documented as a product defect PRB1540542

### Resolution

Workaround:

After commenting on line number 56 of the script includes VulnerableGroupRule flow is getting triggered on the insert of the record.  
  
Whenever the item is added to the group we are updating VI with setworkflow( false) which is causing the flow to not trigger.
