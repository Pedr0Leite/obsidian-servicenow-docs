---
title: "Workflow Engine: Slowness in Workflow Activity Execution"
aliases:
  - KB0662288
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0662288
kb_number: KB0662288
last_modified: 2024-09-20
---

## Workflow Engine: Slowness in Workflow Activity Execution

  

### Issue

Workflow Engine: Slowness in Workflow Activity Execution

Problem

* * *

Users have reported slowness in workflow activity execution. The issue is not reproducible on demand and it is not limited to a specific workflow activity.  

Symptoms

* * *

The symptoms below are examples, but are not limited as this behaviour can impact any workflow activity:  

-   Workflow Timers taking longer to execute than expected, even though the scheduler is clear
-   Sub Workflows are completed but Sub Flow activity not continuing to next activity
-   Begin activities not transitioning to next activity

Cause

* * *

The cause for this issue would be due to custom business rules on the following Workflow Tables. For example, the business rules may exist on (but are not limited to) the following workflow tables:

-   Workflow Context \[wf\_context\]
-   Workflow Executing \[wf\_executing\]
-   Workflow Activity \[wf\_activity\]
-   Workflow Transition \[wf\_transition\]
-   Workflow Version \[wf\_workflow\_version\]

  
Resolution

* * *

Since the tables above have base-system business rules, records and java script execution that are used as part of the Workflow Engine, ServiceNow would recommend to de-activate any custom business rules on the Workflow tables.

<table class="noteTable" style="width: 739px;" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Warning" src="/Warning_25x.pngx" align="baseline" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Warning</strong>: Please ensure that any of the steps taken in the resolution is executed on a non-production instance that is a copy of production for testing purposes, before any modification is made on production instances.</td></tr></tbody></table>
