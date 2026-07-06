---
title: "Prevent duplicates or misclassification of IP switches and routers during discovery"
aliases:
  - KB0693298
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0693298
kb_number: KB0693298
last_modified: 2025-07-17
---

## Prevent duplicates or misclassification of IP switches and routers during discovery

  

### Issue

Duplicate switch and router records are being created when a discovery schedule is running, resulting in misidentified existing configuration items (CI).

### Release

Any release

### Cause

Configuration item (CI) reclassification—changing between a router and a switch—can lead to duplicates when:

-   The Identification Reconciliation Engine receives two simultaneous payloads from discovery with same name for IP Switch and IP Router. 

When this happens:

-   The existing record is deleted and a new one is inserted with the same sys ID, but a second payload may arrive during this process.
-   The second payload cannot match on name, resulting in a duplicate record being created.

### Resolution

To prevent misclassification between routers and switches:

-   Ensure the system OID (object ID) is included in the SNMP - Classify probe payload.
-   Under Standard Network Switch and Standard Network Router classification, make sure that **sysoid** does not equal an empty value.
