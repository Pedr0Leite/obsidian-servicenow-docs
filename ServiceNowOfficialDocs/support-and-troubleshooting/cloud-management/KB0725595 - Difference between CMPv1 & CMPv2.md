---
title: "Difference between CMPv1 & CMPv2 "
aliases:
  - KB0725595
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725595
kb_number: KB0725595
last_modified: 2024-04-07
---

## Difference between CMPv1 & CMPv2

  

### Issue

# Overview

* * *

ServiceNow Cloud Management Platform have 2 versions CMPv1 and CMPv2, this article will demonstrate the basic differences between the versions. 

# CMPv1

* * *

-   Discovery schedule is of type 'Web Service'
-   All probes are created with agent = mid.server.NODE\_AGENT
-   All probes are executed by instance by scheduled job named 'Run Instance-side Probes', no MID Servers involved.
-   All probe results are plain text in input payload
-   RDS discovery not supported

# CMPv2

* * *

-   Discovery schedule is of type 'Cloud Resources'
-   Discovery is executed by MID Servers.
-   All probes have topic 'APIProxyProbe'. 
-   Data is Base64 encoded. You need to go to CAPI Trail to see Decoded text.
-   RDS discovery is supported through RDS Pattern.
