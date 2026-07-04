---
title: "How to match a Workflow Timer scheduler worker job to a Workflow Context, to find the running script"
aliases:
  - KB0551708
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0551708
kb_number: KB0551708
last_modified: 2024-09-20
---

## How to match a Workflow Timer scheduler worker job to a Workflow Context, to find the running script

  

### Issue

# Description

* * *

This article details ways to trace a long-running WFTimer scheduler job back to the workflow context and the current activity that it is running. These steps should be used if the Timer activity correctly started the workflow after the timer expired, but the workflow has continued running the subsequent activities, and one of these is running longer than expected.

# Procedure

* * *

## "WFTimer.." and "SLA breach timer" scheduler worker jobs

If a Workflow includes a Timer or SLA percentage timer activity, then at the point in the workflow that it runs, these steps occur:

1.  The workflow engine creates a Scheduled Job record in table \[sys\_trigger\], and sets the **Next action** time to the end time of the workflow Timer.
2.  The executing workflow pauses, and the current transaction ends.
3.  When the Schedule Job run time comes around, a Scheduler Worker thread starts running the workflow again, and continues to the next activity/activities in the workflow. 
4.  When the workflow has finished running the subsequent activities and performing any updates as a result of them, the job ends, and the Scheduler Worker thread is freed up.

When the activity is a **Timer**, then the scheduler job's name starts with **WFTimer...** . When the activity is a **SLA Percentage Timer**, then the name starts with **SLA breach timer...** instead, but the procedure is identical except you can ignore all contexts except the ones running for the task\_sla table.

## Locating scheduler jobs

### Scheduled Jobs - /sys\_trigger\_list.do

All scheduler jobs that are currently running will be listed in sys\_trigger with state=running. To locate:

1.  Add the **Updated** column to the list, so you know when it really did start running, which will be a short time after the planned **Next Run** time.  
      
    _/sys\_trigger\_list.do?sysparm\_query=nameSTARTSWITHWFTimer%5EORnameSTARTSWITHSLA%20breach%20timer%5Estate%3D1_

![](/sys_attachment.do?sys_id=cbaaa8a6db42b450e515c223059619e5)

### Stats - /stats.do

The Scheduler Worker section of the Stats page gives the following information:

-   **Current job:** name
-   **Job Started:** timestamp

![](/sys_attachment.do?sys_id=dfaae8a6db42b450e515c22305961906)

At this point it is worth clicking the blue link through to the thread dump, which may provide clues as to which script include or business rules are currently running. e.g. The workflow context may be inserting a task and a custom business rule on insert of task is what is actually stuck.

## Locating Workflow Context

The sys\_id mentioned in the name is not useful because this was the sys\_id of the wf\_executing record for the Timer activity when it was the currently executing activity at the time. When the job starts, this gets deleted and replaced with a record for the new **currently running activity** instead.

To locate:

1.  Use the **Start** timestamp of the job, which matches the **End** timestamp of the Timer activity in the Workflow Activity History table \[wf\_history\].
2.  Filter the list on only activities that have finished and where the workflow activity is using the **Timer** activity definition.  
      
    _/wf\_history\_list.do?sysparm\_query=activity.activity\_definition%3D3961a1da0a0a0b5c00ecd84822f70d85%5EORactivity.activity\_definition%3D8e291a23ac1464262f4366bb3182d840%5Estate%3Dfinished_

 ![](/sys_attachment.do?sys_id=97aae8a6db42b450e515c2230596191f)

3.  Open the link in the Context column to go to the Workflow Context that is currently being run in the Scheduler Worker thread.  
      
    

## Finding the long-running activity in the Workflow Context

The Workflow Context form has a related list for Workflow Executing Activities. In this example, it is an activity called **Stupid Script**.

![](/sys_attachment.do?sys_id=6faae8a6db42b450e515c22305961946)

To locate:

1.  Click the **Show Workflow** related link to view activities highlighted in green.
2.  Hover over the icon next to the activity title to a popup of scripts that are part of this activity. This is how you can find your problem.

![](/sys_attachment.do?sys_id=2faae8a6db42b450e515c22305961957)

If the workflow context has finished, then you need to consider what records the workflow would be inserting or updating, and what code might still be running as part of that transaction. You can link to a thread dump from the stats.do page for the scheduler worker thread, that may provided clues.

## How to fix long-running workflow contexts

It may be correct that your workflow is running for a long time. For example:

-   Looping through a large table and making update
-   Performing a complex Orchestration workflow activity
-   Waiting for a response from a REST message integration

You may let these run their course. Consider a redesign of your scripts if this is regularly causing performance issues on the instance. If there is a design issue in the script, then you are going to need to re-publish the workflow after fixing it.

Other solutions include:

-   It is also sometimes possible to update the scripts in activities for older unpublished workflow versions so the existing records do not run into the same problem later in their existing workflow contexts. 
-   If the workflow contexts needs stopping, clicking the **Cancel** link on the workflow context form may work in most cases.
-   If the scheduler job is still running after canceling the workflow context, then the transaction needs manually killing. This can usually be done through the **All Active Transactions** module. The URL column shows the name of the job. Select the row, and **Kill**. If this method cannot kill the job, then a node restart may be required. 

# Applicable Versions

* * *

Any
