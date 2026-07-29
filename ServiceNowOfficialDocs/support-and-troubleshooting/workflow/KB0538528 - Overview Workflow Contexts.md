---
title: "Overview: Workflow Contexts"
aliases:
  - KB0538528
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538528
kb_number: KB0538528
last_modified: 2024-09-20
---

## Overview: Workflow Contexts

  

### Issue

**Overview:** Workflow Contexts 

  

**Goals**

-   Running a Workflow.
-   Visualizing the Workflow Context.
-   Debugging simple workflows.

  

**Summary**  

Workflow in ServiceNow names a running workflow a Workflow Context.

The Workflow Context maintains the state of the overall process in the Workflow Context record.

The Workflow Context maintains the state of the individual activities as they execute in a series of related lists. These lists maintain the state of currently executing activities, the result of finished activities, and the execution path the workflow took through the process model.

The Workflow Context canvas provides a visual representation of the execution path the workflow took through the process model. The state of each activity (finished, executing, canceled, error) is represented using the color palette. The executed paths are represented in the color blue; the non-executed paths are represented in grey.  

### Resolution

**ServiceNow workflow context**

A Workflow Context is a workflow that is executing in the Workflow Engine.

A workflow can be started in one of four ways:

-   From within the Workflow Canvas using the Green Arrow.
-   As part of a Glide transaction.
-   As a sub-flow called from inside the main flow.
-   From within a script using the Workflow Script Include.

A record in the Workflow Context maintains the state of the overall process. The Related Lists maintains the state of the Activities throughout the life cycle of the running workflow.

Once started, a Workflow Context will “run to wait.” That is, the Workflow Engine examines all the Activities currently executing. If an Activity is finished, the Workflow Engine evaluates an Activity’s conditions. For all true conditions, the engine looks to the end of the transition arrow for what to do next. If an activity is not finished, it is assumed to be waiting for an outside Event (Approval, Task Complete, Probe Complete, etc.). 

![](sys_attachment.do?sys_id=36e724811b047414f34d33bc1d4bcb5a)  

**NOTE:** If there are any Workflow Editor tabs open at this time, close them now.

1.  **Workflow > Workflow Editor**.
2.  In the Workflow Editor, **Gear Menu > New.  
      
    ![](sys_attachment.do?sys_id=3ee724811b047414f34d33bc1d4bcbe5)** 
3.  **Fill out the form as shown:  
      
    **Name: **K14 Context Demo**Table: **Global \[global\]** 
4.  Click **Submit.  
      
    ![](sys_attachment.do?sys_id=36e724811b047414f34d33bc1d4bcbeb)**The Workflow Version has a model that at this time contains **Begin** and **End** Activities. This is a complete workflow and enough to create a context. In the header of the Workflow Canvas find the green arrow icon. This is the play button. When a workflow designer selects the play button the Workflow Version in the editor will execute. 
5.  Select the Green play button.  
      
    ![](sys_attachment.do?sys_id=bee724811b047414f34d33bc1d4bcb58)  
      
    ![](sys_attachment.do?sys_id=bae724811b047414f34d33bc1d4bcbec)  
     
6.  Click **Submit** to execute the K14 Context Demo workflow.  
      
    ![](sys_attachment.do?sys_id=32e724811b047414f34d33bc1d4bcbee)  
      
    
    This is the **Context View**. When a workflow has run or is running, the state of the workflow can be visualized in the Context View.
    
    The Workflow Editor uses colors to communicate different states of a workflow and its Activities. In the upper right-hand corner of the Context View, find the blue question mark icon.
    
7.  Hover over the blue question mark icon.  
      
    ![](sys_attachment.do?sys_id=b6e724811b047414f34d33bc1d4bcbef)  
      
    Each color in the key indicates the state of an Activity executing in the workflow. In the key, blue indicates Finished. Looking at the activities on the Context Canvas, we can see that both Activities, Begin and End, are finished.  
      
    ![](sys_attachment.do?sys_id=3ee724811b047414f34d33bc1d4bcbf0)  
      
    The coloring of activities in the Workflow Context reflects the state of each individual Activity. The header of the Workflow Context canvas reflects the state of the overall workflow.  
      
    ![](sys_attachment.do?sys_id=7ae724811b047414f34d33bc1d4bcbfe)  
      
    The Canvas View of the Workflow Context is a convenient summary view. There is also a way to see the details of the Workflow Context.  
      
     
8.  **Workflow > All Contexts.  
      
    ![](sys_attachment.do?sys_id=bae724811b047414f34d33bc1d4bcb5b)  
      
    **The list shows all Workflow Contexts that have finished or are currently executing. 
