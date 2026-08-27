---
title: "Duplicate records and relationships created when discovering solaris serves"
aliases:
  - KB0788298
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0788298
kb_number: KB0788298
last_modified: 2024-04-08
---

## Duplicate records and relationships created when discovering solaris serves

  

### Issue

Duplicate relationships and records created when discovering Solaris servers which have global and local zones. As an example, some of the duplicate records could be in cmdb\_ci\_vm\_instance, and cmdb\_ci\_solaris\_instance.

### Release

All currently supported releases.

### Cause

Solaris local zones and global zones return the same serial number.

### Resolution

Use SNEEP to configure serial numbers per zone. Consult your Solaris team or documentation on how to configure SNEEP for each local zone.

Discovery uses SNEEP to collect serial number information. The serial number returned by SNEEP may be the same if not configure for each zone. It is a requirement for discovery that each zone return a unique serial number. If not, zones may be overwritten and duplicate records created.

From our Solaris discovery documentation, "for Discovery to find Solaris computers, you must install SNEEP. Otherwise, Discovery cannot find the serial number. If using Solaris zones, each zone should be configured to return a unique value for the serial number. Otherwise, each zone will return the same number causing issues with CI identification." 

### Related Links

-   [Solaris discovery](https://docs.servicenow.com/csh?topicname=r_DataCollDiscoSolarisComputers.html&version=latest "Solaris discovery")
