---
title: "Service Catalog user criteria"
aliases:
  - KB0657463
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0657463
kb_number: KB0657463
last_modified: 2025-04-18
---

## Issue

Some users may not be able to see catalog items, although these do not have user criteria set to limit access.  

  
Documentation Topics

* * *

For more information about the _**glide.sc.use\_user\_criteria**_ and **glide.sc.user\_criteria\_migration** system properties, see [Service Catalog properties](https://docs.servicenow.com/csh?topicname=r_ServiceCatalogProperties.html&version=latest)

For more information on the migration process to Service Catalog user criteria, see [Migrate to Service Catalog user criteria](https://docs.servicenow.com/) 

## Resolution

If the user is not able to see the catalog item, set the 'glide.sc.use\_user\_criteria' property to true, so the user criteria related lists are used instead of the roles listed in the Roles field.

If the user Roles field is hidden, set the system property _**glide.sc.use\_user\_criteria**_ to false, the Roles field becomes then visible.

To make the **Available For** and **Not Available For** related lists visible, set the system property _**glide.sc.user\_criteria\_migration**_ to true.
