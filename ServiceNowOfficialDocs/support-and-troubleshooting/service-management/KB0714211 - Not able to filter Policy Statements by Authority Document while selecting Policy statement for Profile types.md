---
title: "Not able to filter Policy Statements by Authority Document while selecting Policy statement for Profile types"
aliases:
  - KB0714211
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0714211
kb_number: KB0714211
last_modified: 2025-01-03
---

## Not able to filter Policy Statements by Authority Document while selecting Policy statement for Profile types

  

### Issue

Not able to filter Policy Statements by Authority Document while selecting Policy statement for Profile types

### Release

Kingston and earlier

### Cause

The reason for no way to select policy statements which have been associated to an Authority Document is because the Policy statement is associated to the citations (from the Authority Document) in a many to many table named "sn\_compliance\_m2m\_statement\_citation". 

  

Whereas the policy statements are in the table "sn\_compliance\_policy\_statement". So the filter runs on the table "sn\_compliance\_policy\_statement". This table does not have any information regarding the association. 

  

Therefore the association with the authority documents cannot be determined in the filter.
