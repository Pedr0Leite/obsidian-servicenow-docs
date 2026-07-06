---
title: "Stand by load balancer not getting discovered"
aliases:
  - KB0752282
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0752282
kb_number: KB0752282
last_modified: 2024-04-07
---

## Stand by load balancer not getting discovered

  

### Issue

When the customer's network has multiple load balancers and a stand by setup, can we expect to see the standby load balancer on the business/application service?

  

  

  

  

### Resolution

1.  When an **'HTTPS endpoint'** is chosen while creating a map, a **Fully Qualified Domain Name** would be fed as the **entry point**.
2.  Once the right is **FQDN** has been provided, the **DNS probe** determines the **IP address** mapped to the FQDN.
3.  The load balancer services table in the ServiceNow's instance would be referred to determine the right LB serving or configured for the IP address determined above.
4.  Once the LB is determined, the vertical discovery process continues until the map is filled with the right set of CIs that are expected to serve a business/application service.
5.  The **Active Load Balancer** that would be serving the request is expected to be shown on the map but the **standby load balancer will not be shown on the map.** It is by design.

  

An example map looks like the below -

  

![](sys_attachment.do?sys_id=a0cc68eedb42b450e515c22305961944)
