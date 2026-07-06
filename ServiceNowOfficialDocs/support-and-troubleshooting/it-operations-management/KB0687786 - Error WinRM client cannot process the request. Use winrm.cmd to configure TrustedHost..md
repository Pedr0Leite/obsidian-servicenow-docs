---
title: "Error WinRM client cannot process the request. Use winrm.cmd to configure TrustedHost."
aliases:
  - KB0687786
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0687786
kb_number: KB0687786
last_modified: 2025-11-04
---

## Error WinRM client cannot process the request. Use winrm.cmd to configure TrustedHost.

  

### Issue

One of the following errors is returned:

Winrs error:The WinRM client cannot process the request. Default authentication may be used with an IP address under the following conditions: the transport is HTTPS or the destination is in the TrustedHosts list, and explicit credentials are provided. Use winrm.cmd to configure TrustedHosts. Note that computers in the TrustedHosts list might not be authenticated. For more information on how to set TrustedHosts run the following command: winrm help config

The WinRM client cannot process the request. If the authentication scheme is different from Kerberos, or if the client computer is not joined to a domain, then HTTPS transport must be used or the destination machine must be added to the TrustedHosts configuration setting. Use winrm.cmd to configure TrustedHosts. Note that computers in the TrustedHosts list might not be authenticated. You can get more information about that by running the following command: winrm help config. For more information, see the about\_Remote\_Troubleshooting Help topic.

### Release

All currently supported releases.

### Cause

-   WinRM HTTP communication via IP
-   The source server(the MID server) is not on the same domain as that of the target server

### Resolution

Add the target IP address to the TrustedHosts list. Run the following command on the Windows command line to add all servers to the TrustedHosts list:

winrm s winrm/config/client @{TrustedHosts="\*"}

**Note:** The command above may fail if run on Powershell and may need to be executed via Windows cmd prompt

Or, run the following command to set a specific IP address:

winrm set winrm/config/client '@{TrustedHosts="IP\_ADDRESS"}'

Run the following command to confirm what computers are in the TrustedHosts list:

Get-Item WSMan:\\localhost\\Client\\TrustedHosts

More information on options to update the TrustedHosts can be found on:

-   [Microsoft Docs: How to add a computer to the trusted hosts list](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_remote_troubleshooting?view=powershell-7.2#how-to-add-a-computer-to-the-trusted-hosts-list "Microsoft Docs: How to add a computer to the trusted hosts list")
