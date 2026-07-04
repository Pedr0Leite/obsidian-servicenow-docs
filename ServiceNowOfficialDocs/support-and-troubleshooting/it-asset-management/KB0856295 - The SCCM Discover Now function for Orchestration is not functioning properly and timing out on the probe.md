---
title: "The SCCM \"Discover Now\" function for Orchestration is not functioning properly and timing out on the probe"
aliases:
  - KB0856295
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0856295
kb_number: KB0856295
last_modified: 2024-04-08
---

## Issue

When we click on Discover Now from SCCM Server Instances module, the applications are not brought in and the payload shows timeout error.

Get applications: Terminated the probe because the max timeout was exceeded: 610 seconds. PowershellProcessRunner terminated due to interrupt java.lang.InterruptedException

  

## Resolution

Open the PowerShell console on the MID server and run the following commands. Please update the password, username and SCCM server FQDN as needed:  
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
\# Start a remote session with the remote SCCM server  
$secpasswd = ConvertTo-SecureString "YOUR\_PASSWORD" -AsPlainText –Force  
$mycreds = New-Object System.Management.Automation.PSCredential ("YOUR\_USERNAME", $secpasswd)  
$session = New-PSSession -ComputerName "YOUR\_SCCM\_SERVER" -Credential $mycreds -ConfigurationName Microsoft.PowerShell32  
Enter-PSSession $session  
  
\# CD into the CMSite directory  
Import-Module -Name "$(split-path $Env:SMS\_ADMIN\_UI\_PATH)\\ConfigurationManager.psd1"  
$PSD = Get-PSDrive -PSProvider CMSite  
CD "$($PSD):"  
  
\# At this point you can should be able to run SCCM cmdlets. For example, to get all SCCM applications:  
Get-CMApplication

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Record how much time it takes for the data to be returned by this call. 

In the probe windows - powershell add a probe parameter process\_timeout and set the value to the Time in seconds which was sufficient for the powershell activity to complete based on the time it took for provide the output of the cmdlet.
