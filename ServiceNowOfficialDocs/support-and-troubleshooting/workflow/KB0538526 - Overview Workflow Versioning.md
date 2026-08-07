---
title: "Overview: Workflow Versioning"
aliases:
  - KB0538526
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538526
kb_number: KB0538526
last_modified: 2024-09-20
---

## Overview: Workflow Versioning

  

### Issue

**Overview:** Workflow Versioning 

  

**Goals**

-   Introduce workflow versioning
-   Experience checkout and publish.
-   Understanding versions in update sets

  

**Summary**

Workflow in ServiceNow offers versioning as a way to deploy an automated process that ensures safe editing of existing workflows. Versions are managed within the Check Out and Publish cycle.

There are three parts of this process: The Workflow, its list of versions, and the workflow model that is editable only when it is checked out.

Workflows may only have one Published version at a time. The Published version is the version that runs for all Glide Records that meet the conditions of the workflow.

Workflows may only have one Checked Out version at a time. The Checked Out version is the version that will run for all Glide Records that meet the conditions of the workflow only for the user who has the workflow Checked Out. This Check Out process provides safety in modifying and updating processes.

Workflows move from instance to instance through Update Sets. Only published workflows are pushed to update sets. The commit process of an Update Set ensures that the published version of a workflow in the Update Set becomes the published version on the target instance by setting all other versions of the committed workflow to Published = false.

### Resolution

**Workflow versioning**

A workflow consists of three parts:

-   The workflow, which is associated with a table.
-   The Workflow Version, which is characterized by Condition, Published Status, and permissions.
-   The Workflow Model, which is the workflow in its entirety as the set of Workflow Activities and their transitions (lines) within a given version.  
      
    Workflows are moved from one instance to another using Update Sets. 

  

**Workflow states**

A Workflow can have three states:  

-   **Published**: The Workflow is available to all users and Glide records that meet the conditions of the workflow.
-   **Unpublished**: The Workflow is no longer available for new Glide Records, but may be required for already running records.
-   **Checked Out**: The Workflow is available to run only for the User who has it checked out.

     
**Create an updated set**

Workflows are moved from one instance to another using an Update Set. For the purposes of this lab, we will create an Update Set called **K14 Workflow 101.** Throughout the lab, we will see how a workflow becomes published in the Update Set. We will not be moving the Update Set to a new instance.  To learn more about moving update sets from one instance to another see the lab: **Update Sets – Best Practices to Move Code Smoothly.** 

1.  In the Application Navigator Type filter text field, enter **Update Set.** 
2.  **System Update Sets > Local Update Sets**. The word local is used to describe Update Sets that are already present on the instance.
3.  Click **New.**
4.  Fill out the form as follows:  
      
    Name: **K14 Workflow 101**  
    My Current Set: **Check**  
      
    ![](sys_attachment.do?sys_id=90d7e4411b047414f34d33bc1d4bcbfe)  
      
     
5.  Click **Submit.** Check your work by clicking the Gear Menu on the right side of the banner and check that the **K14 Workflow 101 Update Set** is the current set.  
      
    ![](sys_attachment.do?sys_id=a0d728411b047414f34d33bc1d4bcb26)  
    

  
Create a workflow version

* * *

1.  Close the Workflow Editor tab. It is a good practice to close the tab after completing your work. The Workflow Editor tabs will stay open until you close them.
2.  Return to the Workflow Editor using **Workflow** \> **Workflow Editor.**  
      
    ![](sys_attachment.do?sys_id=90d7e4411b047414f34d33bc1d4bcbfe)  
      
    
3.  Create a new Workflow **Gear Menu** \> **New Workflow** (note that you can also click **New**).  
      
    Name:  **K14101 – Version Demo**  
    Table: **Incident**  
      
    ![](sys_attachment.do?sys_id=acd728411b047414f34d33bc1d4bcb28)  
     
4.  Click **Submit**.  
      
    ![](sys_attachment.do?sys_id=24d728411b047414f34d33bc1d4bcb2a)  
      
    
    In the Workflow Canvas header, notice the label on the Menu Bar. See the name of the workflow, just as it was entered into the Name field, and the **_Checked out by me_** a text_._
    
    A workflow that indicates that it is checked out runs only for the user that has the workflow checked out.  
      
    ![](sys_attachment.do?sys_id=28d728411b047414f34d33bc1d4bcb44)  
      
    Because this is a new workflow, there is only one version of the workflow, and that version will only run for the user who has the workflow _Checked out_.
    
     
5.  To see the relationship of a Workflow to its Workflow Versions, return to the main ServiceNow tab. Do not close the Workflow Editor.  
      
    ![](sys_attachment.do?sys_id=acd728411b047414f34d33bc1d4bcb45)  
      
     
6.  **Workflow > Workflow Versions.  
      
    **This is the list of all the active workflow versions on this instance. Find your **K14101-Version Demo** workflow.  
    
    What you see is the Workflow record and a Related List of Workflow Versions. In this case, there is only one version.
    
    ![](sys_attachment.do?sys_id=24d728411b047414f34d33bc1d4bcb47)  
      
    Looking at the Workflow Version record we see the following:  
      
      
    **(1) Published = false**  
      
    This indicates that this workflow is not available for general consumption on this instance.  
      
    **(2) Checked out by = K14101 WFAdmin**  
      
    This indicates the current editor of the workflow version and the only person this version of the workflow will run for.  
      
    
