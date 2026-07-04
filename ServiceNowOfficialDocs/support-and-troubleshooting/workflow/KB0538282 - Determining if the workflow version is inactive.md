---
title: "Determining if the workflow version is inactive"
aliases:
  - KB0538282
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538282
kb_number: KB0538282
last_modified: 2024-09-20
---

## Determining if the workflow version is inactive

  

### Issue

Determining if the workflow version is inactive 

Symptoms

* * *

Symptoms may include the following:

-   Workflow did not run when expected
-   Workflow did not run on a specific record
-   Cannot publish workflow
-   Publishing workflow takes too long
-   Cannot modify checked out workflow
-   Cannot start workflow
-   Workflow does not trigger
-   Stalled workflow 

  
Finding the workflow version

* * *

Navigate to the **Workflow Versions** list view and open the workflow version to check.

![](/Screen%20shot%202014-04-25%20at%201.33.15%20PM%20.pngx)

  
  
To check via XML

* * *

While in the form view within the **Workflow Version** record, right-click on the menu and click **Show XML.** You can check the <active>tag to verify if it is true or false.

![](/sys_attachment.do?sys_id=bf4e7422db0ab450e515c223059619ce)  

To check via the workflow editor 

* * *

Click **Show Workflow** in the related links inside the workflow version record.

![](/Screen%20shot%202014-04-25%20at%202.58.13%20PM%20.pngx)

Click on the gear to check if the **Set Active** or **Set Inactive** option is there. Then you can determine the current active state of the workflow version.

![](/Screen%20shot%202014-04-25%20at%201.39.19%20PM%20.pngx)
