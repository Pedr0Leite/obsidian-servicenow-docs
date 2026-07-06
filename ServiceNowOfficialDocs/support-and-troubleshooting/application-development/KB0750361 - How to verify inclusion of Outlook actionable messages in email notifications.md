---
title: "How to verify inclusion of Outlook actionable messages in email notifications"
aliases:
  - KB0750361
  - How to verify inclusion of Outlook actionable messages in email notifications
tags:
  - servicenow
  - support-kb
  - notifications
  - outlook-actionable-messages
  - email
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0750361
kb_number: KB0750361
last_modified: 2025-10-28
---

## How to verify inclusion of Outlook actionable messages in email notifications

  

### Issue

An email notification is sent that uses the Outlook Actionable Messages plugin (com.sn\_ms\_oam) along with an email script in a notification template. The email script specifies "include\_approval\_actionable":  ${mail\_script:include\_approval\_actionable}, but the email body does not show the standard approve or reject links.  This article explains how to verify that the embedded approval request is included correctly. 

### Release

All supported releases

### Cause

 According to Microsoft documentation, when sending actionable messages by email:

-   The actionable message card must be wrapped in a <script> tag.
-   This <script> tag is inserted into the <head> of the email HTML body.
-   The email body must be in HTML format to support the <script> tag with JSON content.

### Resolution

To verify that Outlook Actionable Messages are included in your email notification:

1.  In the HTML body of the notification sys\_email record, check for <script> and </script> tags.
2.  Verify that a JSON payload exists between these tags.

If your notification contains <script> tags and the JSON content, the Outlook Actionable Messages are successfully included in the email notification.

Example of the script content:

<script>{   
"$schema":"http://adaptivecards.io/schemas/adaptive-card.json",   
"type":"AdaptiveCard",   
"version":"1.0",   
"hideOriginalBody":true,   
"expectedActors":\["user@company.com"\],   
"style":"emphasis",   
"originator":"1b0e10fd-f0aa-4b15-9afe-080d0ff-1b932",   
"body":\[{"type":"Container","items":\[{"type":"TextBlock","text":".....  
  
.....  
  
{"type":"Action.OpenUrl","title":"View Approval Request","url":"https://<instance\_name>.service-now.com/sysapproval\_approver.do?sys\_id=39763fdedbad3300e906d12c5e1a1b52"}\]}\]}   
</script>

**Note:** 

The Outlook Actionable Messages (OAM) feature is not supported in all Microsoft mail products and versions. To verify whether your version of Outlook supports OAM, refer to the Microsoft documentation, [Actionable messages in Outlook and Office 365 Groups](https://docs.microsoft.com/en-us/outlook/actionable-messages/)

If the Actionable Message doesn't appear when you open the email, but the script content is included in the email notification, the most likely causes are:

-   Outlook actionable messages is not configured on the client side.
-   Your client version doesn't support Outlook actionable messages.

### Related Links

[How to fix missing actionable messages in Outlook email notifications](https://support.servicenow.com/kb_view.do?sysparm_article=KB0829137 " How to fix missing actionable messages in Outlook email notifications")

[Get started with actionable messages in Office 365](https://docs.microsoft.com/en-us/outlook/actionable-messages/send-via-email) 

[Test and validate Outlook Actionable Message content using Microsoft Designer | Adaptive Cards](https://adaptivecards.io/designer/)

## Related

- [[KB0750584 - Troubleshoot notification issues with cmn_notif_device and cmn_notif_message tables]]
- [[KB0815869 - Outlook Actionable Message 401 error on endpoint]]
- [[KB0783202 - Outlook Actionable Messages - Signed Cards]]
