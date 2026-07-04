---
title: "SLA Definitions are not creating SLAs on Cases"
aliases:
  - KB0778499
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0778499
kb_number: KB0778499
last_modified: 2024-04-08
---

## SLA Definitions are not creating SLAs on Cases

  

### Issue

The user has demo data SLA Definitions on sn\_customerservice\_case for varying priority levels. When the SLA Start conditions match on a Case record, the task\_sla which is expected to attach does not attach.

### Cause

The demo data SLA Definitions are corrupt (more details below).

### Resolution

It was found that there was some issue with the user's SLA Definitions on their demo instance for the sn\_customerservice\_case table. The SLAs were not even being evaluated in the localhost logs when "enable debugging" for the SLA Definition was checked. However, when a new SLA Definition was made, the conditions were being evaluated properly and the appropriate task\_sla attached.  
  
It is worth noting that doing an Insert and Stay on the affected demo data SLA Definitions did rebuild them properly, further proving that the previous SLA Definitions were somehow corrupted.  
  
Therefore, it is recommended that if a user is facing the same behavior, let them (1) deactivate or remove the SLA Definitions which are not functioning and (2) recreate the corrupted definitions entirely so that they register properly in the backend and work as intended.
