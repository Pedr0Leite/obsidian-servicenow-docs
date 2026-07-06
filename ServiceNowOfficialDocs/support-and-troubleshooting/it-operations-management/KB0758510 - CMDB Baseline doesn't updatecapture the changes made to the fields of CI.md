---
title: "CMDB Baseline doesn't update/capture the changes made to the fields of CI"
aliases:
  - KB0758510
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0758510
kb_number: KB0758510
last_modified: 2025-04-07
---

## CMDB Baseline doesn't update/capture the changes made to the fields of CI

  

### Issue

-   CMDB Baseline created for "cmdb\_ci\_hardware" table doesn't capture the changes made to the fields of any CIs.

![](sys_attachment.do?sys_id=e05a02b8dbc070d016d2a345ca96195b)

### Release

-   Any release

### Cause

The probable cause would be,

-   some CIs may not have existed at the time the baseline was created, and
-   it only lists changes of the CI's since the baseline was re-created.

### Resolution

In order to fix the issue,

-   Delete the existing Baseline which is in place and create a new Baseline. (e.g. Name "Hardware baseline" for "cmdb\_ci\_hardware" table.)
-   Once the baseline calculation gets completed, take 2 CI's from different table and perform the changes to the fields.
-   In this case, a CI from the table "u\_cmdb\_ci\_hybrid\_device" and another CI from "cmdb\_ci\_linux\_server" were taken and tried changing a few field attributes.
-   The changes made to the CI from the table "u\_cmdb\_ci\_hybrid\_device" weren't captured in the baseline because the corresponding table "u\_cmdb\_ci\_hybrid\_device" was not audited.

![](sys_attachment.do?sys_id=685a02b8dbc070d016d2a345ca96195c)

-   The changes made to the CI from the table "cmdb\_ci\_linux\_server" were captured in the baseline because the table "cmdb\_ci\_linux\_server" was audited.

![](sys_attachment.do?sys_id=ec5a02b8dbc070d016d2a345ca96195d)

![](sys_attachment.do?sys_id=645a02b8dbc070d016d2a345ca96195f)

### Related Links

### Behavior:

-   The baseline for the table will be calculated only when the corresponding table is Audited.

Documentation reference: [Baseline CMDB](https://docs.servicenow.com/csh?topicname=c_BaselineCMDB.html&version=latest "Baseline CMDB")
