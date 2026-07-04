---
title: "How to troubleshoot MID Server WMI and PowerShell credential issues for Windows Discovery"
aliases:
  - KB0549834
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0549834
kb_number: KB0549834
last_modified: 2026-05-22
---

## How to troubleshoot MID Server WMI and PowerShell credential issues for Windows Discovery

  

### Issue

Troubleshoot credential failures in Discovery Logs that occur after running a Discovery Schedule for Windows machines. In some cases, the Discovery Logs indicate a credential failure but the actual cause is external to the MID Server. This article explains how Windows probes use credentials and provides troubleshooting steps for common WMI and PowerShell errors.

### Facts

#### **Credentials**

To discover target Windows machines, add Windows credentials to the Credentials table. Credential records specify a user name, a password, a credential type (Windows, SSH, SNMP), and the MID Servers allowed to use the credential.

When the MID Server starts or when a credential is modified, the MID Server downloads and caches all available credentials.

#### **MID Server configuration parameters**

The three main configuration parameters covered in this article are:

-   **mid.use\_powershell**—When set to true, the MID Server retrieves WMI and Windows registry values using the PowerShell probe. 
-   **mid.powershell.use\_credentials**—Enables the PowerShell probe to use credentials defined in the Credentials table. 
-   **mid.powershell.local\_mid\_service\_credential\_fallback**—Enables the PowerShell probe to use the local MID account as a last resort. 

Beginning with the Fuji release, these parameters are **true** by default.

#### **Running Windows probes**

Many Windows probes retrieve WMI and Windows registry values from the target machine. There are two methods, depending on the value of the **mid.use\_powershell** configuration parameter.

#### **Running the WMIRunner probe**

This probe cannot use the credentials defined in **Discovery > Credentials**. The MID Server connects to the WMI providers using the account that the MID Server service runs with, referred to as the local MID account. This account could be a domain user account. The local MID account must have access to the remote machines for the WMIRunner probe to work.

#### **Running the PowerShell probe**

This probe can use the credentials defined in **Discovery > Credentials**. The MID Server uses the PowerShell API to retrieve WMI values. If the MID Server is configured to run PowerShell probes using credentials (see the MID Server configuration parameters section), it attempts to connect to the target machine using the first defined credential. If that credential fails, the next credential is attempted. 

If all credentials fail and the MID Server is configured to use the local MID account as a last resort, the MID Server attempts to connect with the account the MID Server service runs with.

#### **Simulating a simple probe**

1.  Go to **System Maintenance** > **Scripts - Background**.
2.  Run the following script, replacing the mid\_server and target\_host variables with the name of your MID Server and the IP address of the target Windows machine:

**var** mid\_server  = 'MID\_SERVER\_1';
**var** target\_host = '192.168.200.14';
**var** debug = **true**;

sendProbeWmiRunner(mid\_server, target\_host);

**function** sendProbeWmiRunner(mid, host) {
	**var** ecc = **new** GlideRecord('ecc\_queue');
	ecc.initialize();
	ecc.agent = 'mid.server.' + mid;
	ecc.topic = 'WMIRunner';
	ecc.name = 'TestWMI';
	ecc.source = host;
	ecc.queue = 'output';
	ecc.payload = '<parameters><parameter name="WMI\_FetchData" value="Win32\_BIOS.SerialNumber"/><parameter name="port" value="135"/><parameter name="debug" value="' + debug + '"/><parameter name="skip\_sensor" value="true"/></parameters>';
	ecc.insert();
}

The script sends a WMIRunner probe to the MID Server that retrieves the serial number from the target machine. If mid.use\_powershell is true, the MID Server switches the WMIRunner probe internally to PowerShell.

### Release

All supported releases

### Resolution

### Troubleshooting Windows probes

If errors appear in the Discovery Logs after running WMI or PowerShell probes, check the MID Server configuration parameter mid.use\_powershell:

-   If mid.use\_powershell is false, see the Troubleshooting WMIRunner probes section.
-   If mid.use\_powershell is true, see the Troubleshooting PowerShell probes section.

