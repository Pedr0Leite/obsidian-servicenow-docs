---
title: "Attachment is not reflecting on the HR case activity page when user add an attachment after submitting a request from portal"
aliases:
  - KB0861826
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0861826
kb_number: KB0861826
last_modified: 2025-09-03
---

## Attachment is not reflecting on the HR case activity page when user add an attachment after submitting a request from portal

  

### Issue

After upgraded instance to Orlando patch 4, When a request is submitted via esc portal and if an attachment is attached to the request. post submission the attachment is deleted from the sys\_attachment table.

### Release

Orlando Patch 4

### Cause

The issue is because of custom ACL which is not allowing attachment for hr\_case table records.  

### Resolution

To resolve the issue:

1.  Modifying the custom ACL, for the new requests.
2.  Post that, Attachments will be populated for HR cases
