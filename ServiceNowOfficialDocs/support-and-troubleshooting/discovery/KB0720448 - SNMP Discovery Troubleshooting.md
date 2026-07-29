---
title: "SNMP Discovery Troubleshooting"
aliases:
  - KB0720448
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0720448
kb_number: KB0720448
last_modified: 2026-06-17
---

## SNMP Discovery Troubleshooting

  

### Issue

The SNMP probes and patterns use the SNMP protocol to query a particular device for a list of OIDs, which are then traversed and the results passed back to the sensors.

Discovery supports SNMP versions 1, 2c, and 3. Discovery uses version 1 and 2c by default. You must enable support for version 3. MID Servers support all SNMP protocol versions by default. You can set a MID Server to only support specific versions of SNMP.

This article discusses some of the most common issues found with SNMP-based Discovery and steps to troubleshoot and resolve these issues.

### Release

All

### Resolution

### Quick links to FAQ / Common problems:

-   [Error when loading a MIB Module](#mib_module)
-   [SNMP probe fails to return information](#probe_fails)
-   [SNMP classification not working](#snmp_classification)
-   [SNMP credential not working](#snmp_credential)

### Error when loading a MIB Module

The user attempts to load the MIB file PAN-COMMON-MIB, and the following error is thrown in the MID server agent log:

12/09/18 16:57:48 (993) MIB Initializer WARNING \*\*\* WARNING \*\*\* MIB loader errors when loading MIB: PAN-COMMON-MIB  
\---line 20, column 9: couldn't find referenced MIB 'PAN-GLOBAL-TC'  
\---line 22, column 9: couldn't find referenced MIB 'PAN-GLOBAL-REG'  
\---line 45, column 9: undefined symbol 'panModules'  
\---line 51, column 9: undefined symbol 'panCommonMib'  
\---line 57, column 9: undefined symbol 'panCommonMib'  
\---line 63, column 9: undefined symbol 'panCommonMib'  
\---line 71, column 9: referenced value is not an object identifier

This issue happens if your new MIB has dependencies on another MIB. The MIB that fills the dependency must exist before you create your new record. Search the existing MIBs to ensure that the required MIBs are already loaded. You can also check the dependent MIBs by opening up the MIB file and inspecting the IMPORTS section. Look up for dependent MIBs that follow the FROM keyword at the beginning of the file. In this PAN-COMMON-MIB MIB file example, the MIBs shown in red are dependent and must be uploaded first:

IMPORTS

MODULE-IDENTITY, OBJECT-IDENTITY,  
OBJECT-TYPE, NOTIFICATION-TYPE,  
Integer32  
FROM **SNMPv2-SMI**  
\-- MODULE-COMPLIANCE, OBJECT-GROUP  
\-- FROM **SNMPv2-CONF**  
DisplayString, TruthValue  
FROM **SNMPv2-TC**  
TcChassisType  
FROM **PAN-GLOBAL-TC**  
panModules, panCommonMib  
FROM **PAN-GLOBAL-REG**;

### SNMP probe fails to return information

A packet capture tool, such as Wireshark, can assist with troubleshooting if the issue is caused either by the MID server not sending a request to the SNMP agent or by the agent failing to respond to the request. This example shows an expected **get-request** and **get-response** for the sysObjectID (OID value 1.3.6.1.2.1.1.2): 

![The screenshot shows an shows an expected get-request and get-response for the sysObjectID (OID value 1.3.6.1.2.1.1.2)](/sys_attachment.do?sys_id=478d3b5597a14f14dfd73dae2153af1f)

You can also filter the packet capture by the sysObjectID by using its OID:

snmp.name==1.3.6.1.2.1.1.2

Notice that SNMP runs over UDP, therefore it's up to SNMP to handle the confirmation of a sent packet, therefore it is important that **request-id** in both request & response are the same when making the above analysis.

In the event that no SNMP requests are sent from the MID server check the items below:

-   OIDs in the probe are active=false
-   A column's name for a table is not there or has a typo

By using a MIB browser, we can easily visualize the items under a particular table, their OID names, values, and source MIB file: 

![](MIB%20explorer.pngx)![](MIB%20explorer.pngx)![The screenshot showcases easy ways to visualize the items under a particular table, their OID names, values, and source MIB file](sys_attachment.do?sys_id=3a8d3b5597a14f14dfd73dae2153af19) 

### SNMP classification not working

The user runs Discovery against an SNMP enabled device, but no CI is created or a CI is created, but it's not classified correctly. Although Discovery supports a wide range of SNMP devices in the base system, the list is finite. If the device you want to discover is not included in the base system you can create your own SNMP classifier. Below is a brief summary of how you can create this classifier:

1.  Navigate to Configuration -> CI Class Manager and create a new table extended from the hardware table.  
    1.  Add a child class to the class you want to extend, cmdb\_ci\_hardware in this case.
    2.  Name the new table and edit the fields as appropriate.
2.  Navigate to Discovery Definition -> CI Classification -> SNMP -> New.
3.  Name the new SNMP Classifier.
4.  Select the extended table you created from the step above and save the record.
5.  Under SNMP OID Classifications, ensure you have an SNMP OID Classification record with the OID of the device you want to run SNMP Discovery against. This will be the sysObjectId. Also select the Table, Manufacturer, and Model as appropriate
6.  Select the Table, Manufacturer, and Model as appropriate
7.  Under Trigger probes, make sure that SNMP - Identity is selected and the phase is set to Identification. You can also include your custom SNMP exploration probes in this step.

For more information on how to create SNMP Classifiers, see "Create a Discovery CI classification" in the product documentation.

If classification already exists but correct OID is not configured then the wrong classification will occur. In this case, add the OID to the existing classification.

### SNMP credential not working

Use "Test credentials" to ensure the credential has been configured properly. You can also use Wireshark to ensure that the correct credential is being sent out.

[Views](https://tools.ietf.org/html/rfc3415 "Views") are more commonly implemented in SNMPv3. In case views are configured on your SNMP agent, ensure that view configuration is not blocking access to the target OIDs. For more information about SNMPv3 Views please consult your SNMP agent documentation.

For SNMP related detail error, you need to add a entry in wrapper-override.conf (<mid\_agent\_folder>/conf/wrapper-override.conf) file like below:

wrapper.java.additional.201=-Dsnmp4j.LogFactory=com.service\_now.mid.extension.trap.Snmp4j2DiscoLogFactory