### Troubleshooting WMIRunner probes - mid.use\_powershell:false

1.  Send the probe (see the Simulating a simple probe section).
2.  Go to **Discovery** > **ECC Queue** and sort the list by **Created** from newest to oldest. Locate the output message with topic "WMIRunner" and name "TestWMI."
3.  Wait a few seconds for the MID Server to process the probe.
4.  Refresh the list until the response ECC message appears.
5.  Open the message and review the contents of Payload. Select the XML button to view the formatted payload.
6.  Review the message within the result tag.

When the probe succeeds, the result is similar to the following:

**<Win32\_BIOS>**
	**<SerialNumber>**
		VMware-56 4d 41 9f 34 6e 0c 3d-1b be f1 3c f7 2c ad 7b
	**</SerialNumber>**
**</Win32\_BIOS>**

When the credential is incorrect, the result is similar to the following:

**<error>**
	Connection failed to WMI service. Error: Permission denied
**</error>**
**<error>**
	Thu May 28 16:24:21 2015 DEBUG: Testing WMI connection to 192.168.200.14
	Thu May 28 16:25:03 2015 DEBUG: Appending element: error
	Thu May 28 16:25:03 2015 DEBUG: getValueText()
	Thu May 28 16:25:03 2015 DEBUG: valueType: string
	Thu May 28 16:25:03 2015 DEBUG: Appended: error; Connection failed to WMI service. Error: Permission denied
	Thu May 28 16:25:03 2015 DEBUG: WMI not running
**</error>**

This error indicates that the account the MID Server service runs with is not a valid credential for the WMI API to connect to the target machine.

#### **Solution**

There are two options:

-   Set mid.use\_powershell to true. This is the preferred option.
-   Set the account the MID Server service runs with (Windows service) to have the correct permissions to access the remote machine. 

### Troubleshooting PowerShell probes - mid.use\_powershell:true

1.  Send the probe (see the Simulating a simple probe section).
2.  Go to **Discovery** \> **ECC Queue** and sort the list by **Created** from newest to oldest. Locate the output message with topic "WMIRunner" and name "TestWMI."
3.  Wait a few seconds for the MID Server to process the probe.
4.  Refresh the list until the response ECC message appears.
5.  Open the message and review the contents of Payload. Select the XML button to view the formatted payload.
6.  Review the message within the result tag.

When the probe succeeds, the result is similar to the following:

**<Win32\_BIOS>**
	**<SerialNumber>**
		VMware-56 4d 41 9f 34 6e 0c 3d-1b be f1 3c f7 2c ad 7b
	**</SerialNumber>**
**</Win32\_BIOS>**

The following sections describe the most common errors.

#### **The RPC server is unavailable**

When mid.powershell.local\_mid\_service\_credential\_fallback is true, the error appears as:

**<error>**
	Authentication failure with the local MID server service credential.
**</error>**
**<error>**
	Failed to access target system. Please check credentials and firewall settings on the target system to ensure accessibility: The RPC server is unavailable. (Exception from HRESULT: 0x800706BA)
	Stack Trace:    at System.Runtime.InteropServices.Marshal.ThrowExceptionForHRInternal(Int32 errorCode, IntPtr errorInfo)
	  at System.Management.ManagementScope.InitializeGuts(Object o)
	  at System.Management.ManagementScope.Initialize()
	  at System.Management.ManagementObjectSearcher.Initialize()
	  at System.Management.ManagementObjectSearcher.Get()
	  at Microsoft.PowerShell.Commands.GetWmiObjectCommand.BeginProcessing()
**</error>**

When mid.powershell.local\_mid\_service\_credential\_fallback is false, the error appears as:

**<error>**
	Failure(s) with available Windows credentials from the instance. Credentials tried: LOCALDOMAIN\\mid,autolab1\\autouser
