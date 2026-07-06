---
title: "Approval emails are not being generated for requested items"
aliases:
  - KB0725194
tags:
  - servicenow
  - support-kb
  - approvals
  - notifications
  - sysapproval_approver
  - service-catalog
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725194
kb_number: KB0725194
last_modified: 2025-06-10
---

## Approval emails are not being generated for requested items

  

### Issue

Ensure that approval emails are automatically sent to approvers for requested items by following the steps in this article.

### Release

All Releases  

### Cause

The system fails to send approval emails to approvers for requested items, contrary to the expected behavior of automatically notifying them via email. For any email to be sent from your instance, an email notification needs to be defined. 

The cause is because there is no notification defined for approval records for RITMs.

### Resolution

To define an email notification:

1\. Go to **System Notification > Email > Notifications**

2\. Select **New.**

3\. Choose the table, **Approval \[sysapproval\_approver\]**

4\. Complete the following fields as necessary for your instance:

-   **Name**
-   **Send when**

5\. Enter the Condition: **\[Approval for.Number\]\[starts with\]\[RITM\]**

6\. Complete the following fields:

-   **Who will receive**
-   **What it will contain** 

7\. Select **Submit**

8\. Test the results.

## Related

- [[KB0723056 - Approving requests through email notifications, Inbound actions, sysapproval_approvers and user table]] - overview of the approval email/inbound-action pipeline
- [[KB0785021 - Approval request reply email does not approve the associated record]] - approval reply-email troubleshooting
- [[KB0812521 - How to troubleshoot the Update Approval Request inbound action]] - inbound action side of approval processing
- [[KB0727617 - Access referenced fields in a notification record against the Approval table]] - building the approval notification body
- [[send-notification-action]] - Flow Designer notification action reference

