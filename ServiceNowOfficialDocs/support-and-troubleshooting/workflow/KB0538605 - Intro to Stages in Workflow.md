---
title: "Intro to Stages in Workflow"
aliases:
  - KB0538605
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538605
kb_number: KB0538605
last_modified: 2024-09-20
---

## Intro to Stages in Workflow

  

### Issue

**Intro to Stages in Workflow**

**Summary:**

The Workflow Engine allows a designer to define stages that represent significant points in the progression of the process. Stages are assigned to Activities in a workflow. By assigning the Stages to the Activities of a Service Catalog Item, the Workflow Engine can report the status of the process. This status is reflected in the Stage Column of the RITM record using colored icons.

This stage summary provides a non-technical view of the workflow progression to the Service Catalog customers, making it a powerful element of the workflow design.

This lab demonstrated one method of defining and reflecting stages using the Linear Renderer in the Workflow Properties. There is a suite of Stage Renderers and Configurations that are available in the Workflow Engine. These will be covered in more detail in the Workflow 301 lab.

### Resolution

**Goal Tracking Catalog Items with Stages**

-   Adding Tasks
-   Adding Stages

**Stages in Workflow with Service Catalog**

The Workflow Editor provides a way to help a user track a process through the use of Stage icons. The designer may choose to assign a Stage to an Activity in the Workflow that represents a significant point in the process being automated. As the workflow progresses through the Activities and encounters a Stage, the Workflow Engine updates the value of the stage icons.

The overall state of the Stages is stored in the Workflow Context.

**NOTE**: This section on Stages is an introduction to add completion to the Service Catalog and Workflow Relationship. Stages will be covered is detail in the Workflow 301  Lab.

1. **Workflow > Workflow Editor**.  
2\. Click **Open**.  
3\. Select the **K14 WF 201 Example - RITM Stages**.

  
  

 ![](sys_attachment.do?sys_id=1b876c8d1bc07414f34d33bc1d4bcbf6)

4\. Select the **Gear Menu > Check Out**.5. Select the **Gear Menu > Properties**.

![](sys_attachment.do?sys_id=9f876c8d1bc07414f34d33bc1d4bcbf7)

5\. Notice that this workflow is also on the **sc\_req\_item** table. Notice the two-stage properties in the right column of the **Workflow Properties** form.

-   Stage Rendering: Linear  
    -   The order that the stages are drawn in the icon list will be the order that the user specifies.
-   Stage Order: User Specified  
    -   When the rendering is Linear, the Icon Stage order always follows the ordering that is specified in the Stage Definition.

6\. Close the **Properties** form.  
7\. Select the **Gear Menu > Edit Stages**.

  
  
![](sys_attachment.do?sys_id=17876c8d1bc07414f34d33bc1d4bcbf9)  

This list represents the stages that are available for assignment in this workflow. Notice the Order values. This is the order in the icons that appear in the list of Request Items.

8\. Select the **New** button.

![](sys_attachment.do?sys_id=9b876c8d1bc07414f34d33bc1d4bcbfa)

9\. Fill out the forms as follows:

Name: **K14 Finished**  
Value: **finished**  
Order**: 500**

10\. Click **Submit**.

![](sys_attachment.do?sys_id=1f876c8d1bc07414f34d33bc1d4bcbfe)

11\. Close the list.  
12\. Double-click on the **Assign the RITM to User** Activity**.**

![](sys_attachment.do?sys_id=5b87ac8d1bc07414f34d33bc1d4bcb0c)

13\. Click the **Search** icon. 

![](sys_attachment.do?sys_id=df87ac8d1bc07414f34d33bc1d4bcb0d)

14\. Select **Assignment**.  
15\. Click **Update**.

Notice the Stage now displays in the Activity.

  

![](sys_attachment.do?sys_id=5787ac8d1bc07414f34d33bc1d4bcb0f)

16\. In the Get Manager Approval Activity, assign the **Waiting Approval** stage.  
17\. In the Fulfill the RITM item Activity, assign the **Fulfillment** stage.  
18\. In the Mark RITM as Closed Activity, assign the **K14 Finished** stage.

Your screen should look like this:

![](sys_attachment.do?sys_id=db87ac8d1bc07414f34d33bc1d4bcb10)

NOTE: A Catalog Item named **K14WF 201 – Stage Catalog Example** has been pre-configured for you to run this workflow.

19\. Return to the main ServiceNow tab.  
20. **Self-Service > Service Catalog**  
21\. Select the **Knowledge 14** -**WF 201 Lab** Category  
22\. Click **Knowledge 14 -WF 201 Stage Catalog Example**.

23\. Select the **Order Now** button.

![](sys_attachment.do?sys_id=13876c8d1bc07414f34d33bc1d4bcbfc)

Notice:

-   The Icons in the Stage column are the stages that were added to each relevant Activity in the **K14 WF 201 Example - RITM Stages.**
-   The Approved at the top of the list. We didn’t have an **Approved** stage!

![](sys_attachment.do?sys_id=97876c8d1bc07414f34d33bc1d4bcbfd)

If there is a **Gateway Approval** that is part of the process, that approval state will show at the top of the icon list for Service Catalog Items.

24\. Select the **K14 WF201 – Stage Catalog Example** link on your order form.

NOTE: If the **Self Service view** is active, switch to the **Catalog** view. This will make it easier to work through this portion of the lab.

  

25\. Scroll to the Related Lists.  
26\. Select the **Approvers** Related List.  
27. **Right-Click > Approve** the **K14 Manager** Approval.  
28\. Select the **Catalog Tasks**.  
29\. Right-Click **> Close Task** on the **Open** task.  
30\. In the Request field, select the form icon. Notice that the coding of the icons represents all the Stages.