**</error>**
**<error>**
	The RPC server is unavailable. (Exception from HRESULT: 0x800706BA)
	Stack Trace:    at System.Runtime.InteropServices.Marshal.ThrowExceptionForHRInternal(Int32 errorCode, IntPtr errorInfo)
	  at System.Management.ManagementScope.InitializeGuts(Object o)
	  at System.Management.ManagementScope.Initialize()
	  at System.Management.ManagementObjectSearcher.Initialize()
	  at System.Management.ManagementObjectSearcher.Get()
	  at Microsoft.PowerShell.Commands.GetWmiObjectCommand.BeginProcessing()
**</error>**

This error can be misleading. In most cases, it is not an authentication failure caused by an incorrect credential.

In the MID Server logs with debug enabled:

-   The MID Server first tries the credentials from the Credentials table. These fail with exit code 2 (when mid.powershell.use\_credentials is true).
-   Then it tries the account the MID Server service runs with. This fails with exit code 3 (when mid.powershell.local\_mid\_service\_credential\_fallback is true).
-   In all cases, the error indicates that the RPC server is unavailable (Exception from HRESULT: 0x800706BA).

The MID Server returns the error details from the last credential attempted. This indicates that the MID Server cannot access the remote machine using RPC, typically caused by a Windows firewall on the remote machine blocking RPC requests.

#### **Troubleshooting**

Run a PowerShell WMI query directly from the MID Server to the remote machine. Open a PowerShell command line and run the following, replacing LOCALDOMAIN\\mid with the credential to test:

gwmi win32\_operatingsystem -computer 192.168.200.14 -credential 'LOCALDOMAIN\\mid'

The expected result is similar to:

SystemDirectory : C:\\Windows\\system32
Organization    :
BuildNumber     : 6001
RegisteredUser  : Windows User
SerialNumber    : 12345-OEM-1234567-12345
Version         : 6.0.6001

In this case, the following error is returned:

Get-WmiObject : The RPC server is unavailable. (Exception from HRESULT: 0x800706BA)
At line:1 char:5
+ gwmi <<<<  win32\_operatingsystem -computer 192.168.200.14 -credential 'localdomain\\mid'
    + CategoryInfo          : InvalidOperation: (:) \[Get-WmiObject\], COMException
    + FullyQualifiedErrorId : GetWMICOMException,Microsoft.PowerShell.Commands.GetWmiObjectCommand 

#### Solution

1.  Verify IP connectivity to the remote machine using ping. If the ping fails, there is a routing problem. Contact your network administrator.
2.  If the ping succeeds, the issue is related to the remote machine or a filtering device between the MID Server and the remote machine. Fix the firewall configuration on the remote machine. See [Opening ports in Windows Firewall for remote server access](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0549828 "Opening ports in Windows Firewall for remote server access") for information about troubleshooting RPC and DCOM related issues.

### Access is denied

When mid.powershell.local\_mid\_service\_credential\_fallback is true, the error appears as:

**<error>**
	Authentication failure with the local MID server service credential.
**</error>**
**<error>**
	Failed to access target system. Please check credentials and firewall settings on the target system to ensure accessibility: Access is denied. (Exception from HRESULT: 0x80070005 (E\_ACCESSDENIED))
	Stack Trace:    at System.Runtime.InteropServices.Marshal.ThrowExceptionForHRInternal(Int32 errorCode, IntPtr errorInfo)
	  at System.Management.ManagementScope.InitializeGuts(Object o)
	  at System.Management.ManagementScope.Initialize()
	  at System.Management.ManagementObjectSearcher.Initialize()
	  at System.Management.ManagementObjectSearcher.Get()
	  at Microsoft.PowerShell.Commands.GetWmiObjectCommand.BeginProcessing()
	  at System.Management.Automation.Cmdlet.DoBeginProcessing()
	  at System.Management.Automation.CommandProcessorBase.DoBegin()
**</error>**

When mid.powershell.local\_mid\_service\_credential\_fallback is false, the error appears as:

**<error>**
	Authentication failure(s) with available Windows credentials from the instance. Credentials tried: autolab1\\autouserBAD,LOCALDOMAIN\\midBAD
**</error>**

