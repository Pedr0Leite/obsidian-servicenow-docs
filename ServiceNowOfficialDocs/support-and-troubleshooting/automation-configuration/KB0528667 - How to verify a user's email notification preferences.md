---
title: "How to verify a user's email notification preferences"
aliases:
  - KB0528667
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0528667
kb_number: KB0528667
last_modified: 2026-04-01
---

## How to verify a user's email notification preferences

  

### Issue

 

Troubleshoot missing email notifications by verifying that a user has not disabled them. Users can enable and disable notifications from their profile or change subscription preferences by device.

Admins must verify settings in the instance through the platform UI and not through Service Portal.

### Release

 All supported releases

### Resolution

Before starting, verify that the user is active, not locked out, and has a valid email address.

**To verify email notification preferences for a user:**

1.  Log in to the instance.
2.  Go to **User Administration** > **Users**.
3.  Select the user record to verify.
4.  Verify that the **Notification** field is set to **Enable**.  
    -   If set to **Disabled**, change the value and update the user record.
    -   If notifications were already enabled, verify that a matching notification device is active.

**To see a list of the user's devices:**

1.  From within the User page, under **Related Links**, select **Notification Preferences**.
2.  Enable or disable notifications per device. 

Notifications are sent to the primary email by default, while other devices require specific enablement to receive notifications. See the following table for details.

| Primary Email | Other Devices |
| --- | --- |
| **Enabled** — Send | **Enabled** — Send |
| **Disabled** — Don't Send | **Disabled** — Don't Send |
| **Not Listed** — Send | **Not Listed** — Don't Send |

### Related Links

[Notification preferences on Service Portal](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0688338)
