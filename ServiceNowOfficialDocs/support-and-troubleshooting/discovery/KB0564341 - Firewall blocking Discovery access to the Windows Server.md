---
title: "Firewall blocking Discovery access to the Windows Server"
aliases:
  - KB0564341
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0564341
kb_number: KB0564341
last_modified: 2023-12-07
---

## Firewall blocking Discovery access to the Windows Server

  

### Issue

This article provides info about ways to resolve various issues that result in firewalls blocking Discovery access to Windows servers.

### Table of Contents

-   [Service Mapping does not listen on all relevant ports](#mcetoc_1fti0tpcbc)
-   [Access to a Windows Server is denied](#mcetoc_1fti0tpcbd)
-   [Service Mapping fails to run commands](#mcetoc_1fti0tpcbe)

### Firewall blocking Discovery access to the Windows Server

#### **Problem**

A firewall blocks Remote Procedure Call (RPC) calls from the MID Server to the Microsoft Windows Server preventing the discovery process. The problem can be caused either by Windows Firewall (embedded) or an external firewall.

#### **Symptoms**

At the end of the discovery and mapping process, Service Mapping displays the following error for a Windows Server: “0x800706BA - RPC Server Unavailable”.

#### **Cause**

The firewall is not configured correctly to let through RPC calls from the MID Server. Typically, RPC uses a large range of ports. The MID Server initiates the RPC connection on port 135, but once the connection is established, it uses any port in the range of 1024 and up.

#### **Resolution**

Perform the following steps to verify that the firewall blocks RPC calls:

1.  On the MID Server, run the following command:  
    
    wmic /NODE:target\_server\_ip\_address /user:domain\\user /password:xxxx cpu get
    
2.  Check the result. If you get the message that the RPC Server is unavailable, it means that the firewall between the MID Server and the Windows Server is blocking the connection. If you do not get an error message, carry on with the next step.
3.  If the Windows Server has embedded Windows Firewall, disable it temporarily and run the same command from the MID Server:  
    
    wmic /NODE:target\_server\_ip\_address /user:domain\\user /password:xxxx cpu get
    
4.  If you get the success message, you must configure the embedded Windows Firewall to let through RPC calls from the MID Server.
    
5.  If this private network uses an external firewall, contact your network administrator for assistance.

### Service Mapping does not listen on all relevant ports

#### **Problem**

Service Mapping does not listen on all relevant ports of the Windows Server it tries to discover and map.

#### **Symptoms**

At the end of the discovery and mapping process, Service Mapping displays the following error for a Windows Server: “0x800706BA - RPC Server Unavailable”.

#### **Cause**

The Windows Server has multiple IP addresses. Service Mapping automatically discovered only one of the IP addresses and therefore is not listening on the full range of ports. Typically, Service Mapping discovers and listens only to the application port.

#### **Resolution**

Perform the following steps:

1.  On the map, right-click on the discovery error message and select **Add Management IP**.
2.  Select one of the IP addresses of this Windows Server.
3.  Verify that the discovery and mapping process is completed without errors.

### Access to a Windows Server is denied

#### **Problem**

Service Mapping cannot access a Windows Server.

#### **Symptoms**

At the end of the discovery and mapping process, Service Mapping displays the following error for a Windows Server: “0x80070005 – E\_ACCESS\_DENIED”.

#### **Possible Cause**

Credentials configured for this Windows Server in the ServiceNow platform are wrong.

#### **Resolution**

Verify that the user name and password for the Windows Server are correct:

1.  Log in to the Windows Server that you must discover using remote desktop connection.
2.  If you fail to connect, the username and password for this Windows Server are wrong. Find out the correct credentials and configure them as described in the Service Mapping documentation. If you connect successfully, continue with this troubleshooting procedure.

#### **Possible Cause**

Access denied errors are displayed if a user is not part of the local administrators group.

#### **Resolution**

Verify that this user is added to the local administrators group.

#### **Possible Cause**

The EnableDCOM registry entry that controls the global activation and call policies is disabled either on the MID Server or on the Windows Server.

#### **Resolution**

Perform the following steps both on the MID Server and on the Windows Server to verify that DCOM is enabled on both servers:

1.  Navigate to the registry.
2.  Check the following registry entry on both computers:  
    Key: HKEY LOCAL MACHINE\\Software\\Microsoft\\Ole  
    Name: EnableDCOM  
    Type: REG\_SZ  
    Data: Y

#### **Possible Cause**

WMI is disabled or not configured properly on this Windows Server.

#### **Resolution**

Check that Windows Management Instrumentation (WMI) is enabled by performing the following steps:

1.  On the Windows Server, navigate to **Start > Run**.
2.  Enter wbemtest.
3.  Check that the Windows Management Instrumentation Tester application starts. If it does, WMI is enabled.
4.  In the Windows Management Instrumentation Tester window, click **Connect**.
5.  In the Connect window, leave the default values for **Namespace** and **Credentials** and click C**onnect**.
6.  Click **Query**.
7.  In the Query window, enter the following WMI query: Select \* from Win32\_ComputerSystem and click **Apply**.
8.  Verify that you get a reply with the computer name.

#### **Possible Cause**

WMI-related service or services are disabled.

#### **Resolution**

Ensure that all WMI-related services can be started on demand:

1.  In Windows Explorer, navigate to **Server Manager**.
2.  In the tree, select **Configuration,** and right-click **WMI Control** and select **Properties**.
3.  In the **WMI Control Properties** window**,** click the **Security**
4.  Click the **Root** folder and click **Security**.
5.  In the **Security for Root** window, click **Advanced**.
6.  In the **Advanced Security Settings for Root** window, > double-click **Administrators**
7.  In the **Permission Entry for Root** window, verify that all checkboxes are selected.  
      
    ![Permission Entry for Root](sys_attachment.do?sys_id=3f422a9847437118d1a5ab29736d43f2 "The Permission Entry for Root window displays all checkboxes in the Allow column as checked.")
8.  In the **Server Manager**, select **Configuration > Services** and verify that the status for the following services is not disabled:  
    -   Remote Access Auto Connection Manager
    -   Remote Access Connection Manager
    -   Remote Procedure Call (RPC)
    -   Remote Procedure Call (RPC) Locator
    -   Remote Registry
    -   Server
    -   Windows Management Instrumentation
    -   Windows Management Instrumentation Driver Extensions
    -   WMI Performance Adapter

### Service Mapping fails to run commands

#### **Problem**

In some cases, Service Mapping may be able to connect to WMI but fails to run all or specific commands, such as netstat.

#### **Possible Cause**

The Administrators group on the Windows Server has reduced DCOM rights compared to the default Windows installation.

#### **Resolution**

Perform the following steps:

1.  In the command-line shell, enter exe.
2.  In the Component Services window, navigate to **Component Services > Computers**.
3.  Right-click on **My Computer** and select **Properties**.
4.  Click the **COM Security**
5.  Click **Edit Limits**.
6.  In the Access Permission window, click **Add**.
7.  In the Select Users or Groups window, enter Distributed COM Users and click **OK**.
8.  In the Access Permission window, select **Distributed COM Users** and verify that the following permissions are allowed:  
    
    -   Local Launch
    -   Remote Launch
    -   Local Activation
    -   Remote Activation
    
    ![Launch and Activation Permission](sys_attachment.do?sys_id=b742e69847437118d1a5ab29736d43e6 "The Launch and Activation Permission window displays all checkboxes for Local Launch, Remote Launch, Local Activation, and Remote activation as checked.")

#### **Possible Cause**

Appropriate security policies are not configured correctly for the Service Mapping user or the group to which this user belongs.

#### **Resolution**

Perform the following steps:

On the Windows Server that you discover, click **Start > Run** and enter secpol.msc.

2.  In the Local Security Policy window, navigate to **Security Settings > Local Policies > User Rights Assignment**.
3.  Right-click **My computer** and select **Properties**.
4.  Right-click relevant policies and check the Service Mapping user configured for them. If necessary, click **Add User or Group** and add the Service Mapping user to this policy. Perform this for the following policies:  
    
    -   Debug Programs
    -   Restore Files and Directories
    -   Logon as batch job
    -   Logon as service
    
    ![Debug programs Properties](sys_attachment.do?sys_id=6742e69847437118d1a5ab29736d43dd "The Debug programs Properties window is displayed and the Local Security Setting tab is open.")
