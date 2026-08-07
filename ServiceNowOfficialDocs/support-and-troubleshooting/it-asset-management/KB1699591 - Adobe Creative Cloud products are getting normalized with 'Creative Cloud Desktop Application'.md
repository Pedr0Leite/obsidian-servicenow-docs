---
title: " Adobe Creative Cloud products are getting normalized with 'Creative Cloud Desktop Application"
aliases:
  - KB1699591
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1699591
kb_number: KB1699591
last_modified: 2026-03-11
---

## Adobe Creative Cloud products are getting normalized with 'Creative Cloud Desktop Application'

  

### Issue

The Adobe Creative Cloud products are getting normalized with the 'Creative Cloud Desktop Application', which is an unlicensed installation. So why is the discovered product 'Adobe Creative Cloud' being matched with 'Creative Cloud Desktop Application' in the discovery models

### Release

Any

### Resolution

Please note that the product "Creative Cloud" is a bundle only and not an installable product  
  
The customer would get a desktop app that gives access to all the products sold under Creative Cloud and this desktop app gets discovered like "Creative Cloud.app", "Creative Cloud Desktop App" etc. hence all such discoveries of Creative Cloud are mapped to a product "Creative Cloud Desktop Application" which is "Not Licensable"  
  
Also, as the product "Creative Cloud Desktop Application" is Not Licensable these installs should not show as unlicensed
