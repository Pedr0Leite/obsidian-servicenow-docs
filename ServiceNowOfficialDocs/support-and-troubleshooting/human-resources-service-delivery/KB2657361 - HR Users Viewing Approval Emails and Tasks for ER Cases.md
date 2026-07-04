---
title: "HR Users Viewing Approval Emails and Tasks for ER Cases"
aliases:
  - KB2657361
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2657361
kb_number: KB2657361
last_modified: 2025-12-17
---

## HR Users Viewing Approval Emails and Tasks for ER Cases

  

### Issue

HR users with only the HR role can view approval-related emails and tasks for Employee Relations (ER) cases they should not access. 

### Release

Yokohama

### Cause

·  Insufficient access controls on sysapproval\_approver and related tables.

·  Product defect tracked under PRB1901163.

### Resolution

·  Fix delivered in Yokohama Patch 7 to correct access control logic.

·  Upgrade to Yokohama Patch 7 or later to resolve the issue.

·  Subscribe to PRB1901163 for updates.
