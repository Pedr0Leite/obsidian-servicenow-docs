---
title: "Using Cart JS Scoped API, when ordering an item with a quantity of '1', multiple RITMs are being ordered (1+)."
aliases:
  - KB0783792
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783792
kb_number: KB0783792
last_modified: 2024-04-08
---

## Using Cart JS Scoped API, when ordering an item with a quantity of '1', multiple RITMs are being ordered (1+).

  

### Issue

The user is facing some issues with the Cart JS Scoped API. Namely, when they are ordering one Request, and setting the quantity of the RITM to '1' (i.e. one RITM should be created), sometimes the user is seeing 2+ RITMs get created. They wanted to know why.

### Resolution

The reason the user is seeing this behavior is that they are using a cart name of the form 'cart\_' + itemId + UserID. This is not advised.

As per an internal task to the Product Owners, it was found that that the user is using a cart name of the form 'cart\_' + itemId + UserID.  
  
Our Product Owners suggested that users please not use cartNames starting with 'cart\_' or ones containing itemId. Rather, something like gs.generateGUID() for cartName is advised.
