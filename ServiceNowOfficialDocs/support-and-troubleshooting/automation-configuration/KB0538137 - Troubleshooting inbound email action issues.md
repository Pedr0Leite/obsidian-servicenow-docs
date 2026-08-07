---
title: "Troubleshooting inbound email action issues"
aliases:
  - KB0538137
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538137
kb_number: KB0538137
last_modified: 2026-03-13
---

## Troubleshooting inbound email action issues

  

### Issue

This article guides you through the process of troubleshooting inbound email action issues. It provides steps to help you eliminate common causes of your problem by verifying that the configuration of your networking is correct. 

### Symptoms

Symptoms may include the following:

-   Record not updated
-   Record not created
-   Mail not processed
-   Wrong inbound action triggered
-   Inbound email did not create the expected incident ticket
-   Inbound email creates duplicate tickets
-   Problems with inbound email action
-   Email not checking for a watermark
-   The wrong record is not updated
-   Inbound email assigns caller to the wrong person
-   Wrong content assigned to record
-   Forward inbound action not working as expected
-   Forwarded mail unexpectedly creates a new incident

### Release

### Resolution

Determine whether any of the troubleshooting steps below are true for your environment. Each step provides a link to an article that will help you eliminate possible causes and take corrective action as necessary.

1.  Review our overview on inbound email troubleshooting or confirm that email is working. For more information, see:
    -   [KB0524472: Inbound Email: Troubleshooting](/kb?id=kb_article_view&sysparm_article=KB0524472 "Inbound Email: Troubleshooting.").
    -   [KB0523577: Validating whether an inbound email action is performed](/kb?id=kb_article_view&sysparm_article=KB0523577 "Validating whether an inbound email action is performed").
2.  Ensure that the correct inbound conditions are set (case sensitivity). For more information, see:  
    -   [KB0535584: Ensuring that Inbound Email actions always work, regardless of case sensitivity](/kb?id=kb_article_view&sysparm_article=KB0535584 "Ensuring that Inbound Email actions always work, regardless of case sensitivity")
3.  Confirm that you are using the correct target table. For more information, see:  
    -   [KB0535511: Inbound Email Action Target Table](/kb?id=kb_article_view&sysparm_article=KB0535511 "Inbound Email Action Target Table")
4.  Verify that it is the correct inbound action type. For more information, see:  
    -   [KB0535515: Inbound Email Action Type is not Matched](/kb?id=kb_article_view&sysparm_article=KB0535515 "Inbound Email Action Type is not Matched")
5.  Confirm that an inbound email action is created. For more information, see:  
    -   [KB0535521: Confirm appropriate inbound email action is created](/kb?id=kb_article_view&sysparm_article=KB0535521 "Confirm appropriate inbound email action is created")
6.  Determine the priority of inbound email actions, or determine if the inbound action script has issues.
7.  Determine whether any of the troubleshooting steps below are true for your environment. Each step provides a link to an article that will help you eliminate possible causes and take corrective action as necessary.
8.  Confirm that email is not being ignored. For more information, see:  
    -   [KB0535493: Ensuring Email is not Ignored](/kb?id=kb_article_view&sysparm_article=KB0535493 "Ensuring Email is not Ignored")
9.  Determine if email handling properties are correctly configured. For more information, see  
    -   [KB0535434: Configure Email Handling Properties: Defining How Inbound Emails are Treated](/kb?id=kb_article_view&sysparm_article=KB0535434 "Configure Email Handling Properties: Defining How Inbound Emails are Treated").

 **Note:** If your problem still exists after trying the steps in this article, submit a case to Technical Support and note this Knowledge Base article ID (KB0538137) in the problem description. For more information, see [Customer Support](/kb?id=kb_article_view&sysparm_article=KB0547260 "Customer Support").
