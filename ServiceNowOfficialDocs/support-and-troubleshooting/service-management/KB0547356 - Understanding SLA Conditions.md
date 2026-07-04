---
title: "Understanding SLA Conditions"
aliases:
  - KB0547356
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547356
kb_number: KB0547356
last_modified: 2026-01-07
---

## Understanding SLA Conditions

  

### Issue

[SLA Definitions](https://docs.servicenow.com/csh?topicname=c_SLADefinitions.html&version=latest "SLA Definitions") contain conditions that control:

-   When an SLA record is created for a particular task
-   When an SLA record is updated as it moves through its lifecycle to completion

This article expands on some of the details for SLA conditions set when [defining an SLA](https://docs.servicenow.com/csh?topicname=t_CreateAnSLADefinition.html&version=latest "defining an SLA").

### Release

All

### Resolution

Defining Start, Stop and Pause Conditions 

* * *

These are all conditions you can specify for an SLA definition.

![](sys_attachment.do?sys_id=70fecbe5471a3298c2488d01426d43a7)

-   **Start condition**: think of this as a "Run" condition, in that it is applied all the time, not just when the SLA starts. The relevant condition must always match for the SLA to continue running; if it does not get matched, the SLA is then cancelled.
-   **Stop condition**: think of this as a "Complete" condition, allowing you to say that the SLA is now completed. For example, if the state of the underlying record is **solved**, then this can be a stop condition, meaning that the SLA is complete when this condition is matched.
-   **Pause condition**: when the pause condition is met, the SLA is paused and will stay dormant in the background, ready to restart when the start condition is matched again. For example, you may have a pause condition to reflect when you are waiting for information from a third-party before you can proceed. 

Please see the [product documentation](https://docs.servicenow.com/csh?topicname=t_CreateAnSLADefinition.html&version=latest "product documentation") for more descriptions of SLA definition fields.

Order of evaluating conditions

* * *

 SLA conditions are evaluated in the following order:

1.  Stop 
2.  Pause
3.  Start

Consider this evaluation order when you create conditions, as otherwise this may cause confusion.

For example, if your Start condition is a subset of your Stop condition, the Start condition will never be matched, as the Stop condition is always evaluated first. So that SLA will never start. 

Similarly, if your Pause condition is a subset of your Start condition, the SLA will attach, but will be permanently in a Paused state. And as soon as the Pause condition does not match, the equivalent Start condition will also not match, so that SLA will be cancelled.

And you create a SLA definition with a Start condition and a Pause condition which are mutually exclusive, your SLA will never pause; it will always be canceled first. For example, an SLA definition where the Start condition is **State is one of "New, Active"** and the Pause condition is **State is "Awaiting User Info"**.

Using the Reset Condition 

* * *

The Reset condition is not shown on the form by default, but is a more advanced condition, allowing you to define the state in which the SLA returns to the beginning.

To use the Reset condition, configure the form layout, and add it to the form (configure and add)

![](sys_attachment.do?sys_id=78fecbe5471a3298c2488d01426d436a)

<table class="noteTable" style="border: 1px solid #e0e0e0;" align="left"><tbody><tr><td style="vertical-align: middle; text-align: center;"><span style="font-size: 12pt;"><img title="Note" src="/Note_25x.pngx" alt="" align="baseline" border="" hspace="" vspace=""></span></td><td style="vertical-align: middle; text-align: left;"><span style="font-size: 12pt;"><strong>Note</strong>: T<span style="text-align: start;">he Reset condition is not sufficient to reset an SLA. Both the&nbsp;Reset and Start conditions&nbsp;must&nbsp;be matched&nbsp;for the SLA to be reset to zero. It may be helpful to remember this, if you create duplicate&nbsp;Reset conditions to match the existing Start conditions, so that all Reset conditions are shown in the same place</span>.</span></td></tr></tbody></table>

### Related Links

-   [Troubleshooting service level agreements (SLAs)](/kb_view.do?sysparm_article=KB0523638 "Troubleshooting service level agreements (SLAs)")
-   [Understanding SLA times: actual elapsed time and business elapsed time](/kb_view.do?sysparm_article=KB0547270 "KB0547270: Understanding SLA times: actual elapsed time and business elapsed time")
-   [SLA Condition Evaluation](/kb_view.do?sysparm_article=KB0547389 "KB0547389, SLA Condition Evaluation")
