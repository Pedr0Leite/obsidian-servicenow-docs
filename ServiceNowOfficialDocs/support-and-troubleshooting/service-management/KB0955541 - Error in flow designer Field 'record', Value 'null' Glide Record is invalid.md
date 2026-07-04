---
title: "Error in flow designer: Field 'record', Value 'null': Glide Record is invalid"
aliases:
  - KB0955541
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0955541
kb_number: KB0955541
last_modified: 2025-06-10
---

## Error in flow designer: Field 'record', Value 'null': Glide Record is invalid

  

### Issue

When updating a record in Flow Designer, an error is thrown: Field 'record', Value 'null': Glide Record is invalid

### Release

All

### Cause

Check if the update action is updating a valid record. In the Configuration Details, look for the Runtime Value for Record. Is it set to a valid value? The error means that Flow Designer can't find a record to update, so the most likely reason is that whatever is defined in the Update Record action is incorrect.

  
**Reasons**:

-   Does the instance have domain separation? is the gliderecord in the same domain as the flow context?
-   is the gliderecord object referencing a valid record on the platform? Is the datapill configured as a valid gliderecord? 
-   check if a query business rule is blocking access

### Resolution

depending on the reasons stated above, additional configuration may be required