9.  Select K14 Context Demo Workflow Context from the list.  
      
    **NOTE:** Switch to the tab view for easier navigation.  
      
    ![](sys_attachment.do?sys_id=72e724811b047414f34d33bc1d4bcbb4)  
      
    To correlate the execution of the Workflow Context to the artifacts of the Workflow Context sees the diagrams. 

  

**Establish the workflow context**

  

![](sys_attachment.do?sys_id=f6e724811b047414f34d33bc1d4bcbb5) 

Looking at the values in the Workflow Context form, we can see that even without doing any work, a Workflow Context has significant status to report.

![](sys_attachment.do?sys_id=7ee724811b047414f34d33bc1d4bcbb6)

-   The Workflow Version that ran this Workflow Context.
-   The Result (if any) of the Workflow.
-   The ID of the document that associated with the Workflow Context.

When a Workflow runs from the green play button of the Workflow Context the ID will always be **Workflow Execution: << the name of the version running >>.** When a Workflow is run against a Glide Record, this ID is the document id. For example, a Routine Change workflow will run against a Change Request Workflow. The ID of that Workflow Context will be **Change Request: CHG0030002.**

  
**Run transitions**

  

![](sys_attachment.do?sys_id=f2e724811b047414f34d33bc1d4bcbb8) 

  
**State of the context**

The final state of a Workflow is one of the following values:

-   Finished
-   Canceled
-   Executing 

1.  Scroll to the bottom of the Workflow Context form.
2.  Select the **Workflow Executing Activities** Related List.  
      
    ![](sys_attachment.do?sys_id=7ae724811b047414f34d33bc1d4bcbb9)  
      
    Because the workflow is already finished, there are no entries into this system.  
     
3.  Select the **Workflow Activity History** Related List.  
      
    ![](sys_attachment.do?sys_id=fee724811b047414f34d33bc1d4bcbba)  
      
    The Workflow Activity History reflects the start, state, and end time of all the activities executed in this Workflow Context.  
     
4.  To the left of the list select the **Personalize List** icon.  
      
    ![](sys_attachment.do?sys_id=76e724811b047414f34d33bc1d4bcbbc)  
     
5.  Select the **Activity index** property in Available and move it to Selected using the Add arrow.
6.  Click **OK**.  
      
    Your Activity History list should look like this:  
      
    ![](sys_attachment.do?sys_id=fae724811b047414f34d33bc1d4bcbbd)  
      
    The Activity index is a number assigned to an activity when it is created. This value is the only reliable method of knowing the exact execution order of the Activities. The timestamps assigned to the Activities are precise to a second. Several activities can execute within a second, making Started ordering an inconsistent means of determining the precise order of execution.  
      
    On the diagram, activities will appear to be executing concurrently based on how they are drawn and how the context colorizes their state. However, the order of appearance of transitions at the same transition level on the diagram does not necessarily reflect the order of execution. The **Activity index** will definitely provide the precise order of execution. In debugging large workflows or workflows that have multiple transitions from a single condition, this value is enormously helpful.  
     
7.  Click the **Workflow Transition History** tab.  
      
    ![](sys_attachment.do?sys_id=72e724811b047414f34d33bc1d4bcbbf)  
      
    The Workflow that we ran had one very simple transition in it, Begin -> End. All transitions that execute are written to this list.  
     
8.  Select the **Workflow Log** list.  
      
    Your Workflow Log list should look like this:  
      
    ![](sys_attachment.do?sys_id=b2e724811b047414f34d33bc1d4bcbe7)  
      
    In a subsequent lab we will address the details of workflow logging. For now, take note of where the Workflow Log list is, and what entries are written to the Log by default.  
     
9.  Select the Workflow Queued Commands list.  
      
    Your Workflow Queued Commands list should look like this:  
      
    ![](sys_attachment.do?sys_id=3ae724811b047414f34d33bc1d4bcbe8)  
      
    The entries in the Workflow Queued Commands list are transient, and should not be there by the time a workflow is finished.  

  

**Outside events**

Recall that part of the stimulus in the process of Running Transitions in a workflow is receiving outside events. 

![](sys_attachment.do?sys_id=bee724811b047414f34d33bc1d4bcbe9) 

If an **Outside Event** comes into the Workflow Engine while the Engine is currently running active transitions in its ‘run to rest’ process, the **Outside Event** will be temporarily cached in the Workflow Queued Commands table. When the ‘run to rest’ process completes its active transitions, it will retrieve incoming events from the **Workflow Queued Commands** list. The commands are deleted as they are read from the table.
