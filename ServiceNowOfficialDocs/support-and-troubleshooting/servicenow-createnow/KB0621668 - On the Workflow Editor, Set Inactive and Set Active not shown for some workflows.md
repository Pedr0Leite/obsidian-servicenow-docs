---
title: "On the Workflow Editor, \"Set Inactive\" and \"Set Active\" not shown for some workflows"
aliases:
  - KB0621668
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0621668
kb_number: KB0621668
last_modified: 2025-08-06
---

## On the Workflow Editor, "Set Inactive" and "Set Active" not shown for some workflows

  

### Issue

On the Workflow Editor, "Set Inactive" and "Set Active" are not shown for some workflows.

On a published workflow, when trying to change the **Active** field (true > false or false > true), the **Set Inactive** / **Set Active** UI action is sometimes not available.

### Symptoms

Follow these steps to see if the issue is occurring on your instance:

1.  Log in to your instance as a user with the _admin_ or _workflow\_admin_ role.
2.  Navigate to **Workflow > Workflow Editor**.
3.  In the Workflow Editor, select a workflow that is used often and likely has active wf\_context records using this workflow, for example, a workflow on the Change Request \[change\_request\] table.
4.  To the left of the workflow name, click the menu icon ![](sys_attachment.do?sys_id=6cd15453dbd2d550fd8d2b69139619af).  
    Note that the **Set Inactive** or **Set Active** UI action may not appear.

### Release

### Cause

In our Java code, we have hard-coded the UI actions so that the Workflow Editor menu only displays the options to change the **Active** flag if the user has the ability to delete the workflow version. If the user cannot delete the workflow version, then they cannot set the **Active** flag on the workflow in the Workflow Editor.

By default, there is an ACL rule against the wf\_workflow\_version table (on the "delete" operation) that only allows a user to delete a workflow version under these conditions.

-   The user must have a role with workflow\_publisher or workflow\_creator (or have a parent role that inherits one of these roles such as admin or workflow\_admin)
-   There must be no active Workflow Context records \[wf\_context\] that are using this current workflow version
-   This workflow version is not being used as a subflow within another active workflow

If these conditions are met, a user can "delete" a workflow version, which subsequently means they can have the **Set Inactive / Set Active** option on the Workflow Editor as well.

### Resolution

 **Warning:** Ensure that the steps are tested on a non-production instance with extensive test cases before following the procedure on a production instance. The steps below can affect if workflows are triggered for new and existing records. Perform the steps with caution.

1.  Log in to a ServiceNow instance as a user with the _admin_ or _workflow\_admin_ role.
2.  Navigate to **Workflow > Workflow Editor**.
3.  In the Workflow Editor, click a workflow on which you need to be able to change the **Active** flag.
4.  To the left of the workflow name, click the menu icon.
5.  Click **Checkout**.  
    Because a new version has been created, the **Set Inactive** option is available.
6.  Click **Set** **Inactive**.
7.  To the left of the workflow name, click the menu icon.
8.  Click **Publish**.  
    Because the check-out workflow version record has been modified to have the **Published** field as **Published** = **True**, the **Active** flag remains and the workflow remains as inactive.
9.  To set the **Active** flag to **True**, navigate to the menu icon on the Workflow Editor and click **Set Active**.  
    Note that this only allows you to be able to continue to have these **Set Active / Set Inactive** options as long as you meet the requirements as stated in the Cause section above.
