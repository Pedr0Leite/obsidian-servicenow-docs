---
title: "How to address the Service Catalog Add Content not showing variables"
aliases:
  - KB0656539
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0656539
kb_number: KB0656539
last_modified: 2024-04-07
---

## How to address the Service Catalog Add Content not showing variables

  

### Issue

Under Service Catalog, if you try to add categories that exist, the selector is blank.  

### Cause

The system property _**glide.sc.home.filter**_ that lists content types (comma-separated) to allow on the catalog homepage is set to blank, which allows all content types.  

  

### Resolution

1.  Go to /sys\_properties\_list.do and search for the _**glide.sc.home.filter**_ property.
2.  In the Value field, fill in Catalog Categories,Catalogs.  
    You will be able to see the category items in Selector.

  

Related references:

[https://docs.servicenow.com/csh?topicname=r\_ServiceCatalogProperties.html&version=latest](https://docs.servicenow.com/csh?topicname=r_ServiceCatalogProperties.html&version=latest)
