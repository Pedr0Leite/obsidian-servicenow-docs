---
title: "Notify Users on Specific Date"
aliases:
  - Notify Users on Specific Date
tags:
  - servicenow-dev-program
  - code-snippet
  - notify-users-on-specific-date
  - notifications
---

This configuration will send an email on the specified date.

This will use a date field to trigger email notifications.

Business Rule will run on Insert/Update to trigger the event. As soon as the event is triggered, the notification will be in the queue to be triggered on the specified date field.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/notifications/pe-bootstrap-notify/README|pe-bootstrap-notify]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Notifications/Add KB Article Link Dynamic Email Script to Notification/readme|Add KB Article Link Dynamic Email Script to Notification]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Notifications/Conditional Trigger/README|Conditional Trigger]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Notifications/Modern Email Layout Designs/Readme|Modern Email Layout Designs]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0715790 - Users see an error message Record doesn't exist or ACL restricts the record retrieval when making changes to their Notif|Users see an error message \"Record doesn't exist or ACL restricts the record retrieval\" when making changes to their Notifications settings]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0717149 - Error message Record doesn't exist or ACL restricts the record retrieval appearing when ITIL users try to disallow notif|Error message \"Record doesn't exist or ACL restricts the record retrieval\" appearing when ITIL users try to disallow notifications]]
