---
title: "In  customer service case form, timeline is not updating \"with customer\" value"
aliases:
  - KB0782087
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0782087
kb_number: KB0782087
last_modified: 2024-02-05
---

## In customer service case form, timeline is not updating "with customer" value

  

### Issue

In customer service case form, the timeline is not updating "with customer" value.

### Cause

In 'sn\_customerservice\_case' table, the label used for State choice of value '18' has been customized.

### Resolution

Issue is resolved after reverting the label to OOB (Awaiting Info) .
