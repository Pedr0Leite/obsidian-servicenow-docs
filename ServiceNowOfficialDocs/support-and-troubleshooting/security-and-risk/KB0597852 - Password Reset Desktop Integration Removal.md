---
title: "Password Reset Desktop Integration Removal"
aliases:
  - KB0597852
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0597852
kb_number: KB0597852
last_modified: 2024-04-07
---

## Issue

Password Reset Desktop Integration Removal

Overview

* * *

This article explains how to identify and uninstall the Password Reset Desktop Integration application in Microsoft Windows.

Determine if the Password Reset Desktop Integration application is installed

* * *

1.  Click **Start > Control Panel > Programs and Features**.
2.  In the search box, type **ServiceNow**.
3.  The application is installed if you see an application named **PasswordResetDesktopIntegration** or **Password\_Reset\_Desktop\_Integration**.  
      
    ![Password Reset Desktop Integration Application Is Installed](sys_attachment.do?sys_id=24d8646edb02b450e515c22305961972 "Password Reset Desktop Integration Application Is Installed")

Uninstall the Password Reset Desktop Integration application

* * *

1.  Right-click on the application name and select **Uninstall**.
2.  In the confirmation, click **Yes**.
3.  Repeat steps 1-2 for all instances of the Password Reset Desktop Integration application (you may have more than one).
4.  Restart Windows.
5.  Delete the following files from the **C:\\Program Files\\ServiceNow** directory  
      
    ![Files To Delete](sys_attachment.do?sys_id=28d8646edb02b450e515c22305961987 "Files To Delete")  
      
    
6.  After you restart, verify that the uninstall was successful by going back to **Start > Control Panel >Programs and Features** and typing **ServiceNow** in the search box. You should see no results.  
      
      
    ![Uninstall Was Successful](sys_attachment.do?sys_id=ecd8646edb02b450e515c22305961993 "Uninstall Was Successful")  
      
      
    It is recommended that the original installation file be deleted as well to prevent an outdated or unsupported version from being installed.
