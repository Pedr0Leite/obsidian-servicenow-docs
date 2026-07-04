---
title: "Duplicate RITM records when created via a script within a Scheduled Job"
aliases:
  - KB0688280
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0688280
kb_number: KB0688280
last_modified: 2024-04-07
---

## Duplicate RITM records when created via a script within a Scheduled Job

  

### Issue

The user experienced an issue where two RITMs were created from a single scheduled job when only one RITM was expected to be created.

### Release

Jakarta Patch 6a

### Cause

The user had multiple scheduled jobs running at the same time.

### Resolution

It was noted that the user had multiple scheduled jobs running at 2:00 am which were assigned to the same user ("Bucky Barnes"). The script being utilized within the job was creating a cart for the user, adding the item into the cart, and then ordering the item.  
  
In several scenarios, with regard to the parent Requests, the system seemed to be confused and added both items to one cart creating one Request, and then another cart is created for the other item, and both items are again added to the cart.  
  
To prohibit such behavior from happening, it was recommended that the user specify a unique cart in the script being utilized. For example:  
  
var cart = new sn\_sc.CartJS(gs.generateGUID());
