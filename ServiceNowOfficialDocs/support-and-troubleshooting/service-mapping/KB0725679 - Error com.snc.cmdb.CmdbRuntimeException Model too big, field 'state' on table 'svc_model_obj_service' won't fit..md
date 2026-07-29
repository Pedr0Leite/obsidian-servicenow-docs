---
title: "Error: com.snc.cmdb.CmdbRuntimeException: Model too big, field 'state' on table 'svc_model_obj_service' won't fit. "
aliases:
  - KB0725679
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725679
kb_number: KB0725679
last_modified: 2024-04-07
---

## Error: com.snc.cmdb.CmdbRuntimeException: Model too big, field 'state' on table 'svc\_model\_obj\_service' won't fit.

  

### Issue

# Symptoms

* * *

ServiceMapping throws error like:

com.snc.cmdb.CmdbRuntimeException: Model too big, field 'state' on table 'svc\_model\_obj\_service' won't fit. Field size: 9,320,000. Actual value size: \[some\_larger\_value\_other\_than\_9,320,000\]

# Release

* * *

Any 

# Cause

* * *

The 'State' field on the table 'svc\_model\_obj\_service' has a default value of 9,320,000 characters. 

In some cases where we have larger maps, this might not be enough and this error will be thrown. 

# Resolution

* * *

1) Go to the "svc\_model\_obj\_service" table

2) Open the sys\_dictionary entries for that table

3) Find the "state" field

4) Modify the field size of that dictionary entry to something higher than the second number you see in that error message.

For example:

ERROR: 

com.snc.cmdb.CmdbRuntimeException: Model too big, field 'state' on table 'svc\_model\_obj\_service' won't fit. Field size: 9,320,000. Actual value size: 11,484,666

Change the size of the field to 12,000,000.

# Additional Information

* * *

Note: Once you increase the size of the field you should not decrease the size. You can only increase further. Only if necessary.
