---
title: "Duplicate load balancer pool member records are created after each run of discovery when we use probes"
aliases:
  - KB0750342
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0750342
kb_number: KB0750342
last_modified: 2024-04-07
---

## Issue

# Symptoms

Duplicate load balancer pool member records are created after each run of discovery when we use probes

# Release

Any

# Cause

1) When running discovery using probes, the load balancer pool members are not identified using the regular identification engine mechanism.

2) There are identified based on the combination of the below 4 fields :

name, pool, ip address, service port

3) The index is specified in the sensor of the "SNMP - F5 BIG-IP - System" probe.

cmdb\_ci\_lb\_pool\_member: {  
index: \[ "name","pool", "ip\_address", "service\_port" \],  
childOf: { cmdb\_ci\_lb\_pool: "Members::Member of" }

4) In case, where either are these fields are not retrieved by the SNMP - F5 BIG-IP - System probe, the load balancer pool member record gets inserted each time and hence we see the duplicates

# Resolution

1) For example, if the SNMP - F5 BIG-IP - System probe fails to retrieve the name of the lb pool member, we can modify the sensor of the probe.

2) Replace

cmdb\_ci\_lb\_pool\_member: {  
index: \[ "name","pool", "ip\_address", "service\_port" \],

with 

cmdb\_ci\_lb\_pool\_member: {  
index: \[ "pool", "ip\_address", "service\_port" \],

2) Similarly you can remove the field that is not retrieved by discovery from the index and run discovery again.
