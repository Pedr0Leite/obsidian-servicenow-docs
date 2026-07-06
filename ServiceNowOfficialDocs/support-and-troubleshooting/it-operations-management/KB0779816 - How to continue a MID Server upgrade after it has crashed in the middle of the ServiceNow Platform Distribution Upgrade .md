---
title: "How to continue a MID Server upgrade after it has crashed in the middle of the ServiceNow Platform Distribution Upgrade service leaving the MID Server down and service not running"
aliases:
  - KB0779816
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779816
kb_number: KB0779816
last_modified: 2026-05-12
---

## How to continue a MID Server upgrade after it has crashed in the middle of the ServiceNow Platform Distribution Upgrade service leaving the MID Server down and service not running

  

### Issue

There are several known problems that cause a MID Server upgrade to stop while in the middle of running the **Upgrade** service process. These are often due to timeouts or exceptions, often to do with files of the main MID Server service still being locked at the time the Upgrade is trying to delete/overwrite those files.

Prior to the Orlando release this service was an actual Windows Service named "ServiceNow Platform Distribution Upgrade (<MID Server Name>)", but to support non-administrator MID Server service users, this process was changed to run the same code but as a normal process.

This method allows the upgrade service to have another go at replacing the files and restarting the main service. The reason works is that the Anti-Virus software has already scanned the files and now knows to trust them, so doesn't interfere on the second go. This should be tried first, before doing anything destructive like a manual upgrade (see [KB0713557](https://support.servicenow.com/kb_view.do?sysparm_article=KB0713557 "KB0713557")), or a re-install.

**Do not start the mid server service in this situation**.  You may have a half-deleted/replaced install that is currently not viable, and if it is able to start then the automatic cleaning up of the temp folder happens, which you need for this process to work. e.g. Everything in the agent\\lib folder may already be deleted.

Symptoms where this can be useful:

-   A MID Server that is set as Down shortly after an instance upgrade.
-   The agent log of the MID Server shows that it shut itself down shortly after launching the Upgrade, and there are no more entries.
-   When inspecting the Windows Services of the host running the MID Server, you see nothing is running, and the ServiceNow Platform Distribution Upgrade service remains in the list

You must check and save the glide-dist-upgrade.log file in the temp folder, which is likely to confirm why the upgrade service did deliberately stop without starting the mid server, because it knew at the point of the failure that it would be unsafe to start the service.:  
**<%TEMP%>\\<a long number>\\upgrade-wrapper\\logs\\glide-dist-upgrade.log**

From the Rome release, the temp folder is created within the agent folder, under **\\agent\\work\\upgrade\_temp\\<a long number>\\upgrade-wrapper\\logs\\glide-dist-upgrade.log**

### Release

Any

### Cause

Known causes where this might be useful are listed in:  
[KB0696937 MID Server upgrade process - What actually happens when a MID Server upgrades itself?](https://support.servicenow.com/kb_view.do?sysparm_article=KB0696937 "KB0696937 MID Server upgrade process - What actually happens when a MID Server upgrades itself?")

### Resolution

1.  Optional: Ideally, copy logs that may help explain the cause - see below.
2.  The temp folder (see below) will contain a script that can be run to launch the upgrade service again. Depending on the operating system:  
    -   **Windows**: <temp folder>\\upgrade-wrapper\\bin\\**glide-dist-upgrade.bat start**
    -   **Linux**: in the folder <temp folder>\\upgrade-wrapper\\bin\\  **"sudo ./glide-dist-upgrade.sh start"**
3.  Wait for a few minutes, and see if the MID Server is Up in the instance. 

If you see just 1 log line "The ServiceNow Platform Distribution Upgrade (xxx) service is not installed ...", and nothing else, then you may still be able to run the wrapper executable directly to continue the upgrade.

-   cd <temp folder>\\upgrade-wrapper\\bin\\
-   **wrapper-windows-x86-64.exe -c ..\\conf\\wrapper.conf**

If you are able to, please use the following steps to capture the upgrade service logs, so you can pass them on to ServiceNow Technical Support in a HI Case. The agent/logs/agent0.log.0 and agent/logs/wrapper.log may only show what the main service was doing up to the upgrade only, and not the upgrade itself.

If this doesn't work then Support will absolutely need this additional log from the temp folder:-

1.  Search the agent log of the mid server for the string "Added marker". You should find a line like this, although the folder will be different.  
    
    AutoUpgrade.3600 Added marker \`C:\\WINDOWS\\TEMP\\1569035472492-0\` to upgrade marker file.
    
2.  Open that folder, and then navigate through further sub-folder to upgrade-wrapper\\logs\\**glide-dist-upgrade.log**  
    e.g. **C:\\WINDOWS\\TEMP\\<a long number>\\upgrade-wrapper\\logs\\glide-dist-upgrade.log** 

That upgrade-wrapper.log may be the only chance to explain why the upgrade service crashed, especially if the crash occurred before the log was copied into the main wrapper.log. Attempting to start the main "ServiceNow MID Server\_<MID Server Name>" may lead to the temporary folder being deleted, at which point that is lost.

### Related Links

To understand the MID Server upgrade process, the steps involved, how it could in theory go wrong, and why this method might work for you, please refer to:  
[KB0696937 MID Server upgrade process - What actually happens when a MID Server upgrades itself?](https://support.servicenow.com/kb_view.do?sysparm_article=KB0696937 "KB0696937 MID Server upgrade process - What actually happens when a MID Server upgrades itself?")
