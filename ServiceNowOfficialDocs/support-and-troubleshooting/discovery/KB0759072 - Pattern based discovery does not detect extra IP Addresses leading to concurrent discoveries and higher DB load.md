---
title: "Pattern based discovery does not detect extra IP Addresses leading to concurrent discoveries and higher DB load"
aliases:
  - KB0759072
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0759072
kb_number: KB0759072
last_modified: 2024-04-07
---

## Pattern based discovery does not detect extra IP Addresses leading to concurrent discoveries and higher DB load

  

### Issue

The DB CPU spikes or Read Replica lag occurs during active discovery schedule. Discovery scans on multiple IP Addresses of the same device went through full cycle leading leading to redundant DB operations. In theory, there should be only one IP Address scan went through the full Discovery cycle, the rest of the IP Addresses for the same device in a discovery schedule should be detected as extra/duplicated IP Addresses and halted. This behavior is observed during Probe based discovery. However, during Pattern based discovery, this did not happen.

### Cause

Out of the box, Pattern based discovery do have features to detect extra/duplicated IP Addresses. The behavior is controlled by a couple of properties:

glide.discovery.ip\_based.active = false  
glide.discovery.device.duplicate.ip.optimization = true

However, an upgrade script checks to see if "Discovery - IP Based" plugin is enabled, if it is set the "glide.discovery.ip\_based.active" to true. Probe-to-Pattern migrated instances will always have this property set to true. "glide.discovery.device.duplicate.ip.optimization" property is always true out of the box.

Because the property "glide.discovery.ip\_based.active" is true for probe-to-pattern migrated instances, Discovery does not attempt extra/duplicate IP Address detection. This allows scans on all IP Address of the same device in the same discovery schedule to go through full cycle and needlessly runs redundant operations on DB leading to much higher DB load.

\*\*\* NOTE: The extra/duplicate IP Address detection feature make use of the "install\_status" field on CI tables. This field is defaulted to 1 OOB. If the default value is removed or modified, this feature will not work.

### Resolution

Set the following System Property:

glide.discovery.ip\_based.active = false  
glide.discovery.device.duplicate.ip.optimization = true

Make sure default value exists for at least IP Address or Network Adapter records.
