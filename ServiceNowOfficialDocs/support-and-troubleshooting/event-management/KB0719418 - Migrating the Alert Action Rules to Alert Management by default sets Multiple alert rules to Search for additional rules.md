---
title: "Migrating the Alert Action Rules to Alert Management by default sets Multiple alert rules to \"Search for additional rules\"
aliases:
  - KB0719418
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0719418
kb_number: KB0719418
last_modified: 2025-01-03
---

## Migrating the Alert Action Rules to Alert Management by default sets Multiple alert rules to "Search for additional rules"

  

### Issue

When migrating the Alert Action Rules to Alert Management, by default sets Multiple alert rules to "Search for additional rules". Which looks for other Alert Action Rules and actual Alert Management rule never works.

  

### Release

From London Release

### Cause

Before the London release ,alert action rules had the next logic:

  
If there are several rules for create incident , only one with highest priority will be selected.  
Same is true for KB and acknowledge .

  
But, if same alerts have different rules for incident, KB and acknowledge the algorithm wouldn’t stop only on the incident rule , it will try to check if there are matching rules for kb or acknowledge.

  
That is why after migration the flag is set to “search for additional rules” since the logic of incident, KB, acknowledge can be spread between different rules.

#   

### Resolution

If there is no additional rules(Creating KB, Incident and other) in Alert Action Rule, up on migrating to Alert Management, set Multiple alert rules to "Stop Searching for additional rules".
