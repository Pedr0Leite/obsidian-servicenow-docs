---
title: "How to enable email receiving in ServiceNow"
aliases:
  - KB0521775
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0521775
kb_number: KB0521775
last_modified: 2026-04-01
---

## How to enable email receiving in ServiceNow

  

### Issue

Resolve email receiving issues when inbound email notifications do not appear in the Inbox or Received folder. This article describes how to verify that the POP3 email properties are configured correctly on the instance.

**Note**: If the mail server is not a ServiceNow server, contact your system administrator to verify that the email message was delivered. 

### Release

All supported releases

### Resolution

To enable email receiving:

1.  Go to **System Properties** > **Email**.
2.  In the Email Properties window, verify that the **Enable email receiving (POP3)** property is marked as **Yes**. This property controls the POP3 mail reader. 
    
    **Note**: This setting applies only if you are using an internal POP3 mail server that also serves as the POP Server.
    
    ![Enable email receiving (POP3) option with Yes or No checkbox](/sys_attachment.do?sys_id=4baea224938c47d45736b25d6cba102b "Enable Email Receiving property")
    
3.  Select **Save**.

After the property is set to **Yes**, queued emails on the mail server are automatically delivered. If the instance still prevents you from receiving emails, open a case with Now Support and provide the Message ID.

### Related Links

[Email properties](https://docs.servicenow.com/csh?topicname=c_EmailProperties.html&version=latest "Email Properties").
