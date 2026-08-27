---
title: "Modify Discovery to prevent updating the assignee in configuration items"
aliases:
  - KB0788805
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0788805
kb_number: KB0788805
last_modified: 2025-07-07
---

## Modify Discovery to prevent updating the assignee in configuration items

  

### Issue

By default, Discovery changes the assignee in configuration items (CI) to the last signed-in user found in the Windows Management Interface (WMI). 

### Resolution

The glide.wmi.assigned\_to\_always\_overwrite property controls updates to the assigned\_to field.

To prevent updates to this field, modify the **Windows OS - Pre Sensor** field. 

1\. Go to **Pattern Pre/Post Script** > **Windows OS - Pre Sensor**.

2\. Find the following code.

if(windowsServer){  
setAssignedTo();  
addLocationToHyperV();  
}

3\. Comment out the following line as shown.

//setAssignedTo();
