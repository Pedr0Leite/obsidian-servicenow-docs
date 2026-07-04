---
title: "'Source Request' for unlimited license entitlement shows \"0\" available rights"
aliases:
  - KB2950791
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2950791
kb_number: KB2950791
last_modified: 2026-04-14
---

## 'Source Request' for unlimited license entitlement shows "0" available rights

  

### Issue

Cannot allocate rights for Unlimited Software license through source request

### Symptoms

1\. Activate samp master and procurement plugin  
2\. Create an entitlement with Unlimited License checked  
3\. Create a Service Catalog request and add the same software model to cart and checkout the cart  
4\. In SCTASK, click on 'Source Request'  
5\. In 'Source Request' page, see available rights is 0 and the 'Allocate' button is disabled

### Release

Seen in Xanadu, Yokohama, Zurich, Australia

### Resolution

WORKAROUND:

1\. To fix the issue temporarily we have to remove the unlimited license flag on the corresponding entitlement.  
2\. Increase the purchased rights to a higher value.

### Related Links

This defect is addressed in [PRB1675022](https://support.servicenow.com/now/nav/ui/classic/params/target/problem.do%3Fsysparm_query%3Dnumber%3DPRB1675022)
