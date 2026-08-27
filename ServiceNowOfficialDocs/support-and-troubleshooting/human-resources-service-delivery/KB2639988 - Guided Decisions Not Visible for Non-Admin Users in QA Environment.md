---
title: "Guided Decisions Not Visible for Non-Admin Users in QA Environment"
aliases:
  - KB2639988
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2639988
kb_number: KB2639988
last_modified: 2025-12-16
---

## Guided Decisions Not Visible for Non-Admin Users in QA Environment

  

### Issue

Guided decisions created in HR Service Delivery were not visible in the QA environment for non-admin users, even those with the guidance\_user role.  
Only HR admins could access guided decisions, blocking deployment and impacting multiple workflows.

### Release

Any Release

### Cause

Missing ACLs in QA prevented visibility for non-admin users.  
A known product defect (PRB1833671) affects guided decision access for users without the HR Admin role in certain plugin versions.

### Resolution

-   Create custom ACLs in the Human Resources: Core scope to allow users with the sn\_hr\_core.case\_writer role to access guided decisions.
-   Upgrade to Agent Workspace for HR Case Management plugin v4.0 (Yokohama release) or later for a permanent fix.
-   Problem record PRB1833671 tracks this issue for future platform updates.
