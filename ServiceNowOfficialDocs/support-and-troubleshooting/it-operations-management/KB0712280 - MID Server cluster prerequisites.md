---
title: "MID Server cluster prerequisites"
aliases:
  - KB0712280
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0712280
kb_number: KB0712280
last_modified: 2024-04-07
---

## MID Server cluster prerequisites

  

### Issue

# Overview

* * *

-   Enable multiple MID server with same capabilities to be grouped together for load balancing and failover protection
-   Provide the flexibility to add MID servers to both a load balanced and failover cluster.
-   All MID servers initiate separate communication with ServiceNow and continually check the ECC queue for work.

#   

# Mid server cluster prerequisites

                                                                               ![](sys_attachment.do?sys_id=c68aec66db42b450e515c22305961908)

![](sys_attachment.do?sys_id=c56eba1fdbe06740a39a0b55ca961962)![](sys_attachment.do?sys_id=754ef21fdbe06740a39a0b55ca961918)![](sys_attachment.do?sys_id=c56eba1fdbe06740a39a0b55ca961962)

-   MID server cluster does not support the domain separation so all  MID servers should be in the same domain.
-   All MID servers should have the same IP ranges.
-   All MID servers should have the same applications supported.
-   All MID Servers should have the same capabilities.

#
