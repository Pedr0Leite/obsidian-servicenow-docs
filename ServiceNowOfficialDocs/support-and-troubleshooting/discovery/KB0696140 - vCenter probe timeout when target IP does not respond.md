---
title: "vCenter probe timeout when target IP does not respond"
aliases:
  - KB0696140
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696140
kb_number: KB0696140
last_modified: 2024-04-07
---

## vCenter probe timeout when target IP does not respond

  

### Issue

# Symptoms

* * *

During discovery, VMWarevCenterDatacentersProbe launches and never finishes, thus causing the discovery schedule to terminate after its max run time.

# Cause

* * *

During discovery, Shazzam probe may have identified an IP with 5480 or 9443 port open. This IP may not respond if this is not a vCenter and may cause VMWarevCenterDatacentersProbe to never respond and discovery would timeout subsequently.

# Resolution

* * *

-   As the IP is not a vCenter IP, port 5480 or 9443 should be disabled on suspected IP.
-   For any reason, if disabling these ports is not an option, a new probe parameter named **"prevalidate\_vcenter"** can be added to "VMWare - vCenter Datacenters" probe. This is used to validate if the vCenter is responding with an HTTP request timeout of 30000 milliseconds by default.
    -   Follow below steps to set this property.
    -   Navigate to Discovery Definition --> Probes
    -   Search and open probe "**VMWare - vCenter Datacenters**"
    -   Goto Probe Parameters related list. If not available configure to have this added
    -   Add new property "**prevalidate\_vcenter**" with value = "true" to the parameters list.
