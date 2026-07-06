---
title: "Layer 2 Discovery : Neighbor interface data not populated in the Discovery Device Neighbors table"
aliases:
  - KB0783185
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783185
kb_number: KB0783185
last_modified: 2024-04-07
---

## Issue

In order to create a physical connection between 2 different network devices, we need to have the discovery\_device\_neighbors table populated with the neighbor interfaces

## Resolution

\- Change line no 143 in Network Devices - Pre Sensor from  
  
neighborCiSysId = remoteNeighborGlideRecord.cmdb\_ci;  
  
to  
  
neighborCiSysId = remoteNeighborGlideRecord.cmdb\_ci.toString();  
  
  
\- After making the above change and re-running discovery on the switches will make sure the neighbor interface data is populate
