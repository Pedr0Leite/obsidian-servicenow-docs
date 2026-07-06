---
title: "Access referenced fields in a notification record against the Approval table"
aliases:
  - KB0727617
tags:
  - servicenow
  - support-kb
  - notifications
  - dot-walking
  - sysapproval_approver
  - approvals
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727617
kb_number: KB0727617
last_modified: 2024-04-07
---

## Access referenced fields in a notification record against the Approval table

  

### Issue

Access referenced fields in a notification record against the Approval table

  

#   

### Resolution

# Procedure

* * *

In a notification record against the Approval \[sysapproval\_approver\] table, you can dot-walk to fields on the associated record through the Approving \[document\_id\] field, which is a reference to the associated record.

For example, if the associated record is a Request \[sc\_request\] record, you can click the Approving field, whose system name is document\_id, and then dot-walk to the sc\_request field you want to use in the notification record:

  

![](/sys_attachment.do?sys_id=94aeb0a2db0ab450e515c22305961925)

Example of dot-walking to a field named delivery\_address on the referenced table:

Delivery address: ${document\_id.delivery\_address}

## Related

- [[KB0725194 - Approval emails are not being generated for requested items]] - approval notification setup
- [[KB0812521 - How to troubleshoot the Update Approval Request inbound action]] - the inbound side of approval processing
- [[KB0785021 - Approval request reply email does not approve the associated record]] - approval reply-email troubleshooting
- [[send-notification-action]] - Flow Designer notification action reference

