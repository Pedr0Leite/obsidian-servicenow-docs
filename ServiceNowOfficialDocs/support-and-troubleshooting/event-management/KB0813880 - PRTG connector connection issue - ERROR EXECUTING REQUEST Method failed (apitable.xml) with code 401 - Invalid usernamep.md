---
title: "PRTG connector connection issue - ERROR EXECUTING REQUEST: Method failed: (/api/table.xml) with code: 401 - Invalid username/password combo"
aliases:
  - KB0813880
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813880
kb_number: KB0813880
last_modified: 2024-04-08
---

## PRTG connector connection issue - ERROR EXECUTING REQUEST: Method failed: (/api/table.xml) with code: 401 - Invalid username/password combo

  

### Issue

-   Post Configuration of PRTG connector and mapping with credentials, when the **Test Connection** is executed the connector shows status as Error status with the below message.

Connection test failed: ERROR EXECUTING REQUEST: Method failed: (/api/table.xml) with code: 401 - Invalid username/password combo TypeError: Cannot read property "0" from null Check point from our side: 

![](sys_attachment.do?sys_id=8b036005dbc8f0d016d2a345ca9619b7)

### Cause

-   The issue is observed with the Password used for configuration.

### Resolution

-   In order to resolve this issue, please check below:  
    -   The username should be defined in the **Login name** in the PRTG system (in the user management screen)
    -   The password field value needs the _**passhash**_ value from PRTG. This is a _**hashed password**_ value, and not what was originally entered as plaintext into PRTG.  
        Note: see the PRTG manual for finding the hashed password [https://www.paessler.com/manuals/prtg/my\_account\_settings](https://www.paessler.com/manuals/prtg/my_account_settings)

![](sys_attachment.do?sys_id=cf036005dbc8f0d016d2a345ca9619b3)

-   If there are no users in the PRTG system (in the user management screen), you should define one. After making the above changes, the connector started working without any issue.

![](sys_attachment.do?sys_id=07036005dbc8f0d016d2a345ca9619b6)
