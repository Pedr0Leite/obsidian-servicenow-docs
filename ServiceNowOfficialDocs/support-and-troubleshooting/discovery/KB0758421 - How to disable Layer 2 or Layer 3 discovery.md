---
title: "How to disable Layer 2 or Layer 3 discovery"
aliases:
  - KB0758421
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0758421
kb_number: KB0758421
last_modified: 2024-04-07
---

## How to disable Layer 2 or Layer 3 discovery

  

### Issue

There can be times where it may be required to disable Layer 2 or Layer 3 discovery independently for troubleshooting issues within your instance.

### Resolution

Disabling Layer 2 discovery: Edit or create the system property **sa.create\_physical\_connections.active** and set the value to false.

Disable Layer 3 discovery: Edit or create the system property **glide.discovery.L3\_mapping** and set it to false.
