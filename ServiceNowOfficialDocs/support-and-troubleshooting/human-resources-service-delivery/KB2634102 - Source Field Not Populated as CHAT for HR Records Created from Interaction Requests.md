---
title: "Source Field Not Populated as \"CHAT\" for HR Records Created from Interaction Requests"
aliases:
  - KB2634102
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2634102
kb_number: KB2634102
last_modified: 2026-01-01
---

## Source Field Not Populated as "CHAT" for HR Records Created from Interaction Requests

  

### Issue

HR records created from Interaction requests are not populating the Source field as "CHAT" when the Interaction type is CHAT.  
This behavior differs from Out-of-Box (OOB) expectations, where the Source field should be set correctly.  
The issue occurs in both production and sub-production environments, even after plugin updates.

### Release

Any Release

### Cause

A custom case creation variant prevented the related interaction record from being created correctly, which stopped the business rule responsible for populating the Source field from running.

### Resolution

-   Activate the standard case creation variant to ensure interaction-related records are created as expected.
-   Validate that the business rule responsible for copying the Source field runs correctly after the change.
-   Test the configuration in a sub-production environment before applying changes to production.
-   Confirm that the Source field populates as expected for new HR cases created from CHAT interactions.
