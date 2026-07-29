---
title: "Not able to select \"sys_hub_flow_snaphost\" from lookup records action in scoped application"
aliases:
  - KB0852462
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0852462
kb_number: KB0852462
last_modified: 2024-04-08
---

## Not able to select "sys\_hub\_flow\_snaphost" from lookup records action in scoped application

  

### Issue

1\. Login to any Orlando instance

2\. Impersonate "system administrator".  
3\. Change the instance scope to "Agent Workspace". ( it happens in any scoped application)  
4\. Go to flow designer  
5\. Create a new flow and add "look up record" action  
6\. Try selecting the table - sys\_hub\_flow\_snapshot

### Release

Any Orlando Release

### Cause

Due to a system property

### Resolution

This is expected behavior of the platform. Since all Flow Designer tables were created in Global scope, the table access from other scope is not permitted with two bypass methods:

1) Login as admin user (then all tables will be accessible in any scope)

2) add the table to the list in sys\_properties->glide.ui.permitted\_tables and the table will be accessible. Please note that sys\_hub\_flow and sys\_hub\_action\_type\_definition are already a part of glide.ui.permitted\_tables. Adding an entry to this list will cause the table to be accessed outside of its scope in all platform, not just in Flow Designer.
