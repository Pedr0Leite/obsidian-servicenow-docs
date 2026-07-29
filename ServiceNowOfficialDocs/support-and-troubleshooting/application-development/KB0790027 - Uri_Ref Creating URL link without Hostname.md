---
title: "Uri_Ref Creating URL link without Hostname"
aliases:
  - KB0790027
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0790027
kb_number: KB0790027
last_modified: 2024-08-13
---

## Uri\_Ref Creating URL link without Hostname

  

### Issue

We have a notification on Catalog task which is sent when a task is assigned to a group. The notification is using URI\_REF to reference the catalog task number. The catalog task link intermittently gets created without host name. 

### Release

All

### Cause

Glide.servlet.Uri value can not be use blank. This is a legacy property is no longer recommended to be used. However, once it is created, it should NOT be deleted, as it can then also impact the URI references sent in Notifications etc.

### Resolution

The value of this property should be set to the URI of your instance is blank it should be updated to  
https://<instancename>.service-now.com/
