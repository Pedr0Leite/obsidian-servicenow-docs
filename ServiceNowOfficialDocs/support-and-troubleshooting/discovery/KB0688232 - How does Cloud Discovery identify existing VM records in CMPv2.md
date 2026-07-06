---
title: "How does Cloud Discovery identify existing VM records in CMPv2?"
aliases:
  - KB0688232
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0688232
kb_number: KB0688232
last_modified: 2024-05-22
---

## How does Cloud Discovery identify existing VM records in CMPv2?

  

### Issue

# Symptoms

* * *

How does Cloud Discovery identify existing VM records in CMPv2?

# Release

* * *

Jakarta and Newer

# Resolution

* * *

-   The following URI describes the classes and fields Cloud Discovery uses for identification: /sn\_cmp\_response\_mapping\_list.do?sysparm\_query=used\_for\_identification%3Dtrue
-   For most Cloud CI's the object\_id is used as CI identification.

#
