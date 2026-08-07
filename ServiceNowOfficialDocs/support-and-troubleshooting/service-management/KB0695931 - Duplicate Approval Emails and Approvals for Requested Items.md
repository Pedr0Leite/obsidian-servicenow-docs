---
title: "Duplicate Approval Emails and Approvals for Requested Items"
aliases:
  - KB0695931
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695931
kb_number: KB0695931
last_modified: 2024-04-07
---

## Duplicate Approval Emails and Approvals for Requested Items

  

### Issue

# Symptoms

* * *

Users are receiving duplicate emails and duplicate approvals for the same requested item in service catalog when generated from an order guide on the service portal.

# Release

* * *

Kingston Patch 7

# Cause

* * *

A customized Order Guide widget in service portal is attempting several insertions of the request which causes a unique key violation error in the logs. For each attempt to insert, a workflow context is generated causing multiple approvals to be created.

# Resolution

* * *

Revert the order guide widget to the out of box version.
