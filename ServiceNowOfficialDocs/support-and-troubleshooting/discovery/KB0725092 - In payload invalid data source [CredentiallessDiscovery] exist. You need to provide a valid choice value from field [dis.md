---
title: "In payload invalid data source [CredentiallessDiscovery] exist. You need to provide a valid choice value from field [discovery_source] in table [cmdb_ci]"
aliases:
  - KB0725092
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725092
kb_number: KB0725092
last_modified: 2024-04-07
---

## In payload invalid data source \[CredentiallessDiscovery\] exist. You need to provide a valid choice value from field \[discovery\_source\] in table \[cmdb\_ci\]

  

### Issue

Discovery error: 

In payload invalid data source \[CredentiallessDiscovery\] exist. You need to provide a valid choice value from field \[discovery\_source\] in table \[cmdb\_ci\]  

The error wil often be seen when:

-   Credentialless discovery is enabled.
-   A discovery pattern is triggered which updates discovery\_source field to CredentiallessDiscovery

### Cause

The CredentiallessDiscovery choice is not present on sys\_choice table for Discovery Source column and table cmdb\_ci.

Note: This same error can happen for other discovery sources as well. The resolution would be the same as listed in the following "Resolution" section.

### Resolution

Note: Please test resolutions on a non-production instance first.

Manually create the record or import attached sys\_choice record.
