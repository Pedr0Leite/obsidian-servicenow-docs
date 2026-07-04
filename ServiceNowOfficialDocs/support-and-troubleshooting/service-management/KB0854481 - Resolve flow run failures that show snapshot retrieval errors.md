---
title: "Resolve flow run failures that show snapshot retrieval errors"
aliases:
  - KB0854481
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0854481
kb_number: KB0854481
last_modified: 2025-08-26
---

## Resolve flow run failures that show snapshot retrieval errors

  

### Issue

When running a flow, either by Test or by triggering it, it fails to run. Checking the Node logs shows an error: Could not retrieve snapshot for test

### Release

All supported releases

### Cause

Flow Designer ran into difficulties executing the flow. To determine the exact cause, use the Node logs. 

### Resolution

In Flow Designer:

1.   Go to Flow Properties and set the log level field to Debug. 
2.   Run the Flow test again to reproduce the error.
3.   Look for the error message "Could not retrieve snapshot for test" 

In the Node logs:   

1.  Find the starting point of the log section, which begins with: DEBUG: Flow Designer: Compiling flow \[flow name\].
2.  Remove unrelated entries, including references to business rules, activity on different threads, or different users.
3.  To identify the failure point, review the remaining log entries (approximately 30 lines) while referencing your flow in Flow Designer. 

For example, consider this log stack:

DEBUG: Flow Designer: Compiling flow TestFlow | Change

DEBUG: Flow Designer: Step Get Catalog Variables Step Created with an input count of 3 and an output count of 0  
DEBUG: Flow Designer: Step Get Catalog Variables Step Created with an input count of 3 and an output count of 5  
DEBUG: Flow Designer: Action created with an input count of 3 an output count of 5

DEBUG: Flow Designer: Step Lookup Record step Created with an input count of 5 and an output count of 2  
DEBUG: Flow Designer: Step Lookup Record step Created with an input count of 5 and an output count of 2  
DEBUG: Flow Designer: Action created with an input count of 5 an output count of 2

DEBUG: Flow Designer: Step Create Task step Created with an input count of 4 and an output count of 2  
DEBUG: Flow Designer: Action created with an input count of 3 an output count of 2

DEBUG: Input param1 assigned with a reference count of 1  
DEBUG: Input param2 assigned with a reference count of 1

SEVERE \*\*\* ERROR \*\*\* Flow Designer: null  
SEVERE \*\*\* ERROR \*\*\* Flow Designer: Could not retrieve snapshot for test  
com.glide.flow\_trigger.engine.FlowSnapshotPlanRetriever.retrieve(FlowSnapshotPlanRetriever.java:33)  
com.snc.process\_flow.engine.serialization.PlanProxy.plan(PlanProxy.java:43)

This stack is going through the various actions of the flow and trying to compile everything. You can check that in the flow and you'd see something like:

1.  Get Catalog Variables: OK
2.  Lookup Record: OK
3.  Create Task: OK

The flow likely fails on the next step in the run. The 'null' in the error is likely a missing input value. The logs show the following inputs for the next step:

DEBUG: Input param1 assigned with a reference count of 1  
DEBUG: Input param2 assigned with a reference count of 1

The first two (param1 and param2) work but the third one fails resulting in the null error.
