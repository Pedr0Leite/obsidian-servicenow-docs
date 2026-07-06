---
title: "Emails are not formatted correctly in Outlook or older email applications"
aliases:
  - KB0746264
  - Emails are not formatted correctly in Outlook or older email applications
tags:
  - servicenow
  - support-kb
  - email
  - notifications
  - html-email
  - outlook
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0746264
kb_number: KB0746264
last_modified: 2025-06-26
---

## Emails are not formatted correctly in Outlook or older email applications

  

### Issue

When a user receives the email notification, the table or HTML format is gone. Although the preview seems fine, the email client does not show all the .css styles including:

-   Tables and cells background
-   Font colors
-   Padding, borders, and margins not as designed in the notification

Following is an example of an email received on an older version of Outlook (Outlook 2010) with broken styles:

![Styles that are not shown in the browser](sys_attachment.do?sys_id=56087b3f478aa650b6d8aa25126d4315 "Styles that are not shown in the browser") 

### Cause

Old email clients such as Outlook 2010 do not render the <style> elements properly and seem to require inline styling.

### Resolution

You should update to a current version of your Microsoft Outlook application on either Windows or Mac. Older versions seem to work on very old engines equivalent to Internet Explorer 5, which only work with inline embedded styles.  

Following is an example of how the mentioned table should look like with the configured styles from the notification:

![Example of a table without broken style with background colour visible as configured in the notification](sys_attachment.do?sys_id=92087b3f478aa650b6d8aa25126d4318 "Example of a table without broken style with background colour visible as configured in the notification")

Embedded styles are included in a `<style>` block in the `<head>` of the file. Inline styles are attached to an HTML element using the style attribute. Instead of including <style></style> code, you should use inline styles in the elements such as <td style='background-color:black'></td> 

**Note**: Microsoft Outlook and other email clients are not a ServiceNow Product. If you have any issue regarding your email client, contact your vendor or internal IT support.

### Related Links

For additional information and references for email client rendering differences, see the knowledge article, [Email preview looks different than in Outlook, Gmail, or other mail application](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0747524)

## Related

- [[KB0747524 - Email Preview looks different than in Outlook, Gmail or other Mail Application]]
- [[KB0745430 - HTML Entity names not displaying in Notification previews and Email previews]]
- [[KB0748592 - HTML Tags are included in email body]]
- [[KB0727884 - How to fix HTML tags appearing in sent email notifications]]
