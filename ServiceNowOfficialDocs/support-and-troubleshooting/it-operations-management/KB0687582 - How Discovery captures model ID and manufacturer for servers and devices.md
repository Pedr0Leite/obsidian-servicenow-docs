---
title: "How Discovery captures model ID and manufacturer for servers and devices"
aliases:
  - KB0687582
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0687582
kb_number: KB0687582
last_modified: 2026-04-06
---

## How Discovery captures model ID and manufacturer for servers and devices

  

### Issue

This article describes how Discovery probes and patterns update the model\_id and manufacturer for network devices, and Linux and Windows servers.

The model\_id and manufacturer are reference fields. In general, a probe gathers both the model\_id and manufacturer from a device and passes the string values to the MakeAndModelJS.fromNames() function along with a model\_type. The model\_type determines the table that is used to get the model\_id. The cmdb\_model table is used if model\_type is empty.

Following are some of the tables used to find the model\_id:

<table style="border-style: solid; border-color: #000000;" border="1" cellspacing="0" cellpadding="4"><tbody><tr><td>&nbsp;Hardware&nbsp;</td><td>&nbsp;cmdb_hardware_product_model&nbsp;</td></tr><tr><td>&nbsp;Consumable&nbsp;</td><td>&nbsp;cmdb_consumable_product_model</td></tr><tr><td>&nbsp;Software</td><td>&nbsp;cmdb_software_product_model</td></tr><tr><td>&nbsp;Application&nbsp;</td><td>&nbsp;cmdb_application_product_model</td></tr></tbody></table>

**Note**: In some cases, the configuration item (CI) may seem to have an empty model and manufacturer when in fact the field is populated. These fields are reference fields and should be populated with sys\_id, not with the values directly. To resolve this issue, the sensor or pattern needs to call _MakeAndModelJS_ to get the reference value instead. This can be confirmed by viewing the xml for the record.

###   
Network Devices (SNMP Discovery)

For network devices, the model\_id and manufacturer are collected in the classification phase of discovery by the _SNMP - Classify_ probe.

The following important object identifiers (OID) determine which model and manufacturer are used:

-   mgmt.mib-2.entityMIB.entityMIBObjects.entityPhysical.entPhysicalTable entPhysicalModelName
-   mgmt.mib-2.entityMIB.entityMIBObjects.entityPhysical.entPhysicalTable entPhysicalMfgName
-   mgmt.mib-2.system.sysObjectID

The model and manufacturer from **Discovery Definition > Classification > SNMP System OIDs** is used when sysObjectID is returned. The values returned by entPhysicalModelName and entPhysicalMfgNam are used if the sysObjectID value is not returned, or if there is no matching record for the sysObjectID under SNMP System OIDs.

**Note:** The model\_id and manufacturer may alternate if the values for entPhysicalModelName and entPhysicalMfgName do not match the SNMP System OID values respectively and the sysObjectID is not returned consistently. Therefore, if possible, the values in the SNMP System OIDs should be updated to match what is returned by the device. Having two options to get model\_id and manufacturer provides redundancy.  
  

### UNIX/Linux

Different distributions of UNIX or Linux use their own probes or sensors to collect the model\_id and manufacturer.

The default probes and sensors that collect the model and manufacturer are:

<table style="border-style: solid; border-color: #000000;" border="1" cellspacing="0" cellpadding="4"><tbody><tr><td><strong>&nbsp;Probe&nbsp;</strong></td><td><strong>&nbsp;Command / Script</strong></td></tr><tr><td>Linux - Hardware Information&nbsp;</td><td>&nbsp;dmidecode; echo dummy &gt; /dev/null&nbsp;</td></tr><tr><td>HP-UX - Hardware Model</td><td>&nbsp;model</td></tr><tr><td>IBM AIX - Hardware Model</td><td>&nbsp;lsattr -El sys0 -a modelname -F value</td></tr><tr><td>Solaris - Hardware Model</td><td>&nbsp;suntype.sh</td></tr></tbody></table>

### Windows

#### **Retrieve Windows OS Servers pattern**

The Windows device's model\_id and manufacturer information are collected by the Windows - OS Information probe.

The WMI fields used for model and manufacturer are:

-   Win32\_ComputerSystem.Manufacturer
-   Win32\_ComputerSystem.Model

To manually test what the model and manufacturer values are via WMI you can execute the following command in PowerShell from your host server:

Get-WmiObject -query "SELECT Name,Domain,Manufacturer,Model,UserName FROM Win32\_ComputerSystem"

The following example shows the result of running a PowerShell command to view the model and manufacturer of a host:

### ![Model and Manufacturer powershell command](sys_attachment.do?sys_id=0eef6c5247c0c7d4b7832920326d43c6 "Model and Manufacturer powershell command")  
Other device classes

There are many other device classes that can be discovered, and custom ones can be created. They each need to query the target device or application for such fields and use the _MakeAndModelJS_ script to get the proper reference values to update the record.

### Patterns

Patterns call the _MakeAndModelJS_ via the _Pattern Designer > Pre Post Processing_ script, in particular the _OSs - Pre Sensor_ script. The **Pattern/s** column determines what patterns use this pre or post script to alter the payload.

### Release

All releases

### Resolution
