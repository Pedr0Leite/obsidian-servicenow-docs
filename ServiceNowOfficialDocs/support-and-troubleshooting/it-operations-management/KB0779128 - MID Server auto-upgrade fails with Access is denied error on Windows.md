---
title: "MID Server auto-upgrade fails with \"Access is denied\" error on Windows"
aliases:
  - KB0779128
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779128
kb_number: KB0779128
last_modified: 2026-05-19
---

## MID Server auto-upgrade fails with "Access is denied" error on Windows

  

### Issue

The MID Server auto-upgrade fails when the required Windows service is not running on the MID Server host. The following errors appear in the wrapper logs:

```
INFO | jvm 1 | 2019/09/07 14:54:15.102 | INFO: <drive>:\ServiceNow\<MID_Server_Name>\agent\lib\sigar-x86-winnt.dll cannot be deleted: <drive>:\ServiceNow\<MID_Server_Name>\agent\lib\sigar-x86-winnt.dll (The process cannot access the file because it is being used by another process)

INFO | jvm 1 | 2019/09/07 14:54:27.582 | SEVERE: com.snc.dist.mid_upgrade.UpgradeException: java.io.FileNotFoundException: <drive>:\ServiceNow\<MID_Server_Name>\agent\bin\wrapper-windows-x86-64.exe (Access is denied)

INFO | jvm 1 | 2019/09/07 14:54:27.598 | Caused by: java.io.FileNotFoundException: <drive>:\ServiceNow\<MID_Server_Name>\agent\bin\wrapper-windows-x86-64.exe (Access is denied)
```

### Release

ANY

### Cause

The _ServiceNow Platform Distribution Upgrade_ Windows service is not running on the MID Server host.

![](/sys_attachment.do?sys_id=551dbd4c478d83d8bb78d9d8736d4344)

### Resolution

1.  On the MID Server host, open the Windows Services panel. To do this, press the Windows key + R, enter `services.msc`, and press Enter.
2.  Locate the service named ServiceNow Platform Distribution Upgrade.
3.  Right-select the service and select Start.
4.  After the service starts, monitor the MID Server wrapper logs to confirm the auto-upgrade completes without errors.
5.  In the ServiceNow instance, navigate to MID Server > MID Servers and verify that the MID Server version matches the current instance version.
