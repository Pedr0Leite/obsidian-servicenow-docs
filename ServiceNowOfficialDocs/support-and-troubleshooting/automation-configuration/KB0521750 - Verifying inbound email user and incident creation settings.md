---
title: "Verifying inbound email user and incident creation settings"
aliases:
  - KB0521750
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0521750
kb_number: KB0521750
last_modified: 2026-06-11
---

## Verifying inbound email user and incident creation settings

  

### Issue

Verifying Inbound Email User and Incident Creation Settings | Inbound Email

### Symptoms

-   Emails are sent to an instance or test instance, but no incidents are created.
-   The instance is not creating users from incoming emails.
-   When users from the _X_ domain send emails to the instance and create an incident, the incident shows a caller of **Guest** instead of the user.
-   Incidents are created by unknown users. 
-   Forwarded emails create or update incidents or other emails with specific subjects.
-   Out-of-Office replies are filling up incidents with unwanted emails.

### Release

### Cause

-   Email receiving property is disabled.
-   The **Automatically create users from incoming email** property is disabled.
-   A list of trusted domains is not defined.
-   The **Ignore Inbound Email** settings are not defined.

### Resolution

**Inbound Email Actions** allow users to log or update incidents via email. The Inbound Email Actions function parses the email and responds using a script. More refined Inbound Email Actions can create incident tickets with more data, thus saving the incident management team valuable time. For more information, refer to [Inbound Email Actions](https://docs.servicenow.com/csh?topicname=c_InboundEmailActions.html&version=latest "Inbound Email Actions").

To [enable automatic user creation](https://www.servicenow.com/docs/r/platform-administration/t_EnablingAutomaticUserCreation.html "enable automatic user creation") from inbound email:

1.  Navigate to All -> System Properties -> Email Properties.
2.  Select the check box for Automatically create users for incoming email from trusted domains.
3.  Enter the list of trusted domains in Trusted domains for creating users from incoming emails.
    
      
    
    Note:
    
    -   The glide.user.trusted\_domain property prevents user creation if the sender is not from a trusted domain. However, the system may still process inbound actions for emails that are received from the domain. To have the system ignore these emails, set up a system address filter. For more information on setting up system address filters, see [System address filters](https://www.servicenow.com/docs/r/UrSRFFKWBbfQBgoRlt~ltw/MeBgnFXuWMvybwi7bGntSg "Prevent your system from communicating with untrusted domains and email addresses."). You can also prevent untrusted users from triggering inbound actions by locking out the guest user.
    -   The glide.user.trusted\_domain property does not accept wildcarded domains or values such as:
        -   \*.edu
        -   \*.net
        -   .edu
        -   .net
    
    4\. Click Save.  
     

To configure the incident creation settings:

1.  Confirm that the instance has an active Inbound Email account (POP3/IMAP) and is properly configured to receive email from a such server. 
2.  Confirm that "Email Receiving" is enabled under "Email Properties"
3.  Ensure instance default "Inbound Email Actions" for the INCIDENT table are active, if not activate such or create new ones. [Create Inbound Email Actions](https://www.servicenow.com/docs/r/platform-administration/t_CreatingAnInboundEmailAction.html "Create Inbound Email Actions").
4.  Configure the instance to ignore certain emails and prevent them from creating incidents. For more information, refer to [Email Filters](https://www.servicenow.com/docs/r/platform-administration/c_EmailFilters.html "Documentation: Email Filters").

For details on other email properties that are used to configure email processing in ServiceNow, refer to [Email Properties](https://docs.servicenow.com/csh?topicname=c_EmailProperties.html&version=latest "Email Properties") in the ServiceNow product documentation.

[ServiceNow video tutorials](https://www.youtube.com/channel/UCQjE37R-Y4DTq7kUWPO83Wg "ServiceNow video tutorials") are a great way to help find solutions. These video tutorials guide you, step-by-step, to a solution and provide common troubleshooting methods. This tutorial covers common issues, their causes, and the required steps to resolve them.
