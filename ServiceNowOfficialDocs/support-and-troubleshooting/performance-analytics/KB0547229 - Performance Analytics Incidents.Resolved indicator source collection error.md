---
title: "Performance Analytics \"Incidents.Resolved\" indicator source collection error"
aliases:
  - KB0547229
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547229
kb_number: KB0547229
last_modified: 2024-05-09
---

## Issue

The Incidents.Resolved indicator source is included with the Performance Analytics default plug-in (com.snc.pa) as of the Eureka release. There is an issue where Incident.Resolved throws collection errors on the resolved\_at field.

## Resolution

During the implementation of Performance Analytics (PA), the Incidents.Resolved indicator source may need some adjustments.

The Incident Resolution Fields plug-in has been active by default since the Aspen release. If your instance was provisioned on a version before Aspen, these resolution fields are not present by default from the time when the instance was created. 

Some customers have made custom implementations to calculate resolution. If that is the case, check the field name. It could be similar to "u\_resolved" or "u\_resolved\_date." When this field is present and identified, the indicators and collector need to be adjusted accordingly.

Attached is a script (\_CHECK\_EXISTS\_COLUMNS.txt) that can be executed from the background scripts page to identify if there are fields missing that base system (out of box) collection would attempt to collect from.
