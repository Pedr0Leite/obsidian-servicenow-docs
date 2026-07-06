---
title: "Email Preview looks different than in Outlook, Gmail or other Mail Application"
aliases:
  - KB0747524
  - Email Preview looks different than in Outlook, Gmail or other Mail Application
tags:
  - servicenow
  - support-kb
  - email
  - notifications
  - html-email
  - email-preview
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0747524
kb_number: KB0747524
last_modified: 2025-05-12
---

## Issue

When designing notification email content, you can use Notification Preview to get an idea of what the email will look like to a recipient.

Note that various email applications and web browsers may render the same HTML code differently.

For simple emails containing some message text and perhaps some inline images (say, a screen shot or a signature image), the differences are typically not discernable. But, as your email's HTML design increases in complexity, you may see more rendering differences between the ServiceNow preview features and the end-user email application.

ServiceNow does not control how third-party web, desktop or mobile mail clients render the HTML of your email. You must ensure your notifications are designed and validated for the mail applications your users typically use.

### Notification Preview and Preview HTML - the Web Browser

The preview is designed to show you what should be a very close approximation of what your recipient will see in their email application. But, ServiceNow cannot always guarantee that your email application will render an email exactly as it is seen in Notification Preview or Preview HTML.

When viewed in Notification Preview or Preview HTML, the email's HTML is rendered in the context of your current session in a **web browser** (e.g., Chrome, Firefox, Safari, Internet Explorer, Edge). Email HTML using common web browser design techniques will naturally look fine in a web browser, but not in some email applications. For instance, your browser and ServiceNow support HTML5, but an older email client may not support it, causing rendering differences.

### Third-Party Email Applications

Emails are usually viewed in individual desktop, web, or mobile **email applications,** not in a standalone web browser. Each third-party email application incorporates its own HTML rendering engine. While it might be based on a popular web browser's rendering engine at its core, it still has its own distinct differences to accommodate the unique needs of that email application.

Examples:

-   A web email application like gmail renders your email by displaying your email HTML inside the gmail web application's HTML. Gmail may make subtle modifications to your email's HTML to allow that.
-   Email applications often deal with CSS differently than a web browser
-   An older mail application does not support particular HTML design features (e.g., HTML5 elements look fine in your browser, but incorrect in a older version of Outlook.)
-   A modern mail application still may have incomplete support for certain HTML features

In addition to HTML rendering differences, there are other general differences when comparing the in-product preview with a third-party email application's view:

-   An email application may have a privacy/security feature to prevent automatically rendering images or accessing external resources, without the recipient first setting a preference in the application
-   An email application does not have an authentication context, so cannot load and display from the instance. (HTML is rendered in a session context when viewed in ServiceNow's preview; this does not exist for the email application.)

### Recommendations

-   As an email "ui developer", familiarize yourself with HTML design constraints unique to email applications
-   Use the Notification Preview feature when designing your email UI for initial testing and validation
-   Test your email notification end-to-end by sending it to a recipient and view it in each of the typical applications your recipients use

### Outside Resources

The below articles are referenced for illustrative purposes and serve to demonstrate that this topic is well-known and there are resources available to handle common situations. (ServiceNow does not endorse any specific company or products referenced in any of these articles, and does not provide support for these external articles.)

-   Handy google search '[HTML differences in email and web browser](https://www.google.com/search?ei=davAXJuHHYTV9AOI3ZjACQ&q=HTML+differences+in+email+and+web+browser "HTML differences in email and web browser")' turns up many articles on this topic.
-   [The Ultimate Guide to CSS](https://www.campaignmonitor.com/css/style-element/style-in-head/ "The Ultimate Guide to CSS") for email shows some differences between mail client support.
-   [Coding your HTML Emails for any Device](https://www.campaignmonitor.com/dev-resources/guides/coding-html-emails/ "Coding your HTML Emails for any Device")
-   [Foundations: Email Coding 101](https://litmus.com/community/learning/13-foundations-email-coding-101 "Foundations: Email Coding 101")

## Related

- [[KB0745430 - HTML Entity names not displaying in Notification previews and Email previews]]
- [[KB0746264 - Emails are not formatted correctly in Outlook or older email applications]]
- [[KB0748592 - HTML Tags are included in email body]]

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0745430 - HTML Entity names not displaying in Notification previews and Email previews|HTML Entity names not displaying in Notification previews and Email previews]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0746264 - Emails are not formatted correctly in Outlook or older email applications|Emails are not formatted correctly in Outlook or older email applications]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0748592 - HTML Tags are included in email body|HTML Tags are included in email body]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0727884 - How to fix HTML tags appearing in sent email notifications|How to fix HTML tags appearing in sent email notifications]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0745172 - Identify the source of emails sent from ServiceNow|Identify the source of emails sent from ServiceNow]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0750361 - How to verify inclusion of Outlook actionable messages in email notifications|How to verify inclusion of Outlook actionable messages in email notifications]]
