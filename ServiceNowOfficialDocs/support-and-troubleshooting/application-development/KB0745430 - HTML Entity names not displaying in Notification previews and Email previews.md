---
title: "HTML Entity names not displaying in Notification previews and Email previews"
aliases:
  - KB0745430
  - HTML Entity names not displaying in Notification previews and Email previews
tags:
  - servicenow
  - support-kb
  - email
  - notifications
  - html-email
  - email-preview
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0745430
kb_number: KB0745430
last_modified: 2024-04-07
---

## HTML Entity names not displaying in Notification previews and Email previews

  

### Issue

Using HTML symbol entities such as &minus, &excl, &check in the notification scripts (email scripts) would not display the symbol in Notification previews and Email previews.

### Release

Any Release

### Cause

Service Now doesn't preview the HTML symbol entities in notifications and emails, but when the email is delivered to the customer, their mail clients (OWA on MacOS and Windows, Outlook on MacOS and Windows, MacMail, Thunderbird, Outlook on iPad, Outlook on Android) all display the actual symbol for all HTML entities. It's only the Notification preview and the Email log preview within ServiceNow that has an issue rendering the actual symbol.

### Resolution

The issue can be resolved by using hex codes in the mail script instead of the symbol entities. For example, the following hex codes are used for &minus, &check, &excl symbols. ! = !  − = −  ✓ = ✓  You can look up codes/entities here: http://www.amp-what.com/unicode/search/

## Related

- [[KB0747524 - Email Preview looks different than in Outlook, Gmail or other Mail Application]]
- [[KB0746264 - Emails are not formatted correctly in Outlook or older email applications]]
- [[KB0748592 - HTML Tags are included in email body]]

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0747524 - Email Preview looks different than in Outlook, Gmail or other Mail Application|Email Preview looks different than in Outlook, Gmail or other Mail Application]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0746264 - Emails are not formatted correctly in Outlook or older email applications|Emails are not formatted correctly in Outlook or older email applications]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0748592 - HTML Tags are included in email body|HTML Tags are included in email body]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0727884 - How to fix HTML tags appearing in sent email notifications|How to fix HTML tags appearing in sent email notifications]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0745172 - Identify the source of emails sent from ServiceNow|Identify the source of emails sent from ServiceNow]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0750361 - How to verify inclusion of Outlook actionable messages in email notifications|How to verify inclusion of Outlook actionable messages in email notifications]]
