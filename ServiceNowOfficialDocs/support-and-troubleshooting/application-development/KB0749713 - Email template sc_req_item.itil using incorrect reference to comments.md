---
title: "Email template sc_req_item.itil using incorrect reference to comments"
aliases:
  - KB0749713
  - Email template sc_req_item.itil using incorrect reference to comments
tags:
  - servicenow
  - support-kb
  - email-templates
  - notifications
  - request-management
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749713
kb_number: KB0749713
last_modified: 2025-05-20
---

## Email template sc\_req\_item.itil using incorrect reference to comments

  

### Issue

Any email notification that uses **sc\_req\_item.itil** email template will not display the comments.

### Release

All releases up to New York

### Cause

This is happening because in OOB **sc\_req\_item.itil** email template comments are denoted by **${u\_comments\_and\_work\_notes}** in the email body.

### Resolution

The comments in the email template can be modified to **${comments\_and\_work\_notes}** and used.

This has been fixed in New York release.

## Related

- [[KB0750584 - Troubleshoot notification issues with cmn_notif_device and cmn_notif_message tables]]
- [[KB0750040 - Exporting Journal Fields to an excel file]]

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0723602 - Unable to get the non-english value of translated text field or translated html field when using the email template|Unable to get the non-english value of translated text field or translated html field when using the email template]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/notifications/pe-bootstrap-notify/README|pe-bootstrap-notify]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Notifications/Add KB Article Link Dynamic Email Script to Notification/readme|Add KB Article Link Dynamic Email Script to Notification]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Notifications/Conditional Trigger/README|Conditional Trigger]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Notifications/Modern Email Layout Designs/Readme|Modern Email Layout Designs]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Notifications/Notify Users on Specific Date/README|Notify Users on Specific Date]]
