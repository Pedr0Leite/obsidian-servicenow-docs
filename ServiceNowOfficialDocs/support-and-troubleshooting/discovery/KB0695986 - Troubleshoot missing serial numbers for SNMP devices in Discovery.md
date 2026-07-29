---
title: "Troubleshoot missing serial numbers for SNMP devices in Discovery"
aliases:
  - KB0695986
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695986
kb_number: KB0695986
last_modified: 2026-03-09
---

## Troubleshoot missing serial numbers for SNMP devices in Discovery

  

### Issue

Discovery **Identification is done primarily based on the Serial Number** extracted from the device by our probes. If that fails we fall back to name and IP address, however names are often not unique and IP address move about. That means **if a device does not return a Serial Number then there is a real chance of mis-identification**, leading to the wrong CI being updated or duplicate CIs being created.

You may also see CIs created without Serial Numbers. 

This article covers common causes and resolutions for missing serial number data.

### Release

All Supported Releases

### Cause

Missing serial numbers can result from various factors, including missing SNMP credentials, probe failures, or other issues.

### Resolution

## Missing Credentials

Discovery SNMP probes can fall back to using the Public community string if none of the SNMP Credentials entered in the instance give access to the device.

However some devices may limit what can be read using the Public community string.

**Solution**:

Ensure SNMP devices are configured to allow Public community string access to identification data, or set up the device with a new credential and also add that credential to the instance. 

## Probes Time-Out before receiving the data

Some SNMP-enabled network devices are very simple embedded microcontroller implementations, which are slow. e.g. PDUs, UPSs. They do give serial number data, but sometimes time-out before they have. 

More advanced fast devices such as L2 Switches will be running the SNMP interface code in the same multi-tasking CPU as functional switch code, and under high load the SNMP thread may not respond very quickly or pass the data back very fast. This has been seen with big Cisco Switches, and others.

This causes 2 main problems:

1.  The Probe times out because **no data at all was received** before the Probe timeout. The Sensor will Error in this situation, and Identification will fail.
2.  Data was received before we time out the probe, **but it was incomplete**. As SNMP is based on UDP, it is hard to detect this situation, and we may not realize we only received partial data back from the device. This can also be the case for big devices that have a lot of data to transfer, such as Cisco Switches with huge routing tables.   
    We will then continue to run the Classify and Identify sensors with incomplete data, missing the key Serial Number information.

**Solution**:

Once you have identified devices that can be slow to respond, you can **incrementally increase the SNMP Probe timeouts until the issues are resolved**. These MID Server Parameters can be used to configure the SNMP probes. More details on these are in the documentation for 'MID Server Parameters' or 'SNMP probe parameters':

-   **mid.snmp.request.timeout** - Maximum time to wait for a response for the first OID request
-   **mid.snmp.session.timeout** - Maximum time to wait for responses to OID requests once a session has been established.
-   **timeout** and **established\_session\_timeout** are Probe Parameters, that will override the above two MID Server Parameters, but for a Specific Probe, such as "SNMP - Classify" or "SNMP - Identity". These would then apply to Discovery via any MID Server.

## SNMP implementation does not include the standard serial number OIDs

Devices known not to return a serial number include some Printers, and there are bound to be other types of devices as well. 

You can confirm this by looking at the ECC Queue input record for the Identity probe. The OIDs may not be there, or have empty values.

**Solutions**: 

There is not a lot ServiceNow can do about this, other than report this to the manufacturer of the device. So long as the device returns a unique name, IP address and MAC address then we have enough data to do the identification.

If the IP has been used before and is still linked with another CI in the CMDB then clearing the IP address information from the main CI, Network Adapter, and IP Address CIs for the old device will allow Identification based on the IP to work.

If the device has a generic Name as well, e.g. "AFICIO MP 2550" or "RACKPDU", then you may have to manually add the CI, or customize the Identifiers, after which discovery can then match the CI and update the additional fields.

## The device has Serial Number data available but there is no current probe to fetch it

Depending on the device type and manufacturer, and which standard or vendor MIBs are implemented, serial number data could be in various OIDs. e.g. sysSerialNumber, prtGeneralSerialNumber, chassisSerialNumberString, entPhysicalSerialNum, etc.

We have out-of-box Probes and Sensors for most standard device types, and some specific manufacturers such as Cisco, but we may miss some.

**Solution**:

It would be possible to **write custom Probes/Sensors** in this situation. It may be required to first add a new MIB from the device vendor to the instance MIB table, before then writing a Sensor to fetch specific OIDs from that MIB, and then write a Sensor to take that data and update the CI.

For common devices it would be very useful if you were to **create an Enhancement Request in HI** with details of the device and where the serial number data is in the SNMP MIBs and OIDs. Our developers would then have the opportunity to write out-of-box code that is aware of the device.

## The Sensor failed to process the data

It is also possible that data returned by the probes has unexpected data, formatting, or extended characters, that the Sensor fails to parse and process. There may even be an Error or exception thrown by the Sensor.

**Solution**:

If you have already confirmed that the ECC Queue input record does include the full SNMP data including serial numbers, then there may be a problem with the sensor code, and it may be necessary to open a Support Incident in HI.

## Shazzam did not launch SNMP - Classify probe

SNMP is a UDP protocol, which has a major drawback for Discovery. Unlike TCP, it is not possible to know if the device is there unless you get a result back from a real SNMP query, and even then we cannot be sure we have all the data. Shazzam does the SNMP port probe by requesting the sysObjectID OID (prior to New York this was sysDescr), and if a value is not returned for that then the "SNMP - Classify" or "SNMP - Identity" probes will not even run.
