---
title: "Currency not converting and GlideAggregate API not working as expected when Aggregating Date/Time fields"
aliases:
  - KB0782307
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0782307
kb_number: KB0782307
last_modified: 2024-04-08
---

## Issue

Currency is not converting and the GlideAggregate API is not working as expected when Aggregating Date/Time fields (typically on-prem)

## Resolution

The 'glide.db.mysql.aggregate.use\_timestampdiff' system property allows the GlideAggregate api to work properly, independent of the underlying app server system clock and database server system clock.  
  
Name = 'glide.db.mysql.aggregate.use\_timestampdiff'  
Type = 'true | false'  
Value = 'true'

Create a sys\_properties record containing this information on all affected MySQL/MariaDB instances.
