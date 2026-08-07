---
title: "ESX host serial number being replaced by chassis serial number after upgrading to esx 6.5 and 6.7"
aliases:
  - KB0717171
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0717171
kb_number: KB0717171
last_modified: 2024-04-07
---

## ESX host serial number being replaced by chassis serial number after upgrading to esx 6.5 and 6.7

  

### Issue

# Symptoms

* * *

After Upgrading to ESX Version  6.5 and 6, serial number of the ESX host is updated with Chassis serial number.

# Release

* * *

All Releases

# Cause

* * *

\-Servicenow discovery looks at the value serviceTag on the Vcenter to populate the serial number of the ESX server. This is a VMware bug where they have mapped the ServiceTag value with chassis serial number in versions starting from 6.5 and 6.7.

# Resolution

* * *

Vmware confirmed this is a known issue with VMWare ESX 6.5 and 6.7.  
VMWare has resolved the issue in ESX 6.7 U1 and has a pending fix for version (ESX 6.5) to be released in November’s 6.5 Patch 03
