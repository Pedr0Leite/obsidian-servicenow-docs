---
title: "Assign a specific MID Server to Integration Hub flows"
aliases:
  - KB0871106
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0871106
kb_number: KB0871106
last_modified: 2025-08-27
---

## Assign a specific MID Server to Integration Hub flows

  

### Issue

Integration Hub flows sometimes use incorrect MID Servers, causing integration issues. This article explains how to assign a specific MID Server using IP address configuration. 

### Release

All supported releases

### Resolution

Integration Hub uses MID Selector to choose appropriate MID Servers. Without IP addresses, MID Selector relies solely on MID capability, which can lead to incorrect selections when multiple MID Servers share the same capabilities.

To assign a specific MID Server to an Integration Hub flow:

1.  Identify the IP address of the target system your flow interacts with.
2.  Configure the intended MID Server to include this IP address in its range.
3.  Configure all other MID Servers to exclude this IP address from their ranges.

### Related Links

For more details on including and excluding IP ranges in MID Server, see [Configure an IP address range for the MID Server](https://docs.servicenow.com/bundle/quebec-servicenow-platform/page/product/mid-server/task/t_ConfigureMIDIPRange.html "Configure an IP address range for the MID Server")
