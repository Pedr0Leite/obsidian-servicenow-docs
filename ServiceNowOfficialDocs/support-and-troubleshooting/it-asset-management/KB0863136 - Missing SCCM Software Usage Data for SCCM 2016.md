---
title: "Missing SCCM Software Usage Data for SCCM 2016"
aliases:
  - KB0863136
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0863136
kb_number: KB0863136
last_modified: 2024-04-08
---

## Issue

Missing SCCM Software Usage Data for SCCM 2016

## Resolution

Configure the SAMP Usage 2016 Import to access the server

https://<<YOUR \_INSTANCE>>.service-now.com/nav\_to.do?uri=sys\_data\_source.do?sys\_id=b204643187700300562e4127f5cb0b44

and rerun the Main SCCM import

https://<<YOUR \_INSTANCE>>.service-now.com/nav\_to.do?uri=scheduled\_import\_set.do?sys\_id=4c29b91b5b623200dade2e65f0f91ae0

Note:

1\. Ensure the correct plugins are active

2\. Created reclamation rules for the correct product

Once SCCM 206 import runs the usage data does not comes in.
