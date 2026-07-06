---
title: "Emails to incidents come in as winmail.dat attachments"
aliases:
  - KB0529478
tags:
  - servicenow
  - support-kb
  - inbound-email
  - tnef
  - winmail-dat
  - attachments
  - exchange
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0529478
kb_number: KB0529478
last_modified: 2026-05-28
---

## Emails to incidents come in as winmail.dat attachments

  

### Issue

##### **Symptom  
**

-   Inbound Email arrives and processes, producing an empty incident record containing an attachment named 'winmail.dat'.
-   Inbound email arrives and when ignored, an attachment named 'winmail.dat' is present on the sys\_email record.
-   Inbound email arrives and some or all expected attachments (such as a screenshot, document, spreadsheet) are not present, but instead an attachment named 'winmail.dat' is present. 

##### **What is 'winmail.dat'?**

Microsoft products (e.g, via Outlook, Exchange, Outlook365) can send email using Microsoft's proprietary Transport Neutral Encapsulation Format (TNEF) format, which is the winmail.dat package. This format might typically be configured for use internally within a company using Microsoft-only mail environment. From Microsoft:

"TNEF, also known as the Transport Neutral Encapsulation Format, Outlook Rich Text Format, or Exchange Rich Text Format, is a Microsoft-specific format for encapsulating MAPI message properties. All versions of Outlook fully support TNEF. Outlook on the web (formerly known as Outlook Web App) translates TNEF into MAPI and displays the formatted messages. Other email clients that don't support TNEF typically display TNEF formatted messages as plain text messages with Winmail.dat or Win.dat attachments."

In this format, the mail message content and attachments normally expected with the MIME email are instead assembled so that all (or most of) the message and attachments are packaged inside a single MIME attachment "winmail.dat". For more information about the TNEF format see Microsoft's [Exchange and Outlook Message Formats](https://docs.microsoft.com/en-us/exchange/mail-flow/content-conversion/content-conversion?view=exchserver-2019#exchange-and-outlook-message-formats "Exchange and Outlook Message Formats") documentation.

The ServiceNow platform supports standard MIME emails, and does not have functionality to parse TNEF. It therefore treats this particular 'winmail.dat' MIME attachment no differently than other attachments, such as a document or spreadsheet.

##### **Can a 'winmail.dat' attachment be created by the instance?**

No. The ServiceNow platform contains no functionality that generates this file as an attachment on an email.

##### **Can a 'winmail.dat' attachment be read and processed by the instance?**

No. The ServiceNow platform contains no functionality that parses the TNEF format.

##### **Does the ServiceNow email infrastructure create 'winmail.dat' files?**

No. The ServiceNow inbound email infrastructure does not generate these files.

### Release

All ServiceNow product families exhibit this behavior.

### Cause

This issue is caused by settings in the sender email environment, either Exchange mail server or Outlook.

### Resolution

##### **ServiceNow Workarounds**

There are no options or workarounds in the ServiceNow platform or in the ServiceNow mail infrastructure to **convert** Microsoft's TNEF into a standard MIME email. ServiceNow recommends you work with your email administrator to configure your Exchange server to not send TNEF-formatted emails to external domains. (Or at least ensure this is configured specifically for your ServiceNow instance email addresses.)

Alternatively you may configure the instance to connect the your own email server. The Exchange mailbox server will present the correct format of the emails to the instance if the instance connects to the Exchange server as a client.

##### **Microsoft Documentation**

**PLEASE NOTE:** The following are examples and are not guaranteed to be appropriate for the latest versions of MicroSoft products , for the most up to date details on the configuration ALWAYS consult the MicroSoft documentation or your email administrator.

Here are two current Microsoft documentation links about this topic that may be of assistance. As Microsoft has myriad mail products and versions, and also uses multiple user-facing names for the TNEF format, ServiceNow cannot guarantee these documentation links and provided information apply to your specific product or version. Therefore, if you have questions about how to configure your specific Exchange or Outlook settings, please work with your email administrator or Microsoft support.

-   [Content Conversion](https://docs.microsoft.com/en-us/exchange/mail-flow/content-conversion/content-conversion?view=exchserver-2019#exchange-and-outlook-message-formats)
-   [TNEF Conversion Options](https://docs.microsoft.com/en-us/exchange/mail-flow/content-conversion/tnef-conversion?view=exchserver-2019)

##### **Example in Microsoft Exchange 2010:**

1.  Log in to your Exchange Server 2010 by opening the Exchange Management Console (EMC).
2.  Expand **Microsoft Exchange On-Premise…**
3.  Expand **Recipient Configuration**.
4.  Select **Mail Contact**.
5.  Find the contact that represents your ServiceNow instance email (e.g., the one that sends emails to <instancename>@service-now.com).
6.  In our example, we will assume the contact is named **Marketing Requests** (yours will be named differently).
7.  Open **Marketing Requests Properties**.
8.  Select the **General** tab.
9.  In the **Use MAPI rich text format** field**,** select **Never** (as shown below).
10.  Click **OK**.

![Marketing Requests Properties](/sys_attachment.do?sys_id=103fb426db0ab450e515c22305961940 "Marketing Requests Properties")

## Related

- [[KB0528852 - Transport Neutral Encapsulation Format (TNEF-encoded, winmail.dat or win.dat) messages aren't processed by the instance]] — deeper dive into TNEF detection and handling
- [[KB0520595 - Inbound Email overview and troubleshooting]] — general inbound email troubleshooting flow
- [[KB0691482 - Inbound emails with attached icons logos signatures images add duplicate repeated attachments in Activity Stream of targ]] — another inbound email attachment artifact issue
