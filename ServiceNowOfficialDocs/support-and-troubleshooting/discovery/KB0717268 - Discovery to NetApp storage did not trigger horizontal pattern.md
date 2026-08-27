---
title: "Discovery to NetApp storage did not trigger horizontal pattern"
aliases:
  - KB0717268
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0717268
kb_number: KB0717268
last_modified: 2024-04-07
---

## Discovery to NetApp storage did not trigger horizontal pattern

  

### Issue

Run Discovery to a NetApp Storage server but the discovery stops after the classification stage.

### Release

Kingston

### Cause

The System Property glide.discovery.sensors.netapp\_native\_cluster\_mode was set to **false**

### Resolution

Set the value of the property glide.discovery.sensors.netapp\_native\_cluster\_mode to **true**.

### Related Links

The instance where this issue was detected had been provisioned initially with the Kingston version. The value of glide.discovery.sensors.netapp\_native\_cluster\_mode is by default **true**. If the instance was upgraded to Kingston from an earlier version, the value is **false**.

In the Classifier Probe: **HorizontalDiscoveryProbe-Horizontal Patt** (/nav\_to.do?uri=discovery\_classifier\_probe.do?sys\_id=f9f0a1909f5803003f2492ec757fcfdb) there is a condition script:

DiscoveryStorageUtilities.checkUseNetAppClusterModePattern()

which triggers the script include "**DiscoveryStorageUtilities**" that makes use of glide.discovery.sensors.netapp\_native\_cluster\_mode in the **checkUseNetAppClusterModePattern()** function. 

![](sys_attachment.do?sys_id=8d8c24aedb42b450e515c22305961984)
