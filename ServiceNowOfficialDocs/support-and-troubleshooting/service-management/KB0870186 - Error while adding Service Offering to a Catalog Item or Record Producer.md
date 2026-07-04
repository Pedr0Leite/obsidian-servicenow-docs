---
title: "Error while adding Service Offering to a Catalog Item or Record Producer"
aliases:
  - KB0870186
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0870186
kb_number: KB0870186
last_modified: 2024-02-22
---

## Error while adding Service Offering to a Catalog Item or Record Producer

  

### Issue

While trying lo link service offering to a record producer or a catalog item, an error being occurred stating "To be associated with an offering. a catalog item must belong to one of these categories: Catalog Item, Product Catalog Item, Hardware Catalog, Software Catalog".

### Release

Paris

### Cause

This is expected behavior in Paris Version as per the OOB configuration.

### Resolution

This is expected behavior in Paris Version as per the OOB configuration.

In Paris Version we have the business rule "Allow association from selected cat items" in place, Hence you are not able to add the service offerings "Available for Subscribers" tab  
  
https://<INSTANCENAME>.service-now.com/sys\_script.do?sys\_id=81dc793c8793001072bfa1fe37cb0b71
