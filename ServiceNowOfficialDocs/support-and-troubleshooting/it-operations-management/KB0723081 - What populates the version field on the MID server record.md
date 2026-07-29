---
title: "What populates the version field on the MID server record?"
aliases:
  - KB0723081
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0723081
kb_number: KB0723081
last_modified: 2024-04-07
---

## Issue

#   

This article explains how the version field on the MID server record is populated. When the MID server files are downloaded, the version information is stored in a **_mid-core.meta_** file. The content of this file is then pulled and sent to the instance as part of ECC queue record with Topic _queue.stats_ which when processed populates the version field on the MID server record.

The mid-core.meta file is present in the following location:  
agent>package>meta
