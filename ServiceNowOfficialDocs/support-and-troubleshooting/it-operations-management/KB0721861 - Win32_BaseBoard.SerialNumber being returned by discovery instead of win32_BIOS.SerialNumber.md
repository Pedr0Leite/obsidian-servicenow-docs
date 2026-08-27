---
title: "Win32_BaseBoard.SerialNumber being returned by discovery instead of win32_BIOS.SerialNumber"
aliases:
  - KB0721861
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0721861
kb_number: KB0721861
last_modified: 2024-04-07
---

## Win32\_BaseBoard.SerialNumber being returned by discovery instead of win32\_BIOS.SerialNumber

  

### Issue

Win32\_BaseBoard.SerialNumber being returned by discovery instead of win32\_BIOS.SerialNumber

### Resolution

Discovery is getting baseboard serial number as CI serial number.   
However bios serial number should be used instead.   
  
The solution is to modify the discovery pattern: Windows OS - Servers, and change bios serial numbers to be added after baseboard.   
Please refer to screenshot 01 which is the steps after the change on dev instance. 

Screenshot 01

![](/sys_attachment.do?sys_id=067aa866db42b450e515c22305961984)

When moving this pattern to prod instance, you can follow screenshot 02 to export the pattern as XML from the list view,   
then import on prod instance, and follow screenshot 03 to sync it with MID server.

Screenshot 02

![](/sys_attachment.do?sys_id=0a7aa866db42b450e515c22305961989)

Screenshot 03 

![](/sys_attachment.do?sys_id=ca7aa866db42b450e515c2230596198e)
