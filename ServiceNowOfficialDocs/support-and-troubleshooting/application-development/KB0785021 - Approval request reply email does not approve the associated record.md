---
title: "Approval request reply email does not approve the associated record"
aliases:
  - KB0785021
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0785021
kb_number: KB0785021
last_modified: 2026-04-02
---

## Approval request reply email does not approve the associated record

  

### Issue

A user replies to an approval request reply email, approving the request, but the associated record does not approved.

### Release

All releases.

### Cause

The user replying to the approval request email is not one of the required approvers for the record.

### Resolution

Open the record that needs to be approved.

Check the Approvers related list.

One of the users in the Approvers related list must approve the request.

It's possible that the approval request email was sent or forwarded to other users in addition to the required approvers. If one of these non-approver users replies, approving the request, the approval reply email will not approve the record because the sender is not a required approver. Assuming that out-of-box configurations are in place, this should also result in an outbound email containing a message similar to this:

The approval for "REQnnnnnnn" failed because the approval response email was not sent by the approver. The Approver is FirstName LastName with email address firstname.lastname@example.com

One of the required approvers in the record's Approvers related list must reply to the approval request email in order for the record to be approved via email.

### Related Links

An approval request may be configured to require multiple approvers, in which case, all approvers must approve the request.

For additional information about approval emails, see this knowledge article: [Approving requests through email: notifications, Inbound actions, sysapproval\_approvers and user table](https://support.servicenow.com/kb_view.do?sysparm_article=KB0723056 "Approving requests through email: notifications, Inbound actions, sysapproval_approvers and user table")
