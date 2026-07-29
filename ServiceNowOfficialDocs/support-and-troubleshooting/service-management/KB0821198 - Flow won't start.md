---
title: "Flow won't start"
aliases:
  - KB0821198
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0821198
kb_number: KB0821198
last_modified: 2025-09-30
---

## Flow won't start

  

### Issue

Submitting the catalog item creates a Request and RITM, but doesn't start the flow for the RITM.

### Cause

The default stage on the sc\_req\_item is 'waiting\_for\_approval.'

When the request is approved (in 'Service Catalog Request' workflow), the 'Cascade Request Approval to Request Item' out-of-the-box (OOTB) business rule on the sc\_request table updates the stage on the sc\_req\_item to 'request\_approved.'

When the stage on the sc\_req\_item record changes to 'request\_approved,' the 'Start FlowDesigner Flow' OOTB business rule on the sc\_req\_item table triggers the associated flow.

The root cause of the issue is the 'Cascade Request Approval to Request Item' OOTB business rule on the sc\_request table is deactivated.

### Resolution

Activate the 'Cascade Request Approval to Request Item' OOTB business rule on the sc\_request table.
