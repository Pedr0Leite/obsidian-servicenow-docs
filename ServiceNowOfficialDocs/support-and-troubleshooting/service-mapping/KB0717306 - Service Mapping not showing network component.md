---
title: "Service Mapping not showing network component"
aliases:
  - KB0717306
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0717306
kb_number: KB0717306
last_modified: 2024-04-07
---

## Issue

# Symptoms

* * *

After running Service Map, you see that in some of the connections there is no option for "Show Network Path" to represent the network components between CIs. 

You look at the sa\_network\_path table and see that there is not value in the field Layer 3 path for those CIs. 

# Cause

* * *

In order to find the layer 3 path, we run traceroute command from the source host to the target host.

Before running the traceroute command, we run ping command on the target host.

# Resolution

* * *

In order to check it, use the following url:

1.  https://\[INSTANCE\_NAME\].service-now.com/SaCmdManager.do?ip=\[IP\_ADDRESS\_OF\_DEVICE\_PATH\_SHOULD\_COME\_FROM\]
2.  Run the following command:  
    \>ping -c 1 \[IP\_ADDRESS\_OF\_DEVICE\_PATH\_SHOULD\_GO\_TO\].
    -   This should be successful.
3.  After that make sure the traceroute also works. If both of these are working then network path should be set.   
    -   If one or both fail, that needs to be fixed on your network side.

#
