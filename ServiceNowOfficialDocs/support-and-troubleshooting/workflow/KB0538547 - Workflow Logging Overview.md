---
title: "Workflow Logging Overview"
aliases:
  - KB0538547
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538547
kb_number: KB0538547
last_modified: 2024-09-20
---

## Workflow Logging Overview

  

### Issue

**Workflow Logging Overview**

  

**Goals**

-   Introduction to Workflow Logging
-   Logging from the Engine
-   Logging from the Activity
-   Writing customized Log messages in Script

  

**Summary**

The Workflow Engine provides configurable logging options using the Workflow Properties.

Log messages indicate their source of the message. A Message log entry comes from either the ENGINE or from within an ACTIVITY.

Log entries can be made into the Context Workflow Log using the Log Message Activity, the Log Trace Activity, and directly through JavaScript.

As the Workflow logging gets more verbose, the list filter is a quick way to locate messages. 

### Resolution

**Logging in ServiceNow Workflow**

ServiceNow Workflow provides logging in a log exclusive to workflows. It is separate from the System log that is specific to a currently executing Workflow Context.

Logging is useful for debugging and tracing progress through a workflow.

ServiceNow Workflow is part of the Glide Script Engine and is invoked with the insert, update, delete or cancel of a Glide record. Log entries in the Workflow Log indicate whether they were entered from the Engine or from the Activity.

The level of logging present in the Workflow Context is configurable by properties. 

**Add a log message activity**

* * *

The first exercise demonstrates the default logging behavior in the workflow. 

1.  Return to the Workflow Editor by re-selecting the ServiceNow tab.
2.  Click **New** on the workflow canvas header.
3.  Fill out the form as follows.  
      
    Name **K14 Logging Demo**.   
    Table: **Global**.  
     
4.  Click the **Submit** button.  
      
    ![](sys_attachment.do?sys_id=f6f720c11b047414f34d33bc1d4bcb50)  
     
5.  Expand the **Utilities** folder of the Activities Tree.
6.  Find the **Log Message** Activity in the **Utilities** folder.
7.  Hold the mouse down and drag the Activity onto the canvas.
8.  Hover the Activity over the transition line until the line turns blue.
9.  Release the mouse. The **New Activity** form displays.
10.  Fill out the form as follows.  
       
     Name: **K14 Log Message**  
     Message: **This is a message in the Log Message Activity**.  
       
     ![](sys_attachment.do?sys_id=c7f720c11b047414f34d33bc1d4bcb5b)  
      
11.  Click the **Submit** button.   
       
     Your workflow should look like this:  
       
     ![](sys_attachment.do?sys_id=4ff720c11b047414f34d33bc1d4bcb5c)  
      
12.  Find the **Log Trace Message** Activity in the **Utilities** folder.
13.  Hold the mouse down and drag the Activity onto the canvas.
14.  Hover the activity over the transition line between **Log Message** and **End** until the line turns blue.
15.  Release the mouse.
16.  Fill out the form as follows:  
       
     Name **K14 Log Trace Message**.  
      
17.  Click **Submit**.  
       
     Your workflow should look like this:  
       
     ![](sys_attachment.do?sys_id=87f720c11b047414f34d33bc1d4bcb9c)  
      
18.  Find the **Run Script** Activity in the **Utilities** folder.
19.  Hold the mouse down and drag the Activity onto the canvas.
20.  Hover the activity over the transition line between the **Log Trace Message** and **End** Activities until the line turns blue.
21.  Release the mouse.  
       
     Fill out the form as follows:  
       
     Name: **K14 Log Message from inside Run Script**  
     Script:  
     **workflow.debug(‘Logging DEBUG from inside a script’);****  
     workflow.info(‘Logging INFO from inside a script’);**  
      
22.  Click the **Submit** button.  
       
     Your workflow should look like this:  
       
     ![](sys_attachment.do?sys_id=0ff720c11b047414f34d33bc1d4bcb9d)  
      
23.  Click the green **Play** button in the header of the canvas.  
       
     ![](sys_attachment.do?sys_id=83f720c11b047414f34d33bc1d4bcb9f)  
      
24.  Click the **Submit** button.  
       
     ![](sys_attachment.do?sys_id=0bf720c11b047414f34d33bc1d4bcba0)  
       
     QUESTION: What does the blue coloring of the activities tell us? 

  

**Review logging output**

  

1.  Return to the main ServiceNow tab. 
2.  In the Applications Select the **All Contexts** module in the Workflow.   
      
    ![](sys_attachment.do?sys_id=8ff720c11b047414f34d33bc1d4bcba1)  
     
3.  Select the Workflow Execution: **K14 Logging Demo** context.  
      
    ![](sys_attachment.do?sys_id=07f720c11b047414f34d33bc1d4bcba3)  
     
4.  Select the **Workflow Log** tab.  
      
    Notice the Source column:  
      
    ![](sys_attachment.do?sys_id=7ef720c11b047414f34d33bc1d4bcb51)  
      
    
    -   ENGINE is a message that is coming from within the Workflow Engine.
    -   ACTIVITY is a message that is coming from the JavaScript within a Workflow Activity.
    
      
    Notice the messages:  
      
    ![](sys_attachment.do?sys_id=f2f720c11b047414f34d33bc1d4bcb53)  
       
    
    (1) The first ACTIVITY message is the output of the Log Message Activity.  
    (2) The next three messages are the output of the Trace Message Activity. The Trace Message Activity logs the name assigned to the Activity, the event that the workflow is transitioning on, and the ID of the Workflow Context.  
    (3) The third message is the INFO message written in the Script field of the Run Script activity.
    
    QUESTION: What message is missing from this log?  
      
    The level of verbosity in the Workflow Log is configurable by properties.  
     
5.  **Workflow >** **Properties**.  
      
    ![](sys_attachment.do?sys_id=7af720c11b047414f34d33bc1d4bcb54)  
     
6.  Check the property **Log details of workflow actions.** This property sets the level of log messaging.
7.  Check **Log workflow debug messages.** It sets the level of log messaging while debugging is activated.
8.  Return to the Workflow Editor and close the tab.
9.  **Open** the K14 Logging Demo workflow. Note that the workflow is Checked out.
10.  Re-execute the workflow using the green **Play** arrow.  
       
     ![](sys_attachment.do?sys_id=fef720c11b047414f34d33bc1d4bcb55)
11.  Return to the main ServiceNow tab.
12.  **Workflow >** **All Contexts**.
13.  Find and select the most recently run **K14 Logging Demo** workflow.
14.  Select the **Workflow Log** tab.  
       
     Your list should look like this:  
       
     ![](sys_attachment.do?sys_id=76f720c11b047414f34d33bc1d4bcb57)  
       
     NOTE: The Actual number of Workflow Log messages will vary.  
       
     Notice:  
     
     -   The dramatic increase in Workflow Log entries.
     -   The mix of Debug and Information messages.
     -   How much information is coming from the ENGINE!
     
        
      

**Search the list for run script logging**

Do these next steps using the List filter. 

1.  Select: Go to **Message**.
2.  Type: **from Run Script.  
      
    ![](sys_attachment.do?sys_id=faf720c11b047414f34d33bc1d4bcb58)** 
3.  Click the Search icon (magnifying glass).Your list should look like this:  
      
    **![](sys_attachment.do?sys_id=72f720c11b047414f34d33bc1d4bcb5a)  
      
    **Notice the previously missing Debug message from the Run Script Activity is now in the Workflow Log. 

NOTE:  The Workflow Logging Properties apply to all running Contexts. Use them only when needed for debugging or testing to optimize performance on your instance.
