---
title: "[Team Development] - Not able to set Parent Instance in Team Dashboard - glide.apps.hub.current"
aliases:
  - KB0793481
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0793481
kb_number: KB0793481
last_modified: 2024-04-08
---

## \[Team Development\] - Not able to set Parent Instance in Team Dashboard - glide.apps.hub.current

  

### Issue

Team Development won't allow you to select the parent instance ID.

### Release

All releases

### Cause

Team Development dashboard populates 'glide.apps.hub.current' system property when you select a parent instance. The populated value is the parent's instance ID (stats.do), as seeing in the documentation: [Change the parent instance](https://docs.servicenow.com/csh?topicname=t_ChangeTheParentInstance.html&version=latest#t_ChangeTheParentInstance "Change the parent instance") 

If system property 'glide.apps.hub.current' is edited manually on \[sys\_properties\] table, Team Development dashboard cannot change the property afterward. This means that you cannot switch Parent from the dashboard

### Resolution

There are three possible solutions:

1.  Populate the parent instance ID manually.
2.  From another instance import the untouched property and flush the cache
3.  Clone down from the parent instance
