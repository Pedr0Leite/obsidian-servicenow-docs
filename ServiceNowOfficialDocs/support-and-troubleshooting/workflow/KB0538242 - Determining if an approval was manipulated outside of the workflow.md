---
title: "Determining if an approval was manipulated outside of the workflow"
aliases:
  - KB0538242
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538242
kb_number: KB0538242
last_modified: 2024-09-20
---

## Determining if an approval was manipulated outside of the workflow

  

### Issue

Determining if an approval was manipulated outside of the workflow

Symptom

* * *

-   Approvals are stuck
-   Hung workflow
-   Workflow is not progressing 

Causes of an approval being manipulated outside of the workflow

* * *

When an approval record is manipulated outside of the workflow, it can cause the workflow to become stuck because the workflow does not know about the changes. There are various ways workflow approvals are manipulated. For example:  

-   manual approval is added that workflow does not know
-   the document in which approval is assigned could be deleted or changed
-   approvers are reassigned after the workflow has progressed and generated approval records

When **Approval User** or **Approval Group** activity runs, it generates approval records. After the approver responds to an approval request, and if workflow does not continue, there is a possibility that manual approval records might have been created and the workflow does not know about them.

How to determine whether the approval record is generated outside of the workflow

* * *

1.  Log in as an admin­.
2.  Open the record for the workflow that is stuck on execution.
3.  In the **Approvers** related list, click on each approval record.
4.  On the approval record, right-click the header and select **History > List view**.
5.  Verify that the record is created by the **System Administrator** and not by any specific user.
6.  -   If a specific user other than the System Administrator created the record, then the record was manually added to the list and the workflow does not know about the record.
    -   It is possible that a user impersonates the **System Administrator** role and then creates an approval record. To verify this, go to the history record and check the time stamp when the approval record was created. If the time stamp is not close to the same time when the **Approval User** or **Approval Group** activity is started, the record is manually created. To find the time stamp for when the workflow activity started, follow these steps
    -   1.  Navigate to **All Contexts**.
        2.  Search for the context of a specific request and click on the context.
        3.  Open the context form and click **Show Workflow Link**.
        4.  Open the workflow in the workflow editor, point to the approval activity, and look for the **Started time**. 

How to determine document that approval is looking at is deleted or changed outside of the workflow

* * *

1.  Login as an admin.
2.  Type sysapproval\_approver.list in type filter text and press the **Enter**.
3.  In the displayed list filter click **All** to obtain all approval records.
4.  Search for the approval records for a specific request.
5.  Verify that the **Approving** field of the approval record is not empty or does not have incorrect data.
6.  To verify who made changes to the approver list, check the record history.

How to determine approver has been changed after the workflow is progressed

* * *

1.  Login as an admin.
2.  Navigate to **My Approvals**.
3.  In the displayed list filter, click **All**.
4.  Search for the approval record for a specific request and open it.
5.  Right-click and check the history of the approval record and verify that the user is not reassigned.
6.  In the case of dot-walked approvals, such as dot-walked managers, verify that the manager has not been changed after the approval record is created. If it is changed after the approval record is created, approvals are not reassigned.
