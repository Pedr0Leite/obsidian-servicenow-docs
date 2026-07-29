---
title: "SNMP Discovery explained"
aliases:
  - KB0752582
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0752582
kb_number: KB0752582
last_modified: 2025-06-24
---

## SNMP Discovery explained

  

### Issue

Looking for more insight about how SNMP Discovery works? This article provides in-depth information about prerequisites, flow, and common troubleshooting steps.

### Release

All

### Resolution

-   [Prerequisites](#HEADING_1)
-   [MID Server capabilities and requirements](#HEADING_2)
-   [SNMP Discovery Flow in a base system](#HEADING_3)
-   [Common issues and how to investigate](#HEADING_4)

### Prerequisites 

-   **SNMP Version:** This is one critical check that has to be verified for the target host.   
    -   ServiceNow Discovery supports SNMP versions 1, 2c and 3.
    -   Discovery uses version 1 and 2c by default.
    -   The support for version 3 must be explicitly enabled.
    -   MID Servers support all SNMP protocol versions by default.
    -   You can also set a MID Server to only support specific versions of SNMP.

-   **Credentials** - Credentials for SNMP do not include a user name, just a password, called the community string.  
    -   The default read-only community string for many SNMP devices is public, and Discovery will try that automatically.
    -   Enter the appropriate SNMP credentials if they differ from the public community string.

### MID server capabilities and requirements

No additional capability needs to be verified for running discovery on SNMP devices. The MID should just have the ability to perform DISCOVERY.

### SNMP Discovery Flow in a base system

-   ServiceNow's discovery process has the capability to discover devices managed by SNMP. A few example devices-  
    -   Switches (Stacked switches as well starting Kingston)
    -   Routers
    -   Printers
    -   Controllers of Wireless Access Points
    -   Load Balancers
-   The Discovery process uses **MIB**s and **OID**s to Classify, Identify and Explore Network-enabled devices.  
    -   **MIB -** **M**anagement **I**nformation **B**ase is like a database that contains a set of Values, both statistical and control, that are defined by the network device. Device vendors also have a choice to choose the MIBs which are referred to as private MIBs.
    -   **OID - O**bject **I**dentifier is a representation followed by the SNMP implementation which is a combination of MIB + Object of Interest. The Object of interest can be defined as the parameter value which a polling device can look for, say for example the Devices' uptime.
    -   Say, for example, a Device has OID = 1.3.6.1.2.1.1.3.0. The image below shows an example of how it adds up. The first 7 digits represent the MIB while the last 2 digits represent the Object of Interest.  
        ![The first 7 digits represent the MIB while the last 2 digits represent the Object of Interest.](/sys_attachment.do?sys_id=6227fb0293d2ae18080af35d6cba1082)
-   Quick brief of discovery phases
    -   **Shazzam or Scan phase** - For the user-provided IP address, the Shazzam polls the device and checks the port(s) it's responding on. Say, in our scenario, the expected port to be responding for the device is **161**. There are all chances that an organization might have customized the port on which SNMP runs and hence, it has to be duly checked.
    -   **Classification phase -** For any active port, the **port probes** module will have the set of probes or Patterns to be triggered and for SNMP devices it's usually **SNMP - Classify**. This probe mainly aims at extracting valid OID from the target device. The Input payload for **SNMP - Classify** looks like the example image below.

![The 'sysDescr' tags define the type of device. The 'sysObjectID' tag contains the OID.](/sys_attachment.do?sys_id=ba273f0293d2ae18080af35d6cba10f8)

-   -   -   -   -   **The 'sysDescr' tags define the type of device**
                -   **The 'sysObjectID' tag contains the OID.**
            -   Device classification is handled by the SNMP discovery process in the below way  
                -   There would be specific SNMP classifiers for that are defined for each device type. They can be found under the table **discovery\_classy\_snmp**.
                -   For each classifier, you would find the **classification criteria**. This section/tab contains the condition that a target host has to satisfy in order to trigger a relevant classifier. All the different classification criteria records can be looked under **discovery\_class\_criteria**. The fetched OID would also be taken into consideration (If the OID exists in SNMP OID table and if it doesn't, even then the classification proceeds but the conditions of all available classifiers would be checked) for choosing the right classifier and the list of OIDs that which are defined and mapped to a classifier, found under the tab **SNMP OID Classifications.** All the OID specific information can be found under **discovery\_snmp\_oid**.
                -   Once the right classifier is chosen, the probe that has to be triggered based on the condition match during classification would be defined under '**Trigger probes**' section and they can also be viewed under **discovery\_classifier\_probe**.
                -   Below is an example SNMP classifier record for Standard Network router.  
                    ![An example SNMP classifier record for Standard Network router where the Classification Criteria for the Name field is 'routing' equals true.](sys_attachment.do?sys_id=7e27ff0293d2ae18080af35d6cba10ab)
        -   **Identification phase**\- Per the obtained MIB, the classification phase feeds the Identification phase with the type of device and the necessary **probes/patterns** which are needed to be triggered to identify the device. The MIB of the target host gets polled to extract the **object(s) of interest** which in turn would be the details that are expected to be populated for the CI. In general, the SNMP MIBs are present in **ecc\_agent\_mib** table on the instance and they are expected to be compiled and loaded on the MID server on which the discovery is running from. Please note that not all MIBs are present OOTB and have to be added as per the requirement. If there is no relevant MIB, the discovery doesn't go beyond classification phase.
        -   **Exploration phase-** In the exploration phase, the target host gets further explored for obtaining internal details by triggering the Layer-2 discovery.
    -   The detailed SNMP discovery flow is outlined in the image below.

![The process flow for SNMP Discovery is outlined. The steps are also outlined in the table below.](sys_attachment.do?sys_id=b227ff0293d2ae18080af35d6cba10ae)

-   -   Following the steps in the flow image above, common issues and their possible solutions are listed in the following table.

<table style="border-collapse: collapse; width: 800px; height: 600px;" border="1"><tbody><tr style="height: 30.7969px;"><td style="width: 57.8047px; background-color: rgb(195, 195, 195); text-align: center; height: 30.7969px;"><strong>Steps</strong></td><td style="width: 136.602px; text-align: center; background-color: rgb(195, 195, 195); height: 30.7969px;"><strong>Input</strong></td><td style="width: 190.047px; text-align: center; background-color: rgb(195, 195, 195); height: 30.7969px;"><strong>Expected Output</strong></td><td style="width: 269.922px; text-align: center; background-color: rgb(195, 195, 195); height: 30.7969px;"><strong>Common issue that can be encountered</strong></td><td style="width: 175.641px; text-align: center; background-color: rgb(195, 195, 195); height: 30.7969px;"><strong>Possible solution</strong></td></tr><tr style="height: 15.3984px;"><td style="width: 57.8047px; height: 15.3984px;"><p>1.1</p><p>1.2</p><p>1.2.1</p></td><td style="width: 136.602px; height: 15.3984px;">IP of a N/W device</td><td style="width: 190.047px; height: 15.3984px;">Acknowledging the Device response on SNMP port and a go-ahead trigger SNMP - Classify</td><td style="width: 269.922px; height: 15.3984px;"><p>Issue 1: Though the SNMP port is active, a connection can be refused.</p><p>Issue 2: SSH taking priority over SNMP if the device responds on both the ports. This eventually results in SNMP being triggered.</p></td><td style="width: 175.641px; height: 15.3984px;"><p>Issue 1: Have port access enabled.</p><p>Issue 2: Create an SNMP behavior for the device and have that inherited to a discovery schedule.</p></td></tr><tr style="height: 15.3984px;"><td style="width: 57.8047px; height: 15.3984px;"><p>2.1</p><p>2.2</p><p>2.3</p></td><td style="width: 136.602px; height: 15.3984px;">SNMPTable and SNMPWalk targeting MIBs for extracting device details</td><td style="width: 190.047px; height: 15.3984px;">System OID and an extraction of condition that would let the discovery process choose the right classifier</td><td style="width: 269.922px; height: 15.3984px;">Device listed as "Active, couldn't classify"</td><td style="width: 175.641px; height: 15.3984px;">A relevant OID may be missing from discovery_snmp_OID. There may be no criteria match for any of the SNMP classifiers.</td></tr><tr style="height: 15.3984px;"><td style="width: 57.8047px; height: 15.3984px;"><p>3.1</p><p>3.1.1</p><p>3.1.2</p><p>3.2</p></td><td style="width: 136.602px; height: 15.3984px;">SNMPTable targeting to extract details like NIC and Serial numbers or a relevant pattern</td><td style="width: 190.047px; height: 15.3984px;">Device-specific details extracted from the MIB</td><td style="width: 269.922px; height: 15.3984px;"><p>Issue 1: "Classified, couldn't identify" errors</p><p>Issue 2: Pattern failures</p></td><td style="width: 175.641px; height: 15.3984px;"><p>Issue 1: Check to see if the SNMP - Identity probe succeeded. If it hasn't, investigate based on the error received.</p><p>Issue 2: Perform a pattern debug to determine the error or look at the pattern execution logs for the error.</p></td></tr><tr style="height: 15.3984px;"><td style="width: 57.8047px; height: 15.3984px;"><p>4.1</p><p>4.2</p></td><td style="width: 136.602px; height: 15.3984px;">SNMPTable targeting to extract details like the neighboring devices</td><td style="width: 190.047px; height: 15.3984px;">Several devices which are the neighbors for the N/W device and the relationship types</td><td style="width: 269.922px; height: 15.3984px;">Relationship between Device Neighbors missing</td><td style="width: 175.641px; height: 15.3984px;">The information about Device Neighbors [discovery_device_neighbors] is gathered by Layer 2 protocol cache probe during exploration. Check to see if it has been triggered or if it has errors.</td></tr></tbody></table>

**Note:** There is a flexibility to add parameters to the SNMP probe. There would be scenarios where OID Children needs to be identified and explored or a time out to be set. To understand more about how to do this, please refer to ServiceNow's documentation for [SNMP probe parameters](https://docs.servicenow.com/csh?topicname=r_SNMPProbeParameters.html&version=latest) and how to add them.

### SNMP Probe parameters  

There are additional probe parameters that can be used while discovering an SNMP device. These can be found in the table below and the [SNMP probe parameters](https://docs.servicenow.com/csh?topicname=r_SNMPProbeParameters.html&version=latest) documentation.

| Parameter | Description | Default Value |
| --- | --- | --- |
| oid\_spec\_list | A list of OID specifications, one per line. Each specification must be in one of the following two forms:
-    walk {OID}: Walks the OID and all its children
-    table {OID} {OID Children}: Walks all entries in the table, returning only the given children (for example, "iso.org.dod.internet")

{OID Children} refers to a comma-delimited list of child nodes within the entries for the given table. For example, "ifEntry.ifIndex,ifEntry.ifDescr,ifEntry.ifType" are OID children of the table "iso.org.dod.internet.mgmt.mib-2.interfaces.ifTable". As a convenience, the table entry prefix may be left off. (The preceding children could be specified as "ifIndex,ifDescr,ifType".)

Any child may include a filter qualifier in parentheses. For example, the child "entPhysicalContainedIn(=0)" specifies returning table entries only if the value of "entPhysicalContainedIn" equals 0. The operators supported in the expression are:

<table><colgroup><col><col></colgroup><tbody><tr><td>=</td><td>equals</td></tr><tr><td>!=</td><td>does not equal</td></tr><tr><td>#</td><td>contains</td></tr></tbody></table>

If more than one child has a filter expression, a match on any one of the children causes that entry to be read.

Any content including and after a "//" is ignored (comments). Any OID that does not start with "1.3.6.1" or "iso.org.dod.internet" automatically prefaces with "1.3.6.1." as a convenience.

 | required |
| source | The IP address or host name of the device to query SNMP on. | required |
| index | The index to apply after the community string, for Cisco-style community string indexing (for VLAN interrogation). | 0 |
| credential\_id | The sys\_id of a specific credential that is preferred for use above the rest. This parameter is for internal use only and is not supported. | none |
| credential\_tag | The credential tag that must be used. This parameter is for internal use only and is not supported. | none |
| timeout | 

The timeout value (in milliseconds) to wait for a response, instead of the default. You can use this parameter to override themid.snmp.request.timeout SNMP MID Server configuration parameter.

Note: When use\_getbulk is set to true, the timeout value is for an individual GETBULK request.

 | 1500 |
| established\_session\_timeout | The interval (in milliseconds) to wait for a response after at least one response has been received. Longer values can be useful for collecting complete and accurate data. You can use this parameter to override the mid.snmp.session.timeout SNMP MID Server configuration parameter. | 500 |
| debug | Enables debug logging. Set to true for debug mode. | false |
| request\_interval | The interval (in milliseconds) between successive requests for an OID when a response has not been received, until the timeout (or established\_session\_timeout) value is reached. If this value is set to at least as long as the timeout (or established\_session\_timeout) value, then only a single request is sent for any particular OID. If you change the timeout (or established\_session\_timeout) value, adjust the request\_interval at the same time to avoid sending too many or too few requests for the same OID, as appropriate for a given environment. | 400 |
| request\_delay | The interval (in milliseconds) between the receipt of a response and the transmission of the next request. The default is 0 (no delay). This value may be set to slow the overall rate of an SNMP query. | 0 |
| result\_format | Returns JSON formatted payloads for these probes:

-   SNMP - F5 BIG-IP - System
-   SNMP - Netscaler - System
-   SNMP - Routing

This parameter returns data in a more compact format to prevent sensor failure or memory problems on a node when the payload becomes large. Do not change this value or delete this parameter.

Caution: Use of this parameter with any other probes causes the sensor to fail.

 | JSON |
| use\_getbulk | 

Enables the use of SNMP GETBULK requests to retrieve tabular data from SNMP devices instead of using multiple SNMP GETNEXT requests. For tabular data, GETBULK is more efficient. Regardless of the request type, certain devices may not return any results when they are busy with other tasks.

This parameter is used to configure at the probe level. GETBULK can also be set for an individual MID Server or globally for all MID servers. Settings are listed in the order of precedence:

-   SNMP probe parameter
-   [MID Server configuration parameter](https://docs.servicenow.com/csh?topicname=mid-server-parameters.html&version=latest#d1147720e1823)
-   [MID Server properties](https://docs.servicenow.com/csh?topicname=r_MIDServerProperties.html&version=latest)

The established\_session\_timeout, request\_interval, andrequest\_delay parameters are ignored when use\_getbulk is set to true. Instead, the retries parameter is available. The timeout configuration is the same one used by use\_getscalar.

By default, the following probes use GETBULK requests (the parameter value is true).

-   SNMP - Switch - Vlan
-   SNMP - Switch - BridgePortTable
-   SNMP - Switch - ForwardingTable
-   SNMP - Switch - SpanningTreeTable
-   SNMP - Network - ArpTable
-   SNMP - Layer 2 Protocol Caches
-   SNMP - F5 BIG IP - System (only for Service Mapping customers)

Note: These probes have a timeout value of 5000.

 | false |
| use\_getscalar | Enables the use of simplified retrieval and handling of scalar values from SNMP devices.

The established\_session\_timeout, request\_interval, and request\_delay parameters are ignored when use\_getscalar is set to true. Instead, the retries and timeout parameters are available. The timeout configuration is the same one used byuse\_getbulk.

 | false |
| retries | The number of additional attempts Discovery makes to complete an individual GETBULK request (see use\_getbulk) or a GETNEXT request when the use\_getscalar parameter is set totrue. | 2 |

### SNMP sys\_properties  

**glide.discovery.L3\_mapping** - Should be enabled if the ask is to extract a logical mapping of the TCP/IP layer for network gears. This is beyond Layer 2 discovery.

### SNMP script includes 

Here are a few SNMP script includes that are useful to know

-   -   1.  **SnmpSensor**  
            1.  Retrieves the OID for the specified field name from the respective Probe for this Sensor.
            2.  Automatically trims the last object name off of Table SNMP field OIDs, for ease of use with the SNMPResponse class.
        2.  **SNMPResponse**
            1.  Wraps an SNMP payload response instance with methods to safely and easily retrieve SNMP singleton fields or tables.
        3.  **SnmpIdentityInfoParser**
            1.  Parses the **SNMP - Identity Info** MultiProbe result, adding generic NICs and serial numbers to the passed CIData object.
        4.  **SNMPNetworkInterfaces**
            1.  Handles creating network interfaces for JavaScript SNMP sensors.

### Common issues and how to investigate

-   -   -   For information about troubleshooting SNMP issues from a MID server and how to perform an SNMP walk, see [KB0696727: MID Server SNMP troubleshooting](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696727 "KB0696727").
        -   For information about the Discovery of Wireless Access Points (WAP), see [KB1511615](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1511615).

### SNMP FAQs

**Q:** Does SNMP discovery support V3 credentials?  
**A:** Yes. A credential type **SNMPv3 Credentials** can be used to configure the V3 credentials. 

**Q:** Do we support Wireless access point discovery?  
**A:** Yes if the WAP is expected to respond on SNMP. No, if its doesn't and in this case, we may have to look at targeting the controller that would be parenting the WAPs.

**Q:** Why do we see slowness while discovering SNMP devices?  
**A:** In some cases, there will be differences between debug and runtime execution because during runtime, the execution demands more OIDs. This may cause the device not to respond properly to SNMP queries because SNMP services on network devices are a low priority. In cases of inconsistency or any weird behaviour, Wireshark logs can be collected and reviewed.

### Related Links

-   [SNMP Discovery Troubleshooting](https://support.servicenow.com/nav_to.do?uri=%2Fkb_view.do%3Fsysparm_article%3DKB0720448 "SNMP Discovery Troubleshooting")
-   [MID Server and SNMP Troubleshooting](https://support.servicenow.com/nav_to.do?uri=%2Fkb_view.do%3Fsysparm_article%3DKB0696727 "MID Server and SNMP Troubleshooting")
-   [Why Did SNMP Put my SNMP Device in the Wrong Table or CI Class](https://support.servicenow.com/kb_view.do?sysparm_article=KB0693328 "Why Did SNMP Put my SNMP Device in the Wrong Table or CI Class")
-   [Discovery Deep Dive - SNMP Classification and Properties](https://support.servicenow.com/kb_view.do?sysparm_article=KB0598507 "Discovery Deep Dive - SNMP Classification and Properties")
