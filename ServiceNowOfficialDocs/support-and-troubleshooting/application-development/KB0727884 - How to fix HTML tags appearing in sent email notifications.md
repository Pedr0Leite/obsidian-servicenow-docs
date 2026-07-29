---
title: "How to fix HTML tags appearing in sent email notifications"
aliases:
  - KB0727884
tags:
  - servicenow
  - support-kb
  - notifications
  - message_html
  - html-email
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727884
kb_number: KB0727884
last_modified: 2025-10-28
---

## How to fix HTML tags appearing in sent email notifications

  

### Issue

When you add HTML content to the message\_text field on a notification record, the outbound emails display HTML tags as literal text instead of rendering them properly. This article describes how to resolve this. The following image is an example of this issue. 

![Example of  outbound emails display HTML tags as literal text instead of rendering them properly](/sys_attachment.do?sys_id=1885d9b247f0fa94c4e1a325126d43b1)

### Release

Madrid Patch 0

### Cause

A notification body consists of two fields:

-   message\_text
-   message\_html

The system treats all characters in the message\_text field as literal text. When you enter HTML markup in this field, it displays as visible tags in the email.

To properly render HTML, place your HTML code in the message\_html field instead.

### Resolution

Place all HTML markup in the Message\_html field, not the Message\_text field. This includes any mail scripts that generate HTML content.

The following image illustrates placing the HTML scripts in the Message\_HTML field. 

![Example of inserting script into the Message HTML field. ](/sys_attachment.do?sys_id=a085d9b247f0fa94c4e1a325126d43b4)

### Related Links

[How to fix unexpected HTML display in email preview tools](https://support.servicenow.com/kb_view.do?sysparm_article=KB0743622 "How to fix unexpected HTML display in email preview tools")

[How to remove formatting from text in email notification message HTML fields](https://support.servicenow.com/kb_view.do?sysparm_article=KB0686053 "How to remove formatting from text in email notification message HTML fields")

## Related

- [[KB0748592 - HTML Tags are included in email body]]
- [[KB0746264 - Emails are not formatted correctly in Outlook or older email applications]]
- [[KB0724449 - Duplicate email notification were sent from the instance when it was not intended]] - other notification/email troubleshooting
- [[KB0743780 - When notification is sent, email is not showing hyperlink for the incident number]] - notification body/display value troubleshooting

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0745430 - HTML Entity names not displaying in Notification previews and Email previews|HTML Entity names not displaying in Notification previews and Email previews]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0746264 - Emails are not formatted correctly in Outlook or older email applications|Emails are not formatted correctly in Outlook or older email applications]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0747524 - Email Preview looks different than in Outlook, Gmail or other Mail Application|Email Preview looks different than in Outlook, Gmail or other Mail Application]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0748592 - HTML Tags are included in email body|HTML Tags are included in email body]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/notifications/pe-bootstrap-notify/README|pe-bootstrap-notify]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Notifications/Add KB Article Link Dynamic Email Script to Notification/readme|Add KB Article Link Dynamic Email Script to Notification]]
