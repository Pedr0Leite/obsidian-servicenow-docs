---
title: "How to check if emails are stuck in the Inbox"
aliases:
  - KB0523576
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0523576
kb_number: KB0523576
last_modified: 2026-05-26
---

## How to check if emails are stuck in the Inbox

  

### Issue

Verify whether inbound emails are stuck in the Inbox and confirm that the scheduled job responsible for processing email records is running. Sent and received emails can be seen in the System Mailboxes application, which includes the Inbox, Outbox, and Sent mailboxes. Every time a message is read, an email.read event is created. The scheduled job (sys\_trigger) then processes the email record.

### Release

  All supported releases 

### Resolution

 To verify if emails are stuck in the Inbox:

1.  Go to System Mailboxes > Inbox.
2.  Check the age of the emails in the Inbox. Under normal conditions, the Inbox should be empty or contain only emails that are less than one minute old.  
      
    ![Sent Emails Create today email log](/sys_attachment.do?sys_id=a07ca44f9773765c24a7739c1253af62 "Sent Emails Create today email log")  
      
    
3.  If emails remain in the Inbox longer than expected, verify that the scheduled job is running.

### Related Links

[Email was Received, but is Stuck in the Inbox](https://www.youtube.com/watch?v=OR_UtHrMqTE "Email was Received, but is Stuck in the Inbox")
