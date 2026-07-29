---
title: "Remediation to create allocations in SAM Pro "
aliases:
  - KB2956648
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2956648
kb_number: KB2956648
last_modified: 2026-04-15
---

## Remediation to create allocations in SAM Pro

  

### Issue

**Problem**  
Discovered users are not fetching with the User table in SAM Pro during Remediation Options for Microsoft 365 Integration, specifically for Exchange Plan 2 Licenses (mailbox accounts). The issue is observed in the samp\_discovered\_user record, where the user reference is blank, indicating the discovered user was never resolved to a sys\_user record. 

### Release

ALL

### Cause

**Root Cause**  
1\. The 'Create Allocation' option is not applicable for user subscription-based software models, leading to confusion.

2\. Discovered users without a sys\_user reference occur due to mismatched user principal names between subscription records and the sys\_user table.  
  

### Resolution

   
1\. Ignore the 'Create Allocation' option for user subscription-based software models, as recommended by ServiceNow.

2\. Recognize that discovered users without a corresponding sys\_user record are expected behavior, typically occurring when the user principal name in subscription records does not match any email or user ID in the sys\_user table.
