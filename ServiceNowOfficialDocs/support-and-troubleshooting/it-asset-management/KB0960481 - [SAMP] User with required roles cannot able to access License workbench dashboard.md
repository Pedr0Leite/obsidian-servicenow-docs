---
title: "[SAMP] User with required roles cannot able to access License workbench dashboard"
aliases:
  - KB0960481
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0960481
kb_number: KB0960481
last_modified: 2024-05-11
---

## Issue

-   The user who has the "**sam\_user**" & "**sam\_admin**" role cannot able to access the License Workbench dashboard. When tried access it gives the error "**You do not have permission to use this page**".

![](sys_attachment.do?sys_id=2f0dd9201bbb2010d01143f6fe4bcbb1)

## Resolution

-   To resolve this set the "**Accessibility enabled**" to "true" and then to "false" back for the affected user from "**System settings >> Accessibility**".
