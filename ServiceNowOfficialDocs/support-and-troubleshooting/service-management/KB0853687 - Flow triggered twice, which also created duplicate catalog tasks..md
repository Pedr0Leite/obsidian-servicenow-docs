---
title: "Flow triggered twice, which also created duplicate catalog tasks."
aliases:
  - KB0853687
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0853687
kb_number: KB0853687
last_modified: 2024-04-08
---

## Flow triggered twice, which also created duplicate catalog tasks.

  

### Issue

Flow triggered twice, which also created duplicate catalog tasks.

### Release

Orlando

### Cause

The issue started even before the flow got triggered. if we check  the audit, the system updated the approval twice on the request, Because the approval is updated twice, "Start FlowDesigner Flow" business rule condition matches twice and hence two flow contexts are seen.

  

This usually happens if there there is a customized before business rule on sc\_req\_item table that is updating the request when the RITM record is inserted. 

  

### Resolution

Please create the business rule directly on request table, insert, run it "after" and give higher order to fix this issue.
