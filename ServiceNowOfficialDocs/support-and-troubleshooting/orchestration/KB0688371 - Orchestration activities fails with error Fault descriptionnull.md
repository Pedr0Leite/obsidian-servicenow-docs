---
title: "Orchestration activities fails with error: \"Fault description:null\"
aliases:
  - KB0688371
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0688371
kb_number: KB0688371
last_modified: 2024-04-07
---

## Orchestration activities fails with error: "Fault description:null"

  

### Issue

All Orchestration activities would immediately fail with an error: "Fault description:null"

![](sys_attachment.do?sys_id=d949e0eedb02b450e515c223059619f0)

### Cause

-   duplicate/Orphan MID entries in Orchestration application.
-   Update set or cloning

### Resolution

-   Log in to the instance.
-   Open the below two links:
    -   _https://<instance\_name>.service-now.com/ecc\_agent\_application\_list.do?sysparm\_query=name%3DOrchestration_
    -   _https://<instance\_name>.service-now.com/ecc\_agent\_application\_m2m\_list.do?sysparm\_query=_
-   You should find duplicate entries over there, i.e one MID server entry may be present twice.
-   Remove Orphan/Invalid entries.
-   Run a cache.do
-   Restart MID server
-   Try to run the Orchestration activities once again.
-   This time it should go good.

### Related Links

You can contact support if you need any assistance.
