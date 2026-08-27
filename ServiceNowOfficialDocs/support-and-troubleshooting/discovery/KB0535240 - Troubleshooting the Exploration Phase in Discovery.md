---
title: "Troubleshooting the Exploration Phase in Discovery"
aliases:
  - KB0535240
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0535240
kb_number: KB0535240
last_modified: 2025-05-27
---

## Troubleshooting the Exploration Phase in Discovery

  

### Issue

During the Exploration Phase in Discovery you may run across one of the below common exploration phase issues such as failed user logins, credential or connection issues. 

### Release

All

### Resolution

This article pertains to Discovery with probes and sensors (not patterns).

CI Classification triggers the initial probes that are launched during the exploration phase. All exploration probes that meet the following conditions are triggered after the identification probe:

1.  Phase = Exploration
2.  Active = True
3.  Condition script is empty or evaluates to true

Additional exploration probes can also be triggered via the Process Classification or within the script of a sensor.

During exploration, most probes use the same credentials used during classification and identification, however there are probes that have additional requirements.

1.  VMware vCenter and ESX/ESXi  
    -   While discovering a Windows Server, if an active process is classified as vCenter, the VMware - vCenter probe is launched. The credential used for this probe is of type=VMware.
    -   During the processing of the results from the VMware - vCenter probe, for each ESX server that is found, a CIM - ESX Chassis Serial Number probe is launched. This probe uses the credential type=CIM
    -   For additional details, see [Discovery for VMware vCenter](https://docs.servicenow.com/csh?topicname=c_DiscoveryForVMwareVCenter.html&version=latest "Discovery for VMware vCenter").
2.  Microsoft SQL  
    -   While discovering a Windows Server, if an active process is classified as Microsoft SQL Server, the Windows - MSSQL probe is triggered. The requirements for this probe are outlined in our document [MSSQL server discovery](https://docs.servicenow.com/csh?topicname=mssql-data-collected-pattern.html&version=latest "MSSQL server discovery").
3.  SSH commands that require sudo:  
    -   Certain SSH probes require elevated privileges and leverage the use of sudo. Here is a list of the probes: [UNIX and Linux commands requiring root privileges for Discovery and Orchestration](https://docs.servicenow.com/csh?topicname=r_SSHCredentialsForm.html&version=latest "UNIX and Linux commands requiring root privileges for Discovery and Orchestration").

### Troubleshooting

The same commands within Discovery probes can be executed outside of the ServiceNow instance on the MID Server host. Typically this is the best way to troubleshoot.

WMI

-   Use the command-line tool wmic to target WMI Objects and registry paths.
-   Use the command-line tool cscript to run javascript against a remote machine.

Powershell

-   Within Powershell, use gwmi to target Managed Objects and registry paths.

SSHCommand 

-   Use an SSH client and connect to the target machine with the same credential that Discovery should be using.
-   Once connected, execute the same command or script.

SNMP

-   Use a command-line tool like snmpwalk to target OIDs on a remote device.
-   Use Wireshark or tcpdump to capture packets between the MID server host and the device to verify whether packets are being transmitted.

### Watch Out For

A credential that is successful during the Classification and Identification does not imply that it is successful during Exploration. 

-   Be wary of the order of credentials. Multiple credentials may have access to the same target, each with different privileges.
-   Probes have a timeout. A probe may return incomplete information or display a timeout error. This may imply that the data is too large to return in the given time or the MID Server is too far from the target. It is possible to extend the timeout of a probe.

### Common Exploration Phase Errors

Below is a list of common exploration phase issues as well as suggestions on how to resolve them.

-   WMI and Powershell  
    -   The impersonation of the user failed.
    -   Ensure that the domain is specified, along with the username in the credentials.

-   Connection failed to WMI service and other common Windows (WMI/Powershell) error messages:  
      
    _Error: The remote server machine does not exist or is unavailable  
    __  
    Failed to access target system. Please check credentials and firewall settings on the target system to ensure accessibility: Access is denied. (Exception from HRESULT: 0x80070005 (E\_ACCESSDENIED))  
      
    Failed to access target system. Please check credentials and firewall settings on the target system to ensure accessibility: The RPC server is unavailable. (Exception from HRESULT: 0x800706BA)  
    _  
    -   WMI, does the MID server service account have access to the targeted machine? What if a domain admin account is used as the MID server service account?
    -   From the command prompt on the mid server host, execute for runner\_type=WMI  
          
        wmic /node:"<target>" /user:"<user>" /password:"<password>" path win32\_operatingsystem  
         
    -   From within a Powershell console on the mid server host, execute for runner\_type=Powershell  
          
        gwmi win32\_operatingsystem -computer <ip> -credential '<username>'  
         
    -   It is possible that the probe is timing out while waiting for a response. If the command is successful from a command prompt, try extending the wmi\_timeout value of the probe.  
         
-   vCenter Discovery  
    -   _Unable to establish connection to https://10.249.17.207/sdk_
    -   No VMWare type credential is stored in the credential table.
    -   The user name being used is a domain account and needs to be prefixed with a domain.  
         
-   _CIM\_RegisteredProfile{{RegisteredName='Base Server'}}.CIM\_ElementConformsToProfile{{ResultClass:'CIM\_ComputerSystem'}}.CIM\_ComputerSystemPackage{{ResultClass:'CIM\_Chassis',PackageType='3'}}.\* - CIM\_RegisteredProfile - Authentication failed._  
    -   No CIM type credential is stored in the credential table. Also, see vCenter: Setting up CIM read-only access: [Creating a local read-only user](http://community.kaseya.com/kb/w/wiki/932.aspx "Creating a local read only user") and [Dedicated CIM account fail](http://communities.vmware.com/message/1644658 "Dedicated CIM account fail").  
         
-    _com.vmware.vim25.NoPermission errors_  
    -   Need to have a credential of type=VMware within the Credentials table. If the user is part of the domain, it needs to be explicitly defined, username=domain\\user.
    -   Within ecc\_agent\_jar, _vijava.jar_ there needs to be an attached and readable (downloadable) jar file. The MID server needs to be able to download this jar.  
         
-   MSSQL  
    -   _Cannot find type \[Microsoft.SqlServer.Management.Smo.Server\]: make sure the assembly containing this type is loaded_
    -   You need to install Microsoft SQL Server management library (SMO): [MSSQL server discovery](https://docs.servicenow.com/csh?topicname=mssql-data-collected-pattern.html&version=latest "MSSQL server discovery").

-   _java.sql.SQLException: com.microsoft.sqlserver.jdbc.SQLServerException: SQL Server version 8 is not supported by this driver_  
    -   [Microsoft dropped support for SQL Server 2000 (8.0)](http://msdn.microsoft.com/en-US/data/ff928484 "Microsoft dropped support for SQL Server 2000 (8.0)") in JDBC version 4, in exchange for native support for SQL Server 2012.
