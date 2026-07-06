---
title: "SNMP Trap Listener error: \"The MID Server does not contain a MID Server member. The extension with the sys_id <SNMP_Extension_SYS_ID> is not currently active.\""
aliases:
  - KB0744271
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0744271
kb_number: KB0744271
last_modified: 2024-04-07
---

## Issue

# Symptoms

Resolving error "The MID Server does not contain a MID Server member" while configuring the SNMP Trap Listener.

SNMP Trap Listener error "The extension with the sys\_id <SYS\_ID> is not currently active"

![](sys_attachment.do?sys_id=d9a96062db42b450e515c223059619c7)

# Release

All Releases

# Cause

The error occurs when the MID Server has unresolved issues. The MID Server does not have any applications in the supported application which needs tp be configured. On the MID Server Host machine the MID Server service and SNMP service gets stuck due to which the MID Host System needs to be restarted.

# Resolution

1.  In instance from filter navigator goto MID Server > MID SNMP Trap Listener
2.  Open the collector record and check the MID Server  
    **Note**: Verify the UDP port information for listener to make sure right port number is used.
3.  Goto configured MID Server for this trap listener
4.  In the related tabs select tab Support Application
5.  Click on edit to support ALL applications
6.  Log on to the MID Server host system
7.  Open services and look for MID Server service
8.  Make sure it is not stuck
9.  Restart the MID Server  
    **Note:** Collector service when stuck may require to restart the entire Host System.
10.  Make sure MID Server service along with SNMP service is running on MID Server Host System

After following the steps, the error should be resolved.
