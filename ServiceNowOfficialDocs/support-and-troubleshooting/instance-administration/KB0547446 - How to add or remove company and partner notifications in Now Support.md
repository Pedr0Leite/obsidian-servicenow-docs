---
title: "How to add or remove company and partner notifications in Now Support"
aliases:
  - KB0547446
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547446
kb_number: KB0547446
last_modified: 2025-08-26
---

## How to add or remove company and partner notifications in Now Support

  

### Issue

This article details how administrators can add or remove company users and partners from notifications in HI.

### Company notifications

On the Company record, you can edit the **Communication** and **Notification list** fields:

-   Users added to the **Communication** field receive messages about maintenance windows, upgrades, and patches. If the **Communication** field is left blank, the messages are sent to the users identified in the _business contact_ and _support contact_ fields. 
-   Users added to the **Notification list** field are included on all email notifications sent to the company.  

To remove or add users to the **Communication** or **Notification list** field:

1.  Do one of the following: 
    -   Navigate to **Self-Service > Administration > Manage Company Contacts**.   
    -   Navigate to **User Administration > Company**. 
2.  In the **Communication** or **Notification** **list** field, click the lock icon.
3.  Add one or multiple user names. 
4.  Click the lock icon again to secure the field. 
5.  Click **Update**.

### Partner notifications  

ServiceNow partners are notified about changes that occur for their own ServiceNow instance and instances of associated customers.

In addition, partners receive auto-upgrade notifications, which are different from the normal Cases and Change notifications. These are special notifications that are sent to primary/secondary Support/Technical contacts in the parent chain.

To request the partner no longer receive these types of notifications, you can send an email to the partner deployment team at [partnerdeploy@servicenow.com](mailto:partnerdeploy@servicenow.com) to remove them from your company's record (**Partner** and **Parent** field).

### Resources

-   HI Notifications Resources
-   [Troubleshooting Email Notifications](https://hi.service-now.com/kb_view.do?sysparm_article=KB0535129 "Troubleshooting Email Notifications")
-   [Notifications on HI](https://hi.service-now.com/kb_view.do?sysparm_article=KB0547254 "Notifications on HI")
-   [Managing Company Contacts](https://hi.service-now.com/kb_view.do?sysparm_article=KB0547262 "Managing Company Contacts")
-   [Determining if notifications exceed max size limit in HI](https://hi.service-now.com/kb_view.do?sysparm_article=KB0547452 "Determining if update notifications exceed max size limit in HI")

### Release

### Resolution
