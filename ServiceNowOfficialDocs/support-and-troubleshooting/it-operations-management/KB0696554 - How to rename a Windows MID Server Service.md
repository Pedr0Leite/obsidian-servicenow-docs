---
title: "How to rename a Windows MID Server Service"
aliases:
  - KB0696554
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696554
kb_number: KB0696554
last_modified: 2025-01-03
---

## How to rename a Windows MID Server Service

  

### Issue

  
  

# Description

* * *

There may be a time when a user wishes to rename what is shown for a MID Server name in Windows Services. This involves removing the service and then reinstalling it.

# Procedure

* * *

1\. Log onto the Windows Server hosting the MID Server.

2\. Stop the MID Server Service in Windows Control panel > Administrative tools > Services.

3\. Run <MID Server installation directory>\\bin\\UninstallMID-NT.bat to remove the old Windows Service. 

4\. Open the file <MID Server installation directory>\\conf\\wrapper-override.conf

Edit the line: 

    wrapper.displayname=ServiceNow MID Server\_NEW\_MID\_SERVER\_NAME\_HERE

Note: You can consider keeping the name prefix "ServiceNow MID Server\_" as this will allow for easier troubleshooting in the future. 

5\. Save the file. 

6\. Run the file <MID Server installation directory>\\bin\\InstallMID-NT.bat to install a Windows Service with the new name. 

7\. Back in Windows Services, right click and refresh the window, then Start the new service. 

The MID Server will now reconnect to the instance. 

You will need to repeat this for each MID Server that you wish to rename. 

# Applicable Versions

* * *

Any
