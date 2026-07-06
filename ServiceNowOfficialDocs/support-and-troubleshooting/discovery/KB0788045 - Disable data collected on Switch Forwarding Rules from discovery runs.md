---
title: "Disable data collected on Switch Forwarding Rules from discovery runs"
aliases:
  - KB0788045
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0788045
kb_number: KB0788045
last_modified: 2025-06-26
---

## Disable data collected on Switch Forwarding Rules from discovery runs

  

### Issue

During Layer 2 Discovery, Information collected by a specific SNMP probe has the ability to create multiple CI records in CMDB for every route forwarding rule detected on a networking device.

There maybe scenarios where this behaviour of having unique CI records being created for every forwarding rule might not be desirable and considered as clutter.

  

### Release

All

### Cause

The data on the forwarding table/rules is collected by the probe "SNMP - Switch - ForwardingTable"

This probe returns information from a switch's forwarding table.

  

Discovery Definition -> Probes -> SNMP - Switch - ForwardingTable

### Resolution

In order to stop data to be collected on forwarding rules, and CI's being created we can disable the corresponding sensor reacting to the probe. 

  
Probe: SNMP - Switch - Forwarding table - https://<instance-name>.service-now.com/nav\_to.do?uri=discovery\_probes\_snmp.do?sys\_id=409d4625eb31310020ee20b6a206fe0b  
  
Sensor: SNMP Switch Forwarding table - https://<instance-name>.service-now.com/nav\_to.do?uri=discovery\_sensor.do?sys\_id=c0056676eb31310020ee20b6a206fe38
