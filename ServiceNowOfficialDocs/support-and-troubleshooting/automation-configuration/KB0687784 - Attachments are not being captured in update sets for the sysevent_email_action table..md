---
title: "Attachments are not being captured in update sets for the sysevent_email_action table."
aliases:
  - KB0687784
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0687784
kb_number: KB0687784
last_modified: 2025-04-07
---

## Attachments are not being captured in update sets for the sysevent\_email\_action table.

  

### Issue

Attachments are not being captured in update sets for the sysevent\_email\_action table.

### Release

  Jakarta+ 

### Cause

-   The sysevent\_email\_action table does not capture attachments by default.
-   The property `synch_attachments=true` must be set manually to enable this.

### Resolution

1.  Navigate to System Definition > Dictionary
2.  Add the property `synch_attachments=true` to the sysevent\_email\_action table.
3.  Verify that the tracking of attachments for this table has been enabled.
