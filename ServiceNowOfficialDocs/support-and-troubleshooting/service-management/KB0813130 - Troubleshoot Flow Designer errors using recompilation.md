---
title: "Troubleshoot Flow Designer errors using recompilation"
aliases:
  - KB0813130
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813130
kb_number: KB0813130
last_modified: 2025-08-26
---

## Troubleshoot Flow Designer errors using recompilation

  

### Issue

When running flows that contain subflows or flow actions, Flow Designer may fail and display the following localhost log error. 

Flow Designer: Operation(\_FLOW\_ACTION\_NAME\_HERE\_.If$1.caabc882db02c010a19d121d13961933.If$2.evalConditions) failed with error: com.snc.process\_flow.exception.OpException: unable to evaluate condition for /if/\_0\_06abc882db02c010a19d121d1396193a = {{0657a5bf-e279-41ab-9842-863b2f52114f.Record.u\_field\_name.name}}=Maintenance is not a valid conditional expression

### Release

All supported releases

### Resolution

You can resolve many flow issues, including the If flow action error in the preceding example, by recompiling the flow, flow action, or subflow. 

To recompile the flow:

1.  Deactivate the flow.
2.  Reactivate the flow.
3.  Republish the flow.

If the error persists: 

1.  Identify where the error occurs (which flow action or subflow).
2.  Either:
    -   Delete and rebuild the affected flow action
    -   Delete and re-add the troublesome subflow
