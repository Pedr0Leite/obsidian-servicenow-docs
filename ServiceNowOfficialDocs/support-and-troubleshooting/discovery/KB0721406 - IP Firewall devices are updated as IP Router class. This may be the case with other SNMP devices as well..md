---
title: "IP Firewall devices are updated as IP Router class. This may be the case with other SNMP devices as well."
aliases:
  - KB0721406
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0721406
kb_number: KB0721406
last_modified: 2024-04-07
---

## IP Firewall devices are updated as IP Router class. This may be the case with other SNMP devices as well.

  

### Issue

# Symptoms

* * *

Firewall devices that are already discovered would be reclassified as Routers. This may be the case with other SNMP based devices.

Also, SNMP-Classify system OID information.

# Cause

* * *

sysObjectOID is primarily used for SNMP device classification. If sysObjectOID is not returned in the SNMP-Classify input payload or not been added to the SNMP OID list, then "SNMP-Classify" sensor would scan through some of the input payload OIDs to construct some capabilities ( ex : routing, printing, switching, etc to name a few ) which would then be used to classify a device further.

During this phase, sometimes sysObjectOID is not returned due to timeout and this may lead to the device classification based on the capabilities.

Missing sysObjectOID may look like this. All other OIDs are present, but the systemObjectOID is missing.

<system oid="1.3.6.1.2.1.1">   
<sysName oid="1.3.6.1.2.1.1.5" type="SnmpOctetString">apcfwven1b</sysName>   
<sysUpTime oid="1.3.6.1.2.1.1.3" type="SnmpTimeTicks">1043305934</sysUpTime>   
<sysDescr oid="1.3.6.1.2.1.1.1" type="SnmpOctetString">   
IPSO apcfwven1b 6.2-GA083a02 releng 1 08.15.2013-191852 i386   
</sysDescr>   
</system> 

# Resolution

* * *

Add "request\_interval" snmp probe parameter with a greater value and see if this fetches the sysObjectOID. If this OID is returned and present in the SNMP OID list, the device should be classified accordingly.
