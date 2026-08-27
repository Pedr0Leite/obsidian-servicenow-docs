---
title: "Why did Discovery put my SNMP device in the wrong Table/CI Class?"
aliases:
  - KB0693328
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0693328
kb_number: KB0693328
last_modified: 2025-09-10
---

## Why did Discovery put my SNMP device in the wrong Table/CI Class?

  

### Issue

When Discovery scans a SNMP enabled device, it can sometimes mis-identify it. e.g. A Server may look to Discovery like a Printer. Or a Printer is classified as a Router. **The CI will then be inserted in or moved to the wrong CMDB table.**

### Resolution

There are many causes. Here are a few:

## A Server has SNMP enabled, and the normal SSH or WMI/Powershell/WinRM probes fail

If the normal Linux/Solaris/HP-UX or Windows identifiers fail, perhaps due to connection or credentials issues, Shazzam will fall back to using SNMP to Identify the device. Discovery may mis-identify a server as something else if OID values returned by the SNMP - Classify probe includes the clues that tell us if a device can Route, Switch, Print or other functions that may also be present in a server.

A Linux server could therefore be identified as a Router because of this. 

**Solution**: We cannot discover servers by SNMP alone, so **fix whatever is causing the SSH or WMI/Powershell/WinRM probes to fail**. The SNMP probe will then not be used.

## An HP Server has an iLO card with 'Passthrough' enabled, and the card's IP is scanned

Compaq/HP servers usually have an iLO device in them that has its own Ethernet port and IP address. This is like an independent watchdog or monitor inside the same box, and not part of "the server" from the discovery point of view.

These implement SNMP, and if they are configured for "SNMP Pass-through", then instead of reporting on itself it makes the card look like the Server instead. The SNMP results for the iLO IP address will appear to be for the server's hardware and operating system.  

e.g. the input from the 'SNMP - Classify' probe might look like one of these, which are clearly the server operating system and not the iLO card:

<sysDescr oid="1.3.6.1.2.1.1.1" type="SnmpOctetString">HP-UX atksts00 B.11.31 U ia64 3910543201</sysDescr>  
<sysObjectID oid="1.3.6.1.2.1.1.2" type="SnmpObjectId">.1.3.6.1.4.1.11.2.3.2.6</sysObjectID>

<sysDescr oid="1.3.6.1.2.1.1.1" type="SnmpOctetString">Hardware: Intel64 Family 6 Model 47 Stepping 2 AT/AT COMPATIBLE - Software: Windows Version 6.3 (Build 9600 Multiprocessor Free)</sysDescr>  
<sysObjectID oid="1.3.6.1.2.1.1.2" type="SnmpObjectId">.1.3.6.1.4.1.311.1.1.3.1.2</sysObjectID>

  

The big problem with this is that the iLO card does not have pass-through for SSH or WMI as well, so all Shazzam sees the SNMP port open. We cannot use the Windows or Unix probes via this IP. If those ports had been open then those Classifiers would have taken priority and we would not even have done a SNMP Classify on the device.

  

This can cause duplication of records or flipping of the CI class if the Server/OS IPs are also scanned separately, perhaps later in the same discovery schedule.

  

**Solution**: **Exclude the iLO card IP range** from the Discovery Schedule, and ensure the main IPs of the server/OS are scanned instead.

  

Note: If iLO is **_not_** set to use pass-through, then you have no problem, because then these devices report their own details, and the unique OIDs specific to HP iLO card versions. A CI will not be created in this case, because there is nothing out-of-box for discovering these iLO card, but a custom implementation would in theory be possible.

## An SNMP OID Classification record has been added incorrectly

There is a table in the instance that allows entering overrides so that instead of the out-of-box code figuring out the class, **we use the specified Table and Identifier for a particular unique System OID value, which may be entered in error**.

e.g. If scanning a "Xerox WorkCentre Pro" printer, the 'SNMP - Classify' probe result includes this 'system' data:

