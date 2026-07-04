---
title: "First response time is not being captured on Case"
aliases:
  - KB0745263
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0745263
kb_number: KB0745263
last_modified: 2025-11-13
---

## First response time is not being captured on Case

  

### Issue

Even when the case has received a response, the first response time is not being recorded

### Cause

Conditions for Business Rule "First Response Time" are not met

### Resolution

Below business Rule is populating "First Response Time" on "sn\_customerservice\_case" table.

-   **Name**: Set First Response Time
-   **URL**: https://<your-instance>.service-now.com/nav\_to.do?uri=sys\_script.do?sys\_id=a9f63a34d70331004f1e82285e610382

Business rule conditions on "When to Run" section:

-   \[First Response time\] \[is\] \[empty\]  
    -   AND
-   \[Additional comments\] \[changes\] OR \[Close note\] \[is\] \[not empty\]  
    -   AND
-   \[State\] \[is\] \[Awaiting Info\] OR \[State\] \[is\] \[Resolved\]

Even if the Case is responded, it should satisfy the above conditions to populate "First Response Time" field.
