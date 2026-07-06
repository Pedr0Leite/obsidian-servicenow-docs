---
title: "LDAP URL endpoints go up and down on a regular basis when using a VPN"
aliases:
  - KB0748737
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748737
kb_number: KB0748737
last_modified: 2026-05-05
---

## LDAP URL endpoints go up and down on a regular basis when using a VPN

  

### Issue

There are LDAP URL endpoints configured that traverse a VPN. Thess will most likely been seen when there is more than one LDAP Server URL configured, where one URL will be considered the primary LDAP URL and the others secondary.

The secondary URL endpoints will be seen to go down in the LDAP Log several times a day:

2019-04-22 10:20:04 Error LDAP Server: LDAP1 URL: ldap://xxx.xxx.xxx.xxx:389/ failed scheduled connection test. ErrorCode: 10301. ErrorMessage: Connection timed out, failed to connect to server. 

They will come up as well showing this message:

2019-04-22 11:04:01  Information LDAP Server: LDAP1 URL: ldap://xxx.xxx.xxx.xxx:389/ ErrorCode: 0. ErrorMessage: Connected successfully. Server Operational Status is true.

But then they would go down again, and this cycle is seen several times a day.

### Symptoms

g

### Release

N/A

### Cause

The VPN used to connect to LDAP URLs has Dead Peer Detection (DPD) configured.

As the LDAP connection failures are seen mostly on what are considered secondary LDAP URLs, this is because the traffic across those URLs is usually very low, and the DPD has determined the low traffic indicating that those endpoints are down, which leads to those connections being taken down.

DPD detection will depend on how aggressively it is setup on the VPN. Note that on the ServiceNow VPN side, DPD is never activated on our VPNs.

### Resolution

Turn off Dead Peer Detection on the customer instance side of the VPN. Doing this will match what ServiceNow has configured on our side of the VPN tunnels.
