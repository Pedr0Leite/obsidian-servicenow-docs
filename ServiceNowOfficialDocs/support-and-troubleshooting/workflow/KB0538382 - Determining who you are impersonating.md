---
title: "Determining who you are impersonating"
aliases:
  - KB0538382
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538382
kb_number: KB0538382
last_modified: 2024-09-20
---

## Determining who you are impersonating

  

### Issue

Determining who you are impersonating

Symptoms

* * *

Symptoms may include the following:  

-   Unexpected behavior in workflow execution
-   Workflow editor does not reflect the right person
-   Workflow does not run on an insertion of a record
-   The **Checked out by** user cannot make changes to the checked out version
-   Cannot start workflow
-   Workflow does not start
-   Workflow does not trigger

Unexpected behavior in workflow execution

* * *

When impersonation is used in different tabs, the workflow editor may not always reflect the right person. This can cause unexpected behavior in workflow execution or in the workflow editor making changes to the checked out version. For example:

-   the workflow does not run on an insertion of a record
-   the **Checked out by** user cannot make changes on the checked out version or may not be able to publish the checked out version

How to determine why the workflow did not run when the workflow condition matches on a glide record insert

* * *

The issue could occur for a newly created workflow version that is not published yet.

To troubleshoot this issue:

1.  Log in as a workflow admin.
2.  Navigate to **Workflow > Workflow versions**.
3.  Search for name of the workflow and open a record form.
4.  Verify that it has a published version. The **Published** option should be selected.  
    If it does not have a published version and the user is trying to run a workflow that is different than the **Checked out by** user, the workflow does not run because there is no valid workflow version available for that user to run.
5.  To fix this issue, the **Checked out by** user needs to publish the checked out version so that other users can use it.

Determining why the **Checked out by** user is not able to make changes to or publish the checked out version

* * *

1.  Verify that the user does not have multiple tabs open and is impersonating different users.
2.  Verify that the user has not created a workflow in one tab and opened up another tab, impersonatng another user there. In this situation, the workflow editor does not reflect the right person during impersonation, which could cause unexpected behavior.
3.  Close the different tabs. 
4.  Open the workflow editor again with proper logged in user.  
     

Example use case:

-   User logs in as a workflow author and creates a new workflow or checks out an existing workflow. In either case, it is a **Checked out** version.
-   User opens up a new tab and impersonates another user named Joe Smith. 
-   User then goes back to the original workflow editor tab and tries to make some changes.
-   The user might notice that the workflow editor has unexpected behavior because the workflow editor does not reflect the right person.
-   Since the other tab has Joe Smith impersonated, this is not a valid user for the checked out version.
-   To fix this issue, close the workflow editor tab, then open up the workflow editor again with the proper logged in user.
-   Verify that the workflow editor reflects the right person.
-   Verify that the workflow editor has the expected behavior.
