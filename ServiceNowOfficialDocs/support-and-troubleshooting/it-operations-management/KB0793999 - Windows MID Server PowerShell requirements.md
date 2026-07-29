---
title: "Windows MID Server PowerShell requirements"
aliases:
  - KB0793999
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0793999
kb_number: KB0793999
last_modified: 2025-04-08
---

## Windows MID Server PowerShell requirements

  

## PowerShell requirements

Microsoft has deprecated PowerShell 2.0 and is discontinuing support for it. As a consequence, current Windows MID Servers require the minimum PowerShell version 3.0, and supports versions up to PowerShell 5.1. Versions prior to New York required the minimum PowerShell version 2.0. If you are upgrading to New York or Orlando, make sure PowerShell meets this new minimum requirement.  MID Servers with Windows 2008 Service Pack 2, Windows 2008R2 Service Pack 1, and every later version of Windows will have PowerShell 3.0 (or later) installed on it.

For more information from Microsoft on the PowerShell 2.0 deprecation, see [their blog post](https://devblogs.microsoft.com/powershell/windows-powershell-2-0-deprecation/ "their blog post").

Refer to [MID Server system requirements](https://docs.servicenow.com/bundle/orlando-servicenow-platform/page/product/mid-server/reference/r_MIDServerSystemRequirements.html "MID Server system requirements") for the latest system information.

## Check PowerShell version

There are two methods to check the PowerShell version of a MID Server.

You can find the PowerShell version using your instance with the following steps:

1.  Log into your ServiceNow instance.
    
2.  Go to **ecc\_agent\_list.do**.
    
3.  Using the Update Personalize List gear icon, add **Host PowerShell Version** to the Selected column.
    
4.  Sort the list of MID Servers by their PowerShell version to find outdated MID Servers.
    

You can also find the PowerShell version on the individual host machine with the following steps:

1.  Log into the host machine.
    
2.  Open the PowerShell console.
    
3.  Enter the command **$Host.Version**.
    
4.  The PowerShell version is listed as PSVersion.
    

## PowerShell for Discovery and Service Mapping

MID Servers use PowerShell and PowerShell Remoting for accessing configuration items (CIs) during horizontal and top-down discovery. PowerShell is used to control and automate the administration of Windows servers and applications.

MID Servers use PowerShell to directly communicate with Windows servers using both WMI and WinRM protocols. PowerShell is also the preferred method for performing discovery over multiple Windows domains. PowerShell allows a single MID Server to authenticate on servers on different domains using credentials stored on the instance.

For more information on PowerShell requirements for these applications, see [PowerShell for Discovery and Service Mapping](https://docs.servicenow.com/bundle/orlando-it-operations-management/page/product/discovery/reference/r_PowerShellForDiscovery.html "PowerShell for Discovery and Service Mapping").

### Additional Resources

[KB0791835](/kb_view.do?sysparm_article=KB0791835 "KB0791835") [WMI Collector deprecation details](/kb_view.do?sysparm_article=KB0791835)
