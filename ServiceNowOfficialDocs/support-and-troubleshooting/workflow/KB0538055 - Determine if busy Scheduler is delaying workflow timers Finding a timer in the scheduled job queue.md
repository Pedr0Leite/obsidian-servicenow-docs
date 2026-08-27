---
title: "Determine if busy Scheduler is delaying workflow timers | Finding a timer in the scheduled job queue"
aliases:
  - KB0538055
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538055
kb_number: KB0538055
last_modified: 2025-03-05
---

## Determine if busy Scheduler is delaying workflow timers | Finding a timer in the scheduled job queue

  

### Issue

### Symptoms

-   Timer did not execute or failed
-   Timer stuck
-   Slow timers
-   Hung workflow
-   Workflow is not progressing
-   Stuck workflow with asynchronous wftimer <sysID>

### Workflow timer

When a workflow timer is executed, it creates a scheduled job according to the parameters set in the timer workflow activity. The scheduled job is a simple script that fires a timer event into the workflow. The created job is identified as WFTimer + the sys\_id of the executing activity.

### Release

All

### Resolution

# Finding the executing activity for a timer

* * *

1.  Navigate to **Workflow > Live Workflows > Active Contexts**.  
    A list of running workflows appears.
2.  Find the workflow context containing the timer being investigated.
3.  Open the context.
4.  Select the **Workflow Executing Activities** related list.
5.  Select the timer being investigated.
6.  Right-click the header bar and select **Copy sys\_id**.  
    A number similar to this appears: 9d9d0633d733110043ea6f14ce61038d. This is the sys\_id of the executing record. It is the record of the **Scheduled Job** containing the **Timer** that the callback script will fire the _timer_ event into. Follow any instructions to copy sys\_id.
7.  Navigate to **System Scheduler > Scheduled Jobs > Scheduled Jobs**.
8.  In the Search field type: **WFTimer** + the **sys\_id** you copied.  
    Your search item should look something like this: WFTimer9d9d0633d733110043ea6f14ce61038d.
9.  Click the **Search** icon**.  
    **If the timer is still in the scheduled job queue, the timer has not been fired. If the workflow appears to be stuck and waiting for this timer, the workflow is still in the queue. The workflow picks up once the timer is picked up by the scheduler. 

# How to determine if scheduler is backed up

* * *

1.  Navigate to **System Diagonostics**.
2.  On the page, find **System Overview**.
3.  If the scheduler backed up, **Events Pending** displays in red.

# What to do if scheduler is backed up

* * *

If a scheduler is backed up, it is important to identify the scheduled jobs that are running and see if they are operating as expected.

1.  In the Application Navigator, type **sys\_trigger.list**.   
    A list of jobs displays.
2.  Filter out all jobs in the **Ready** state**.**

The remaining jobs are currently running and occupying the scheduler. Examine the running jobs. If one or more jobs are not operating as expected and are blocking the timer unnecessarily, cancel the offending transactions using the following steps:

1.  Navigate to **User** **Adminstration** > **All Active Transactions.**
2.  Identify the offending transaction.
3.  Select the checkbox next to the transaction.
4.  In the choice list actions, click **Selected Rows**.
5.  Then click **Kill**.   
    A series of messages explains that the transaction may not be terminated immediatey.   
    After the offending jobs are cancelled, the scheduler picks up the next set of queued jobs, which should include any due or overdue WFTimer jobs that have been queued as **Ready**.
