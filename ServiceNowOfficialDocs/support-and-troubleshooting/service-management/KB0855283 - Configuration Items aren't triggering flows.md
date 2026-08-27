---
title: "Configuration Items aren't triggering flows"
aliases:
  - KB0855283
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0855283
kb_number: KB0855283
last_modified: 2024-04-08
---

## Configuration Items aren't triggering flows

  

### Issue

Flows on the cmdb\_ci table are not triggering with configuration items.

### Cause

The configuration items are not on the cmdb\_ci table. They are on extended tables from the cmdb\_ci table.

### Resolution

For configuration items, you could use a business rule to run a script using the flow api

[https://docs.servicenow.com/csh?topicname=ScriptableFlowAPI.html&version=latest#ScriptableFlow-startFlow](https://docs.servicenow.com/csh?topicname=ScriptableFlowAPI.html&version=latest#ScriptableFlow-startFlow)
