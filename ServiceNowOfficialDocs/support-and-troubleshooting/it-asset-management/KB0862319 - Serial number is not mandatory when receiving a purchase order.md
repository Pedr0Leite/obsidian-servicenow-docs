---
title: "Serial number is not mandatory when receiving a purchase order "
aliases:
  - KB0862319
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0862319
kb_number: KB0862319
last_modified: 2025-03-11
---

## Serial number is not mandatory when receiving a purchase order

  

### Issue

When receiving a PO, if the user only enters the asset tag number and NOT the serial number, we get an error "Unexpected error has occurred". Happened after upgrade to paris.

### Release

Paris

### Cause

Making serial number mandatory is new feature introduced in 'Paris', which will be turned off by default for upgrading customers.

### Resolution

In upgraded instance the field does not show up as mandatory.  
\-> Making serial number mandatory is new feature introduced in 'Paris', which will be turned off by default for upgrading customers.  
This feature is controlled by a system property "glide.asset.create\_ci\_with\_ire".  
Release notes - https://docs.servicenow.com/csh?topicname=c\_ManagingAssets.html&version=latest  
  
The current issue has nothing to do with the new feature introduced in 'Paris', as the property is turned off.  
  

### Related Links

https://docs.servicenow.com/csh?topicname=c\_ManagingAssets.html&version=latest
