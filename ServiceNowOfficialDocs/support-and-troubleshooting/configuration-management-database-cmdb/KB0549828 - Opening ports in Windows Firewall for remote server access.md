---
title: "Opening ports in Windows Firewall for remote server access"
aliases:
  - KB0549828
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0549828
kb_number: KB0549828
last_modified: 2026-05-26
---

## Opening ports in Windows Firewall for remote server access

  

### Issue

This article explains how to configure Windows Firewall to allow access to remote servers using Windows Management Instrumentation (WMI) and PowerShell. 

### Release

All releases

### Resolution

#### Windows Firewall and DCOM ports

When accessing a remote Windows server with Windows Firewall enabled, simply opening port 135 might not be enough for successful discovery. The MID Server connects to the remote server's RPC (Remote Procedure Call) endpoint on port 135. The RPC service then dynamically assigns a port for DCOM (Distributed Component Object Model) communication. The MID Server needs to use this DCOM port to communicate further with the remote server.

The range of ports used for DCOM communication depends on the Windows version:

-   Windows 2000, Windows XP, and Windows Server 2003: Ports 1025 to 5000
-   Windows Server 2008 and later, Windows Vista and later: Ports 49152 to 65535

If these DCOM ports are blocked by Windows Firewall, discovery fails. The WMIRunner - WMI: Classify probe will return an error similar to this: 

<error>
Authentication failure with the local MID server service credential.
</error>
<error>
  Failed to access target system.  Please check credentials and firewall settings on the target system to ensure accessibility: Access is denied. (Exception from HRESULT: 0x80070005 (E\_ACCESSDENIED))  
   Stack Trace:  
      at System.Runtime.InteropServices.Marshal.ThrowExceptionForHRInternal(Int32 errorCode, IntPtr errorInfo)  
      at System.Management.ManagementScope.InitializeGuts(Object o)  
      at System.Management.ManagementScope.Initialize()  
      at System.Management.ManagementObjectSearcher.Initialize()  
      at System.Management.ManagementObjectSearcher.Get()  
      at Microsoft.PowerShell.Commands.GetWmiObjectCommand.BeginProcessing()  
      at System.Management.Automation.Cmdlet.DoBeginProcessing()  
      at System.Management.Automation.CommandProcessorBase.DoBegin()
</error>

#### How to open ports to the MID Server

