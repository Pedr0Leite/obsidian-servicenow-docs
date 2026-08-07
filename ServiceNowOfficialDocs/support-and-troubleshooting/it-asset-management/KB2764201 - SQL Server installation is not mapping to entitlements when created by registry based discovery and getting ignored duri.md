---
title: "SQL Server installation is not mapping to entitlements when created by registry based discovery and getting ignored during reconciliation"
aliases:
  - KB2764201
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2764201
kb_number: KB2764201
last_modified: 2026-02-06
---

## Issue

● Microsoft SQL Server software installation records exist but do not map to entitlements and show an ignore reason stating they were generated through registry based discovery and represent component services only

## Resolution

● This is expected behavior in SAM Pro for SQL Server installs discovered only via registry or probe based evidence  
● For entitlement mapping and compliance, ensure SQL Server installations are discovered using SQL Server application patterns so installs are created with Created by application pattern set to true  
● After pattern based discovery evidence is available, run reconciliation again and validate.
