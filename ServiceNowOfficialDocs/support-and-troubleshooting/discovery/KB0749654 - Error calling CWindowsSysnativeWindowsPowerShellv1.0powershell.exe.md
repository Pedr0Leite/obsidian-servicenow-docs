---
title: "Error calling \"C:\Windows\Sysnative\WindowsPowerShell\v1.0\powershell.exe\"
aliases:
  - KB0749654
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749654
kb_number: KB0749654
last_modified: 2024-04-07
---

## Error calling "C:\\Windows\\Sysnative\\WindowsPowerShell\\v1.0\\powershell.exe"

  

### Issue

MID Server will have an error which includes:

C:\\Windows\\Sysnative\\WindowsPowerShell\\v1.0\\powershell.exe

Example when running upgrade:

Error encountered when invoking PowerShell, the result from running '"C:\\Windows\\Sysnative\\WindowsPowerShell\\v1.0\\powershell.exe" -noninteractive -nologo -noprofile -command "$ver = if (Test-Path Variable:\\PSVersionTable) { $PSVersionTable.PSVersion } else { (get-host).Version }; 'full\_version:' + $ver.ToString() + ', major\_version:' + $ver.Major"

Example when enabling Credential-less discovery:

"C:\\Windows\\Sysnative\\WindowsPowerShell\\v1.0\\powershell.exe\\" is not recognized as an internal or external command

### Release

All currently supported releases

### Cause

This error is due to a 64-bit host running a 32-bit MID JRE. Sysnative is a virtual Windows folder, a special alias, that can be used to access the 64-bit System32 folder from a 32-bit application or script.

To confirm the version a MID server is using:

1.  Navigate to the MID server list
2.  Add column "MID Java command directory" to see the location of the JRE being used
3.  On the MID server host navigate to the directory where the JRE is
4.  Run command "java -version"
5.  Example of 64-bit JRE:
    
    openjdk version "1.8.0\_181-sncmid1"  
    OpenJDK Runtime Environment (build 1.8.0\_181-sncmid1-b13)  
    OpenJDK 64-Bit Server VM (build 25.181-b13, mixed mode)
    
    Notice above the "64-bit" in the version.

### Resolution

Use OOB MID server JRE

1.  Stop the MID server service
2.  Move the current MID's JRE folder to another location
3.  In the instance, navigate to "MID Server > Downloads" and download the 64-bit MID package
4.  Move the new 64-bit JRE folder into the directory specified in "MID Java command directory" field of the MID server
5.  Restart the MID server service
6.  Navigate to the MID server record in the instance and wait for the MID server status to change to up
7.  Attempt to reproduce issue in order to confirm resolution
