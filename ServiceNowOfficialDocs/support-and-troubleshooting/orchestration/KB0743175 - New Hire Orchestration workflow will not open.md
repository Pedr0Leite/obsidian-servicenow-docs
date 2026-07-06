---
title: "New Hire Orchestration workflow will not open"
aliases:
  - KB0743175
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0743175
kb_number: KB0743175
last_modified: 2024-04-07
---

## New Hire Orchestration workflow will not open

  

### Issue

# Symptoms

* * *

Workflow does not load and the wheel keeps on spinning on workflow editor.

# Release

* * *

London Patch 4

# Cause

* * *

Orchestration Activities are not present in the instance which fails the workflow to load.

# Resolution

* * *

First ground rule, identify the custom activities which needs modification and validate that it has the same "SYS\_ID" on all the instances.   
No changes or modifications should be done to the update sets which capture the changes.  
  
Custom Activity:   
  
On source instance   
First create an update set in the Application where the workflow and custom activity are and then make it the current update set to contain the change of the custom activity   
Once the update set is made current, then open Workflow editor. This way we can make sure the workflow is opened in the correct application.   
Make the necessary changes.   
Complete the Update set.   
  
On target instance:   
Retrieve the update set that contains the custom activity which was modified.   
Preview the update set   
Commit the update set   
Now open Workflow Editor.   
Open the Custom tab of the Workflow Editor, check the activity's version.   
Open the workflow and notice that the "Custom Activity" is color coded to orange.   
Click on the Custom activity and check if there is a dialog indicating that there is a newer version of the activity.   
  
Workflow:   
  
On source instance:   
Create a new update set in the Application where the workflow is to hold the Workflow change.   
Open Workflow Editor:   
Check out the workflow   
Updated the "Custom Activity" to the newer version available.   
Notice the changes done on the custom activity.   
Publish the workflow.   
Complete the update set   
  
On target instance:   
Retrieve the update set that contains the workflow which was modified.   
Preview update set   
Commit the update set.   
Open the Workflow Editor   
Select the "Workflow" tab   
Open the workflow.   
Notice that the workflow is updated with the changes done on the custom activity.
