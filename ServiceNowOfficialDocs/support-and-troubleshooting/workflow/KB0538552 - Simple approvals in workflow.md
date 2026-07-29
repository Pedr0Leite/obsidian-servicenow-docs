---
title: "Simple approvals in workflow "
aliases:
  - KB0538552
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538552
kb_number: KB0538552
last_modified: 2024-09-20
---

## Simple approvals in workflow

  

### Issue

**Simple approvals in workflow**  

  

**Goals**

-   Creating approvals with workflow
-   Single approvers

  

**ServiceNow approval workflow**  

ServiceNow Workflow provides three activities to assign and manage approvals: **Approval - User**, **Approval – Group**, and **Approval Coordinator**.

The approvals created in workflows interface with the ServiceNow Platform Approval Engine.

The Workflow Engine creates the approvals and then waits for an **Approval** or **Rejection** to transition forward.

The interaction between the approval records created by workflow and the tasks being approved or rejected is not part of the workflow. They are a part of the Approval Engine. Workflow only creates approvals and reacts to the approved state.

 

### Resolution

**Creating the Knowledge simple approval workflow**  

  

1. In the Application Navigator filter text, type **workflow** to find the **Workflow** application menu.

2. Select the **Workflow Editor** module. The Workflow Editor always opens in an adjacent browser tab.

3. Click the **New** button.

![](sys_attachment.do?sys_id=ed87288d1bc07414f34d33bc1d4bcbb0)

4. Fill out the form as shown

    Name: **Knowledge Simple Approval**

    Table: **Global \[global\]**

5. Click the **Submit** button.

![](sys_attachment.do?sys_id=2d87688d1bc07414f34d33bc1d4bcb73)

6. In the Activity Tree, expand the **Approvals** category folder.

    The open Approvals folder should look like this:

![](sys_attachment.do?sys_id=a187688d1bc07414f34d33bc1d4bcb75)

These are the global Approval-related Activities available in the Workflow Engine.

-   Approval – User

o   Creates a single **User Approval** record in the database.

-   Approval Action

o   Updates the current record associated with the workflow with an **Approved** or **Rejected** value in the **Approval** field of the Glide record, if the field exists.

-   Rollback To

o   Provides a way to restart portions of a Workflow. If there are Approvals in the restarted portion of the Workflow, the Approval states will be rolled back to **Not Yet** **Requested** or **Requested** depending on the configuration of the **Rollback To** path.

7. Find the **Approval – User** Activity in the **Approvals** folder.

8. Hold the mouse down and drag the Activity onto the canvas. Hover the activity over the Transition Line until the line turns blue.

9.  Let go of the mouse.

NOTE: In subsequent labs, these steps will be abbreviated to **Drag Activity onto the transition**.

  

![](sys_attachment.do?sys_id=2987688d1bc07414f34d33bc1d4bcb76)

10. Fill out the form as shown:

      Name: **Approval One**

11. Select the **Users** Lock icon.

![](sys_attachment.do?sys_id=ad87688d1bc07414f34d33bc1d4bcb77)

  

12. Select the **Search** looking glass icon.

13. Select **K14-Approver One** as the approver.

NOTE: In subsequent labs, these steps will be abbreviated to **User** **Search icon > User Name.** 

![](sys_attachment.do?sys_id=2587688d1bc07414f34d33bc1d4bcb79)

14. Click the **Submit** button.

Your workflow should look like this:

  

![](sys_attachment.do?sys_id=6d87688d1bc07414f34d33bc1d4bcbb8)

  
**Add the log message activities**  

1. In the Activity Tree, expand the **Utilities** folder and locate the **Log Message** Activity.

2. Drag Log Message onto the transition between the **Approved** condition and the **End** Activity.

3. Fill out the form as shown:

    Name: **Approved**

    Message: **Approval One was approved**.

4. Click the **Submit** button.

Your workflow should look like this:

![](sys_attachment.do?sys_id=e187688d1bc07414f34d33bc1d4bcbba)

NOTE: You may have to click and drag the Activities on the canvas to spread them out.

5. Find the **Log Message** Activity in the **Utilities** Category Folder in the Activities Tree on the right.

6. Single-click the **Log Message** Activity onto the Canvas.

7. Fill out the form as shown

    Name: **Rejected**.

    Message: **Approval One was rejected**.

8. Click the **Submit** button.

  

NOTE: The Log Message Activity is placed on top of the existing Log Message Activity. Move it off and onto another area of the Workflow Canvas.

 ![](sys_attachment.do?sys_id=6987688d1bc07414f34d33bc1d4bcbbb)

9. Select the **Rejected** node on the **Approval – User** Activity and draw a transition to the **Log Message** Activity.

10. Select the **Always** node on the Rejected **Log Message** Activity and draw a transition to the **End** Activity. Review your work in the next screen capture.

11. Select the green **Play** button.

![](sys_attachment.do?sys_id=6587288d1bc07414f34d33bc1d4bcbb2)

  

  

12. Select **Submit.**

Your workflow should look like this:

![](sys_attachment.do?sys_id=2587688d1bc07414f34d33bc1d4bcb6e)  

  

The green state of the **Approval One** Activity indicates that the workflow is waiting for the approver to act on the approval.

13. Return to the main ServiceNow tab.

14.  **Self-Service > My Approvals**.

15.  Clear the breadcrumb to display **ALL** approvals.

16.  In the list view, find **the K14-Approver One** record and right-click the **State** field. Change the State to **Approved**.

![](sys_attachment.do?sys_id=a987688d1bc07414f34d33bc1d4bcb6f)

  

  

NOTE: In subsequent labs, these steps will be abbreviated to **approve the record from the list State field.**

     17. Return to the Workflow Editor in the right tab. 

     18. Use the Refresh icon ![](/refresh.pngx)to refresh the Workflow Editor. It is located in the banner next to the Help icon.

![](sys_attachment.do?sys_id=2187688d1bc07414f34d33bc1d4bcb71)

  

  

1  9. Click the **Refresh** icon in the Workflow Context view.

Y.  our workflow should look like this:

![](sys_attachment.do?sys_id=a587688d1bc07414f34d33bc1d4bcb72)  

20\. Close the Workflow Context diagram by selecting the X in the upper right-hand corner.
