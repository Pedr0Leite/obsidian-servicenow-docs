---
title: "How to access the output returned by an Orchestration Activity"
aliases:
  - KB0635207
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0635207
kb_number: KB0635207
last_modified: 2025-09-09
---

## How to access the output returned by an Orchestration Activity

  

### Issue

This article describes how to use the Orchestration Databus to access the output returned by a powershell activity. 

### How To

In this article, we'll use an example custom powershell activity that pings a host. The input IP address is passed by a service catalog item, which in turn triggers the workflow with the custom activity.

The **Outputs** section of the activity contains two output variables, as seen in the following screenshot.

![](sys_attachment.do?sys_id=bc604d811b611194ed6c9979b04bcba2) 

1.  Add the Ping Server activity and a Run Script activity into a workflow.
2.  Inside the **Run Script** activity, access the Databus variables using the method **data.get()**.
    -   The **data.get()** function receives an integer as its argument.
    -   The integer number should match the number used by the Databus to refer to the activity. In this case the number is **3**, this number can be seen to the righthand side of the activity name.  
          
        ![Accessing the Databus Variables from within a Run Script activity](sys_attachment.do?sys_id=6c604d811b611194ed6c9979b04bcb32 "Accessing the Databus Variables from within a Run Script activity")

In the screenshot above, the output is passed to a workflow.scratchpad variable which can be used in other parts of the workflow.

With the steps given above, the data returned by an orchestration activity can be used successfully in other parts of a workflow.
