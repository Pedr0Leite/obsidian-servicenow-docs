---
title: "Manage company key contacts and notification lists on Now Support"
aliases:
  - KB0547262
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547262
kb_number: KB0547262
last_modified: 2026-06-23
---

## Manage company key contacts and notification lists on Now Support

  

### Issue

Company contacts are critical for communications with ServiceNow. If you are a customer or partner admin, you are responsible for keeping your company contact information accurate and up-to-date on Now Support. For example, company contacts receive email notifications if there is a mass outage or an issue affecting your company instance. You should specify an alternative, temporary primary support contact in case you are unavailable.

## In this article

-   [Contact roles and communications](#mcetoc_1ffqf04el4j)
-   [Types of notifications](#mcetoc_1gmdl3l166)
-   [Patching Program notifications](#mcetoc_1ffqhgll133)
-   [Notifications and communication lists](#mcetoc_1ffqf04el4n)

* * *

## Contact roles and communications

The following table shows contact roles, their focus areas, and which communications they receive.

<table style="border-collapse: collapse; width: 100%; border-color: #000000; border-style: solid;" border="1" cellpadding="2"><tbody><tr><td style="border-style: solid; border-color: #000000; background-color: #f2f2f2;" colspan="2"><p><span style="color: #ffffff;"><span style="color: #000000;">Contact information is very important to make sure that you receive updates about maintenance window activity, support cases, and any other key information.&nbsp;</span></span></p></td><td style="border-style: none; border-color: #000000; background-color: #379099;" colspan="4"><p><strong><span style="color: #ffffff;">Notification Types&nbsp;</span></strong></p></td><td style="border-style: none; border-color: #000000; background-color: #379099;"><p><strong><span style="color: #ffffff;">&nbsp;</span></strong></p></td></tr><tr><td style="border-style: solid; border-color: #000000; background-color: #379099; text-align: left;"><p style="text-align: center;"><strong><span style="color: #ffffff; font-size: 10pt;">Contact Role &nbsp;</span></strong></p></td><td style="border-style: solid; border-color: #000000; background-color: #379099; text-align: left;"><p style="text-align: center;"><strong><span style="color: #ffffff; font-size: 10pt;">Short Description &nbsp;</span></strong></p></td><td style="border-style: solid; border-color: #000000; background-color: #379099; text-align: center;"><p><strong><span style="color: #ffffff; font-size: 10pt;">Maintenance Windows&nbsp;</span></strong></p></td><td style="border-style: solid; border-color: #000000; background-color: #379099; text-align: center;"><p><strong><span style="color: #ffffff; font-size: 10pt;">Patching/</span></strong></p><p><strong><span style="color: #ffffff; font-size: 10pt;">EOL&nbsp;</span></strong></p></td><td style="border-style: solid; border-color: #000000; background-color: #379099; text-align: center;"><p><strong><span style="color: #ffffff; font-size: 10pt;">Security&nbsp;</span></strong></p></td><td style="border-style: solid; border-color: #000000; background-color: #379099; text-align: center;"><p><strong><span style="color: #ffffff; font-size: 10pt;">Advisory &nbsp;</span></strong><br><strong><span style="color: #ffffff; font-size: 10pt;">(non-technical)&nbsp;</span></strong></p></td><td style="border-style: solid; border-color: #000000; background-color: #379099; text-align: center;"><p><strong><span style="color: #ffffff; font-size: 10pt;">&nbsp;Cases&nbsp;</span></strong><strong><span style="color: #ffffff; font-size: 10pt;">Opened</span></strong></p><p><strong><span style="color: #ffffff; font-size: 10pt;">&amp; Updated</span></strong></p></td></tr><tr><td style="border-style: solid; border-color: #000000; background-color: #f2f2f2;"><p>Primary Customer Admin&nbsp;</p></td><td style="border-style: solid; border-color: #000000; background-color: #f2f2f2;"><p>Each account requires a Primary Customer Admin to review and approve Now Support user account requests. Admins have the highest access privileges in Now Support and can activate plugins, administer an upgrade, and more. &nbsp;</p></td><td style="border-style: solid; border-color: #000000; background-color: #d1f4f7; text-align: center;"><p><span style="font-size: 24pt;">✓</span></p></td><td style="border-style: solid; border-color: #000000; background-color: #d1f4f7; text-align: center;"><p><span style="font-size: 24pt;">✓</span>&nbsp;</p></td><td style="border-style: solid; border-color: #000000; background-color: #d1f4f7; text-align: center;"><p><span style="font-size: 24pt;">✓</span>&nbsp;</p></td><td style="border-style: solid; border-color: #000000; background-color: #d1f4f7; text-align: center;"><p><span style="font-size: 24pt;">✓</span>&nbsp;</p></td><td style="border-style: solid; border-color: #000000; background-color: #d1f4f7; text-align: center;"><p><span style="font-size: 24pt;">&nbsp;</span></p></td></tr><tr><td style="border-style: solid; border-color: #000000; background-color: #f2f2f2;"><p>Primary Support &nbsp;</p></td><td style="border-style: solid; border-color: #000000; background-color: #f2f2f2;"><p>Oversees your ServiceNow instances. Manages accounts, monitors system performance, support cases, and verifies your services run as expected. &nbsp;</p></td><td style="border-style: solid; border-color: #000000; background-color: #d1f4f7; text-align: center;"><p><span style="font-size: 24pt;">✓</span></p></td><td style="border-style: solid; border-color: #000000; background-color: #d1f4f7; text-align: center;"><p><span style="font-size: 24pt;">✓</span></p></td><td style="border-style: solid; border-color: #000000; background-color: #d1f4f7; text-align: center;"><p><span style="font-size: 24pt;">✓</span></p></td><td style="border-style: solid; border-color: #000000; background-color: #d1f4f7; text-align: center;"><p><span style="font-size: 24pt;">✓</span>&nbsp;</p></td><td style="border-style: solid; border-color: #000000; background-color: #d1f4f7; text-align: center;"><p><span style="font-size: 24pt;">&nbsp;</span></p></td></tr><tr><td style="border-style: solid; border-color: #000000; background-color: #f2f2f2;"><p>Secondary Support &nbsp;</p></td><td style="border-style: solid; border-color: #000000; background-color: #f2f2f2;"><p>Is a backup for the Primary Support contact and assists with instance oversight.   &nbsp;</p></td><td style="border-style: solid; border-color: #000000; background-color: #d1f4f7; text-align: center;"><p><span style="font-size: 24pt;">✓</span></p></td><td style="border-style: solid; border-color: #000000; background-color: #d1f4f7; text-align: center;"><p><span style="font-size: 24pt;">✓</span></p></td><td style="border-style: solid; border-color: #000000; background-color: #d1f4f7; text-align: center;"><p><span style="font-size: 24pt;">✓</span></p></td><td style="border-style: solid; border-color: #000000; background-color: #d1f4f7; text-align: center;"><p><span style="font-size: 24pt;">✓</span></p></td><td style="border-style: solid; border-color: #000000; background-color: #d1f4f7; text-align: center;"><p><span style="font-size: 24pt;">&nbsp;</span></p></td></tr><tr><td style="border-style: solid; border-color: #000000; background-color: #f2f2f2;"><p>Primary Technical &nbsp;</p></td><td style="border-style: solid; border-color: #000000; background-color: #f2f2f2;"><p>Provides technical solutions to satisfy business requirements. Owns most configuration work in the platform. Designs, develops, and configures ServiceNow apps and services. &nbsp;</p></td><td style="border-style: solid; border-color: #000000; background-color: #d1f4f7; text-align: center;"><p><span style="font-size: 24pt;">✓</span></p></td><td style="border-style: solid; border-color: #000000; background-color: #d1f4f7; text-align: center;"><p><span style="font-size: 24pt;">✓</span></p></td><td style="border-style: solid; border-color: #000000; background-color: #d1f4f7; text-align: center;"><p><span style="font-size: 24pt;">✓</span></p></td><td style="border-style: solid; border-color: #000000; text-align: center; background-color: #d1f4f7;"><p>&nbsp;</p></td><td style="border-style: solid; border-color: #000000; text-align: center; background-color: #d1f4f7;"><p>&nbsp;</p></td></tr><tr><td style="border-style: solid; border-color: #000000; background-color: #f2f2f2;"><p>Secondary Technical &nbsp;</p></td><td style="border-style: solid; border-color: #000000; background-color: #f2f2f2;"><p>Backup to Primary Technical contact or a Product Owner who is accountable for a particular process and owns the vision, experience, and functionality of the tools within the process. &nbsp;</p></td><td style="border-style: solid; border-color: #000000; background-color: #d1f4f7; text-align: center;"><p><span style="font-size: 24pt;">✓</span></p></td><td style="border-style: solid; border-color: #000000; background-color: #d1f4f7; text-align: center;"><p><span style="font-size: 24pt;">✓</span></p></td><td style="border-style: solid; border-color: #000000; background-color: #d1f4f7; text-align: center;"><p><span style="font-size: 24pt;">✓</span></p></td><td style="border-style: solid; border-color: #000000; text-align: center; background-color: #d1f4f7;"><p>&nbsp;</p></td><td style="border-style: solid; border-color: #000000; text-align: center; background-color: #d1f4f7;"><p>&nbsp;</p></td></tr><tr><td style="border-style: solid; border-color: #000000; background-color: #f2f2f2;"><p>Security Contact &nbsp;</p></td><td style="border-style: solid; border-color: #000000; background-color: #f2f2f2;"><p>Proactively monitors instance security and security patches. Seeks to understand the why and how of security protocols and implementation. Stays current on potential vulnerabilities to ensure optimal instance health and compliance.</p></td><td style="border-style: solid; border-color: #000000; text-align: center; background-color: #d1f4f7;"><p>&nbsp;</p></td><td style="border-style: solid; border-color: #000000; background-color: #d1f4f7; text-align: center;"><p><span style="font-size: 24pt;">✓</span></p></td><td style="border-style: solid; border-color: #000000; background-color: #d1f4f7; text-align: center;"><p><span style="font-size: 24pt;">✓</span></p></td><td style="border-style: solid; border-color: #000000; text-align: center; background-color: #d1f4f7;"><p>&nbsp;</p></td><td style="border-style: solid; border-color: #000000; text-align: center; background-color: #d1f4f7;"><p>&nbsp;</p></td></tr><tr><td style="border-style: solid; border-color: #000000; background-color: #f2f2f2;"><p>Primary Business &nbsp;</p></td><td style="border-style: solid; border-color: #000000; background-color: #f2f2f2;"><p>Develops strategic plan and roadmap for ServiceNow services. Owns and oversees ServiceNow instances from a business perspective. Analyzes trends to make decisions. &nbsp;</p></td><td style="border-style: solid; border-color: #000000; text-align: center; background-color: #d1f4f7;"><p>&nbsp;</p></td><td style="border-style: solid; border-color: #000000; background-color: #d1f4f7; text-align: center;"><p><span style="font-size: 24pt;">✓</span></p><div><p>&nbsp;</p></div></td><td style="border-style: solid; border-color: #000000; text-align: center; background-color: #d1f4f7;"><p>&nbsp;</p></td><td style="border-style: solid; border-color: #000000; text-align: center; background-color: #d1f4f7;"><p>&nbsp;</p></td><td style="border-style: solid; border-color: #000000; text-align: center; background-color: #d1f4f7;"><p>&nbsp;</p></td></tr><tr><td style="border-style: solid; border-color: #000000; background-color: #f2f2f2;"><p>Secondary Business &nbsp;</p></td><td style="border-style: solid; border-color: #000000; background-color: #f2f2f2;"><p>Implementation specialist, analyst, or business process owner who supports the Primary Business contact in analyzing, designing, and implementing processes. &nbsp;</p></td><td style="border-style: solid; border-color: #000000; text-align: center; background-color: #d1f4f7;"><p>&nbsp;</p></td><td style="border-style: solid; border-color: #000000; background-color: #d1f4f7; text-align: center;"><p><span style="font-size: 24pt;">✓</span>&nbsp;</p></td><td style="border-style: solid; border-color: #000000; text-align: center; background-color: #d1f4f7;"><p>&nbsp;</p></td><td style="border-style: solid; border-color: #000000; text-align: center; background-color: #d1f4f7;"><p>&nbsp;</p></td><td style="border-style: solid; border-color: #000000; text-align: center; background-color: #d1f4f7;"><p>&nbsp;</p></td></tr><tr><td style="border-style: solid; border-color: #000000; background-color: #f2f2f2;" colspan="2"><p>Patching and Upgrades list&nbsp;</p></td><td style="border-style: solid; border-color: #000000; background-color: #d1f4f7; text-align: center;"><p><span style="font-size: 24pt;">✓</span></p></td><td style="border-style: solid; border-color: #000000; background-color: #d1f4f7; text-align: center;"><p><span style="font-size: 24pt;">✓</span></p></td><td style="border-style: solid; border-color: #000000; background-color: #d1f4f7; text-align: center;"><p><span style="font-size: 24pt;">✓</span></p></td><td style="border-style: solid; border-color: #000000; background-color: #d1f4f7; text-align: center;"><p><span style="font-size: 24pt;">✓</span></p></td><td style="border-style: solid; border-color: #000000; background-color: #d1f4f7; text-align: center;"><p><span style="font-size: 24pt;">&nbsp;</span></p></td></tr><tr><td style="border-style: solid; border-color: #000000; background-color: #f2f2f2;" colspan="2"><p>Maintenance and Advisories list&nbsp;</p></td><td style="border-style: solid; border-color: #000000; background-color: #d1f4f7; text-align: center;"><p><span style="font-size: 24pt;">✓</span></p></td><td style="border-style: solid; border-color: #000000; background-color: #d1f4f7; text-align: center;"><p><span style="font-size: 24pt;">✓</span></p></td><td style="border-style: solid; border-color: #000000; background-color: #d1f4f7; text-align: center;"><p><span style="font-size: 24pt;">✓</span></p></td><td style="border-style: solid; border-color: #000000; background-color: #d1f4f7; text-align: center;"><p>&nbsp;</p></td><td style="border-style: solid; border-color: #000000; background-color: #d1f4f7; text-align: center;"><span style="font-size: 24pt;">✓</span></td></tr></tbody></table>

  
To manage your company key contacts, see [Manage company key contacts in Now Support User Management tool.](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1285089 "Manage company key contacts in Now Support User Management tool")

## Types of notifications

-   **Maintenance Windows:** Activities based on ServiceNow infrastructure. For example, server or data center OS patching (not related to the patching program for version releases) and SSL certificate updates.
-   **Patching and End of Life (EOL):** Family versions and new release activities that affect customer instances. For example, monthly patching, quarterly upgrades. 
-   **Security:** Cloud-security related issues 
-   **Advisory (non-technical):** Now Support, webinars, and general announcements 

You can also designate users to receive notifications and communications about the [Patching Program](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696901).

## Patching Program notifications

The Patching Program schedules patches in intervals throughout the year so your instance has the latest security, performance, and availability of hot fixes and patches. The following roles receive notifications as part of the Patching Program:

-   Primary Business Contact
-   Primary Customer Admin
-   Primary Support Contact
-   Secondary Support Contact
-   Primary Technical Contact
-   Secondary Technical Contact
-   Support Account Manager
-   Patching and Upgrades List
-   Maintenance and Advisories List
-   Security Contact
-   Secondary Business Contact
-   Solution Consultant
-   Territory Contact

**Note:** This list can change from program to program, as these fields are selectable and are not hard-coded. Also, if you do not have a valid user assigned for a specific role, there is no notification.

## Maintenance and Advisories And Patching and Upgrades lists

Users added to the **Maintenance and Advisories list** receive notifications for auto-upgrades, upgrade notifications, all cases opened, and cases updated with comments

Users added to the **Patching and Upgrades** **list** receive notifications for patches, auto-upgrades, and upgrade notifications. If the Patching and Upgrades list is left blank, the messages are sent to the users identified in the business contact and support contact fields.  
  
**Important:** Users added to the Maintenance and Advisories or Patching and Upgrades lists are not automatically added to the watchlist for patching changes raised prior to them being added to these lists.

Sys\_id details appear in the Maintenance and Advisories or Patching and Upgrades lists lists when ServiceNow employee details are added to the lists. This is by design in Now Support as customers are not authorized to see the name behind the sys\_id

### Release

All releases  

### Resolution

### Add and remove users from Maintenance and Advisories or Patching and Upgrades lists

1.  Go to [Now Support](/now). 
2.  Scroll to the **Maintenance Center** link under the 'Upcoming Maintenance' module.  
    4\. In the **Search people** field, add user names or email addresses.

The user is added to list.

## Validate profile information

Periodically, Now Support asks you to validate that your company information is correct. 

1.  Go to [Now Support](https://support.servicenow.com/now "Now Support")
2.  Verify that your profile information is correct and current.
3.  To confirm, select **This info is up to date**.

## Additional details for key contact sync

On Now Support, each key contact can be mapped to only one user. For example, there can only be one Primary Technical Contact.

One Now Support user can be mapped to multiple key contacts. For example, the same user can be mapped to Primary Technical Contact and Primary Customer Admin.
