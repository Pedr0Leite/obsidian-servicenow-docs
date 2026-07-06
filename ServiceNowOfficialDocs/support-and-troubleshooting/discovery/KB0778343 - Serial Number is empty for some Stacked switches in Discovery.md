---
title: "Serial Number is empty for some Stacked switches in Discovery"
aliases:
  - KB0778343
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0778343
kb_number: KB0778343
last_modified: 2024-10-30
---

## Serial Number is empty for some Stacked switches in Discovery

  

### Issue

Serial number field on main CI and Serial Number related list is empty for some of the stacked switches.

### Cause

On pattern step "Keep only entities that are not contained in any object" of pattern library "SNMP Identify" we filter the results of OID table entPhysicalTable (1.3.6.1.2.1.47.1.1.1.1) so that only values where entPhysicalContainedIn is 0 are kept.

![](sys_attachment.do?sys_id=4294d2cbdbc88d1080073ca8f496191e)

A serial number will not be set for the master switch when no results for the SNMP query on OID table entPhysicalTable where entPhysicalContainedIn is 0 are returned.

Run step "Get entPhysicalTable if not already polled" in pattern debug and check that the result only contains records where entPhysicalContainedIn is 1.

Example return when this is the root cause of the issue:

![](sys_attachment.do?sys_id=bce55a07db0c8d1080073ca8f496190b)

Later when the "Stacked Switches" library step "Filter entPysicalTable1 for master stack details" runs it cannot find a match as it is empty.

This issue is due to a Cisco bug described below.  
https://quickview.cloudapps.cisco.com/quickview/bug/CSCuy20251  
  
When polling entPhysicalContainedIn on the N9k, it is returning 1 instead of 0 for the stack root, when there is no entry in the table with entPhysicalIndex of 1.

### Resolution

By design, the pattern only keeps the serial number for the "root" switch when entPhysicalContainedIn==0.

To resolve the issue contact Cisco to determine if the device is affected by this bug and for a solution on how to get the device to return the appropriate value for the stack root.
