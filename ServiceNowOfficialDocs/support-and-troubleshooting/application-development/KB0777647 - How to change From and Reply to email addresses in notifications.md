---
title: "How to change From and Reply to email addresses in notifications"
aliases:
  - KB0777647
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0777647
kb_number: KB0777647
last_modified: 2025-10-24
---

## How to change From and Reply to email addresses in notifications

  

### Issue

You can customize the **From** and **Reply to** email addresses in notifications to display your company's email domain instead of the default ServiceNow domain. For example, changing from [MyInstance@service-now.com](mailto:MyInstance@service-now.com) to [ServiceDesk@mycompany.com](mailto:ServiceDesk@mycompany.com). This article explains how to make this change.

### Release

All supported releases  

### Resolution

The notification form contains **From** and **Reply to** fields that accept any valid email address.

Follow these steps to change the fields:

1.  Open the notification where you want to display your custom email address.
2.  Go to the **What it will contain** tab, and locate the **From** field.
    -   If you don't see the **From** field, at the bottom of the page under **Related Links**, select **Advanced View**. This display the From field and additional options.
3.  In the **From** field, enter your friendly email address in this format: Service Desk [ServiceDesk@mycompany.com](mailto:ServiceDesk@mycompany.com)
4.  Save the notification and test it.

For more information, see [Create an email notification](https://docs.servicenow.com/csh?topicname=t_CreateANotification.html&version=latest "Create an email notification")

### Related Links

Examples from Community posts:

[Changing the From field in email notification](https://www.servicenow.com/community/developer-forum/changing-the-quot-from-quot-in-email-notification/m-p/1581370) 

[Defining the From email field on email notifications](https://www.servicenow.com/community/hrsd-articles/defining-quot-from-quot-email-field-on-email-notifications/ta-p/2313183#:~:text=Navigate%20to%20System%20Notification%20%3E%20Email,Set%20needs%20to%20be%20selected%29)
