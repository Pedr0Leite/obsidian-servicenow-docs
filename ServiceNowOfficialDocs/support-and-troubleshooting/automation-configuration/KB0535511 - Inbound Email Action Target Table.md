---
title: "Inbound Email Action Target Table"
aliases:
  - KB0535511
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0535511
kb_number: KB0535511
last_modified: 2026-05-29
---

## Inbound Email Action Target Table

  

### Issue

An email sent to your ServiceNow instance may not match up with a record that you expect it to. The Inbound Email Action's target table, along with the presence of a watermark or a record number in the email, affects whether your Inbound Email Action will match against this email.

For details on configuring your inbound action's target table and other conditions, as well as on how ServiceNow searches the email for watermarks or records, see [Inbound Email Actions](https://docs.servicenow.com/csh?topicname=c_InboundEmailActions.html&version=latest "Inbound Email Actions").

### Release

Any

### Cause

When a target table is incorrect, the following symptoms may occur:

-   Email sent to your ServiceNow instance does not create a new incident or other record.
-   Reply email sent to your ServiceNow instance does not update the expected incident or other record
-   Email log shows _Skipping <Inbound Action>, email is a reply, and the record it matches is not in the Inbound Email Action's table_
-   Email not processed by any inbound action and remains in the **Ready** state
-   General problems with Inbound Email Actions.

### Resolution

ServiceNow logs information about the record table or watermark that may help you diagnose a problem related to target table mismatches. For more information, see [Ensuring Email is not Ignored](/kb_view.do?sysparm_article=KB0535493&ni.dependent.topic=kb_knowledge.category&sysparm_category=&sysparm_ck=3f86964a80846d44c14db3a5dc083e0756112837994a040f1326fc9365f8c44698241b46&sysparm_nameofstack=&sysparm_product=&sysparm_search=KB0535493&sysparm_topic= "Ensuring Email is not Ignored").

To change the Inbound Email Action's target table:

1.  Open the **Inbound Email Action** record.
2.  Chose a table from the **Target Table** menu.

**Watermarks**

When a watermark is present in a reply email, ServiceNow looks up the record associated with the watermark to find its table. In order for your inbound action to match the email, the record's table must match the Inbound Email Action's target table.

For instance, if an email contains _Ref:MSG000001_, and it is associated with incident record INT1234567, then your Inbound Email Action's target table must be _incident_ in order for it to match against this email.

**Record Numbers**

When there is no watermark, but a record number is present in a reply email's subject, ServiceNow looks up the record to find its table. In order for your inbound action to match the email, the record's table must match the Inbound Email Action's target table.

For instance, if the email subject is _Re: CHG0000001_, then your Inbound Email Action's target table must be _change_ in order for it to match against this email.

  
The base system inbound action **Update Approval Request** is defined to match for records that belong to the \[sysapprover\_approval\] table. It matches only if the record found through the watermark or record number belongs to this table.  

If the watermark cannot be found in the reply email, then the system looks for a record number. If the subject were "RE: Please approve CHG123456", then the located record belongs to the Change table. Therefore, the message logged for this inbound action would be:

_Skipping 'Update Approval Request', email is a reply, and the record it matches is not in the Inbound Email Action's table_

This demonstrates the importance of watermarks in matching, particularly if record numbers from other tables are present in the email.

### Related Links

[Inbound Email Action does not run on the email record with the error - Skipping 'Name\_Of\_Inbound\_Action', a suitable GlideRecord not found](https://support.servicenow.com/kb_view.do?sysparm_article=KB0759187 "Inbound Email Action does not run on the email record with the error - Skipping 'Name_Of_Inbound_Action', a suitable GlideRecord not found")
