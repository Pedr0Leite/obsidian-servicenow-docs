---
title: "Midserver stuck in upgrading state due to pre-upgrade check failure"
aliases:
  - KB0696133
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696133
kb_number: KB0696133
last_modified: 2025-09-17
---

## Issue

MID server is stuck in 'Upgrading' state.

If you open the logs for MID server and it shows following error:

SEVERE \*\*\* ERROR \*\*\* Aborting MID Server upgrade due to pre-upgrade check failure: Unable to verify file permissions: null  
  
SEVERE \*\*\* ERROR \*\*\* Unable to refresh packages. Platform upgrade is currently in progress.

## Resolution

1.  Check the MID server service on the host and see what account the Log On user is set to. 
2.  If it is something other than Local Admin, change it to the local admin user by right-clicking on the service > properties > Log On tab > select first radio button to run as local user. 
3.  Restart mid server service. 
4.  Once the upgrade is complete, you can change the user back to what it was and restart the service again to apply the change. 

While this represents a single potential cause of upgrade failure, other contributing factors may exist.

Nonetheless, it is a commonly observed issue when the MID Server remains in a persistent "Upgrading" state.
