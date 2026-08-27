---
title: "Reviewing emails getting ignored by inbound actions"
aliases:
  - KB0535493
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0535493
kb_number: KB0535493
last_modified: 2026-05-29
---

## Reviewing emails getting ignored by inbound actions

  

### Issue

Emails sent to a ServiceNow instance are processed by each of the active Inbound Actions, but only if the specified conditions apply to the email.

Depending on the Inbound Action configuration, it is possible that an email could get skipped by all inbound actions, remaining ignored in the Inbox in **Ready** state instead of **Processed** state.

### Release

Any

### Cause

There are multiple conditions as well as configurable properties that determine whether an Inbound Email Action will ignore an email. For example you might configure your inbound action to match only emails classified as a reply to the Case table.

### Resolution

Each Inbound Email Action logs whether it skipped a particular email and why. For instance, you might have an Inbound Email Action named **Update Change** that matches on emails classified as reply.  When your action gets a chance to process an email classified as _new_, it logs an entry such as:

Skipping 'Update Change', email is type 'new', which does not match Inbound Email Action's type 'reply'

View the logged entries for the email by opening the email record from the email log. The **Default view** does not include the related log records, so you may need to first change the form view to **Inbox**.

1.  Right-click the email record header to show the context menu.
2.  Select **View**.
3.  Select **Inbox**.

Review the related log entries on the form to see why an email was skipped.

There is also a log entry describing whether the email was classified as **New**, **Reply**, or **Forward**. For emails classified as a reply, the log entry includes the reason why it was matched as a reply.

### Related Links

[Emails being received-ignored with an unknown error string](https://support.servicenow.com/kb_view.do?sysparm_article=KB0870995 "Emails being received-ignored with an unknown error string")

Configuring inbound action conditions: [Inbound Email Actions](https://docs.servicenow.com/csh?topicname=c_InboundEmailActions.html&version=latest "Inbound Email Actions")
