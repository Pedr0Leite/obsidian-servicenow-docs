---
title: "New ESX Server records are not created."
aliases:
  - KB0754383
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0754383
kb_number: KB0754383
last_modified: 2024-04-07
---

## New ESX Server records are not created.

  

### Issue

# Symptoms

-   A single ESX record is updated multiple times.
-   On every update, the morid, ip address, etc. changes

# Release

All

# Cause

-   ESX data is fetched by the 'VMWare - vCenter ESX Hosts' probe.
-   The identifier for the ESX server is correlation\_id.
-   In this case, there were multiple ESX hosts with the same correlation\_id and serial number. Due to this, the same ESX record is getting updated.

# Resolution

-   Check with VMWare admin to understand why multiple ESX servers share the same correlation\_id and serial number.
-   To temporarily resolve the issue, modify the ESX identifier.
