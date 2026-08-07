---
title: "Windows server and desktop discovery - assigned_to field"
aliases:
  - KB0751713
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0751713
kb_number: KB0751713
last_modified: 2024-04-07
---

## Windows server and desktop discovery - assigned\_to field

  

### Issue

# Overview

If you are using Windows OS - Desktops or Windows OS - Servers for Windows Discovery, the "assigned\_to" that is set on the CI, is fetched from "Win32\_ComputerSystem" WMI class, "UserName" object.

UserName gives us the name of a user that is logged on currently. This property must have a value. In a terminal services session, UserName returns the name of the user that is logged on to the console, not the user logged on during the terminal service session. 

# Additional Information

[https://docs.microsoft.com/en-us/windows/desktop/cimwin32prov/win32-computersystem](https://docs.microsoft.com/en-us/windows/desktop/cimwin32prov/win32-computersystem)
