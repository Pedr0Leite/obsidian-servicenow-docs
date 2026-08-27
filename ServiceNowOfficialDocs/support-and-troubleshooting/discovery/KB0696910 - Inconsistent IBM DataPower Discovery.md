---
title: "Inconsistent IBM DataPower Discovery "
aliases:
  - KB0696910
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696910
kb_number: KB0696910
last_modified: 2024-04-07
---

## Inconsistent IBM DataPower Discovery

  

### Issue

# Symptoms

* * *

When there is a schedule for discovering multiple IBM DataPower devices, not all devices are discovered successfully on each Discovery run.

# Release

* * *

This is applicable to all releases

# Cause

* * *

This could happen when all the devices have the same SNMP v3 (authoritative) engine IDs, which is forbidden.

Let us take a situation where there are three Devices: Device1, Device2 and Device3. When running discovery, the devices are mistaken for each other. For example, while trying to discover Device2 we have success, when trying Device3 we are failing as discovery thinks Device3 is Device2 and tries to connect using some Device2 properties which causes a security error.

# Resolution

* * *

The Engine ID should be changed on the DataPower devices, such that they are unique across all the devices

# Additional Information

* * *

[https://www-01.ibm.com/support/docview.wss?uid=swg1IC94542](https://www-01.ibm.com/support/docview.wss?uid=swg1IC94542)
