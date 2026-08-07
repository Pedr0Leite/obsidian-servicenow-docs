---
title: "Determine if there was an exception that prevents workflow from starting or resuming"
aliases:
  - KB0538284
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538284
kb_number: KB0538284
last_modified: 2024-09-20
---

## Determine if there was an exception that prevents workflow from starting or resuming

  

### Issue

Determine if there was an exception that prevents workflow from starting or resuming  

Symptoms  

* * *

Symptoms may include the following:  

-   Workflow did not run when expected
-   Workflow did not run on a specific record
-   Workflow not attaching
-   Workflow not progressing to the next activity
-   Cannot publish workflow
-   Publishing workflow takes too long
-   Cannot start workflow
-   Workflow does not trigger
-   Stalled workflow   

Cause

* * *

In most cases, the problem is due to an exception during the transaction following the workflow activity. Updating the record that the workflow is attached to starts or resumes the workflow. 

How to locate the exception in the logs

* * *

Look in the logs on both nodes and determine the node on which the transaction happened. Go to the **Log File Download** and locate the date on which the tranaction happened and download the logs from that day on both nodes.  
  
![](/Screen%20shot%202014-04-29%20at%203.31.57%20PM%20.pngx)

1.  Locate the exact time at which the transaction occured and check to see if there were any transactions that caused any exceptions.
2.  In most cases, **Null Pointer Exception** is the cause of a cancelled transaction, which will prevent the update of the business rule that triggers the workflow to continue.
3.  Once the exception is located, continue to investigate the cause of the exception and how to prevent the exception. This can be done by tracing the stack trace of the exception and locating where this happened.
