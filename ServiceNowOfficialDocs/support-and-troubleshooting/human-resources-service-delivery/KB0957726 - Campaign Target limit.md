---
title: "Campaign Target limit"
aliases:
  - KB0957726
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0957726
kb_number: KB0957726
last_modified: 2024-02-22
---

## Campaign Target limit

  

### Issue

Why Campaign Targets limits to 90000 when the user criteria for inclusion should have more than 90000 users.

### Cause

System properties:

"Max number of events to add users per campaign"

"Max number of users to add per event" 

### Resolution

There are some properties in Content Automation:  
"Max number of events to add users per campaign" which is set to 90  
"Max number of users to add per event" is set to 1000 by default.

These make a max of 90000 users which can be added to any campaign by default. If you would like to add more than 90000 users, the default values will need to be increased.

### Related Links

Properties installed with content delivery

[https://docs.servicenow.com/bundle/paris-hr-service-delivery/page/product/human-resources/reference/properties-content-delivery.html](https://docs.servicenow.com/bundle/paris-hr-service-delivery/page/product/human-resources/reference/properties-content-delivery.html)

-   -