<system oid="1.3.6.1.2.1.1">  
  <sysName oid="1.3.6.1.2.1.1.5" type="SnmpOctetString">P01IT08</sysName>  
  <sysDescr oid="1.3.6.1.2.1.1.1" type="SnmpOctetString">Xerox WorkCentre Pro Multifunction System; ESS 0.040.010.51172, IOT 50.0.0, UI 0.12.50.3, Finisher 3.20.0, Scanner 4.9.0</sysDescr>  
  <sysUpTime oid="1.3.6.1.2.1.1.3" type="SnmpTimeTicks">51948316</sysUpTime>  
  <sysObjectID oid="1.3.6.1.2.1.1.2" type="SnmpObjectId">.**1.3.6.1.4.1.253.8.62.1.20.1.24.1**</sysObjectID>  
</system> 

If there has been a record accidentally added to the table with OID=1.3.6.1.4.1.253.8.62.1.20.1.24.1, and set to a Table and/or Classifier that is simply wrong, **it uses that regardless.**

**Solution**: Delete or **Correct the SNMP OID Classification record** for that OID. 

Note: There have been a few bad OIDs included out-of-box that have since been removed from the product:  

-   PRB1412617 An OID 1.3.6.1.4.1.232.9.4.10 for HP/Compaq iLO causes servers to be re-classified or duplicated as an IP Switch
-   PRB1408983 3 generic Microsoft OIDs starting with 1.3.6.1.4.1.311.1.1.3. causing Windows servers to be re-classified as Computers, Printers, or Routers 
-   PRB1376883 3x Bad OIDs starting 1.3.6.1.4.1.8072.3.2. have been added - These are generic linux snmp stack OIDs and not Unique devices of any particular type

## An SNMP OID Classification record needs to be added because the device is non-Standard

Some manufacturer's devices have very unusual SNMP implementations, making it impossible to accurately classify programatically, based on the rules of the Standard MIBs.

**Solution**: **Create a SNMP OID Classification record** for this Make and Model

You will need to search the ECC Queue table for the SNMP - Classify probe input record for this device's IP address. The use the sysObjectID value, like the one highlighted above.

## An SNMP OID Classification record can't be used, because the manufacturer doesn't use a Unique OID per Model, or the device has been re-branded by an OEM

Some manufacturer's devices may share standard components between multiple models, such as Ricoh's range of Network Printers. The SNMP - Classify probe may return this data for the CI's description field for a RICOH MP C6503  printer, but all other models in the same range will use the same OID too.

RICOH MP C6503 1.03 / RICOH Network Printer C model / RICOH Network Scanner C model / RICOH Network Facsimile C model  
System OID: 1.3.6.1.4.1.367.1.1  

And another example of the raw SNMP - Classify input data for a different model using the same OID:

<system oid="1.3.6.1.2.1.1">  
<sysName oid="1.3.6.1.2.1.1.5" type="SnmpOctetString">Aficio MP C305</sysName>  
<sysObjectID oid="1.3.6.1.2.1.1.2" type="SnmpObjectId">.1.3.6.1.4.1.367.1.1</sysObjectID>  
<sysDescr oid="1.3.6.1.2.1.1.1" type="SnmpOctetString">  
RICOH Aficio MP C305 4.10 / RICOH Network Printer C model / RICOH Network Scanner C model / RICOH Network Facsimile C model  
</sysDescr>  
</system>   

There are a few other unusual things about Ricoh printers:

-   Some printers from other manufacturers are actually re-badged Ricoh printers and have the Ricoh OID.
-   The sysName value may be set as a default value of the printer model, rather than the (DNS) name of the printer. This might need Discovery properties setting to trust the Reverse DNS name over the name returned by SNMP for the CI's name and for identification of the CI. Or, an [Identification Rule specific to Printers that does not use Name as a criteria](https://support.servicenow.com/kb_view.do?sysparm_article=KB0693296 "Identification Rule specific to Printers that does not use Name as a criteria").
-   The device may be seen as a Router. If a device has the clues that suggest it can Print, but can also Route, then it gets classified as a Router.  The device is seen as a router if "ipForwarding" OID is set to 1 and "ipForwDatagrams" OID is set to any number that is higher than 0. In your devices case, both conditions are matching. That can be confirmed by looking for these OIDs in the SNMP - Classify input. To resolve this, you may have to add an OID anyway, but leave the Model name as 'unknown' so that CIs don' t get the wrong model names.

