---
title: "Emails Are Not Being Delivered to the ServiceNow Instance via a POP3 or IMAP Microsoft Exchange Email Account"
aliases:
  - KB0688478
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0688478
kb_number: KB0688478
last_modified: 2026-04-16
---

## Emails Are Not Being Delivered to the ServiceNow Instance via a POP3 or IMAP Microsoft Exchange Email Account

  

### Issue

You have configured a POP3 or IMAP email account on the instance that uses a Microsoft Exchange Server, Server = outlook.office365.com in the email account record.

By observing the Exchange Server email backlog, it is noticed that emails are not being read by the instance even though the email account is active and the connection test passes on the instance.  As a result, the email backlog on the Exchange Server continues to grow larger.

The way the email reader on the instance works (reading in emails using pop3 or IMAP protocols) is that the instance reads 20 emails (by default or a different number as defined in the system property com.glide.email.max\_read) at a cycle.  Once those emails are read into the instance it sends a delete command to the email server to delete those read emails from the email server, then the next 20 are read and deletes are sent for those and so on until all of the emails are processed.

If the delete does not work on the email server the instance will keep reading the same 20 emails over and over again.

To debug the issue set the glide.pop3.debug or glide.imap.debug (depending on if the account uses pop3 or imap protocol) to true.

With glide.pop3.debug or glide.imap.debug system properties turned on - see the email (identified by the Message-ID) get deleted when it is read in the wrapper\_<date>.log :

2023-11-10 00:01:13 (609) worker.7 worker.7 txid=8f0891e32984 DEBUG: Date: Fri, 10 Nov 2023 00:01:13 -0800 (PST)  
2023-11-10 00:01:13 (609) worker.7 worker.7 txid=8f0891e32984 DEBUG: From: instance@service-now.com  
2023-11-10 00:01:13 (609) worker.7 worker.7 txid=8f0891e32984 DEBUG: Reply-To:  <instance@service-now.com>  
2023-11-10 00:01:13 (609) worker.7 worker.7 txid=8f0891e32984 DEBUG: To: _recipient_  
2023-11-10 00:01:13 (609) worker.7 worker.7 txid=8f0891e32984 DEBUG: Message-ID: <123@app123.ytz3.service-now.com>  
2023-11-10 00:01:13 (609) worker.7 worker.7 txid=8f0891e32984 DEBUG: Subject: Very important email

...

...

...

2023-11-10 00:01:13 (751) worker.7 worker.7 txid=8f0891e32984 DEBUG: .  
2023-11-10 00:01:13 (834) worker.7 worker.7 txid=8f0891e32984 DEBUG: 250 2.0.0 Ok: queued as B62B22031E40  
2023-11-10 00:01:13 (834) worker.7 worker.7 txid=8f0891e32984 DEBUG: SMTP: message successfully delivered to mail server  
2023-11-10 00:01:13 (859) worker.7 worker.7 txid=8f0891e32984 \[AMB\] AMBQueue Published amb message, sys\_id: 070891e3871a359083d08409cebb352d   
2023-11-10 00:01:13 (861) worker.7 worker.7 txid=8f0891e32984 Sending took: 326ms  
2023-11-10 00:01:13 (875) worker.7 worker.7 txid=8f0891e32984 Releasing chunk took: 13ms  
2023-11-10 00:01:13 (875) worker.7 worker.7 txid=8f0891e32984 DEBUG: NOOP  
2023-11-10 00:01:13 (876) worker.7 worker.7 txid=8f0891e32984 DEBUG: 250 2.0.0 Ok

2023-11-10 00:01:13 (875) worker.7 worker.7 txid=8f0891e32984 DEBUG: DELE 1  
2023-11-10 00:01:13 (876) worker.7 worker.7 txid=8f0891e32984 DEBUG: 250 2.0.0 Ok

The message is deleted with the DELE 1 command and there is an acknowledgment with the 250 2.0.0 OK response from the email server, but in reality, the email is not deleted from the Microsoft Exchange email server itself.

So when the email reader runs again it downloads the same email that is already read and processed, the following will be seen in the system node log (again with glide.pop3.debug or glide.imap.debug system properties turned on) indicating that an email with the same Message-ID is already on the instance:

