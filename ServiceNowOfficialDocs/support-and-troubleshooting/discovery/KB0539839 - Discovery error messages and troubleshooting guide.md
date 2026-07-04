---
title: "Discovery error messages and troubleshooting guide"
aliases:
  - KB0539839
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0539839
kb_number: KB0539839
last_modified: 2026-05-26
---

## Discovery error messages and troubleshooting guide

  

### Issue

Resolve common Discovery error messages using this troubleshooting reference. This article covers error messages for Discovery general operations, sensors, Oracle database instances, MID Server agent logs, vCenter, MSSQL, and IIS.

### In this article

-   [Discovery general messages](#discovery-general)
-   [Discovery sensor messages](#discovery-sensor)
-   [Discovery Oracle database instance messages (Unix)](#discovery-oracle-unix)
-   [Discovery Oracle database instance messages (Windows)](#discovery-oracle-windows)
-   [Discovery MID Server agent log messages](#discovery-mid-server-agent-log)
-   [vCenter Discovery messages](#vcenter-discovery)
-   [MSSQL messages](#microsoft-sql)
-   [IIS messages](#iis-messages)

### Discovery general messages

#### **org.xml.sax.SAXParseException: The entity name must immediately follow the '&' in the entity reference**

-   **Cause:** Special characters were used in a password saved in an XML file.  
      
    
-   **Solution:** See the related documentation for information about handling special characters in XML files.

#### **Identified, ignored extra IP**

-   **Cause**: A targeted IP address belongs to a device that is already being discovered. This occurs when a device has multiple IP addresses (for example, a Windows server with two NIC cards) and Discovery targets both IP addresses in the same schedule.  
      
    
-   **Solution**: No action required. This warning is expected behavior. Discovery ignores the second IP address to prevent updating the same CI twice in a single Discovery run.

#### **Authentication failures**

-   **Cause**: The Discovery application could not authenticate to the target device, preventing discovery of the CI.  
      
    
-   **Solution**: Add the credentials for the target machine to the Discovery credentials table.

#### **Identified, not updating CI, now finished**

-   **Cause**: No match was found on any of the CI identifiers.  
      
    
-   **Solution:** Review the CI identification rules and verify the target device has identifiable attributes.

#### **The impersonation of user failed**

-   **Cause**: This PowerShell error occurs when the domain is not specified with the user name.  
      
    
-   **Solution**: Verify the domain is specified along with the user name in the credentials (for example, domain\\username).

#### **Connection failed to WMI service. Error: Permission denied**

-   **Cause**: This WMI error occurs when the MID Server service does not have permission to access the target device.  
      
    
-   **Solution**: Verify the MID Server service is running with correct credentials and has access to the target device.  
    To test connectivity, run the following command from the command prompt on the MID Server host:  
      
    wmic /node:<target> /user:<user> /password:<password> path win32\_operatingsystem  
      
    Where:

-   -   <target> = IP address of target device
    -   <user> = user account used by the MID Server service
    -   <password> = password used by the MID Server service

#### **Connection failed to WMI service. Error: The remote server machine does not exist or is unavailable**

-   **Cause**: This WMI error occurs when the MID Server cannot reach the target machine. Possible causes include incorrect service account permissions or firewall restrictions.   
      
    
-   **Solution**: Verify the following:
    -   The MID Server service account has access to the targeted machine
    -   A domain admin account is used as the MID Server service account (if required)
    -   Firewalls allow the connection

To test connectivity, run the following commands from the MID Server host:

**For WMI:**

wmic /node:"<target>" /user:"<user>" /password:"<password>" path win32\_operatingsystem

**For PowerShell:**

gwmi win32\_operatingsystem -computer <ip> -credential '<username>' 

#### **Provider is not capable of the attempted operation**

-   **Cause**: The WMI repository is corrupted.  
      
    
-   **Solution**: Rebuild the WMI repository. For instructions, see the Microsoft TechNet article on rebuilding the WMI repository.

#### **The result file can't be fetched because it doesn't exist**

-   **Cause**: PowerShell cannot write to the admin share. The admin share requires write permissions for Discovery to function.  
      
    
-   **Solution**: Verify write permissions are enabled for the admin share. For more information, see [Additional permissions](https://docs.servicenow.com/csh?topicname=r_AdditionalPermissions.html&version=latest).

#### **Please run sneep as root to ensure correct serial number from fserial data source**

-   **Cause**: The Oracle Sneep command line tool is required for the Solaris - Serial Number probe to work correctly. There is a known limitation with Fujitsu PRIMEPOWER devices.  
      
    
-   **Solution**: Run the Solaris discovery with root credentials. Verify the Oracle Sneep tool is installed on the target device.

### Discovery sensor messages

#### **Version mismatch errors (major version)** 

#### "The multisensor will not process because its major version = X while probe\_name responding script's major version = Y"  
"The multisensor will not process because its responding script's major version = X while its referenced probe probe\_name major version = Y"  
"sensor\_name sensor's major version = X while its related probe's major version = Y"

-   **Cause**: A major version mismatch exists between the probe and sensor versions.  
      
    
-   **Solution**: The sensor stops processing until this condition is resolved. Update the probe or sensor to matching major versions. For more information, see [Discovery probes and sensors.](https://docs.servicenow.com/csh?topicname=c_DiscoveryProbesAndSensors.html&version=latest "Probe and Sensor Versions")

#### **Version mismatch errors (minor version)**

#### "sensor\_name multisensor's minor version = X while probe\_name responding script's minor version = Y"  
"sensor\_name multisensor's responding script's minor version = X while its referenced probe probe\_name minor version = Y"  
"sensor\_name sensor's minor version = X while its related probe's minor version = Y"

-   **Cause**: A minor version mismatch exists between the probe and sensor versions.  
      
    
-   **Solution**: Processing continues, but consider resolving this condition by updating the probe or sensor to matching minor versions. For more information, see [Discovery probes and sensors.](https://docs.servicenow.com/csh?topicname=c_DiscoveryProbesAndSensors.html&version=latest "Probe and Sensor Versions")

#### **Sensor error when processing . . .  : No sensors defined**

-   **Cause**: The corresponding sensor for the probe is missing or inactive. Every active probe requires a corresponding sensor to process collected data.  
      
    
-   **Solution**: Verify the sensor exists and is active. For more information, see [Find the cause of a "No Sensor Defined" error message](https://docs.servicenow.com/csh?topicname=t_IdentifyCauseNoSenDefEM.html&version=latest "Evaluating the No Sensors Defined Message").

#### **Sensor error when processing . . . : typeError: . . .**

-   **Cause**: The sensor encountered a JavaScript core error constructor.  
      
    
-   **Solution**: Review the sensor script for JavaScript errors. For more information, see [Discovery error messages](https://www.servicenow.com/docs/r/it-operations-management/discovery/c_DiscoveryErrorMessages.html).

  

### Discovery Oracle database instance messages (Unix)

#### **No Oracle SID was provided**

-   **Cause**: The process classification script failed to pass the SID value or passed an empty value to the probe script. Process classification parses the SID value from running processes with names starting with ora\_pmon\_.  
      
    
-   **Solution**: Verify the Oracle process (ora\_pmon\_\*) is running on the target device and the SID can be parsed from the process name.

#### **No Oracle oratab file found**

-   **Cause**: Discovery could not find the oratab file in any of the expected locations.  
      
    Discovery searches the following paths in order:

-   -   /var/opt/oracle/oratab
    -   /etc/oratab
    -   /var/opt/unix/oratab
    -   /etc/oracle/oratab
    -   /etc/opt/oracle/oratab
    -   /shared/opt/oracle/oratab
-   **Solution**: Verify the oratab file exists in one of the expected locations and Discovery has read permissions.

#### **Could not read Oracle (s)pfile: pfile**

-   **Cause**: The command to read the spfile on the target machine failed.  
      
    
-   **Solution**: Verify Discovery has permissions to read the Oracle system parameter file on the target device.

#### **No Oracle (s)pfile found (or insufficient permissions)**

-   **Cause**: Discovery cannot find the Oracle system parameter file or lacks permissions to access it.  
      
    
-   **Solution**: Verify the spfile exists and Discovery has the correct permissions to access the Oracle system parameter file.

#### **Could not determine Oracle instance version**

-   **Cause**: Discovery failed to extract Oracle version information using any of the following methods:
    -   Output from the ORA\_HOME/bin/sqlplus /NOLOG command
    -   Output from the ORA\_HOME/bin/lsnrctl status command
    -   Path of ORA\_HOME  
          
        
-   **Solution**: Verify the Oracle installation is complete and the sqlplus and lsnrctl utilities are accessible from ORA\_HOME/bin.

### Discovery Oracle database instance messages (Windows)

#### **Value for SID is empty. Invocation of Probe 'WMIRunner-Oracle - Instance PFile' is skipped.**

-   **Cause**: The oracle.exe process was started without a SID value as a parameter. The probe parses parameters passed to the oracle.exe process to identify the SID value.  
      
    
-   **Solution**: This warning displays in the Discovery Log. Verify the Oracle instance is started with the correct SID parameter.

#### **Invalid value of oracle exe path: path**

-   **Cause**: The process classification script failed to pass the full path of oracle.exe or passed an empty value to the probe's PowerShell script.  
      
    
-   **Solution**: Verify the Oracle installation path is correct and the oracle.exe file exists at the expected location.

#### **Invalid value of SID:<<$sid>>**

-   **Cause**: The process classification script failed to pass the SID value or passed an empty value to the probe's PowerShell script.  
      
    
-   **Solution**: Verify the Oracle instance is running and the SID can be parsed from the oracle.exe process parameters.

#### **Could not able to find the Server Parameter (spfile) file**

-   **Cause**: The spfile is not in one of the expected locations. Discovery searches specific locations for the spfile.  
      
    
-   **Solution**: Verify the spfile location and confirm Discovery can access it. Consider moving the spfile to a standard location. For more information, see the product documentation on [Discovery](https://www.servicenow.com/docs/r/it-operations-management/discovery/r-discovery.html).

#### **Oracle exe path is invalid**

-   **Cause**: The process classification script failed to pass the full path of oracle.exe or passed an empty value to the probe's PowerShell script.  
      
    
-   **Solution**: Verify the Oracle installation path is correct and the oracle.exe file exists at the expected location.

#### **Could not determine Oracle instance version**

-   **Cause**: The command sqlplus.exe -V failed to return a result on the target machine.  
      
    
-   **Solution**: Verify sqlplus.exe is installed and accessible on the target machine. Test by running the following command locally:

 sqlplus.exe -V

#### Could not determine oracle instance version from result: result

-   **Cause**: The command sqlplus.exe -V returned a result, but Discovery could not parse the version information.  
      
    
-   **Solution**: Verify the Oracle installation is valid. The sqlplus.exe -V command should return a parseable version string.

### Discovery MID Server agent log messages

#### **WARNING \*\*\* WARNING \*\*\* A private key has invalid format**

-   **Cause**: The SSH private key was not copied completely.  
      
    
-   **Solution**: Copy the entire contents of the private key, including the ---BEGIN and END--- markers:

### vCenter Discovery messages

#### **Unable to establish connection to [https://10.249.17.207/sdk](https://10.249.17.207/sdk)**

-   **Cause**: One of the following issues exists:
    -   No VMware type credential is stored in the credential table
    -   The user name is a domain account and needs to be prefixed with the domain  
          
        
-   **Solution**: Add a VMware credential to the Credentials table. If using a domain account, format the user name as domain\\username.

#### **CIM\_RegisteredProfile{{RegisteredName='Base Server'}}.CIM\_ElementConformsToProfile{{ResultClass:'CIM\_ComputerSystem'}}.CIM\_ComputerSystemPackage{{ResultClass:'CIM\_Chassis',PackageType='3'}}.\* - CIM\_RegisteredProfile - Authentication failed.**

-   **Cause**: No CIM type credential is stored in the credential table.  
      
    
-   **Solution**: Add a CIM credential to the Credentials table with root user access.

#### com.vmware.vim25.NoPermission errors

-   **Cause**: VMware permissions are not configured correctly.  
      
    
-   **Solution**: Verify the following:
    -   A VMware credential exists in the Credentials table (type = VMware)
    -   If using a domain account, format the user name as domain\\username
    -   The vijava.jar file is attached and readable (downloadable) in the ecc\_agent\_jar table
    -   The MID Server can download the JAR file

### Microsoft SQL messages

#### **Cannot find type \[Microsoft.SqlServer.Management.Smo.Server\]: make sure the assembly containing this type is loaded**

-   **Cause**: The Microsoft SQL Server Management Objects (SMO) library is not installed.  
      
    
-   **Solution**: Install the Microsoft SQL Server Management Objects (SMO) library on the target machine. For installation instructions, see [Software discovery](https://docs.servicenow.com/csh?topicname=c_Software.html&version=latest).

#### **java.sql.SQLException: com.microsoft.sqlserver.jdbc.SQLServerException: SQL Server version 8 is not supported by this driver**

-   **Cause**: Microsoft discontinued support for SQL Server 2000 (version 8.0) in JDBC version 4. [Learn more](http://msdn.microsoft.com/en-US/data/ff928484)  
      
    
-   **Solution**: Use JDBC version 3, which supports SQL Server 2000 but lacks native support for SQL Server 2012.

  

### IIS messages

#### **WMI: Get IIS information Message: Invalid namespace**

-   **Cause**: The WMI namespace root\\MicrosoftIISv2 was replaced by root\\WebAdministration starting with IIS 7.0 (Windows Server 2008).  
      
    
-   **Solution**: Install the IIS 6 WMI Compatibility server role for the root\\MicrosoftIISv2 namespace to be available on Windows Server.

To view available namespaces, run the following PowerShell command:

Get-WMIObject -class \_\_Namespace -namespace root | Format-Table name

### Release

All supported releases

### Resolution

### Related Links

-   [Microsoft TechNet article](http://technet.microsoft.com/en-us/library/0a71c4f6-68de-40f7-94cf-74b73cbda37b.aspx)
-   [More Information to enable IIS6 Compatibility Support for IIS 7](http://docs.liebsoft.com/Account-Reset-Console-Installation-Guide/4469.htm)
