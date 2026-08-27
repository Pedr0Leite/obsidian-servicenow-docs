---
title: "Discovery of Windows servers is not triggering \"WMI - Classify\" probe even when the WMI port is open. "
aliases:
  - KB0695337
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695337
kb_number: KB0695337
last_modified: 2024-04-07
---

## Issue

## Description:

Discovery of Windows servers is not triggering "WMI - Classify" probe even though the WMI port is open and classifying the server with SNMP instead.

## Possible Cause:

IP Service Affinity could be configured and set to SNMP. The IP Service affinity saves the IP service information that is used to successfully find a device and associate it with the IP address of the device. So if the device was initially miss-classified in a discovery with a specific protocol, discovery will store that service/protocol information in the IP Service Affinity table \[ip\_service\_affinity\] and use it in future discoveries instead of checking on the open ports. It is enabled through system property:  "glide.discovery.ip\_service\_affinity"

For more information about the IP service affinity:

[https://docs.servicenow.com/csh?topicname=t\_CheckIPServiceAffinity.html&version=latest](https://docs.servicenow.com/csh?topicname=t_CheckIPServiceAffinity.html&version=latest)
