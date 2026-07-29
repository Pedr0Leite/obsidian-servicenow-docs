---
title: "How to resolve Windows Server access denied errors during Discovery, Orchestration, or Integration Hub"
aliases:
  - KB0564283
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0564283
kb_number: KB0564283
last_modified: 2026-02-16
---

## How to resolve Windows Server access denied errors during Discovery, Orchestration, or Integration Hub

  

### Issue

Resolve the Windows Server error "Access is denied (Exception from HRESULT: 0x80070005 (E\_ACCESSDENIED))" that occurs when running a Discovery, Orchestration, or IntegrationHub step. This article provides common causes and resolutions for this error.

The following prerequisites must be met for PowerShell probes to run successfully:

-   The environment is configured to allow communication between the MID Server and the target server.
-   A credential with the necessary rights is configured for the target server.

It is often necessary to work with the Windows team managing the target server to resolve access issues.

### Release

All supported releases

### Cause

This error can result from one or more of the following conditions:

-   Incorrect credentials are configured for the target Windows Server.
-   The credential does not contain the domain name.
-   The credential does not have the required permissions.
-   Windows Management Instrumentation (WMI) is disabled or not configured properly on the target Windows Server.
-   WMI permissions are not configured correctly.
-   One or more WMI-related services are disabled.
-   The EnableDCOM registry entry (controls the global activation and call policies) is disabled on the MID Server or the target Windows Server.
-   The execution policy on the target server does not allow scripts to run.
-   The target server does not allow remote execution.

### Resolution

#### **Incorrect credentials configured for target Windows Server**

Verify that the user name and password for the Windows Server are correct:

1.  Log in to the target Windows Server using a remote desktop connection.
2.  If the connection fails, the credentials are incorrect. Obtain the correct credentials and configure them as described in the Service Mapping documentation.
3.  If the connection succeeds, continue with the following troubleshooting steps.

#### **The credential does not contain the domain name**

1.  Go to **MID Server** > **Credentials**.
2.  Select the Windows credential configured for the target Windows Server.
3.  Verify that the credential contains the domain name. The domain name appears before the user name and is separated with a backslash (\\).
4.  If the domain name is missing, add it to the credential. Use the domain name that allows access to the target Windows Server.

![Domain name part of user name](sys_attachment.do?sys_id=6ac470e297cfb298dfd73dae2153afdc "Domain name part of user name")

#### **Credential permissions**

For information on credential permissions, review the following documentation:

-   [Windows credentials](https://docs.servicenow.com/csh?topicname=r_WindowsCredentialsForm.html&version=latest)
-   [Windows probes and permissions](https://docs.servicenow.com/csh?topicname=r_DiscoWinProbesAndPermissions.html&version=latest)

#### **WMI is disabled or not configured properly on the target Windows Server**

Verify that WMI is enabled on the target Windows Server:

1.  On the Windows Server, go to **Start** \> **Run**.
2.  Enter **wbemtest**.
3.  Verify that the Windows Management Instrumentation Tester application starts. If it starts, WMI is enabled.
4.  In the Windows Management Instrumentation Tester window, select **Connect**.
5.  In the Connect window, leave the default values for **Namespace** and **Credentials**, then select **Connect.**
6.  Select **Query**.
7.  In the Query window, enter the following WMI query,  Select \* from Win32\_ComputerSystem 
8.  Select **Apply.**
9.  Verify that a reply with the computer name is returned.

#### **WMI permissions**

Verify that WMI permissions are configured correctly:

1.  In Windows Explorer, go to **Server Manager**.
2.  In the tree, select **Configuration**, right-click **WMI Control**, and select **Properties**.
3.  In the WMI Control Properties window, select **Security**.
4.  Select the **Root** folder, then select **Security**.
5.  In the Security for Root window, select **Advanced**.
6.  In the Advanced Security Settings for Root window, double-click **Administrators**.
7.  In the Permission Entry for Root window, verify that all checkboxes are selected.

  
![Example of window selections for WMI permissions and Permission Entry for Root window](/PermissionEntry.pngx)

#### **WMI-related services are disabled**

In Server Manager, go to Configuration > Services and verify that the following services are not disabled:

-   Remote Access Auto Connection Manager
-   Remote Access Connection Manager
-   Remote Procedure Call (RPC)
-   Remote Procedure Call (RPC) Locator
-   Remote Registry
-   Server
-   Windows Management Instrumentation
-   Windows Management Instrumentation Driver Extensions
-   WMI Performance Adapter

#### **EnableDCOM registry entry is disabled**

Verify that DCOM is enabled on both the MID Server and the target Windows Server:

1.  Open the registry on the MID Server.
2.  Verify the following registry entry:  
    Key: HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Ole  
    Name: EnableDCOM  
    Type: REG\_SZ  
    Data: Y 
3.  Repeat steps 1–2 on the target Windows Server.

#### **Execution policy does not allow scripts to run**

Verify that the execution policy allows scripts to run. See the following documentation for requirements:

-   [PowerShell for Discovery and Service Mapping](https://docs.servicenow.com/csh?topicname=r_PowerShellForDiscovery.html&version=latest "PowerShell for Discovery and Service Mapping")

The following Microsoft documentation describes how to check and set the execution policy:

-   [Get-ExecutionPolicy](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/get-executionpolicy?view=powershell-7.2 "Get-ExecutionPolicy")
-   [Set-ExecutionPolicy](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-7.2 "Set-ExecutionPolicy")

#### **Target server does not allow remote execution**

Enable remote execution on the target server. See the following Microsoft documentation:

-   [Enable-PSRemoting](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/enable-psremoting?view=powershell-7.2 "Enable-PSRemoting")
