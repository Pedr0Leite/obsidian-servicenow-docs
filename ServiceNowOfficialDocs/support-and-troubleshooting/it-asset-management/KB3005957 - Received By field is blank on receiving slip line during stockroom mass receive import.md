---
title: "Received By field is blank on receiving slip line during stockroom mass receive import"
aliases:
  - KB3005957
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3005957
kb_number: KB3005957
last_modified: 2026-05-07
---

## Issue

The Received By field on the receiving slip line remains blank when assets are received in bulk through the stockroom import flow. This occurs because the purchase order (PO) receive flow runs in a background or automated context, such as through a scheduled job. In this context, the session runs as the system user. Because there is no corresponding user record for the system user, the Received By field returns an empty value. Some customers require this information for critical audit purposes.

## Resolution

To resolve this issue, update to one of the fixed versions listed above. The fix includes the following code change in the ProcurementUtils script include.

To locate the script include, navigate to System Definition > Script Includes and search for ProcurementUtils.

Previous code:

```
rsl.received_by = gs.getUserID();
```

Updated code:

```
var receivedBy = !gs.nil(receivedUser) ? receivedUser : gs.getUserID();
rsl.received_by = receivedBy;
```

This change ensures that when a valid receiving user is available, that user is recorded in the Received By field. If no receiving user is identified, the system falls back to the current user ID.

## Additional Information

This issue is addressed in PRB1970134.
