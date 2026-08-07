---
title: "HR case not changing the state to Approved as per the UI action 'Submit\" logic"
aliases:
  - KB0864283
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0864283
kb_number: KB0864283
last_modified: 2025-09-03
---

## HR case not changing the state to Approved as per the UI action 'Submit" logic

  

### Issue

-   The approval state does not change to approved when an HR case is submitted

### Release

-   Paris Patch 1 Hot Fix 5

### Cause

-   The issue is because if custom UI action taking the precedence of OOB Submit UI action.

### Resolution

After the UI action XML is updated with the change in Order, the HR cases are setting the Approval state is Approved.
