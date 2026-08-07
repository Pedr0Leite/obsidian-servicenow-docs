---
title: "Server is not discovered as a guest VM and no Virtualized by relationships are created"
aliases:
  - KB0787292
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0787292
kb_number: KB0787292
last_modified: 2024-04-08
---

## Server is not discovered as a guest VM and no Virtualized by relationships are created

  

### Issue

Discovery is run on a guest VM however no "Virtualized by::Virtualizes" relation is created between the guest VM and the associated hypervisor. The "is Virtual" (virtual) field is set to false, meaning that the host is a physical server instead of a guest VM.

### Release

All

### Cause

There are many scenarios where this would happen depending on the virtualization type, Discovery method used and instance configuration. The best source to find the possible root cause is to look at the "Virtual Computer Check" Business rule and inspect the script to follow the code. Below are some possible scenarios:

-   The Business Rule "Virtual Computer Check" has been customized or disabled;
-   serial\_number field is empty or not returning the expected value for a guest VM;
-   correlation\_id field not matching

### Resolution

-   Check if the Business Rule "Virtual Computer Check" has been customized or disabled;
-   Check if the serial\_number field is empty or is not returning the expected value for a guest VM. For example for VMWare, the serial\_number should be in the format VMware-<correlation\_id>, this correlation\_id should be the same for the related record in cmdb\_ci\_vmware\_instance
