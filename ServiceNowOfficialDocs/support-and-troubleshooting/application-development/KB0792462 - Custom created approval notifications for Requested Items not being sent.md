---
title: "Custom created approval notifications for Requested Items not being sent"
aliases:
  - KB0792462
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0792462
kb_number: KB0792462
last_modified: 2026-06-11
---

## Custom created approval notifications for Requested Items not being sent

  

### Issue

When a requested item requires an approval, an email notification should be sent out.

The business rule Approval Events (Tasks) uses the sc\_request table for requested items.

### Cause

A custom email notification is used for requested item approval instead of the out-of-box 'Approval Record Assigned - RITM,' and is missing information in "When to send".

### Resolution

The out-of-box record 'Approval Record Assigned - RITM' should be activated. If this record is not being used and a custom notification has taken its place, ensure the conditions and events are set appropriately.

The “When to send” Configuration can be setup as follows: 

Event name:  approval.inserted along with the conditions matching Approval for.Task type is Requested item.

The business rule Approval Events (Tasks) must be activated. 

### Related Links

[https://community.servicenow.com/community?id=community\_question&sys\_id=9ff2c9a3db8cf3c0feb1a851ca9619c2](https://community.servicenow.com/community?id=community_question&sys_id=9ff2c9a3db8cf3c0feb1a851ca9619c2)

[Change Request Workflow "Approval - User" activity is not sending notification to approvers so they are not able to approve or reject the request through email](https://support.servicenow.com/kb_view.do?sysparm_article=KB0780313 "Change Request Workflow \"Approval - User\" activity is not sending notification to approvers so they are not able to approve or reject the request through email")
