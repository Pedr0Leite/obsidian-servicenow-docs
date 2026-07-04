---
title: "Overview: Other Routing Workflows"
aliases:
  - KB0538558
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538558
kb_number: KB0538558
last_modified: 2024-09-20
---

## Overview: Other Routing Workflows

  

### Issue

Overview: Other Routing Workflows  

Goal

* * *

Demonstrate options in workflow routing.  

Routing workflows with conditions

* * *

As we saw in the previous lab, a workflow can be routed using conditions of activities such as **If** and **Switch**.  Routing off conditions is the most common way to route a workflow but it is not the only way.

Workflows can have execution paths that wait for an event to fire or wait until for a state change on a specified field. The activities **Wait for Event** and **Wait for Condition** both provide a way for a workflow to wait.

Waiting for events and conditions can simplify the layout of a workflow and can provide a way to visually isolate transition paths in a workflow with complicating the main execution path of a workflow.  

1.  Return to the Workflow Editor. 
2.  Click **Open**.
3.  Select the **K14 – Choices in Workflow – Wait for Condition** workflow.
4.  **Gear Menu > Check Out**.  
      
    Your workflow should look like this:  
      
    ![](/sys_attachment.do?sys_id=7a9e30a2db0ab450e515c22305961958)  
      
    
    This is essentially the same example workflow as the Switch example but with added decision making to provide a more complete process. We will detail the Activities pointed to by the arrows.
    
    The process being defined is as follows:
    
    -   Determine the Request Type
    -   Route the work to the correct Approver.
    -   Based on the Approve | Reject status of the Approver
        -   Update the State of the record to **Final** on **Approve**
        -   Update the State of the record to **Revision** on **Reject**
    
    **Branch**
    
    The Branch activity does **not** by default evaluate the Conditions. Its primary purpose is to direct the workflow down multiple paths and provide a label for them. You can script conditions, but this example does not.
    
    -   **Execute** condition routes to the same process flows as the switch example in the prior lab.
    -   **Wait for Disposition** condition will route the workflow to two **Wait for Condition** Activities.
        -   These activities are waiting for mutually exclusive conditions, so when designing the workflow, they were routed off the same Branch condition.
    
    **Wait for Condition**
    
    The **Wait for Condition** Activity will execute and then wait for a specified field to be assigned a value. Once that value is assigned the Activity will transition. If that condition is not met in the process of executing the workflow, the Activity will never transition.
    
5.  Double-click on **Wait for Rejection** Activity.  
      
    ![](/sys_attachment.do?sys_id=7e9e30a2db0ab450e515c22305961963)  
      
    Notice the condition builder specified the field on the Current Record to listen to and the value to listen for.  
      
    
6.  Close the Activity.
7.  Double-click on **Wait for Approval** Activity and see that it is waiting for the same field but with a different value.  
    
    By listening to the same field for different values, the designer can use the **Wait for Condition** to route the workflows down two mutually exclusive paths.  This same thing could have been done with an **If** Activity. Using an If however, would require the conditional logic to be intermingled with the execution logic. Using the **Wait for Condition** allows a designer to separate the transition paths into isolated, testable execution scenarios.
    
    **End**
    
    Any transition to the **End** Activity ends the Workflow. Though this seems obvious, the most important note is that because any transition ends the workflow, the first transition to the workflow will cancel any executing activities. In the Context Diagram we see a record was created that did not specify a **Review Type.** The workflow logs a message and then routes directly to **End** notice that the two Wait for Conditions are cancelled. It was the execution of the first transition to **End** that cancelled those activities.
    
    There are however, many reasons to have concurrently transitioning paths do some work and then wait for other transition paths before continuing or before ending a workflow. The **Join** Activity provides a meeting place for different transition paths to route to.
    
    **Join**
    
    The **Join** Activity can accept any number of transitions as inputs. Each time a transition routes to a Join the activity does an evaluation of all transitions that are assigned to it. The evaluation determines if all **possible** routes to decide if it is finished waiting.  A Join can finish on a **Complete** or an **Incomplete** condition.
    
    -   **Complete** indicates that all transitions arrived to the **Join** successfully.
    -   **Incomplete** indicates that not all transitions arrived, but all **possible**transitions arrived.
        -   In the example workflow, **Approval Action** **Approved** and **Approval Action Rejected** both transition to the same **Join**. Because these are mutually exclusive transitions, the Join will always be Incomplete.  On Incomplete, the **Join** will progress to the next activity.  
              
            
8.  Return to the main ServiceNow tab.
9.  Create a new K14 301 record.
10.  Fill out the form as follows:   
       
     Name: **Wait for Condition  
     **Review Type: **Budget Review**  
       
     
11.  Click **Submit**.
12.  **K14 > K14 Approvals**.
13.  Approve the associated **Approval**.
14.  Examine the Workflow Context**.**
15.  ****K14 > K14 Live Approvals****.  
       
     ![](/sys_attachment.do?sys_id=b29e30a2db0ab450e515c2230596196d)  
       
     Notice that the Wait for condition was cancelled. This is because the **Do More Work** activity got to the **End**. The first one to **End** will always win.  
       
     
16.  Using the **Branch** Activity and the **Wait for Conditions** as your guide, take a few moments to test some other routings in the workflow and examine the difference.
