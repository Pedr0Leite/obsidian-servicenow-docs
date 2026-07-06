---
title: "Discovery fails to classify SNMP device with \"Active, couldn't classify\" error"
aliases:
  - KB0758145
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0758145
kb_number: KB0758145
last_modified: 2026-03-06
---

## Discovery fails to classify SNMP device with "Active, couldn't classify" error

  

### Issue

Troubleshoot Discovery classification failures for SNMP devices that return an "Active, couldn't classify" error. This issue occurs when the device's SNMP Object Identifier (OID) is missing from the SNMP System OIDs CI Classification table, even when valid credentials and Management Information Base (MIB) configurations are in place.

### Release

All Supported Releases

### Cause

The device SNMP OID is not present in the SNMP System OIDs CI Classification table. Discovery requires a matching OID entry in this table to classify the device into the correct Configuration Item (CI) class.

### Resolution

### Confirm the SNMP OID in the Discovery payload

1.  Run a quick Discovery against the device.
2.  Open the Discovery status record and go to the ECC Queue output for the SNMP classification probe.
3.  In the input payload, verify that the sysObjectID value is captured with the device details. The payload resembles the following example:

<system oid="1.3.6.1.2.1.1">   
<sysName oid="1.3.6.1.2.1.1.5" type="SnmpOctetString">SAlla\_TK\_sw7</sysName>   
<sysUpTime oid="1.3.6.1.2.1.1.3" type="SnmpTimeTicks">753833700</sysUpTime>   
<sysDescr oid="1.3.6.1.2.1.1.1" type="SnmpOctetString">   
**ExtremeXOS (X440G2-48t-10G4) version 21.1.0.17 21.1.0.17 by release-manager on Thu Nov 5 18:06:44 EST 2015**   
</sysDescr>   
<sysObjectID oid="1.3.6.1.2.1.1.2" type="**SnmpObjectId**">.**1.3.6.1.4.1.1916.2.221**</sysObjectID>   
</system>

In this example, the OID value is `.1.3.6.1.4.1.1916.2.221`.

### Add the missing OID to the classification table

1.  Go to Discovery > CI Classification > SNMP System OIDs.
2.  Check whether the OID from the payload exists in the table.
3.  If the OID is missing, select New to create a record and enter the device OID and corresponding CI class.
4.  Select Submit to save the record.

![](sys_attachment.do?sys_id=c950745c97af3e5485e13bbe2153af4a)

### Verify classification

1.  Re-run Discovery against the device.
2.  Confirm that the CI is classified correctly and the record is created.

### Related Links

[Load a MIB module](https://www.servicenow.com/docs/r/it-operations-management/discovery/t_LoadAMIBModule.html "Load a MIB module")
