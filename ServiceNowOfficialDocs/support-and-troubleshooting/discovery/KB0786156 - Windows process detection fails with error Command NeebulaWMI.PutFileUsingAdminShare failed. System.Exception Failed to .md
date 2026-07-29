---
title: "Windows process detection fails with error \"Command NeebulaWMI.PutFileUsingAdminShare failed. System.Exception: Failed to create connection. Unable to connect to.\"
aliases:
  - KB0786156
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0786156
kb_number: KB0786156
last_modified: 2024-04-08
---

## Windows process detection fails with error "Command NeebulaWMI.PutFileUsingAdminShare failed. System.Exception: Failed to create connection. Unable to connect to."

  

### Issue

Windows process detection fails with error:

Put file on Windows host <ip\_address> failed. filePath: 64/msvcp100.dll error: Unable to execute command. None of the command implementations was successful.  
Command NeebulaWMI.PutFileUsingAdminShare failed. System.Exception: Failed to create connection. Unable to connect to \\\\<ip\_address>\\c$. Error=53

### Release

All currently supported releases.

### Cause

The process detection in windows discovery, depending on settings, will use the WMI collector. The WMI collector will attempt to collect the results from either the C$ or via sending the result file back to the MID server via HTTP.

### Resolution

If WinRM is available on the target, set the following MID Server properties:

-   mid.sa.use\_powershell = true
-   mid.sa.prefer\_powershell = true
-   mid.sa.prefer\_powershell\_fallback = true

  
If both mid.sa.use\_powershell and mid.sa.prefer\_powershell are true, WMIProvider will try Powershell first. If powershell command returns nothing it will try to fall back to WMI Collector, if mid.sa.prefer\_powershell\_fallback is true. When it tries Powershell it will check if WinRM is available on the target and run the command via Powershell remoting. If WinRM is not availble, it will try WMI and will still need the admin share to copy the script to run on the target. Thus, WinRM needs to be setup in order to use Powershell without the admin share.

### Related Links

-   [Setup a MID Server to use Powershell](https://docs.servicenow.com/csh?topicname=r_PowerShellForDiscovery.html&version=latest#t_SetUpAMIDServerToUsePowerShell "Setup a MID Server to use Powershell")
