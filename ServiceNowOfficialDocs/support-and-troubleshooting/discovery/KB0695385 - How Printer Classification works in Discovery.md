---
title: "How Printer Classification works in Discovery"
aliases:
  - KB0695385
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695385
kb_number: KB0695385
last_modified: 2024-04-07
---

## Issue

# Overview

* * *

When using discovery the instance will determine if a device is a Printer or not in the following manner. 

# Printer Classification

* * *

1) First you will need to look at the Standard Network Printer classifier

-   Go to Discovery Definition > Ci Classification > All
-   Search for Name = "Standard Network Printer"

2) You will see that a printer will be classified as such if 'printing equal true'

So what does that mean? 

3) To find the answer we will open the SNMP - Classify Sensor

-   Go to Discovery Definition > Sensors
-   Looks for name = "SNMP - Classify"

4) In that sensor's script you will see around line 150 (may be different if you have customized this). It may also be different based on version but logic should be pretty much the same.

    // is this thing a printer?

    var isPrinter = false;

    var isHrDevicePrinter = false;

    var hasPrtGeneralSerialNumber = false;

    // first look in the Host Resources MIB...

    var devices = snmp.getOIDTable(oid\_mib2 + 'host.hrDevice', 'hrDeviceEntry');

    var hrDeviceDescrs = \[\];  //used in short\_description

    for (var index in devices) {

         var deviceType = devices\[index\]\['hrDeviceType'\];

         isHrDevicePrinter = isHrDevicePrinter || (deviceType.substr(-2) == '.5'); 

5) This script is evaluates/runs on the returned response from the SNMP - Classify probe. 

6) So with isPrinter initiallized to 0, then checking the substr(-2) == .5 of the OID returned for "hrDeviceEntry" for that device we see that (deviceType.substr(-2) == '.5') evaluates to 1 if true and 0 if false. The || bitwise operation then evaluates this as 0||1 = 1 or 0||0 = 0, which = true for 1 and false for 0. 

7) There is a subsequent steps that checks another OID as well, see around lines 168:

        var prtGens = snmp.getOIDTable(oid\_mib2 + 'printmib.prtGeneral', 'prtGeneralEntry');

        for (var index in prtGens) {

            var prtSerial = prtGens\[index\]\['prtGeneralSerialNumber'\];

            hasPrtGeneralSerialNumber = hasPrtGeneralSerialNumber || JSUtil.notNil(prtSerial);

        }

        // if both conditions are true we assume the device has printing capability

        isPrinter = isHrDevicePrinter && hasPrtGeneralSerialNumber;

        capabilities\['printing'\] = '' + isPrinter;

8) This does the same as the previous script, as far a logic. Only difference is, it looks for "prtGeneralEntry" instead of "hrDeviceEntry". If prtGeneralEntry is not returned in the payload of the probe, this part of the script is not evaluated and only relies on the previous script block.
