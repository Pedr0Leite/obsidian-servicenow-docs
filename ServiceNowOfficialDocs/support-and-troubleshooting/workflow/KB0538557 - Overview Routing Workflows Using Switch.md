---
title: "Overview: Routing Workflows Using Switch"
aliases:
  - KB0538557
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538557
kb_number: KB0538557
last_modified: 2024-09-20
---

## Overview: Routing Workflows Using Switch

  

### Issue

Overview: Routing Workflows Using Switch  

Goal

* * *

Understand the Activities available for making decisions in a Workflow based on the values of the Current Record.  

Routing workflows

* * *

One of the most powerful aspects of the Workflow Engine is its ability to interact with the platform. For the most part, this interaction is through the manipulation of the Current Record.

The Workflow Editor provides Activities that will read specified fields on the Current Record and route the workflow along specific transition paths based on the values of those fields.

In the Conditions Category folder, the **Switch** and **If** Activities that assist the designer with routing. In the Utilities Category folder, the **Branch** can be used.  

1.  Return to the Workflow Editor.
2.  Click **Open**.
3.  Select **K14 – Choices in Workflow – Switch Demo**.  
      
    ![](/sys_attachment.do?sys_id=a3a92462db42b450e515c223059619aa)  
      
    
4.  Select the **Gear Menu > Check Out**.
5.  Select the **Gear Menu > Properties**.  
      
    ![](/sys_attachment.do?sys_id=afa92462db42b450e515c223059619b4)  
      
    Notice that this workflow is on the Same K14 301 table used in earlier labs. In this demo, condition that runs the workflow is **Name** starts with **Switch Demo.**  
      
    
6.  Close the **Properties** form.
7.  Double click on the If **Budget Review** Activity.  
      
    ![](/sys_attachment.do?sys_id=7ba92462db42b450e515c223059619c9)  
      
    The **If** Activity contains a simple condition builder. The condition choices are based on the fields that are available in the table associated with the workflow. In this case **K14 301 Demo**. Take a minute to look back at the form and look at the choices for Review type.  
      
    
8.  Close the **Activity** form.
9.  Double-click on the If **Budget Review** Activity.
10.  Return to the main ServiceNow tab.
11.  In the Application Navigator Text filter type, **K14**.
12.  Select a record from the K14 301 list.
13.  Select **Review Type** control.  
       
     ![](/sys_attachment.do?sys_id=7ba92462db42b450e515c223059619e2)  
       
     Notice that the Review type has 3 options, Budget Review, Facilities Review and a default of None.  
       
     
14.  Return to the Workflow Editor.
15.  Close the Activity.
16.  In the **Activities Tree**, expand the Conditions Category to locate the **Switch** Activity.  
       
     ![](/sys_attachment.do?sys_id=7fa92462db42b450e515c223059619f7)  
       
     
17.  Drag the **Switch** Activity onto the Canvas.  
       
     ![](/sys_attachment.do?sys_id=bfa96462db42b450e515c22305961901)  
       
     
18.  Fill out the form as follows:  
       
     Name: **Switch on Review Type**  
     Type: **Field**  
     Field: **Review Type**  
       
     
19.  Click **Submit**.  
       
     ![](/sys_attachment.do?sys_id=fba96462db42b450e515c2230596190a)  
       
     Notice that the auto-generated conditions are the same values as the items in the choice list on the K14 301 forms.  Using the Switch instead of the If in this situation allows us to route the workflow differently on a **None** selection.  
       
     
20.  Delete the If by clicking the X on the Activity.
21.  Route the **Begin** to the **Switch.**
22.  Route the **Budget Review** Condition to the **Budget Ok?** Approval.
23.  Route the **Facilities Plan** Condition to the **Plan OK?** Approval.
24.  In the **Utilities** folder in the right panel, find the **Log Message**.
25.  Drag the **Log Message** onto the canvas.
26.  Fill out the form as follows:  
       
     Name: **Error**  
     Message: **No Review Type Selected**  
       
     
27.  Click **Submit**.
28.  Route the **None** Condition of the Switch to the **Error** Log Message.
29.  Route the **Error** Log Message to **End**.  
       
     Your workflow should look like this:  
       
     ![](/sys_attachment.do?sys_id=8cb96462db42b450e515c2230596192e)  
       
     
30.  Return to the main ServiceNow tab.
31.  Select **New** on the K14 301 list header.
32.  Fill out the form as follows:  
       
     Name: **Switch Demo**  
     Review Type: **Budget Review**  
       
     
33.  Click **Submit**.
34.  Select **K14 Approvals.**
35.  **Right click > Approve** the Requested Approval.
36.  Select **K14 Live Workflows**.
37.  Select the Context that matches the Number of the last K14 301 record.
38.  Select **Show workflow** from the Related Lists.  
       
     ![](/sys_attachment.do?sys_id=0cb96462db42b450e515c22305961949)  
       
     Notice that the Workflow was routed through transitions of the Workflow according the selection in the Review Type selection.  
       
     
39.  Repeat steps 31 - 38 for the **None** selection. Fill out the form as follows:  
       
     Name: **Switch Demo**  
     Review Type: **None**  
       
     
40.  Repeat steps 31 to 38 for the **Facilities** **Plan** selection. Fill out the form as follows:  
       
     Name: **Switch Demo**  
     Review Type: **Facilities Plan**  
       
     
41.  Validate the routing matches the selection.

Summary

* * *

The Workflow Editor offers several ways to route a workflow through transitions based on the data in the Current Record.

The **If** Activity can be configured to evaluate values of fields in the Current Record using a Condition builder.

The **Switch** Activity auto-generates conditions based on the values of a choice list in the Current Record.
