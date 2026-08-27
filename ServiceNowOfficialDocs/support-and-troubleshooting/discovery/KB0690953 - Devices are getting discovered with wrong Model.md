---
title: "Devices are getting discovered with wrong Model"
aliases:
  - KB0690953
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0690953
kb_number: KB0690953
last_modified: 2024-04-07
---

## Devices are getting discovered with wrong Model

  

### Issue

# Symptoms

* * *

Devices are getting discovery with different model name than expected.

# Release

* * *

All releases.

# Cause

* * *

The cause of this problem is either the Sys Object IDs are not present in the system or for the problematic devices, model name and number are updated incorrectly under "SNMP System OIDs"

# Resolution

* * *

Add appropriate Sys Object ID under "SNMP System OIDs" section by navigating to "Discovery definition -> CI CLassification -> SNMP System OIDs"

For example, if you are trying to discover a device with sys object ID of 1.3.6.1.4.1.9.1.1935, it should get discovered with model Cisco ISR 4431, but since the OID is not present in Out of the box, it may be discovered with an unexpected model name.

Below screenshot exemplifies on search and add System OIDs.

![](sys_attachment.do?sys_id=826a2466db42b450e515c223059619c1)

You can add new Sys OID by clicking on "New" button and filling the details as below.

![](sys_attachment.do?sys_id=c26a2466db42b450e515c223059619c6)

Click on submit once you are done and do a resicovery of the device. 

# Additional Information

* * *

[Create a Discovery CI classification](https://docs.servicenow.com/csh?topicname=create-discovery-ci-classification.html&version=latest "Create a Discovery CI classification")
