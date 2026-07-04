---
title: "User able to add comments even after case is closed"
aliases:
  - KB0993940
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0993940
kb_number: KB0993940
last_modified: 2025-09-12
---

## Issue

End users can add comments from the **ESC portal** on their cases even after the case has been **closed completely.**

## Resolution

#### **Solution:**

In order to achieve the requirement, follow the below steps:

1.  Navigate to the **ACL table**
2.  Filter out the write ACLS on "**sn\_customerservice\_case.comments**" and "**sn\_customerservice\_case**"
3.  Modify the existing ACLs to restrict users to add comments on the closed cases by adding the condition "**State is not closed**"
