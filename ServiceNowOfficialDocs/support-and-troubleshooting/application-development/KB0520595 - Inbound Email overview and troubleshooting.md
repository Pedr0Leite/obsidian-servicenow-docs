---
title: "Inbound Email overview and troubleshooting"
aliases:
  - KB0520595
tags:
  - servicenow
  - support-kb
  - inbound-email
  - email
  - pop3
  - troubleshooting
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0520595
kb_number: KB0520595
last_modified: 2026-04-13
---

## Inbound Email overview and troubleshooting

  

### Issue

**Inbound email** automatically routes inbound email inquiries to the right place both quickly and efficiently. All inbound emails are placed in the Inbox mailbox until they are processed. Once cleared, they are moved to the Received (if processed) or Junk (if ignored by your Inbound Email Actions) mailbox. If the ServiceNow system is restarted for any reason, such as during a system upgrade, all inbound mail remains in the external mail server until ServiceNow can request delivery.

### Release

  All supported releases

### Resolution

 ![Inbound email troubleshooting diagram](/sys_attachment.do?sys_id=15665aa0939887d0e7eef35d6cba1068 "Inbound email troubleshooting diagram")

### Procedure

If emails are not received or processed as expected, it is important to identify the root cause. The following steps help understand the inbound email process as well as guide you through troubleshooting common issues. 

1.  A message is sent from a customer's email such as Microsoft Outlook, Hotmail, or Gmail.
2.  Email is delivered to a mail server.
3.  The ServiceNow instance polls the email server every two minutes to download sent messages.  
    -   [Verify if the instance is configured to receive emails](/kb?id=kb_article_view&sysparm_article=KB0521775 "Verify if the instance is configured to receive emails")
4.  [Confirm the scheduled job (POP Reader) is running](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0524472 "Confirm the scheduled job (POP Reader) is running").  
    **Note**: Polling time is configurable and may vary by instance.
5.  Emails are received in the ServiceNow instance and processed.  
    -   [Emails are stuck in the inbox](/kb?id=kb_article_view&sysparm_article=KB0523576 "Emails are stuck in the inbox")
    -   [Validate the inbound email action is performed](/kb?id=kb_article_view&sysparm_article=KB0523577 "Validate the inbound email action is performed")
6.  [Confirm the email is processed by the instance](/kb?id=kb_article_view&sysparm_article=KB0523578 "Confirm the email is processed by the instance").

### Related Links

### Video Tutorials

If you are having issues using the inbound email functionality in ServiceNow, our video tutorials are a great way to help find solutions. These video tutorials guide you step by step to a solution and provide common troubleshooting methods. This tutorial covers common issues, their causes, and the required steps to resolve them. They range from basic to more advanced topics, and are best watched in the order that they are listed.

You can view an overview to the inbound email troubleshooting below or follow a link below to jump to a different section of the serie. The steps can generally be applied to other email issues as they often have common root causes.

<table><tbody><tr><td width="30"><img title="Video Tutorial" src="/VideoTutorial_Icon.pngx" alt="" width="25" height="25" align="bottom"></td><td><strong><a title="Troubleshooting Inbound Email Part 1: Introduction" href="https://youtu.be/KX0b-MrTDpY?list=PLCOmiTb5WX3o-8pchYsG4DuyvrDXjbgjd" target="_blank" rel="noopener noreferrer">Troubleshooting Inbound Email Part 1: Introduction</a>&nbsp;</strong><span style="color: rgb(100, 100, 100);"><em>[2:17]</em></span></td></tr><tr valign="middle"><td><img title="Video Tutorial" src="/VideoTutorial_Icon.pngx" alt="" width="25" height="25" align="bottom"></td><td><strong><a title="Part 2: Instance Does Not Receive Email" href="https://youtu.be/ND08pDqtdgc?list=PLCOmiTb5WX3o-8pchYsG4DuyvrDXjbgjd" target="_blank" rel="noopener noreferrer">Part 2: Instance Does Not Receive Email</a>&nbsp;&nbsp;</strong><span style="color: rgb(100, 100, 100);"><em>[4:25]</em></span></td></tr><tr><td><img title="Video Tutorial" src="/VideoTutorial_Icon.pngx" alt="" width="25" height="25" align="bottom"></td><td><strong><a title="Part 3: Inbound Email Action Not Processed" href="https://youtu.be/6LKYfq1FsdA?list=PLCOmiTb5WX3o-8pchYsG4DuyvrDXjbgjd" target="_blank" rel="noopener noreferrer">Part 3: Inbound Email Action Not Processed</a>&nbsp;&nbsp;</strong><em><span style="color: rgb(100, 100, 100);">[4:16]</span></em></td></tr><tr><td><img title="Video Tutorial" src="/VideoTutorial_Icon.pngx" alt="" width="25" height="25" align="bottom"></td><td><strong><a title="Part 4: Email Events in System Logs" href="https://youtu.be/RTT1c3WfA_0?list=PLCOmiTb5WX3o-8pchYsG4DuyvrDXjbgjd" target="_blank" rel="noopener noreferrer">Part 4: Email Events in System Logs</a>&nbsp;&nbsp;</strong><span style="color: rgb(100, 100, 100);"><em>[3:22]</em></span></td></tr></tbody></table>

## Related

- [[KB0529413 - Troubleshooting duplicate emails generated by the instance]] — troubleshooting a specific inbound/outbound email issue
- [[KB0529478 - Emails to incidents come in as winmail.dat attachments]] — a common inbound email processing symptom
- [[KB0691482 - Inbound emails with attached icons logos signatures images add duplicate repeated attachments in Activity Stream of targ]] — another inbound email attachment troubleshooting scenario
- [[c_InboundEmailActions]] — official docs on Inbound Email Actions

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0745172 - Identify the source of emails sent from ServiceNow|Identify the source of emails sent from ServiceNow]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0539112 - Troubleshooting SAML or SSO issues in ServiceNow|Troubleshooting SAML or SSO issues in ServiceNow]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0529413 - Troubleshooting duplicate emails generated by the instance|Troubleshooting duplicate emails generated by the instance]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0529478 - Emails to incidents come in as winmail.dat attachments|Emails to incidents come in as winmail.dat attachments]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0691482 - Inbound emails with attached icons logos signatures images add duplicate repeated attachments in Activity Stream of targ|Inbound emails with attached icons / logos / signatures images add duplicate repeated attachments in Activity Stream of target record]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0693349 - Inbound emails received and processed display broken attached images in preview HTML body and in target record activity |Inbound emails received and processed display broken attached images in preview HTML body and in target record activity stream notes]]
