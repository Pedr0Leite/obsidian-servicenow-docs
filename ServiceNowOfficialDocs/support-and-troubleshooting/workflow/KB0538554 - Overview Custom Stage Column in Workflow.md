---
title: "Overview: Custom Stage Column in Workflow"
aliases:
  - KB0538554
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538554
kb_number: KB0538554
last_modified: 2024-09-20
---

## Overview: Custom Stage Column in Workflow

  

### Issue

Overview: Custom Stage Column in Workflow  

Goals

* * *

-   Learn how to add a custom stage column to a table.
-   Learn how to have a workflow write stages to that column.

Adding a custom stage column

* * *

When designing applications, using the Stage column is an excellent way to reflect process progress to a user while abstracting away from the complexity of the Workflow.

The Element type of **Workflow**, when associated with a **Workflow Version** will receive the stage state as the workflow executes.

For this lab, a custom application named **K14** has been added to your instance.  

1.  Return to the main ServiceNow tab.
2.  In the Application Navigator Text filter type, **K14.**  
      
    ![](/sys_attachment.do?sys_id=c48a6c66db42b450e515c22305961908)  
      
    
3.  Select the **K14 301s** link. 
4.  Select the **New** button.
5.  In the header of the form, right-click and **Personalize > Form Layout.  
      
    ![](/sys_attachment.do?sys_id=408a6c66db42b450e515c22305961910)  
      
    **
6.  Find the **Create new field** section on the form.  
      
    ![](/sys_attachment.do?sys_id=8c8a6c66db42b450e515c22305961918)  
      
    
7.  Fill out the **Create new field** section as follows:  
      
    Name: **Stage**  
    Type: **Workflow**  
      
    
8.  Click the **Add** button.
9.  Use the Up Arrow to move the new **Stage** field just under **State**.
10.  Click the **Save** button.  
       
     ![](/sys_attachment.do?sys_id=dc8a6c66db42b450e515c22305961922)  
       
     
11.  Right-click on the **Stage** label.
12.  Select **Personalize Dictionary.  
       
     ![](/sys_attachment.do?sys_id=188a6c66db42b450e515c2230596192a)  
       
     **NOTE: When adding a Stage column to a table in an application that is specific to rendering the Stage progression icons, it is best practice to make that field Read only. In this way, conflicts between the workflow process and what the user sees are not possible. The Workflow Engine _writes_ to the Stage field, it does not _read_ or _react_ to it.
13.  Check ****Read only**.**
14.  Click ****Update**.**Now that there is a Workflow field that can accept Stages from a workflow, configure a workflow to write to that field.

    
Associate stage column to stages

* * *

1.  Return to the Workflow Editor tab.
2.  Click **Open**.
3.  Select **K14 – 301 Custom Stage Demo****.**
4.  Select **Gear Menu > Check out**.
5.  Select **Gear Menu > Properties**.  
      
    ![](/sys_attachment.do?sys_id=188a6c66db42b450e515c22305961943)  
      
    
    Notice:
    
    -   This workflow is written against the K14\_301 table just modified.
    -   The workflow runs only when the **Name** starts with **Custom Stage.**
    
    -   The **Stage** field is the field that tells the Workflow Engine to write the current Stage value to the current record. It is possible to have Stages in a workflow and not have them communicate to the current record. They can be on the workflow just for clarity when viewing the Workflow on the Canvas. However, if the designer intends to reflect the progress of the workflow in **Stage** icons, this field must be selected.
6.  Select the **Stage** column from the choice list.
7.  The stage section of your screen should look like this:  
      
    ![](/sys_attachment.do?sys_id=588a6c66db42b450e515c2230596194d)  
      
    
8.  Notice the two additional Stage Fields. These are fields that will determine how the Workflow Engine follows the stages through the workflow execution and how it reports them.

Stage rendering

* * *

The Workflow Engine determines how to render the stages in the icon list based on one of these selections.

**Legacy**: This is the least desired selection. The legacy rendering will continue to support all the icon script includes and Business Rules that are already deployed in previous versions of the product. This is specifically for backwards compatibility.

**Linear**: The Workflow Engine will render all the icons in the Workflow Stage list, in the order that is assigned to the individual Stages. With the Linear renderer, the Workflow Engine will maintain the Stage state even if the Stages are changing in subflows. With this selection, the designer has the most control over how the Stages will appear in the list. Every Stage will appear, regardless of whether or not the stage was executed in the Workflow.

**Main flow**: The Workflow Engine will render only the icons that represent Stages executed in the Main flow. If there are Stages in subflows they will not reflect in this icon list. If there are stages on execution paths not executed in a workflow, they will not show in the stage icon list.

