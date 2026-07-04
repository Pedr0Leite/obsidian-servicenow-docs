---
title: "Verifying that an email event is created in the Event Log "
aliases:
  - KB0523579
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0523579
kb_number: KB0523579
last_modified: 2025-10-24
---

## Verifying that an email event is created in the Event Log

  

### Issue

Verifying that an email event is created in the Event Log

### Symptoms

If an email fails to send and does not appear in the Outbox or Sent mailbox, there may be an issue with the event it is linked to.

### Release

All

### Resolution

To Review the event log for issues:

1.   Navigate to **System Policy > Event Log** and locate the event 
    1.  If the event is not listed, open an incident ticket that includes the event name, the code that inserts the event, and where to locate the code (such as the particular business rule or workflow).
2.   After confirming that the event is listed, open the event record and verify that the **State** is set to **Error**.
    1.  If the **State** is not set to **Error**, open an Incident and include the following value from the event record:  **Name**, **Created Time**, and **User ID** fields.
3.  Click the Reprocess Event related link.
    1.  If the event fails to process, open an incident and include the following values from the event record:  **Name**, **Created Time**, and **User ID** fields.
