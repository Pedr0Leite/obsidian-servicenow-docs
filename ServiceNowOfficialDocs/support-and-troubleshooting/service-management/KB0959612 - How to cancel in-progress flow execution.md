---
title: "How to cancel in-progress flow execution"
aliases:
  - KB0959612
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0959612
kb_number: KB0959612
last_modified: 2026-02-17
---

## How to cancel in-progress flow execution

  

### Summary

Flows typically run to completion without needing manual intervention, reaching the flow end point automatically. However, you might accidentally create flows with logic that causes them to loop endlessly. Infinite loops can occur in any programming language. This article explains how to cancel these in-progress flow executions.

### Release

All ServiceNow releases that support flows

### Instructions

To cancel all running flow executions (where State is "In Progress") for a specific flow, follow these steps:

1\. Open **Scripts – Background**.

2\. Run the following script:

var now\_GR = new GlideRecord("sys\_flow\_context");   
now\_GR.addQuery("name", "NAME OF FLOW TO CANCEL HERE");   
now\_GR.query();   
  
while (now\_GR.next()) {   
sn\_fd.FlowAPI.cancel(now\_GR.getUniqueValue(), 'Canceling Test Flows');   
} 

3\. Replace NAME OF FLOW TO CANCEL HERE with the exact name of the flow. You can find the flow name under **Properties** \> **Name** when viewing the flow in Flow Designer.

**Important**: Test this process in a non-production instance first. This script has been used successfully to cancel thousands of flow executions on a customer instance. However, ServiceNow developers have not officially tested or verified this code, so it is not officially supported. Test this script carefully in a non-production environment before using it in production.

### Related Links

[Flow Designer](https://www.servicenow.com/docs/r/washingtondc/build-workflows/flow-designer.html)
