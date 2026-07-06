---
title: "\"PowerShellVersionUnsupportedException\" error during discovery causes the schedule to hang"
aliases:
  - KB0750843
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0750843
kb_number: KB0750843
last_modified: 2024-04-07
---

## Issue

"PowerShellVersionUnsupportedException" error during discovery causes the schedule to hang. Below are the symptoms:

1) The discovery schedule gets stuck and all the ECC queue records for the affected mid server will be in ready state.

2) Mid Server agent logs will have the below errors :

ECCQueueMonitor.5 SEVERE \*\*\* ERROR \*\*\* java.lang.NullPointerException   
java.lang.NullPointerException   
at com.service\_now.mid.probe.PowershellProbe.isValid(PowershellProbe.java:238)   
  
ECCQueueMonitor.5 SEVERE \*\*\* ERROR \*\*\* java.lang.reflect.InvocationTargetException   
java.lang.reflect.InvocationTargetException   
at sun.reflect.GeneratedConstructorAccessor24.newInstance(Unknown Source)   
at sun.reflect.DelegatingConstructorAccessorImpl.newInstance(DelegatingConstructorAccessorImpl.java:45)   
  
Caused by: com.snc.automation\_common.integration.exceptions.PowerShellVersionUnsupportedException: Error encountered when invoking PowerShell, the result from running '"C:\\Windows\\SysWOW64\\WindowsPowerShell\\v1.0\\powershell.exe   
C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -noninteractive -nologo -noprofile -command "$ver = if (Test-Path Variable:\\PSVersionTable) { $PSVersionTable.PSVersion } else { (get-host).Version }; 'full\_version:' + $ver.ToString() + ', major\_version:' + $ver.Major"' is   
at com.service\_now.mid.probe.util.PowershellStatus.validate(PowershellStatus.java:100)   
at com.service\_now.mid.probe.Powershell.<init>(Powershell.java:204) 

## Resolution

Make sure the path for PowerShell in the PATH environment is set correctly on the mid server.