7.  Return to the Workflow Editor by re-selecting the second ServiceNow tab.
8.  Using the **Gear Menu,** select **Publish**.  
    
    NOTE:  In subsequent labs, these steps will be abbreviated to **Gear Menu** > **Publish.**
    
    The header of your workflow should look like this:  
      
    ![](sys_attachment.do?sys_id=a8d728411b047414f34d33bc1d4bcb48)  
      
     
9.  Return to the main ServiceNow tab.
10.  **Refresh List** in the Workflow Version list. You can do this by right-clicking the context-sensitive menu in the list header.  
       
     The Related List of your workflow versions should look like this:  
       
     ![](sys_attachment.do?sys_id=18d7e4411b047414f34d33bc1d4bcbff)  
       
     
     Looking at the Workflow Version record we see the following:
     
     (1) **Published = true (**Indicating that this workflow is now available for use on this instance.)  
     (2) **Checked out by = blank**  
      

  
**Workflow version life cycle**

A workflow goes through the Develop -> QA -> Deploy life cycle on the same instance using the Checked Out -> Published states. 

In ServiceNow Best Practices, a workflow Develop -> QA -> Deploy process is managed across at least 2 instances (Dev. -> Production), sometimes 3 (Dev. -> QA -> Production).  A workflow is moved from one instance to another using an Update Set. A workflow is added to an Update Set on Publish. Checked Out workflows will not be entered into an Update Set, making them very safe for development and test. 

![](sys_attachment.do?sys_id=acd728411b047414f34d33bc1d4bcb00) 

1.  Return to the main ServiceNow tab. 
2.  In the Application Navigator Type filter text field, enter **Update Set.**
3.  **Select Local Update Sets.  
      
    **Your Update Sets list should at the minimum list these Update Sets: **![](sys_attachment.do?sys_id=24d728411b047414f34d33bc1d4bcb02)**
4.  Select the K14 Workflow 101 Update Set.
5.  Scroll down to the **Customer Update-related** list.  
      
    ![](sys_attachment.do?sys_id=a8d728411b047414f34d33bc1d4bcb03)  
     
6.  Select the update record.  
      
    ![](sys_attachment.do?sys_id=20d728411b047414f34d33bc1d4bcb05)  
      
    Notice the Payload field. The content of the Payload field is the XML mapping of all the database entries required to move the Workflow and its dependencies. 

  

**Edit then publish a workflow**

1.  Return to the Workflow Editor tab.
2.  Select **Gear Menu > Checkout**.  
      
    Your workflow header bar will again reflect the checked-out status like this:  
      
    ![](sys_attachment.do?sys_id=24d728411b047414f34d33bc1d4bcb1f)
3.  Return to the **ServiceNow** main tab.
4.  **Workflow > Workflow Versions.**
5.  Find the **K14101 – Version Demo** in the list.  
      
    ![](sys_attachment.do?sys_id=2cd728411b047414f34d33bc1d4bcb24)  
      
    The workflow version that was published earlier and is in the **K14 Workflow 101** Update Set is at this time unchanged.  There is also now another version associated with this workflow.  
    
    This is the Checked Out version that was just created in the Workflow Editor. This version of the workflow will run, as we learned earlier, only for the **K14WF Admin** user, while the existing, Published version will run for all other users on the instance who meet the conditions of the workflow 
    
6.  Return to the Workflow Editor tab.
7.  Select **Gear Menu > Publish**.
8.  Return to the main **ServiceNow** tab.
9.  Refresh the Workflow Version list.  
      
    ![](sys_attachment.do?sys_id=20d728411b047414f34d33bc1d4bcb22)  
      
    Notice that there is now only one version of the K14101 – Version.  
      
    
    -   All processes already running against that original workflow will continue to run against that version.
    -   The edited version is now the published version.
    -   All new Glide Records that meet the conditions of the Workflow will run against the new version.
    
    It is not possible to apply a newly published workflow to existing records. The Workflow Engine evaluates the conditions when the record is inserted and identifies the ID of the appropriate workflow version. From that point on, the Workflow Engine needs only reference the ID of the version and not the conditions.
    
    To see how that publish event affected the update set:  
     
10.  In the text filter type **Update Set**.
11.  Select **Local Update Sets**.
12.  Select the **K14 Workflow 101** Update Set.
13.  Scroll down to the **Customer Update-related** list.  
       
     ![](sys_attachment.do?sys_id=a4d728411b047414f34d33bc1d4bcb23)   
       
     Notice that:  
     
     -   The original workflow now has an UPDATE action.  
         -   This update is to change the Published state from true to false.
     -   The newly published version INSERT\_OR\_UPDATE.  
         -   This is a new insert into the update set of the newly published workflow.
     
     When the Update Set is moved to the new instance, the commit process ensures that the published version of the Workflow in the committed Update Set will be the published version on the instance for all users and Glide Records that meet the conditions of the Workflow.