2018-06-01 09:51:29 (695) worker.3 worker.3 Message UID='123456' Message-ID='<SN50102MB309B2AB554843DE444A9620@SM44354.prod.sn..com>' was previously read and will be ignored.

In Portuguese: 

2018-06-01 09:51:29 (695) worker.3 worker.3 Message UID='123456' Message-ID='<SN50102MB309B2AB554843DE444A9620@SM44354.prod.sn..com>' foi lida anteriormente (sys\_id do e-mail='fdfdfgdfgfgdasedadeewdwed') e será ignorada

If you look on the instance for the sys\_email records you will find an email already exists on the instance with the Message-ID='<SN50102MB309B2AB554843DE444A9620@SM44354.prod.sn..com>'

### Release

This applies to any ServiceNow release.

### Cause

The failure to delete the message from the Microsoft email server may be due to the email account being on "Litigation Hold" or "Retention Hold" which in itself is not stopping the deletes from happening on the email server, but while the account is on "Litigation Hold" or "Retention Hold" there can only be 100GB of deleted emails allowed for the account.  If this 100GB threshold has been reached while on "Litigation Hold" or "Retention Hold" the delete commands sent by the ServiceNow instance will not be honored by the Microsoft email server resulting in this issue.

Another reason may be that the mailbox user has not set up an archive to move emails there automatically.

A third cause of this issue that has been seen is where a customer had a _Deleted Items_ sub-folder off the main inbox (the inbox that the Email Reader was retrieving emails from), and their mail admin had manually started a long-running delete process on that sub-folder. Their _Deleted Items_ sub-folder had had tens of thousands of emails deleted from it, and it appeared that the fact that this process was still running was preventing deletions being effective on the parent inbox. See _Alternative/Workaround Solution_ below.

Even though you see the positive +OKs from the Microsoft email server for the delete commands (DELE) sent by the instance in the wrapper\_<date>.log, the emails are not actually getting deleted from the Microsoft email server.

### Resolution

**NOTE:** This issue _cannot_ be fixed on the ServiceNow side.

Please consult the knowledge documents below provided by Microsoft support related to "Litigation Hold / Retention Hold" and setting up archiving. If these documents do not resolve the issue, please contact [Microsoft support](https://www.microsoft.com/en-us/microsoft-365/support) for further assistance:

[Increase the Recoverable Items quota for mailboxes on hold](https://support.office.com/en-us/article/increase-the-recoverable-items-quota-for-mailboxes-on-hold-a8bdcbdd-9298-462f-b889-df26037a990c)

[Place a mailbox on Litigation Hold](https://technet.microsoft.com/en-us/library/dn743673%28v=exchg.160%29.aspx)

[Delete items in the Recoverable Items folder of cloud-based mailboxes on hold](https://support.office.com/en-us/article/Delete-items-in-the-Recoverable-Items-folder-of-cloud-based-mailboxes-on-hold-Admin-Help-a85e1c87-a48e-4715-bfa9-d5275cde67b0?ui=en-US&rs=en-US&ad=US)

[YouTube: How to enable online archiving for Office 365](https://www.youtube.com/watch?v=8Rar2WJc6Ro)

**Alternative/Workaround Solutions**

(1) A workaround that might help in some circumstances is to rename the mailbox and create a new one with the original name. For example renaming the mailbox support@<customer.com> to support2@<customer.com>, and then re-creating a brand-new mailbox support@<customer.com> with the same password as before. This should also mean that no changes are required on the ServiceNow side (not even in Email Accounts).

This worked in a situation where a long-running delete on a sub-folder of the original mailbox ([support@<customer.com>](mailto:support@\<customer.com\>)) was preventing deletes from being effective. This may not work where the cause of the issue is _Litigation Hold or "Retention Hold"_

(2) Create and set the system property com.glide.email.max\_read to a larger value than 20, say 50 or 100 or 500.  This will allow more emails to be read into the instance.  However, this will not resolve the issue since unread emails will continue to build up until the new limit for com.glide.email.max\_read is reached again, when this happens email reading will be stopped again.  Once the issue with the account is resolved please delete the com.glide.email.max\_read property or set it back to the default value of 20.
