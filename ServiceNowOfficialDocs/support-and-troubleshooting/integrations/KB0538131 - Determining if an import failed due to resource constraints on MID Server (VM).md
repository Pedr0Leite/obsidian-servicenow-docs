---
title: "Determining if an import failed due to resource constraints on MID Server (VM)"
aliases:
  - KB0538131
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538131
kb_number: KB0538131
last_modified: 2024-04-30
---

## Determining if an import failed due to resource constraints on MID Server (VM)

  

### Issue

Determining if an import failed due to resource constraints on a MID Server installed on VM 

Problem

* * *

Scheduled or manual imports are not updating or creating records in the desired table.

  

Symptoms

* * *

-   Import set contains zero records
-   MID Server and instance logs contain _Blank column headers were found_ message

Cause

* * *

As part of the JDBC or LDAP import process, remote GlideRecord queries are performed against the glide instance to pull data from sys\_data\_source, ldap\_ou\_config, and ldap\_server\_config.

This can be interrupted by a socket error. 

Resolution

* * *

If possible, upgrade to the latest Dublin release or above.

However, if upgrading is not an option, we recommend installing the associated MID Server on a different physical machine that does not have the same network load.
