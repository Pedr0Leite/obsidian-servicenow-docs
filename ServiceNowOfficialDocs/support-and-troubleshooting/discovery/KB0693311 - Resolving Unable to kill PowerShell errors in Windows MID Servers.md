---
title: "Resolving \"Unable to kill PowerShell\" errors in Windows MID Servers"
aliases:
  - KB0693311
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0693311
kb_number: KB0693311
last_modified: 2024-04-16
---

## Issue

  
  

# Description

* * *

As part of Discovery for Windows machines (and during Orchestration) the MID server executes Powershell scripts from the MID server to the intended remote targets. After these scripts are completed a java process uses taskkill.exe on the MID to kill the Powershell process.

If the client reports a high volume of hung taskkill.exe processes and you observe errors similar to the following in the agent log, the client is likely subject to this bug:

  
04/03/18 08:10:29 (253) Worker-Interactive:PowershellProbe WARNING \*\*\* WARNING \*\*\* PowershellProcessRunner terminated due to interrupt java.lang.InterruptedException   
04/03/18 08:10:29 (253) ProbeReaper Probe reaper interrupted following thread: Worker-Interactive:PowershellProbe id: 58   
04/03/18 08:10:29 (316) Worker-Interactive:PowershellProbe WARNING \*\*\* WARNING \*\*\* Attempting to kill PowerShell, PID =15496   
04/03/18 08:10:29 (347) Worker-Interactive:PowershellProbe WARNING \*\*\* WARNING \*\*\* ProcessRunner terminated due to interrupt java.lang.InterruptedException   
04/03/18 08:10:29 (347) Gobbling stdout: cmd.exe /C Taskkill /F /PID 15496 SEVERE \*\*\* ERROR \*\*\* IOException while gobbling stream   
java.io.IOException: Stream closed   
at java.io.BufferedInputStream.getInIfOpen(BufferedInputStream.java:159)   
at java.io.BufferedInputStream.available(BufferedInputStream.java:410)   
at com.glide.util.StreamGobbler.run(StreamGobbler.java:75)   
  

# Procedure

* * *

Microsoft has provided a hotfix, which will need to be installed, located here: 

[https://support.microsoft.com/en-us/help/2798040/you-cannot-stop-a-process-by-using-the-taskkill-exe-utility-in-windows](https://support.microsoft.com/en-us/help/2798040/you-cannot-stop-a-process-by-using-the-taskkill-exe-utility-in-windows) 

# Applicable Versions

* * *

Any with MID server running a Windows version affected by the bug as listed in the article

#
