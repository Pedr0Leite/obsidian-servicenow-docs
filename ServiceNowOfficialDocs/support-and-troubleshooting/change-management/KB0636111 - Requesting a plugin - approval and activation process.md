---
title: "Requesting a plugin - approval and activation process"
aliases:
  - KB0636111
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0636111
kb_number: KB0636111
last_modified: 2024-04-07
---

## Issue

Requesting a plugin - approval and activation process

Overview

* * *

This article describes the plugin approval and activation process, provides some tips for managing plugin requests, and explains an issue that may occur when activating plugins.

Plugin approval and activation process

* * *

In the various releases of ServiceNow, over 1400 plugins are available. Admin users can activate approximately 700 plugins in their instance without assistance from ServiceNow. However, some plugins do need to be requested. To obtain a plugin from ServiceNow, create a plugin activation request on HI. The request automatically creates a change record that is used for communication until the plugin is activated successfully. 

For plugins requested from ServiceNow, there is a manual, internal approval process that is generally done by ServiceNow employees Monday-Friday, 7:00am-4:00pm (United States Pacific timezone).

After a request is approved, activations are performed on the date scheduled in the plugin activate request at 2 batch activation times:

-   10:00am (United States Pacific timezone)
-   6:00PM (United States Pacific timezone)

#### Tips for managing plugin requests

-   Due to the manual approval and activation process, plugins require a 2 day lead time for review. However, if you need the plugin sooner, update the change record. All communications should be done through the change record.
-   If you need a plugin to be activated at a specific time you have scheduled, or at a specific earlier or later time, update the change record with this information. We will do our best to accommodate the request.
-   If you are updating the change record during the approval hours (listed above), you should receive a response on the same day, most likely within a few hours.
-   If you are updating the change record outside of the approval hours (listed above) and you do not receive a response to your update within a few hours, contact [ServiceNow Customer Support](http://www.servicenow.com/support/contact-support.html "ServiceNow Customer Support") and reference the change record.

Subscription plugin error

* * *

An issue is occurring when activating subscription plugins on non-production and production instances. 

The new Subscription Management application, introduced in the Istanbul release, validates subscriptions. This validation should not occur on non-production instances; it should only validate subscriptions in production.

The error is caused by cloning from production to the non-production instances, prior to Istanbul Patch 6. In those versions, the subscription validation functionality was included in the cloning process and it should have been excluded.

The issue has been resolved in Istanbul Patch 6. To apply the fix, upgrade your production instance to Istanbul Patch 6 or higher and then clone down to your non-production instances to activate the fix for the non-production systems. Upgrading and then cloning enables an admin to activate any plugin they can access in the instance.

If you are not ready to upgrade production to the latest Istanbul or Jakarta release, we can provide an XML export of a fixed script. The script can be applied to the production instance to exclude the subscription validation functionality. After applying the xml script to production, apply the fix to the non-production instances through a clone from the fixed production instance.

#### Managing the error in a non-production instance

In the Istanbul release, an admin may not be able to activate a subscription plugin and receive the following error:

Activation failed for plugin <id> because you need to purchase a subscription to install this plugin

This error should never occur on non-production instances because all plugins in the System Plugins module, on any non-production instance, can be activated by an admin user.

If you are receiving this error message on a non-production instance, it is due to an issue that was fixed in Istanbul Patch 6 and later releases. If your non-production instance was cloned from production prior to that patch level and your non-production instance runs on any version of Istanbul or Jakarta, you will experience the issue.

**If you encounter this error in a non-production instance**

1.  Do not submit a case.
2.  Submit a plugin activation request on HI for each plugin you need by navigating to **Service Catalog > Activate Plugin**. 
3.  Include the following information in the activation request:
    -   note that you are receiving the error message about needing a subscription for the plugin to be activated
    -   let us know, in the CHG, if you would like to have the xml file for the error fix (as a workaround until you are ready to upgrade production)

#### Managing the error in a production instance

 If you are seeing the error when trying to activate a published (admin) plugin in production and you believe that your company has purchased the subscription related to the plugin, follow these steps:

1.  Do not submit a case.
2.  To validate the subscriptions for your company, navigate to **Subscription Management > Subscriptions**.
3.  If the subscription (for example, Performance Analytics) is listed and you are not able to activate any of the content packs listed in the System Plugins, go to the next step.
4.  Submit a plugin activation request on HI for each plugin you need by navigating to **Service Catalog > Activate Plugin**.
5.  In the **Reason/Comments** field, explain that you cannot activate the plugin even though a subscription exists.  
    After submitting your request, it is reviewed, the purchase is validated, and the plugin is activated by our activation team.
