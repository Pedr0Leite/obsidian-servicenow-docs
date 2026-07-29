---
title: "Determining if there are competing business rules that cause the workflow to stop"
aliases:
  - KB0538069
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538069
kb_number: KB0538069
last_modified: 2024-09-20
---

## Determining if there are competing business rules that cause the workflow to stop

  

### Issue

Determining if there are competing business rules that cause the workflow to stop

  
  

# Symptoms

* * *

-   Approvals are stuck
-   Hung workflow
-   Cannot start workflow
-   Workflow doesn't start
-   Workflow won't trigger
-   Workflow is not progressing
-   Workflow hung on activity
-   Workflow not returning
-   Subflow won't return
-   Subflow running too long
-   Subflow stuck

# Video

* * *

# Workflow and business rules

* * *

The workflow engine is part of the glide script engine. The workflow engine is typically invoked along with the business rules of the current record (for example, a change request). However, workflows can also be invoked via a script from within business rules as part of a post-processing action. 

# An example of post-processing business rule

* * *

In the base instance, an example of a post-processing business rule is **SNC - Run parent workflows (Approval)**. This is an **After** business rule on the sysapproval\_approver table.

Based on the conditions, **SNC - Run parent workflows (Approval)** runs:

-   after the **Insert/Update** of the sysapproval\_approver record (it is a post processing rule)
-   if the state of the workflow changes to **Approved** or **Rejected**, or if the approval is deleted
-   if it performs a glide query to find related records and uses the interface defined in the **Script Include Workflow** to invoke the workflow of the related records

To determine the business rules that fire on a specific table: 

1.  In the Application Text Filter, type **Business Rules**.
2.  Select **System Definition > Business Rules**.
3.  In the Filter select **Go to** > **table**.
4.  In the Filter, type the name of the table. For example, **sysapproval\_approver**.  
    A list of business rules that fire off the specified table is displayed.

How to troubleshoot by examining the conditions: 

1.  In the Application Text Filter, type **Business Rules**.
2.  Select **System Definition > Business Rules**.
3.  In the Filter, select **Go to** > **table**.
4.  In the Filter, type the name of the table. For example, **sysapproval\_approver**.  
    A list of business rules that fire off the specified table is displayed.
