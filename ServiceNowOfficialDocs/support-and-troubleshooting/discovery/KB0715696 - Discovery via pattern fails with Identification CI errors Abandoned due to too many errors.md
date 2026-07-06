---
title: "Discovery via pattern fails with \"Identification CI errors: Abandoned due to too many errors\""
aliases:
  - KB0715696
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0715696
kb_number: KB0715696
last_modified: 2026-06-10
---

## Discovery via pattern fails with "Identification CI errors: Abandoned due to too many errors"

  

### Issue

The Discovery process may fail with an error on the pattern logs where you can see: 

"Identification CI Errors: Abandoned due to too many errors".

### Cause

This is possibly caused by duplicates on the relationship type table \[cmdb\_rel\_type\].

### Resolution

1 - Enable the Debug for the CI Identification parameter on the Discovery properties ( glide.discovery.debug.ci\_identification ).  
  
2 - Quick discovery the affected device.

3 - Check the logs on the syslog\_list.do, the CI Identification ones would be like: 

```
identification_engine : DUPLICATE_RELATIONSHIP_TYPES Duplicate relationship type records exists with name [Master of::Stack Member of] 
```

4 - Figure out which relationship type has got duplicates. Go to cmdb\_rel\_type\_list.do and filter by name, there should be only one record for the same type.

5 - Check on the cmdb\_rel\_ci\_list.do if there is any relationship using that particular type, in which case a deletion would break the link.  
  
6 - Delete the record that is not being used.
