---
title: "Error: Found duplicate cmdb_rel_type records with name: Hosted on::Hosts having sys_ids: xxx, yyy: no thrown error"
aliases:
  - KB0727668
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727668
kb_number: KB0727668
last_modified: 2024-04-07
---

## Issue

# Symptoms

* * *

After Discovery, the following error occurs:

"**Found duplicate cmdb\_rel\_type records with name: Hosted on::Hosts having sys\_ids: xxx, yyy: no thrown error**."

# Cause

* * *

There are two records of the same relation type in the cmdb\_rel\_ci table. The sys id's of them are different.

# Resolution

* * *

There are some OOTB script include that rely on the hardcoded sys\_ids of the cmdb\_rel\_type table.  
  
For example "**MetadataRulesProvider"** script include uses the hardcoded Sys ID's for RUNS\_ON, HOSTED\_ON, CONTAINS, CLUSTER\_OF relationship types. So it is not advisable to change the Sys ID's of the OOTB cmdb\_rel\_type records.  
  
Delete the duplicate rel type records and import the records from OOTB to avoid any issues with discovery/Service Mapping.

# Additional Information

* * *

Since the design is not ideal with hardcoded Sys ID's a problem PRB1290379 was created to address issue in future releases.
