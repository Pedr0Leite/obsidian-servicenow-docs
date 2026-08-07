---
title: "Discovery: Deep Dive - SNMP classification capabilities and properties"
aliases:
  - KB0598507
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0598507
kb_number: KB0598507
last_modified: 2025-09-10
---

## Issue

Discovery: Deep Dive - SNMP classification capabilities and properties

  

  

<table class="tocTable" width="375"><tbody><tr><td>style="text-decoration: none;" name="toc"&gt;<span class="hd1">Table of Contents</span></td></tr><tr><td><span style="color: #888888;"><a style="text-decoration: none;" href="#overview"><span style="color: #888888;">1. Overview</span></a></span></td></tr><tr><td><span style="color: #888888;"><a style="text-decoration: none;" href="#capabilities"><span style="color: #888888;">2. Capabilities</span></a></span></td></tr><tr><td style="padding-left: 30px;"><span style="color: #888888;"><a style="text-decoration: none;" href="#discover"><span style="color: #888888;">discover</span></a></span></td></tr><tr><td style="padding-left: 30px;"><span style="color: #888888;"><a style="text-decoration: none;" href="#hosting"><span style="color: #888888;">hosting</span></a></span></td></tr><tr><td style="padding-left: 30px;"><span style="color: #888888;"><a style="text-decoration: none;" href="#printing"><span style="color: #888888;">printing</span></a></span></td></tr><tr><td style="padding-left: 30px;"><span style="color: #888888;"><a style="text-decoration: none;" href="#switching"><span style="color: #888888;">switching</span></a></span></td></tr><tr><td style="padding-left: 30px;"><span style="color: #888888;"><a style="text-decoration: none;" href="#blockswitchexploration"><span style="color: #888888;">block switch exploration</span></a></span></td></tr><tr><td style="padding-left: 30px;"><span style="color: #888888;"><a style="text-decoration: none;" href="#vlans"><span style="color: #888888;">vlans</span></a></span></td></tr><tr><td style="padding-left: 30px;"><span style="color: #888888;"><a style="text-decoration: none;" href="#routing"><span style="color: #888888;">routing</span></a></span></td></tr><tr><td style="padding-left: 30px;"><span style="color: #888888;"><a style="text-decoration: none;" href="#blockrouterexploration"><span style="color: #888888;">block router exploration</span></a></span></td></tr><tr><td style="padding-left: 30px;"><span style="color: #888888;"><a style="text-decoration: none;" href="#hintrouter"><span style="color: #888888;">hint router</span></a></span></td></tr><tr><td style="padding-left: 30px;"><span style="color: #888888;"><a style="text-decoration: none;" href="#powering"><span style="color: #888888;">powering</span></a></span></td></tr><tr><td style="padding-left: 30px;"><span style="color: #888888;"><a style="text-decoration: none;" href="#mfrapc"><span style="color: #888888;">mfr apc</span></a></span></td></tr><tr><td style="padding-left: 30px;"><span style="color: #888888;"><a style="text-decoration: none;" href="#powerdistribution"><span style="color: #888888;">power distribution</span></a></span></td></tr><tr><td style="padding-left: 30px;"><span style="color: #888888;"><a style="text-decoration: none;" href="#netware"><span style="color: #888888;">netware</span></a></span></td></tr><tr><td><span style="color: #888888;"><a style="text-decoration: none;" href="#properties"><span style="color: #888888;">3. Properties</span></a></span></td></tr><tr><td style="padding-left: 30px;"><span style="color: #888888;"><a style="text-decoration: none;" href="#sysdescr"><span style="color: #888888;">sysdescr</span></a></span></td></tr><tr><td style="padding-left: 30px;"><span style="color: #888888;"><a style="text-decoration: none;" href="#sysoid"><span style="color: #888888;">sysoid</span></a></span></td></tr><tr><td style="padding-left: 30px;"><span style="color: #888888;"><a style="text-decoration: none;" href="#ipaddress"><span style="color: #888888;">ip address</span></a></span></td></tr><tr><td style="padding-left: 30px;"><span style="color: #888888;"><a style="text-decoration: none;" href="#maker"><span style="color: #888888;">maker</span></a></span></td></tr><tr><td style="padding-left: 30px;"><span style="color: #888888;"><a style="text-decoration: none;" href="#model"><span style="color: #888888;">model</span></a></span></td></tr><tr><td style="padding-left: 30px;"><span style="color: #888888;"><a style="text-decoration: none;" href="#name"><span style="color: #888888;">name</span></a></span></td></tr><tr><td><span style="color: #888888;"><a style="text-decoration: none;" href="#references"><span style="color: #888888;">4. References</span></a></span></td></tr></tbody></table>

  

