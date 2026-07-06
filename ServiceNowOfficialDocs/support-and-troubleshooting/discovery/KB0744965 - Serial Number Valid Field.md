---
title: "Serial Number Valid Field"
aliases:
  - KB0744965
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0744965
kb_number: KB0744965
last_modified: 2025-11-19
---

## Serial Number Valid Field

  

### Issue

Serial number's valid field set to false after discovery.

### Release

All currently supported releases.

### Cause

The default value for cmdb\_serial\_number.valid is "false". Discovery, or any other source creating such CIs, must set valid = true before creating/updating a serial number. Discovery calls SncSerialNumber() with a list of serial numbers to determine if the serial numbers are valid or not.

SncSerialNumber sets the serial numbers to active. Then iterates through a set of conditions to determine if this serial number should be set to invalid. The condition to determine if a serial number is "valid = false" are:

1.  Serial number is empty.
2.  Serial number is composed of the same repeating character.
3.  Serial number meets any of the conditions listed under dscy\_invalid\_serial.

### Resolution

If discovered/created via an Out-of-Box probe/sensor or pattern the SncSerialNumber should be called and properly set the serial number valid field accordingly.

If discovered/created via a probe/sensor, pattern, or any other sources which are not Out-of-Box the SncSerialNumber may not be called to set the field valid to true. The field value will be set to false since the default value for this field is false. The resolution will depend on how the CI is being created.

**Discovery Probe/Sensor:**

1.  Ensure the sensor properly calls SncSerialNumber to set the valid field to true for each serial number. Review the Out-Of-Box "Windows - Hardware Information" sensor for an example.

**Discovery Pattern:**

1.  Patterns set the valid field to true via "Pre Post Processing" scripts. Review "Windows OS - Pre Sensor" for an example. Validate serial number via a pre postscript, "Pattern Designer > Pre Post Processing" (sa\_pattern\_prepost\_script). 

**Other:**

1.  Use SncSerialNumber to validate serial numbers before inserting them into the CMDB.

**SncSerialNumber being called appropriately or Out-of-Box discovery:**

1.  Check if the serial number meets one of the conditions found on table dscy\_invalid\_serial. If so, the serial number will be considered invalid (valid = false).

### Related Links

[Serial number types for identification](https://docs.servicenow.com/csh?topicname=r_SerialNumberTypes.html&version=latest "Serial number types for identification")