If the local MID service credential is not enabled, the E\_ACCESSDENIED error message does not appear. The authentication failure message is reliable. In most cases, this error is caused by an incorrect credential.

In the MID Server logs with debug enabled:

-   The MID Server first tries the credentials from the Credentials table. These fail with exit code 1 (when mid.powershell.use\_credentials is true).
-   Then it tries the account the MID Server service runs with. This fails with exit code 3 (when mid.powershell.local\_mid\_service\_credential\_fallback is true).

The MID Server returns the error details from the last credential attempted. The MID Server logs return a different error for remote and local credentials, which can be misleading. Complete the following troubleshooting steps to confirm this is an incorrect credential issue.

#### **Troubleshooting**

Run a PowerShell WMI query directly from the MID Server to the remote machine. Open a PowerShell command line and run the following, replacing LOCALDOMAIN\\mid with the credential to test:

gwmi win32\_operatingsystem -computer 192.168.200.14 -credential 'LOCALDOMAIN\\mid'

The expected result is similar to:

SystemDirectory : C:\\Windows\\system32
Organization    :
BuildNumber     : 6001
RegisteredUser  : Windows User
SerialNumber    : 12345-OEM-1234567-12345
Version         : 6.0.6001

In this case, the following error is returned:

Get-WmiObject : Access is denied. (Exception from HRESULT: 0x80070005 (E\_ACCESSDENIED))
At line:1 char:5
+ gwmi <<<<  win32\_operatingsystem -computer 192.168.200.14 -credential 'localdomain\\mid'
    + CategoryInfo          : NotSpecified: (:) \[Get-WmiObject\], UnauthorizedAccessException
    + FullyQualifiedErrorId : System.UnauthorizedAccessException,Microsoft.PowerShell.Commands.GetWmiObjectCommand

This confirms that the credential (user name, password, or both) is incorrect.

#### **Solution**

Find a credential that works and update it in ServiceNow.

### Call was canceled by the message filter

When mid.powershell.local\_mid\_service\_credential\_fallback is true, the error appears as:

**<error>**
	Authentication failure with the local MID server service credential.
**</error>**
**<error>**
	Call was canceled by the message filter. (Exception from HRESULT: 0x80010002 (RPC\_E\_CALL\_CANCELED))
	Stack Trace:    at System.Runtime.InteropServices.Marshal.ThrowExceptionForHRInternal(Int32 errorCode, IntPtr errorInfo)
	  at System.Management.ManagementScope.InitializeGuts(Object o)
	  at System.Management.ManagementScope.Initialize()
	  at System.Management.ManagementObjectSearcher.Initialize()
	  at System.Management.ManagementObjectSearcher.Get()
	  at Microsoft.PowerShell.Commands.GetWmiObjectCommand.BeginProcessing()
**</error>**

When mid.powershell.local\_mid\_service\_credential\_fallback is false, the error appears as:

**<error>**
	Failure(s) with available Windows credentials from the instance. Credentials tried: AUTOLAB1\\autouser,localdomain\\mid
**</error>**
**<error>**
	Call was canceled by the message filter. (Exception from HRESULT: 0x80010002 (RPC\_E\_CALL\_CANCELED))
	Stack Trace:    at System.Runtime.InteropServices.Marshal.ThrowExceptionForHRInternal(Int32 errorCode, IntPtr errorInfo)
	  at System.Management.ManagementScope.InitializeGuts(Object o)
	  at System.Management.ManagementScope.Initialize()
	  at System.Management.ManagementObjectSearcher.Initialize()
	  at System.Management.ManagementObjectSearcher.Get()
	  at Microsoft.PowerShell.Commands.GetWmiObjectCommand.BeginProcessing()
**</error>**

#### **Troubleshooting**

The method for troubleshooting this error is similar to the methods used for the previous errors. Run the PowerShell test command and determine if the error can be reproduced. If it can, the issue is between the MID Server and the remote machine.

This error indicates that the RPC connection is being canceled by the remote machine. Try running the same command against other Windows machines to determine if it works. If it does, this confirms the problem is isolated to one particular Windows machine. The cause on the remote machine could be the Windows firewall filtering access to RPC/DCOM.

