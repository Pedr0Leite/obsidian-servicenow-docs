---
title: "Issue while running discovery for Storage Devices using Compellent CIM server (e.g. Dell Storage Center)"
aliases:
  - KB0696211
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696211
kb_number: KB0696211
last_modified: 2024-04-07
---

## Issue while running discovery for Storage Devices using Compellent CIM server (e.g. Dell Storage Center)

  

### Issue

# Symptoms

* * *

When discovering Storage Devices using Compellent CIM server (e.g. Dell Storage Center), Probe SMIStorageServer returns empty result, and related information is not collected for Storage Server CI (cmdb\_ci\_storage\_server): e.g. below information is empty in related list: storage devices / storage volumes / storage pools / storage controllers / iSCSI Exports etc

# Release

* * *

Jakarta

# Cause

* * *

Compellent CIM server requires "/cimom" to be included in the URL.

# Resolution

* * *

1> Navigate to: MID Server > Script Include > search for CIM Query > make it inactive 2> Import attached script include: "new CimQuery Script Include.xml"   Once upgraded to Kingston in the future, revert to out of box script include.
