---
title: "Resolve inactive flows for requested items"
aliases:
  - KB0829282
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0829282
kb_number: KB0829282
last_modified: 2025-08-19
---

## Resolve inactive flows for requested items

  

### Issue

Understand what causes a requested item (RITM) flow to not start after the request is approved, and how to resolve it. 

When a RITM stage changes to request\_approved, the flow fails to start and generates the following error in system logs, which show a FlowObjectAPIException indicating the flow has not been published : 

com.glide.plan.runners.FlowObjectAPIException: The flow named: <flow\_display\_name\_here> has not been published within application scope: global
Caused by error in sys\_script\_include.8f3a2778c0a8002700fbde5ad148abe3.script at line 54
com.glide.plan.runners.PlanRecordRetriever.getPlanRecord(PlanRecordRetriever.java:49)
com.glide.plan.runners.FlowObjectInstanceFactory.createFlowObjectInstance(FlowObjectInstanceFactory.java:23)
com.glide.plan.runners.scriptable.ScriptableFlow.jsStaticFunction\_startAsync(ScriptableFlow.java:40)
sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
java.lang.reflect.Method.invoke(Method.java:498)
...

### Release

Any supported release

### Cause

This issue occurs when:

-   The flow is deactivated in Flow Designer.
-   The active flag on the sys\_flow\_catalog\_trigger table is set to false.
-   The service catalog business rule tries to launch the catalog item flow when the RITM stage changes to request\_approved.

### Resolution

To resolve this issue:

1.  1.  Go to Flow Designer.
    2.  Open the inactive flow.
    3.  Select the Activate button to publish the flow.
