---
title: "Reject Button Missing in Mobile Approval Screens After Upgrade"
aliases:
  - KB2626893
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2626893
kb_number: KB2626893
last_modified: 2026-01-03
---

## Reject Button Missing in Mobile Approval Screens After Upgrade

  

### Issue

After upgrading the HR Service Delivery for Mobile and Service Catalog for Mobile plugins (Yokohama version), the Reject button disappeared from approval screens in NowMobile for RITM and HR cases.  
Log analysis showed that the button was deactivated immediately after the plugin update by upgrade scripts, without any explicit business rule triggers.

### Release

Yokohama

### Cause

The issue occurs because the upgrade script responsible for cleaning up old configurations was executed more than once. This script is designed to run only during the initial plugin upgrade and determines which buttons to deactivate based on customization status. When it was manually reactivated and executed again, both old and new Reject buttons were deactivated, causing them to disappear from the mobile interface.

### Resolution

-   The Reject button disappeared because the upgrade script ran twice instead of once, deactivating all button instances.
-   To fix this, review the mobile UI button configuration and ensure:
    -   The new Reject button is set to Active = True.
    -   Any deprecated button remains inactive.
-   Avoid manually rerunning the upgrade script in the future, as it is intended to execute only once during the plugin upgrade process.
-   If similar issues occur, check the mobile UI configuration for button records and confirm their active status.