**Progress Bar**: The Workflow Engine will not render icons as all. It will render a single progress bar that shows the overall progress of the Workflow.

**Workflow**\-**Driven**: This is the default selection. With this selection the Workflow Engine will initially render icons that represent Stages that are on the ‘happy path’ of execution. That is the Stages on **Approved**, **Yes**, **Always**, and **Complete** condition paths. However, if during execution an “unhappy path” begins (for example an Approval Rejection), the Workflow Engine will re-calculate and redraw the icon tree. In the adjusted rendering, the “happy path” no longer displays and the Workflow Engine attempts to predict the next likely path the workflow could transition towards.    

Stage order

* * *

The Workflow Engine will determine the order in which stages will appear in the icon list based on one of these selections.

**Computed**: Icons by default are ordered in the order of execution of a workflow and based on the expected or surmised future path found in all transitions. This default ordering is called the **Computed** order and is defined in the workflow properties under the field Stage order.

**User Specified**: The workflow designer may determine the exact order of icon rendering in a list, regardless of execution order by selecting **User Specified** in the Stage order: field of workflow properties and appropriately adding an order value to the defined Workflow Stages.  

For this lab, we will choose Linear, since we have the most control over what we see.

1.  Select Stage Rendering: **Linear**. 
2.  Stage Order: **User Specified.**
3.  Click **Update**.
4.  Select **Gear Menu > Edit Stages.**
5.  Select **Import from Stage Set**.  
      
    ![](/sys_attachment.do?sys_id=908a6c66db42b450e515c22305961955)  
      
    
6.  Select **K14-301 Custom Stage Column**.  
      
    ![](/sys_attachment.do?sys_id=d88a6c66db42b450e515c2230596195c)  
      
    
7.  Close the Workflow Stages list.
8.  To the **Custom Stage Log Starting** Log Message Activity, assign the **Starting** stage.
9.  To the **Waiting** Timer Activity, assign the **Working** stage.
10.  To **Log Ending** Log Message Activity, assign the **Ending** stage.
11.  Return to the main ServiceNow tab.
12.  In the Application Navigator Text filter type, **K14**.
13.  Select the **K14 301s** link.
14.  Click **New**.
15.  Fill out the form as follows:  
       
     Name: **Custom Stage**  
       
     
16.  Click **Submit.**
17.  Personalize the List Layout and add the **Stage** column after the Name field.  
       
     ![](/sys_attachment.do?sys_id=ac8a6c66db42b450e515c22305961964)  
       
     If it does not look like that right away, refresh you list. It could just be your timer has not come back and completed the stage yet.  
       
     
18.  Return to the Workflow Editor.
19.  **Gear Menu > Edit Stages**.
20.  In the **Working** Stage, change the value in the Order column to **600**.
21.  Close the Stage List.
22.  Return to the **K14** application. You can see the difference in progression in the workflow by submitting additional records.
23.  Click **New**.
24.  Fill out the form as follows:  
       
     Name: **Custom Stage**  
       
     
25.  Click **Submit.  
       
     ![](/sys_attachment.do?sys_id=e88a6c66db42b450e515c2230596196d)**Notice that the order of the icons has changed according to the user ordering specified in the Workflow Stage List. Ordering is one way the designer has to convey the status of a workflow. It is also possible to change the rendering format completely.
26.  Return to the Workflow Editor.
27.  **Gear Menu > Publish.**
28.  ****Gear Menu > Check out.****
29.  ******Gear Menu > Properties.******
30.  In the Stage Rendering field select SimpleProgressBar.
31.  Click **Update**.
32.  Return to the **K14** application. You can see the difference in progression in the workflow by submitting additional records.
33.  Click **New**.
34.  Fill out the form as follows:  
       
     Name: **Custom Stage**  
       
     
35.  Click **Submit.**Your list should look like this:**  
       
     ![](/sys_attachment.do?sys_id=688a6c66db42b450e515c22305961983)  
       
     **The icons and the progress bar are the currently available base instance rendering options for displaying the progress of a workflow.

Summary

* * *

Workflow Stage icons are a powerful way to reflect the progress of a workflow to users.

The Workflow Engine can be configured to reflect icons in a variety of ways:

-   In the order the process designer specifies
-   In the order the Workflow Engine discovers stages as it executes
-   Stages only in the main flow with multiple subflows
-   As a progress bar that reflects overall progress.

The order and rendering of Stage icons is configured in the Workflow Properties form.

The Workflow Engine will publish icons if:

-   A table has a field of Workflow Type.
-   A Workflow is written against that table.
-   The Stage column has been identified in the Workflow Properties.
-   Stages have been assigned to activities in a Workflow.
