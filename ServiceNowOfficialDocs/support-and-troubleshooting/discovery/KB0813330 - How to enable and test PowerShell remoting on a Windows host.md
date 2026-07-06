---
title: "How to enable and test PowerShell remoting on a Windows host"
aliases:
  - KB0813330
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813330
kb_number: KB0813330
last_modified: 2025-12-22
---

## How to enable and test PowerShell remoting on a Windows host

  

### Issue

Resolve Windows Discovery errors that occur when PowerShell remoting is not enabled on target hosts. Windows discovery uses PowerShell remoting to run scripts on target devices. If PowerShell remoting is not enabled, you may see errors such as:

"Failed to launch process powershell -ExecutionPolicy ByPass -NonInteractive -WindowStyle Hidden -command"

### Release

Beginning with the Madrid release

### Resolution

#### **Enable PowerShell remoting**

To enable a remote connection on your server:

1.  Open PowerShell, and select **Run as administrator**.  
      
       ![](/sys_attachment.do?sys_id=a3e9631893caf2908960fb2d6cba10a6)
    
2.  In the PowerShell window, type the cmdlet:   
    Enable-PSRemoting -Force.
3.  Select **Enter**.

![](/sys_attachment.do?sys_id=abe9631893caf2908960fb2d6cba10f1)

This command starts the WinRM service, sets it to start automatically with your system, and creates a firewall rule that allows incoming connections. The \-Force parameter tells PowerShell to perform these actions without prompting you for each step.

#### **Add a remote-connected host host to the trusted hosts list** 

1.  Open PowerShell and select **Run as administrator**.
2.  In the PowerShell window, type the following cmdlet:  
    Set-Item wsman:\\localhost\\client\\trustedhosts \*

The asterisk is a wildcard symbol for all hosts. To restrict which servers can connect, replace the asterisk with a comma-separated list of IP addresses or hostnames. 

#### **Restart the WinRM service**

1.  In the PowerShell window, type the following cmdlet:  
    Restart-Service WinRM
2.  Select **Enter**.

![](/sys_attachment.do?sys_id=a7e9631893caf2908960fb2d6cba10ed)

#### **Test the connection**

1.  From the MID Server, open PowerShell and run the following cmdlet:  
    Test-WsMan <Target IP> 
2.  Select **Enter**.

This command tests whether the WinRM service is running on the remote host.

-   If it completes successfully, information about the remote host WinRM service displays. This indicates that WinRM is enabled and your target host can communicate.
-   If the command fails, an error message displays instead.

![](/sys_attachment.do?sys_id=bfe9a31893caf2908960fb2d6cba102b)

#### **Run a single remote command on the remote system**

Use the Invoke-Command cmdlet as follows: 

Invoke-Command -ComputerName COMPUTER -ScriptBlock { COMMAND } -credential USERNAME.

**Example**

The following command displays the contents of the C:\\ directory on a remote host with the specified IP address and user name:

Invoke-Command -ComputerName <TargetIP> -ScriptBlock { Get-ChildItem C:\\ } -credential domain\\username

![](/sys_attachment.do?sys_id=b3e9a31893caf2908960fb2d6cba1030)

#### **Run multiple cmdlets on the remote host**

Instead of repeating the Invoke-Command cmdlet and the remote IP address, start a remote session:

1.  Type the following cmdlet:   
    Enter-PSSession -ComputerName <Target IP> -Credential Domain\\USER
2.  Select **Enter**.

![](/sys_attachment.do?sys_id=abe9a31893caf2908960fb2d6cba1027)

### Related Links

[PowerShell remoting for Discovery](https://docs.servicenow.com/csh?topicname=powershell-remoting.html&version=latest "PowerShell remoting for Discovery")

[MID Server PowerShell files](https://docs.servicenow.com/csh?topicname=mid-server-powershell-files.html&version=latest "MID Server PowerShell files")
