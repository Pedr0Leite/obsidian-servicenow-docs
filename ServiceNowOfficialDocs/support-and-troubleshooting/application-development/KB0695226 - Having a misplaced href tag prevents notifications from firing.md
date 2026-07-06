---
title: "Having a misplaced href tag prevents notifications from firing"
aliases:
  - KB0695226
tags:
  - servicenow
  - support-kb
  - notifications
  - mail-script
  - email-notifications
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695226
kb_number: KB0695226
last_modified: 2024-04-30
---

## Having a misplaced href tag prevents notifications from firing

  

### Issue

# Symptoms

* * *

A notification containing a mail script does not fire to create an email. The localhost log file shows:

SEVERE \*\*\* ERROR \*\*\* For input string: "mail\_script\_name" 

java.lang.NumberFormatException: For input string: "mail\_script\_name" 

at java.lang.NumberFormatException.forInputString(NumberFormatException.java:65) 

at java.lang.Integer.parseInt(Integer.java:580)

# Release

* * *

Any Release

# Cause

* * *

Looking at the html source for the notification, you can see a href tag added in between the parts of the mail script call. For Example:

$mail\_<a href="script:mail\_script\_name}">script:mail\_script\_name}

When looking at this in the html viewer, you can see parts of the mail script call highlighted as a link but not all.

# Resolution

* * *

Remove the href attribute.

For Example: <p>${mail\_script:mail\_script\_name}</p>

## Related

- [[KB0716520 - Notification emails are not generated when the Message HTML field contains a hyperlink]]
- [[KB0694768 - Email client only supports one email client template per table]]
- [[KB0723602 - Unable to get the non-english value of translated text field or translated html field when using the email template]]

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0716520 - Notification emails are not generated when the Message HTML field contains a hyperlink|Notification emails are not generated when the Message HTML field contains a hyperlink]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0694768 - Email client only supports one email client template per table|Email client only supports one email client template per table]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0712569 - How to setup a SMS Email Notification in ServiceNow|How to setup a SMS Email Notification in ServiceNow]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/notifications/pe-bootstrap-notify/README|pe-bootstrap-notify]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Notifications/Add KB Article Link Dynamic Email Script to Notification/readme|Add KB Article Link Dynamic Email Script to Notification]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Notifications/Conditional Trigger/README|Conditional Trigger]]
