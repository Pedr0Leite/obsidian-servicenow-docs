---
title: "How to customize incident autoclosure"
aliases:
  - KB0552820
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0552820
kb_number: KB0552820
last_modified: 2026-02-23
---

## How to customize incident autoclosure

  

### Issue

Learn how to customize the automatic closure behavior for resolved incidents, including turning autoclosure off, changing the wait period, adjusting the check frequency, and modifying closure behavior.

In the base system, Incident Management automatically closes incidents one day after they are resolved if no updates are made to the incident. This automates the Resolved to Closed state transition. If any field on the record is updated, the one-day counter resets to the last updated timestamp.

**Note**: Major incidents are not part of the default autoclose functionality.

### Release

All supported releases

### Resolution

You can modify the auto-close behavior in several ways. All of the following modifications require the admin role.

-   Turn off auto-closure
-   Change the number of days before a resolved incident is closed
-   Change how frequently the system checks for resolved incidents to close (default is hourly)
-   Set a specific user as the **Updated by** value on the incident record
-   Add other changes to the incident record at the time of closure, such as work notes

#### **Turn off auto-closure**

1.  Go to **System Properties** > **System**.
2.  Locate the property **Number of days (integer) after which Resolved incidents are automatically closed**.
3.  Set the **Value** to 0.

#### **Change the number of days before closure**

1.  Go to **System Properties** > **System**.
2.  Locate the property **Number of days (integer) after which Resolved incidents are automatically closed**.
3.  Set the **Value** to the number of days to wait before closing a resolved incident. For example, to wait one week, set the value to 7.

#### **Change the check frequency**

The Autoclose Incidents scheduled job runs every hour by default. If any incidents have been in the Resolved state longer than the configured auto-close period since the last check, the job closes them.

1.  Go to **System Scheduler** > **Scheduled Jobs** > **Today's Scheduled Jobs**.
2.  Locate the record named **Autoclose Incidents**.
3.  Update the **Repeat time** to change the frequency. To run the job at a specific time each day, change the **Trigger Type** to Daily and set the time.

#### **Set a specific user as Updated by**

You can set a specific user as the **Updated by** value on incidents closed by the auto-close process.

1.  Go to **System Scheduler** > **Scheduled Jobs** \> **Today's Scheduled Jobs**.
2.  Locate the record named **Autoclose Incidents**.
3.  In the **Job content** field, add the following line above the scScriptName: fcRunAs=itil 

Replace itil with a valid user\_id for the user you want recorded as the **Updated by** value. You can set this to any user in your system.

#### **Add other changes at closure**

You can modify the autoclose business rule to make additional changes to the incident record at the time of closure, such as adding a comment documenting the autoclosure.

1.  Go to **System Definition** > **Business Rules**.
2.  Locate the record named **Incident autoclose**.
3.  In the **Advanced** section, edit the **Script** field to add your changes. The commented lines in the script provide an example of adding information to the comments field.

The following image shows an example of adding information in the comments field.

1.  ![In the Advanced section, the script field is displayed.](sys_attachment.do?sys_id=91b5343847db3a502c31b98a436d430b)

**Warning:** If you edit this script, it is excluded from future upgrades.

### **Technical components of incident autoclose**

**Note**: This section contains advanced technical details about the components that make up the autoclose behavior. These options are suggested only for advanced users. 

The autoclose behavior consists of three configuration components: a property, a business rule, and a scheduled job.

#### **Property**

The glide.ui.autoclose.time property determines the number of days after which a silent resolved incident is closed. A silent record is one that has not been updated on any field. Any update resets the auto-closure timer to the last updated timestamp.

This record is located at: /sys\_properties.do?sys\_id=d5c26446c0a8011800cdf450892cec2d

#### **Business rule**

The Incident autoclose business rule contains the code that performs the closure. It queries all incidents in the Resolved state that have not been updated for longer than the configured autoclose period. The business rule also sets the following values:

-   **closed\_by** — Set to the same value as resolved\_by
-   **state** — Set to Closed
-   **Active** — Set to false

This record is located at: /sys\_script.do?sys\_id=d67b8d9ec0a80118008cd8f0f7f92fae

#### **Scheduled job**

The Autoclose Incidents scheduled job calls the business rule every hour to search for silent resolved incidents. The job runs every hour by default and typically completes quickly without significant impact on instance performance. If your instance has a high volume of incidents moving to the Resolved state, you can change the frequency to run less often or once per day.

This record is located at: /sys\_trigger.do?sys\_id=d67e98dac0a8011801393f5054790aa5
