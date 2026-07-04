---
title: "Configure test email addresses, journal entries, and time zone format for outbound email"
aliases:
  - KB0521751
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0521751
kb_number: KB0521751
last_modified: 2025-08-28
---

## Configure test email addresses, journal entries, and time zone format for outbound email

  

### Issue

This knowledge article addresses the following issues:

-   While testing email notifications, unwanted emails are sent unintentionally.
-   Email notifications do not show all of the activity log.
-   When an email is sent, the current time zone is not applied to the date and time.

### Release

All supported releases.

### Cause

-   There is no test user email address where all emails are sent.
-   The number of journal entries is not defined.
-   The time zone property is disabled.

### Resolution

Administrators can control the number of journal entry notifications that are sent, set up a test email address to receive messages during testing, and add the time zone values to sent emails. There are three types of journal fields: **journal**, **journal\_list**, and **journal\_input**. They each behave differently. 

All times are stored in the platform in _Universal Coordinated Time_. They are displayed globally based on the system time zone, but are displayed to users in their local time zone, according to user preferences. The notification system uses the **System time zone** for its date and time stamp rather than the time zone of any recipient. 

To configure email properties for testing and general formatting:

1.  1.  Go to **System Properties > Email**.
    2.  Verify that the following properties are set correctly.  
          
        
        <table class="internalTable" style="width: 726.364px;" width="85%"><tbody><tr class="sphr"><td align="left" valign="top" width="25%"><strong>Field</strong></td><td align="left" valign="top" width="75%"><strong>Description</strong></td></tr><tr class="sp"><td>Number of journal entries included in the email notifications.</td><td>Define the number of entries from a journal field (such as&nbsp;<strong>Additional comments</strong>&nbsp;and&nbsp;<strong>Work notes</strong>) included in email notifications. A value of -1 includes all journal entries.</td></tr><tr class="sp"><td>Email address to which all emails will be sent.</td><td>Enter a test email address to which the instance will send all email messages. This property prevents emails from being sent to real users during testing.<p><strong>Note</strong>:&nbsp;Typically used in non-production instances for testing purposes.</p></td></tr><tr class="sp"><td>Append the time zone to all dates and times in outbound emails.</td><td><p>The instance appends the system time zone to&nbsp;<strong>date</strong>&nbsp;or&nbsp;<strong>date/time</strong>&nbsp;values in outbound emails. For example,&nbsp;<strong>2010-07-02 04:01:14 PST</strong>.</p></td></tr></tbody></table>
        
          
          
        
    3.  Select **Save**.

### Related Links

For more information, see the product documentation:

-   [Using Journal Fields](https://docs.servicenow.com/csh?topicname=r_JournalFields.html&version=latest "Using Journal Fields"). 
-   [Using Time Zones](https://docs.servicenow.com/csh?topicname=r_TimeZones.html&version=latest "Using Time Zones")

For details on other properties that are used to configure email processing in ServiceNow, see [Email Properties](https://docs.servicenow.com/csh?topicname=c_EmailProperties.html&version=latest "Email Properties").
