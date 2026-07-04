---
title: "Subscription records are deleted when an SSO application is disconnected"
aliases:
  - KB3023577
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3023577
kb_number: KB3023577
last_modified: 2026-05-15
---

## Subscription records are deleted when an SSO application is disconnected

  

### Issue

When a Single Sign-On (SSO) application is disconnected in Software Asset Management (SAM), the associated subscription records are automatically deleted. This article explains the expected behavior.

### Release

ALL

### Cause

When an SSO application is disconnected, the following sequence occurs:

1.  The business rule _Delete related records on disconnect_ is triggered.
2.  This business rule deletes all associated SSO application role records linked to the disconnected application.
3.  Because SSO subscription records reference SSO application role records, and cascade delete is configured on that relationship, the related subscription records are also deleted automatically.

### Resolution

Expected behavior

This is expected behavior. Disconnecting an SSO application removes all dependent role and subscription data to maintain data integrity.

Resolution

If subscription records should be retained after disconnecting an SSO application, review the cascade delete configuration on the SSO subscription table's reference field before disconnecting the application. Contact ServiceNow Support if you require assistance evaluating this configuration.