<ip oid="1.3.6.1.2.1.4">  
<ipForwarding oid="1.3.6.1.2.1.4.1" type="SnmpInt32">1</ipForwarding>  
<ipForwDatagrams oid="1.3.6.1.2.1.4.6" type="SnmpCounter32">4581</ipForwDatagrams>  

**Solution**: You will need to rely on the SNMP - Classify probe returning all the OIDs we probe for, so that the sensor script can correctly work out what the device can do, and so classify it as a Printer. Increasing timeouts can help with this (see below). But you risk the possibility of the device being identified as a Router if it appears as if it is doing forwarding.

## An network device based on Linux uses the 'Linux' OID

A lot of network devices are fundamentally ARM- or MIPS-based embedded systems running Linux OS, plus some dedicated hardware and interfaces. These can appear to be Linux, so a Router may be put in the Linux Server table.

In some cases manufacturers fail to assign their own SNMP SnmpObjectId and other SNMP data specific to their make and model, and the default 'Linux' OID remains.

e.g. An embedded linux device using the Net-SNMP SNMP MIB module software returns sysObjectID "1.3.6.1.4.1.8072.3.2.10". The following non-server devices have been seen reporting that non-unique SnmpObjectId:

-   Riverbed Technology, SteelCentral Flow Gateway/User Interface Module
-   Aruba Network, CP-HW-5K IP Router
-   Dell, iDRAC7 Remote Access Controller
-   ExtraHop, Discover 8100
-   Intermec PM43 Printer

**Solution:** In this situation **don't add the OID to the SNMP OID Classification table**, because several different makes/models may use it. It should still be possible to automatically classify the device based on other clues in the SNMP data. If not. you may consider contacting the device manufacturer to have this corrected to use a unique OID for the make and model.

Notes:

-   This cause should not be confused with a Linux Server with SNMP enabled failing to classify. With SSH configured correctly, SNMP is not used.
-   This in theory could be seen with any embedded device using the Net-SNMP SNMP MIB module, with a different final digit of the OID for different Operating Systems. 10=Linux, 3=Solaris, etc.

## Probes Time-Out before receiving the data

Some SNMP-enabled network devices are very simple embedded microcontroller implementations, which are slow. e.g. PDUs, UPSs. They do give serial number data, but sometimes time-out before they have. 

More advanced fast devices such as L2 Switches will be running the SNMP interface code in the same multi-tasking CPU as functional switch code, and under high load the SNMP thread may not respond very quickly or pass the data back very fast. This has been seen with big Cisco Switches, and others.

This causes 2 main problems:

1.  The Probe times out because **no data at all was received** before the Probe timeout. The Sensor will Error in this situation, and Identification will fail.
2.  Data was received before we time out the probe, **but it was incomplete**. As SNMP is based on UDP, it is hard to detect this situation, and we may not realise we only received partial data back from the device. This can also be the case for big devices that have a lot of data to transfer, such as Cisco Switches with huge routing tables.   
    We will then continue to run the Classify and Identify sensors with incomplete data, potentially missing the key classification information.

**Solution**:

Once you have identified devices that can be slow to respond, you can **incrementally increase the SNMP Probe timeouts until the issues are resolved**. These MID Server Parameters can be used to configure the SNMP probes. More details on these are in the documentation for 'MID Server Parameters' or 'SNMP probe parameters':

-   **mid.snmp.request.timeout** - Maximum time to wait for a response for the first OID request
-   **mid.snmp.session.timeout** - Maximum time to wait for responses to OID requests once a session has been established.
-   **timeout** and **established\_session\_timeout** are Probe Parameters, that will override the above two MID Server Parameters, but for a Specific Probe, such as "SNMP - Classify" or "SNMP - Identity". These would then apply to Discovery via any MID Server.
