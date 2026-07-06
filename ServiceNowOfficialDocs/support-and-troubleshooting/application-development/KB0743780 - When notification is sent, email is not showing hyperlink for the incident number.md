---
title: "When notification is sent, email is not showing hyperlink for the  incident number "
aliases:
  - KB0743780
tags:
  - servicenow
  - support-kb
  - notifications
  - dictionary
  - display-value
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0743780
kb_number: KB0743780
last_modified: 2024-04-26
---

## When notification is sent, email is not showing hyperlink for the incident number

  

### Issue

When notification is sent, email is not showing hyperlink of a incident number

### Cause

OOB script displays hyperlink based on Display Value. Display value was false for "Number" column on incident table.

### Resolution

Right click on "Number" field in incident table > Configure dictionary > Check the "Display" checkbox for 'Number' column to fix the issue.

## Related

- [[KB0727617 - Access referenced fields in a notification record against the Approval table]] - notification body configuration
- [[KB0725194 - Approval emails are not being generated for requested items]] - notification troubleshooting

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/notifications/pe-bootstrap-notify/README|pe-bootstrap-notify]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Notifications/Add KB Article Link Dynamic Email Script to Notification/readme|Add KB Article Link Dynamic Email Script to Notification]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Notifications/Conditional Trigger/README|Conditional Trigger]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Notifications/Modern Email Layout Designs/Readme|Modern Email Layout Designs]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Notifications/Notify Users on Specific Date/README|Notify Users on Specific Date]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0715790 - Users see an error message Record doesn't exist or ACL restricts the record retrieval when making changes to their Notif|Users see an error message \"Record doesn't exist or ACL restricts the record retrieval\" when making changes to their Notifications settings]]
