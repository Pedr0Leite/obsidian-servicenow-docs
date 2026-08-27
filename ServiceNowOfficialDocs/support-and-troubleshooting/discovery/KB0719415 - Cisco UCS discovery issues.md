---
title: "Cisco UCS discovery issues"
aliases:
  - KB0719415
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0719415
kb_number: KB0719415
last_modified: 2024-04-07
---

## Cisco UCS discovery issues

  

### Issue

# Symptoms

* * *

Discovery of Cisco UCS device fail after shazzam stage in discovery

# Release

* * *

Any release

# Cause

* * *

When you are trying to discover UCS cluster by scanning the Web Portal IP address, the device responds back from a different IP address. Since shazzam probe listens only to the IP address it scans, the device response it not acknowledged.

This happens because the UCS cluster responds back from the IP address of the active node. 

# Resolution

* * *

The UCS cluster should be scanned from the IP address of the active node instead of the Web Portal IP
