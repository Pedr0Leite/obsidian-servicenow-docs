---
title: "Understand inbound email flow behavior with Run as property settings"
aliases:
  - KB0821206
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0821206
kb_number: KB0821206
last_modified: 2026-02-26
---

## Understand inbound email flow behavior with Run as property settings

  

### Issue

Inbound email triggered flows continue to run as the email sender even after setting the Run as property to System User in Flow Designer. This behavior persists despite saving or reactivating the flow. While test mode correctly runs as the system user, actual flow execution runs as the initiating user. 

### Release

All supported releases

### Cause

This is expected default behavior for inbound email flow triggers.

### Resolution

Inbound email triggered flows always run as the user who sent the email (or as the guest user if the email sender cannot be resolved to a sys\_user record). 

Unlike other flow types where you can choose to run as either system user or the initiating user, inbound email flows follow these rules: 

-   The flow always executes as the email sender.
-   If the system cannot identify the sender, the flow runs as the Guest user.
-   All actions in the flow are subject to the sender's access control list (ACL) restrictions.

To test access controls for an inbound email flow:

1.  Impersonate a typical inbound email user.
2.  Manually trigger the flow to verify behavior.

If your flow requires elevated privileges that the email sender may not have: 

1.  Move those actions to a subflow.
2.  Configure the subflow with Run as System property.
3.  The subflow runs with system privileges even though the main flow runs as the email sender.

### Related Links

For more information, see the product documentation, [Workflow Studio flow trigger types](https://docs.servicenow.com/csh?topicname=flow-triggers.html&version=latest "Flow Trigger Types")
