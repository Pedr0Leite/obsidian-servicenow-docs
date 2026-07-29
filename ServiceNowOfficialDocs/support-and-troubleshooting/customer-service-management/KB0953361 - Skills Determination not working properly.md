---
title: "Skills Determination not working properly"
aliases:
  - KB0953361
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0953361
kb_number: KB0953361
last_modified: 2025-01-03
---

## Skills Determination not working properly

  

### Issue

Even when the skill determination rules are active and the case matches them, the system does not seem to be relating a rule/skill on insert so it ends up offering the case to anyone within the assignment group. 

### Release

ALL

### Cause

Custom business rules that run slow and skip the OOB business rule that's responsible for determining the Skill Group - 

https://<instance<.service-now.com/sys\_script.do?sys\_id=8fd2493d7f932300a8b1bdc8adfa91b1&sysparm\_record\_target=sys\_script&sysparm\_record\_row=1&sysparm\_record\_rows=5254&sysparm\_record\_list=ORDERBYDESCsys\_updated\_on

### Resolution

There are a lot of custom business rules on sn\_customerservice\_case table that are doing updates on case table which and running slow.

The custom slow business rules are skipping the OOB Business rule - 

https://<instance>.service-now.com/sys\_script.do?sys\_id=8fd2493d7f932300a8b1bdc8adfa91b1&sysparm\_record\_target=sys\_script&sysparm\_record\_row=1&sysparm\_record\_rows=5254&sysparm\_record\_list=ORDERBYDESCsys\_updated\_on
