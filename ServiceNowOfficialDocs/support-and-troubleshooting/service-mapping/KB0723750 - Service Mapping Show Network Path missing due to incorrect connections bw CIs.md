---
title: "Service Mapping: Show Network Path missing due to incorrect connections b/w CIs"
aliases:
  - KB0723750
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0723750
kb_number: KB0723750
last_modified: 2024-04-07
---

## Service Mapping: Show Network Path missing due to incorrect connections b/w CIs

  

### Issue

# Symptoms

* * *

'Show Network Path' option doesn't show up b/w CIs in a BSM.

# Release

* * *

All

# Cause

* * *

1.  The issue is due to incorrect ip address connections in sa\_network\_paths.  
    2\. For example: The issue is witnessed if the connections are created to IP X.X.232.36, and there is no host with this IP in cmdb\_ci. Network path calculation requires that CMDB will have a host with this IP.

# Resolution

* * *

-   In this case, discovery was executed on ip address that's not tied to a NIC because of which a random ip is tied to one of the NICs. During Service Mapping, the network connection is tied to the VIP of the entry point.
-   To resolve, we disabled "glide.discovery.enforce\_ip\_sync" property. After clearing the ip address field on the CI and running discovery took care of populating the field with discovered ip address (xx.xx.xx.36)
-   Now when discovery is complete, we are seeing the "Show network path" option for the connections b/w CIs.