Verify that the MID Server application host machine has access to the targets on all ports. This is necessary because of the unique nature of the WMI requirements. For more information, see [MID Server Requirements.](https://docs.servicenow.com/csh?version=latest&topicname=r_MIDServerSystemRequirements.html "MID Server Requirements")

If opening all ports is not feasible, follow these steps: 

#### 1 - Open port 135 on the Windows Firewall

For Windows 2000, XP, Server 2003

This solution adds an exception to Windows Firewall. 

1.  Go to **Control Panel** > **Windows Firewall** > **Exceptions** \> **Add Port**...
2.  Name: **RPC Endpoint Mapper - TCP Port 135**
3.  Port: **135**
4.  Protocol: **TCP**

For Windows Server 2008, Vista, and later

This solution adds a rule to Windows Firewall with Advanced Security to open the port 135/RPC. 

1.  Go to **Administrative Tools** > **Windows Firewall with Advanced Security**.
2.  Go to **Inbound Rules** (right-click) > **New Rule**...
3.  \[Rule Type\]: Select **Custom,** and then select **Next**.
4.  \[Program\]: Select **All programs**.
5.  \[Program\]: Under Services:  
    -   Select **Customize**.
    -   Select **Apply to this service: Remote Procedure Call (RPC) - RpcSs**
    -   Select **OK** to close the dialog box.
    -   Select **Next**.
6.  \[Protocol and Ports\]: Select Protocol type: **TCP**.
7.  \[Protocol and Ports\]: Select Local port: RPC **Endpoint Mapper**.
8.  \[Protocol and Ports\]: Keep Report port: **All Ports**, and select **Next**.
9.  \[Scope\]: Keep Which local/remote IP addresses does this rule match: Any IP address (you might need to set it different for your security policy), and select **Next**.
10.  \[Action\]: Select **Allow the connection**.
11.  \[Profile\]: Select Domain, Private, and Public (you might need to set it different for your security policy), and select **Next**.
12.  \[Name\]: Name the rule. For example, RPC Endpoint Mapper - TCP Port 135
13.  Select **Finish**.

Other predefined rules may already allow access to 135/RPC, such as the rule _File and Printer Sharing - RPC-EPMAP_.  
  

#### 2 – Open access to standard DCOM ports

For Windows 2000, XP, Server 2003:

This solution adds exceptions to Windows Firewall. Because there are many exceptions to add, run this script to add the entries for you. 

1.  Ensure that port 135 is open (see the previous section).
2.  Open a command line and enter:
    
    FOR /L %I in (1025,1,5000) do netsh firewall add portopening TCP %I "Dcom - TCP Port "%I
    
    This adds an entry per port to the Windows Firewall (3975 entries). If you find that there are too many entries, follow the steps in section 3 to have DCOM use only a few ports.

For Windows Server 2008, Vista, and later:

There are a couple of ways to achieve this:

-   Use the command from the previous section, substituting the port range for Windows 2008
-   Substitute(1025,1,5000) in the command with (49152,1,65535). This adds an entry per port to the Windows Firewall (16383 entries). If you find that there are too many entries, follow the next steps in section 3 to have DCOM use only a few ports.
-   Add rules to Windows Firewall with Advanced Security from section 1.   
      
    1.  Make sure that port 135 is open (see section 1).
    2.  Go to **Administrative Tools** > **Windows Firewall with Advanced Security**.
    3.  Go to **Inbound Rules** (right-click) > **New Rule**...
    4.  \[Rule Type\]: Select **Custom**, and select **Next**.
    5.  \[Program\]: Select **All programs**.
    6.  \[Program\]: Under Services:  
        -   Select **Customize**...
        -   Select **Apply to all programs and services**.
        -   Select **OK** to close the dialog box.
        -   Select **Next**.
    7.  \[Protocol and Ports\]: Select Protocol type: **TCP**.
    8.  \[Protocol and Ports\]: Select Local port: **Dynamic RPC**.
    9.  \[Protocol and Ports\]: Keep Report port: **All Ports**, and select **Next**.
    10.  \[Scope\]: Keep Which local/remote IP addresses does this rule match: **Any IP address** (you might need to set it differently for your security policy), and click Next.
    11.  \[Action\]: Select **Allow the connection**.
    12.  \[Profile\]: Select Domain, Private, and Public (you might need to set it differently for your security policy), and select **Next**.
    13.  \[Name\]: Name the rule (for example, DCOM - TCP Dynamic RPC), and select **Finish**.  
           
         

#### 3 – Configure DCOM to Use a Limited Range of Ports (Optional)

Configure DCOM by adding 100 ports: 65000 – 65100:

1.  Go to **Administrative Tools** > **Component Services**.
2.  Go to **Console Root** > **Component Services** > **Computers** \> **My Computer** (right click) > **Default Protocols** > "**Connection-oriented TCP/IP**" > **Properties**...
3.  Add Port range: **65000-65100**.
4.  Restart the server.
5.  Follow the steps in section 2. For Windows 2000, XP, Server 2003 substitute (1025,1,5000) in the command by (65000,1,65100). This adds 100 entries to the Windows Firewall.

**Note**: This is a really low value and would result in Discovery (and other remote applications) running too slow.

### Related Links

[Windows Discovery – Troubleshooting WMI/Powershell issues on the remote machine](/kb_view.do?sysparm_article=KB0549830 "Windows Discovery - Troubleshooting WMI/Powershell issues on the remote machine")
