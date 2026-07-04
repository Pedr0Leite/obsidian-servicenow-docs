---
title: "Linux server classified as a standard network printer "
aliases:
  - KB0657524
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0657524
kb_number: KB0657524
last_modified: 2024-04-07
---

## Linux server classified as a standard network printer

  

### Issue

Linux server classified as a standard network printer

  
  

# Overview

* * *

In some discoveries, a Linux Server may be classified as a standard network printer.

For this scenario to occur the following conditions must be true:

-   SSH classification must have failed
-   The Linux device has SNMP turned on and returned information that classified it as a printer

OR

-   SNMP classification was set to run before SSH classification
-   The Linux device has SNMP turned on and returned information that classified it as a printer

# Cause

* * *

Based on the results returned from the Shazzam probe, discovery attempts to classify a device in the order of the classification priority configured under Discovery Definition > Port Probes. If Shazzam detects more than one open port that might be used for classification, classification will be attempted on both until the device is classified or all classification attempts have failed. 

For example, if Shazzam detects SSH and SNMP available for classification it will try to classify the device based on SSH classification first, per the default classification priority. If successful, the discovery proceed to the identification phase of discovery. If classification of SSH fails, discovery moves on to SNMP classification.

Therefore, given the steps followed by discovery to classify a device and the described conditions, it is to be expected that such a Linux device would be classified as a printer. However, you can change this behavior by updating the classification criteria.

# Workaround

* * *

The classification probes gather information from the device being discovered. This information is then passed through the classification criteria to check for a match. You can see the classifications by navigating to **Discovery Definition > CI Classification**.

Because the device is classified as a printer instead of a Linux server, adding new classification criteria for the Standard Network Printer will ensure that the Linux device is not classified as a printer.

For more information about the fields that are available for SNMP classification, see the product documentation topic [SNMP parameters for Discovery](https://docs.servicenow.com/).

The general steps to resolve the issue are as follows:

1.  View the SNMP - Classify input payload.
2.  Find an oid value that can be used to avoid having the device to be classified as a printer or any other SNMP device.
3.  Confirm that the field is available for classification based on the SNMP parameters for discovery link.
4.  Add a new classification criteria to the classifier.

You can also use this procedure to configure other SNMP classifiers to better fit a specific environment. For cases where the issue is caused due to SSH classification failure, start by resolving the SSH issue failure first.

For example, suppose a Linux server returns the following as part of the SNMP - Classify probe input:

<sysDescr oid="1.3.6.1.2.1.1.1" type="SnmpOctetString">UnixOS servername 6.2 Generic\_2600</sysDescr> 

The SNMP parameters link indicates that sysdescr is one of the fields available for classification. Therefore, based on sysdescr, you would add criteria such as the following to ensure the Standard Network Printer classification does not classify the device:

**\[sysdescr\] \[does not contain\] \[UnixOS\]**

The Standard Network Printer classification criteria would then be as follows: 

![](sys_attachment.do?sys_id=2e4c646edb42b450e515c22305961917)
