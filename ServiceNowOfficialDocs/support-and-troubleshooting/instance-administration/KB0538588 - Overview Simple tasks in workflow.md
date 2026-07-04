---
title: "Overview: Simple tasks in workflow "
aliases:
  - KB0538588
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538588
kb_number: KB0538588
last_modified: 2025-04-14
---

## Overview: Simple tasks in workflow

  

### Issue

The **Create Task** activity allows the designer to decide if the workflow should wait for the task to complete before transitioning to the next Activity. If the designer selects Wait for Complete, the Workflow inserts the task into the database and waits for an update from that record. When the user changes the state of the task, the Workflow Engine is notified of the update event and the Activity will finish and transition to the next Activity.

Completed tasks have a _State_ change when they are in a rollback path.

-   The state of tasks in a rollback path will set to _Pending_.
-   Tasks that are the destination of a Rollback To Activity will be set to _Open_.

### Resolution

### Goals

-   Assign tasks to Change Requests
-   Rolling back tasks.

### Tasks in ServiceNow workflow

The _ServiceNow Workflow Editor_ provides three activities to assign and manage tasks using the _Create Task_ activity. The tasks created from within a workflow typically appear inside a related list of the current record. The workflow engine creates the tasks and then waits for a _Complete_ or _Incomplete_ state to transition forward. The interaction between the state change of tasks and the workflow engine is through the update of the current record. The update event will invoke the glide script engine and fire the update event into the workflow.

1.  In the Workflow Editor click **Open**.
2.  Locate and select the K14 Change Task Example workflow.  
    Your workflow should look like this:  
      
    ![](sys_attachment.do?sys_id=699443f1dbf36c504819fb24399619c6)  
      
    
3.  Select **Gear Menu > Check Out**
4.  Select **Gear Menu > Properties  
      
    **![](sys_attachment.do?sys_id=319443f1dbf36c504819fb2439961902)  
      
    Notice that this workflow is on the **Change Request** table. Because our other workflow is also on **Change Request** a different condition is set. This workflow is configured to run only when the **Priority** field is set to **3 – Moderate**. As we test this time, we will actually have to change the **Priority** on the Change Request. Close the **Workflow Properties** window using the X in the upper right-hand corner of the form.
5.  Expand the **Tasks** category in the activities tree.
6.  Drag the **Create Task** activity onto the transition between **Log Approval One** and **Approval Two – Create Task Example**.  
      
    ![](sys_attachment.do?sys_id=319403f1dbf36c504819fb24399619ae)  
      
    ![](sys_attachment.do?sys_id=bd9483f1dbf36c504819fb2439961906)  
      
    Fill out the form as shown:
    -   **Name**: Create a Change Task
    -   **Task Type**: Change Task \[change\_task\]
    -   **Assigned to**: K14Task one user
    -   **Short Description**: Task assigned to K14 User One
    -   **Instructions**: Enjoy your conference!  
        Notice the **Wait for Completion** checkbox. When checked, this will cause the workflow to wait for the task to be in a state of **Complete** or **Incomplete** before transitioning to the next activity.
7.  Click **Submit**  
    Your screen should look like this:  
      
    ![](sys_attachment.do?sys_id=ce9443f1dbf36c504819fb24399619d4)  
    **QUESTION**: Find the _Create Task_ in the rollback path. What will be the state of the _Create Task_ in the _Workflow Context Activity History_ related list if the _Approval Two_ activity is rejected?  
    Tasks have rolled back states, just like the Approvals did in the previous lab. If a Task is in the path of a rollback, its **State** is set to **Pending**. If a task is the target of a **Rollback To** transition, the task state is set to **Open**.  
      
    
8.  Return to the main tab of your instance.
9.  Go to **Change > Create New**
10.  Set the Priority: **3 –Moderate**
11.  **Right-click** in the form header and select **Save**.
12.  Scroll to the related lists
13.  Select the **Approver** tab
14.  **Right-click > K14-Approver One**, set the Requested approval to Approve.
15.  Select the Change Tasks Related List.  
       
     ![](sys_attachment.do?sys_id=0e9403f1dbf36c504819fb2439961941)  
     Notice how the new task has been added to the Change Request.
16.  **Right-Click > Close Task**
17.  Select the **Approvers** related list  
       
     ![](sys_attachment.do?sys_id=de9443f1dbf36c504819fb2439961913)
18.  **QUESTION**: We are going to reject the _Requested_ approval. What will be the new state of K14-Approval One? Approval Two?
19.  **Right-Click > Reject** the K14-Approver Two Requested approval.
20.  Select the **Change Tasks** related list  
       
     ![](sys_attachment.do?sys_id=9a9483f1dbf36c504819fb2439961937)  
     Note the rolled back state of the Change Task is set to Pending
21.  Select **Show Workflow** from the related links to view the workflow
22.  Close the browser tab of the Workflow Context view
23.  Select the **Approvers** related list
24.  **Right-Click > Approve** the K14-Approver One Requested Approval
25.  Select the **Change Tasks** related list
26.  **Right-Click > Close Task**
27.  Select the **Approvers** related list
28.  **Right-Click > Approve** the K14-Approver Two Requested Approval
29.  Select the **Show Workflow** related link  
       
     ![](sys_attachment.do?sys_id=34558bb9dbf36c504819fb243996190c)  
     The workflow context is displayed.
