---
title: "Flow fails with error: com.glide.transform.transformer.exceptions.InvalidStructureException: JsonStreamParser[44087]: Exceeded maximum allowed length 16384 for a string"
aliases:
  - KB0965644
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0965644
kb_number: KB0965644
last_modified: 2026-06-04
---

## Flow fails with error: com.glide.transform.transformer.exceptions.InvalidStructureException: JsonStreamParser\[44087\]: Exceeded maximum allowed length 16384 for a string

  

### Issue

Flow fails with error: com.glide.transform.transformer.exceptions.InvalidStructureException: JsonStreamParser\[44087\]: Exceeded maximum allowed length 16384 for a string

or you are seeing error: Flow state changed from IN\_PROGRESS to PRESUMED\_INTERRUPTED due to inactivity after 28800 seconds for contextId: <context\_id> claimed by other node: <instance node> with transaction: <transaction\_id>

### Resolution

Create a new sys\_properties record:  
com.glide.transform.json.max-partial-length

Type: integer

Value: 65536
