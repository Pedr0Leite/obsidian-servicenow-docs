---
title: "Can we have Firewall as an Entry point for Business Service Mapping?"
aliases:
  - KB0755960
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0755960
kb_number: KB0755960
last_modified: 2024-04-07
---

## Can we have Firewall as an Entry point for Business Service Mapping?

  

### Issue

# Resolution

Since the MID server sits in the customer's internal network, we would expect that the entry point is not that of a firewall but another device (like load balancer, etc.) in the internal network. We also do not have a pattern to discover a NAT firewall Out of the box and so, unfortunately, we do not support that. 

# Additional Information

Please review the documentation in the link below to understand the prerequisite required for performing top-down discovery using Service Mapping -   
[https://docs.servicenow.com/csh?topicname=prerequisites-service-mapping.html&version=latest](https://docs.servicenow.com/csh?topicname=prerequisites-service-mapping.html&version=latest)
