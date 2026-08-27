---
title: "Limit on exporting report in XML"
aliases:
  - KB0815332
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815332
kb_number: KB0815332
last_modified: 2024-04-08
---

## Issue

Exporting an excel report failed which contains 811893 records.

Even after setting the glide system property "glide.ui.export.limit" to value 1000000 the export is not successful. 

glide.ui.export.limit - is used for exporting CSV and excel

## Resolution

**_"glide.ui.export.limit"_** property is used to increase the export limit for "**CSV**" and "**Excel**"

"**com.glide.processors.XMLProcessor.record\_count** " is used to increase the export limit for XML.  
  

## Additional Information

[https://docs.servicenow.com/csh?topicname=c\_ExportLimits.html&version=latest](https://docs.servicenow.com/csh?topicname=c_ExportLimits.html&version=latest)
