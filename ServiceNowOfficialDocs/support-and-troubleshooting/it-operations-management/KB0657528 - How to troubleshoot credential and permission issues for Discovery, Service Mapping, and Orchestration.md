---
title: "How to troubleshoot credential and permission issues for Discovery, Service Mapping, and Orchestration"
aliases:
  - KB0657528
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0657528
kb_number: KB0657528
last_modified: 2026-02-17
---

## How to troubleshoot credential and permission issues for Discovery, Service Mapping, and Orchestration

  

### Issue

Troubleshoot common credential and permission issues for Discovery, Service Mapping, and Orchestration. This article covers general troubleshooting steps, credential testing, and specific guidance for Windows, SSH, SNMP, and VMware credentials.

For a video walkthrough on troubleshooting credential issues with Discovery, see [Troubleshooting common issues when launching the Discovery app (YouTube)](https://www.youtube.com/watch?v=ac2W53_c_hQ).

### Release

All supported releases

### Resolution

### Credentials

To discover a device or perform orchestration activities, add credentials to the credentials table. Credential records specify a user name, a password, a credential type (Windows, SSH, SNMP, VMware), and the MID Servers allowed to use the credential.

When the MID Server starts or when a credential is modified, the MID Server downloads and caches all available credentials.

Credentials for Discovery, Service Mapping, and Orchestration all use the same credentials table.

**Note**: The error message for credential failures was updated from "Adding target to blacklist. No valid credential found for types..." to "Could not find any valid credentials to authenticate the target for types..." There is no behavioral change.

### **General Troubleshooting**

General troubleshooting involves three main actions: test the credential, ping the device, and telnet into the port used for the credential test. See the following sections for details on each action.

#### **Test the credential**

1.  Go to the Credentials table.
2.  Select the credential.
3.  Select **Test Credential**.
4.  Complete the form fields for the credential test.
5.  Select **OK**.

If the credential test fails, verify that the user name and password are correct. A typographical error is often the cause of credential failures. If the credentials are correct and the error continues, enable debug logging on the MID Server for further investigation. Review the MID Server logs after reproducing the issue with debug enabled. Before enabling debug, verify that the MID Server can communicate with the target using the following steps.

#### **Ping the device**

A ping confirms the device is available on the network.

1.  Log in to the MID Server host and open a command prompt.
2.  Run the following command: ping <ip\_address>

If the ping is not successful, contact the target device administrator.

**Note**: Some environments may have ICMP requests disabled, which can cause ping to fail.

#### **Telnet into the port**

If the ping is successful, the device is available on the network and reachable from the MID Server host. However, protocols used to communicate with target hosts connect to a specified port. The port may not be open on the target host or along the network path.

Run the following telnet command to verify whether the port is open:

telnet <ip\_address> <port\_number>

The following are some of the default ports. A system administrator may change these ports.

-   WMI: 135
-   SSH: 22
-   VCenter: 443
-   WinRM: 5985
-   WBEM: 5989
-   LDAP: 389

If the telnet test fails, contact the target device administrator and the network administrator to confirm the following:

-   The firewall on the device allows traffic on the port tested by telnet.
-   No network firewalls are blocking traffic from the MID Server to the target host on the tested port.

**Note**: Telnet uses the TCP protocol. UDP connectivity cannot be tested using telnet.

Collecting MID Server Debug logs

To enable debug logging on the MID Server:

1.  Go to **MID Server** > **Servers**.
    
2.  Select the MID Server used for the failed discovery or orchestration activity.
    
3.  In the **Configuration Parameters** related list, select **New**.
    
4.  Set **Parameter Name** to mid.log.level and set the value to debug.
    

After debugging is complete, set the value back to info.

To collect the MID Server logs:

1.  On the MID Server record, select **Grab MID Logs**.
    
2.  Select the input records displayed.
    

Windows Credentials

A PowerShell WMI query from the MID Server to the remote machine can test access and permissions.

1.  Open a PowerShell command line on the MID Server host.
    
2.  Run the following command, replacing LOCALDOMAIN\\mid with the credential to test and 192.168.200.14 with the target IP address:
    
    gwmi win32\_operatingsystem -computer 192.168.200.14 -credential 'LOCALDOMAIN\\mid'
    

The expected result is similar to:

SystemDirectory : C:\\Windows\\system32   
Organization : BuildNumber : 6001   
RegisteredUser : Windows User   
SerialNumber : 12345-OEM-1234567-12345   
Version : 6.0.6001

If the WMI command fails, the credential is either incorrect or lacks the required permissions. Contact your Windows administration team to investigate further. If basic WMI queries from the MID Server to the target host fail, discovery and orchestration activities cannot succeed.

**Further documentation on ServiceNow Windows credentials**

The following articles provide in-depth troubleshooting for Windows credential errors:

-   [KB0549834](https://support.servicenow.com/kb_view.do?sysparm_article=KB0549834) - MID Server: troubleshooting WMI/Powershell issues - Credentials
-   [KB0549830](https://support.servicenow.com/kb_view.do?sysparm_article=KB0549830) - Windows Discovery - Troubleshooting WMI/Powershell issues on the remote machine
-   [Opening ports in Windows Firewall for remote server access](https://support.servicenow.com/kb_view.do?sysparm_article=KB0549828 "Opening ports in Windows Firewall for remote server access")

The following product documentation describes permission requirements for Windows credentials:

-   [Permission requirements for Windows credentials](https://docs.servicenow.com/csh?topicname=r_WindowsCredentialsForm.html&version=latest "Permission requirements for Windows credentials")
-   [Discovery Windows probes and permissions](https://docs.servicenow.com/csh?topicname=r_DiscoWinProbesAndPermissions.html&version=latest "Discovery Windows probes and permissions")
-   [Additional Discovery probe permissions](https://docs.servicenow.com/csh?topicname=r_AdditionalPermissions.html&version=latest "Additional Discovery probe permissions")

### SSH Credential

#### **Confirm authentication**

To troubleshoot SSH credential errors, use an SSH client (for example, PuTTY) to connect to the target IP address from the MID Server host. Use the same user name and password combination configured in the credentials table. Access to the target system is required for any discovery or orchestration activity.

#### **Confirm authorization and permissions**

A user may be able to log in to a target system but may not have permission to run the commands attempted by discovery or orchestration. See the following documentation to confirm that the user meets the requirements:

-   [Access Requirements for Non-Root Credentials](https://docs.servicenow.com/search?q=UNIX+and+Linux+credentials "Access Requirements for Non-Root Credentials")
-   [UNIX and Linux commands requiring root privileges for Discovery and Orchestration](https://docs.servicenow.com/search?q=UNIX+and+Linux+commands+requiring+root+privileges+for+Discovery+and+Orchestration "UNIX and Linux commands requiring root privileges for Discovery and Orchestration")

To check what commands a user can run on a UNIX-based device, log in to the target host with the user and run the following command:

sudo -l

The output shows what privileged commands the user can run using sudo.

#### **Check the SSH client implementation**

The MID Server parameter mid.ssh.use\_snc enables the ServiceNow SSH client (SNCSSH) on individual MID Servers. SNCSSH is the ServiceNow implementation of an SSH client and is active by default for all MID Servers on new instances. Enabling the ServiceNow SSH client disables the legacy J2SSH client.

**Important**: Do not mix SSH client types for MID Servers connected to the same instance.

The default value is **true** for new instances beginning with the Eureka release and false for prior existing instances.

#### **Private key credentials**

In some cases, sudo commands do not work with private key credentials because there is no password to supply to the sudo command. To resolve this, add the NOPASSWD option to the sudo configuration or provide a password to the credential. For example:

disco ALL=(root) NOPASSWD:/usr/sbin/dmidecode,/usr/sbin/lsof,/sbin/ifconfig

In this example, the user disco can run dmidecode through sudo without providing a password. If a command fails when using a private key credential, confirm the user can run the command without providing a password.

If the account can successfully log in to the target and run the commands used by the probe or orchestration activity but fails when using the MID Server, follow the **Collecting MID Server debug logs** section. Add the parameter mid.ssh.debug = true for additional details.

### SNMP credential

SNMP uses UDP, which does not create a virtual connection to the target host like TCP. If a credential is incorrect or unauthorized, no reply may be given depending on the SNMP version used. A timeout may appear in the discovery log when an invalid credential is used.

Common reasons for a timeout include:

-   The credential is not valid.
-   The network or target server is too busy and does not return the OIDs within the timeout.

#### **Run an SNMP query to the target**

Using an SNMP tool from the MID Server, query OID 1.3.6.1.2.1.1.1 (sysDescr), which returns a description of the device.

The following example uses SnmpWalk.exe. In the first test, the credential was set to "publi," which is an incorrect community string. The correct community string is "public."

C:\\SNMPWalk>.\\SnmpWalk.exe -r:10.127.212.181 -c:"publi" -os:.1.3.6.1.2.1.1 -op:.1.3.6.1.2.1.1.1.0  
  
%Failed to get value of SNMP variable. Timedout.

No credential failure error is returned. Instead, the query times out.

In the following example, the community string was corrected to "public."

C:\\SNMPWalk>.\\SnmpWalk.exe -r:10.127.212.181 -c:"public" -os:.1.3.6.1.2.1.1 -op:.1.3.6.1.2.1.1.1.0  
  
OID=.1.3.6.1.2.1.1.1.0, Type=OctetString, Value=Linux Linux-Tomcat 3.10.0-327.el7.x86\_64 31 SMP Thu Nov 19 22:10:57 UTC 2015 x86\_64

After correcting the community string, the sysDescr value was returned instead of timing out.

#### **SNMP parameters**

The timeout for an SNMP request can be increased using the timeout probe parameter. The default value is 1500 (1.5 seconds). Try increasing the timeout if a credential is known to be correct but no OIDs are returned. For tabular data, try the use\_getbulk parameter to improve efficiency.

For more information on SNMP probe parameters, see [SNMP probes](https://docs.servicenow.com/search?q=snmp+probes "SNMP probes").

#### **No result returned from probe**

In some cases, a warning appears in the discovery log stating "No result returned from probe." This occurs when an input returns empty for the OID queried by the probe. The device does not have any results to return for the specified OID, and this behavior is expected. If you suspect discovery may be incorrect, run a query for the same OID against the target IP address to check the output.

**Further documentation for SNMP credentials**

-   [How to troubleshoot MID Server SNMP issues for Discovery, Service Mapping, and Orchestration](https://support.servicenow.com/kb_view.do?sysparm_article=KB0696727 "How to troubleshoot MID Server SNMP issues for Discovery, Service Mapping, and Orchestration")

### VMWare credential

#### **Confirm authentication**

Verify that the same account configured in the credentials table can log in to the VCenter target:

1.  Log in to the MID Server host.
2.  Open a browser and go to the following URL, replacing <V-Center\_IP\_Address> with the IP address of the VCenter server:  
    https://<V-Center\_IP\_Address>/mob
3.  Use the same user name, password, and format as configured in the credentials table record.

If the test fails, contact your VMware team to troubleshoot or provide access to the credential. If the test succeeds but discovery still fails, follow the **Collecting MID Server debug logs** section for further investigation.

**Further documentation**

-   [Understand vCenter Discovery process and troubleshooting](https://support.servicenow.com/kb?sysparm_article=KB0813327&id=kb_article_view "Understand vCenter Discovery process and troubleshooting")
-   [How to resolve UCS-HD Discovery errors 551 and 555 for authentication and session failures](https://support.servicenow.com/kb_view.do?sysparm_article=KB0726469 "How to resolve UCS-HD Discovery errors 551 and 555 for authentication and session failures")
