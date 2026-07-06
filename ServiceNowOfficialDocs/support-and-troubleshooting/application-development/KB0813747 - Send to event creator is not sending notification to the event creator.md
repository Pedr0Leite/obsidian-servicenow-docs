---
title: "Send to event creator is not sending notification to the event creator "
aliases:
  - KB0813747
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813747
kb_number: KB0813747
last_modified: 2026-07-02
---

## Send to event creator is not sending notification to the event creator

  

### Issue

When a notification is configured to send to the approver of a request and **Send to event creator** is set to True, the notification sends to the approver only — not to the user who triggered the event.

### Release

### Cause

By design, users are not notified for actions they perform themselves. The following scenarios illustrate how \*\*Send to event creator\*\* controls notification behaviour.

Consider a notification triggered when a RITM request moves to approval. The notification is sent to an approver group with four members (User A, User B, User C, and User D). User A moves the RITM to the approval stage.

**Scenario 1 — Send to event creator is set to True**

All four members receive the notification email. User A is added as the event creator and is included in the distribution.

**Scenario 2 — Send to event creator is set to False**

Only three members receive the notification. User A is excluded as the event creator. Users B, C, and D receive the notification.

### Resolution

In scenarios where users must be notified even for actions they triggered, turn on Send to event creator on the notification record.

To turn on or turn off Send to event creator:

1\. Navigate to All > System Notification > Notifications.

2\. Open the relevant notification record.

3\. Select Advanced view.

4\. Select the Who will receive tab.

5\. Select or clear the Send to event creator option as needed.

6\. Click Update to save the notification

7\. Test the notification workflow to verify email is sent to event creator

### Related Links

[Email Notification Not Sent When Event Creator and Recipient Are the Same User](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2903106)
