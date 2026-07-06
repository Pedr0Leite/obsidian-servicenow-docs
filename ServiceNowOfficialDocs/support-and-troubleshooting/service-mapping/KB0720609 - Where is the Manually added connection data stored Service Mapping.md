---
title: "Where is the \"Manually added connection\" data stored Service Mapping"
aliases:
  - KB0720609
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0720609
kb_number: KB0720609
last_modified: 2025-04-08
---

## Issue

-   Based on the docs URL "[Components installed with Service Mapping](https://docs.servicenow.com/csh?topicname=components-installed-with-service-mapping.html&version=latest "Components installed with Service Mapping")", the Manual connections \[sa\_manual\_connections\], contains information on endpoints that customers use while adding manual connections.  
    
-   However, it is not displayed when "Manually add a connection" is triggered from Business Service. 

  

  

## Resolution

-   When the "Manually add a connection" is triggered from the View Map of the Business Service, the record will be saved in Manual Connection Qualifier \[cmdb\_ci\_qualifier\_manual\_connection\] table of the instance.
