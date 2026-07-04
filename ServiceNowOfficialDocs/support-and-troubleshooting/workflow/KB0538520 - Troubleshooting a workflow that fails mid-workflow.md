---
title: "Troubleshooting a workflow that fails mid-workflow"
aliases:
  - KB0538520
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538520
kb_number: KB0538520
last_modified: 2025-07-31
---

## Troubleshooting a workflow that fails mid-workflow

  

### Issue

This article guides you through the process of troubleshooting a workflow that fails mid-workflow. It provides steps to help you eliminate common causes by verifying that the configuration of your networking is correct.

### Symptoms

-   Workflow is not progressing
-   Workflow not progressing in domain-separated environment
-   Workflow hung on activity
-   Workflow does not generate a task
-   Workflow not found
-   Workflow not returning
-   Workflow does not generate approval
-   The generate activity does not create tasks or approvals
-   Duplicate workflows
-   Duplicate approvals
-   Subflow does not return
-   Subflow running too long
-   Subflow stuck
-   Timer did not execute
-   Timer failed
-   Stuck worker with timer stuck
-   Stuck work with async wftimer <sysID>
-   Workflow notification not triggered
-   Event does not trigger
-   Unable to open workflow

### Release

All

### Resolution

Determine whether any of the troubleshooting steps below are true for your environment. Each step provides a link to an article that can help you eliminate possible causes and take corrective action as necessary. 

1.  [KB0538055: Determine if busy Scheduler is delaying workflow timers](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538055 "KB0538055: Determine if busy Scheduler is delaying workflow timers").  
2.  [KB0538242: Determining if an approval was manipulated outside of the workflow](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538242 "KB0538242: Determining if an approval was manipulated outside of the workflow"). 
3.  [KB0538502: Determining if there are inconsistent domain issues (approver in the wrong domain)](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538502 "KB0538502: Determining if there are inconsistent domain issues (approver in the wrong domain)").
4.  [KB0538284: Determine if there was an exception that prevents workflow from starting or resuming](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538284 "KB0538284: Determine if there was an exception that prevents workflow from starting or resuming").
5.  [KB0538069: Determining if there are competing business rules that cause the workflow to stop](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538069 "KB0538069: Determining if there are competing business rules that cause the workflow to stop"). 
6.  [KB0538279: Determining a table cleaner issue](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538279 "KB0538279: Determining a table cleaner issue"). 

<table class="noteTable" align="left"><tbody><tr><td style="vertical-align: middle; text-align: center;"><img title="Note" src="/Note_25x.pngx" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Note</strong>: If the problem still exists after trying the steps in this article, submit an incident to SN Technical Support and note this Knowledge Base article ID (KB0538520) in the problem description. For more information, see <a title="Customer Support" href="https://support.servicenow.com/kb_view.do?sysparm_article=KB0547260" target="_blank" rel="noopener noreferrer">Customer Support</a>.</td></tr></tbody></table>
