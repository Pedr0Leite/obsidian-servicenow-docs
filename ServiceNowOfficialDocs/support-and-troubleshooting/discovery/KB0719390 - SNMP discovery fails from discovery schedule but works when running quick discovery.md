---
title: "SNMP discovery fails from discovery schedule but works when running quick discovery"
aliases:
  - KB0719390
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0719390
kb_number: KB0719390
last_modified: 2026-05-05
---

## SNMP discovery fails from discovery schedule but works when running quick discovery

  

### Issue

SNMP Discovery from discovery schedule fails and is successful from quick discovery.

### Release

All Releases

### Cause

1.  When we run quick discovery, all the SNMP versions will be tested out against the device. This is not true in the case of discovery schedules unless we are using ALL SNMP functionality.  
      
    
2.  Customers generally select SNMPV1/V2 with schedules, this eliminates using SNMPv3 even if the device is configured to use SNMPV3.

### Resolution

Add appropriate SNMP versions to the discovery schedule. If you are not sure on the version of your devices, you can specify ALL(SNMPV1, SNMPV2, SNMPV3)
