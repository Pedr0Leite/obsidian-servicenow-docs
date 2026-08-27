---
title: "ServiceNow WMI Collector service missing from Windows Services on MID Server host"
aliases:
  - KB0758133
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0758133
kb_number: KB0758133
last_modified: 2026-07-02
---

## ServiceNow WMI Collector service missing from Windows Services on MID Server host

  

### Issue

-   Upon installing MID server on a new Host Machine, we can see "**ServiceNow MID Server**" service getting listed but there exist no service or reference to "**ServiceNow WMI Collector**" service under Windows Services in the same MID Server host machine. 

![Screenshot of Windows Services window](sys_attachment.do?sys_id=9136d15647fd439cf93138ce536d4364)

### Release

Orlando and older releases.

### Cause

-   Found **WMI\_Collector.exe** already available under MID server agent install location: **C:\\servicenow\\mid\\agent\\bin\\sw\_wmi\\bin**. However, upon running wmi\_collector.exe manually it could not find service listed. Please refer below error screenshot.

![Windows service error message](sys_attachment.do?sys_id=0536d15647fd439cf93138ce536d435e)

### Resolution

-   In order to fix this issue, Manually create the service from MID Server host machine in command prompt.
-   **Command**: sc.exe create "ServiceNow WMI Collector" binPath= C:\\servicenow\\mid\\agent\\bin\\sw\_wmi\\bin\\wmi\_collector.exe start= auto
-   New "ServiceNow WMI Collector" service created in Windows services and successfully gets listed under service.

![Window showing ServiceNow WMI Collector running](sys_attachment.do?sys_id=1536d55647fd439cf93138ce536d431a)
