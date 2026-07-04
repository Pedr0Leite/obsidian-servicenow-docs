---
title: "Downgrade Software model licenses are not compliant after reconciliation"
aliases:
  - KB0819635
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0819635
kb_number: KB0819635
last_modified: 2024-04-08
---

## Downgrade Software model licenses are not compliant after reconciliation

  

### Issue

During reconciliation, ServiceNow is not considering latest version entitlements for the older version. As a result downgrade Software model licenses are not compliant. 

### Release

All

### Cause

Downgrade rights are created on the software models

### Resolution

Downgrade rights are created on the software models. Reconciliation only honors the downgrade rights on the entitlements. Please make sure downgrade rights are created on the entitlements.
