---
title: "Determining if a workflow condition has been met"
aliases:
  - KB0538385
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538385
kb_number: KB0538385
last_modified: 2024-09-20
---

## Determining if a workflow condition has been met

  

### Issue

Determining if a workflow condition has been met

# Symptoms

* * *

Symptoms may include the following:

-   Workflow did not run when expected
-   Workflow did not run on a specific record
-   Cannot publish workflow
-   Publishing workflow takes too long
-   Cannot modify checked out workflow
-   Cannot start workflow
-   Workflow does not trigger
-   Stalled workflow 

# How to determine why the workflow did not run when expected

* * *

For the reproducible issue:

Sometimes when a user inserts a glide record, it results in unexpected behavior, such as the workflow does or does not start. This issue is related to the condition property of a workflow version. When a specific workflow does not run on a glide record, it is most likely that the condition property is specified on a workflow version is not met. Use the following steps to troubleshoot this.

1.  Navigate to **Workflow > Workflow Version**.
2.  Search for name of a workflow that has issues to run.
3.  Look for only the published version or the checked out version. If you have checked out the workflow, you need to focus on the checked out version. Otherwise, focus on the published version.
4.  Click the selected version from the list.  
    The workflow version form opens up.
5.  Look for the **Condition** field on the form.  
    If the **Condition** field is not visible on the form, right-click the header and select **Personalize >Form Layout**. Add the **Condition** field to the right slush bucket and click **Save**.
6.  Verify that the glide record against the workflow that did not run matches the condition specified in the workflow version.

# How to determine why a workflow runs when it is not expected to run on a specific record

* * *

For the reproducible issue:

1.  Navigate to **Workflow > Workflow Version**.
2.  Search for the name of the workflow that is running unexpectedly.  
    Remember to focus on the published version or checked out versions only.
3.  On the workflow version of the form, check the **Condition** field.  
    If the condition is not visible on the form, right click the header and select **Personalize > Form Layout**. Add the **Condition** field to the right slush bucket and click **Save**.
4.  Verify that the glide record against the workflow that is running matches the condition specified in workflow version.
5.  If you do not want to run this workflow on a glide record, insert the matched condition, and mark this workflow as inactive.
6.  On the Workflow version form, right-click the header and select **Personalize > Form Layout**.
7.  Add the **Active** field to the right slush bucket and click **Save**.
8.  On the Workflow version form, clear the **Active** option, right-click the header, and click **Save**.

For the nonreproducible issue:

If the above issue is not reproducible, but happened for a specific record and you would like to find a root cause, follow these steps.

1.  Navigate to **Workflow > All Contexts**.
2.  On this list, find the context record in which the workflow ran unexpectedly.
3.  On a selected record, click on the workflow version entry.  
    This opens up the workflow version record.
4.  On the workflow version record, verify that the condition matches the glide record. This may not be the published version.  
    In the published version, the condition might have been changed, so the issue is not reproducible anymore.
