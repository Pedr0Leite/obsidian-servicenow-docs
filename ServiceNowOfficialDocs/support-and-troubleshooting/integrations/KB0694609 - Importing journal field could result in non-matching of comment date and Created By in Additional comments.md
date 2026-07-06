---
title: "Importing journal field  could result in non-matching of comment date  and Created By in \"Additional comments\""
aliases:
  - KB0694609
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0694609
kb_number: KB0694609
last_modified: 2024-04-07
---

## Importing journal field could result in non-matching of comment date and Created By in "Additional comments"

  

### Issue

Importing journal field could result in non-matching of comment date and 'Created By' in "Additional comments"

Problem

* * *

Importing journal field using xml from a different instance with a different time zone could result in non-matching of comment date  and Created By in "Additional comments"

Symptoms

* * *

In the XML Journal Field, when comparing the Comment date and the Created By in the "Additional comments", the date and Created By will not match.

![Created By and Comment Date](sys_attachment.do?sys_id=30ba2ca6db42b450e515c223059619f2 "it shows the incorrect text")

Cause

* * *

The sys\_history\_set entries related to on sys\_journal\_field records do not get automatically updated after import, if the journal fields have been added or manually updated.

Resolution

* * *

Delete all the **sys\_history\_set** entries related to the record imported. They will be automatically re-generated with the correct information.
