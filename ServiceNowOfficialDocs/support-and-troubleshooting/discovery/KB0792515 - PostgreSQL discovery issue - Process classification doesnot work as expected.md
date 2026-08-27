---
title: "PostgreSQL discovery issue - Process classification doesnot work as expected"
aliases:
  - KB0792515
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0792515
kb_number: KB0792515
last_modified: 2024-04-08
---

## PostgreSQL discovery issue - Process classification doesnot work as expected

  

### Issue

If a host that has PostgreSQL installed that is being discovered, though it has a process running with name 'postgres' and/or name contains 'postmaster', the process classification wouldn't be triggered and there would be no instances inserted under cmdb\_ci\_db\_postgresql\_instance.

### Cause

This issue would be seen because of the classifier conditions not being honoured. 

The 'PostgreSQL Instance' classifier out of the box contains 2 conditions-

1.  Name of the running process on the host should start with either postgres or postmaster.
2.  Parameters should contain -D.

Though both the conditions above are met, the process classifier wouldn't succeed in triggering the 'PorsgreSQL DB' Pattern.

### Resolution

To make the process classifier honour the conditions, follow the below steps

1.  Hop on to the instance and navigate to **Discovery Definition -> Processes.**
2.  Filter for the classifier name **'PostgreSQL Instance'**.
3.  Open up the classifier and focus on the '**Condition**' section.
4.  The 'Name starts with' parameter should be updated to **'postgres'** from **postgres** and **'postmaster'** from **postmaster**.
5.  Save or update the classifier post the change.

PostgreSQL instance process classifier before change-

![](/sys_attachment.do?sys_id=c8c020c5dbc838d0fec4fb24399619a0)

PostgreSQL instance process classifier after change-

![](/sys_attachment.do?sys_id=44c020c5dbc838d0fec4fb243996199f)

Post the update, the discovery process with honour the conditions of the process classification and we would see instance records getting created under 'cmdb\_ci\_db\_postgresql\_instance'.
