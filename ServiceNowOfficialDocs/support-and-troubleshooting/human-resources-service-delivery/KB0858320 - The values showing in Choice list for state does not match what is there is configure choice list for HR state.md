---
title: "The values showing in Choice list for state does not match what is there is configure choice list for HR state"
aliases:
  - KB0858320
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0858320
kb_number: KB0858320
last_modified: 2025-09-03
---

## Issue

The values showing in Choice list for state does not match what is there is configure choice list for HR state on sn\_hr\_core\_case\_relations record.

## Resolution

Since there were so many custom choice values created on sn\_hr\_core\_case\_relation which on sys\_choicelist they override the OOB values so what you see is extected.

  
If you wish to see how its OOB , you would need to delete the custom choice list you created , save , clear cache and test again.  
Before deleting take a backup of them.
