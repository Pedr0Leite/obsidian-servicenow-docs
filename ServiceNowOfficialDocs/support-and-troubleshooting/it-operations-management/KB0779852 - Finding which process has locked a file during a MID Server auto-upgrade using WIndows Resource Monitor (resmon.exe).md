---
title: "Finding which process has locked a file during a MID Server auto-upgrade using WIndows Resource Monitor (resmon.exe)"
aliases:
  - KB0779852
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779852
kb_number: KB0779852
last_modified: 2026-04-13
---

## Finding which process has locked a file during a MID Server auto-upgrade using WIndows Resource Monitor (resmon.exe)

  

### Summary

This article aims to suggest tools that may be useful to investigate **File Locks that cause timeout and crashes of the "ServiceNow Platform Distribution Upgrade" service**. 

This KB article gives one way of recovering from this situation, and lists some of the Known Problems related to this that we are currently trying to get to the bottom of:  
[KB0779816 How to continue a MID Server upgrade after it has crashed in the middle of the ServiceNow Platform Distribution Upgrade service, leaving the MID Server Down and the Service not running](https://hi.service-now.com/kb_view.do?sysparm_article=KB0779816 "KB0779816 How to continue a MID Server upgrade after it has crashed in the middle of the ServiceNow Platform Distribution Upgrade service, leaving the MID Server Down and the Service not running")

When a MID Server upgrades itself, it launches a "ServiceNow Platform Distribution Upgrade" service, and then shuts itself down (which can be confirmed in the logs/agent0.log.0 file). For the upgrade service to delete/copy/overwrite all the files to do with the main "ServiceNow MID Server\_..." service, **it must be fully shut down with all files freed up, or the upgrade will fail**.  The agent/logs/agent0.log.0 and agent/logs/wrapper.log may only show what the main service was doing up to the upgrade service was started, and not the upgrade itself.

While the upgrade service runs, it will log to upgrade-wrapper.log somewhere in a temp folder. This should be monitored as the upgrade service runs, and tools used to check what files remain locked, and locked by what, in order to figure out why it fails.

You can find **glide-dist-upgrade.log** like so:

1.  Search the agent log of the mid server for the string "Added marker". You should find a line like this, although the folder will be different.  
    
    AutoUpgrade.3600 Added marker \`C:\\WINDOWS\\TEMP\\1569035472492-0\` to upgrade marker file.
    
2.  Open that folder, and then navigate through further sub-folder to **upgrade-wrapper\\logs\\glide-dist-upgrade.log**  
    e.g. **C:\\WINDOWS\\TEMP\\<a long number>\\upgrade-wrapper\\logs\\glide-dist-upgrade.log**

The sort of errors in that log that we need to figure out the cause of are:-

Here we see a timeout while trying to delete agent\\lib\\sigar-amd64-winnt.dll. This will be retried, and so won't break anything immediately, but even starting to delete files before the main mid server service has fully stopped is not good.

INFO | jvm 1 | 2018/04/27 17:12:11.951 | INFO: E:\\ServiceNow\\MID\_Server\\agent\\lib\\sigar-amd64-winnt.dll cannot be deleted: E:\\ServiceNow\\MID\_Server\\**agent\\lib\\sigar-amd64-winnt.dll** (The process cannot access the file because it is being used by another process)

Here an exception is caused that crashes the upgrade service, while trying to access agent\\bin\\wrapper-windows-x86-64.exe. Is that because another process, such as antivirus, is locking it?

INFO | jvm 1 | 2018/04/27 17:12:19.232 | SEVERE: com.snc.dist.mid\_upgrade.UpgradeException: java.io.FileNotFoundException: E:\\ServiceNow\\MID\_Server\\**agent\\bin\\wrapper-windows-x86-64.exe** (Access is denied)  
INFO | jvm 1 | 2018/04/27 17:12:19.248 | com.snc.dist.mid\_upgrade.UpgradeException: java.io.FileNotFoundException: E:\\ServiceNow\\MID\_Server\\agent\\bin\\wrapper-windows-x86-64.exe (Access is denied)

Here we see the jre folder cannot be deleted:

INFO   | jvm 1    | 2019/09/21 16:30:47.114 | Sep 21, 2019 4:30:47 PM com.snc.dist.mid\_upgrade.UpgradeMain deleteJreDirIfSourced
INFO   | jvm 1    | 2019/09/21 16:30:47.130 | INFO: Removing previous MID JRE at \`C:\\ServiceNow\\agent\\jre\`.
INFO   | jvm 1    | 2019/09/21 16:30:47.802 | Sep 21, 2019 4:30:47 PM com.snc.dist.mid\_upgrade.UpgradeMain deleteJreDirIfSourced
INFO   | jvm 1    | 2019/09/21 16:30:47.817 | WARNING: java.io.IOException: Unable to delete directory C:\\ServiceNow\\agent\\jre\\bin.
INFO   | jvm 1    | 2019/09/21 16:30:47.833 | java.io.IOException: **Unable to delete directory C:\\ServiceNow\\agent\\jre\\bin**.

### Release

Any, where MID Servers regularly fail to auto-upgrade _after_ launching the "ServiceNow Platform Distribution Upgrade" service.

### Instructions

#### Windows Resource Monitor

This tool, which is out-of-box on all Windows Servers, can be used to see what File locks exist.

In this example I:

-   Run Resource Monitor (remon.exe)
-   Click 'CPU' tab
-   In the 'Processes' section, select all, by ticking next to 'Images' at the top
-   In the 'Associated Handles' section, in the Search Handles search box, add something that filter for only files within the MID Sever installation folders.  
    e.g. C:\\ServiceNow\\MID\_SERVERS\\Prod\_Disco\_MID\\agent

![](/sys_attachment.do?sys_id=d18c47fcdb8434d0471f9c41ba961971)

### Related Links

Where this process is used, it is important to record other pertinent info of the server in case the cause is not immediately clear. This may come in useful later:

-   Which OS version? e.g. Windows Server 2012R2 SP1
-   What Anti-Virus and security software is also running? e.g. McAfee, WIndows defender
-   Which folder is the MID Server installed in, and is this within a Users profile? e.g. Downloads or Desktop of a user.
-   Which user was the mid server service running as, and is that a member of the local Administrators group?
-   Is the Server a VM, and what resources does it have?
-   Which JRE is installed?
-   ...
