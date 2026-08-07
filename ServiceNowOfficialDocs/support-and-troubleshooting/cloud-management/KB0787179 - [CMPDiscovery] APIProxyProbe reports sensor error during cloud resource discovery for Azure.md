---
title: "[CMP/Discovery] APIProxyProbe reports sensor error during cloud resource discovery for Azure"
aliases:
  - KB0787179
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0787179
kb_number: KB0787179
last_modified: 2024-04-08
---

## \[CMP/Discovery\] APIProxyProbe reports sensor error during cloud resource discovery for Azure

  

### Issue

-   During the Cloud resource discovery for Azure, the APIProxyProbe runs out of time due to processing the huge payload for the Multipage sensor and below error will be reported in the ECC queue containing **"Executing API DSL for correlation id ('midserver-8f6d7821-7531-4889-9c8a-220fba13a6c3') - MultiPage 81 of 82"**

**Sensor error: Transaction cancelled: maximum execution time exceeded**

**![](sys_attachment.do?sys_id=0cd15c89dbcc78d066e0a345ca961923)**

### Release

-   Instance with Cloud Management capability.

### Cause

-   This sensor error will occur when discovering Cloud resource which has a huge number of resources i.e. if the payload is too large to be processed.

### Resolution

-   We generally store these payloads chunk by chunk, i.e if 1/1 means then we had only a small set of data which will get processed only in one chunk.
-   But in a specific case if the data which came back was large enough and had to be processed chunk by chunk i.e. if 60/99 means you revoked 99 chunk of the response as the data here is large it is expected to take time to process the payload.
-   In order to resolve this Multipage sensors timeout issue,

1.  Increase the "Discovery MultiPage Sensors" Transaction Quota Rule from 3600 (1 hour) to 259200 (72 hours) (or) any desired value to avoid premature timeouts during long-running cloud resource discoveries.

**Discovery MultiPage Sensors**

Navigate >> System Definition >> Transaction Quota Rules >> Discovery MultiPage Sensors >> Maximum Duration (seconds).

2.  Set the MID Server configuration parameter for "mid.capi.chunk\_size" to 1000 (instead of default 200). So that Multipage sensors will have enough time to process the large payload.

**mid.capi.chunk\_size**

Navigate >> MID Server >> Server >> Select each MID server >> Click on "Configuration Parameter" tab >> click "NEW" >> under the Parameter Name section, select "mid.capi.chunk\_size" and set the Value to "1000".
