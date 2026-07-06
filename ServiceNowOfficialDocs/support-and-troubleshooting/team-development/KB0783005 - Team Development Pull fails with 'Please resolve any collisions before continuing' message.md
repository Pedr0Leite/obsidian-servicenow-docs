---
title: "Team Development: Pull fails with 'Please resolve any collisions before continuing' message"
aliases:
  - KB0783005
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783005
kb_number: KB0783005
last_modified: 2024-05-22
---

## Team Development: Pull fails with 'Please resolve any collisions before continuing' message

  

### Issue

Pull requests from Team dashboard fail with the following message although no collisions are listed in the 'Collisions' related list (regardless of the parent):

  

![](/sys_attachment.do?sys_id=877403c7dbf07810d58ea345ca9619bf)

### Release

All releases

### Cause

There are existing collisions from a previous pull that were (most likely) brought over from a Clone.

### Resolution

Identify and remove any existing collisions from the 'sys\_sync\_history\_version' table.

https://<INSTANCE\_NAME\_HERE>.service-now.com/sys\_sync\_history\_version\_list.do?sysparm\_query=state%3Dcollision&sysparm\_view=
