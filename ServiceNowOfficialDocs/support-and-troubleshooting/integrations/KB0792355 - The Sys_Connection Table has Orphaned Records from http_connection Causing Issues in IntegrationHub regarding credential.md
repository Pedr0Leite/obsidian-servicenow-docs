---
title: "The Sys_Connection Table has Orphaned Records from http_connection Causing Issues in IntegrationHub regarding credential and connection"
aliases:
  - KB0792355
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0792355
kb_number: KB0792355
last_modified: 2026-06-29
---

## The Sys\_Connection Table has Orphaned Records from http\_connection Causing Issues in IntegrationHub regarding credential and connection

  

### Issue

All connections profile created the instance are unavailable , they can't be used or deleted nor new connection profiles with same information can be created.

This issue may happen after a clone that that was done recently. 

![](sys_attachment.do?sys_id=1258559d47f14fd43542f24c736d435f)

### Release

All

### Cause

Cloning may create orphaned records on sys\_connection table from the http\_connection table when http\_connection and/or sys\_connection or excluded.

### Resolution

To avoid this problem when cloning, please do not exclude the following tables  
\* http\_connection  
\* sys\_connection
