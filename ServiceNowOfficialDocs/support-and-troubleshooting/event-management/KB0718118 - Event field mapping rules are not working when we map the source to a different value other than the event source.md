---
title: "Event field mapping rules are not working when we map the source to a different value other than the event source"
aliases:
  - KB0718118
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0718118
kb_number: KB0718118
last_modified: 2025-01-17
---

## Event field mapping rules are not working when we map the source to a different value other than the event source

  

### Issue

Event field mapping rules are not working when we map the source to a different value other than the event source.

### Procedure

Event Compose rules always get executed before field mapping rules. If you are mapping the source value from composing fields, your field mapping rule source should match the source value after composing rules are executed.

Example:

From your event rule, if you are mapping source to value 'OEM' as opposed to the actual source of the event. Your Field mapping rule source should be 'OEM' as opposed to the source of the event. This is because composing fields always get triggered first and we change the source to OEM, not we look for all mapping rules with source as 'OEM' as opposed to the source of the event that is coming in.

### Release

All releases
