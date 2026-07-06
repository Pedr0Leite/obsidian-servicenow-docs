---
title: "Discovery of Cloud Datacenter failed at 'List Resource Group' API"
aliases:
  - KB0688227
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0688227
kb_number: KB0688227
last_modified: 2024-04-07
---

## Discovery of Cloud Datacenter failed at 'List Resource Group' API

  

### Issue

-   When going to Cloud Account > Datacenters > Discover Now, discovery failed. Discovery Log shows: ITapp Azure Compute Manger.List resource groups -- Error
-   When goto Cloud API > Cloud API Trail, ListResourceGroups call is actually successful and returned data.

### Release

Jakarta and newer

#   

### Cause

-   The error can be resulted from variety of issues. When data is returned, it indicates issue with processing the data from cloud provider.
-   For this particular issue, root cause was due to the out of the box relationship type 'Contains::Contained By' was missing (sysid = 55c95bf6c0a8010e0118ec7056ebc54d). This resulted in Metadata Containment broken, ie, containment records referencing non-existing Relationship Type records.
-   Because of broken Metadata Containment rules, this caused Cloud CI reconciliation error resulting in failed discovery

### Resolution

If Discovery has been running, a new 'Contains::Contained By' relationship type should have been recreated. If not create a new relationship type with same name then do the following:

1.  Goto CMDB Metadata Containment Rules table list (recordscmdb\_metadata\_containment\_list.do)
2.  Find all records that references old 'Contains::Contained By' (cmdb\_metadata\_containment\_list.do?sysparm\_query=rel\_type.sys\_id%3D55c95bf6c0a8010e0118ec7056ebc54d)
3.  Update all and change 'Relation Type' field for these records to point to the new 'Contains::Contained By' relationship type that was recreated either by Discovery or manually.
