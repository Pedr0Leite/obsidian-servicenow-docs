---
title: "Issue with the AD Spoke Action Error: Invalid hostname in connection or Host not reachable from Mid server"
aliases:
  - KB0793247
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0793247
kb_number: KB0793247
last_modified: 2024-04-08
---

## Issue with the AD Spoke Action Error: Invalid hostname in connection or Host not reachable from Mid server

  

### Issue

When using the "Is User In Group" AD action through Service Catalog flow designer, you get the error:

Error: Invalid hostname in connection or Host not reachable from Mid server.

Where other actions like "Add User To Group" and "Remove User from Group" are working fine.

### Cause

Likely a result of the flow not being updated to the new action id.

### Resolution

To fix this issue:

(1) Delete the pill in the if User Exists (Answer = true).

(2) Re-drag the Answer pill from the Is User In Group.  
  
What likely happened is that the previous pill referred to the old snapshot and since it was not changed when the flow was re-activated, it was not updated.  By removing it and re-dragging it, it forced the connection.
