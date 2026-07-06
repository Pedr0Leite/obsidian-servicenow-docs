---
title: "Turning off Network Device Exploration in the Discovery Configuration Console causes the Network Switch/Router pattern to fail"
aliases:
  - KB0747592
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0747592
kb_number: KB0747592
last_modified: 2024-04-07
---

## Turning off Network Device Exploration in the Discovery Configuration Console causes the Network Switch/Router pattern to fail

  

### Issue

# Overview

Turning off Network Device Exploration in the Discovery Configuration Console causes the Network Switch/Router pattern to fail.

# Subject

When the Network Device Exploration is turned off in the Discovery Configuration Console as shown in the below screenshot

![](sys_attachment.do?sys_id=491b682adb42b450e515c22305961915)

The shared libraries such as SNMP - Switching, SNMP - Switch - Vlan, SNMP - Routing, SNMP - ARP Table, SNMP - CDP and LLDP, SNMP - IP Device Handler will be inactive while debugging the pattern and the steps in the libraries are not executed while running discovery. This causes the Network Switch/Router pattern to fail as the steps dependent on the libraries mentioned above will fail.
