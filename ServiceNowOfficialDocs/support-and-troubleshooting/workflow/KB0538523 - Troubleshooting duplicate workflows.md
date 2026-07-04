---
title: "Troubleshooting duplicate workflows"
aliases:
  - KB0538523
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538523
kb_number: KB0538523
last_modified: 2024-09-20
---

## Troubleshooting duplicate workflows

  

### Issue

Troubleshooting duplicate workflows

  
Description  

* * *

This article guides you through the process of troubleshooting duplicate workflows. It provides steps to help you eliminate common causes for your problem by verifying that the configuration of your networking is correct.

Symptoms

* * *

Symptoms may include the following:  
  

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

  
   
Resolution

* * *

Determine if any of the troubleshooting steps below are true for your environment. Each step provides a link to an article that can help you eliminate possible causes and take corrective action as necessary. 

1.  Determine if the workflow is actually a duplicate. For more information, see [KB0538217: Moving workflows within update sets](/kb_view.do?sysparm_article=KB0538217 "KB0538217: Moving workflows within update sets").
2.  Determine if there is an out of sync workflow after an update set. For more information, see [KB0538500: Determining if there is an out-of-sync workflow after an update set](/kb_view.do?sysparm_article=KB0538500&ni.dependent.topic=kb_knowledge.category&sysparm_category=&sysparm_ck=4155117b87a02100491683bdff434d5fb10bf2c9f16b5f7724847b4c741ce44e50470ee1&sysparm_nameofstack=&sysparm_product=&sysparm_search=out-of-sync&sysparm_topic= "KB0538500: Determining if there is an out-of-sync workflow after an update set"). 

<table class="noteTable" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Note" src="/Note_25x.pngx" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Note</strong>: If your problem still exists after trying the steps in this article: Submit an incident to Technical Support and note this Knowledge Base article ID (KB0538523) in the problem description.</td></tr></tbody></table>
