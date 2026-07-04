---
title: "Overview: Stage Sets for Applications"
aliases:
  - KB0538555
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538555
kb_number: KB0538555
last_modified: 2024-09-20
---

## Overview: Stage Sets for Applications

  

### Issue

Overview: Stage Sets for Applications  

Goal

* * *

Learn how to share stages sets for workflows in a shared process.  

Stage sets for applications

* * *

Recall that the purpose of Stage icons is to place the user in the progression of a business process. The user does not need to be aware of where they are in a workflow execution – being in a subflow or the main workflow is not really relevant to them. 

Stage Sets elevate the notable aspects of a business process to the user and communicate using icons. As a designer involved in service automation, you will know the meaningful business process stages independent of the design of the workflow. The value of designing Stage Sets to identify the stages then apply them to all workflows involved in a process.

This lab provides a simple example of sharing a stage set across a main flow that uses a subflow within a single business process.

When designing applications it is typical to put common re-usable behavior in subflows. As was learned in Lab 1, the significant elements of a business process may be defined in a single stage set.

For this lab, a simple main flow and subflow have been added to the **K14** application. has been added to your instance.  

1.  Return to the main ServiceNow tab. 
2.  In the Application Navigator Text filter type, **Stage Sets.**
3.  Select **K14-301 Main to Subflow** **Set Stage**.
4.  Notice there are four elements in this stage set. Notice the order of the stages. In the example we will use Linear Renderer.  
      
    ![](/sys_attachment.do?sys_id=34ebe4eadb42b450e515c2230596197f)  
      
    QUESTION: What is relevance of the Order column when using the Linear Renderer?  
      
    
5.  Return to the main Workflow Editor.
6.  Select **Open**.
7.  Open **K14 – Stage Set Main Flow**.  
      
    Your workflow should look like this:  
      
    ![](/sys_attachment.do?sys_id=3cebe4eadb42b450e515c22305961988)  
      
    
8.  Select the **Gear Menu > Check Out**.
9.  Select the **Gear Menu > Properties**.  
      
    ![](/sys_attachment.do?sys_id=fcebe4eadb42b450e515c22305961990)  
      
    
    QUESTION: Looking at the properties, what is the Condition start workflow execution?
    
    QUESTION: What property needs to be updated so that the workflow will update the Stages icons?
    
    QUESTION: What does User Specified mean in relation to the Linear Stage Renderer?  
      
    
10.  In the Stage field, assign the  **Stage** column if not already assigned.
11.  Close the Workflow Properties form.
12.  Select the **Gear Menu > Edit Stages.**
13.  Select **Import from Stage Set**.
14.  Select **K14-301 Main to Subflow Set**.  
       
     Your Workflow Stages should look like this:  
       
     ![](/sys_attachment.do?sys_id=b4ebe4eadb42b450e515c2230596199a)  
       
     
15.  Close the Workflow Stages list.
16.  To the **Log from Main Flow - Request** Log Message Activity, assign the **Main Flow Start** stage.
17.  To the **Log Message After Subflow** Log Message Activity, assign the **Main Flow End** stage. Note that the Stage displays on the Activity.  
       
     Notice in the workflow there is a subflow right in the center.  We will check out that subflow next and add the same Stage Set, but assign it different Stages of the Stage Set to subflow activities.  
       
     ![](/sys_attachment.do?sys_id=f0ebe4eadb42b450e515c223059619a3)  
       
     
18.  Select the **Gear Menu > Publish.**
19.  Select ****Open**.**
20.  **Open **K14 – Stage Set Sub Flow**.**
21.  Your workflow should look like this:  
       
     ![](/sys_attachment.do?sys_id=f4ebe4eadb42b450e515c223059619b8)  
       
     
22.  Select the **Gear Menu > Check Out**.
23.  Select the **Gear Menu > Properties**.  
       
     ![](/sys_attachment.do?sys_id=89ebe4eadb42b450e515c223059619c0)  
       
     
     Notice the **If Condition Matches** property is set to **None**.
     
     QUESTION: Why do you think this Condition is set to None?
     
     When None is the selection the Workflow Engine will not run the workflow. Since this is a subflow, that is perfect. In this scenario, it will only run when called from the main workflow.
     
     QUESTION: If we want this workflow to report stages, what do we need to make sure is defined in the Workflow Properties?  
       
     
24.  Select the **Stage** column, if not set in the Stage field.
25.  Click **Update**.
26.  Import the **K14-301 Main to Subflow Set** Stage Set into the subflow.
27.  To the Log from Subflow Flow  Log Message Activity, assign the **Sub Flow Start** Stage.
28.  To the Second Message from Subflow Log Message Activity, assign the **Sub Flow End** Stage.  
       
     ![](/sys_attachment.do?sys_id=c5ebe4eadb42b450e515c223059619c9)  
       
     
29.  Select the **Gear Menu > Publish**.
30.  Return to the Main ServiceNow tab and navigate to **K14 301s**.
31.  Select the **New** button.
32.  Fill out the form as follows:  
       
     Name: **Stage Set**  
       
     
33.  Click **Submit**.  
       
     Your Stage Set icons appear in the Stage column.  Expand the Stage icons.  
       
     ![](/sys_attachment.do?sys_id=c5ebe4eadb42b450e515c223059619dd)  
       
     Notice the stages from both the main flow and the subflow are represented in a single icon list.

  
   
Summary

* * *

As a designer involved in service automation, you will know the meaningful business process stages independent of the design of the workflow. Once defined, a Stage Set can be shared across all workflows and subflows in the Application simply by importing it into workflow. 

The Linear is the most effective Renderer when designing applications because the order that the icons appear to the user will remain consistent throughout the process, even when executing over multiple workflows.
