---
title: "Verify that the SMTP Sender schedule job is running"
aliases:
  - KB0523599
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0523599
kb_number: KB0523599
last_modified: 2026-02-23
---

## Verify that the SMTP Sender schedule job is running

  

### Issue

If an email is listed in the **Outbox** for an unusual amount of time (the exact amount of time varies by instance and configuration), there may be an issue with a Simple Mail Transfer Protocol (**SMTP) Sender** scheduled job.

### Facts

**SMTP Sender** scheduled jobs determine when a duplicate email notification is going to be sent. Once an _action_ or _business rule_ is triggered, emails are placed in the Outbox. All emails remain in the **State** of **Ready** until they are processed.

### Release

All

### Resolution

To check if the email is stuck in the Outbox:

1.  Navigate to **System Mailboxes > Outbound > Outbox**.
    
    The Outbox should be empty or contain messages less than a few minutes old.  
      
    ![System outbox with undelivered emails](sys_attachment.do?sys_id=25afebfe93e83690101833527cba1013 "System outbox with undelivered emails")
    
2.  Click **Emails \[Outbox view\]** and choose **Refresh List**.
    
    If the same email messages are listed in the Outbox, verify that the **SMTP Sender** job is running.
    
3.  Verify at least one SMTP Sender job is running. See the procedure below.
    

To verify that the **SMTP** **Sender** scheduled job is running:

1.  Navigate to **System Scheduler > Today's Scheduled Jobs**.
2.  In the **Go to** field, select **Name** and search for **\*SMTP Sender**.
3.  In the corresponding result set, look at the **Next Action** field. When email notifications function properly, the value of this field, which indicates the next time the job runs, is not more than a few minutes from the time you opened the record. 
4.  If it is more than a few minutes, look at the **State** field and take the corresponding action based on these conditions:  
    -   **Error** or **Queued**: If the **State** of the SMTP Sender jobs is set to either of these, select the fields and change them to **Ready**.
    -   **Ready** or **Running**: If the value of the **Next action** field is more than a few minutes from the time you opened the record, open an incident in Hi and include the **Next action** value.
5.  Right-click the form header and choose **Refresh List**.   
    The **Next action** field value should update. If the value is unchanged, open an incident ticket and include the value. 

### Related Links

[Email diagnostics](https://www.servicenow.com/docs/csh?topicname=r_MailDiagnostics.html&version=latest "Email diagnostics")
