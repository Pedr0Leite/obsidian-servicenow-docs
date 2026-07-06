---
title: "How to troubleshoot the \"Update Approval Request\" inbound action"
aliases:
  - KB0812521
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0812521
kb_number: KB0812521
last_modified: 2026-06-29
---

## How to troubleshoot the "Update Approval Request" inbound action

  

### Issue

The user receives an approval email and sends an approval/reject response to the instance expecting the inbound action to fire. The error "Skipping 'Update Approval Request', did not create or update" is produced in the error message

### Release

All releases

### Cause

When an inbound email is processed and matches the conditions for the OOTB inbound action "Update Approval Request" to fire. This typical error message can occur:

"Skipping 'Update Approval Request', did not create or update"

When reviewing the inbound action, line 76 in the OOTB "update approval request" 

**return 'Approval email from ' + email.from + ' for task "' + displayValue + '" assigned to "' + current.approver.getDisplayValue()**

Where it will create an error message in the system logs:

"Approval email from SenderApproval@test.com for task " " assigned to "name\_of\_user\_that\_is\_the\_approval\_assignee" failed because: Sender email does not match approval assignee."

NOTE: If you see this message in the email logs "Classified as reply to 'null' via watermark 'Ref:<MSG\_NUMBER>' in message", it merely states that it cannot find the number to relate the original outgoing email that had the watermark, to begin with (due to number not being in the sysapproval\_approver table). Keep in mind that the purpose of the watermark is for the system to identify that the email is treated as a reply, which the system does acknowledge. There will be messages in the email logs list such as (Skipping 'notification\_name', email is type 'reply', which does not match Inbound Email Action's type 'new') to verify that.

### Resolution

Cross-reference the email sender's address with the approval assignee to confirm that there's a mismatch on the \[sys\_user\] table. This means that the approval/reject request must come from the email address of the approval assignee.

Be mindful that users who are delegate members of the approval assignee are allowed to send approve/reject requests to the instance so far as their delegate record is active, valid and the cc notification checkbox is check. Review this documentation for further information:

Delegate approval and tasks to another user:

[https://docs.servicenow.com/csh?topicname=t\_DelegateApprovalsTasks.html&version=latest](https://docs.servicenow.com/csh?topicname=t_DelegateApprovalsTasks.html&version=latest)
