---
title: "High level flow on populating the software installation record for \"SQL server\" product."
aliases:
  - KB2607144
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2607144
kb_number: KB2607144
last_modified: 2025-11-05
---

## High level flow on populating the software installation record for "SQL server" product.

  

1) During the discovery of a device we run a software installation probe " WMI: Installed Software" which brings all the installations with respective to H registry. Which lacks the capability to bring the edition value.  
  
2) And for the "SQL Server" product we need edition for accurate licensing. So we use pattern based to discovery where ADM probe triggers the pattern "MSSql DB On Windows"  based on the running process and in the pattern we pull the edition value and  Post sensor script "Sync Installed Software" will create a software install record. and mark the field "Created by application pattern" to "true".  
  
3) So we mark the software installation record which is created by the pattern with field "Created by application pattern" to "true" and other record which is populated by "WMI: Installed Software" to "Created by application pattern" to false.   
  
4) When the "SAM - Deduplicate Install Table" job runs the record with "Created by application pattern = true" will be marked Active install to true and other to false as we assume the record created with Pattern has the edition value.
