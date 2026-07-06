---
title: "Slowness because of high memory contention when the job 'Flow Engine Event Handler' is running"
aliases:
  - KB0817583
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0817583
kb_number: KB0817583
last_modified: 2026-05-01
---

## Slowness because of high memory contention when the job 'Flow Engine Event Handler' is running

  

### Issue

#### **Slowness because of high memory contention when the job 'Flow Engine Event Handler' is running**

### Cause

#### **You can experience slowness on the app node where the job `Flow Engine Event Handler` is running because of high memory contention, due to flow(s) looping tens of thousands or hundreds of thousands of times in "for each" flow logic.**  

### Resolution

The workaround is to refactor the flow to take the steps inside the for each loop and move them into a separate subflow. Then either:  
1) (pre-Orlando) Create an action with a script step that used scriptable flow api to call the subflow (sn\_fd.FlowApi.executeSubflow(...)).  Call this action inside your loop.  
2) (Orlando and newer) Use dynamic subflow to call the subflow.  Call this subflow inside your loop.

  
Either option will cause the subflow execution to occur in a separate context, dividing up the steps and reducing the maximum memory used at any one time. You will know it is working by looking at sys\_flow\_context table and seeing that a context is created for the parent flow and then subsequent contexts are created for the subflow on each iteration.

You may also see some benefit to changing the property `com.snc.process_flow.reporting.level` to value to OFF which was previously suggested.

### Related Links

#### **1****) Documentation will give you more insight on the property `com.snc.process_flow.reporting.level`: Link: `[https://docs.servicenow.com/csh?topicname=flow-execution-details.html&version=latest](https://docs.servicenow.com/csh?topicname=flow-execution-details.html&version=latest)`**

Please see this PRB as well. Most of these high memory issues can be related to this PRB1407971.