#### **Solution**

The following articles can help troubleshoot and fix these problems:

-   [Opening ports in Windows Firewall for remote server access](/kb_view.do?sysparm_article=KB0549828 "Opening ports in Windows Firewall for remote server access")
-   [How to troubleshoot WMI and PowerShell issues on a remote machine for Windows Discovery](/kb_view.do?sysparm_article=KB0549830 "How to troubleshoot WMI and PowerShell issues on a remote machine for Windows Discovery")

### Server execution failed

When mid.powershell.local\_mid\_service\_credential\_fallback is true, the error appears as:

**<error>**
	Authentication failure with the local MID server service credential.
**</error>**
**<error>**
	Failed to access target system. Please check credentials and firewall settings on the target system to ensure accessibility: Access is denied. (Exception from HRESULT: 0x80070005 (E\_ACCESSDENIED))
	Stack Trace:    at System.Runtime.InteropServices.Marshal.ThrowExceptionForHRInternal(Int32 errorCode, IntPtr errorInfo)
	 at System.Management.ManagementScope.InitializeGuts(Object o)
	 at System.Management.ManagementScope.Initialize()
	 at System.Management.ManagementObjectSearcher.Initialize()
	 at System.Management.ManagementObjectSearcher.Get()
	 at Microsoft.PowerShell.Commands.GetWmiObjectCommand.BeginProcessing()
	 at System.Management.Automation.Cmdlet.DoBeginProcessing()
	 at System.Management.Automation.CommandProcessorBase.DoBegin()
**</error>**

When mid.powershell.local\_mid\_service\_credential\_fallback is false, the error appears as:

**<error>**
	Failure(s) with available Windows credentials from the instance. Credentials tried: autolab1\\autouser,LOCALDOMAIN\\mid
**</error>**
**<error>**
	Server execution failed (Exception from HRESULT: 0x80080005 (CO\_E\_SERVER\_EXEC\_FAILURE))
	Stack Trace:    at System.Runtime.InteropServices.Marshal.ThrowExceptionForHRInternal(Int32 errorCode, IntPtr errorInfo)
	 at System.Management.ManagementScope.InitializeGuts(Object o)
	 at System.Management.ManagementScope.Initialize()
	 at System.Management.ManagementObjectSearcher.Initialize()
	 at System.Management.ManagementObjectSearcher.Get()
	 at Microsoft.PowerShell.Commands.GetWmiObjectCommand.BeginProcessing()
**</error>**

If an incorrect credential is used, the E\_ACCESSDENIED error message appears. If a valid credential is used, the CO\_E\_SERVER\_EXEC\_FAILURE error message appears. This occurs when the Windows Management Instrumentation service is paused or stopped on the remote machine.

#### **Troubleshooting**

Open a PowerShell command line on the MID Server and run the following, replacing LOCALDOMAIN\\mid with the credential to test:

gwmi win32\_operatingsystem -computer 192.168.200.14 -credential 'LOCALDOMAIN\\mid'

The expected result is similar to:

SystemDirectory : C:\\Windows\\system32
Organization    :
BuildNumber     : 6001
RegisteredUser  : Windows User
SerialNumber    : 12345-OEM-1234567-12345
Version         : 6.0.6001

In this case, the following error is returned:

Get-WmiObject : Server execution failed (Exception from HRESULT: 0x80080005 (CO\_E\_SERVER\_EXEC\_FAILURE))
At line:1 char:5
+ gwmi <<<<  win32\_operatingsystem -computer 192.168.200.14
    + CategoryInfo          : InvalidOperation: (:) \[Get-WmiObject\], COMException
    + FullyQualifiedErrorId : GetWMICOMException,Microsoft.PowerShell.Commands.GetWmiObjectCommand

This issue is typically caused by the Windows Management Instrumentation service being stopped on the remote machine.

#### **Solution**

Start the Windows Management Instrumentation on the remote machine.
