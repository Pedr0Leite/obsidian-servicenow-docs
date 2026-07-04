---
title: "Troubleshooting the Identification Phase in Discovery"
aliases:
  - KB0535238
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0535238
kb_number: KB0535238
last_modified: 2026-05-19
---

## Troubleshooting the Identification Phase in Discovery

  

### Issue

During the identification stage in Discovery you may run into situations where no identifier was able to find a match or more than one match was found. 

### Release

All

### Resolution

This article describes Discovery with probes and sensors (not patterns).  
  
The CI Identification phase is where Discovery attempts to determine whether the target device that is being discovered already has a record in the CMDB. If the answer is _yes_, then Discovery continues by launching the exploration probes. If their answer is _no_, then Discovery creates a record for it in the CMDB before launching the exploration probes.

The identification probe is determined by the CI Classification, in the **Triggers probes** related list, under the following conditions: **\[****Phase = Identification\]**, **\[Active = true\]**, **\[and\]** **\[condition scripts is empty\] \[or\] \[evaluates to true\]**. 

![](/aleckimage1.jpgx)

By design, each identity probe attempts to gather as much identifying information about the target as possible. This typically includes things like hostname, serial numbers, and network adapters. With this identifying information, Discovery runs them through a list of identifiers until it comes to a stopping point, which could be:

1.  An identifier has found one and only one match.
2.  No active identifiers are able to find one and there is only one match in the CMDB. Here are the possible outcomes:  
    1.  No identifier was able to find any match at all.
    2.  At least one of the identifiers found more than one match.

In the case of 1, an identifier has found one and only one match in the CMDB. Then Discovery declares that it knows exactly which CI record it is.   
In the case of 2-a, no identifiers are able to find any match in the CMDB. Therefore, the device being discovered must be a new CI. Discovery creates a record for it in the CMDB.  
In the case of 2-b, the best case any of the identifiers is able to do is to find multiple matches. In this case, Discovery stops because it is unable to determine which record it needs to update. In other words, until someone steps in and cleans up the duplicate records, Discovery is not able to continue to the exploration phase.

![](/aleckimage2.pngx)

Typically, the identifiers are run in order of the best identification method. In other words, the most reliable methods to identify a CI should typically go first, followed by lesser ones. To find hardware-based CIs in the base system, serial number identifiers are chosen to go first because serial numbers are typically the most reliable way to identify a CI, followed by name, and then network adapters. The exceptions here are CI specific identifiers. For example, ESX servers can be identified reliably through UUID much more than any other piece of information. Therefore, it should be at the very top. 

The identifications order should always be modified to tailor to your specific environment. For example, if you know that the names of devices in your network are not unique, then by all means turn off the **Name & Class Name** identifier because it is not going to help. Or conversely, if you know that all the names of devices in your network are unique, then go ahead and promote the **Name & Class Name** identifier ahead of the two serial number identifiers (for example, changing the order from 1100 to 990).   
  
Sometimes devices could have multiple IP addresses on the network. Suppose a device has IP addresses A, B, and C, during a Discovery, and all three IP addresses respond to Shazzam (port scanning). Therefore, Discovery sends out a probe for each of the IP addresses. During the identification phase, Discovery at some point realizes that the three IP addresses are actually the same device and simply pick one to finish the Discovery (whatever IP Discovery happens to find first). Here is an example of what it looks like:

![](/aleckimagesmall.jpgx)

### Troubleshooting Techniques

**If the identity probes are somehow not launched, check the following:** 

1.  Did the classification probe run successfully? If not, check the credential against the target.
2.  Find the appropriate classification (UNIX, Windows, SNMP) and check if the identified probe is included in the **Triggers probe** related list. If not, add it back in.

**Discovery is overwriting the incorrect CI record**

This could happen if, during the identification phase, an identifier finds a match in the CMDB that is, in fact, incorrect. For example, if someone created or imported a CI and entered an incorrect serial number or a serial number that is too generic, such as a chassis serial number, Discovery identifies it by the serial number and overwrites the record by mistake. This can be remedied either by not using the serial number identifier or by modifying the serial number input so that the serial number is always unique.   
  
**I have different CIs that are overwriting each other in the same record**

This is typically due to an identifier mistaking the same record in the CMDB for different devices. For example, there are two devices with the exact same name and they somehow have no serial number as the identifiable information. Discovery always ends up creating/updating the same record for both devices. If both devices happen to be in the same Discovery run, it would even look like they are the same CI with multiple IPs and one gets the **_Identified, ignored extra IP_** message. 

**A discovered device matches more than one existing CI**

Navigate to **Discovery Definition > Properties** and select **Yes** for the CI identification debugging property. This property writes additional data for each IP address to the Discovery log during the CI identification process. Consult this log to resolve issues with duplicate CIs.  
  
**Discovery stops after the identity probe has run**

This could be due to identifiers finding multiple matches in the CMDB. In other words, Discovery has found matches in the CMDB, but is not able to determine which one is the correct record to update. In this case, human intervention to the CMDB is needed. The duplicate records must be cleaned up for Discovery to continue properly. Here is an example of what it looks like in the log:

![](/aleckimage3.jpgx)
