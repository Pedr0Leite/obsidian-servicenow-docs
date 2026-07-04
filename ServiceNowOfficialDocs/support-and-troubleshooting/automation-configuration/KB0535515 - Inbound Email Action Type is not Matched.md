---
title: "Inbound Email Action Type is not Matched"
aliases:
  - KB0535515
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0535515
kb_number: KB0535515
last_modified: 2025-07-02
---

## Inbound Email Action Type is not Matched

  

### Issue

An email sent to your ServiceNow instance may not match your Inbound Email Action because the email is a **New**, **Reply**, or **Forward**.

Unexpected matching behavior is often due to misunderstanding the way ServiceNow classifies an email into **New**, **Reply**, or **Forward** types. For more information, see [Matching Incoming Email to an Inbound Action Type](https://docs.servicenow.com/csh?topicname=r_InboundActionTypeCriteria.html&version=latest "Matching Incoming Email to an Inbound Action Type") in the product documentation.

For general information on configuring your inbound action's type and other conditions, see [Inbound Email Actions](https://docs.servicenow.com/csh?topicname=c_InboundEmailActions.html&version=latest "Inbound Email Actions").

### Symptoms

When the Inbound Action's type is incorrect, the following symptoms may occur:

-   Email sent to your ServiceNow instance does not create a new incident or any other record.
-   Reply email sent to your ServiceNow instance does not update the expected incident or any other record.
-   Email is not processed by any inbound action and remains in the **Ready** state.
-   The wrong Inbound Email Action is triggered.
-   The email watermark appears to be ignored.
-   **Forward** and **Reply** inbound actions are not working.
-   General problems with Inbound Email Actions.

### Release

All

### Resolution

### Troubleshooting

1.  Open the email record.
2.  Right-click the form header to change the view to **Inbox**.
3.  Review the related log entries. These identify a reason an Inbound Action was skipped. 

### Troubleshooting Reply Inbound Actions

As shown in the article in the overview, an email is classified as a reply only if it matches multiple criteria. If your inbound action of type **Reply** is not matching on an email you expect it to, it is possible your ServiceNow instance has actually classifiied the email as **New** or **Forward** because other **Reply** conditions do not exist in the email. To diagnose, check the following:

1.  Open the email record in the **Inbox** view and review the log entries.
2.  Check that the email subject's reply prefix is one of those listed in the glide property, glide.email.reply\_subject\_prefix.
3.  If the email has a watermark (for example, _Ref:MSG000001_), check that it exists and refers to a record that exists in the same table as your Inbound Action's target table.
4.  If the email has a record number in the subject, check that it exists and is in the same table as your Inbound Action's target table.
