---
title: "How to troubleshoot WMI and PowerShell issues on a remote machine for Windows Discovery"
aliases:
  - KB0549830
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0549830
kb_number: KB0549830
last_modified: 2026-05-22
---

## How to troubleshoot WMI and PowerShell issues on a remote machine for Windows Discovery

  

### Issue

Troubleshoot WMI and PowerShell issues on a remote machine that may cause Windows Discovery to fail. This article provides steps to verify firewall settings, credentials, WMI configuration, remote PowerShell, and WMI permissions on the target machine.  
  

### Release

All supported releases

### Resolution

Discovery may fail to discover a remote machine due to a configuration issue on the target machine. Follow these steps to troubleshoot.

**Note**: Some of these steps take an aggressive approach but in most cases resolve the issue. Test these steps in a non-production environment first.

#### **Step 1: Check for issues caused by Windows Firewall or RPC/DCOM**

1.  Try disabling Windows Firewall to isolate the issue.
2.  If disabling the firewall resolves the issue, follow the steps in [Opening ports in Windows Firewall for remote server access](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0549828) to configure the firewall correctly.

#### **Step 2: Verify that the MID Server credential can log in to the remote machine**

From a computer other than the MID Server, try to connect to the remote machine using the user account configured in the credential.

#### **Step 3: Verify that WMI is correctly configured on the remote machine**

1.  Verify that the WinRM service is running.
2.  Open a command prompt as an administrator and run the following command: winrm quickconfig 
3.  Open a PowerShell session as an administrator and run the following command: Enable-PSRemoting -Force 

#### **Step 4: Enable and configure remote PowerShell on the remote machine**

1.  Right-click the PowerShell icon and select **Run as administrator**.
2.  Check the current script execution policy by running the following command: Get-ExecutionPolicy PowerShell returns a value of Restricted.
3.  Change the script execution policy by running the following command: Set-ExecutionPolicy unrestricted 
4.  Verify that the policy has changed by running Get-ExecutionPolicy again. PowerShell should return a value of Unrestricted. You should now be able to run PowerShell scripts.

#### **Step 5: Grant WMI access for the MID Server user on the remote machine**

1.  Go to **Server Manager (mmc.exe)** > **Configuration** \> **WMI Control** > **Properties**.
2.  Go to **Root** \> **Security** \> **Add**.
3.  Enter the MID Server account and enable account and remote call permissions.

#### **Step 6: Check for Windows Server 2003**

If the remote machine runs Windows Server 2003, the MID Server account may need to be in the local Administrators group of the remote machine.

#### **Step 7: Check domain trust in multi-domain environments**

In a multi-domain environment, a domain trust may be required for a credential to successfully use WMI to discover devices that belong to a different domain.

#### **Step 8: Verify WMI connectivity**

Use the PowerShell cmdlets Get-WmiObject or Get-CimInstance to verify WMI connectivity:

Get-WmiObject -Class Win32\_OperatingSystem -ComputerName <RemoteComputerNameOrIP>  
  
Get-CimInstance -ClassName Win32\_OperatingSystem -ComputerName <RemoteComputerNameOrIP>
