---
title: "Configuring multiple SCOM instances(SCOM 2012 and SCOM 2016) at the same time to your ServiceNow instance. "
aliases:
  - KB0714098
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0714098
kb_number: KB0714098
last_modified: 2024-04-07
---

## Issue

# Symptoms

* * *

Configuring multiple SCOM instances at the same time to your ServiceNow instance. 

# Release

* * *

ALL.

# Cause

* * *

This generally happens when you try to use the SCOM 2012 and SCOM 2016 together and the name change you make to the .dll file for the SCOM 2016 connector is as follows-   
Microsoft.EnterpriseManagement.OperationsManager.2016.dll. 

  
 

# Resolution

* * *

  
However, if you're using the SCOM 2016 connector, it is recommended to go by appending 2012 as your version number in the .dll file name. You should also be specifying 2012 on the scom\_version parameter for your SCOM 2016 connector.   
  
Please change the filename to include 2016 instead of 2012 like below and then run a test. 

Microsoft.EnterpriseManagement.OperationsManager.2012.dll.