style="text-decoration: none;" name="overview">Overview

* * *

When discovering a device using SNMP (as part of the [device classification process](https://docs.servicenow.com/bundle/istanbul-it-operations-management/page/product/discovery/reference/r_DeviceClassification.html "device classification process")), you may see inside many SNMP classification records \[discovery\_classy\_snmp\]. The Classification Criteria section or tab contains conditions that must be met in order to match the specific classifier against the device being scanned. For example, the screenshot below shows the Classification Criteria record \[discovery\_class\_criteria\] for the default Standard Network Switch:

![](https://support.servicenow.com/sys_attachment.do?sys_id=39a9a062db42b450e515c22305961934)

The Triggers probes section or tab \[discovery\_classifier\_probe\] determines which probes are triggered after the Classify probe. For some probes, there are conditions set that check for some of the same values. For example, the screenshot below shows the same Standard Network Switch and if the SNMP - Routing probe is triggered:

![](sys_attachment.do?sys_id=b9a9a062db42b450e515c22305961941)

In both cases, the values are being determined from the SNMP - Classify sensor script. The values are set in arrays named capabilities and props. The values for the capabilities are determined based on the information retrieved from the SNMP - Classify probe.

  

style="text-decoration: none;" name="capabilities">Capabilities

* * *

Listed below are the capabilities that are instantiated by default in the base system version of the SNMP - Classify Sensor (beginning with the Istanbul release).

  

style="text-decoration: none;" name="discover">discover

* * *

This capability is defined in the _process_ function in the SNMP - Classify sensor script.

It is the first capability defined after setting up this capabilities array variable.

![](sys_attachment.do?sys_id=02a9a062db42b450e515c2230596195c)

The value is determined from the **Discover** field value from the Discovery Status record that is running this SNMP - Classify probe. It is based on the type of Discovery scan being run. For example, if a normal Configuration Item type scan is run, the value is Cis, or if a Web Service scan is run, the value is Web Service. The value is used, by default, to determine the probes that should not be run when certain types of scans are run.

For reference, in the Standard Network Switch Classifier, for the **Triggers Probes** records such as DNS and SNMP - Switching, one of the conditions listed in the **Conditions** field is **values.get('discover') != 'Nets'**. This means that the probe should not be run during a Network Discovery schedule.

  

style="text-decoration: none;" name="hosting">hosting

* * *

This capability is defined in the _analyze_ function of the SNMP - Classify sensor script.

![](sys_attachment.do?sys_id=8ea9a062db42b450e515c22305961964)

This value is determined from the results of the OIDs starting under the mgmt.mib-2.host.hrSystem OID.

Based on the Istanbul release, this **hosting** capability is not used in any of the Classification Criteria or Triggers Probes lists in the default SNMP Device Classifications.

The isHost value is sometimes checked later in the Sensor script as described in the [routing](#routing) capability.

  

style="text-decoration: none;" name="printing">printing

* * *

This capability is defined in the _analyze_ function of the SNMP - Classify sensor script.

![](sys_attachment.do?sys_id=cea9a062db42b450e515c22305961971)

This value is determined by the results either from the OIDs starting under the mgmt.mib-2.host.hrDevice.hrDeviceTable OID or under the mgmt.mib-2.printmib.prtGeneral.prtGeneralTable OID, if existing.

This value is mainly used for classifying a Standard Network Printer based on the Classification Criteria record that specifies to check for if "printing....equals....true."

This value is checked to see if it is false in the Standard Network Switch Classifier, because some Network Printers may have Switch type OIDs returned as well. This **printing** value can distinguish between a Printer and a Switch.

  

style="text-decoration: none;" name="switching">switching and style="text-decoration: none;" name="blockswitchexploration">block switch exploration

* * *

These capabilities are defined in the _analyze_ function of the SNMP - Classify sensor script.

![](sys_attachment.do?sys_id=5aa9a062db42b450e515c223059619aa)

The **switching** value is determined by the results from the mgmt.mib-2.dot1dBridge.dot1dBase.dot1dBaseNumPorts OID or from the OIDs under the private.enterprises.cisco.ciscoMgmt.ciscoVtpMIB.vtpMIBObjects.vlanInfo.vtpVlanTable OID (while also having the property glide.discovery.cisco\_switch\_community\_string\_indexing set to true).

The **block\_switch\_exploration** value is always set to false by default.

The **switching** value is checked in the following locations:

-   the Classification Criteria for Standard Network Switch to check if "switching....equals....true"
-   some Triggers probes lists (such as for triggering the SNMP - Switching probe in the Standard Network Router classification)

The **block\_switch\_exploration** value is checked by default in some of the same Triggers probes conditions where "switching == true", and also in some others where the **switching** value is not used (such as when trying to trigger the SNMP - Network - ArpTable probe in the Standard Network Switch classification).

  

style="text-decoration: none;" name="vlans">vlans

* * *

This capability is defined in the _analyze_ function of the SNMP - Classify sensor script.

![](sys_attachment.do?sys_id=d6a9a062db42b450e515c223059619cd)

This value is determined by the results from the OIDs starting under the mgmt.mib-2.interface.ifTable OID and is only checked if isSwitch is set as true.

Based on the Istanbul release, this **vlans** capability is not used in any of the Classification Criteria or Triggers Probes lists in the default SNMP Device Classifications.

  

style="text-decoration: none;" name="routing">routing and style="text-decoration: none;" name="blockrouterexploration">block router exploration

* * *

These capabilities are defined in the _analyze_ function of the SNMP - Classify sensor script.

Following is the first location where both the **routing** and the **block\_router\_exploration** capabilities can be set.

![](sys_attachment.do?sys_id=5aa9e062db42b450e515c22305961948)

In this segment, the **routing** value is determined by the results from the OIDs starting under the mgmt.mib-2.ip OID.

The **block\_router\_exploration** value is always set as false by default.

This second location is an alternate place where just the **routing** capability could also be set based on other values being set or not. 

![](sys_attachment.do?sys_id=a6a9e062db42b450e515c22305961954)

In here, the **routing** value could also be set as true if none of the other capability values are set as true and if the forwarder value (set from the previous snippet) is set as 1.

The **routing** value is checked in both the Classification Criteria for the Standard Network Router Classification and also in some Triggers probes lists, such as triggering the SNMP - Routing probe in the Standard Network Switch classification.

The **block\_router\_exploration** field is used by default in some of the same Triggers probes conditions where "routing == true," such as for triggering the SNMP - Routing probe in the Standard Network Switch and Standard Network Router classifications.

  

style="text-decoration: none;" name="hintrouter">hint\_router

* * *

This capability is defined in the analyze function of the SNMP - Classify sensor script.

![](sys_attachment.do?sys_id=eea9e062db42b450e515c2230596195e) 

This value is initially set as true and is only changed to false if all of the following are true:

-   isRouter is true (as detailed in the routing section)
-   there are interfaces under the mgmt.mib-2.interface.ifTable OID
-   if any of the ifType values for any of these interfaces has a value that matches one of the values listed in the switchIntMap list (defined earlier in the analyze function)

Based on the Istanbul release, the **hint\_router** capability is not used in any of the Classification Criteria or Triggers Probes lists in the default SNMP Device Classifications.

  

style="text-decoration: none;" name="powering">powering, style="text-decoration: none;" name="mfrapc">mfr\_apc, and style="text-decoration: none;" name="powerdistribution">power\_distribution

* * *

These capabilities are defined in the _analyze_ function of the SNMP - Classify sensor script.

![](sys_attachment.do?sys_id=e6a9e062db42b450e515c22305961978) 

The **powering** value is determined based on the isUPS or isAPC variable values. If either of these values are set as true, then **powering** is set as true. If both are false, then **powering** is set as false.

The **mfr\_apc** value can be set to true in one of two ways:

-   if isAPC is set as true
-   if isAPC is false and isAPCPDU is true

The **power\_distribution** value is solely based on the isAPCPDU value.

The **powering** value is checked in both the Classification Criteria for the Standard UPS Classification and also in some Triggers probes lists, such as for triggering the SNMP - UPS or SNMP - APC UPS probe in the Standard UPS classification.

The **mfr\_apc** value is checked in both the Classification Criteria for the PDU Classification and also in some Triggers probes lists, such as for triggering the SNMP - UPS or SNMP - APC UPS probe in the Standard UPS classification.

The **power\_distribution** value is checked in the Classification Criteria for the PDU Classification.

  

style="text-decoration: none;" name="netware">netware

* * *

This capability is defined in the _analyze_ function of the SNMP - Classify sensor script.

![](sys_attachment.do?sys_id=a6a9e062db42b450e515c2230596198c)

This value is determined if there is any result in the payload from the novell.mibDob.nwServer.nwSystem.nwSysServerName OID.

The **netware** value is checked in the Classification Criteria for the Netware Classification.

  

style="text-decoration: none;" name="properties">Properties

* * *

Listed below are the additional **props** (properties) values that are instantiated by default in the base system version of the SNMP - Classify Sensor (beginning with the Istanbul release).

style="text-decoration: none;" name="sysdescr">sysdescr

* * *

This property is defined in the _analyze_ function of the SNMP - Classify sensor script.

![](sys_attachment.do?sys_id=2ea9e062db42b450e515c22305961995)

This value is based on the mgmt.mib-2.system.sysDescr OID.

This **sysdescr** value is checked in several Classification Criteria records (however, as of Istanbul, the only active records using it are Firewall and Cisco GSS Load Balancer) and also in some Triggers probes lists, such as for triggering the SNMP - HP Printer Model probe in the Standard Network Printer classification.

  

style="text-decoration: none;" name="sysoid">sysoid

* * *

This property is defined in the _analyze_ function of the SNMP - Classify sensor script.

![](sys_attachment.do?sys_id=f2a9e062db42b450e515c2230596199d)

This value is based on the mgmt.mib-2.system.sysObjectID OID.

Based on the Istanbul release, this **sysoid** property is not used in any of the Classification Criteria or Triggers Probes lists in the default SNMP Device Classifications.

However, this value is later referenced in the getClassifier function in this sensor script to see if a match can be made to a record in the discovery\_snmp\_oid table.

  

style="text-decoration: none;" name="ipaddress">ip\_address

* * *

This property is defined in the _analyze_ function of the SNMP - Classify sensor script.

![](sys_attachment.do?sys_id=baa9e062db42b450e515c223059619a4)

This value is set based on the IP on which the SNMP - Classify probe is run against.

Based on the Istanbul release, this **ip\_address** property is not used in any of the Classification Criteria or Triggers Probes lists in the default SNMP Device Classifications.

  

style="text-decoration: none;" name="maker">maker and style="text-decoration: none;" name="model">model

* * *

These properties are defined in the _analyze_ function of the SNMP - Classify sensor script.

 ![](sys_attachment.do?sys_id=f6a9e062db42b450e515c223059619ab) 

  .............

![](sys_attachment.do?sys_id=faa9e062db42b450e515c223059619be)

Both of these values are initially set as null and can only obtain a potential value based on any existing values for the mgmt.mib-2.entityMIB.entityMIBObjects.entityPhysical.entPhysicalTable OID Table _._

The **maker** value can be set based on the first value that can be found in the entPhysicalMfgName OID_._

The **model** value can be set based on the first value that can be found in the entPhysicalModelName OID_._

Based on the Istanbul release, these **maker** and **model** properties are not used in any of the Classification Criteria or Triggers Probes lists in the default SNMP Device Classifications.

However, these values are later referenced in the runClassifier function in this sensor script to potentially determine the manufacturer and model values for the device being scanned.

  

style="text-decoration: none;" name="name">name

* * *

![](sys_attachment.do?sys_id=b6a9e062db42b450e515c223059619d1) 

 .............

![](sys_attachment.do?sys_id=f2a9e062db42b450e515c223059619d8)

This value is initially set as null and can only obtain a potential value based on an existing value for the mgmt.mib-2.system.sysObjectID OID.

This **name** value is then formatted based on several criteria, such as:

-   if the domain should be included or not
-   if the value should be set to all uppercase or lowercase (based on the properties glide.discovery.hostname.include\_domain and glide.discovery.hostname.case - for more information, see [Configure Discovery Properties](https://docs.servicenow.com/bundle/istanbul-it-operations-management/page/product/discovery/reference/r_DiscoveryProperties.html "Configure Discovery Properties") in the product documentation).

Based on the Istanbul release, this **name** property is not used in any of the Classification Criteria or Triggers Probes lists in the default SNMP Device Classifications.

However, this **name** property is later referenced in the runClassifier function in this sensor script and is passed into the ci\_data array for setting the name of the device.

style="text-decoration: none;" name="references">References

* * *

-   [Discovery Device Classification](https://docs.servicenow.com/bundle/istanbul-it-operations-management/page/product/discovery/reference/r_DeviceClassification.html "Discovery Device Classification")
-   [Discovery Classification Parameters](https://docs.servicenow.com/bundle/istanbul-it-operations-management/page/product/discovery/concept/c_DiscoClassificationParam.html "Discovery Classification Parameters")
-   [SNMP Parameters for Discovery](https://docs.servicenow.com/bundle/istanbul-it-operations-management/page/product/discovery/reference/r_SNMPParameters.html "SNMP Parameters for Discovery")
