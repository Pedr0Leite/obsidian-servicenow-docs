---
title: "SCCM does not populate IP address on the computer record, and glide.discovery.enforce_ip_sync  doesn't work"
aliases:
  - KB0812625
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0812625
kb_number: KB0812625
last_modified: 2024-04-10
---

## Issue

When importing computer/workstations from SCCM NO IP Address is import to the computer record.   The data source SCCM Network is creating the network adaptors as expected. Also the property glide.discovery.enforce\_ip\_sync is set to true. Still, the IP addresses of computer CIs are showing blank, but the IP address is shown in the related record.

## Resolution

This is not supported out of the box.  It will require customization on your part to get this information. 

  

What to consider when you're populating the IP address of the computer CI.

1.  If the computer/server had multiple network adapter which IP address would want to populate the CI with?

  

You can check community article/s like the below one to see how others have implemented this feature.  

[Does SCCM Integration populate the IP Address field on a Computer record?](https://community.servicenow.com/community?id=community_question&sys_id=bd528f751b5a8010ada243f6fe4bcb26&view_source=searchResult "Does SCCM Integration populate the IP Address field on a Computer record?")
